## 3. Sampling

### KSampler
- **Display**: KSampler
- **Category**: sampling
- **Inputs (required)**: model (MODEL) | seed (INT) | steps (INT, default=20) | cfg (FLOAT, default=8.0) | sampler_name (COMBO) | scheduler (COMBO) | positive (CONDITIONING) | negative (CONDITIONING) | latent_image (LATENT) | denoise (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: LATENT [0]
- **Function**: sample

### KSamplerAdvanced
- **Display**: KSampler (Advanced)
- **Category**: sampling
- **Inputs (required)**: model (MODEL) | add_noise (COMBO: enable/disable) | noise_seed (INT) | steps (INT, default=20) | cfg (FLOAT, default=8.0) | sampler_name (COMBO) | scheduler (COMBO) | positive (CONDITIONING) | negative (CONDITIONING) | latent_image (LATENT) | start_at_step (INT, default=0) | end_at_step (INT, default=10000) | return_with_leftover_noise (COMBO: disable/enable)
- **Outputs**: LATENT [0]
- **Function**: sample

---
