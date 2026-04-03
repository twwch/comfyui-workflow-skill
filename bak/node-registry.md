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

### QuadrupleCLIPLoader
- **Display**: QuadrupleCLIPLoader
- **Category**: advanced/loaders
- **Inputs (required)**: clip_name1 (COMBO) | clip_name2 (COMBO) | clip_name3 (COMBO) | clip_name4 (COMBO)
- **Outputs**: CLIP [0]
- **Function**: execute
- **Notes**: HiDream recipe: long clip-l, long clip-g, t5xxl, llama_8b_3.1_instruct

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

### HypernetworkLoader
- **Display**: HypernetworkLoader
- **Category**: loaders
- **Inputs (required)**: model (MODEL) | hypernetwork_name (COMBO) | strength (FLOAT, default=1.0, min=-10.0, max=10.0)
- **Outputs**: MODEL [0]
- **Function**: load_hypernetwork

### PhotoMakerLoader
- **Display**: PhotoMakerLoader
- **Category**: _for_testing
- **Inputs (required)**: photomaker_model_name (COMBO)
- **Outputs**: PHOTOMAKER [0]
- **Function**: execute

### AudioEncoderLoader
- **Display**: AudioEncoderLoader
- **Category**: loaders
- **Inputs (required)**: audio_encoder_name (COMBO)
- **Outputs**: AUDIO_ENCODER [0]
- **Function**: execute

### ModelPatchLoader
- **Display**: ModelPatchLoader
- **Category**: advanced/loaders
- **Inputs (required)**: model_patch_name (COMBO)
- **Outputs**: MODEL_PATCH [0]
- **Function**: execute

### LTXAVTextEncoderLoader
- **Display**: LTXV Audio Text Encoder Loader
- **Category**: advanced/loaders
- **Inputs (required)**: text_encoder (COMBO) | ckpt_name (COMBO)
- **Inputs (optional)**: device (COMBO: default/cpu)
- **Outputs**: CLIP [0]
- **Function**: execute

### LTXVAudioVAELoader
- **Display**: LTXV Audio VAE Loader
- **Category**: audio
- **Inputs (required)**: ckpt_name (COMBO)
- **Outputs**: VAE [0]
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

### ConditioningStableAudio
- **Display**: ConditioningStableAudio
- **Category**: conditioning
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | seconds_start (FLOAT, default=0.0, min=0.0, max=1000.0) | seconds_total (FLOAT, default=47.0, min=0.0, max=1000.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute

### AudioEncoderEncode
- **Display**: AudioEncoderEncode
- **Category**: conditioning
- **Inputs (required)**: audio_encoder (AUDIO_ENCODER) | audio (AUDIO)
- **Outputs**: AUDIO_ENCODER_OUTPUT [0]
- **Function**: execute

### PhotoMakerEncode
- **Display**: PhotoMakerEncode
- **Category**: _for_testing
- **Inputs (required)**: photomaker (PHOTOMAKER) | image (IMAGE) | clip (CLIP) | text (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### CLIPTextEncodeControlnet
- **Display**: CLIPTextEncodeControlnet
- **Category**: _for_testing/conditioning
- **Inputs (required)**: clip (CLIP) | conditioning (CONDITIONING) | text (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute
- **Notes**: Experimental

### T5TokenizerOptions
- **Display**: T5TokenizerOptions
- **Category**: _for_testing/conditioning
- **Inputs (required)**: clip (CLIP) | min_padding (INT, default=0) | min_length (INT, default=0)
- **Outputs**: CLIP [0]
- **Function**: execute
- **Notes**: Experimental

### InstructPixToPixConditioning
- **Display**: InstructPixToPixConditioning
- **Category**: conditioning/instructpix2pix
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | pixels (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### LotusConditioning
- **Display**: LotusConditioning
- **Category**: conditioning
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute

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

### WanCameraEmbedding
- **Display**: WanCameraEmbedding
- **Category**: conditioning/video_models
- **Inputs (required)**: camera_pose (COMBO) | length (INT, default=81)
- **Outputs**: WAN_CAMERA_EMBEDDING [0]
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

### WanMoveVisualizeTracks
- **Display**: WanMoveVisualizeTracks
- **Category**: conditioning/video_models
- **Inputs (required)**: tracks (STRING, multiline) | image (IMAGE)
- **Outputs**: IMAGE [0]
- **Function**: execute

### WanMoveTracksFromCoords
- **Display**: WanMoveTracksFromCoords
- **Category**: conditioning/video_models
- **Inputs (required)**: coordinates (STRING, multiline)
- **Outputs**: STRING [0] (tracks)
- **Function**: execute

### GenerateTracks
- **Display**: GenerateTracks
- **Category**: conditioning/video_models
- **Inputs (required)**: width (INT) | height (INT) | length (INT) | motion_type (COMBO)
- **Outputs**: STRING [0] (tracks)
- **Function**: execute

### WanMoveConcatTrack
- **Display**: WanMoveConcatTrack
- **Category**: conditioning/video_models
- **Inputs (required)**: tracks1 (STRING, multiline) | tracks2 (STRING, multiline)
- **Outputs**: STRING [0] (tracks)
- **Function**: execute

### WanMoveTrackToVideo
- **Display**: WanMoveTrackToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | tracks (STRING) | width (INT) | height (INT) | length (INT) | batch_size (INT) | start_image (IMAGE)
- **Inputs (optional)**: clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### wanBlockSwap
- **Display**: wanBlockSwap
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | offload_blocks (INT) | offload_extra (BOOLEAN)
- **Outputs**: MODEL [0]
- **Function**: execute

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

### SkipLayerGuidanceSD3
- **Display**: SkipLayerGuidanceSD3
- **Category**: advanced/guidance
- **Inputs (required)**: model (MODEL) | layers (STRING, default="7, 8, 9") | scale (FLOAT, default=3.0) | start_percent (FLOAT, default=0.01) | end_percent (FLOAT, default=0.15)
- **Outputs**: MODEL [0]
- **Function**: execute
- **Notes**: Experimental. Generic SkipLayerGuidance for DiT models.

### SkipLayerGuidanceDiT
- **Display**: SkipLayerGuidanceDiT
- **Category**: advanced/guidance
- **Inputs (required)**: model (MODEL) | double_layers (STRING) | single_layers (STRING) | scale (FLOAT, default=3.0) | start_percent (FLOAT, default=0.01) | end_percent (FLOAT, default=0.15)
- **Outputs**: MODEL [0]
- **Function**: execute

### SkipLayerGuidanceDiTSimple
- **Display**: SkipLayerGuidanceDiTSimple
- **Category**: advanced/guidance
- **Inputs (required)**: model (MODEL) | skip_type (COMBO) | scale (FLOAT, default=3.0) | start_percent (FLOAT, default=0.01) | end_percent (FLOAT, default=0.15)
- **Outputs**: MODEL [0]
- **Function**: execute

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

### SD_4XUpscale_Conditioning
- **Display**: SD_4XUpscale_Conditioning
- **Category**: conditioning/upscale_diffusion
- **Inputs (required)**: images (IMAGE) | positive (CONDITIONING) | negative (CONDITIONING) | scale_ratio (FLOAT, default=4.0) | noise_augmentation (FLOAT, default=0.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### LTXVLatentUpsampler
- **Display**: LTXVLatentUpsampler
- **Category**: latent/video/ltxv
- **Inputs (required)**: model (MODEL) | samples (LATENT) | vae (VAE)
- **Outputs**: LATENT [0]
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

### AlignYourStepsScheduler
- **Display**: AlignYourStepsScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model_type (COMBO) | steps (INT, default=10) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### GITSScheduler
- **Display**: GITSScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: coeff (FLOAT, default=1.2) | steps (INT, default=10) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### OptimalStepsScheduler
- **Display**: OptimalStepsScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model_type (COMBO) | steps (INT, default=10) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### LTXVScheduler
- **Display**: LTXVScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | max_shift (FLOAT, default=2.05) | base_shift (FLOAT, default=0.95) | stretch (BOOLEAN, default=True) | terminal (FLOAT, default=0.1)
- **Inputs (optional)**: latent (LATENT)
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

### SamplerEulerCFGpp
- **Display**: SamplerEulerCFGpp
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: (none)
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

### SamplerLCMUpscale
- **Display**: SamplerLCMUpscale
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: scale_ratio (FLOAT, default=1.0) | scale_steps (INT, default=-1) | upscale_method (COMBO)
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

### PerpNegGuider
- **Display**: PerpNegGuider
- **Category**: sampling/custom_sampling/guiders
- **Inputs (required)**: model (MODEL) | positive (CONDITIONING) | negative (CONDITIONING) | empty_conditioning (CONDITIONING) | cfg (FLOAT, default=8.0) | neg_scale (FLOAT, default=1.0)
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

---

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

## 18. Model Advanced Nodes

### ModelSamplingDiscrete
- **Display**: ModelSamplingDiscrete
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | sampling (COMBO: eps/v_prediction/lcm/x0/img_to_img/img_to_img_flow) | zsnr (BOOLEAN, default=False)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingContinuousEDM
- **Display**: ModelSamplingContinuousEDM
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | sampling (COMBO: v_prediction/edm/edm_playground_v2.5/eps/cosmos_rflow) | sigma_max (FLOAT, default=120.0) | sigma_min (FLOAT, default=0.002)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingContinuousV
- **Display**: ModelSamplingContinuousV
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | sampling (COMBO: v_prediction) | sigma_max (FLOAT, default=500.0) | sigma_min (FLOAT, default=0.03)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingStableCascade
- **Display**: ModelSamplingStableCascade
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | shift (FLOAT, default=2.0, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingSD3
- **Display**: ModelSamplingSD3
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | shift (FLOAT, default=3.0, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingAuraFlow
- **Display**: ModelSamplingAuraFlow
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | shift (FLOAT, default=1.73, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: patch_aura

### ModelSamplingFlux
- **Display**: ModelSamplingFlux
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | max_shift (FLOAT, default=1.15) | base_shift (FLOAT, default=0.5) | width (INT, default=1024) | height (INT, default=1024)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingLTXV
- **Display**: ModelSamplingLTXV
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | max_shift (FLOAT, default=2.05) | base_shift (FLOAT, default=0.95)
- **Inputs (optional)**: latent (LATENT)
- **Outputs**: MODEL [0]
- **Function**: execute

### RescaleCFG
- **Display**: RescaleCFG
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | multiplier (FLOAT, default=0.7, min=0.0, max=1.0)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelComputeDtype
- **Display**: ModelComputeDtype
- **Category**: advanced/debug/model
- **Inputs (required)**: model (MODEL) | dtype (COMBO: default/fp32/fp16/bf16)
- **Outputs**: MODEL [0]
- **Function**: patch

### RenormCFG
- **Display**: RenormCFG
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | cfg_trunc (FLOAT, default=100) | renorm_cfg (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

---

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

## 21. Audio Nodes

### EmptyLatentAudio
- **Display**: Empty Latent Audio
- **Category**: latent/audio
- **Inputs (required)**: seconds (FLOAT, default=47.6, min=1.0, max=1000.0) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### VAEEncodeAudio
- **Display**: VAE Encode Audio
- **Category**: latent/audio
- **Inputs (required)**: audio (AUDIO) | vae (VAE)
- **Outputs**: LATENT [0]
- **Function**: execute

### VAEDecodeAudio
- **Display**: VAE Decode Audio
- **Category**: latent/audio
- **Inputs (required)**: samples (LATENT) | vae (VAE)
- **Outputs**: AUDIO [0]
- **Function**: execute

### VAEDecodeAudioTiled
- **Display**: VAE Decode Audio (Tiled)
- **Category**: latent/audio
- **Inputs (required)**: samples (LATENT) | vae (VAE) | tile_size (INT, default=512) | overlap (INT, default=64)
- **Outputs**: AUDIO [0]
- **Function**: execute

### SaveAudio
- **Display**: Save Audio (FLAC)
- **Category**: audio
- **Inputs (required)**: audio (AUDIO) | filename_prefix (STRING, default="audio/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: execute

### SaveAudioMP3
- **Display**: Save Audio (MP3)
- **Category**: audio
- **Inputs (required)**: audio (AUDIO) | filename_prefix (STRING, default="audio/ComfyUI") | quality (COMBO: V0/128k/320k)
- **Outputs**: (none - output node)
- **Function**: execute

### SaveAudioOpus
- **Display**: Save Audio (Opus)
- **Category**: audio
- **Inputs (required)**: audio (AUDIO) | filename_prefix (STRING, default="audio/ComfyUI") | quality (COMBO: 64k/96k/128k/192k/320k)
- **Outputs**: (none - output node)
- **Function**: execute

### PreviewAudio
- **Display**: Preview Audio
- **Category**: audio
- **Inputs (required)**: audio (AUDIO)
- **Outputs**: (none - output node)
- **Function**: execute

### LoadAudio
- **Display**: Load Audio
- **Category**: audio
- **Inputs (required)**: audio (COMBO, audio_upload)
- **Outputs**: AUDIO [0]
- **Function**: execute

### RecordAudio
- **Display**: Record Audio
- **Category**: audio
- **Inputs (required)**: audio (AUDIO_RECORD)
- **Outputs**: AUDIO [0]
- **Function**: execute

### TrimAudioDuration
- **Display**: Trim Audio Duration
- **Category**: audio
- **Inputs (required)**: audio (AUDIO) | start_index (FLOAT, default=0.0) | duration (FLOAT, default=60.0)
- **Outputs**: AUDIO [0]
- **Function**: execute

### SplitAudioChannels
- **Display**: Split Audio Channels
- **Category**: audio
- **Inputs (required)**: audio (AUDIO)
- **Outputs**: AUDIO [0] (left), AUDIO [1] (right)
- **Function**: execute

### JoinAudioChannels
- **Display**: Join Audio Channels
- **Category**: audio
- **Inputs (required)**: audio_left (AUDIO) | audio_right (AUDIO)
- **Outputs**: AUDIO [0]
- **Function**: execute

### AudioConcat
- **Display**: Audio Concat
- **Category**: audio
- **Inputs (required)**: audio1 (AUDIO) | audio2 (AUDIO) | direction (COMBO: after/before)
- **Outputs**: AUDIO [0]
- **Function**: execute

### AudioMerge
- **Display**: Audio Merge
- **Category**: audio
- **Inputs (required)**: audio1 (AUDIO) | audio2 (AUDIO) | merge_method (COMBO: add/mean/subtract/multiply)
- **Outputs**: AUDIO [0]
- **Function**: execute

### AudioAdjustVolume
- **Display**: Audio Adjust Volume
- **Category**: audio
- **Inputs (required)**: audio (AUDIO) | volume (INT, default=1, min=-100, max=100)
- **Outputs**: AUDIO [0]
- **Function**: execute

### EmptyAudio
- **Display**: Empty Audio
- **Category**: audio
- **Inputs (required)**: duration (FLOAT, default=60.0) | sample_rate (INT, default=44100) | channels (INT, default=2, min=1, max=2)
- **Outputs**: AUDIO [0]
- **Function**: execute

### AudioEqualizer3Band
- **Display**: Audio Equalizer (3-Band)
- **Category**: audio
- **Inputs (required)**: audio (AUDIO) | low_gain_dB (FLOAT, default=0.0) | low_freq (INT, default=100) | mid_gain_dB (FLOAT, default=0.0) | mid_freq (INT, default=1000) | mid_q (FLOAT, default=0.707) | high_gain_dB (FLOAT, default=0.0) | high_freq (INT, default=5000)
- **Outputs**: AUDIO [0]
- **Function**: execute
- **Notes**: Experimental

### TextEncodeAceStepAudio
- **Display**: TextEncodeAceStepAudio
- **Category**: conditioning
- **Inputs (required)**: clip (CLIP) | tags (STRING, multiline) | lyrics (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### TextEncodeAceStepAudio1.5
- **Display**: TextEncodeAceStepAudio1.5
- **Category**: conditioning
- **Inputs (required)**: clip (CLIP) | tags (STRING, multiline) | lyrics (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### EmptyAceStepLatentAudio
- **Display**: EmptyAceStepLatentAudio
- **Category**: latent/audio
- **Inputs (required)**: seconds (FLOAT, default=60.0) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### EmptyAceStep1.5LatentAudio
- **Display**: EmptyAceStep1.5LatentAudio
- **Category**: latent/audio
- **Inputs (required)**: seconds (FLOAT, default=60.0) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### ReferenceTimbreAudio
- **Display**: ReferenceTimbreAudio
- **Category**: conditioning
- **Inputs (required)**: conditioning (CONDITIONING) | vae (VAE) | audio (AUDIO)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

---

## 22. LTXV Nodes

### EmptyLTXVLatentVideo
- **Display**: EmptyLTXVLatentVideo
- **Category**: latent/video/ltxv
- **Inputs (required)**: width (INT, default=768, step=32) | height (INT, default=512, step=32) | length (INT, default=97, step=8) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### LTXVImgToVideo
- **Display**: LTXVImgToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | image (IMAGE) | width (INT, default=768, step=32) | height (INT, default=512, step=32) | length (INT, default=97, step=8) | batch_size (INT, default=1) | strength (FLOAT, default=1.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### LTXVImgToVideoInplace
- **Display**: LTXVImgToVideoInplace
- **Category**: conditioning/video_models
- **Inputs (required)**: vae (VAE) | image (IMAGE) | latent (LATENT) | strength (FLOAT, default=1.0) | bypass (BOOLEAN, default=False)
- **Outputs**: LATENT [0]
- **Function**: execute

### LTXVAddGuide
- **Display**: LTXVAddGuide
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | latent (LATENT) | image (IMAGE) | frame_idx (INT, default=0) | strength (FLOAT, default=1.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### LTXVCropGuides
- **Display**: LTXVCropGuides
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | latent (LATENT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### LTXVConditioning
- **Display**: LTXVConditioning
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | frame_rate (FLOAT, default=25.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute

### LTXVPreprocess
- **Display**: LTXVPreprocess
- **Category**: image
- **Inputs (required)**: image (IMAGE) | img_compression (INT, default=35, min=0, max=100)
- **Outputs**: IMAGE [0]
- **Function**: execute

### LTXVConcatAVLatent
- **Display**: LTXVConcatAVLatent
- **Category**: latent/video/ltxv
- **Inputs (required)**: video_latent (LATENT) | audio_latent (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute

### LTXVSeparateAVLatent
- **Display**: LTXV Separate AV Latent
- **Category**: latent/video/ltxv
- **Inputs (required)**: av_latent (LATENT)
- **Outputs**: LATENT [0] (video_latent), LATENT [1] (audio_latent)
- **Function**: execute

### LTXVReferenceAudio
- **Display**: LTXV Reference Audio (ID-LoRA)
- **Category**: conditioning/audio
- **Inputs (required)**: model (MODEL) | positive (CONDITIONING) | negative (CONDITIONING) | reference_audio (AUDIO) | audio_vae (VAE) | identity_guidance_scale (FLOAT, default=3.0) | start_percent (FLOAT, default=0.0) | end_percent (FLOAT, default=1.0)
- **Outputs**: MODEL [0], CONDITIONING [1] (positive), CONDITIONING [2] (negative)
- **Function**: execute

### LTXVAudioVAEEncode
- **Display**: LTXV Audio VAE Encode
- **Category**: audio
- **Inputs (required)**: audio (AUDIO) | audio_vae (VAE)
- **Outputs**: LATENT [0]
- **Function**: execute

### LTXVAudioVAEDecode
- **Display**: LTXV Audio VAE Decode
- **Category**: audio
- **Inputs (required)**: samples (LATENT) | audio_vae (VAE)
- **Outputs**: AUDIO [0]
- **Function**: execute

### LTXVEmptyLatentAudio
- **Display**: LTXV Empty Latent Audio
- **Category**: latent/audio
- **Inputs (required)**: frames_number (INT, default=97) | frame_rate (INT, default=25) | batch_size (INT, default=1) | audio_vae (VAE)
- **Outputs**: LATENT [0]
- **Function**: execute

---

## 23. Stable Cascade Nodes

### StableCascade_EmptyLatentImage
- **Display**: StableCascade_EmptyLatentImage
- **Category**: latent/stable_cascade
- **Inputs (required)**: width (INT, default=1024) | height (INT, default=1024) | compression (INT, default=42) | batch_size (INT, default=1)
- **Outputs**: LATENT [0] (stage_c), LATENT [1] (stage_b)
- **Function**: execute

### StableCascade_StageC_VAEEncode
- **Display**: StableCascade_StageC_VAEEncode
- **Category**: latent/stable_cascade
- **Inputs (required)**: image (IMAGE) | vae (VAE) | compression (INT, default=42)
- **Outputs**: LATENT [0] (stage_c), LATENT [1] (stage_b)
- **Function**: execute

### StableCascade_StageB_Conditioning
- **Display**: StableCascade_StageB_Conditioning
- **Category**: conditioning/stable_cascade
- **Inputs (required)**: conditioning (CONDITIONING) | stage_c (LATENT)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### StableCascade_SuperResolutionControlnet
- **Display**: StableCascade_SuperResolutionControlnet
- **Category**: _for_testing/stable_cascade
- **Inputs (required)**: image (IMAGE) | vae (VAE)
- **Outputs**: IMAGE [0] (controlnet_input), LATENT [1] (stage_c), LATENT [2] (stage_b)
- **Function**: execute
- **Notes**: Experimental

---

## 24. Stable 3D Nodes

### StableZero123_Conditioning
- **Display**: StableZero123_Conditioning
- **Category**: conditioning/3d_models
- **Inputs (required)**: clip_vision (CLIP_VISION) | init_image (IMAGE) | vae (VAE) | width (INT, default=256) | height (INT, default=256) | batch_size (INT, default=1) | elevation (FLOAT, default=0.0) | azimuth (FLOAT, default=0.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### StableZero123_Conditioning_Batched
- **Display**: StableZero123_Conditioning_Batched
- **Category**: conditioning/3d_models
- **Inputs (required)**: clip_vision (CLIP_VISION) | init_image (IMAGE) | vae (VAE) | width (INT, default=256) | height (INT, default=256) | batch_size (INT, default=1) | elevation (FLOAT) | azimuth (FLOAT) | elevation_batch_increment (FLOAT) | azimuth_batch_increment (FLOAT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### SV3D_Conditioning
- **Display**: SV3D_Conditioning
- **Category**: conditioning/3d_models
- **Inputs (required)**: clip_vision (CLIP_VISION) | init_image (IMAGE) | vae (VAE) | width (INT, default=576) | height (INT, default=576) | video_frames (INT, default=21) | elevation (FLOAT, default=0.0)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

---

## 25. Cosmos Nodes

### EmptyCosmosLatentVideo
- **Display**: EmptyCosmosLatentVideo
- **Category**: latent/video
- **Inputs (required)**: width (INT, default=1280, step=16) | height (INT, default=704, step=16) | length (INT, default=121, step=8) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### CosmosImageToVideoLatent
- **Display**: CosmosImageToVideoLatent
- **Category**: conditioning/inpaint
- **Inputs (required)**: vae (VAE) | width (INT, default=1280) | height (INT, default=704) | length (INT, default=121) | batch_size (INT, default=1)
- **Inputs (optional)**: start_image (IMAGE) | end_image (IMAGE)
- **Outputs**: LATENT [0]
- **Function**: execute

### CosmosPredict2ImageToVideoLatent
- **Display**: CosmosPredict2ImageToVideoLatent
- **Category**: conditioning/inpaint
- **Inputs (required)**: vae (VAE) | width (INT, default=848) | height (INT, default=480) | length (INT, default=93) | batch_size (INT, default=1)
- **Inputs (optional)**: start_image (IMAGE) | end_image (IMAGE)
- **Outputs**: LATENT [0]
- **Function**: execute

---

## 26. Mochi Nodes

### EmptyMochiLatentVideo
- **Display**: EmptyMochiLatentVideo
- **Category**: latent/video
- **Inputs (required)**: width (INT, default=848, step=16) | height (INT, default=480, step=16) | length (INT, default=25, step=6) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

---

## 27. HiDream Nodes

### CLIPTextEncodeHiDream
- **Display**: CLIPTextEncodeHiDream
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | clip_l (STRING, multiline) | clip_g (STRING, multiline) | t5xxl (STRING, multiline) | llama (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

---

## 28. Lumina2 Nodes

### CLIPTextEncodeLumina2
- **Display**: CLIP Text Encode for Lumina2
- **Category**: conditioning
- **Inputs (required)**: system_prompt (COMBO: superior/alignment) | user_prompt (STRING, multiline) | clip (CLIP)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

---

## 29. PixArt Nodes

### CLIPTextEncodePixArtAlpha
- **Display**: CLIPTextEncodePixArtAlpha
- **Category**: advanced/conditioning
- **Inputs (required)**: width (INT, default=1024) | height (INT, default=1024) | text (STRING, multiline) | clip (CLIP)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

---

## 30. Chroma / Radiance Nodes

### EmptyChromaRadianceLatentImage
- **Display**: EmptyChromaRadianceLatentImage
- **Category**: latent/chroma_radiance
- **Inputs (required)**: width (INT, default=1024, step=16) | height (INT, default=1024, step=16) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

---

## 31. Hunyuan 3D Nodes

### EmptyLatentHunyuan3Dv2
- **Display**: EmptyLatentHunyuan3Dv2
- **Category**: latent/3d
- **Inputs (required)**: resolution (INT, default=3072) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### Hunyuan3Dv2Conditioning
- **Display**: Hunyuan3Dv2Conditioning
- **Category**: conditioning/video_models
- **Inputs (required)**: clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute

### Hunyuan3Dv2ConditioningMultiView
- **Display**: Hunyuan3Dv2ConditioningMultiView
- **Category**: conditioning/video_models
- **Inputs (optional)**: front (CLIP_VISION_OUTPUT) | left (CLIP_VISION_OUTPUT) | back (CLIP_VISION_OUTPUT) | right (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute

### VAEDecodeHunyuan3D
- **Display**: VAEDecodeHunyuan3D
- **Category**: latent/3d
- **Inputs (required)**: samples (LATENT) | vae (VAE) | num_chunks (INT, default=8000) | octree_resolution (INT, default=256)
- **Outputs**: VOXEL [0]
- **Function**: execute

### VoxelToMeshBasic
- **Display**: VoxelToMeshBasic
- **Category**: 3d
- **Inputs (required)**: voxel (VOXEL) | threshold (FLOAT, default=0.6)
- **Outputs**: MESH [0]
- **Function**: execute

### VoxelToMesh
- **Display**: VoxelToMesh
- **Category**: 3d
- **Inputs (required)**: voxel (VOXEL) | algorithm (COMBO: surface net/basic) | threshold (FLOAT, default=0.6)
- **Outputs**: MESH [0]
- **Function**: execute

### SaveGLB
- **Display**: Save 3D Model
- **Category**: 3d
- **Inputs (required)**: mesh (MESH or File3D) | filename_prefix (STRING, default="mesh/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: execute

---

## 32. 3D Nodes

### Load3D
- **Display**: Load 3D & Animation
- **Category**: 3d
- **Inputs (required)**: model_file (COMBO) | image (LOAD3D) | width (INT, default=1024) | height (INT, default=1024)
- **Outputs**: IMAGE [0], MASK [1], STRING [2] (mesh_path), IMAGE [3] (normal), LOAD3D_CAMERA [4], VIDEO [5] (recording), FILE3D [6]
- **Function**: execute
- **Notes**: Experimental

### Preview3D
- **Display**: Preview 3D & Animation
- **Category**: 3d
- **Inputs (required)**: model_file (STRING or File3D)
- **Inputs (optional)**: camera_info (LOAD3D_CAMERA) | bg_image (IMAGE)
- **Outputs**: (none - output node)
- **Function**: execute
- **Notes**: Experimental

---

## 33. Kandinsky Nodes

### Kandinsky5ImageToVideo
- **Display**: Kandinsky5ImageToVideo
- **Category**: conditioning/video_models
- **Inputs (required)**: positive (CONDITIONING) | negative (CONDITIONING) | vae (VAE) | width (INT) | height (INT) | length (INT) | batch_size (INT)
- **Inputs (optional)**: start_image (IMAGE)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative), LATENT [2]
- **Function**: execute

### NormalizeVideoLatentStart
- **Display**: NormalizeVideoLatentStart
- **Category**: latent/video
- **Inputs (required)**: samples (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute

### CLIPTextEncodeKandinsky5
- **Display**: CLIPTextEncodeKandinsky5
- **Category**: advanced/conditioning
- **Inputs (required)**: clip (CLIP) | t5xxl (STRING, multiline) | umt5xxl (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

---

## 34. Qwen / OmniGen / ZImage Nodes

### TextEncodeQwenImageEdit
- **Display**: TextEncodeQwenImageEdit
- **Category**: conditioning
- **Inputs (required)**: clip (CLIP) | text (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### TextEncodeQwenImageEditPlus
- **Display**: TextEncodeQwenImageEditPlus
- **Category**: conditioning
- **Inputs (required)**: clip (CLIP) | text (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

### EmptyQwenImageLayeredLatentImage
- **Display**: EmptyQwenImageLayeredLatentImage
- **Category**: latent
- **Inputs (required)**: width (INT) | height (INT) | batch_size (INT) | num_layers (INT)
- **Outputs**: LATENT [0]
- **Function**: execute

### TextEncodeZImageOmni
- **Display**: TextEncodeZImageOmni
- **Category**: conditioning
- **Inputs (required)**: clip (CLIP) | text (STRING, multiline)
- **Outputs**: CONDITIONING [0]
- **Function**: execute

---

## 35. String Nodes

### StringConcatenate
- **Display**: StringConcatenate
- **Category**: utils/string
- **Inputs (required)**: string1 (STRING) | string2 (STRING)
- **Outputs**: STRING [0]
- **Function**: execute

### StringSubstring
- **Display**: StringSubstring
- **Category**: utils/string
- **Inputs (required)**: string (STRING) | start (INT) | end (INT)
- **Outputs**: STRING [0]
- **Function**: execute

### StringLength
- **Display**: StringLength
- **Category**: utils/string
- **Inputs (required)**: string (STRING)
- **Outputs**: INT [0]
- **Function**: execute

### CaseConverter
- **Display**: CaseConverter
- **Category**: utils/string
- **Inputs (required)**: string (STRING) | mode (COMBO: upper/lower/title/capitalize/swapcase)
- **Outputs**: STRING [0]
- **Function**: execute

### StringTrim
- **Display**: StringTrim
- **Category**: utils/string
- **Inputs (required)**: string (STRING) | mode (COMBO: both/left/right)
- **Outputs**: STRING [0]
- **Function**: execute

### StringReplace
- **Display**: StringReplace
- **Category**: utils/string
- **Inputs (required)**: string (STRING) | old (STRING) | new (STRING)
- **Outputs**: STRING [0]
- **Function**: execute

### StringContains
- **Display**: StringContains
- **Category**: utils/string
- **Inputs (required)**: string (STRING) | substring (STRING)
- **Outputs**: BOOLEAN [0]
- **Function**: execute

### StringCompare
- **Display**: StringCompare
- **Category**: utils/string
- **Inputs (required)**: string1 (STRING) | string2 (STRING)
- **Outputs**: BOOLEAN [0]
- **Function**: execute

### RegexMatch
- **Display**: RegexMatch
- **Category**: utils/string
- **Inputs (required)**: string (STRING) | pattern (STRING)
- **Outputs**: BOOLEAN [0]
- **Function**: execute

### RegexExtract
- **Display**: RegexExtract
- **Category**: utils/string
- **Inputs (required)**: string (STRING) | pattern (STRING)
- **Outputs**: STRING [0]
- **Function**: execute

### RegexReplace
- **Display**: RegexReplace
- **Category**: utils/string
- **Inputs (required)**: string (STRING) | pattern (STRING) | replacement (STRING)
- **Outputs**: STRING [0]
- **Function**: execute

---

## 36. Primitive Nodes

### PrimitiveString
- **Display**: PrimitiveString
- **Category**: utils/primitive
- **Inputs (required)**: value (STRING)
- **Outputs**: STRING [0]
- **Function**: execute

### PrimitiveStringMultiline
- **Display**: PrimitiveStringMultiline
- **Category**: utils/primitive
- **Inputs (required)**: value (STRING, multiline)
- **Outputs**: STRING [0]
- **Function**: execute

### PrimitiveInt
- **Display**: PrimitiveInt
- **Category**: utils/primitive
- **Inputs (required)**: value (INT)
- **Outputs**: INT [0]
- **Function**: execute

### PrimitiveFloat
- **Display**: PrimitiveFloat
- **Category**: utils/primitive
- **Inputs (required)**: value (FLOAT)
- **Outputs**: FLOAT [0]
- **Function**: execute

### PrimitiveBoolean
- **Display**: PrimitiveBoolean
- **Category**: utils/primitive
- **Inputs (required)**: value (BOOLEAN)
- **Outputs**: BOOLEAN [0]
- **Function**: execute

---

## 37. Logic / Utility Nodes

### ComfySwitchNode
- **Display**: ComfySwitchNode
- **Category**: utils
- **Inputs (required)**: select (INT) | (dynamic inputs)
- **Outputs**: * [0]
- **Function**: execute

### ComfySoftSwitchNode
- **Display**: ComfySoftSwitchNode
- **Category**: utils
- **Inputs (required)**: select (INT) | (dynamic inputs)
- **Outputs**: * [0]
- **Function**: execute

### ConvertStringToComboNode
- **Display**: ConvertStringToComboNode
- **Category**: utils
- **Inputs (required)**: string (STRING)
- **Outputs**: COMBO [0]
- **Function**: execute

### InvertBooleanNode
- **Display**: InvertBooleanNode
- **Category**: utils
- **Inputs (required)**: value (BOOLEAN)
- **Outputs**: BOOLEAN [0]
- **Function**: execute

### ComfyNumberConvert
- **Display**: ComfyNumberConvert
- **Category**: utils
- **Inputs (required)**: value (INT or FLOAT)
- **Outputs**: INT [0], FLOAT [1]
- **Function**: execute

### ColorToRGBInt
- **Display**: ColorToRGBInt
- **Category**: utils
- **Inputs (required)**: color (INT, display=color)
- **Outputs**: INT [0] (r), INT [1] (g), INT [2] (b)
- **Function**: execute

### ComfyMathExpression
- **Display**: ComfyMathExpression
- **Category**: utils/math
- **Inputs (required)**: expression (STRING)
- **Inputs (optional)**: a (FLOAT) | b (FLOAT) | c (FLOAT)
- **Outputs**: FLOAT [0], INT [1]
- **Function**: execute

### ResolutionSelector
- **Display**: ResolutionSelector
- **Category**: utils
- **Inputs (required)**: resolution (COMBO) | swap (BOOLEAN, default=False)
- **Outputs**: INT [0] (width), INT [1] (height)
- **Function**: execute

### CreateList
- **Display**: CreateList
- **Category**: utils
- **Inputs (required)**: (dynamic ANY inputs)
- **Outputs**: * [0] (list)
- **Function**: execute

### EasyCache
- **Display**: EasyCache
- **Category**: utils
- **Inputs (required)**: (dynamic inputs)
- **Outputs**: (dynamic outputs)
- **Function**: execute

### LazyCache
- **Display**: LazyCache
- **Category**: utils
- **Inputs (required)**: (dynamic inputs)
- **Outputs**: (dynamic outputs)
- **Function**: execute

### PreviewAny
- **Display**: Preview Any
- **Category**: utils
- **Inputs (required)**: value (*)
- **Outputs**: (none - output node)
- **Function**: execute

### CurveEditor
- **Display**: CurveEditor
- **Category**: utils
- **Inputs (required)**: curve (STRING)
- **Outputs**: FLOAT [0]
- **Function**: execute

### Painter
- **Display**: Painter
- **Category**: image
- **Inputs (required)**: image (COMBO) | width (INT) | height (INT)
- **Outputs**: IMAGE [0], MASK [1]
- **Function**: execute

### GLSLShader
- **Display**: GLSLShader
- **Category**: image
- **Inputs (required)**: fragment_code (STRING, multiline) | width (INT) | height (INT) | frame_count (INT) | fps (FLOAT)
- **Outputs**: IMAGE [0]
- **Function**: execute

---

## 38. Text Generation Nodes

### TextGenerate
- **Display**: TextGenerate
- **Category**: text
- **Inputs (required)**: model (MODEL) | clip (CLIP) | text (STRING, multiline) | max_tokens (INT) | temperature (FLOAT) | top_k (INT) | top_p (FLOAT)
- **Outputs**: STRING [0]
- **Function**: execute

### TextGenerateLTX2Prompt
- **Display**: TextGenerateLTX2Prompt
- **Category**: text
- **Inputs (required)**: model (MODEL) | clip (CLIP) | text (STRING, multiline)
- **Outputs**: STRING [0]
- **Function**: execute

---

## 39. Object Detection Nodes

### RTDETR_detect
- **Display**: RTDETR_detect
- **Category**: image/detection
- **Inputs (required)**: model_name (COMBO) | image (IMAGE) | threshold (FLOAT, default=0.5)
- **Outputs**: BBOXES [0]
- **Function**: execute

### DrawBBoxes
- **Display**: DrawBBoxes
- **Category**: image/detection
- **Inputs (required)**: image (IMAGE) | bboxes (BBOXES)
- **Outputs**: IMAGE [0]
- **Function**: execute

### SDPoseDrawKeypoints
- **Display**: SDPoseDrawKeypoints
- **Category**: image/pose
- **Inputs (required)**: keypoints (KEYPOINTS) | width (INT) | height (INT)
- **Outputs**: IMAGE [0]
- **Function**: execute

### SDPoseKeypointExtractor
- **Display**: SDPoseKeypointExtractor
- **Category**: image/pose
- **Inputs (required)**: model_name (COMBO) | image (IMAGE)
- **Outputs**: KEYPOINTS [0]
- **Function**: execute

### SDPoseFaceBBoxes
- **Display**: SDPoseFaceBBoxes
- **Category**: image/pose
- **Inputs (required)**: keypoints (KEYPOINTS)
- **Outputs**: BBOXES [0]
- **Function**: execute

### CropByBBoxes
- **Display**: CropByBBoxes
- **Category**: image
- **Inputs (required)**: image (IMAGE) | bboxes (BBOXES) | padding (INT, default=0)
- **Outputs**: IMAGE [0]
- **Function**: execute

---

## 40. Training Nodes

### TrainLoraNode
- **Display**: TrainLoraNode
- **Category**: training
- **Inputs (required)**: model (MODEL) | dataset (DATASET) | (training parameters)
- **Outputs**: MODEL [0]
- **Function**: execute

### LoraModelLoader
- **Display**: LoraModelLoader
- **Category**: training
- **Inputs (required)**: model_name (COMBO)
- **Outputs**: MODEL [0]
- **Function**: execute

### SaveLoRA
- **Display**: SaveLoRA
- **Category**: training
- **Inputs (required)**: model (MODEL) | filename_prefix (STRING)
- **Outputs**: (none - output node)
- **Function**: execute

### LossGraphNode
- **Display**: LossGraphNode
- **Category**: training
- **Inputs (required)**: loss (FLOAT)
- **Outputs**: (none - output node)
- **Function**: execute

### LoraSave
- **Display**: LoraSave
- **Category**: advanced/model_merging
- **Inputs (required)**: filename_prefix (STRING) | rank (INT) | (model inputs)
- **Outputs**: (none - output node)
- **Function**: execute

---

## 41. Dataset Nodes

### LoadImageDataSetFromFolder
- **Display**: LoadImageDataSetFromFolder
- **Category**: training/dataset
- **Inputs (required)**: folder_path (STRING)
- **Outputs**: IMAGE [0] (list)
- **Function**: execute

### LoadImageTextDataSetFromFolder
- **Display**: LoadImageTextDataSetFromFolder
- **Category**: training/dataset
- **Inputs (required)**: folder_path (STRING)
- **Outputs**: IMAGE [0] (list), STRING [1] (list)
- **Function**: execute

### SaveImageDataSetToFolder
- **Display**: SaveImageDataSetToFolder
- **Category**: training/dataset
- **Inputs (required)**: images (IMAGE, list) | folder_path (STRING)
- **Outputs**: (none - output node)
- **Function**: execute

### SaveImageTextDataSetToFolder
- **Display**: SaveImageTextDataSetToFolder
- **Category**: training/dataset
- **Inputs (required)**: images (IMAGE, list) | texts (STRING, list) | folder_path (STRING)
- **Outputs**: (none - output node)
- **Function**: execute

### ShuffleImageTextDataset
- **Display**: ShuffleImageTextDataset
- **Category**: training/dataset
- **Inputs (required)**: images (IMAGE, list) | texts (STRING, list) | seed (INT)
- **Outputs**: IMAGE [0] (list), STRING [1] (list)
- **Function**: execute

### ResolutionBucket
- **Display**: ResolutionBucket
- **Category**: training/dataset
- **Inputs (required)**: width (INT) | height (INT) | bucket_size (INT)
- **Outputs**: INT [0] (width), INT [1] (height)
- **Function**: execute

### MakeTrainingDataset
- **Display**: MakeTrainingDataset
- **Category**: training/dataset
- **Inputs (required)**: images (IMAGE, list) | texts (STRING, list) | batch_size (INT)
- **Outputs**: DATASET [0]
- **Function**: execute

### SaveTrainingDataset
- **Display**: SaveTrainingDataset
- **Category**: training/dataset
- **Inputs (required)**: dataset (DATASET) | filename_prefix (STRING)
- **Outputs**: (none - output node)
- **Function**: execute

### LoadTrainingDataset
- **Display**: LoadTrainingDataset
- **Category**: training/dataset
- **Inputs (required)**: dataset_name (COMBO)
- **Outputs**: DATASET [0]
- **Function**: execute

---

## 42. Debug / Misc Nodes

### LoraLoaderBypass
- **Display**: Load LoRA (Bypass) (For debugging)
- **Category**: loaders
- **Inputs (required)**: model (MODEL) | clip (CLIP) | lora_name (COMBO) | strength_model (FLOAT, default=1.0) | strength_clip (FLOAT, default=1.0)
- **Outputs**: MODEL [0], CLIP [1]
- **Function**: load_lora

### LoraLoaderBypassModelOnly
- **Display**: Load LoRA (Bypass, Model Only) (for debugging)
- **Category**: loaders
- **Inputs (required)**: model (MODEL) | lora_name (COMBO) | strength_model (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: load_lora_model_only

### WebcamCapture
- **Display**: WebcamCapture
- **Category**: image
- **Inputs (required)**: image (WEBCAM)
- **Outputs**: IMAGE [0]
- **Function**: execute
# ComfyUI Node Registry - Additions

New nodes extracted from comfy_extras source files, not yet in the main node-registry.md.

---

### nodes_audio.py

## EmptyLatentAudio
- **Category:** latent/audio
- **Inputs:**
  - seconds: FLOAT (default=47.6, min=1.0, max=1000.0, step=0.1)
  - batch_size: INT (default=1, min=1, max=4096)
- **Outputs:** LATENT

## ConditioningStableAudio
- **Category:** conditioning
- **Inputs:**
  - positive: CONDITIONING
  - negative: CONDITIONING
  - seconds_start: FLOAT (default=0.0, min=0.0, max=1000.0, step=0.1)
  - seconds_total: FLOAT (default=47.0, min=0.0, max=1000.0, step=0.1)
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative)

## VAEEncodeAudio
- **Category:** latent/audio
- **Inputs:**
  - audio: AUDIO
  - vae: VAE
- **Outputs:** LATENT

## VAEDecodeAudio
- **Category:** latent/audio
- **Inputs:**
  - samples: LATENT
  - vae: VAE
- **Outputs:** AUDIO

## VAEDecodeAudioTiled
- **Category:** latent/audio
- **Inputs:**
  - samples: LATENT
  - vae: VAE
  - tile_size: INT (default=512, min=32, max=8192, step=8)
  - overlap: INT (default=64, min=0, max=1024, step=8)
- **Outputs:** AUDIO

## SaveAudio
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
  - filename_prefix: STRING (default="audio/ComfyUI")
- **Outputs:** (output node)

## SaveAudioMP3
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
  - filename_prefix: STRING (default="audio/ComfyUI")
  - quality: COMBO (options: V0, 128k, 320k; default=V0)
- **Outputs:** (output node)

## SaveAudioOpus
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
  - filename_prefix: STRING (default="audio/ComfyUI")
  - quality: COMBO (options: 64k, 96k, 128k, 192k, 320k; default=128k)
- **Outputs:** (output node)

## PreviewAudio
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
- **Outputs:** (output node)

## LoadAudio
- **Category:** audio
- **Inputs:**
  - audio: COMBO (audio files, upload)
- **Outputs:** AUDIO

## RecordAudio
- **Category:** audio
- **Inputs:**
  - audio: AUDIO_RECORD
- **Outputs:** AUDIO

## TrimAudioDuration
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
  - start_index: FLOAT (default=0.0, step=0.01)
  - duration: FLOAT (default=60.0, min=0.0, step=0.01)
- **Outputs:** AUDIO

## SplitAudioChannels
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
- **Outputs:** AUDIO (left), AUDIO (right)

## JoinAudioChannels
- **Category:** audio
- **Inputs:**
  - audio_left: AUDIO
  - audio_right: AUDIO
- **Outputs:** AUDIO

## AudioConcat
- **Category:** audio
- **Inputs:**
  - audio1: AUDIO
  - audio2: AUDIO
  - direction: COMBO (options: after, before; default=after)
- **Outputs:** AUDIO

## AudioMerge
- **Category:** audio
- **Inputs:**
  - audio1: AUDIO
  - audio2: AUDIO
  - merge_method: COMBO (options: add, mean, subtract, multiply)
- **Outputs:** AUDIO

## AudioAdjustVolume
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
  - volume: INT (default=1, min=-100, max=100)
- **Outputs:** AUDIO

## EmptyAudio
- **Category:** audio
- **Inputs:**
  - duration: FLOAT (default=60.0, min=0.0, step=0.01)
  - sample_rate: INT (default=44100, min=1, max=192000) (advanced)
  - channels: INT (default=2, min=1, max=2) (advanced)
- **Outputs:** AUDIO

## AudioEqualizer3Band
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
  - low_gain_dB: FLOAT (default=0.0, min=-24.0, max=24.0, step=0.1)
  - low_freq: INT (default=100, min=20, max=500)
  - mid_gain_dB: FLOAT (default=0.0, min=-24.0, max=24.0, step=0.1)
  - mid_freq: INT (default=1000, min=200, max=4000)
  - mid_q: FLOAT (default=0.707, min=0.1, max=10.0, step=0.1)
  - high_gain_dB: FLOAT (default=0.0, min=-24.0, max=24.0, step=0.1)
  - high_freq: INT (default=5000, min=1000, max=15000)
- **Outputs:** AUDIO

---

### nodes_audio_encoder.py

## AudioEncoderLoader
- **Category:** loaders
- **Inputs:**
  - audio_encoder_name: COMBO (audio_encoders list)
- **Outputs:** AUDIO_ENCODER

## AudioEncoderEncode
- **Category:** conditioning
- **Inputs:**
  - audio_encoder: AUDIO_ENCODER
  - audio: AUDIO
- **Outputs:** AUDIO_ENCODER_OUTPUT

---

### nodes_lt_audio.py

## LTXVAudioVAELoader
- **Category:** audio
- **Inputs:**
  - ckpt_name: COMBO (checkpoints list)
- **Outputs:** VAE (Audio VAE)

## LTXVAudioVAEEncode
- **Category:** audio
- **Inputs:**
  - audio: AUDIO
  - audio_vae: VAE (Audio VAE)
- **Outputs:** LATENT (Audio Latent)

## LTXVAudioVAEDecode
- **Category:** audio
- **Inputs:**
  - samples: LATENT
  - audio_vae: VAE (Audio VAE)
- **Outputs:** AUDIO

## LTXVEmptyLatentAudio
- **Category:** latent/audio
- **Inputs:**
  - frames_number: INT (default=97, min=1, max=1000)
  - frame_rate: INT (default=25, min=1, max=1000)
  - batch_size: INT (default=1, min=1, max=4096)
  - audio_vae: VAE (Audio VAE)
- **Outputs:** LATENT

## LTXAVTextEncoderLoader
- **Category:** advanced/loaders
- **Inputs:**
  - text_encoder: COMBO (text_encoders list)
  - ckpt_name: COMBO (checkpoints list)
  - device: COMBO (options: default, cpu) (advanced)
- **Outputs:** CLIP

---

### nodes_lt.py (LTXV)

## EmptyLTXVLatentVideo
- **Category:** latent/video/ltxv
- **Inputs:**
  - width: INT (default=768, min=64, max=MAX_RESOLUTION, step=32)
  - height: INT (default=512, min=64, max=MAX_RESOLUTION, step=32)
  - length: INT (default=97, min=1, max=MAX_RESOLUTION, step=8)
  - batch_size: INT (default=1, min=1, max=4096)
- **Outputs:** LATENT

## LTXVImgToVideo
- **Category:** conditioning/video_models
- **Inputs:**
  - positive: CONDITIONING
  - negative: CONDITIONING
  - vae: VAE
  - image: IMAGE
  - width: INT (default=768, min=64, max=MAX_RESOLUTION, step=32)
  - height: INT (default=512, min=64, max=MAX_RESOLUTION, step=32)
  - length: INT (default=97, min=9, max=MAX_RESOLUTION, step=8)
  - batch_size: INT (default=1, min=1, max=4096)
  - strength: FLOAT (default=1.0, min=0.0, max=1.0)
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative), LATENT (latent)

## LTXVImgToVideoInplace
- **Category:** conditioning/video_models
- **Inputs:**
  - vae: VAE
  - image: IMAGE
  - latent: LATENT
  - strength: FLOAT (default=1.0, min=0.0, max=1.0)
  - bypass: BOOLEAN (default=False)
- **Outputs:** LATENT

## LTXVAddGuide
- **Category:** conditioning/video_models
- **Inputs:**
  - positive: CONDITIONING
  - negative: CONDITIONING
  - vae: VAE
  - latent: LATENT
  - image: IMAGE
  - frame_idx: INT (default=0, min=-9999, max=9999)
  - strength: FLOAT (default=1.0, min=0.0, max=1.0, step=0.01)
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative), LATENT (latent)

## LTXVCropGuides
- **Category:** conditioning/video_models
- **Inputs:**
  - positive: CONDITIONING
  - negative: CONDITIONING
  - latent: LATENT
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative), LATENT (latent)

## LTXVConditioning
- **Category:** conditioning/video_models
- **Inputs:**
  - positive: CONDITIONING
  - negative: CONDITIONING
  - frame_rate: FLOAT (default=25.0, min=0.0, max=1000.0, step=0.01)
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative)

## ModelSamplingLTXV
- **Category:** advanced/model
- **Inputs:**
  - model: MODEL
  - max_shift: FLOAT (default=2.05, min=0.0, max=100.0, step=0.01)
  - base_shift: FLOAT (default=0.95, min=0.0, max=100.0, step=0.01)
  - latent: LATENT (optional)
- **Outputs:** MODEL

## LTXVScheduler
- **Category:** sampling/custom_sampling/schedulers
- **Inputs:**
  - steps: INT (default=20, min=1, max=10000)
  - max_shift: FLOAT (default=2.05, min=0.0, max=100.0, step=0.01)
  - base_shift: FLOAT (default=0.95, min=0.0, max=100.0, step=0.01)
  - stretch: BOOLEAN (default=True) (advanced)
  - terminal: FLOAT (default=0.1, min=0.0, max=0.99, step=0.01) (advanced)
  - latent: LATENT (optional)
- **Outputs:** SIGMAS

## LTXVPreprocess
- **Category:** image
- **Inputs:**
  - image: IMAGE
  - img_compression: INT (default=35, min=0, max=100)
- **Outputs:** IMAGE (output_image)

## LTXVConcatAVLatent
- **Category:** latent/video/ltxv
- **Inputs:**
  - video_latent: LATENT
  - audio_latent: LATENT
- **Outputs:** LATENT

## LTXVSeparateAVLatent
- **Category:** latent/video/ltxv
- **Inputs:**
  - av_latent: LATENT
- **Outputs:** LATENT (video_latent), LATENT (audio_latent)

## LTXVReferenceAudio
- **Category:** conditioning/audio
- **Inputs:**
  - model: MODEL
  - positive: CONDITIONING
  - negative: CONDITIONING
  - reference_audio: AUDIO
  - audio_vae: VAE (Audio VAE)
  - identity_guidance_scale: FLOAT (default=3.0, min=0.0, max=100.0, step=0.01)
  - start_percent: FLOAT (default=0.0, min=0.0, max=1.0, step=0.001) (advanced)
  - end_percent: FLOAT (default=1.0, min=0.0, max=1.0, step=0.001) (advanced)
- **Outputs:** MODEL, CONDITIONING (positive), CONDITIONING (negative)

---

### nodes_mochi.py

## EmptyMochiLatentVideo
- **Category:** latent/video
- **Inputs:**
  - width: INT (default=848, min=16, max=MAX_RESOLUTION, step=16)
  - height: INT (default=480, min=16, max=MAX_RESOLUTION, step=16)
  - length: INT (default=25, min=7, max=MAX_RESOLUTION, step=6)
  - batch_size: INT (default=1, min=1, max=4096)
- **Outputs:** LATENT

---

### nodes_cosmos.py

## EmptyCosmosLatentVideo
- **Category:** latent/video
- **Inputs:**
  - width: INT (default=1280, min=16, max=MAX_RESOLUTION, step=16)
  - height: INT (default=704, min=16, max=MAX_RESOLUTION, step=16)
  - length: INT (default=121, min=1, max=MAX_RESOLUTION, step=8)
  - batch_size: INT (default=1, min=1, max=4096)
- **Outputs:** LATENT

## CosmosImageToVideoLatent
- **Category:** conditioning/inpaint
- **Inputs:**
  - vae: VAE
  - width: INT (default=1280, min=16, max=MAX_RESOLUTION, step=16)
  - height: INT (default=704, min=16, max=MAX_RESOLUTION, step=16)
  - length: INT (default=121, min=1, max=MAX_RESOLUTION, step=8)
  - batch_size: INT (default=1, min=1, max=4096)
  - start_image: IMAGE (optional)
  - end_image: IMAGE (optional)
- **Outputs:** LATENT

## CosmosPredict2ImageToVideoLatent
- **Category:** conditioning/inpaint
- **Inputs:**
  - vae: VAE
  - width: INT (default=848, min=16, max=MAX_RESOLUTION, step=16)
  - height: INT (default=480, min=16, max=MAX_RESOLUTION, step=16)
  - length: INT (default=93, min=1, max=MAX_RESOLUTION, step=4)
  - batch_size: INT (default=1, min=1, max=4096)
  - start_image: IMAGE (optional)
  - end_image: IMAGE (optional)
- **Outputs:** LATENT

---

### nodes_pixart.py

## CLIPTextEncodePixArtAlpha
- **Category:** advanced/conditioning
- **Inputs:**
  - width: INT (default=1024, min=0, max=MAX_RESOLUTION)
  - height: INT (default=1024, min=0, max=MAX_RESOLUTION)
  - text: STRING (multiline)
  - clip: CLIP
- **Outputs:** CONDITIONING

---

### nodes_lumina2.py

## RenormCFG
- **Category:** advanced/model
- **Inputs:**
  - model: MODEL
  - cfg_trunc: FLOAT (default=100, min=0.0, max=100.0, step=0.01) (advanced)
  - renorm_cfg: FLOAT (default=1.0, min=0.0, max=100.0, step=0.01) (advanced)
- **Outputs:** MODEL

## CLIPTextEncodeLumina2
- **Category:** conditioning
- **Inputs:**
  - system_prompt: COMBO (options: superior, alignment)
  - user_prompt: STRING (multiline)
  - clip: CLIP
- **Outputs:** CONDITIONING

---

### nodes_hidream.py

## QuadrupleCLIPLoader
- **Category:** advanced/loaders
- **Inputs:**
  - clip_name1: COMBO (text_encoders list)
  - clip_name2: COMBO (text_encoders list)
  - clip_name3: COMBO (text_encoders list)
  - clip_name4: COMBO (text_encoders list)
- **Outputs:** CLIP

## CLIPTextEncodeHiDream
- **Category:** advanced/conditioning
- **Inputs:**
  - clip: CLIP
  - clip_l: STRING (multiline)
  - clip_g: STRING (multiline)
  - t5xxl: STRING (multiline)
  - llama: STRING (multiline)
- **Outputs:** CONDITIONING

---

### nodes_chroma_radiance.py

## EmptyChromaRadianceLatentImage
- **Category:** latent/chroma_radiance
- **Inputs:**
  - width: INT (default=1024, min=16, max=MAX_RESOLUTION, step=16)
  - height: INT (default=1024, min=16, max=MAX_RESOLUTION, step=16)
  - batch_size: INT (default=1, min=1, max=4096)
- **Outputs:** LATENT

## ChromaRadianceOptions
- **Category:** model_patches/chroma_radiance
- **Inputs:**
  - model: MODEL
  - preserve_wrapper: BOOLEAN (default=True)
  - start_sigma: FLOAT (default=1.0, min=0.0, max=1.0) (advanced)
  - end_sigma: FLOAT (default=0.0, min=0.0, max=1.0) (advanced)
  - nerf_tile_size: INT (default=-1, min=-1) (advanced)
- **Outputs:** MODEL

---

### nodes_hunyuan3d.py

## EmptyLatentHunyuan3Dv2
- **Category:** latent/3d
- **Inputs:**
  - resolution: INT (default=3072, min=1, max=8192)
  - batch_size: INT (default=1, min=1, max=4096)
- **Outputs:** LATENT

## Hunyuan3Dv2Conditioning
- **Category:** conditioning/video_models
- **Inputs:**
  - clip_vision_output: CLIP_VISION_OUTPUT
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative)

## Hunyuan3Dv2ConditioningMultiView
- **Category:** conditioning/video_models
- **Inputs:**
  - front: CLIP_VISION_OUTPUT (optional)
  - left: CLIP_VISION_OUTPUT (optional)
  - back: CLIP_VISION_OUTPUT (optional)
  - right: CLIP_VISION_OUTPUT (optional)
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative)

## VAEDecodeHunyuan3D
- **Category:** latent/3d
- **Inputs:**
  - samples: LATENT
  - vae: VAE
  - num_chunks: INT (default=8000, min=1000, max=500000) (advanced)
  - octree_resolution: INT (default=256, min=16, max=512) (advanced)
- **Outputs:** VOXEL

## VoxelToMeshBasic
- **Category:** 3d
- **Inputs:**
  - voxel: VOXEL
  - threshold: FLOAT (default=0.6, min=-1.0, max=1.0, step=0.01)
- **Outputs:** MESH

## VoxelToMesh
- **Category:** 3d
- **Inputs:**
  - voxel: VOXEL
  - algorithm: COMBO (options: surface net, basic) (advanced)
  - threshold: FLOAT (default=0.6, min=-1.0, max=1.0, step=0.01)
- **Outputs:** MESH

## SaveGLB
- **Category:** 3d
- **Inputs:**
  - mesh: MESH | FILE_3D (multi-type: GLB, GLTF, OBJ, FBX, STL, USDZ)
  - filename_prefix: STRING (default="mesh/ComfyUI")
- **Outputs:** (output node)

---

### nodes_stable3d.py

## StableZero123_Conditioning
- **Category:** conditioning/3d_models
- **Inputs:**
  - clip_vision: CLIP_VISION
  - init_image: IMAGE
  - vae: VAE
  - width: INT (default=256, min=16, max=MAX_RESOLUTION, step=8)
  - height: INT (default=256, min=16, max=MAX_RESOLUTION, step=8)
  - batch_size: INT (default=1, min=1, max=4096)
  - elevation: FLOAT (default=0.0, min=-180.0, max=180.0, step=0.1)
  - azimuth: FLOAT (default=0.0, min=-180.0, max=180.0, step=0.1)
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative), LATENT (latent)

## StableZero123_Conditioning_Batched
- **Category:** conditioning/3d_models
- **Inputs:**
  - clip_vision: CLIP_VISION
  - init_image: IMAGE
  - vae: VAE
  - width: INT (default=256, min=16, max=MAX_RESOLUTION, step=8)
  - height: INT (default=256, min=16, max=MAX_RESOLUTION, step=8)
  - batch_size: INT (default=1, min=1, max=4096)
  - elevation: FLOAT (default=0.0, min=-180.0, max=180.0, step=0.1)
  - azimuth: FLOAT (default=0.0, min=-180.0, max=180.0, step=0.1)
  - elevation_batch_increment: FLOAT (default=0.0, min=-180.0, max=180.0, step=0.1) (advanced)
  - azimuth_batch_increment: FLOAT (default=0.0, min=-180.0, max=180.0, step=0.1) (advanced)
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative), LATENT (latent)

## SV3D_Conditioning
- **Category:** conditioning/3d_models
- **Inputs:**
  - clip_vision: CLIP_VISION
  - init_image: IMAGE
  - vae: VAE
  - width: INT (default=576, min=16, max=MAX_RESOLUTION, step=8)
  - height: INT (default=576, min=16, max=MAX_RESOLUTION, step=8)
  - video_frames: INT (default=21, min=1, max=4096)
  - elevation: FLOAT (default=0.0, min=-90.0, max=90.0, step=0.1)
- **Outputs:** CONDITIONING (positive), CONDITIONING (negative), LATENT (latent)

---

### nodes_stable_cascade.py

## StableCascade_EmptyLatentImage
- **Category:** latent/stable_cascade
- **Inputs:**
  - width: INT (default=1024, min=256, max=MAX_RESOLUTION, step=8)
  - height: INT (default=1024, min=256, max=MAX_RESOLUTION, step=8)
  - compression: INT (default=42, min=4, max=128, step=1) (advanced)
  - batch_size: INT (default=1, min=1, max=4096)
- **Outputs:** LATENT (stage_c), LATENT (stage_b)

## StableCascade_StageC_VAEEncode
- **Category:** latent/stable_cascade
- **Inputs:**
  - image: IMAGE
  - vae: VAE
  - compression: INT (default=42, min=4, max=128, step=1) (advanced)
- **Outputs:** LATENT (stage_c), LATENT (stage_b)

## StableCascade_StageB_Conditioning
- **Category:** conditioning/stable_cascade
- **Inputs:**
  - conditioning: CONDITIONING
  - stage_c: LATENT
- **Outputs:** CONDITIONING

## StableCascade_SuperResolutionControlnet
- **Category:** _for_testing/stable_cascade
- **Inputs:**
  - image: IMAGE
  - vae: VAE
- **Outputs:** IMAGE (controlnet_input), LATENT (stage_c), LATENT (stage_b)

---

### nodes_load_3d.py

## Load3D
- **Category:** 3d
- **Inputs:**
  - model_file: COMBO (3d model files, upload)
  - image: LOAD_3D
  - width: INT (default=1024, min=1, max=4096)
  - height: INT (default=1024, min=1, max=4096)
- **Outputs:** IMAGE (image), MASK (mask), STRING (mesh_path), IMAGE (normal), LOAD_3D_CAMERA (camera_info), VIDEO (recording_video), FILE_3D_ANY (model_3d)

## Preview3D
- **Category:** 3d
- **Inputs:**
  - model_file: STRING | FILE_3D (multi-type: GLB, GLTF, FBX, OBJ, STL, USDZ)
  - camera_info: LOAD_3D_CAMERA (optional, advanced)
  - bg_image: IMAGE (optional, advanced)
- **Outputs:** (output node)

---

### nodes_lt_upsampler.py

## LTXVLatentUpsampler
- **Category:** latent/video
- **Inputs:**
  - samples: LATENT
  - upscale_model: LATENT_UPSCALE_MODEL
  - vae: VAE
- **Outputs:** LATENT

