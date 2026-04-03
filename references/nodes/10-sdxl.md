## 10. SDXL Nodes

### CLIPTextEncodeSDXL
- **Display**: CLIPTextEncodeSDXL
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | width (INT, default=1024) | height (INT, default=1024) | crop_w (INT, default=0) | crop_h (INT, default=0) | target_width (INT, default=1024) | target_height (INT, default=1024) | text_g (STRING, multiline) | text_l (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### CLIPTextEncodeSDXLRefiner
- **Display**: CLIPTextEncodeSDXLRefiner
- **Category**: advanced/conditioning
- **Inputs (required)**: ascore (FLOAT, default=6.0) | width (INT, default=1024) | height (INT, default=1024) | text (STRING, multiline) | clip (CLIP)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

---
