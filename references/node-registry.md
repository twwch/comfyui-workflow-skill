# ComfyUI Built-in Node Registry

Complete registry of ComfyUI built-in nodes extracted from source code.

**Format**: For each node: class name, display name, category, inputs (required/optional), outputs, function name, and notes.

---

## 1. Loaders

### CheckpointLoaderSimple
- **Display**: Load Checkpoint
- **Category**: loaders
- **Inputs (required)**: ckpt_name (COMBO)
- **Outputs**: MODEL [0], CLIP [1], VAE [2]
- **Function**: load_checkpoint

### CheckpointLoader
- **Display**: Load Checkpoint With Config (DEPRECATED)
- **Category**: advanced/loaders
- **Inputs (required)**: config_name (COMBO) | ckpt_name (COMBO)
- **Outputs**: MODEL [0], CLIP [1], VAE [2]
- **Function**: load_checkpoint
- **Notes**: Deprecated

### unCLIPCheckpointLoader
- **Display**: unCLIPCheckpointLoader
- **Category**: loaders
- **Inputs (required)**: ckpt_name (COMBO)
- **Outputs**: MODEL [0], CLIP [1], VAE [2], CLIP_VISION [3]
- **Function**: load_checkpoint

### DiffusersLoader
- **Display**: DiffusersLoader
- **Category**: advanced/loaders/deprecated
- **Inputs (required)**: model_path (COMBO)
- **Outputs**: MODEL [0], CLIP [1], VAE [2]
- **Function**: load_checkpoint

### VAELoader
- **Display**: Load VAE
- **Category**: loaders
- **Inputs (required)**: vae_name (COMBO)
- **Outputs**: VAE [0]
- **Function**: load_vae

### LoraLoader
- **Display**: Load LoRA (Model and CLIP)
- **Category**: loaders
- **Inputs (required)**: model (MODEL) | clip (CLIP) | lora_name (COMBO) | strength_model (FLOAT, default=1.0, min=-100.0, max=100.0) | strength_clip (FLOAT, default=1.0, min=-100.0, max=100.0)
- **Outputs**: MODEL [0], CLIP [1]
- **Function**: load_lora

### LoraLoaderModelOnly
- **Display**: Load LoRA
- **Category**: loaders
- **Inputs (required)**: model (MODEL) | lora_name (COMBO) | strength_model (FLOAT, default=1.0, min=-100.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: load_lora_model_only

### CLIPLoader
- **Display**: Load CLIP
- **Category**: advanced/loaders
- **Inputs (required)**: clip_name (COMBO) | type (COMBO: stable_diffusion/stable_cascade/sd3/stable_audio/mochi/ltxv/pixart/cosmos/lumina2/wan/hidream/chroma/ace/omnigen2/qwen_image/hunyuan_image/flux2/ovis/longcat_image)
- **Inputs (optional)**: device (COMBO: default/cpu)
- **Outputs**: CLIP [0]
- **Function**: load_clip

### DualCLIPLoader
- **Display**: DualCLIPLoader
- **Category**: advanced/loaders
- **Inputs (required)**: clip_name1 (COMBO) | clip_name2 (COMBO) | type (COMBO: sdxl/sd3/flux/hunyuan_video/hidream/hunyuan_image/hunyuan_video_15/kandinsky5/kandinsky5_image/ltxv/newbie/ace)
- **Inputs (optional)**: device (COMBO: default/cpu)
- **Outputs**: CLIP [0]
- **Function**: load_clip

### TripleCLIPLoader
- **Display**: TripleCLIPLoader
- **Category**: advanced/loaders
- **Inputs (required)**: clip_name1 (COMBO) | clip_name2 (COMBO) | clip_name3 (COMBO)
- **Outputs**: CLIP [0]
- **Function**: execute
- **Notes**: SD3 recipe: clip-l, clip-g, t5

### UNETLoader
- **Display**: Load Diffusion Model
- **Category**: advanced/loaders
- **Inputs (required)**: unet_name (COMBO) | weight_dtype (COMBO: default/fp8_e4m3fn/fp8_e4m3fn_fast/fp8_e5m2)
- **Outputs**: MODEL [0]
- **Function**: load_unet

### CLIPVisionLoader
- **Display**: Load CLIP Vision
- **Category**: loaders
- **Inputs (required)**: clip_name (COMBO)
- **Outputs**: CLIP_VISION [0]
- **Function**: load_clip

### ControlNetLoader
- **Display**: Load ControlNet Model
- **Category**: loaders
- **Inputs (required)**: control_net_name (COMBO)
- **Outputs**: CONTROL_NET [0]
- **Function**: load_controlnet

### DiffControlNetLoader
- **Display**: Load ControlNet Model (diff)
- **Category**: loaders
- **Inputs (required)**: model (MODEL) | control_net_name (COMBO)
- **Outputs**: CONTROL_NET [0]
- **Function**: load_controlnet

### StyleModelLoader
- **Display**: Load Style Model
- **Category**: loaders
- **Inputs (required)**: style_model_name (COMBO)
- **Outputs**: STYLE_MODEL [0]
- **Function**: load_style_model

### GLIGENLoader
- **Display**: GLIGENLoader
- **Category**: loaders
- **Inputs (required)**: gligen_name (COMBO)
- **Outputs**: GLIGEN [0]
- **Function**: load_gligen

### ImageOnlyCheckpointLoader
- **Display**: Image Only Checkpoint Loader (img2vid model)
- **Category**: loaders/video_models
- **Inputs (required)**: ckpt_name (COMBO)
- **Outputs**: MODEL [0], CLIP_VISION [1], VAE [2]
- **Function**: load_checkpoint

### UpscaleModelLoader
- **Display**: Load Upscale Model
- **Category**: loaders
- **Inputs (required)**: model_name (COMBO)
- **Outputs**: UPSCALE_MODEL [0]
- **Function**: execute

### LatentUpscaleModelLoader
- **Display**: Load Latent Upscale Model
- **Category**: loaders
- **Inputs (required)**: model_name (COMBO)
- **Outputs**: LATENT_UPSCALE_MODEL [0]
- **Function**: execute

---

## 2. Conditioning

### CLIPTextEncode
- **Display**: CLIP Text Encode (Prompt)
- **Category**: conditioning
- **Inputs (required)**: text (STRING, multiline) | clip (CLIP)
- **Outputs**: CONDITIONING [0]
- **Function**: encode

### CLIPSetLastLayer
- **Display**: CLIP Set Last Layer
- **Category**: conditioning
- **Inputs (required)**: clip (CLIP) | stop_at_clip_layer (INT, default=-1, min=-24, max=-1)
- **Outputs**: CLIP [0]
- **Function**: set_last_layer

### CLIPVisionEncode
- **Display**: CLIP Vision Encode
- **Category**: conditioning
- **Inputs (required)**: clip_vision (CLIP_VISION) | image (IMAGE) | crop (COMBO: center/none)
- **Outputs**: CLIP_VISION_OUTPUT [0]
- **Function**: encode

### ConditioningCombine
- **Display**: Conditioning (Combine)
- **Category**: conditioning
- **Inputs (required)**: conditioning_1 (CONDITIONING) | conditioning_2 (CONDITIONING)
- **Outputs**: CONDITIONING [0]
- **Function**: combine

### ConditioningAverage
- **Display**: Conditioning (Average)
- **Category**: conditioning
- **Inputs (required)**: conditioning_to (CONDITIONING) | conditioning_from (CONDITIONING) | conditioning_to_strength (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: CONDITIONING [0]
- **Function**: addWeighted

### ConditioningConcat
- **Display**: Conditioning (Concat)
- **Category**: conditioning
- **Inputs (required)**: conditioning_to (CONDITIONING) | conditioning_from (CONDITIONING)
- **Outputs**: CONDITIONING [0]
- **Function**: concat

### ConditioningSetArea
- **Display**: Conditioning (Set Area)
- **Category**: conditioning
- **Inputs (required)**: conditioning (CONDITIONING) | width (INT, default=64, min=64, max=16384, step=8) | height (INT, default=64, min=64, max=16384, step=8) | x (INT, default=0) | y (INT, default=0) | strength (FLOAT, default=1.0, min=0.0, max=10.0)
- **Outputs**: CONDITIONING [0]
- **Function**: append

### ConditioningSetAreaPercentage
- **Display**: Conditioning (Set Area with Percentage)
- **Category**: conditioning
- **Inputs (required)**: conditioning (CONDITIONING) | width (FLOAT, default=1.0, max=1.0) | height (FLOAT, default=1.0, max=1.0) | x (FLOAT, default=0, max=1.0) | y (FLOAT, default=0, max=1.0) | strength (FLOAT, default=1.0, max=10.0)
- **Outputs**: CONDITIONING [0]
- **Function**: append

### ConditioningSetAreaStrength
- **Display**: ConditioningSetAreaStrength
- **Category**: conditioning
- **Inputs (required)**: conditioning (CONDITIONING) | strength (FLOAT, default=1.0, min=0.0, max=10.0)
- **Outputs**: CONDITIONING [0]
- **Function**: append

### ConditioningSetMask
- **Display**: Conditioning (Set Mask)
- **Category**: conditioning
- **Inputs (required)**: conditioning (CONDITIONING) | mask (MASK) | strength (FLOAT, default=1.0, min=0.0, max=10.0) | set_cond_area (COMBO: default/mask bounds)
- **Outputs**: CONDITIONING [0]
- **Function**: append

### ConditioningZeroOut
- **Display**: ConditioningZeroOut
- **Category**: advanced/conditioning
- **Inputs (required)**: conditioning (CONDITIONING)
- **Outputs**: CONDITIONING [0]
- **Function**: zero_out

### ConditioningSetTimestepRange
- **Display**: ConditioningSetTimestepRange
- **Category**: advanced/conditioning
- **Inputs (required)**: conditioning (CONDITIONING) | start (FLOAT, default=0.0, min=0.0, max=1.0) | end (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: CONDITIONING [0]
- **Function**: set_range

### StyleModelApply
- **Display**: Apply Style Model
- **Category**: conditioning/style_model
- **Inputs (required)**: conditioning (CONDITIONING) | style_model (STYLE_MODEL) | clip_vision_output (CLIP_VISION_OUTPUT) | strength (FLOAT, default=1.0, min=0.0, max=10.0) | strength_type (COMBO: multiply/attn_bias)
- **Outputs**: CONDITIONING [0]
- **Function**: apply_stylemodel

### unCLIPConditioning
- **Display**: unCLIPConditioning
- **Category**: conditioning
- **Inputs (required)**: conditioning (CONDITIONING) | clip_vision_output (CLIP_VISION_OUTPUT) | strength (FLOAT, default=1.0, min=-10.0, max=10.0) | noise_augmentation (FLOAT, default=0.0, min=0.0, max=1.0)
- **Outputs**: CONDITIONING [0]
- **Function**: apply_adm

### GLIGENTextBoxApply
- **Display**: GLIGENTextBoxApply
- **Category**: conditioning/gligen
- **Inputs (required)**: conditioning_to (CONDITIONING) | clip (CLIP) | gligen_textbox_model (GLIGEN) | text (STRING, multiline) | width (INT, default=64) | height (INT, default=64) | x (INT, default=0) | y (INT, default=0)
- **Outputs**: CONDITIONING [0]
- **Function**: append

### InpaintModelConditioning
- **Display**: InpaintModelConditioning
- **Category**: conditioning/inpaint
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | pixels (IMAGE) | mask (MASK) | noise_mask (BOOLEAN, default=True)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: encode

### ConditioningSetAreaPercentageVideo
- **Display**: ConditioningSetAreaPercentageVideo
- **Category**: conditioning
- **Inputs (required)**: conditioning (CONDITIONING) | width (FLOAT) | height (FLOAT) | temporal (FLOAT) | x (FLOAT) | y (FLOAT) | z (FLOAT) | strength (FLOAT, default=1.0)
- **Outputs**: CONDITIONING [0]
- **Function**: append

---

## 3. Sampling

### KSampler
- **Display**: KSampler
- **Category**: sampling
- **Inputs (required)**: model (MODEL) | seed (INT) | steps (INT, default=20) | cfg (FLOAT, default=8.0) | sampler_name (COMBO) | scheduler (COMBO) | positive (CONDITIONING) | negative (CONDITIONING) | latent_image (LATENT) | denoise (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: LATENT [0]
- **Function**: sample

### KSamplerAdvanced
- **Display**: KSampler (Advanced)
- **Category**: sampling
- **Inputs (required)**: model (MODEL) | add_noise (COMBO: enable/disable) | noise_seed (INT) | steps (INT, default=20) | cfg (FLOAT, default=8.0) | sampler_name (COMBO) | scheduler (COMBO) | positive (CONDITIONING) | negative (CONDITIONING) | latent_image (LATENT) | start_at_step (INT, default=0) | end_at_step (INT, default=10000) | return_with_leftover_noise (COMBO: disable/enable)
- **Outputs**: LATENT [0]
- **Function**: sample

---

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

---

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

---

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

---

## 7. Video / Wan Nodes

### WanImageToVideo
- **Display**: WanImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832, step=16) | height (INT, default=480, step=16) | length (INT, default=81, step=4) | batch_size (INT, default=1)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT) | start_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### WanFunControlToVideo
- **Display**: WanFunControlToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | batch_size (INT, default=1)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT) | start_image (IMAGE) | control_video (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### Wan22FunControlToVideo
- **Display**: Wan22FunControlToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | batch_size (INT, default=1)
- **Inputs (optional)**: ref_image (IMAGE) | control_video (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### WanFirstLastFrameToVideo
- **Display**: WanFirstLastFrameToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | batch_size (INT, default=1)
- **Inputs (optional)**: clip_vision_start_image (CLIP_VISION_OUTPUT) | clip_vision_end_image (CLIP_VISION_OUTPUT) | start_image (IMAGE) | end_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### WanFunInpaintToVideo
- **Display**: WanFunInpaintToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | batch_size (INT, default=1)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT) | start_image (IMAGE) | end_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### WanVaceToVideo
- **Display**: WanVaceToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | batch_size (INT, default=1) | strength (FLOAT, default=1.0)
- **Inputs (optional)**: control_video (IMAGE) | control_masks (MASK) | reference_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2], INT [3] (trim_latent)
- **Function**: execute

### TrimVideoLatent
- **Display**: TrimVideoLatent
- **Category**: latent/video
- **Inputs (required)**: samples (LATENT) | trim_amount (INT, default=0, min=0, max=99999)
- **Outputs**: LATENT [0]
- **Function**: execute

### WanCameraImageToVideo
- **Display**: WanCameraImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | batch_size (INT, default=1)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT) | start_image (IMAGE) | camera_conditions (WAN_CAMERA_EMBEDDING)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### WanPhantomSubjectToVideo
- **Display**: WanPhantomSubjectToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | batch_size (INT, default=1)
- **Inputs (optional)**: images (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative_text), CONDITIONING [2] (negative_img_text), LATENT [3]
- **Function**: execute

### WanTrackToVideo
- **Display**: WanTrackToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | tracks (STRING, multiline, default="[]") | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | batch_size (INT, default=1) | temperature (FLOAT, default=220.0) | topk (INT, default=2) | start_image (IMAGE)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### WanSoundImageToVideo
- **Display**: WanSoundImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=77) | batch_size (INT, default=1)
- **Inputs (optional)**: audio_encoder_output (AUDIO_ENCODER_OUTPUT) | ref_image (IMAGE) | control_video (IMAGE) | ref_motion (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### WanSoundImageToVideoExtend
- **Display**: WanSoundImageToVideoExtend
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | length (INT, default=77) | video_latent (LATENT)
- **Inputs (optional)**: audio_encoder_output (AUDIO_ENCODER_OUTPUT) | ref_image (IMAGE) | control_video (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### WanHuMoImageToVideo
- **Display**: WanHuMoImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=97) | batch_size (INT, default=1)
- **Inputs (optional)**: audio_encoder_output (AUDIO_ENCODER_OUTPUT) | ref_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute
- **Notes**: Experimental

### WanAnimateToVideo
- **Display**: WanAnimateToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=77) | batch_size (INT, default=1) | continue_motion_max_frames (INT, default=5) | video_frame_offset (INT, default=0)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT) | reference_image (IMAGE) | face_video (IMAGE) | pose_video (IMAGE) | background_video (IMAGE) | character_mask (MASK) | continue_motion (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2], INT [3] (trim_latent), INT [4] (trim_image), INT [5] (video_frame_offset)
- **Function**: execute
- **Notes**: Experimental

### Wan22ImageToVideoLatent
- **Display**: Wan22ImageToVideoLatent
- **Category**: conditioning/inpaint
- **Inputs (required)**: vae (VAE) | width (INT, default=1280, step=32) | height (INT, default=704, step=32) | length (INT, default=49) | batch_size (INT, default=1)
- **Inputs (optional)**: start_image (IMAGE)
- **Outputs**: LATENT [0]
- **Function**: execute

### WanInfiniteTalkToVideo
- **Display**: WanInfiniteTalkToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: mode (DYNAMIC_COMBO: single_speaker/two_speakers) | model (MODEL) | model_patch (MODEL_PATCH) | positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=832) | height (INT, default=480) | length (INT, default=81) | audio_encoder_output_1 (AUDIO_ENCODER_OUTPUT) | motion_frame_count (INT, default=9) | audio_scale (FLOAT, default=1.0)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT) | start_image (IMAGE) | previous_frames (IMAGE)
- **Outputs**: MODEL [0], CONDITIONING [1] (positive), CONDITIONING [2] (negative), LATENT [3], INT [4] (trim_image)
- **Function**: execute

### WanSCAILToVideo
- **Display**: WanSCAILToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=512, step=32) | height (INT, default=896, step=32) | length (INT, default=81) | batch_size (INT, default=1) | pose_strength (FLOAT, default=1.0) | pose_start (FLOAT, default=0.0) | pose_end (FLOAT, default=1.0)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT) | reference_image (IMAGE) | pose_video (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute
- **Notes**: Experimental

### SVD_img2vid_Conditioning
- **Display**: SVD_img2vid_Conditioning
- **Category**: conditioning/video_models
- **Inputs (required)**: clip_vision (CLIP_VISION) | init_image (IMAGE) | vae (VAE) | width (INT, default=1024, step=8) | height (INT, default=576, step=8) | video_frames (INT, default=14) | motion_bucket_id (INT, default=127) | fps (INT, default=6) | augmentation_level (FLOAT, default=0.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: encode

### VideoLinearCFGGuidance
- **Display**: VideoLinearCFGGuidance
- **Category**: sampling/video_models
- **Inputs (required)**: model (MODEL) | min_cfg (FLOAT, default=1.0, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: patch

### VideoTriangleCFGGuidance
- **Display**: VideoTriangleCFGGuidance
- **Category**: sampling/video_models
- **Inputs (required)**: model (MODEL) | min_cfg (FLOAT, default=1.0, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: patch

### ImageOnlyCheckpointSave
- **Display**: ImageOnlyCheckpointSave
- **Category**: advanced/model_merging
- **Inputs (required)**: model (MODEL) | clip_vision (CLIP_VISION) | vae (VAE) | filename_prefix (STRING, default="checkpoints/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: save

---

## 8. Video I/O Nodes

### SaveWEBM
- **Display**: SaveWEBM
- **Category**: image/video
- **Inputs (required)**: images (IMAGE) | filename_prefix (STRING) | codec (COMBO: vp9/av1) | fps (FLOAT, default=24.0) | crf (FLOAT, default=32.0)
- **Outputs**: (none - output node)
- **Function**: execute
- **Notes**: Experimental

### SaveVideo
- **Display**: Save Video
- **Category**: image/video
- **Inputs (required)**: video (VIDEO) | filename_prefix (STRING, default="video/ComfyUI") | format (COMBO) | codec (COMBO)
- **Outputs**: (none - output node)
- **Function**: execute

### CreateVideo
- **Display**: Create Video
- **Category**: image/video
- **Inputs (required)**: images (IMAGE) | fps (FLOAT, default=30.0)
- **Inputs (optional)**: audio (AUDIO)
- **Outputs**: VIDEO [0]
- **Function**: execute

### GetVideoComponents
- **Display**: Get Video Components
- **Category**: image/video
- **Inputs (required)**: video (VIDEO)
- **Outputs**: IMAGE [0] (images), AUDIO [1] (audio), FLOAT [2] (fps)
- **Function**: execute

### LoadVideo
- **Display**: Load Video
- **Category**: image/video
- **Inputs (required)**: file (COMBO, video upload)
- **Outputs**: VIDEO [0]
- **Function**: execute

### Video Slice
- **Display**: Video Slice
- **Category**: image/video
- **Inputs (required)**: video (VIDEO) | start_time (FLOAT, default=0.0) | duration (FLOAT, default=0.0) | strict_duration (BOOLEAN, default=False)
- **Outputs**: VIDEO [0]
- **Function**: execute

---

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

## 11. SD3 Nodes

### CLIPTextEncodeSD3
- **Display**: CLIPTextEncodeSD3
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | clip_l (STRING, multiline) | clip_g (STRING, multiline) | t5xxl (STRING, multiline) | empty_padding (COMBO: none/empty_prompt)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### EmptySD3LatentImage
- **Display**: EmptySD3LatentImage
- **Category**: latent/sd3
- **Inputs (required)**: width (INT, default=1024, step=16) | height (INT, default=1024, step=16) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### ControlNetApplySD3
- **Display**: Apply Controlnet with VAE
- **Category**: conditioning/controlnet
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | control_net (CONTROL_NET) | vae (VAE) | image (IMAGE) | strength (FLOAT, default=1.0) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=1.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute
- **Notes**: Deprecated

### SkipLayerGuidanceSD3
- **Display**: SkipLayerGuidanceSD3
- **Category**: advanced/guidance
- **Inputs (required)**: model (MODEL) | layers (STRING, default="7, 8, 9") | scale (FLOAT, default=3.0) | start_percent (FLOAT, default=0.01) | end_percent (FLOAT, default=0.15)
- **Outputs**: MODEL [0]
- **Function**: execute
- **Notes**: Experimental. Generic SkipLayerGuidance for DiT models.

---

## 12. HunyuanVideo Nodes

### CLIPTextEncodeHunyuanDiT
- **Display**: CLIPTextEncodeHunyuanDiT
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | bert (STRING, multiline) | mt5xl (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### TextEncodeHunyuanVideo_ImageToVideo
- **Display**: TextEncodeHunyuanVideo_ImageToVideo
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | clip_vision_output (CLIP_VISION_OUTPUT) | prompt (STRING, multiline) | image_interleave (INT, default=2, min=1, max=512)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### EmptyHunyuanLatentVideo
- **Display**: Empty HunyuanVideo 1.0 Latent
- **Category**: latent/video
- **Inputs (required)**: width (INT, default=848, step=16) | height (INT, default=480, step=16) | length (INT, default=25, step=4) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### EmptyHunyuanVideo15Latent
- **Display**: Empty HunyuanVideo 1.5 Latent
- **Category**: latent/video
- **Inputs (required)**: width (INT, default=848, step=16) | height (INT, default=480, step=16) | length (INT, default=25, step=4) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute
- **Notes**: Uses 32 latent channels and scale factor 16

### HunyuanVideo15ImageToVideo
- **Display**: HunyuanVideo15ImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT, default=848) | height (INT, default=480) | length (INT, default=33) | batch_size (INT, default=1)
- **Inputs (optional)**: start_image (IMAGE) | clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### HunyuanVideo15SuperResolution
- **Display**: HunyuanVideo15SuperResolution
- **Category**: (default)
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | latent (LATENT) | noise_augmentation (FLOAT, default=0.70)
- **Inputs (optional)**: vae (VAE) | start_image (IMAGE) | clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### HunyuanVideo15LatentUpscaleWithModel
- **Display**: Hunyuan Video 15 Latent Upscale With Model
- **Category**: latent
- **Inputs (required)**: model (LATENT_UPSCALE_MODEL) | samples (LATENT) | upscale_method (COMBO) | width (INT, default=1280) | height (INT, default=720) | crop (COMBO: disabled/center)
- **Outputs**: LATENT [0]
- **Function**: execute

### HunyuanImageToVideo
- **Display**: HunyuanImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | vae (VAE) | width (INT, default=848) | height (INT, default=480) | length (INT, default=53) | batch_size (INT, default=1) | guidance_type (COMBO: v1 (concat)/v2 (replace)/custom)
- **Inputs (optional)**: start_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), LATENT [1]
- **Function**: execute

### EmptyHunyuanImageLatent
- **Display**: EmptyHunyuanImageLatent
- **Category**: latent
- **Inputs (required)**: width (INT, default=2048, step=32) | height (INT, default=2048, step=32) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### HunyuanRefinerLatent
- **Display**: HunyuanRefinerLatent
- **Category**: (default)
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | latent (LATENT) | noise_augmentation (FLOAT, default=0.10)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

---

## 13. Upscale Nodes

### ImageUpscaleWithModel
- **Display**: Upscale Image (using Model)
- **Category**: image/upscaling
- **Inputs (required)**: upscale_model (UPSCALE_MODEL) | image (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ImageScaleToTotalPixels
- **Display**: Scale Image to Total Pixels
- **Category**: image/upscaling
- **Inputs (required)**: image (IMAGE) | upscale_method (COMBO: nearest-exact/bilinear/area/bicubic/lanczos) | megapixels (FLOAT, default=1.0, min=0.01, max=16.0) | resolution_steps (INT, default=1, min=1, max=256)
- **Outputs**: IMAGE [0]
- **Function**: execute

### ResizeImageMaskNode
- **Display**: Resize Image/Mask
- **Category**: transform
- **Inputs (required)**: input (IMAGE or MASK) | resize_type (DYNAMIC_COMBO: scale dimensions/scale by multiplier/scale longer dimension/scale shorter dimension/scale width/scale height/scale total pixels/match size/scale to multiple) | scale_method (COMBO: nearest-exact/bilinear/area/bicubic/lanczos)
- **Outputs**: IMAGE or MASK [0] (matches input type)
- **Function**: execute

---

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

---

## 15. Custom Samplers & Schedulers

### SamplerCustom
- **Display**: SamplerCustom
- **Category**: sampling/custom_sampling
- **Inputs (required)**: model (MODEL) | add_noise (BOOLEAN, default=True) | noise_seed (INT) | cfg (FLOAT, default=8.0) | positive (CONDITIONING) | negative (CONDITIONING) | sampler (SAMPLER) | sigmas (SIGMAS) | latent_image (LATENT)
- **Outputs**: LATENT [0] (output), LATENT [1] (denoised_output)
- **Function**: execute

### SamplerCustomAdvanced
- **Display**: SamplerCustomAdvanced
- **Category**: sampling/custom_sampling
- **Inputs (required)**: noise (NOISE) | guider (GUIDER) | sampler (SAMPLER) | sigmas (SIGMAS) | latent_image (LATENT)
- **Outputs**: LATENT [0] (output), LATENT [1] (denoised_output)
- **Function**: execute

### BasicScheduler
- **Display**: BasicScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model (MODEL) | scheduler (COMBO) | steps (INT, default=20) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### KarrasScheduler
- **Display**: KarrasScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | sigma_max (FLOAT, default=14.614642) | sigma_min (FLOAT, default=0.0291675) | rho (FLOAT, default=7.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### ExponentialScheduler
- **Display**: ExponentialScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | sigma_max (FLOAT, default=14.614642) | sigma_min (FLOAT, default=0.0291675)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### PolyexponentialScheduler
- **Display**: PolyexponentialScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | sigma_max (FLOAT, default=14.614642) | sigma_min (FLOAT, default=0.0291675) | rho (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### LaplaceScheduler
- **Display**: LaplaceScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | sigma_max (FLOAT) | sigma_min (FLOAT) | mu (FLOAT, default=0.0) | beta (FLOAT, default=0.5)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### SDTurboScheduler
- **Display**: SDTurboScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model (MODEL) | steps (INT, default=1, min=1, max=10) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### BetaSamplingScheduler
- **Display**: BetaSamplingScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model (MODEL) | steps (INT, default=20) | alpha (FLOAT, default=0.6) | beta (FLOAT, default=0.6)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### VPScheduler
- **Display**: VPScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | beta_d (FLOAT, default=19.9) | beta_min (FLOAT, default=0.1) | eps_s (FLOAT, default=0.001)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### KSamplerSelect
- **Display**: KSamplerSelect
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: sampler_name (COMBO)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMPP_3M_SDE
- **Display**: SamplerDPMPP_3M_SDE
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0) | noise_device (COMBO: gpu/cpu)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMPP_2M_SDE
- **Display**: SamplerDPMPP_2M_SDE
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: solver_type (COMBO: midpoint/heun) | eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0) | noise_device (COMBO: gpu/cpu)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMPP_SDE
- **Display**: SamplerDPMPP_SDE
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0) | r (FLOAT, default=0.5) | noise_device (COMBO: gpu/cpu)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMPP_2S_Ancestral
- **Display**: SamplerDPMPP_2S_Ancestral
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerEulerAncestral
- **Display**: SamplerEulerAncestral
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerEulerAncestralCFGPP
- **Display**: SamplerEulerAncestralCFG++
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0, max=1.0) | s_noise (FLOAT, default=1.0, max=10.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerLMS
- **Display**: SamplerLMS
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: order (INT, default=4, min=1, max=100)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMAdaptative
- **Display**: SamplerDPMAdaptative
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: order (INT, default=3) | rtol (FLOAT, default=0.05) | atol (FLOAT, default=0.0078) | h_init (FLOAT, default=0.05) | pcoeff (FLOAT, default=0.0) | icoeff (FLOAT, default=1.0) | dcoeff (FLOAT, default=0.0) | accept_safety (FLOAT, default=0.81) | eta (FLOAT, default=0.0) | s_noise (FLOAT, default=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerER_SDE
- **Display**: SamplerER_SDE
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: solver_type (COMBO: ER-SDE/Reverse-time SDE/ODE) | max_stage (INT, default=3, min=1, max=3) | eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerSASolver
- **Display**: SamplerSASolver
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: model (MODEL) | eta (FLOAT, default=1.0) | sde_start_percent (FLOAT, default=0.2) | sde_end_percent (FLOAT, default=0.8) | s_noise (FLOAT, default=1.0) | predictor_order (INT, default=3) | corrector_order (INT, default=4) | use_pece (BOOLEAN) | simple_order_2 (BOOLEAN)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerSEEDS2
- **Display**: SamplerSEEDS2
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: solver_type (COMBO: phi_1/phi_2) | eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0) | r (FLOAT, default=0.5, min=0.01, max=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SplitSigmas
- **Display**: SplitSigmas
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS) | step (INT, default=0)
- **Outputs**: SIGMAS [0] (high_sigmas), SIGMAS [1] (low_sigmas)
- **Function**: execute

### SplitSigmasDenoise
- **Display**: SplitSigmasDenoise
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS) | denoise (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: SIGMAS [0] (high_sigmas), SIGMAS [1] (low_sigmas)
- **Function**: execute

### FlipSigmas
- **Display**: FlipSigmas
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### SetFirstSigma
- **Display**: SetFirstSigma
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS) | sigma (FLOAT, default=136.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### ExtendIntermediateSigmas
- **Display**: ExtendIntermediateSigmas
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS) | steps (INT, default=2) | start_at_sigma (FLOAT, default=-1.0) | end_at_sigma (FLOAT, default=12.0) | spacing (COMBO: linear/cosine/sine)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### SamplingPercentToSigma
- **Display**: SamplingPercentToSigma
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: model (MODEL) | sampling_percent (FLOAT, default=0.0) | return_actual_sigma (BOOLEAN, default=False)
- **Outputs**: FLOAT [0] (sigma_value)
- **Function**: execute

### BasicGuider
- **Display**: BasicGuider
- **Category**: sampling/custom_sampling/guiders
- **Inputs (required)**: model (MODEL) | conditioning (CONDITIONING)
- **Outputs**: GUIDER [0]
- **Function**: execute

### CFGGuider
- **Display**: CFGGuider
- **Category**: sampling/custom_sampling/guiders
- **Inputs (required)**: model (MODEL) | positive (CONDITIONING) | negative (CONDITIONING) | cfg (FLOAT, default=8.0)
- **Outputs**: GUIDER [0]
- **Function**: execute

### DualCFGGuider
- **Display**: DualCFGGuider
- **Category**: sampling/custom_sampling/guiders
- **Inputs (required)**: model (MODEL) | cond1 (CONDITIONING) | cond2 (CONDITIONING) | negative (CONDITIONING) | cfg_conds (FLOAT, default=8.0) | cfg_cond2_negative (FLOAT, default=8.0) | style (COMBO: regular/nested)
- **Outputs**: GUIDER [0]
- **Function**: execute

### DisableNoise
- **Display**: DisableNoise
- **Category**: sampling/custom_sampling/noise
- **Inputs (required)**: (none)
- **Outputs**: NOISE [0]
- **Function**: execute

### RandomNoise
- **Display**: RandomNoise
- **Category**: sampling/custom_sampling/noise
- **Inputs (required)**: noise_seed (INT)
- **Outputs**: NOISE [0]
- **Function**: execute

### AddNoise
- **Display**: AddNoise
- **Category**: _for_testing/custom_sampling/noise
- **Inputs (required)**: model (MODEL) | noise (NOISE) | sigmas (SIGMAS) | latent_image (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute
- **Notes**: Experimental

### ManualSigmas
- **Display**: ManualSigmas
- **Category**: _for_testing/custom_sampling
- **Inputs (required)**: sigmas (STRING, default="1, 0.5")
- **Outputs**: SIGMAS [0]
- **Function**: execute
- **Notes**: Experimental

---

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
