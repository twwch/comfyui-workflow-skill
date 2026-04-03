# ComfyUI Workflow Skill

> Generate ready-to-use ComfyUI workflow JSON files through natural language conversation.

**No API costs. No backend needed. Just describe what you want → get a valid workflow JSON → import into ComfyUI.**

## What is this?

A skill (for Claude Code, Codex, Cursor, and other AI coding agents) that generates ComfyUI workflow JSON files through conversation. Instead of manually connecting nodes in ComfyUI's node editor, just describe what you want in plain language.

## Features

- **34 built-in templates** covering all mainstream models and tasks
- **360+ node definitions** extracted from ComfyUI source code
- **Auto model download** — workflows include native `models` field, ComfyUI auto-detects missing models and prompts download
- **LLM integration** — built-in support for comfyui_LLM_party nodes (OpenAI / Claude / Gemini / Ollama / DeepSeek)
- **Strict validation** — all templates pass link integrity, slot bounds, and widget type checks

## Quick Start

### Install

```bash
# For Claude Code — symlink recommended (auto-syncs updates)
ln -s /path/to/comfyui-workflow-skill ~/.claude/skills/comfyui-workflow

# Or copy
cp -r comfyui-workflow-skill/ ~/.claude/skills/comfyui-workflow
```

### Usage

Just tell your AI agent what you want:

```
"Generate a ComfyUI workflow for FLUX text-to-image with LoRA"
"Create a Wan 2.2 image-to-video workflow with camera control"
"Make an SDXL inpainting workflow"
"帮我生成一个 LLM 剧本 → 角色 → 分镜 → 视频的完整流水线"
"用 Gemini 增强提示词然后生成图片"
```

## Supported Templates (34)

### Image Generation

| Template | File | Description |
|----------|------|-------------|
| SD 1.5 txt2img | `sd15-txt2img.json` | Basic SD 1.5 text-to-image |
| SD 1.5 img2img | `sd15-img2img.json` | SD 1.5 image-to-image |
| SD 1.5 + LoRA | `sd15-lora.json` | SD 1.5 with LoRA |
| SD 1.5 + ControlNet | `sd15-controlnet.json` | SD 1.5 with ControlNet |
| SD 1.5 Inpaint | `sd15-inpaint.json` | SD 1.5 inpainting |
| SDXL txt2img | `sdxl-txt2img.json` | SDXL text-to-image |
| SDXL img2img | `sdxl-img2img.json` | SDXL image-to-image |
| SDXL + LoRA | `sdxl-lora.json` | SDXL with LoRA |
| SDXL + ControlNet | `sdxl-controlnet.json` | SDXL with ControlNet |
| SDXL Inpaint | `sdxl-inpaint.json` | SDXL inpainting |
| SD3 txt2img | `sd3-txt2img.json` | SD3 with TripleCLIPLoader |
| FLUX txt2img | `flux-txt2img.json` | FLUX.1 with advanced sampling |
| FLUX img2img | `flux-img2img.json` | FLUX.1 image-to-image |
| FLUX + LoRA | `flux-lora.json` | FLUX.1 with LoRA |

### Video Generation

| Template | File | Description |
|----------|------|-------------|
| Wan 2.2 txt2vid | `wan22-txt2vid.json` | Wan 2.2 text-to-video (832x480, 81 frames) |
| Wan 2.2 img2vid | `wan22-img2vid.json` | Wan 2.2 image-to-video with CLIP vision |
| Wan 2.2 First-Last | `wan22-first-last.json` | First+last frame video interpolation |
| Wan 2.2 Fun Control | `wan22-fun-control.json` | Control video + reference image |
| Wan 2.2 Camera | `wan22-camera.json` | Camera motion control |
| HunyuanVideo T2V | `hunyuan-video.json` | HunyuanVideo text-to-video |
| HunyuanVideo I2V | `hunyuan-video-i2v.json` | HunyuanVideo image-to-video |
| LTXV txt2vid | `ltxv-txt2vid.json` | LTXV text-to-video (768x512, 97 frames) |
| LTXV img2vid | `ltxv-img2vid.json` | LTXV image-to-video |
| Mochi txt2vid | `mochi-txt2vid.json` | Mochi text-to-video (848x480) |
| Cosmos txt2vid | `cosmos-txt2vid.json` | Cosmos text-to-video (1280x704) |
| Cosmos img2vid | `cosmos-img2vid.json` | Cosmos image-to-video |

### Audio, 3D & Special

| Template | File | Description |
|----------|------|-------------|
| Image Upscale | `upscale-model.json` | Upscale with RealESRGAN etc. |
| Stable Audio | `stable-audio.json` | Audio generation (47s) |
| Hunyuan3D v2 | `hunyuan3d-v2.json` | Image to 3D mesh |
| Stable Cascade | `stable-cascade.json` | Two-stage generation |

### LLM Integration (comfyui_LLM_party/)

| Template | File | Description |
|----------|------|-------------|
| LLM Chat (API) | `comfyui_LLM_party/llm-chat-api.json` | API LLM chat |
| LLM Chat (Ollama) | `comfyui_LLM_party/llm-chat-ollama.json` | Local Ollama chat |
| LLM Prompt Enhance | `comfyui_LLM_party/llm-prompt-enhance.json` | LLM → FLUX image |
| LLM Script Pipeline | `comfyui_LLM_party/llm-script-to-video.json` | Script → characters → storyboard |

## Auto Model Download

All templates include ComfyUI's native `models` field. When you import a workflow, ComfyUI automatically detects missing models and shows a download dialog:

```json
{
  "models": [
    {
      "name": "flux1-dev.safetensors",
      "url": "https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors",
      "directory": "diffusion_models"
    }
  ]
}
```

Supported download sources: HuggingFace, CivitAI.

## LLM Integration

Workflows can include LLM nodes from [comfyui_LLM_party](https://github.com/heshengtao/comfyui_LLM_party) for:
- Script/storyboard generation
- Character extraction
- Prompt enhancement
- Multi-stage video production pipelines

Supported providers: OpenAI, Claude, Gemini, DeepSeek, Ollama, and any OpenAI-compatible API.

## Node Knowledge Base

The skill includes a registry of **360+ ComfyUI nodes** extracted from source code:

- `references/node-registry.md` — Core 200+ nodes with full INPUT_TYPES
- `references/node-registry-additions.md` — 66 additional nodes (audio, LTXV, 3D, etc.)
- `references/workflow-format.md` — JSON format specification
- `references/common-workflows.md` — Common patterns & best practices

## Project Structure

```
comfyui-workflow-skill/
├── SKILL.md                              # Skill definition (entry point)
├── README.md                             # This file
├── references/
│   ├── node-registry.md                  # 360+ node definitions
│   ├── node-registry-additions.md        # Additional nodes (audio, 3D, etc.)
│   ├── workflow-format.md                # JSON format spec
│   └── common-workflows.md              # Common patterns
├── templates/                            # 30 core workflow templates
│   ├── sd15-txt2img.json
│   ├── sdxl-txt2img.json
│   ├── sd3-txt2img.json
│   ├── flux-txt2img.json
│   ├── flux-img2img.json
│   ├── flux-lora.json
│   ├── wan22-txt2vid.json
│   ├── wan22-img2vid.json
│   ├── wan22-first-last.json
│   ├── wan22-fun-control.json
│   ├── wan22-camera.json
│   ├── hunyuan-video.json
│   ├── hunyuan-video-i2v.json
│   ├── ltxv-txt2vid.json
│   ├── ltxv-img2vid.json
│   ├── mochi-txt2vid.json
│   ├── cosmos-txt2vid.json
│   ├── cosmos-img2vid.json
│   ├── stable-audio.json
│   ├── hunyuan3d-v2.json
│   ├── stable-cascade.json
│   ├── upscale-model.json
│   ├── ... (30 total)
│   └── comfyui_LLM_party/               # 4 LLM integration templates
│       ├── llm-chat-api.json
│       ├── llm-chat-ollama.json
│       ├── llm-prompt-enhance.json
│       └── llm-script-to-video.json
├── generate_all_templates.py             # Template generator (core)
├── generate_llm_templates.py             # Template generator (LLM)
├── generate_storyboard_workflow.py       # Storyboard pipeline generator
└── ComfyUI-ModelAutoDownloader/          # Model download utility
    └── inject_metadata.py               # Inject models field into workflows
```

## Contributing

PRs welcome! You can contribute:
- New workflow templates
- Support for additional custom nodes
- Bug fixes for generated JSON
- Documentation improvements

## License

MIT
