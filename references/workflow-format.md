# ComfyUI Workflow JSON Format Specification

## Two Formats

ComfyUI uses two JSON formats:
- **API format** — submitted to `/prompt` for execution (this is what we generate)
- **UI format** — Litegraph serialization with visual layout (saved by the web UI)

## API Format Structure

### Top-level

```json
{
  "<node_id>": {
    "class_type": "NodeClassName",
    "inputs": {
      "<input_name>": <value_or_link>
    },
    "_meta": {
      "title": "Display Title"
    }
  }
}
```

### Input Values

**Literal values:**
```json
"text": "a beautiful landscape",
"seed": 42,
"width": 1024,
"denoise": 1.0,
"sampler_name": "euler"
```

**Links to other nodes:**
```json
"model": ["4", 0],
"clip": ["4", 1]
```
Format: `["source_node_id_string", output_slot_index_int]`

The slot index maps to the source node's `RETURN_TYPES` tuple (0-based).

### Validation Rules

1. Every node must have `class_type` matching a registered node
2. At least one OUTPUT_NODE must exist (SaveImage, PreviewImage, SaveVideo, etc.)
3. All `required` inputs must be provided
4. Links must be `[string, int]` format
5. Source node's `RETURN_TYPES[slot]` must match target input type
6. Literal values must satisfy min/max constraints
7. Graph must be a DAG (no cycles)

### Common Data Types

| Type | Description | Flow |
|------|-------------|------|
| MODEL | Diffusion model | node→node |
| CLIP | Text encoder | node→node |
| VAE | Autoencoder | node→node |
| CONDITIONING | Encoded prompt | node→node |
| LATENT | Latent tensor | node→node |
| IMAGE | Decoded image | node→node |
| MASK | Binary mask | node→node |
| CONTROL_NET | ControlNet model | node→node |
| CLIP_VISION | CLIP vision model | node→node |
| CLIP_VISION_OUTPUT | Encoded vision | node→node |
| UPSCALE_MODEL | Upscale model | node→node |
| INT | Integer | literal only |
| FLOAT | Float | literal only |
| STRING | Text | literal only |
| BOOLEAN | Bool | literal only |

### Available Samplers

euler, euler_cfg_pp, euler_ancestral, euler_ancestral_cfg_pp, heun, heunpp2, dpm_2, dpm_2_ancestral, lms, dpm_fast, dpm_adaptive, dpmpp_2s_ancestral, dpmpp_sde, dpmpp_sde_gpu, dpmpp_2m, dpmpp_2m_sde, dpmpp_2m_sde_gpu, dpmpp_3m_sde, dpmpp_3m_sde_gpu, ddpm, lcm, ipndm, ipndm_v, deis, ddim, uni_pc, uni_pc_bh2

### Available Schedulers

normal, karras, exponential, sgm_uniform, simple, ddim_uniform, beta
