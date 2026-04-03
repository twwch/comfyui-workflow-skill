## 6. ControlNet Nodes

### ControlNetApply
- **Display**: Apply ControlNet (OLD)
- **Category**: conditioning/controlnet
- **Inputs (required)**: conditioning (CONDITIONING) | control_net (CONTROL_NET) | image (IMAGE) | strength (FLOAT, default=1.0, min=0.0, max=10.0)
- **Outputs**: CONDITIONING [0]
- **Function**: apply_controlnet
- **Notes**: Deprecated

### ControlNetApplyAdvanced
- **Display**: Apply ControlNet
- **Category**: conditioning/controlnet
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | control_net (CONTROL_NET) | image (IMAGE) | strength (FLOAT, default=1.0) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=1.0)
- **Inputs (optional)**: vae (VAE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: apply_controlnet

### SetUnionControlNetType
- **Display**: SetUnionControlNetType
- **Category**: conditioning/controlnet
- **Inputs (required)**: control_net (CONTROL_NET) | type (COMBO: auto + union types)
- **Outputs**: CONTROL_NET [0]
- **Function**: execute

### ControlNetInpaintingAliMamaApply
- **Display**: ControlNetInpaintingAliMamaApply
- **Category**: conditioning/controlnet
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | control_net (CONTROL_NET) | vae (VAE) | image (IMAGE) | mask (MASK) | strength (FLOAT, default=1.0) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=1.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute

### ControlNetApplySD3
- **Display**: Apply Controlnet with VAE
- **Category**: conditioning/controlnet
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | control_net (CONTROL_NET) | vae (VAE) | image (IMAGE) | strength (FLOAT, default=1.0) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=1.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute
- **Notes**: Deprecated

### QwenImageDiffsynthControlnet
- **Display**: QwenImageDiffsynthControlnet
- **Category**: advanced/loaders/qwen_image
- **Inputs (required)**: model (MODEL) | model_patch (MODEL_PATCH) | vae (VAE) | image (IMAGE) | strength (FLOAT, default=1.0)
- **Inputs (optional)**: inpaint_image (IMAGE) | mask (MASK)
- **Outputs**: MODEL [0]
- **Function**: execute

### ZImageFunControlnet
- **Display**: ZImageFunControlnet
- **Category**: advanced/loaders/zimage
- **Inputs (required)**: model (MODEL) | model_patch (MODEL_PATCH) | vae (VAE) | strength (FLOAT, default=1.0)
- **Inputs (optional)**: image (IMAGE) | inpaint_image (IMAGE) | mask (MASK)
- **Outputs**: MODEL [0]
- **Function**: execute

### USOStyleReference
- **Display**: USOStyleReference
- **Category**: advanced/model_patches/flux
- **Inputs (required)**: model (MODEL) | model_patch (MODEL_PATCH) | clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: MODEL [0]
- **Function**: apply_patch
- **Notes**: Experimental

---
