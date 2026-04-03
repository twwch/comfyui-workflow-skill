# Common ComfyUI Workflow Patterns

## Basic Text-to-Image Pipeline
```
CheckpointLoaderSimple → [MODEL, CLIP, VAE]
    ├── CLIP → CLIPTextEncode (positive) → CONDITIONING
    ├── CLIP → CLIPTextEncode (negative) → CONDITIONING
    ├── MODEL ─────────────────────────────────┐
    │                                          ▼
    │   EmptyLatentImage → LATENT ──→ KSampler → LATENT
    │                                          │
    └── VAE ──────────────────────→ VAEDecode ←┘
                                       │
                                  SaveImage
```

## Adding LoRA
Insert between CheckpointLoaderSimple and CLIPTextEncode:
```
CheckpointLoaderSimple → [MODEL, CLIP]
    → LoraLoader(model, clip, lora_name, strength_model, strength_clip)
    → [MODEL, CLIP] (modified)
```

## Adding ControlNet
Insert between CLIPTextEncode and KSampler:
```
ControlNetLoader → CONTROL_NET
LoadImage → IMAGE (control image)
CLIPTextEncode → positive CONDITIONING
CLIPTextEncode → negative CONDITIONING
    → ControlNetApplyAdvanced(positive, negative, control_net, image, strength)
    → [positive CONDITIONING, negative CONDITIONING] (modified)
```

## Image-to-Image (img2img)
Same as txt2img but:
- Replace EmptyLatentImage with: LoadImage → VAEEncode → LATENT
- Set KSampler denoise < 1.0 (typical: 0.5-0.8)

## Inpainting
```
LoadImage → [IMAGE, MASK]
VAEEncodeForInpaint(pixels=IMAGE, vae=VAE, mask=MASK) → LATENT
KSampler(denoise=1.0) → LATENT
```

## Upscale with Model
```
UpscaleModelLoader → UPSCALE_MODEL
LoadImage (or VAEDecode output) → IMAGE
ImageUpscaleWithModel(upscale_model, image) → IMAGE (upscaled)
SaveImage
```

## Hi-Res Fix (Two-pass)
```
Pass 1: KSampler at low resolution → LATENT
LatentUpscale or LatentUpscaleBy → LATENT (upscaled)
Pass 2: KSampler(denoise=0.5-0.7) at high resolution → LATENT
VAEDecode → SaveImage
```

## SDXL Specific
- Use CLIPTextEncodeSDXL for base model (text_g + text_l, with dimensions)
- Or use standard CLIPTextEncode (simpler, works fine)
- Default resolution: 1024x1024 (or other SDXL-supported ratios)
- Common resolutions: 1024x1024, 1152x896, 896x1152, 1216x832, 832x1216

## FLUX Specific
- Use UNETLoader + CLIPLoader (or DualCLIPLoader) instead of CheckpointLoaderSimple
- Use CLIPTextEncodeFlux with clip_l + t5xxl prompts + guidance
- Use BasicGuider + BasicScheduler + KSamplerSelect + SamplerCustomAdvanced
- Or use simple KSampler with FluxGuidance applied to conditioning
- Default resolution: 1024x1024
- VAE loaded separately with VAELoader

## Wan 2.2 Text-to-Video
```
UNETLoader → MODEL
DualCLIPLoader(type="wan") → CLIP
VAELoader → VAE
CLIPTextEncode (positive) → CONDITIONING
CLIPTextEncode (negative) → CONDITIONING
WanImageToVideo(positive, negative, vae, width=832, height=480, length=81)
    → [positive, negative, LATENT]
KSampler(model, positive, negative, latent) → LATENT
VAEDecode → IMAGE
SaveAnimatedWEBP or SaveWEBM
```

## Wan 2.2 Image-to-Video
Same as text-to-video but:
- Add CLIPVisionLoader → CLIP_VISION
- Add LoadImage → IMAGE (start frame)
- CLIPVisionEncode(clip_vision, image) → CLIP_VISION_OUTPUT
- Pass clip_vision_output and start_image to WanImageToVideo

## HunyuanVideo
```
UNETLoader → MODEL
CLIPLoader(type="wan" or specific) or DualCLIPLoader → CLIP
VAELoader → VAE
CLIPTextEncode → CONDITIONING
EmptyHunyuanLatentVideo(width, height, length) → LATENT
KSampler → LATENT
VAEDecode → IMAGE
SaveAnimatedWEBP
```

## Recommended Parameters by Model

### SD 1.5
- Resolution: 512x512, 512x768, 768x512
- Steps: 20-30
- CFG: 7-8
- Sampler: euler_ancestral, dpmpp_2m
- Scheduler: karras

### SDXL
- Resolution: 1024x1024, 1152x896, 896x1152
- Steps: 20-30
- CFG: 7-8
- Sampler: euler, dpmpp_2m
- Scheduler: karras

### FLUX
- Resolution: 1024x1024, 1280x720
- Steps: 20-28
- CFG: 1.0 (uses guidance in conditioning instead)
- Guidance: 3.5
- Sampler: euler
- Scheduler: simple or beta

### Wan 2.2
- Resolution: 832x480 (landscape), 480x832 (portrait)
- Video length: 81 frames (default), step=4
- Steps: 20-30
- CFG: 6-7
- Sampler: euler
- Scheduler: normal

### HunyuanVideo
- Resolution: 848x480
- Video length: 25-53 frames, step=4
- Steps: 30
- CFG: 6
- Sampler: euler
- Scheduler: normal
