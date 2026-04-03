## 13. Upscale Nodes

### ImageUpscaleWithModel
- **Display**: Upscale Image (using Model)
- **Category**: image/upscaling
- **Inputs (required)**: upscale_model (UPSCALE_MODEL) | image (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageScaleToTotalPixels
- **Display**: Scale Image to Total Pixels
- **Category**: image/upscaling
- **Inputs (required)**: image (IMAGE) | upscale_method (COMBO: nearest-exact/bilinear/area/bicubic/lanczos) | megapixels (FLOAT, default=1.0, min=0.01, max=16.0) | resolution_steps (INT, default=1, min=1, max=256)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ResizeImageMaskNode
- **Display**: Resize Image/Mask
- **Category**: transform
- **Inputs (required)**: input (IMAGE or MASK) | resize_type (DYNAMIC_COMBO: scale dimensions/scale by multiplier/scale longer dimension/scale shorter dimension/scale width/scale height/scale total pixels/match size/scale to multiple) | scale_method (COMBO: nearest-exact/bilinear/area/bicubic/lanczos)
- **Outputs**: IMAGE or MASK [0] (matches input type)
- **Function**: execute

### SD_4XUpscale_Conditioning
- **Display**: SD_4XUpscale_Conditioning
- **Category**: conditioning/upscale_diffusion
- **Inputs (required)**: images (IMAGE) | positive (CONDITIONING) | negative (CONDITIONING) | scale_ratio (FLOAT, default=4.0) | noise_augmentation (FLOAT, default=0.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### LTXVLatentUpsampler
- **Display**: LTXVLatentUpsampler
- **Category**: latent/video/ltxv
- **Inputs (required)**: model (MODEL) | samples (LATENT) | vae (VAE)
- **Outputs**: LATENT [0]
- **Function**: execute

---
