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
