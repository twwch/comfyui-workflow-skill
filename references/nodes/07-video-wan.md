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
