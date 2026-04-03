# ComfyUI Workflow Skill

> Generate ready-to-use ComfyUI workflow JSON files through natural language conversation.

**No API costs. No backend needed. Just describe what you want → get a valid workflow JSON → import into ComfyUI.**

## What is this?

A skill (for Claude Code, Codex, Cursor, and other AI coding agents) that generates ComfyUI workflow JSON files through conversation. Instead of manually connecting nodes in ComfyUI's node editor, just describe what you want in plain language.

## Quick Start

### Install

Copy the `SKILL.md` file and the entire project directory to your AI agent's skills folder:

```bash
# For Claude Code
cp -r comfyui-workflow-skill/ ~/.claude/skills/

# Or add to your project
cp -r comfyui-workflow-skill/ .claude/skills/
```

### Usage

Just tell your AI agent what you want:

```
"Generate a ComfyUI workflow for SDXL text-to-image, 1024x1024, with LoRA"

"Create a Wan 2.2 text-to-video workflow, 832x480, 81 frames"

"Make an inpainting workflow for SD 1.5"

"帮我生成一个 FLUX 文生图工作流"
```

The skill will output a valid JSON file you can directly import into ComfyUI via **Load** or drag-and-drop.

## Supported Workflows

| Workflow | Template | Model |
|----------|----------|-------|
| Text to Image | `sd15-txt2img.json` | SD 1.5 |
| Text to Image | `sdxl-txt2img.json` | SDXL |
| Text to Image | `flux-txt2img.json` | FLUX.1 |
| Text to Video | `wan22-txt2vid.json` | Wan 2.2 |
| Image to Video | `wan22-img2vid.json` | Wan 2.2 |
| Text/Image to Video | `hunyuan-video.json` | HunyuanVideo |
| Image Upscale | `upscale-model.json` | RealESRGAN etc. |
| ControlNet | `sd15-controlnet.json` | SD 1.5 + ControlNet |
| LoRA | `sdxl-lora.json` | SDXL + LoRA |
| Inpainting | `sd15-inpaint.json` | SD 1.5 Inpaint |

## Composable Modules

The skill can combine modules on top of base templates:

- **LoRA** — Add one or more LoRA models with custom strengths
- **ControlNet** — Canny, Depth, Pose, and more
- **Upscale** — Model-based or latent upscaling
- **Hi-Res Fix** — Two-pass generation for higher quality
- **Video output** — WEBP, WEBM, or MP4 format

## How It Works

1. You describe what you want in natural language
2. The skill selects the appropriate base template
3. Customizes parameters (resolution, steps, CFG, prompts, etc.)
4. Adds optional modules (ControlNet, LoRA, upscale, etc.)
5. Outputs a validated ComfyUI API-format JSON
6. You import it into ComfyUI and hit "Queue"

## Node Knowledge Base

The skill includes a complete registry of **199 built-in ComfyUI nodes** extracted directly from the [ComfyUI source code](https://github.com/comfyanonymous/ComfyUI), including:

- All input types, default values, and constraints
- Output slot mappings (critical for correct node linking)
- Category organization
- Deprecated/experimental status

See `references/node-registry.md` for the full registry.

## Project Structure

```
comfyui-workflow-skill/
├── SKILL.md                          # Skill definition (entry point)
├── README.md                         # This file
├── references/
│   ├── node-registry.md              # Complete node definitions (199 nodes)
│   ├── workflow-format.md            # JSON format specification
│   └── common-workflows.md           # Common patterns & best practices
└── templates/
    ├── sd15-txt2img.json             # SD 1.5 text-to-image
    ├── sdxl-txt2img.json             # SDXL text-to-image
    ├── flux-txt2img.json             # FLUX.1 text-to-image
    ├── wan22-txt2vid.json            # Wan 2.2 text-to-video
    ├── wan22-img2vid.json            # Wan 2.2 image-to-video
    ├── hunyuan-video.json            # HunyuanVideo
    ├── upscale-model.json            # Image upscale with model
    ├── sd15-controlnet.json          # SD 1.5 + ControlNet
    ├── sdxl-lora.json                # SDXL + LoRA
    └── sd15-inpaint.json             # SD 1.5 inpainting
```

## Contributing

PRs welcome! You can contribute:
- New workflow templates
- Support for additional custom nodes
- Bug fixes for generated JSON
- Documentation improvements

## License

MIT
