## 25. Cosmos Nodes

### EmptyCosmosLatentVideo
- **Display**: EmptyCosmosLatentVideo
- **Category**: latent/video
- **Inputs (required)**: width (INT, default=1280, step=16) | height (INT, default=704, step=16) | length (INT, default=121, step=8) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### CosmosImageToVideoLatent
- **Display**: CosmosImageToVideoLatent
- **Category**: conditioning/inpaint
- **Inputs (required)**: vae (VAE) | width (INT, default=1280) | height (INT, default=704) | length (INT, default=121) | batch_size (INT, default=1)
- **Inputs (optional)**: start_image (IMAGE) | end_image (IMAGE)
- **Outputs**: LATENT [0]
- **Function**: execute

### CosmosPredict2ImageToVideoLatent
- **Display**: CosmosPredict2ImageToVideoLatent
- **Category**: conditioning/inpaint
- **Inputs (required)**: vae (VAE) | width (INT, default=848) | height (INT, default=480) | length (INT, default=93) | batch_size (INT, default=1)
- **Inputs (optional)**: start_image (IMAGE) | end_image (IMAGE)
- **Outputs**: LATENT [0]
- **Function**: execute

---
