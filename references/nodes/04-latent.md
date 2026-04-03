## 4. Latent

### EmptyLatentImage
- **Display**: Empty Latent Image
- **Category**: latent
- **Inputs (required)**: width (INT, default=512, min=16, max=16384, step=8) | height (INT, default=512, min=16, max=16384, step=8) | batch_size (INT, default=1, min=1, max=4096)
- **Outputs**: LATENT [0]
- **Function**: generate

### VAEDecode
- **Display**: VAE Decode
- **Category**: latent
- **Inputs (required)**: samples (LATENT) | vae (VAE)
- **Outputs**: IMAGE [0]
- **Function**: decode

### VAEEncode
- **Display**: VAE Encode
- **Category**: latent
- **Inputs (required)**: pixels (IMAGE) | vae (VAE)
- **Outputs**: LATENT [0]
- **Function**: encode

### VAEDecodeTiled
- **Display**: VAE Decode (Tiled)
- **Category**: _for_testing
- **Inputs (required)**: samples (LATENT) | vae (VAE) | tile_size (INT, default=512) | overlap (INT, default=64) | temporal_size (INT, default=64) | temporal_overlap (INT, default=8)
- **Outputs**: IMAGE [0]
- **Function**: decode

### VAEEncodeTiled
- **Display**: VAE Encode (Tiled)
- **Category**: _for_testing
- **Inputs (required)**: pixels (IMAGE) | vae (VAE) | tile_size (INT, default=512) | overlap (INT, default=64) | temporal_size (INT, default=64) | temporal_overlap (INT, default=8)
- **Outputs**: LATENT [0]
- **Function**: encode

### VAEEncodeForInpaint
- **Display**: VAE Encode (for Inpainting)
- **Category**: latent/inpaint
- **Inputs (required)**: pixels (IMAGE) | vae (VAE) | mask (MASK) | grow_mask_by (INT, default=6, min=0, max=64)
- **Outputs**: LATENT [0]
- **Function**: encode

### SetLatentNoiseMask
- **Display**: Set Latent Noise Mask
- **Category**: latent/inpaint
- **Inputs (required)**: samples (LATENT) | mask (MASK)
- **Outputs**: LATENT [0]
- **Function**: set_mask

### LatentUpscale
- **Display**: Upscale Latent
- **Category**: latent
- **Inputs (required)**: samples (LATENT) | upscale_method (COMBO: nearest-exact/bilinear/area/bicubic/bislerp) | width (INT, default=512) | height (INT, default=512) | crop (COMBO: disabled/center)
- **Outputs**: LATENT [0]
- **Function**: upscale

### LatentUpscaleBy
- **Display**: Upscale Latent By
- **Category**: latent
- **Inputs (required)**: samples (LATENT) | upscale_method (COMBO) | scale_by (FLOAT, default=1.5, min=0.01, max=8.0)
- **Outputs**: LATENT [0]
- **Function**: upscale

### LatentFromBatch
- **Display**: Latent From Batch
- **Category**: latent/batch
- **Inputs (required)**: samples (LATENT) | batch_index (INT, default=0, min=0, max=63) | length (INT, default=1, min=1, max=64)
- **Outputs**: LATENT [0]
- **Function**: frombatch

### RepeatLatentBatch
- **Display**: Repeat Latent Batch
- **Category**: latent/batch
- **Inputs (required)**: samples (LATENT) | amount (INT, default=1, min=1, max=64)
- **Outputs**: LATENT [0]
- **Function**: repeat

### LatentComposite
- **Display**: Latent Composite
- **Category**: latent
- **Inputs (required)**: samples_to (LATENT) | samples_from (LATENT) | x (INT, default=0, step=8) | y (INT, default=0, step=8) | feather (INT, default=0, step=8)
- **Outputs**: LATENT [0]
- **Function**: composite

### LatentBlend
- **Display**: Latent Blend
- **Category**: _for_testing
- **Inputs (required)**: samples1 (LATENT) | samples2 (LATENT) | blend_factor (FLOAT, default=0.5, min=0, max=1)
- **Outputs**: LATENT [0]
- **Function**: blend

### LatentRotate
- **Display**: Rotate Latent
- **Category**: latent/transform
- **Inputs (required)**: samples (LATENT) | rotation (COMBO: none/90 degrees/180 degrees/270 degrees)
- **Outputs**: LATENT [0]
- **Function**: rotate

### LatentFlip
- **Display**: Flip Latent
- **Category**: latent/transform
- **Inputs (required)**: samples (LATENT) | flip_method (COMBO: x-axis: vertically/y-axis: horizontally)
- **Outputs**: LATENT [0]
- **Function**: flip

### LatentCrop
- **Display**: Crop Latent
- **Category**: latent/transform
- **Inputs (required)**: samples (LATENT) | width (INT, default=512, min=64, step=8) | height (INT, default=512, min=64, step=8) | x (INT, default=0, step=8) | y (INT, default=0, step=8)
- **Outputs**: LATENT [0]
- **Function**: crop

### SaveLatent
- **Display**: SaveLatent
- **Category**: _for_testing
- **Inputs (required)**: samples (LATENT) | filename_prefix (STRING, default="latents/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: save

### LoadLatent
- **Display**: LoadLatent
- **Category**: _for_testing
- **Inputs (required)**: latent (COMBO)
- **Outputs**: LATENT [0]
- **Function**: load

### LatentAdd
- **Display**: LatentAdd
- **Category**: latent/advanced
- **Inputs (required)**: samples1 (LATENT) | samples2 (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute

### LatentSubtract
- **Display**: LatentSubtract
- **Category**: latent/advanced
- **Inputs (required)**: samples1 (LATENT) | samples2 (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute

### LatentMultiply
- **Display**: LatentMultiply
- **Category**: latent/advanced
- **Inputs (required)**: samples (LATENT) | multiplier (FLOAT, default=1.0, min=-10.0, max=10.0)
- **Outputs**: LATENT [0]
- **Function**: execute

### LatentInterpolate
- **Display**: LatentInterpolate
- **Category**: latent/advanced
- **Inputs (required)**: samples1 (LATENT) | samples2 (LATENT) | ratio (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: LATENT [0]
- **Function**: execute

### LatentConcat
- **Display**: LatentConcat
- **Category**: latent/advanced
- **Inputs (required)**: samples1 (LATENT) | samples2 (LATENT) | dim (COMBO: x/-x/y/-y/t/-t)
- **Outputs**: LATENT [0]
- **Function**: execute

### LatentCut
- **Display**: LatentCut
- **Category**: latent/advanced
- **Inputs (required)**: samples (LATENT) | dim (COMBO: x/y/t) | index (INT, default=0) | amount (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### LatentCutToBatch
- **Display**: LatentCutToBatch
- **Category**: latent/advanced
- **Inputs (required)**: samples (LATENT) | dim (COMBO: t/x/y) | slice_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### LatentBatch
- **Display**: LatentBatch
- **Category**: latent/batch
- **Inputs (required)**: samples1 (LATENT) | samples2 (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute
- **Notes**: Deprecated

### LatentBatchSeedBehavior
- **Display**: LatentBatchSeedBehavior
- **Category**: latent/advanced
- **Inputs (required)**: samples (LATENT) | seed_behavior (COMBO: random/fixed, default=fixed)
- **Outputs**: LATENT [0]
- **Function**: execute

### LatentApplyOperation
- **Display**: LatentApplyOperation
- **Category**: latent/advanced/operations
- **Inputs (required)**: samples (LATENT) | operation (LATENT_OPERATION)
- **Outputs**: LATENT [0]
- **Function**: execute
- **Notes**: Experimental

### LatentApplyOperationCFG
- **Display**: LatentApplyOperationCFG
- **Category**: latent/advanced/operations
- **Inputs (required)**: model (MODEL) | operation (LATENT_OPERATION)
- **Outputs**: MODEL [0]
- **Function**: execute
- **Notes**: Experimental

### LatentOperationTonemapReinhard
- **Display**: LatentOperationTonemapReinhard
- **Category**: latent/advanced/operations
- **Inputs (required)**: multiplier (FLOAT, default=1.0, min=0.0, max=100.0)
- **Outputs**: LATENT_OPERATION [0]
- **Function**: execute
- **Notes**: Experimental

### LatentOperationSharpen
- **Display**: LatentOperationSharpen
- **Category**: latent/advanced/operations
- **Inputs (required)**: sharpen_radius (INT, default=9) | sigma (FLOAT, default=1.0) | alpha (FLOAT, default=0.1)
- **Outputs**: LATENT_OPERATION [0]
- **Function**: execute
- **Notes**: Experimental

### LatentCompositeMasked
- **Display**: LatentCompositeMasked
- **Category**: latent
- **Inputs (required)**: destination (LATENT) | source (LATENT) | x (INT, default=0, step=8) | y (INT, default=0, step=8) | resize_source (BOOLEAN, default=False)
- **Inputs (optional)**: mask (MASK)
- **Outputs**: LATENT [0]
- **Function**: execute

### ReplaceVideoLatentFrames
- **Display**: ReplaceVideoLatentFrames
- **Category**: latent/batch
- **Inputs (required)**: destination (LATENT) | index (INT, default=0)
- **Inputs (optional)**: source (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute

### BatchLatentsNode
- **Display**: Batch Latents
- **Category**: latent
- **Inputs (required)**: latents (AUTOGROW, min=2 LATENT inputs)
- **Outputs**: LATENT [0]
- **Function**: execute

### RebatchLatents
- **Display**: RebatchLatents
- **Category**: latent/batch
- **Inputs (required)**: latents (LATENT) | batch_size (INT, default=1, min=1, max=4096)
- **Outputs**: LATENT [0]
- **Function**: execute

### ReferenceLatent
- **Display**: ReferenceLatent
- **Category**: latent
- **Inputs (required)**: model (MODEL) | reference (LATENT) | latent (LATENT)
- **Outputs**: MODEL [0], LATENT [1]
- **Function**: execute

---
