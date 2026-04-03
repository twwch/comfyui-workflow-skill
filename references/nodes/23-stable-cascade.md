## 23. Stable Cascade Nodes

### StableCascade_EmptyLatentImage
- **Display**: StableCascade_EmptyLatentImage
- **Category**: latent/stable_cascade
- **Inputs (required)**: width (INT, default=1024) | height (INT, default=1024) | compression (INT, default=42) | batch_size (INT, default=1)
- **Outputs**: LATENT [0] (stage_c), LATENT [1] (stage_b)
- **Function**: execute

### StableCascade_StageC_VAEEncode
- **Display**: StableCascade_StageC_VAEEncode
- **Category**: latent/stable_cascade
- **Inputs (required)**: image (IMAGE) | vae (VAE) | compression (INT, default=42)
- **Outputs**: LATENT [0] (stage_c), LATENT [1] (stage_b)
- **Function**: execute

### StableCascade_StageB_Conditioning
- **Display**: StableCascade_StageB_Conditioning
- **Category**: conditioning/stable_cascade
- **Inputs (required)**: conditioning (CONDITIONING) | stage_c (LATENT)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### StableCascade_SuperResolutionControlnet
- **Display**: StableCascade_SuperResolutionControlnet
- **Category**: _for_testing/stable_cascade
- **Inputs (required)**: image (IMAGE) | vae (VAE)
- **Outputs**: IMAGE [0] (controlnet_input), LATENT [1] (stage_c), LATENT [2] (stage_b)
- **Function**: execute
- **Notes**: Experimental

---
