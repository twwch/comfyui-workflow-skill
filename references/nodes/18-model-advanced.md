## 18. Model Advanced Nodes

### ModelSamplingDiscrete
- **Display**: ModelSamplingDiscrete
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | sampling (COMBO: eps/v_prediction/lcm/x0/img_to_img/img_to_img_flow) | zsnr (BOOLEAN, default=False)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingContinuousEDM
- **Display**: ModelSamplingContinuousEDM
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | sampling (COMBO: v_prediction/edm/edm_playground_v2.5/eps/cosmos_rflow) | sigma_max (FLOAT, default=120.0) | sigma_min (FLOAT, default=0.002)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingContinuousV
- **Display**: ModelSamplingContinuousV
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | sampling (COMBO: v_prediction) | sigma_max (FLOAT, default=500.0) | sigma_min (FLOAT, default=0.03)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingStableCascade
- **Display**: ModelSamplingStableCascade
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | shift (FLOAT, default=2.0, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingSD3
- **Display**: ModelSamplingSD3
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | shift (FLOAT, default=3.0, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingAuraFlow
- **Display**: ModelSamplingAuraFlow
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | shift (FLOAT, default=1.73, min=0.0, max=100.0)
- **Outputs**: MODEL [0]
- **Function**: patch_aura

### ModelSamplingFlux
- **Display**: ModelSamplingFlux
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | max_shift (FLOAT, default=1.15) | base_shift (FLOAT, default=0.5) | width (INT, default=1024) | height (INT, default=1024)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelSamplingLTXV
- **Display**: ModelSamplingLTXV
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | max_shift (FLOAT, default=2.05) | base_shift (FLOAT, default=0.95)
- **Inputs (optional)**: latent (LATENT)
- **Outputs**: MODEL [0]
- **Function**: execute

### RescaleCFG
- **Display**: RescaleCFG
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | multiplier (FLOAT, default=0.7, min=0.0, max=1.0)
- **Outputs**: MODEL [0]
- **Function**: patch

### ModelComputeDtype
- **Display**: ModelComputeDtype
- **Category**: advanced/debug/model
- **Inputs (required)**: model (MODEL) | dtype (COMBO: default/fp32/fp16/bf16)
- **Outputs**: MODEL [0]
- **Function**: patch

### RenormCFG
- **Display**: RenormCFG
- **Category**: advanced/model
- **Inputs (required)**: model (MODEL) | cfg_trunc (FLOAT, default=100) | renorm_cfg (FLOAT, default=1.0)
- **Outputs**: MODEL [0]
- **Function**: execute

---
