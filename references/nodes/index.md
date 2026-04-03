# ComfyUI Node Registry — Index

**Usage:** Read only the category file you need, not the entire registry.

Total: 449 nodes across 42 categories.

| # | Category | File | Nodes | Key Node Types |
|---|----------|------|-------|----------------|
| 1 | Loaders | `nodes/01-loaders.md` | 26 | CheckpointLoaderSimple, CheckpointLoader, unCLIPCheckpointLoader, DiffusersLoader, VAELoader, ... (+21) |
| 2 | Conditioning | `nodes/02-conditioning.md` | 24 | CLIPTextEncode, CLIPSetLastLayer, CLIPVisionEncode, ConditioningCombine, ConditioningAverage, ... (+19) |
| 3 | Sampling | `nodes/03-sampling.md` | 2 | KSampler, KSamplerAdvanced |
| 4 | Latent | `nodes/04-latent.md` | 36 | EmptyLatentImage, VAEDecode, VAEEncode, VAEDecodeTiled, VAEEncodeTiled, ... (+31) |
| 5 | Image | `nodes/05-image.md` | 33 | SaveImage, PreviewImage, LoadImage, LoadImageMask, LoadImageOutput, ... (+28) |
| 6 | ControlNet Nodes | `nodes/06-controlnet.md` | 8 | ControlNetApply, ControlNetApplyAdvanced, SetUnionControlNetType, ControlNetInpaintingAliMamaApply, ControlNetApplySD3, ... (+3) |
| 7 | Video / Wan Nodes | `nodes/07-video-wan.md` | 28 | WanImageToVideo, WanFunControlToVideo, Wan22FunControlToVideo, WanFirstLastFrameToVideo, WanFunInpaintToVideo, ... (+23) |
| 8 | Video I/O Nodes | `nodes/08-video-io.md` | 6 | SaveWEBM, SaveVideo, CreateVideo, GetVideoComponents, LoadVideo, ... (+1) |
| 9 | FLUX Nodes | `nodes/09-flux.md` | 8 | CLIPTextEncodeFlux, FluxGuidance, FluxDisableGuidance, FluxKontextImageScale, FluxKontextMultiReferenceLatentMethod, ... (+3) |
| 10 | SDXL Nodes | `nodes/10-sdxl.md` | 2 | CLIPTextEncodeSDXL, CLIPTextEncodeSDXLRefiner |
| 11 | SD3 Nodes | `nodes/11-sd3.md` | 5 | CLIPTextEncodeSD3, EmptySD3LatentImage, SkipLayerGuidanceSD3, SkipLayerGuidanceDiT, SkipLayerGuidanceDiTSimple |
| 12 | HunyuanVideo Nodes | `nodes/12-hunyuan-video.md` | 10 | CLIPTextEncodeHunyuanDiT, TextEncodeHunyuanVideo_ImageToVideo, EmptyHunyuanLatentVideo, EmptyHunyuanVideo15Latent, HunyuanVideo15ImageToVideo, ... (+5) |
| 13 | Upscale Nodes | `nodes/13-upscale.md` | 5 | ImageUpscaleWithModel, ImageScaleToTotalPixels, ResizeImageMaskNode, SD_4XUpscale_Conditioning, LTXVLatentUpsampler |
| 14 | Post Processing Nodes | `nodes/14-post-processing.md` | 8 | ImageBlend, ImageBlur, ImageQuantize, ImageSharpen, Canny, ... (+3) |
| 15 | Custom Samplers & Schedulers | `nodes/15-custom-samplers.md` | 42 | SamplerCustom, SamplerCustomAdvanced, BasicScheduler, KarrasScheduler, ExponentialScheduler, ... (+37) |
| 16 | Mask Nodes | `nodes/16-mask.md` | 12 | MaskToImage, ImageToMask, ImageColorToMask, SolidMask, InvertMask, ... (+7) |
| 17 | Compositing Nodes | `nodes/17-compositing.md` | 3 | PorterDuffImageComposite, SplitImageWithAlpha, JoinImageWithAlpha |
| 18 | Model Advanced Nodes | `nodes/18-model-advanced.md` | 11 | ModelSamplingDiscrete, ModelSamplingContinuousEDM, ModelSamplingContinuousV, ModelSamplingStableCascade, ModelSamplingSD3, ... (+6) |
| 19 | Model Merging Nodes | `nodes/19-model-merging.md` | 16 | ModelMergeSimple, ModelMergeBlocks, ModelMergeSubtract, ModelMergeAdd, CLIPMergeSimple, ... (+11) |
| 20 | Model Patches | `nodes/20-model-patches.md` | 26 | FreeU, FreeU_V2, PerturbedAttentionGuidance, SelfAttentionGuidance, PerpNeg, ... (+21) |
| 21 | Audio Nodes | `nodes/21-audio.md` | 23 | EmptyLatentAudio, VAEEncodeAudio, VAEDecodeAudio, VAEDecodeAudioTiled, SaveAudio, ... (+18) |
| 22 | LTXV Nodes | `nodes/22-ltxv.md` | 13 | EmptyLTXVLatentVideo, LTXVImgToVideo, LTXVImgToVideoInplace, LTXVAddGuide, LTXVCropGuides, ... (+8) |
| 23 | Stable Cascade Nodes | `nodes/23-stable-cascade.md` | 4 | StableCascade_EmptyLatentImage, StableCascade_StageC_VAEEncode, StableCascade_StageB_Conditioning, StableCascade_SuperResolutionControlnet |
| 24 | Stable 3D Nodes | `nodes/24-stable-3d.md` | 3 | StableZero123_Conditioning, StableZero123_Conditioning_Batched, SV3D_Conditioning |
| 25 | Cosmos Nodes | `nodes/25-cosmos.md` | 3 | EmptyCosmosLatentVideo, CosmosImageToVideoLatent, CosmosPredict2ImageToVideoLatent |
| 26 | Mochi Nodes | `nodes/26-mochi.md` | 1 | EmptyMochiLatentVideo |
| 27 | HiDream Nodes | `nodes/27-hidream.md` | 1 | CLIPTextEncodeHiDream |
| 28 | Lumina2 Nodes | `nodes/28-lumina2.md` | 1 | CLIPTextEncodeLumina2 |
| 29 | PixArt Nodes | `nodes/29-pixart.md` | 1 | CLIPTextEncodePixArtAlpha |
| 30 | Chroma / Radiance Nodes | `nodes/30-chroma-radiance.md` | 1 | EmptyChromaRadianceLatentImage |
| 31 | Hunyuan 3D Nodes | `nodes/31-hunyuan-3d.md` | 7 | EmptyLatentHunyuan3Dv2, Hunyuan3Dv2Conditioning, Hunyuan3Dv2ConditioningMultiView, VAEDecodeHunyuan3D, VoxelToMeshBasic, ... (+2) |
| 32 | 3D Nodes | `nodes/32-3d.md` | 2 | Load3D, Preview3D |
| 33 | Kandinsky Nodes | `nodes/33-kandinsky.md` | 3 | Kandinsky5ImageToVideo, NormalizeVideoLatentStart, CLIPTextEncodeKandinsky5 |
| 34 | Qwen / OmniGen / ZImage Nodes | `nodes/34-qwen-omnigen.md` | 4 | TextEncodeQwenImageEdit, TextEncodeQwenImageEditPlus, EmptyQwenImageLayeredLatentImage, TextEncodeZImageOmni |
| 35 | String Nodes | `nodes/35-string.md` | 11 | StringConcatenate, StringSubstring, StringLength, CaseConverter, StringTrim, ... (+6) |
| 36 | Primitive Nodes | `nodes/36-primitive.md` | 5 | PrimitiveString, PrimitiveStringMultiline, PrimitiveInt, PrimitiveFloat, PrimitiveBoolean |
| 37 | Logic / Utility Nodes | `nodes/37-logic-utility.md` | 15 | ComfySwitchNode, ComfySoftSwitchNode, ConvertStringToComboNode, InvertBooleanNode, ComfyNumberConvert, ... (+10) |
| 38 | Text Generation Nodes | `nodes/38-text-generation.md` | 2 | TextGenerate, TextGenerateLTX2Prompt |
| 39 | Object Detection Nodes | `nodes/39-object-detection.md` | 6 | RTDETR_detect, DrawBBoxes, SDPoseDrawKeypoints, SDPoseKeypointExtractor, SDPoseFaceBBoxes, ... (+1) |
| 40 | Training Nodes | `nodes/40-training.md` | 5 | TrainLoraNode, LoraModelLoader, SaveLoRA, LossGraphNode, LoraSave |
| 41 | Dataset Nodes | `nodes/41-dataset.md` | 9 | LoadImageDataSetFromFolder, LoadImageTextDataSetFromFolder, SaveImageDataSetToFolder, SaveImageTextDataSetToFolder, ShuffleImageTextDataset, ... (+4) |
| 42 | Debug / Misc Nodes | `nodes/42-debug-misc.md` | 18 | LoraLoaderBypass, LoraLoaderBypassModelOnly, WebcamCapture, nodes_audio, nodes_audio_encoder, ... (+13) |

## Quick Lookup

Common nodes and which file to read:

| Need | Read |
|------|------|
| CheckpointLoaderSimple, UNETLoader, VAELoader, CLIPLoader, LoraLoader | `nodes/01-loaders.md` |
| CLIPTextEncode, CLIPTextEncodeFlux, CLIPTextEncodeSD3 | `nodes/02-conditioning.md` |
| KSampler, KSamplerAdvanced | `nodes/03-sampling.md` |
| EmptyLatentImage, VAEDecode, VAEEncode | `nodes/04-latent.md` |
| SaveImage, LoadImage, ImageScale | `nodes/05-image.md` |
| ControlNetLoader, ControlNetApplyAdvanced | `nodes/06-controlnet.md` |
| WanImageToVideo, WanCameraImageToVideo, WanFirstLastFrameToVideo | `nodes/07-video-wan.md` |
| CLIPTextEncodeFlux, BasicGuider, SamplerCustomAdvanced | `nodes/09-flux.md` |
| BasicScheduler, KSamplerSelect, RandomNoise | `nodes/15-custom-samplers.md` |
| EmptyLTXVLatentVideo, LTXVImgToVideo | `nodes/22-ltxv.md` |
| EmptyCosmosLatentVideo, CosmosImageToVideoLatent | `nodes/25-cosmos.md` |
| StableAudio, EmptyLatentAudio, VAEDecodeAudio | `nodes/21-audio.md` |
| Hunyuan3Dv2Conditioning, VAEDecodeHunyuan3D, SaveGLB | `nodes/31-hunyuan-3d.md` |
