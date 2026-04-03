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
