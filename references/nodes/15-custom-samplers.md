## 15. Custom Samplers & Schedulers

### SamplerCustom
- **Display**: SamplerCustom
- **Category**: sampling/custom_sampling
- **Inputs (required)**: model (MODEL) | add_noise (BOOLEAN, default=True) | noise_seed (INT) | cfg (FLOAT, default=8.0) | positive (CONDITIONING) | negative (CONDITIONING) | sampler (SAMPLER) | sigmas (SIGMAS) | latent_image (LATENT)
- **Outputs**: LATENT [0] (output), LATENT [1] (denoised_output)
- **Function**: execute

### SamplerCustomAdvanced
- **Display**: SamplerCustomAdvanced
- **Category**: sampling/custom_sampling
- **Inputs (required)**: noise (NOISE) | guider (GUIDER) | sampler (SAMPLER) | sigmas (SIGMAS) | latent_image (LATENT)
- **Outputs**: LATENT [0] (output), LATENT [1] (denoised_output)
- **Function**: execute

### BasicScheduler
- **Display**: BasicScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model (MODEL) | scheduler (COMBO) | steps (INT, default=20) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### KarrasScheduler
- **Display**: KarrasScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | sigma_max (FLOAT, default=14.614642) | sigma_min (FLOAT, default=0.0291675) | rho (FLOAT, default=7.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### ExponentialScheduler
- **Display**: ExponentialScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | sigma_max (FLOAT, default=14.614642) | sigma_min (FLOAT, default=0.0291675)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### PolyexponentialScheduler
- **Display**: PolyexponentialScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | sigma_max (FLOAT, default=14.614642) | sigma_min (FLOAT, default=0.0291675) | rho (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### LaplaceScheduler
- **Display**: LaplaceScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | sigma_max (FLOAT) | sigma_min (FLOAT) | mu (FLOAT, default=0.0) | beta (FLOAT, default=0.5)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### SDTurboScheduler
- **Display**: SDTurboScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model (MODEL) | steps (INT, default=1, min=1, max=10) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### BetaSamplingScheduler
- **Display**: BetaSamplingScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model (MODEL) | steps (INT, default=20) | alpha (FLOAT, default=0.6) | beta (FLOAT, default=0.6)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### VPScheduler
- **Display**: VPScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | beta_d (FLOAT, default=19.9) | beta_min (FLOAT, default=0.1) | eps_s (FLOAT, default=0.001)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### AlignYourStepsScheduler
- **Display**: AlignYourStepsScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model_type (COMBO) | steps (INT, default=10) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### GITSScheduler
- **Display**: GITSScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: coeff (FLOAT, default=1.2) | steps (INT, default=10) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### OptimalStepsScheduler
- **Display**: OptimalStepsScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: model_type (COMBO) | steps (INT, default=10) | denoise (FLOAT, default=1.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### LTXVScheduler
- **Display**: LTXVScheduler
- **Category**: sampling/custom_sampling/schedulers
- **Inputs (required)**: steps (INT, default=20) | max_shift (FLOAT, default=2.05) | base_shift (FLOAT, default=0.95) | stretch (BOOLEAN, default=True) | terminal (FLOAT, default=0.1)
- **Inputs (optional)**: latent (LATENT)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### KSamplerSelect
- **Display**: KSamplerSelect
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: sampler_name (COMBO)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMPP_3M_SDE
- **Display**: SamplerDPMPP_3M_SDE
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0) | noise_device (COMBO: gpu/cpu)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMPP_2M_SDE
- **Display**: SamplerDPMPP_2M_SDE
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: solver_type (COMBO: midpoint/heun) | eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0) | noise_device (COMBO: gpu/cpu)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMPP_SDE
- **Display**: SamplerDPMPP_SDE
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0) | r (FLOAT, default=0.5) | noise_device (COMBO: gpu/cpu)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMPP_2S_Ancestral
- **Display**: SamplerDPMPP_2S_Ancestral
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerEulerAncestral
- **Display**: SamplerEulerAncestral
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerEulerAncestralCFGPP
- **Display**: SamplerEulerAncestralCFG++
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: eta (FLOAT, default=1.0, max=1.0) | s_noise (FLOAT, default=1.0, max=10.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerEulerCFGpp
- **Display**: SamplerEulerCFGpp
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: (none)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerLMS
- **Display**: SamplerLMS
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: order (INT, default=4, min=1, max=100)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerDPMAdaptative
- **Display**: SamplerDPMAdaptative
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: order (INT, default=3) | rtol (FLOAT, default=0.05) | atol (FLOAT, default=0.0078) | h_init (FLOAT, default=0.05) | pcoeff (FLOAT, default=0.0) | icoeff (FLOAT, default=1.0) | dcoeff (FLOAT, default=0.0) | accept_safety (FLOAT, default=0.81) | eta (FLOAT, default=0.0) | s_noise (FLOAT, default=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerER_SDE
- **Display**: SamplerER_SDE
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: solver_type (COMBO: ER-SDE/Reverse-time SDE/ODE) | max_stage (INT, default=3, min=1, max=3) | eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerSASolver
- **Display**: SamplerSASolver
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: model (MODEL) | eta (FLOAT, default=1.0) | sde_start_percent (FLOAT, default=0.2) | sde_end_percent (FLOAT, default=0.8) | s_noise (FLOAT, default=1.0) | predictor_order (INT, default=3) | corrector_order (INT, default=4) | use_pece (BOOLEAN) | simple_order_2 (BOOLEAN)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerSEEDS2
- **Display**: SamplerSEEDS2
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: solver_type (COMBO: phi_1/phi_2) | eta (FLOAT, default=1.0) | s_noise (FLOAT, default=1.0) | r (FLOAT, default=0.5, min=0.01, max=1.0)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SamplerLCMUpscale
- **Display**: SamplerLCMUpscale
- **Category**: sampling/custom_sampling/samplers
- **Inputs (required)**: scale_ratio (FLOAT, default=1.0) | scale_steps (INT, default=-1) | upscale_method (COMBO)
- **Outputs**: SAMPLER [0]
- **Function**: execute

### SplitSigmas
- **Display**: SplitSigmas
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS) | step (INT, default=0)
- **Outputs**: SIGMAS [0] (high_sigmas), SIGMAS [1] (low_sigmas)
- **Function**: execute

### SplitSigmasDenoise
- **Display**: SplitSigmasDenoise
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS) | denoise (FLOAT, default=1.0, min=0.0, max=1.0)
- **Outputs**: SIGMAS [0] (high_sigmas), SIGMAS [1] (low_sigmas)
- **Function**: execute

### FlipSigmas
- **Display**: FlipSigmas
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### SetFirstSigma
- **Display**: SetFirstSigma
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS) | sigma (FLOAT, default=136.0)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### ExtendIntermediateSigmas
- **Display**: ExtendIntermediateSigmas
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: sigmas (SIGMAS) | steps (INT, default=2) | start_at_sigma (FLOAT, default=-1.0) | end_at_sigma (FLOAT, default=12.0) | spacing (COMBO: linear/cosine/sine)
- **Outputs**: SIGMAS [0]
- **Function**: execute

### SamplingPercentToSigma
- **Display**: SamplingPercentToSigma
- **Category**: sampling/custom_sampling/sigmas
- **Inputs (required)**: model (MODEL) | sampling_percent (FLOAT, default=0.0) | return_actual_sigma (BOOLEAN, default=False)
- **Outputs**: FLOAT [0] (sigma_value)
- **Function**: execute

### BasicGuider
- **Display**: BasicGuider
- **Category**: sampling/custom_sampling/guiders
- **Inputs (required)**: model (MODEL) | conditioning (CONDITIONING)
- **Outputs**: GUIDER [0]
- **Function**: execute

### CFGGuider
- **Display**: CFGGuider
- **Category**: sampling/custom_sampling/guiders
- **Inputs (required)**: model (MODEL) | positive (CONDITIONING) | negative (CONDITIONING) | cfg (FLOAT, default=8.0)
- **Outputs**: GUIDER [0]
- **Function**: execute

### DualCFGGuider
- **Display**: DualCFGGuider
- **Category**: sampling/custom_sampling/guiders
- **Inputs (required)**: model (MODEL) | cond1 (CONDITIONING) | cond2 (CONDITIONING) | negative (CONDITIONING) | cfg_conds (FLOAT, default=8.0) | cfg_cond2_negative (FLOAT, default=8.0) | style (COMBO: regular/nested)
- **Outputs**: GUIDER [0]
- **Function**: execute

### PerpNegGuider
- **Display**: PerpNegGuider
- **Category**: sampling/custom_sampling/guiders
- **Inputs (required)**: model (MODEL) | positive (CONDITIONING) | negative (CONDITIONING) | empty_conditioning (CONDITIONING) | cfg (FLOAT, default=8.0) | neg_scale (FLOAT, default=1.0)
- **Outputs**: GUIDER [0]
- **Function**: execute

### DisableNoise
- **Display**: DisableNoise
- **Category**: sampling/custom_sampling/noise
- **Inputs (required)**: (none)
- **Outputs**: NOISE [0]
- **Function**: execute

### RandomNoise
- **Display**: RandomNoise
- **Category**: sampling/custom_sampling/noise
- **Inputs (required)**: noise_seed (INT)
- **Outputs**: NOISE [0]
- **Function**: execute

### AddNoise
- **Display**: AddNoise
- **Category**: _for_testing/custom_sampling/noise
- **Inputs (required)**: model (MODEL) | noise (NOISE) | sigmas (SIGMAS) | latent_image (LATENT)
- **Outputs**: LATENT [0]
- **Function**: execute
- **Notes**: Experimental

### ManualSigmas
- **Display**: ManualSigmas
- **Category**: _for_testing/custom_sampling
- **Inputs (required)**: sigmas (STRING, default="1, 0.5")
- **Outputs**: SIGMAS [0]
- **Function**: execute
- **Notes**: Experimental

---
