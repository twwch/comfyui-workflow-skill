## 14. Post Processing Nodes

### ImageBlend
- **Display**: Image Blend
- **Category**: image/postprocessing
- **Inputs (required)**: image1 (IMAGE) | image2 (IMAGE) | blend_factor (FLOAT, default=0.5, min=0.0, max=1.0) | blend_mode (COMBO: normal/multiply/screen/overlay/soft_light/difference)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageBlur
- **Display**: Image Blur
- **Category**: image/postprocessing
- **Inputs (required)**: image (IMAGE) | blur_radius (INT, default=1, min=1, max=31) | sigma (FLOAT, default=1.0, min=0.1, max=10.0)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageQuantize
- **Display**: ImageQuantize
- **Category**: image/postprocessing
- **Inputs (required)**: image (IMAGE) | colors (INT, default=256, min=1, max=256) | dither (COMBO: none/floyd-steinberg/bayer-2/bayer-4/bayer-8/bayer-16)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageSharpen
- **Display**: ImageSharpen
- **Category**: image/postprocessing
- **Inputs (required)**: image (IMAGE) | sharpen_radius (INT, default=1, min=1, max=31) | sigma (FLOAT, default=1.0) | alpha (FLOAT, default=1.0)
- **Outputs**: IMAGE [0]
- **Function**: execute

### Canny
- **Display**: Canny
- **Category**: image/preprocessors
- **Inputs (required)**: image (IMAGE) | low_threshold (FLOAT, default=0.4, min=0.01, max=0.99) | high_threshold (FLOAT, default=0.8, min=0.01, max=0.99)
- **Outputs**: IMAGE [0]
- **Function**: execute

### Morphology
- **Display**: Morphology
- **Category**: image/postprocessing
- **Inputs (required)**: image (IMAGE) | operation (COMBO: erode/dilate/open/close/gradient/top_hat/bottom_hat) | kernel_size (INT, default=3, min=1, max=31)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageRGBToYUV
- **Display**: ImageRGBToYUV
- **Category**: image/color
- **Inputs (required)**: image (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageYUVToRGB
- **Display**: ImageYUVToRGB
- **Category**: image/color
- **Inputs (required)**: image (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: execute

---
