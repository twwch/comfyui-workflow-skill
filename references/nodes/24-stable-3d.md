## 24. Stable 3D Nodes

### StableZero123_Conditioning
- **Display**: StableZero123_Conditioning
- **Category**: conditioning/3d_models
- **Inputs (required)**: clip_vision (CLIP_VISION) | init_image (IMAGE) | vae (VAE) | width (INT, default=256) | height (INT, default=256) | batch_size (INT, default=1) | elevation (FLOAT, default=0.0) | azimuth (FLOAT, default=0.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### StableZero123_Conditioning_Batched
- **Display**: StableZero123_Conditioning_Batched
- **Category**: conditioning/3d_models
- **Inputs (required)**: clip_vision (CLIP_VISION) | init_image (IMAGE) | vae (VAE) | width (INT, default=256) | height (INT, default=256) | batch_size (INT, default=1) | elevation (FLOAT) | azimuth (FLOAT) | elevation_batch_increment (FLOAT) | azimuth_batch_increment (FLOAT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### SV3D_Conditioning
- **Display**: SV3D_Conditioning
- **Category**: conditioning/3d_models
- **Inputs (required)**: clip_vision (CLIP_VISION) | init_image (IMAGE) | vae (VAE) | width (INT, default=576) | height (INT, default=576) | video_frames (INT, default=21) | elevation (FLOAT, default=0.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

---
