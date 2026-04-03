## 19. Model Merging Nodes

### ModelMergeSimple
- **Display**: ModelMergeSimple
- **Category**: advanced/model_merging
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL) | ratio (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: MODEL [0]
- **Function**: merge

### ModelMergeBlocks
- **Display**: ModelMergeBlocks
- **Category**: advanced/model_merging
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL) | input (FLOAT, default=1.0) | middle (FLOAT, default=1.0) | out (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: merge

### ModelMergeSubtract
- **Display**: ModelMergeSubtract
- **Category**: advanced/model_merging
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL) | multiplier (FLOAT, default=1.0, min=-10.0, max=10.0)
- **Outputs**: MODEL [0]
- **Function**: merge

### ModelMergeAdd
- **Display**: ModelMergeAdd
- **Category**: advanced/model_merging
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL)
- **Outputs**: MODEL [0]
- **Function**: merge

### CLIPMergeSimple
- **Display**: CLIPMergeSimple
- **Category**: advanced/model_merging
- **Inputs (required)**: clip1 (CLIP) | clip2 (CLIP) | ratio (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: CLIP [0]
- **Function**: merge

### CLIPMergeSubtract
- **Display**: CLIPMergeSubtract
- **Category**: advanced/model_merging
- **Inputs (required)**: clip1 (CLIP) | clip2 (CLIP) | multiplier (FLOAT, default=1.0, min=-10.0, max=10.0)
- **Outputs**: CLIP [0]
- **Function**: merge

### CLIPMergeAdd
- **Display**: CLIPMergeAdd
- **Category**: advanced/model_merging
- **Inputs (required)**: clip1 (CLIP) | clip2 (CLIP)
- **Outputs**: CLIP [0]
- **Function**: merge

### CheckpointSave
- **Display**: Save Checkpoint
- **Category**: advanced/model_merging
- **Inputs (required)**: model (MODEL) | clip (CLIP) | vae (VAE) | filename_prefix (STRING, default="checkpoints/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: save

### CLIPSave
- **Display**: CLIPSave
- **Category**: advanced/model_merging
- **Inputs (required)**: clip (CLIP) | filename_prefix (STRING, default="clip/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: save

### VAESave
- **Display**: VAESave
- **Category**: advanced/model_merging
- **Inputs (required)**: vae (VAE) | filename_prefix (STRING, default="vae/ComfyUI_vae")
- **Outputs**: (none - output node)
- **Function**: save

### ModelSave
- **Display**: ModelSave
- **Category**: advanced/model_merging
- **Inputs (required)**: model (MODEL) | filename_prefix (STRING, default="diffusion_models/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: save

### ModelMergeSD1
- **Display**: ModelMergeSD1
- **Category**: advanced/model_merging/model_specific
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL) | (per-block FLOAT ratios)
- **Outputs**: MODEL [0]
- **Function**: merge

### ModelMergeSDXL
- **Display**: ModelMergeSDXL
- **Category**: advanced/model_merging/model_specific
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL) | (per-block FLOAT ratios)
- **Outputs**: MODEL [0]
- **Function**: merge

### ModelMergeSD3_2B
- **Display**: ModelMergeSD3_2B
- **Category**: advanced/model_merging/model_specific
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL) | (per-block FLOAT ratios)
- **Outputs**: MODEL [0]
- **Function**: merge

### ModelMergeFlux1
- **Display**: ModelMergeFlux1
- **Category**: advanced/model_merging/model_specific
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL) | (per-block FLOAT ratios)
- **Outputs**: MODEL [0]
- **Function**: merge

### ModelMergeSD35_Large
- **Display**: ModelMergeSD35_Large
- **Category**: advanced/model_merging/model_specific
- **Inputs (required)**: model1 (MODEL) | model2 (MODEL) | (per-block FLOAT ratios)
- **Outputs**: MODEL [0]
- **Function**: merge

---
