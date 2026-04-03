## 16. Mask Nodes

### MaskToImage
- **Display**: Convert Mask to Image
- **Category**: mask
- **Inputs (required)**: mask (MASK)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageToMask
- **Display**: Convert Image to Mask
- **Category**: mask
- **Inputs (required)**: image (IMAGE) | channel (COMBO: red/green/blue/alpha)
- **Outputs**: MASK [0]
- **Function**: execute

### ImageColorToMask
- **Display**: ImageColorToMask
- **Category**: mask
- **Inputs (required)**: image (IMAGE) | color (INT, default=0, max=0xFFFFFF)
- **Outputs**: MASK [0]
- **Function**: execute

### SolidMask
- **Display**: SolidMask
- **Category**: mask
- **Inputs (required)**: value (FLOAT, default=1.0, min=0.0, max=1.0) | width (INT, default=512) | height (INT, default=512)
- **Outputs**: MASK [0]
- **Function**: execute

### InvertMask
- **Display**: InvertMask
- **Category**: mask
- **Inputs (required)**: mask (MASK)
- **Outputs**: MASK [0]
- **Function**: execute

### CropMask
- **Display**: CropMask
- **Category**: mask
- **Inputs (required)**: mask (MASK) | x (INT, default=0) | y (INT, default=0) | width (INT, default=512) | height (INT, default=512)
- **Outputs**: MASK [0]
- **Function**: execute

### MaskComposite
- **Display**: MaskComposite
- **Category**: mask
- **Inputs (required)**: destination (MASK) | source (MASK) | x (INT, default=0) | y (INT, default=0) | operation (COMBO: multiply/add/subtract/and/or/xor)
- **Outputs**: MASK [0]
- **Function**: execute

### FeatherMask
- **Display**: FeatherMask
- **Category**: mask
- **Inputs (required)**: mask (MASK) | left (INT, default=0) | top (INT, default=0) | right (INT, default=0) | bottom (INT, default=0)
- **Outputs**: MASK [0]
- **Function**: execute

### GrowMask
- **Display**: Grow Mask
- **Category**: mask
- **Inputs (required)**: mask (MASK) | expand (INT, default=0, min=-16384, max=16384) | tapered_corners (BOOLEAN, default=True)
- **Outputs**: MASK [0]
- **Function**: execute

### ThresholdMask
- **Display**: ThresholdMask
- **Category**: mask
- **Inputs (required)**: mask (MASK) | value (FLOAT, default=0.5, min=0.0, max=1.0)
- **Outputs**: MASK [0]
- **Function**: execute

### MaskPreview
- **Display**: Preview Mask
- **Category**: mask
- **Inputs (required)**: mask (MASK)
- **Outputs**: (none - output node)
- **Function**: execute

### BatchMasksNode
- **Display**: Batch Masks
- **Category**: mask
- **Inputs (required)**: masks (AUTOGROW, min=2 MASK inputs)
- **Outputs**: MASK [0]
- **Function**: execute

---
