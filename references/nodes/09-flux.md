## 9. FLUX Nodes

### CLIPTextEncodeFlux
- **Display**: CLIPTextEncodeFlux
- **Category**: advanced/conditioning/flux
- **Inputs (required)**: clip (CLIP) | clip_l (STRING, multiline) | t5xxl (STRING, multiline) | guidance (FLOAT, default=3.5, min=0.0, max=100.0)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### FluxGuidance
- **Display**: FluxGuidance
- **Category**: advanced/conditioning/flux
- **Inputs (required)**: conditioning (CONDITIONING) | guidance (FLOAT, default=3.5, min=0.0, max=100.0)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### FluxDisableGuidance
- **Display**: FluxDisableGuidance
- **Category**: advanced/conditioning/flux
- **Inputs (required)**: conditioning (CONDITIONING)
- **Outputs**: CONDITIONING [0]
- **Function**: execute
- **Notes**: Completely disables guidance embed on Flux models

### FluxKontextImageScale
- **Display**: FluxKontextImageScale
- **Category**: advanced/conditioning/flux
- **Inputs (required)**: image (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: execute
- **Notes**: Resizes image to optimal Flux Kontext resolution

### FluxKontextMultiReferenceLatentMethod
- **Display**: Edit Model Reference Method
- **Category**: advanced/conditioning/flux
- **Inputs (required)**: conditioning (CONDITIONING) | reference_latents_method (COMBO: offset/index/uxo/uno/index_timestep_zero)
- **Outputs**: CONDITIONING [0]
- **Function**: execute
- **Notes**: Experimental

### EmptyFlux2LatentImage
- **Display**: Empty Flux 2 Latent
- **Category**: latent
- **Inputs (required)**: width (INT, default=1024, step=16) | height (INT, default=1024, step=16) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### Flux2Scheduler
- **Display**: Flux2Scheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | width (INT, default=1024) | height (INT, default=1024)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### FluxKVCache
- **Display**: Flux KV Cache
- **Category**: (root)
- **Inputs (required)**: model (MODEL)
- **Outputs**: MODEL [0]
- **Function**: execute
- **Notes**: Experimental. Enables KV Cache optimization for reference images on Flux family models.

---
