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
