## 39. Object Detection Nodes

### RTDETR_detect
- **Display**: RTDETR_detect
- **Category**: image/detection
- **Inputs (required)**: model_name (COMBO) | image (IMAGE) | threshold (FLOAT, default=0.5)
- **Outputs**: BBOXES [0]
- **Function**: execute

### DrawBBoxes
- **Display**: DrawBBoxes
- **Category**: image/detection
- **Inputs (required)**: image (IMAGE) | bboxes (BBOXES)
- **Outputs**: IMAGE [0]
- **Function**: execute

### SDPoseDrawKeypoints
- **Display**: SDPoseDrawKeypoints
- **Category**: image/pose
- **Inputs (required)**: keypoints (KEYPOINTS) | width (INT) | height (INT)
- **Outputs**: IMAGE [0]
- **Function**: execute

### SDPoseKeypointExtractor
- **Display**: SDPoseKeypointExtractor
- **Category**: image/pose
- **Inputs (required)**: model_name (COMBO) | image (IMAGE)
- **Outputs**: KEYPOINTS [0]
- **Function**: execute

### SDPoseFaceBBoxes
- **Display**: SDPoseFaceBBoxes
- **Category**: image/pose
- **Inputs (required)**: keypoints (KEYPOINTS)
- **Outputs**: BBOXES [0]
- **Function**: execute

### CropByBBoxes
- **Display**: CropByBBoxes
- **Category**: image
- **Inputs (required)**: image (IMAGE) | bboxes (BBOXES) | padding (INT, default=0)
- **Outputs**: IMAGE [0]
- **Function**: execute

---
