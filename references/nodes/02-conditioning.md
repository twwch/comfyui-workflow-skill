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
