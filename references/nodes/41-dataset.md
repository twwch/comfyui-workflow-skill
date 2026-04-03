## 41. Dataset Nodes

### LoadImageDataSetFromFolder
- **Display**: LoadImageDataSetFromFolder
- **Category**: training/dataset
- **Inputs (required)**: folder_path (STRING)
- **Outputs**: IMAGE [0] (list)
- **Function**: execute

### LoadImageTextDataSetFromFolder
- **Display**: LoadImageTextDataSetFromFolder
- **Category**: training/dataset
- **Inputs (required)**: folder_path (STRING)
- **Outputs**: IMAGE [0] (list), STRING [1] (list)
- **Function**: execute

### SaveImageDataSetToFolder
- **Display**: SaveImageDataSetToFolder
- **Category**: training/dataset
- **Inputs (required)**: images (IMAGE, list) | folder_path (STRING)
- **Outputs**: (none - output node)
- **Function**: execute

### SaveImageTextDataSetToFolder
- **Display**: SaveImageTextDataSetToFolder
- **Category**: training/dataset
- **Inputs (required)**: images (IMAGE, list) | texts (STRING, list) | folder_path (STRING)
- **Outputs**: (none - output node)
- **Function**: execute

### ShuffleImageTextDataset
- **Display**: ShuffleImageTextDataset
- **Category**: training/dataset
- **Inputs (required)**: images (IMAGE, list) | texts (STRING, list) | seed (INT)
- **Outputs**: IMAGE [0] (list), STRING [1] (list)
- **Function**: execute

### ResolutionBucket
- **Display**: ResolutionBucket
- **Category**: training/dataset
- **Inputs (required)**: width (INT) | height (INT) | bucket_size (INT)
- **Outputs**: INT [0] (width), INT [1] (height)
- **Function**: execute

### MakeTrainingDataset
- **Display**: MakeTrainingDataset
- **Category**: training/dataset
- **Inputs (required)**: images (IMAGE, list) | texts (STRING, list) | batch_size (INT)
- **Outputs**: DATASET [0]
- **Function**: execute

### SaveTrainingDataset
- **Display**: SaveTrainingDataset
- **Category**: training/dataset
- **Inputs (required)**: dataset (DATASET) | filename_prefix (STRING)
- **Outputs**: (none - output node)
- **Function**: execute

### LoadTrainingDataset
- **Display**: LoadTrainingDataset
- **Category**: training/dataset
- **Inputs (required)**: dataset_name (COMBO)
- **Outputs**: DATASET [0]
- **Function**: execute

---
