# ComfyUI Node Registry - Additions

New nodes extracted from comfy_extras source files, not yet in the main node registry under `references/nodes/`.

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

