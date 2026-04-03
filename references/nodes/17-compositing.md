## 17. Compositing Nodes

### PorterDuffImageComposite
- **Display**: Porter-Duff Image Composite
- **Category**: mask/compositing
- **Inputs (required)**: source (IMAGE) | source_alpha (MASK) | destination (IMAGE) | destination_alpha (MASK) | mode (COMBO: ADD/CLEAR/DARKEN/DST/DST_ATOP/DST_IN/DST_OUT/DST_OVER/LIGHTEN/MULTIPLY/OVERLAY/SCREEN/SRC/SRC_ATOP/SRC_IN/SRC_OUT/SRC_OVER/XOR)
- **Outputs**: IMAGE [0], MASK [1]
- **Function**: execute

### SplitImageWithAlpha
- **Display**: Split Image with Alpha
- **Category**: mask/compositing
- **Inputs (required)**: image (IMAGE)
- **Outputs**: IMAGE [0], MASK [1]
- **Function**: execute

### JoinImageWithAlpha
- **Display**: Join Image with Alpha
- **Category**: mask/compositing
- **Inputs (required)**: image (IMAGE) | alpha (MASK)
- **Outputs**: IMAGE [0]
- **Function**: execute

---
