# ComfyUI Workflow Generator

## Description

Generate ready-to-use ComfyUI workflow JSON files through natural language conversation. Users describe what they want to create, and this skill produces valid ComfyUI API-format JSON that can be directly imported and executed.

## Activation

Trigger when the user asks to:
- Create/generate a ComfyUI workflow
- Make an image generation workflow
- Build a video generation pipeline
- Set up txt2img, img2img, img2vid, txt2vid workflows
- Generate a ComfyUI JSON file

Trigger keywords: comfyui, workflow, 工作流, 文生图, 图生图, 文生视频, 图生视频, txt2img, img2img, txt2vid, img2vid, upscale, 放大, inpaint, 重绘, controlnet, lora

## Instructions

### Step 1: Understand User Intent

Ask the user what they want to create. Gather:

1. **Task type**: txt2img / img2img / txt2vid / img2vid / upscale / inpaint
2. **Model**: SD1.5 / SDXL / FLUX / Wan2.2 / HunyuanVideo / SD3
3. **Key parameters**: resolution, steps, CFG, sampler
4. **Optional modules**: ControlNet, LoRA, IPAdapter, upscale model
5. **Prompt content**: positive and negative prompts

If the user is vague, suggest the most common configuration for their task type.

### Step 2: Select and Compose Template

Based on user intent, load the appropriate base template from `templates/` directory and customize it:

1. Read the matching template JSON file
2. Modify parameters according to user requirements
3. Add optional modules (ControlNet, LoRA, etc.) by inserting additional nodes and links
4. Validate the workflow DAG structure

### Step 3: Generate and Deliver

1. Output the complete workflow JSON (API format)
2. Save it to a `.json` file if the user requests
3. Provide a brief explanation of the workflow structure
4. List any required models/custom nodes the user needs to install

### Workflow JSON Format Rules

**CRITICAL — follow these rules exactly:**

- Use **API format** (flat dict, string node IDs, `class_type` + `inputs`)
- Links are `["source_node_id", output_slot_index]` — slot index is 0-based, maps to source node's RETURN_TYPES
- Every workflow MUST have at least one output node (SaveImage, PreviewImage, SaveVideo, etc.)
- All `required` inputs must be provided (check node-registry.md)
- Values must satisfy min/max constraints
- Node IDs are arbitrary strings (use sequential numbers: "1", "2", "3"...)
- For model/file selection inputs (ckpt_name, lora_name, etc.), use descriptive placeholders like `"your_model.safetensors"` with a comment explaining what to replace

### Common Output Slot Mappings

```
CheckpointLoaderSimple: 0=MODEL, 1=CLIP, 2=VAE
UNETLoader:             0=MODEL
CLIPLoader:             0=CLIP
DualCLIPLoader:         0=CLIP
VAELoader:              0=VAE
LoraLoader:             0=MODEL, 1=CLIP
CLIPTextEncode:         0=CONDITIONING
EmptyLatentImage:       0=LATENT
KSampler:               0=LATENT
VAEDecode:              0=IMAGE
LoadImage:              0=IMAGE, 1=MASK
ControlNetLoader:       0=CONTROL_NET
UpscaleModelLoader:     0=UPSCALE_MODEL
ImageUpscaleWithModel:  0=IMAGE
CLIPVisionLoader:       0=CLIP_VISION
CLIPVisionEncode:       0=CLIP_VISION_OUTPUT
```

### Node Reference

For complete node definitions (INPUT_TYPES, RETURN_TYPES, defaults, constraints), read:
- `references/node-registry.md` — all 199 built-in nodes
- `references/workflow-format.md` — JSON format specification
- `references/common-workflows.md` — common workflow patterns and best practices

### Available Templates

| Template | File | Description |
|----------|------|-------------|
| SD 1.5 Text to Image | `templates/sd15-txt2img.json` | Basic SD 1.5 text-to-image |
| SDXL Text to Image | `templates/sdxl-txt2img.json` | SDXL with dual CLIP encoding |
| FLUX Text to Image | `templates/flux-txt2img.json` | FLUX.1 with guidance |
| Wan2.2 Text to Video | `templates/wan22-txt2vid.json` | Wan 2.2 text-to-video generation |
| Wan2.2 Image to Video | `templates/wan22-img2vid.json` | Wan 2.2 image-to-video with CLIP vision |
| Image Upscale | `templates/upscale-model.json` | Upscale with model (RealESRGAN etc.) |
| SD 1.5 + ControlNet | `templates/sd15-controlnet.json` | SD 1.5 with ControlNet |
| SDXL + LoRA | `templates/sdxl-lora.json` | SDXL with LoRA loading |
| HunyuanVideo | `templates/hunyuan-video.json` | HunyuanVideo text/image to video |
| Inpaint | `templates/sd15-inpaint.json` | SD 1.5 inpainting workflow |

### Quality Checklist

Before delivering a workflow, verify:
- [ ] Every node has `class_type` and `inputs`
- [ ] All required inputs are present
- [ ] All links point to valid node IDs and correct slot indices
- [ ] At least one output node exists (SaveImage/PreviewImage/SaveVideo)
- [ ] No circular dependencies
- [ ] Model file placeholders are clearly marked
- [ ] Parameter values are within valid ranges
