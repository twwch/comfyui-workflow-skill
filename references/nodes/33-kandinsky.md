## 33. Kandinsky Nodes

### Kandinsky5ImageToVideo
- **Display**: Kandinsky5ImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT) | height (INT) | length (INT) | batch_size (INT)
- **Inputs (optional)**: start_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### NormalizeVideoLatentStart
- **Display**: NormalizeVideoLatentStart
- **Category**: latent/video
- **Inputs (required)**: samples (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute

### CLIPTextEncodeKandinsky5
- **Display**: CLIPTextEncodeKandinsky5
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | t5xxl (STRING, multiline) | umt5xxl (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

---
