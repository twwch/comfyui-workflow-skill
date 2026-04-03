## 12. HunyuanVideo Nodes

### CLIPTextEncodeHunyuanDiT
- **Display**: CLIPTextEncodeHunyuanDiT
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | bert (STRING, multiline) | mt5xl (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### TextEncodeHunyuanVideo_ImageToVideo
- **Display**: TextEncodeHunyuanVideo_ImageToVideo
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | clip_vision_output (CLIP_VISION_OUTPUT) | prompt (STRING, multiline) | image_interleave (INT, default=2, min=1, max=512)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### EmptyHunyuanLatentVideo
- **Display**: Empty HunyuanVideo 1.0 Latent
- **Category**: latent/video
- **Inputs (required)**: width (INT, default=848, step=16) | height (INT, default=480, step=16) | length (INT, default=25, step=4) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### EmptyHunyuanVideo15Latent
- **Display**: Empty HunyuanVideo 1.5 Latent
- **Category**: latent/video
- **Inputs (required)**: width (INT, default=848, step=16) | height (INT, default=480, step=16) | length (INT, default=25, step=4) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute
- **Notes**: Uses 32 latent channels and scale factor 16

### HunyuanVideo15ImageToVideo
- **Display**: HunyuanVideo15ImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=848) | height (INT, default=480) | length (INT, default=33) | batch_size (INT, default=1)
- **Inputs (optional)**: start_image (IMAGE) | clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### HunyuanVideo15SuperResolution
- **Display**: HunyuanVideo15SuperResolution
- **Category**: (default)
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | latent (LATENT) | noise_augmentation (FLOAT, default=0.70)
- **Inputs (optional)**: vae (VAE) | start_image (IMAGE) | clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### HunyuanVideo15LatentUpscaleWithModel
- **Display**: Hunyuan Video 15 Latent Upscale With Model
- **Category**: latent
- **Inputs (required)**: model (LATENT_UPSCALE_MODEL) | samples (LATENT) | upscale_method (COMBO) | width (INT, default=1280) | height (INT, default=720) | crop (COMBO: disabled/center)
- **Outputs**: LATENT [0]
- **Function**: execute

### HunyuanImageToVideo
- **Display**: HunyuanImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | vae (VAE) | width (INT, default=848) | height (INT, default=480) | length (INT, default=53) | batch_size (INT, default=1) | guidance_type (COMBO: v1 (concat)/v2 (replace)/custom)
- **Inputs (optional)**: start_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), LATENT [1]
- **Function**: execute

### EmptyHunyuanImageLatent
- **Display**: EmptyHunyuanImageLatent
- **Category**: latent
- **Inputs (required)**: width (INT, default=2048, step=32) | height (INT, default=2048, step=32) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### HunyuanRefinerLatent
- **Display**: HunyuanRefinerLatent
- **Category**: (default)
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | latent (LATENT) | noise_augmentation (FLOAT, default=0.10)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

---
