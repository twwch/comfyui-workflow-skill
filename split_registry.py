#!/usr/bin/env python3
"""Split node-registry.md into per-category files for on-demand loading.

Creates:
  references/nodes/index.md          — Category index with file pointers
  references/nodes/01-loaders.md     — Loaders section
  references/nodes/02-conditioning.md — Conditioning section
  ... etc
"""

import re, os

SRC = os.path.join(os.path.dirname(__file__), "references", "node-registry.md")
OUT_DIR = os.path.join(os.path.dirname(__file__), "references", "nodes")

# Category slug mapping (section number → filename)
SLUG_MAP = {
    1: "loaders",
    2: "conditioning",
    3: "sampling",
    4: "latent",
    5: "image",
    6: "controlnet",
    7: "video-wan",
    8: "video-io",
    9: "flux",
    10: "sdxl",
    11: "sd3",
    12: "hunyuan-video",
    13: "upscale",
    14: "post-processing",
    15: "custom-samplers",
    16: "mask",
    17: "compositing",
    18: "model-advanced",
    19: "model-merging",
    20: "model-patches",
    21: "audio",
    22: "ltxv",
    23: "stable-cascade",
    24: "stable-3d",
    25: "cosmos",
    26: "mochi",
    27: "hidream",
    28: "lumina2",
    29: "pixart",
    30: "chroma-radiance",
    31: "hunyuan-3d",
    32: "3d",
    33: "kandinsky",
    34: "qwen-omnigen",
    35: "string",
    36: "primitive",
    37: "logic-utility",
    38: "text-generation",
    39: "object-detection",
    40: "training",
    41: "dataset",
    42: "debug-misc",
}


def split():
    with open(SRC, "r", encoding="utf-8") as f:
        content = f.read()

    # Split by ## N. Title pattern
    sections = re.split(r"(?=^## \d+\.)", content, flags=re.MULTILINE)

    # First section is the header (before ## 1.)
    header = sections[0].strip()

    # Also handle the additions file appended at the end
    # (node-registry-additions.md was concatenated, starts with "# Additional...")
    additions_start = content.find("# Additional ComfyUI Node Definitions")
    additions_content = ""
    if additions_start > 0:
        additions_content = content[additions_start:]

    files_written = []
    index_entries = []

    for section in sections[1:]:
        # Extract section number and title
        match = re.match(r"^## (\d+)\.\s*(.*?)$", section, re.MULTILINE)
        if not match:
            continue
        num = int(match.group(1))
        title = match.group(2).strip()

        slug = SLUG_MAP.get(num, f"section-{num}")
        filename = f"{num:02d}-{slug}.md"

        # Count nodes in this section (### NodeName patterns)
        nodes = re.findall(r"^### (\w+)", section, re.MULTILINE)

        # Write section file
        filepath = os.path.join(OUT_DIR, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(section.strip() + "\n")
        files_written.append(filename)

        index_entries.append({
            "num": num,
            "title": title,
            "filename": filename,
            "nodes": nodes,
            "count": len(nodes),
        })

    # Handle additions (if present as separate content)
    if additions_content:
        add_filename = "99-additions.md"
        filepath = os.path.join(OUT_DIR, add_filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(additions_content.strip() + "\n")
        files_written.append(add_filename)

        add_nodes = re.findall(r"^## (\w+)", additions_content, re.MULTILINE)
        # Filter out section headers
        add_nodes = [n for n in add_nodes if not n[0].isdigit()]
        index_entries.append({
            "num": 99,
            "title": "Additional Nodes (audio, 3D, LTXV, etc.)",
            "filename": add_filename,
            "nodes": add_nodes,
            "count": len(add_nodes),
        })

    # Write index
    index_path = os.path.join(OUT_DIR, "index.md")
    with open(index_path, "w", encoding="utf-8") as f:
        f.write("# ComfyUI Node Registry — Index\n\n")
        f.write("**Usage:** Read only the category file you need, not the entire registry.\n\n")
        f.write(f"Total: {sum(e['count'] for e in index_entries)} nodes across {len(index_entries)} categories.\n\n")
        f.write("| # | Category | File | Nodes | Key Node Types |\n")
        f.write("|---|----------|------|-------|----------------|\n")
        for e in index_entries:
            key_nodes = ", ".join(e["nodes"][:5])
            if len(e["nodes"]) > 5:
                key_nodes += f", ... (+{len(e['nodes'])-5})"
            f.write(f"| {e['num']} | {e['title']} | `nodes/{e['filename']}` | {e['count']} | {key_nodes} |\n")

        f.write("\n## Quick Lookup\n\n")
        f.write("Common nodes and which file to read:\n\n")
        f.write("| Need | Read |\n")
        f.write("|------|------|\n")
        f.write("| CheckpointLoaderSimple, UNETLoader, VAELoader, CLIPLoader, LoraLoader | `nodes/01-loaders.md` |\n")
        f.write("| CLIPTextEncode, CLIPTextEncodeFlux, CLIPTextEncodeSD3 | `nodes/02-conditioning.md` |\n")
        f.write("| KSampler, KSamplerAdvanced | `nodes/03-sampling.md` |\n")
        f.write("| EmptyLatentImage, VAEDecode, VAEEncode | `nodes/04-latent.md` |\n")
        f.write("| SaveImage, LoadImage, ImageScale | `nodes/05-image.md` |\n")
        f.write("| ControlNetLoader, ControlNetApplyAdvanced | `nodes/06-controlnet.md` |\n")
        f.write("| WanImageToVideo, WanCameraImageToVideo, WanFirstLastFrameToVideo | `nodes/07-video-wan.md` |\n")
        f.write("| CLIPTextEncodeFlux, BasicGuider, SamplerCustomAdvanced | `nodes/09-flux.md` |\n")
        f.write("| BasicScheduler, KSamplerSelect, RandomNoise | `nodes/15-custom-samplers.md` |\n")
        f.write("| EmptyLTXVLatentVideo, LTXVImgToVideo | `nodes/22-ltxv.md` |\n")
        f.write("| EmptyCosmosLatentVideo, CosmosImageToVideoLatent | `nodes/25-cosmos.md` |\n")
        f.write("| StableAudio, EmptyLatentAudio, VAEDecodeAudio | `nodes/21-audio.md` |\n")
        f.write("| Hunyuan3Dv2Conditioning, VAEDecodeHunyuan3D, SaveGLB | `nodes/31-hunyuan-3d.md` |\n")

    print(f"Split into {len(files_written)} files + index.md")
    print(f"Total nodes indexed: {sum(e['count'] for e in index_entries)}")
    for e in index_entries:
        print(f"  {e['filename']:35s} {e['count']:3d} nodes")


if __name__ == "__main__":
    split()
