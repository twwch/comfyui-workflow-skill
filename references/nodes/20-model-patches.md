## 20. Model Patches

### FreeU
- **Display**: FreeU
- **Category**: model_patches/unet
- **Inputs (required)**: model (MODEL) | b1 (FLOAT, default=1.1) | b2 (FLOAT, default=1.2) | s1 (FLOAT, default=0.9) | s2 (FLOAT, default=0.2)
- **Outputs**: MODEL [0]
- **Function**: execute

### FreeU_V2
- **Display**: FreeU_V2
- **Category**: model_patches/unet
- **Inputs (required)**: model (MODEL) | b1 (FLOAT, default=1.3) | b2 (FLOAT, default=1.4) | s1 (FLOAT, default=0.9) | s2 (FLOAT, default=0.2)
- **Outputs**: MODEL [0]
- **Function**: execute

### PerturbedAttentionGuidance
- **Display**: PerturbedAttentionGuidance
- **Category**: model_patches/unet
- **Inputs (required)**: model (MODEL) | scale (FLOAT, default=3.0, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### SelfAttentionGuidance
- **Display**: SelfAttentionGuidance
- **Category**: _for_testing
- **Inputs (required)**: model (MODEL) | scale (FLOAT, default=0.5) | blur_sigma (FLOAT, default=2.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### PerpNeg
- **Display**: PerpNeg
- **Category**: _for_testing
- **Inputs (required)**: model (MODEL) | empty_conditioning (CONDITIONING) | neg_scale (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### HyperTile
- **Display**: HyperTile
- **Category**: _for_testing
- **Inputs (required)**: model (MODEL) | tile_size (INT, default=256) | swap_size (INT, default=2) | max_depth (INT, default=0) | scale_depth (BOOLEAN, default=False)
- **Outputs**: MODEL [0]
- **Function**: execute

### PatchModelAddDownscale
- **Display**: PatchModelAddDownscale
- **Category**: _for_testing
- **Inputs (required)**: model (MODEL) | block_number (INT) | downscale_factor (FLOAT, default=2.0) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=0.35) | downscale_after_skip (BOOLEAN, default=True) | downscale_method (COMBO) | upscale_method (COMBO)
- **Outputs**: MODEL [0]
- **Function**: execute

### TomePatchModel
- **Display**: TomePatchModel
- **Category**: _for_testing
- **Inputs (required)**: model (MODEL) | ratio (FLOAT, default=0.3, min=0.0, max=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### DifferentialDiffusion
- **Display**: Differential Diffusion
- **Category**: _for_testing
- **Inputs (required)**: model (MODEL)
- **Inputs (optional)**: strength (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute
- **Notes**: Experimental

### UNetSelfAttentionMultiply
- **Display**: UNetSelfAttentionMultiply
- **Category**: _for_testing/attention_multiply
- **Inputs (required)**: model (MODEL) | q (FLOAT, default=1.0) | k (FLOAT, default=1.0) | v (FLOAT, default=1.0) | out (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### UNetCrossAttentionMultiply
- **Display**: UNetCrossAttentionMultiply
- **Category**: _for_testing/attention_multiply
- **Inputs (required)**: model (MODEL) | q (FLOAT, default=1.0) | k (FLOAT, default=1.0) | v (FLOAT, default=1.0) | out (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### CLIPAttentionMultiply
- **Display**: CLIPAttentionMultiply
- **Category**: _for_testing/attention_multiply
- **Inputs (required)**: clip (CLIP) | q (FLOAT, default=1.0) | k (FLOAT, default=1.0) | v (FLOAT, default=1.0) | out (FLOAT, default=1.0)
- **Outputs**: CLIP [0]
- **Function**: execute

### UNetTemporalAttentionMultiply
- **Display**: UNetTemporalAttentionMultiply
- **Category**: _for_testing/attention_multiply
- **Inputs (required)**: model (MODEL) | self_structural (FLOAT, default=1.0) | self_temporal (FLOAT, default=1.0) | cross_structural (FLOAT, default=1.0) | cross_temporal (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### ScaleROPE
- **Display**: ScaleROPE
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | width_factor (FLOAT, default=1.0) | height_factor (FLOAT, default=1.0) | temporal_factor (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### CFGZeroStar
- **Display**: CFGZeroStar
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL)
- **Outputs**: MODEL [0]
- **Function**: execute

### CFGNorm
- **Display**: CFGNorm
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | strength (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### TCFG
- **Display**: TCFG
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | eta (FLOAT, default=0.2) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### NAGuidance
- **Display**: NAGuidance
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | scale (FLOAT, default=0.5) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### APG
- **Display**: APG
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | eta (FLOAT, default=1.0) | norm_threshold (FLOAT, default=0.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### Epsilon Scaling
- **Display**: Epsilon Scaling
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | scaling (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### TemporalScoreRescaling
- **Display**: TemporalScoreRescaling
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL)
- **Outputs**: MODEL [0]
- **Function**: execute

### FreSca
- **Display**: FreSca
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | scale (FLOAT, default=1.0) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

### Mahiro
- **Display**: Mahiro
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL)
- **Outputs**: MODEL [0]
- **Function**: execute

### TorchCompileModel
- **Display**: TorchCompileModel
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | backend (COMBO)
- **Outputs**: MODEL [0]
- **Function**: execute

### ContextWindowsManual
- **Display**: ContextWindowsManual
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | context_length (INT) | context_overlap (INT) | context_stride (INT)
- **Outputs**: MODEL [0]
- **Function**: execute

### ChromaRadianceOptions
- **Display**: ChromaRadianceOptions
- **Category**: model_patches/chroma_radiance
- **Inputs (required)**: model (MODEL) | preserve_wrapper (BOOLEAN, default=True) | start_sigma (FLOAT, default=1.0) | end_sigma (FLOAT, default=0.0) | nerf_tile_size (INT, default=-1)
- **Outputs**: MODEL [0]
- **Function**: execute

---
