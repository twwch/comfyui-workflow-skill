## 5. Image

### SaveImage
- **Display**: Save Image
- **Category**: image
- **Inputs (required)**: images (IMAGE) | filename_prefix (STRING, default="ComfyUI")
- **Outputs**: (none - output node)
- **Function**: save_images

### PreviewImage
- **Display**: Preview Image
- **Category**: image
- **Inputs (required)**: images (IMAGE)
- **Outputs**: (none - output node)
- **Function**: save_images

### LoadImage
- **Display**: Load Image
- **Category**: image
- **Inputs (required)**: image (COMBO, image_upload)
- **Outputs**: IMAGE [0], MASK [1]
- **Function**: load_image

### LoadImageMask
- **Display**: Load Image (as Mask)
- **Category**: mask
- **Inputs (required)**: image (COMBO, image_upload) | channel (COMBO: alpha/red/green/blue)
- **Outputs**: MASK [0]
- **Function**: load_image

### LoadImageOutput
- **Display**: Load Image (from Outputs)
- **Category**: image
- **Inputs (required)**: image (COMBO, from output folder)
- **Outputs**: IMAGE [0], MASK [1]
- **Function**: load_image
- **Notes**: Experimental

### ImageScale
- **Display**: Upscale Image
- **Category**: image/upscaling
- **Inputs (required)**: image (IMAGE) | upscale_method (COMBO: nearest-exact/bilinear/area/bicubic/lanczos) | width (INT, default=512) | height (INT, default=512) | crop (COMBO: disabled/center)
- **Outputs**: IMAGE [0]
- **Function**: upscale

### ImageScaleBy
- **Display**: Upscale Image By
- **Category**: image/upscaling
- **Inputs (required)**: image (IMAGE) | upscale_method (COMBO) | scale_by (FLOAT, default=1.0, min=0.01, max=8.0)
- **Outputs**: IMAGE [0]
- **Function**: upscale

### ImageInvert
- **Display**: Invert Image
- **Category**: image
- **Inputs (required)**: image (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: invert

### ImageBatch
- **Display**: Batch Images
- **Category**: image
- **Inputs (required)**: image1 (IMAGE) | image2 (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: batch
- **Notes**: Deprecated. Use BatchImagesNode instead.

### EmptyImage
- **Display**: EmptyImage
- **Category**: image
- **Inputs (required)**: width (INT, default=512) | height (INT, default=512) | batch_size (INT, default=1) | color (INT, default=0, display=color)
- **Outputs**: IMAGE [0]
- **Function**: generate

### ImagePadForOutpaint
- **Display**: Pad Image for Outpainting
- **Category**: image
- **Inputs (required)**: image (IMAGE) | left (INT, default=0, step=8) | top (INT, default=0, step=8) | right (INT, default=0, step=8) | bottom (INT, default=0, step=8) | feathering (INT, default=40)
- **Outputs**: IMAGE [0], MASK [1]
- **Function**: expand_image

### ImageCrop
- **Display**: Image Crop (Deprecated)
- **Category**: image/transform
- **Inputs (required)**: image (IMAGE) | width (INT, default=512) | height (INT, default=512) | x (INT, default=0) | y (INT, default=0)
- **Outputs**: IMAGE [0]
- **Function**: execute
- **Notes**: Deprecated

### ImageCropV2
- **Display**: Image Crop
- **Category**: image/transform
- **Inputs (required)**: image (IMAGE) | crop_region (BOUNDING_BOX, component=ImageCrop)
- **Outputs**: IMAGE [0]
- **Function**: execute

### PrimitiveBoundingBox
- **Display**: Bounding Box
- **Category**: utils/primitive
- **Inputs (required)**: x (INT, default=0) | y (INT, default=0) | width (INT, default=512) | height (INT, default=512)
- **Outputs**: BOUNDING_BOX [0]
- **Function**: execute

### RepeatImageBatch
- **Display**: RepeatImageBatch
- **Category**: image/batch
- **Inputs (required)**: image (IMAGE) | amount (INT, default=1, min=1, max=4096)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageFromBatch
- **Display**: ImageFromBatch
- **Category**: image/batch
- **Inputs (required)**: image (IMAGE) | batch_index (INT, default=0) | length (INT, default=1)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageAddNoise
- **Display**: ImageAddNoise
- **Category**: image
- **Inputs (required)**: image (IMAGE) | seed (INT) | strength (FLOAT, default=0.5, min=0.0, max=1.0)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageCompositeMasked
- **Display**: ImageCompositeMasked
- **Category**: image
- **Inputs (required)**: destination (IMAGE) | source (IMAGE) | x (INT, default=0) | y (INT, default=0) | resize_source (BOOLEAN, default=False)
- **Inputs (optional)**: mask (MASK)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageStitch
- **Display**: Image Stitch
- **Category**: image/transform
- **Inputs (required)**: image1 (IMAGE) | direction (COMBO: right/down/left/up) | match_image_size (BOOLEAN, default=True) | spacing_width (INT, default=0) | spacing_color (COMBO: white/black/red/green/blue)
- **Inputs (optional)**: image2 (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ResizeAndPadImage
- **Display**: ResizeAndPadImage
- **Category**: image/transform
- **Inputs (required)**: image (IMAGE) | target_width (INT, default=512) | target_height (INT, default=512) | padding_color (COMBO: white/black) | interpolation (COMBO: area/bicubic/nearest-exact/bilinear/lanczos)
- **Outputs**: IMAGE [0]
- **Function**: execute

### GetImageSize
- **Display**: Get Image Size
- **Category**: image
- **Inputs (required)**: image (IMAGE)
- **Outputs**: INT [0] (width), INT [1] (height), INT [2] (batch_size)
- **Function**: execute

### ImageRotate
- **Display**: Image Rotate
- **Category**: image/transform
- **Inputs (required)**: image (IMAGE) | rotation (COMBO: none/90 degrees/180 degrees/270 degrees)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageFlip
- **Display**: ImageFlip
- **Category**: image/transform
- **Inputs (required)**: image (IMAGE) | flip_method (COMBO: x-axis: vertically/y-axis: horizontally)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageScaleToMaxDimension
- **Display**: ImageScaleToMaxDimension
- **Category**: image/upscaling
- **Inputs (required)**: image (IMAGE) | upscale_method (COMBO) | largest_size (INT, default=512)
- **Outputs**: IMAGE [0]
- **Function**: execute

### SaveAnimatedWEBP
- **Display**: SaveAnimatedWEBP
- **Category**: image/animation
- **Inputs (required)**: images (IMAGE) | filename_prefix (STRING) | fps (FLOAT, default=6.0) | lossless (BOOLEAN, default=True) | quality (INT, default=80) | method (COMBO: default/fastest/slowest)
- **Outputs**: (none - output node)
- **Function**: execute

### SaveAnimatedPNG
- **Display**: SaveAnimatedPNG
- **Category**: image/animation
- **Inputs (required)**: images (IMAGE) | filename_prefix (STRING) | fps (FLOAT, default=6.0) | compress_level (INT, default=4, min=0, max=9)
- **Outputs**: (none - output node)
- **Function**: execute

### SaveSVGNode
- **Display**: SaveSVGNode
- **Category**: image/save
- **Inputs (required)**: svg (SVG) | filename_prefix (STRING, default="svg/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: execute

### SplitImageToTileList
- **Display**: Split Image into List of Tiles
- **Category**: image/batch
- **Inputs (required)**: image (IMAGE) | tile_width (INT, default=1024) | tile_height (INT, default=1024) | overlap (INT, default=128)
- **Outputs**: IMAGE [0] (list)
- **Function**: execute

### ImageMergeTileList
- **Display**: Merge List of Tiles to Image
- **Category**: image/batch
- **Inputs (required)**: image_list (IMAGE, list) | final_width (INT, default=1024) | final_height (INT, default=1024) | overlap (INT, default=128)
- **Outputs**: IMAGE [0]
- **Function**: execute

### BatchImagesNode
- **Display**: Batch Images
- **Category**: image
- **Inputs (required)**: images (AUTOGROW, min=2 IMAGE inputs)
- **Outputs**: IMAGE [0]
- **Function**: execute

### RebatchImages
- **Display**: RebatchImages
- **Category**: image/batch
- **Inputs (required)**: images (IMAGE) | batch_size (INT, default=1, min=1, max=4096)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageCompare
- **Display**: ImageCompare
- **Category**: image
- **Inputs (required)**: image1 (IMAGE) | image2 (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: execute

### BatchImagesMasksLatentsNode
- **Display**: Batch Images Masks Latents
- **Category**: batch
- **Inputs (required)**: (AUTOGROW, supports IMAGE, MASK, LATENT)
- **Outputs**: IMAGE [0], MASK [1], LATENT [2]
- **Function**: execute

---
