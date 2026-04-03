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
