## 31. Hunyuan 3D Nodes

### EmptyLatentHunyuan3Dv2
- **Display**: EmptyLatentHunyuan3Dv2
- **Category**: latent/3d
- **Inputs (required)**: resolution (INT, default=3072) | batch_size (INT, default=1)
- **Outputs**: LATENT [0]
- **Function**: execute

### Hunyuan3Dv2Conditioning
- **Display**: Hunyuan3Dv2Conditioning
- **Category**: conditioning/video_models
- **Inputs (required)**: clip_vision_output (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute

### Hunyuan3Dv2ConditioningMultiView
- **Display**: Hunyuan3Dv2ConditioningMultiView
- **Category**: conditioning/video_models
- **Inputs (optional)**: front (CLIP_VISION_OUTPUT) | left (CLIP_VISION_OUTPUT) | back (CLIP_VISION_OUTPUT) | right (CLIP_VISION_OUTPUT)
- **Outputs**: CONDITIONING [0] (positive), CONDITIONING [1] (negative)
- **Function**: execute

### VAEDecodeHunyuan3D
- **Display**: VAEDecodeHunyuan3D
- **Category**: latent/3d
- **Inputs (required)**: samples (LATENT) | vae (VAE) | num_chunks (INT, default=8000) | octree_resolution (INT, default=256)
- **Outputs**: VOXEL [0]
- **Function**: execute

### VoxelToMeshBasic
- **Display**: VoxelToMeshBasic
- **Category**: 3d
- **Inputs (required)**: voxel (VOXEL) | threshold (FLOAT, default=0.6)
- **Outputs**: MESH [0]
- **Function**: execute

### VoxelToMesh
- **Display**: VoxelToMesh
- **Category**: 3d
- **Inputs (required)**: voxel (VOXEL) | algorithm (COMBO: surface net/basic) | threshold (FLOAT, default=0.6)
- **Outputs**: MESH [0]
- **Function**: execute

### SaveGLB
- **Display**: Save 3D Model
- **Category**: 3d
- **Inputs (required)**: mesh (MESH or File3D) | filename_prefix (STRING, default="mesh/ComfyUI")
- **Outputs**: (none - output node)
- **Function**: execute

---
