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
