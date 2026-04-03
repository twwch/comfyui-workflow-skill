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
