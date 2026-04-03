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
