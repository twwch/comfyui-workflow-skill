#!/usr/bin/env python3
"""Generate ALL missing ComfyUI workflow templates.

Existing templates (10):
  sd15-txt2img, sdxl-txt2img, flux-txt2img,
  sd15-controlnet, sd15-inpaint, sdxl-lora,
  upscale-model, wan22-txt2vid, wan22-img2vid, hunyuan-video

Templates to generate (13):
  sd3-txt2img, sd15-img2img, sd15-lora,
  sdxl-controlnet, sdxl-inpaint, sdxl-img2img,
  flux-img2img, flux-lora,
  ltxv-txt2vid, ltxv-img2vid, mochi-txt2vid,
  cosmos-img2vid, stable-audio, hunyuan-video-i2v,
  hunyuan3d-v2, stable-cascade
"""

import json
import uuid
import os

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates")


# ============================================================
# Helpers
# ============================================================

def conn_input(name, typ, link):
    return {"name": name, "type": typ, "link": link, "label": name, "localized_name": name}

def opt_conn_input(name, typ, link):
    return {"name": name, "type": typ, "link": link, "shape": 7, "label": name, "localized_name": name}

def widget_input(name, typ):
    return {"label": name, "localized_name": name, "name": name, "type": typ,
            "widget": {"name": name}, "link": None}

def make_output(name, typ, links, slot=0):
    return {"name": name, "type": typ, "links": links or [], "slot_index": slot,
            "label": name, "localized_name": name}

def null_output(name, typ, slot=0):
    return {"name": name, "type": typ, "links": None, "slot_index": slot,
            "label": name, "localized_name": name}


class TB:
    """Template Builder."""
    def __init__(self):
        self.nodes = []
        self._links = []
        self._lid = 0
        self._order = 0
        self._out = {}  # (node_id, slot) -> [link_ids]

    def L(self, src, src_slot, tgt, tgt_slot, typ):
        self._lid += 1
        self._links.append([self._lid, src, src_slot, tgt, tgt_slot, typ])
        self._out.setdefault((src, src_slot), []).append(self._lid)
        return self._lid

    def outs(self, nid, slot):
        return self._out.get((nid, slot)) or []

    def node(self, nid, ntype, pos, size, inputs, outputs,
             title=None, wv=None, color=None, bgcolor=None):
        n = {"id": nid, "type": ntype, "pos": pos, "size": size,
             "flags": {}, "order": self._order, "mode": 0,
             "inputs": inputs, "outputs": outputs,
             "properties": {"Node name for S&R": ntype}}
        self._order += 1
        if title: n["title"] = title
        if wv is not None: n["widgets_values"] = wv
        if color: n["color"] = color; n["bgcolor"] = bgcolor
        self.nodes.append(n)

    def build(self, groups=None):
        return {
            "id": str(uuid.uuid4()), "revision": 0,
            "last_node_id": max(n["id"] for n in self.nodes),
            "last_link_id": self._lid,
            "nodes": self.nodes, "links": self._links,
            "groups": groups or [], "config": {}, "extra": {}, "version": 0.4
        }


def save(name, workflow):
    path = os.path.join(TEMPLATES_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(workflow, f, indent=2, ensure_ascii=False)
    print(f"  {name} ({len(workflow['nodes'])} nodes, {len(workflow['links'])} links)")


# ============================================================
# SD3 Text-to-Image
# ============================================================

def build_sd3_txt2img():
    t = TB()
    # Node 1: UNETLoader
    # Node 2: TripleCLIPLoader
    # Node 3: VAELoader
    # Node 4: CLIPTextEncodeSD3 (positive)
    # Node 5: CLIPTextEncodeSD3 (negative)
    # Node 6: EmptySD3LatentImage
    # Node 7: KSampler
    # Node 8: VAEDecode
    # Node 9: SaveImage

    l1 = t.L(2, 0, 4, 0, "CLIP")   # CLIP -> pos encode
    l2 = t.L(2, 0, 5, 0, "CLIP")   # CLIP -> neg encode
    l3 = t.L(4, 0, 7, 1, "CONDITIONING")  # pos -> KSampler
    l4 = t.L(5, 0, 7, 2, "CONDITIONING")  # neg -> KSampler
    l5 = t.L(1, 0, 7, 0, "MODEL")  # model -> KSampler
    l6 = t.L(6, 0, 7, 3, "LATENT") # latent -> KSampler
    l7 = t.L(7, 0, 8, 0, "LATENT") # KSampler -> VAEDecode
    l8 = t.L(3, 0, 8, 1, "VAE")    # VAE -> VAEDecode
    l9 = t.L(8, 0, 9, 0, "IMAGE")  # VAEDecode -> SaveImage

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load SD3 Model", wv=["sd3_medium_incl_clips_t5xxlfp8.safetensors", "default"])

    t.node(2, "TripleCLIPLoader", [0, 130], [400, 120],
        [widget_input("clip_name1", "COMBO"), widget_input("clip_name2", "COMBO"), widget_input("clip_name3", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load Triple CLIP (SD3)",
        wv=["clip_l.safetensors", "clip_g.safetensors", "t5xxl_fp16.safetensors"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["sd3_vae.safetensors"])

    t.node(4, "CLIPTextEncodeSD3", [450, 0], [350, 200],
        [conn_input("clip", "CLIP", l1),
         widget_input("clip_l", "STRING"), widget_input("clip_g", "STRING"),
         widget_input("t5xxl", "STRING"), widget_input("empty_padding", "COMBO")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Positive Prompt",
        wv=["beautiful landscape", "a stunning mountain landscape with a crystal clear lake, golden hour, dramatic clouds, photorealistic",
            "a stunning mountain landscape with a crystal clear lake at golden hour, dramatic volumetric clouds, rays of sunlight, photorealistic, masterpiece, 8k uhd",
            "none"],
        color="#232", bgcolor="#353")

    t.node(5, "CLIPTextEncodeSD3", [450, 250], [350, 200],
        [conn_input("clip", "CLIP", l2),
         widget_input("clip_l", "STRING"), widget_input("clip_g", "STRING"),
         widget_input("t5xxl", "STRING"), widget_input("empty_padding", "COMBO")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Negative Prompt",
        wv=["ugly, blurry", "worst quality, low quality, blurry, deformed, watermark",
            "worst quality, low quality, blurry, deformed, ugly, watermark, text, oversaturated",
            "none"],
        color="#322", bgcolor="#533")

    t.node(6, "EmptySD3LatentImage", [450, 500], [225, 106],
        [widget_input("width", "INT"), widget_input("height", "INT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        wv=[1024, 1024, 1])

    t.node(7, "KSampler", [850, 0], [300, 340],
        [conn_input("model", "MODEL", l5), conn_input("positive", "CONDITIONING", l3),
         conn_input("negative", "CONDITIONING", l4), conn_input("latent_image", "LATENT", l6),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(7, 0))],
        wv=[0, "randomize", 28, 4.5, "dpmpp_2m", "sgm_uniform", 1])

    t.node(8, "VAEDecode", [1200, 0], [265, 72],
        [conn_input("samples", "LATENT", l7), conn_input("vae", "VAE", l8)],
        [make_output("IMAGE", "IMAGE", t.outs(8, 0))])

    t.node(9, "SaveImage", [1200, 120], [320, 270],
        [conn_input("images", "IMAGE", l9), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_SD3"])

    return t.build()


# ============================================================
# SD 1.5 Image-to-Image
# ============================================================

def build_sd15_img2img():
    t = TB()
    l1 = t.L(1, 0, 6, 0, "MODEL")
    l2 = t.L(1, 1, 3, 0, "CLIP")
    l3 = t.L(1, 1, 4, 0, "CLIP")
    l4 = t.L(1, 2, 5, 1, "VAE")
    l5 = t.L(3, 0, 6, 1, "CONDITIONING")
    l6 = t.L(4, 0, 6, 2, "CONDITIONING")
    l7 = t.L(2, 0, 5, 0, "IMAGE")
    l8 = t.L(5, 0, 6, 3, "LATENT")
    l9 = t.L(6, 0, 7, 0, "LATENT")
    l10 = t.L(1, 2, 7, 1, "VAE")
    l11 = t.L(7, 0, 8, 0, "IMAGE")

    t.node(1, "CheckpointLoaderSimple", [0, 0], [315, 98],
        [widget_input("ckpt_name", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0)),
         make_output("CLIP", "CLIP", t.outs(1, 1), 1),
         make_output("VAE", "VAE", t.outs(1, 2), 2)],
        title="Load Checkpoint", wv=["v1-5-pruned-emaonly.safetensors"])

    t.node(2, "LoadImage", [0, 150], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(2, 0)),
         null_output("MASK", "MASK", 1)],
        title="Load Input Image", wv=["input.png"])

    t.node(3, "CLIPTextEncode", [350, 0], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(3, 0))],
        title="Positive Prompt",
        wv=["masterpiece, best quality, 1girl, beautiful scenery, detailed face"],
        color="#232", bgcolor="#353")

    t.node(4, "CLIPTextEncode", [350, 170], [280, 120],
        [conn_input("clip", "CLIP", l3), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Negative Prompt",
        wv=["worst quality, low quality, blurry, deformed"],
        color="#322", bgcolor="#533")

    t.node(5, "VAEEncode", [350, 340], [265, 72],
        [conn_input("pixels", "IMAGE", l7), conn_input("vae", "VAE", l4)],
        [make_output("LATENT", "LATENT", t.outs(5, 0))],
        title="Encode Image to Latent")

    t.node(6, "KSampler", [700, 0], [300, 340],
        [conn_input("model", "MODEL", l1), conn_input("positive", "CONDITIONING", l5),
         conn_input("negative", "CONDITIONING", l6), conn_input("latent_image", "LATENT", l8),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        wv=[0, "randomize", 20, 7, "euler", "normal", 0.75])

    t.node(7, "VAEDecode", [1050, 0], [265, 72],
        [conn_input("samples", "LATENT", l9), conn_input("vae", "VAE", l10)],
        [make_output("IMAGE", "IMAGE", t.outs(7, 0))])

    t.node(8, "SaveImage", [1050, 120], [320, 270],
        [conn_input("images", "IMAGE", l11), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_img2img"])

    return t.build()


# ============================================================
# SD 1.5 + LoRA
# ============================================================

def build_sd15_lora():
    t = TB()
    l1 = t.L(1, 0, 2, 0, "MODEL")   # ckpt model -> LoRA
    l2 = t.L(1, 1, 2, 1, "CLIP")    # ckpt clip -> LoRA
    l3 = t.L(2, 0, 6, 0, "MODEL")   # LoRA model -> KSampler
    l4 = t.L(2, 1, 3, 0, "CLIP")    # LoRA clip -> pos
    l5 = t.L(2, 1, 4, 0, "CLIP")    # LoRA clip -> neg
    l6 = t.L(3, 0, 6, 1, "CONDITIONING")
    l7 = t.L(4, 0, 6, 2, "CONDITIONING")
    l8 = t.L(5, 0, 6, 3, "LATENT")
    l9 = t.L(6, 0, 7, 0, "LATENT")
    l10 = t.L(1, 2, 7, 1, "VAE")
    l11 = t.L(7, 0, 8, 0, "IMAGE")

    t.node(1, "CheckpointLoaderSimple", [0, 0], [315, 98],
        [widget_input("ckpt_name", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0)),
         make_output("CLIP", "CLIP", t.outs(1, 1), 1),
         make_output("VAE", "VAE", t.outs(1, 2), 2)],
        title="Load Checkpoint", wv=["v1-5-pruned-emaonly.safetensors"])

    t.node(2, "LoraLoader", [0, 150], [315, 126],
        [conn_input("model", "MODEL", l1), conn_input("clip", "CLIP", l2),
         widget_input("lora_name", "COMBO"),
         widget_input("strength_model", "FLOAT"), widget_input("strength_clip", "FLOAT")],
        [make_output("MODEL", "MODEL", t.outs(2, 0)),
         make_output("CLIP", "CLIP", t.outs(2, 1), 1)],
        title="Load LoRA", wv=["example_lora.safetensors", 1.0, 1.0])

    t.node(3, "CLIPTextEncode", [400, 0], [280, 120],
        [conn_input("clip", "CLIP", l4), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(3, 0))],
        title="Positive Prompt",
        wv=["masterpiece, best quality, 1girl, beautiful, detailed"],
        color="#232", bgcolor="#353")

    t.node(4, "CLIPTextEncode", [400, 170], [280, 120],
        [conn_input("clip", "CLIP", l5), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Negative Prompt",
        wv=["worst quality, low quality, blurry, deformed"],
        color="#322", bgcolor="#533")

    t.node(5, "EmptyLatentImage", [400, 340], [225, 106],
        [widget_input("width", "INT"), widget_input("height", "INT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(5, 0))],
        wv=[512, 512, 1])

    t.node(6, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l3), conn_input("positive", "CONDITIONING", l6),
         conn_input("negative", "CONDITIONING", l7), conn_input("latent_image", "LATENT", l8),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        wv=[0, "randomize", 20, 7, "euler", "normal", 1])

    t.node(7, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l9), conn_input("vae", "VAE", l10)],
        [make_output("IMAGE", "IMAGE", t.outs(7, 0))])

    t.node(8, "SaveImage", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l11), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_LoRA"])

    return t.build()


# ============================================================
# SDXL ControlNet
# ============================================================

def build_sdxl_controlnet():
    t = TB()
    # 1: CheckpointLoader, 2: ControlNetLoader, 3: LoadImage (control),
    # 4: CLIPTextEncode (pos), 5: CLIPTextEncode (neg),
    # 6: ControlNetApplyAdvanced, 7: EmptyLatentImage,
    # 8: KSampler, 9: VAEDecode, 10: SaveImage

    l1 = t.L(1, 1, 4, 0, "CLIP")
    l2 = t.L(1, 1, 5, 0, "CLIP")
    l3 = t.L(4, 0, 6, 0, "CONDITIONING")   # pos -> CNA
    l4 = t.L(5, 0, 6, 1, "CONDITIONING")   # neg -> CNA
    l5 = t.L(2, 0, 6, 2, "CONTROL_NET")    # controlnet -> CNA
    l6 = t.L(3, 0, 6, 3, "IMAGE")          # image -> CNA
    l7 = t.L(6, 0, 8, 1, "CONDITIONING")   # CNA pos -> KSampler
    l8 = t.L(6, 1, 8, 2, "CONDITIONING")   # CNA neg -> KSampler
    l9 = t.L(1, 0, 8, 0, "MODEL")
    l10 = t.L(7, 0, 8, 3, "LATENT")
    l11 = t.L(8, 0, 9, 0, "LATENT")
    l12 = t.L(1, 2, 9, 1, "VAE")
    l13 = t.L(9, 0, 10, 0, "IMAGE")

    t.node(1, "CheckpointLoaderSimple", [0, 0], [315, 98],
        [widget_input("ckpt_name", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0)),
         make_output("CLIP", "CLIP", t.outs(1, 1), 1),
         make_output("VAE", "VAE", t.outs(1, 2), 2)],
        title="Load SDXL Checkpoint", wv=["sd_xl_base_1.0.safetensors"])

    t.node(2, "ControlNetLoader", [0, 150], [290, 82],
        [widget_input("control_net_name", "COMBO")],
        [make_output("CONTROL_NET", "CONTROL_NET", t.outs(2, 0))],
        title="Load ControlNet", wv=["diffusers_xl_canny_full.safetensors"])

    t.node(3, "LoadImage", [0, 280], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(3, 0)),
         null_output("MASK", "MASK", 1)],
        title="Load Control Image", wv=["control_image.png"])

    t.node(4, "CLIPTextEncode", [380, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Positive Prompt",
        wv=["masterpiece, best quality, a beautiful woman standing in a garden, detailed face, photorealistic"],
        color="#232", bgcolor="#353")

    t.node(5, "CLIPTextEncode", [380, 170], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Negative Prompt",
        wv=["worst quality, low quality, blurry, deformed, ugly"],
        color="#322", bgcolor="#533")

    t.node(6, "ControlNetApplyAdvanced", [380, 340], [280, 186],
        [conn_input("positive", "CONDITIONING", l3), conn_input("negative", "CONDITIONING", l4),
         conn_input("control_net", "CONTROL_NET", l5), conn_input("image", "IMAGE", l6),
         widget_input("strength", "FLOAT"), widget_input("start_percent", "FLOAT"),
         widget_input("end_percent", "FLOAT")],
        [make_output("positive", "CONDITIONING", t.outs(6, 0)),
         make_output("negative", "CONDITIONING", t.outs(6, 1), 1)],
        title="Apply ControlNet", wv=[1.0, 0.0, 1.0])

    t.node(7, "EmptyLatentImage", [380, 580], [225, 106],
        [widget_input("width", "INT"), widget_input("height", "INT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(7, 0))],
        wv=[1024, 1024, 1])

    t.node(8, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l9), conn_input("positive", "CONDITIONING", l7),
         conn_input("negative", "CONDITIONING", l8), conn_input("latent_image", "LATENT", l10),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(8, 0))],
        wv=[0, "randomize", 25, 7, "euler", "normal", 1])

    t.node(9, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l11), conn_input("vae", "VAE", l12)],
        [make_output("IMAGE", "IMAGE", t.outs(9, 0))])

    t.node(10, "SaveImage", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l13), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_SDXL_CN"])

    return t.build()


# ============================================================
# SDXL Inpaint
# ============================================================

def build_sdxl_inpaint():
    t = TB()
    l1 = t.L(1, 1, 3, 0, "CLIP")
    l2 = t.L(1, 1, 4, 0, "CLIP")
    l3 = t.L(2, 0, 5, 0, "IMAGE")   # image -> VAEEncodeForInpaint
    l4 = t.L(1, 2, 5, 1, "VAE")
    l5 = t.L(2, 1, 5, 2, "MASK")    # mask -> VAEEncodeForInpaint
    l6 = t.L(1, 0, 6, 0, "MODEL")
    l7 = t.L(3, 0, 6, 1, "CONDITIONING")
    l8 = t.L(4, 0, 6, 2, "CONDITIONING")
    l9 = t.L(5, 0, 6, 3, "LATENT")
    l10 = t.L(6, 0, 7, 0, "LATENT")
    l11 = t.L(1, 2, 7, 1, "VAE")
    l12 = t.L(7, 0, 8, 0, "IMAGE")

    t.node(1, "CheckpointLoaderSimple", [0, 0], [315, 98],
        [widget_input("ckpt_name", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0)),
         make_output("CLIP", "CLIP", t.outs(1, 1), 1),
         make_output("VAE", "VAE", t.outs(1, 2), 2)],
        title="Load SDXL Checkpoint", wv=["sd_xl_base_1.0.safetensors"])

    t.node(2, "LoadImage", [0, 150], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(2, 0)),
         make_output("MASK", "MASK", t.outs(2, 1), 1)],
        title="Load Image + Mask", wv=["input_with_mask.png"])

    t.node(3, "CLIPTextEncode", [380, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(3, 0))],
        title="Positive Prompt",
        wv=["masterpiece, best quality, a beautiful garden with flowers"],
        color="#232", bgcolor="#353")

    t.node(4, "CLIPTextEncode", [380, 170], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Negative Prompt",
        wv=["worst quality, low quality, blurry, deformed, ugly"],
        color="#322", bgcolor="#533")

    t.node(5, "VAEEncodeForInpaint", [380, 340], [265, 106],
        [conn_input("pixels", "IMAGE", l3), conn_input("vae", "VAE", l4),
         conn_input("mask", "MASK", l5), widget_input("grow_mask_by", "INT")],
        [make_output("LATENT", "LATENT", t.outs(5, 0))],
        title="Encode for Inpaint", wv=[6])

    t.node(6, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l6), conn_input("positive", "CONDITIONING", l7),
         conn_input("negative", "CONDITIONING", l8), conn_input("latent_image", "LATENT", l9),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        wv=[0, "randomize", 25, 7, "euler", "normal", 0.85])

    t.node(7, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l10), conn_input("vae", "VAE", l11)],
        [make_output("IMAGE", "IMAGE", t.outs(7, 0))])

    t.node(8, "SaveImage", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l12), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_SDXL_Inpaint"])

    return t.build()


# ============================================================
# SDXL Image-to-Image
# ============================================================

def build_sdxl_img2img():
    t = TB()
    l1 = t.L(1, 0, 6, 0, "MODEL")
    l2 = t.L(1, 1, 3, 0, "CLIP")
    l3 = t.L(1, 1, 4, 0, "CLIP")
    l4 = t.L(1, 2, 5, 1, "VAE")
    l5 = t.L(3, 0, 6, 1, "CONDITIONING")
    l6 = t.L(4, 0, 6, 2, "CONDITIONING")
    l7 = t.L(2, 0, 5, 0, "IMAGE")
    l8 = t.L(5, 0, 6, 3, "LATENT")
    l9 = t.L(6, 0, 7, 0, "LATENT")
    l10 = t.L(1, 2, 7, 1, "VAE")
    l11 = t.L(7, 0, 8, 0, "IMAGE")

    t.node(1, "CheckpointLoaderSimple", [0, 0], [315, 98],
        [widget_input("ckpt_name", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0)),
         make_output("CLIP", "CLIP", t.outs(1, 1), 1),
         make_output("VAE", "VAE", t.outs(1, 2), 2)],
        title="Load SDXL Checkpoint", wv=["sd_xl_base_1.0.safetensors"])

    t.node(2, "LoadImage", [0, 150], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(2, 0)), null_output("MASK", "MASK", 1)],
        title="Load Input Image", wv=["input.png"])

    t.node(3, "CLIPTextEncode", [380, 0], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(3, 0))],
        title="Positive Prompt",
        wv=["masterpiece, best quality, a stunning landscape, photorealistic, 8k"],
        color="#232", bgcolor="#353")

    t.node(4, "CLIPTextEncode", [380, 170], [280, 120],
        [conn_input("clip", "CLIP", l3), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Negative Prompt",
        wv=["worst quality, low quality, blurry, deformed, ugly"],
        color="#322", bgcolor="#533")

    t.node(5, "VAEEncode", [380, 340], [265, 72],
        [conn_input("pixels", "IMAGE", l7), conn_input("vae", "VAE", l4)],
        [make_output("LATENT", "LATENT", t.outs(5, 0))],
        title="Encode Image")

    t.node(6, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l1), conn_input("positive", "CONDITIONING", l5),
         conn_input("negative", "CONDITIONING", l6), conn_input("latent_image", "LATENT", l8),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        wv=[0, "randomize", 25, 7, "euler", "normal", 0.70])

    t.node(7, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l9), conn_input("vae", "VAE", l10)],
        [make_output("IMAGE", "IMAGE", t.outs(7, 0))])

    t.node(8, "SaveImage", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l11), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_SDXL_I2I"])

    return t.build()


# ============================================================
# FLUX Image-to-Image
# ============================================================

def build_flux_img2img():
    t = TB()
    # FLUX uses advanced sampling pipeline
    l1 = t.L(2, 0, 4, 0, "CLIP")       # CLIP -> encode
    l2 = t.L(4, 0, 6, 1, "CONDITIONING") # cond -> guider
    l3 = t.L(1, 0, 6, 0, "MODEL")       # model -> guider
    l4 = t.L(1, 0, 8, 0, "MODEL")       # model -> scheduler
    l5 = t.L(6, 0, 10, 1, "GUIDER")
    l6 = t.L(7, 0, 10, 2, "SAMPLER")
    l7 = t.L(8, 0, 10, 3, "SIGMAS")
    l8 = t.L(9, 0, 10, 0, "NOISE")
    l9 = t.L(5, 0, 10, 4, "LATENT")     # VAEEncode -> SCA
    l10 = t.L(10, 0, 11, 0, "LATENT")
    l11 = t.L(3, 0, 11, 1, "VAE")
    l12 = t.L(11, 0, 12, 0, "IMAGE")
    l13 = t.L(13, 0, 5, 0, "IMAGE")     # LoadImage -> VAEEncode
    l14 = t.L(3, 0, 5, 1, "VAE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load FLUX Model", wv=["flux1-dev.safetensors", "default"])

    t.node(2, "DualCLIPLoader", [0, 130], [315, 120],
        [widget_input("clip_name1", "COMBO"), widget_input("clip_name2", "COMBO"), widget_input("type", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load CLIP (FLUX)", wv=["clip_l.safetensors", "t5xxl_fp16.safetensors", "flux"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["ae.safetensors"])

    t.node(13, "LoadImage", [0, 430], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(13, 0)), null_output("MASK", "MASK", 1)],
        title="Load Input Image", wv=["input.png"])

    t.node(4, "CLIPTextEncodeFlux", [400, 0], [300, 180],
        [conn_input("clip", "CLIP", l1),
         widget_input("clip_l", "STRING"), widget_input("t5xxl", "STRING"),
         widget_input("guidance", "FLOAT")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="FLUX Text Encode",
        wv=["a beautiful woman in a garden",
            "a beautiful woman standing in a lush garden with blooming flowers, soft natural lighting, photorealistic",
            3.5],
        color="#232", bgcolor="#353")

    t.node(5, "VAEEncode", [400, 430], [265, 72],
        [conn_input("pixels", "IMAGE", l13), conn_input("vae", "VAE", l14)],
        [make_output("LATENT", "LATENT", t.outs(5, 0))],
        title="Encode Image")

    t.node(6, "BasicGuider", [750, 0], [225, 72],
        [conn_input("model", "MODEL", l3), conn_input("conditioning", "CONDITIONING", l2)],
        [make_output("GUIDER", "GUIDER", t.outs(6, 0))])

    t.node(7, "KSamplerSelect", [750, 120], [225, 58],
        [widget_input("sampler_name", "COMBO")],
        [make_output("SAMPLER", "SAMPLER", t.outs(7, 0))],
        wv=["euler"])

    t.node(8, "BasicScheduler", [750, 230], [225, 106],
        [conn_input("model", "MODEL", l4),
         widget_input("scheduler", "COMBO"), widget_input("steps", "INT"),
         widget_input("denoise", "FLOAT")],
        [make_output("SIGMAS", "SIGMAS", t.outs(8, 0))],
        wv=["simple", 20, 0.75])

    t.node(9, "RandomNoise", [750, 390], [225, 82],
        [widget_input("noise_seed", "INT"), widget_input("control_after_generate", "COMBO")],
        [make_output("NOISE", "NOISE", t.outs(9, 0))],
        wv=[0, "randomize"])

    t.node(10, "SamplerCustomAdvanced", [1050, 0], [280, 160],
        [conn_input("noise", "NOISE", l8), conn_input("guider", "GUIDER", l5),
         conn_input("sampler", "SAMPLER", l6), conn_input("sigmas", "SIGMAS", l7),
         conn_input("latent_image", "LATENT", l9)],
        [make_output("output", "LATENT", t.outs(10, 0)),
         null_output("denoised_output", "LATENT", 1)])

    t.node(11, "VAEDecode", [1400, 0], [265, 72],
        [conn_input("samples", "LATENT", l10), conn_input("vae", "VAE", l11)],
        [make_output("IMAGE", "IMAGE", t.outs(11, 0))])

    t.node(12, "SaveImage", [1400, 120], [320, 270],
        [conn_input("images", "IMAGE", l12), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_FLUX_I2I"])

    return t.build()


# ============================================================
# FLUX + LoRA
# ============================================================

def build_flux_lora():
    t = TB()
    l1 = t.L(2, 0, 4, 0, "CLIP")
    l2 = t.L(4, 0, 6, 1, "CONDITIONING")
    # LoRA modifies model
    l3 = t.L(1, 0, 14, 0, "MODEL")     # UNET -> LoRA
    l4 = t.L(14, 0, 6, 0, "MODEL")     # LoRA model -> guider
    l5 = t.L(14, 0, 8, 0, "MODEL")     # LoRA model -> scheduler
    l6 = t.L(6, 0, 10, 1, "GUIDER")
    l7 = t.L(7, 0, 10, 2, "SAMPLER")
    l8 = t.L(8, 0, 10, 3, "SIGMAS")
    l9 = t.L(9, 0, 10, 0, "NOISE")
    l10 = t.L(5, 0, 10, 4, "LATENT")
    l11 = t.L(10, 0, 11, 0, "LATENT")
    l12 = t.L(3, 0, 11, 1, "VAE")
    l13 = t.L(11, 0, 12, 0, "IMAGE")
    # LoRA also takes CLIP
    l14 = t.L(2, 0, 14, 1, "CLIP")
    # LoRA outputs modified CLIP for encoding
    l15 = t.L(14, 1, 4, 0, "CLIP")  # This would conflict with l1... let me redesign

    # Actually, for FLUX LoRA, LoraLoader takes MODEL and CLIP, outputs MODEL and CLIP
    # But FLUX uses UNETLoader for MODEL and DualCLIPLoader for CLIP
    # LoraLoader: model (MODEL), clip (CLIP), lora_name, strength_model, strength_clip -> MODEL, CLIP
    # So: UNETLoader -> LoraLoader -> model; DualCLIPLoader -> LoraLoader -> clip -> CLIPTextEncodeFlux

    # Let me rebuild this properly
    t = TB()
    l_unet_to_lora = t.L(1, 0, 13, 0, "MODEL")
    l_clip_to_lora = t.L(2, 0, 13, 1, "CLIP")
    l_lora_model_to_guider = t.L(13, 0, 6, 0, "MODEL")
    l_lora_model_to_sched = t.L(13, 0, 8, 0, "MODEL")
    l_lora_clip_to_encode = t.L(13, 1, 4, 0, "CLIP")
    l_encode_to_guider = t.L(4, 0, 6, 1, "CONDITIONING")
    l_guider = t.L(6, 0, 10, 1, "GUIDER")
    l_sampler = t.L(7, 0, 10, 2, "SAMPLER")
    l_sigmas = t.L(8, 0, 10, 3, "SIGMAS")
    l_noise = t.L(9, 0, 10, 0, "NOISE")
    l_latent = t.L(5, 0, 10, 4, "LATENT")
    l_sca_to_dec = t.L(10, 0, 11, 0, "LATENT")
    l_vae_to_dec = t.L(3, 0, 11, 1, "VAE")
    l_dec_to_save = t.L(11, 0, 12, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load FLUX Model", wv=["flux1-dev.safetensors", "default"])

    t.node(2, "DualCLIPLoader", [0, 130], [315, 120],
        [widget_input("clip_name1", "COMBO"), widget_input("clip_name2", "COMBO"), widget_input("type", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load CLIP (FLUX)", wv=["clip_l.safetensors", "t5xxl_fp16.safetensors", "flux"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["ae.safetensors"])

    t.node(13, "LoraLoader", [0, 430], [315, 126],
        [conn_input("model", "MODEL", l_unet_to_lora),
         conn_input("clip", "CLIP", l_clip_to_lora),
         widget_input("lora_name", "COMBO"),
         widget_input("strength_model", "FLOAT"),
         widget_input("strength_clip", "FLOAT")],
        [make_output("MODEL", "MODEL", t.outs(13, 0)),
         make_output("CLIP", "CLIP", t.outs(13, 1), 1)],
        title="Load LoRA", wv=["example_flux_lora.safetensors", 1.0, 1.0])

    t.node(4, "CLIPTextEncodeFlux", [400, 0], [300, 180],
        [conn_input("clip", "CLIP", l_lora_clip_to_encode),
         widget_input("clip_l", "STRING"), widget_input("t5xxl", "STRING"),
         widget_input("guidance", "FLOAT")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="FLUX Text Encode",
        wv=["a beautiful scene", "a beautiful woman standing in a lush garden, photorealistic, detailed", 3.5],
        color="#232", bgcolor="#353")

    t.node(5, "EmptyLatentImage", [400, 240], [225, 106],
        [widget_input("width", "INT"), widget_input("height", "INT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(5, 0))],
        wv=[1024, 1024, 1])

    t.node(6, "BasicGuider", [750, 0], [225, 72],
        [conn_input("model", "MODEL", l_lora_model_to_guider),
         conn_input("conditioning", "CONDITIONING", l_encode_to_guider)],
        [make_output("GUIDER", "GUIDER", t.outs(6, 0))])

    t.node(7, "KSamplerSelect", [750, 120], [225, 58],
        [widget_input("sampler_name", "COMBO")],
        [make_output("SAMPLER", "SAMPLER", t.outs(7, 0))],
        wv=["euler"])

    t.node(8, "BasicScheduler", [750, 230], [225, 106],
        [conn_input("model", "MODEL", l_lora_model_to_sched),
         widget_input("scheduler", "COMBO"), widget_input("steps", "INT"),
         widget_input("denoise", "FLOAT")],
        [make_output("SIGMAS", "SIGMAS", t.outs(8, 0))],
        wv=["simple", 20, 1])

    t.node(9, "RandomNoise", [750, 390], [225, 82],
        [widget_input("noise_seed", "INT"), widget_input("control_after_generate", "COMBO")],
        [make_output("NOISE", "NOISE", t.outs(9, 0))],
        wv=[0, "randomize"])

    t.node(10, "SamplerCustomAdvanced", [1050, 0], [280, 160],
        [conn_input("noise", "NOISE", l_noise), conn_input("guider", "GUIDER", l_guider),
         conn_input("sampler", "SAMPLER", l_sampler), conn_input("sigmas", "SIGMAS", l_sigmas),
         conn_input("latent_image", "LATENT", l_latent)],
        [make_output("output", "LATENT", t.outs(10, 0)),
         null_output("denoised_output", "LATENT", 1)])

    t.node(11, "VAEDecode", [1400, 0], [265, 72],
        [conn_input("samples", "LATENT", l_sca_to_dec), conn_input("vae", "VAE", l_vae_to_dec)],
        [make_output("IMAGE", "IMAGE", t.outs(11, 0))])

    t.node(12, "SaveImage", [1400, 120], [320, 270],
        [conn_input("images", "IMAGE", l_dec_to_save), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_FLUX_LoRA"])

    return t.build()


# ============================================================
# LTXV Text-to-Video
# ============================================================

def build_ltxv_txt2vid():
    t = TB()
    l1 = t.L(2, 0, 4, 0, "CLIP")
    l2 = t.L(2, 0, 5, 0, "CLIP")
    l3 = t.L(4, 0, 6, 0, "CONDITIONING")  # pos -> LTXVConditioning
    l4 = t.L(5, 0, 6, 1, "CONDITIONING")  # neg -> LTXVConditioning
    l5 = t.L(6, 0, 8, 1, "CONDITIONING")  # LTXVCond pos -> KSampler
    l6 = t.L(6, 1, 8, 2, "CONDITIONING")  # LTXVCond neg -> KSampler
    l7 = t.L(1, 0, 8, 0, "MODEL")
    l8 = t.L(7, 0, 8, 3, "LATENT")
    l9 = t.L(8, 0, 9, 0, "LATENT")
    l10 = t.L(3, 0, 9, 1, "VAE")
    l11 = t.L(9, 0, 10, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load LTXV Model", wv=["ltxv_2b_0.9.7_dev_fp8.safetensors", "default"])

    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load CLIP (LTXV)", wv=["t5xxl_fp16.safetensors", "ltxv", "default"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["ltxv_vae.safetensors"])

    t.node(4, "CLIPTextEncode", [400, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Positive Prompt",
        wv=["a beautiful sunset over the ocean, waves crashing on rocks, cinematic, smooth motion"],
        color="#232", bgcolor="#353")

    t.node(5, "CLIPTextEncode", [400, 170], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static, jittery, watermark"],
        color="#322", bgcolor="#533")

    t.node(6, "LTXVConditioning", [400, 340], [280, 80],
        [conn_input("positive", "CONDITIONING", l3), conn_input("negative", "CONDITIONING", l4),
         widget_input("frame_rate", "FLOAT")],
        [make_output("positive", "CONDITIONING", t.outs(6, 0)),
         make_output("negative", "CONDITIONING", t.outs(6, 1), 1)],
        title="LTXV Conditioning", wv=[25.0])

    t.node(7, "EmptyLTXVLatentVideo", [400, 470], [225, 130],
        [widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(7, 0))],
        title="Empty LTXV Latent", wv=[768, 512, 97, 1])

    t.node(8, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l7), conn_input("positive", "CONDITIONING", l5),
         conn_input("negative", "CONDITIONING", l6), conn_input("latent_image", "LATENT", l8),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(8, 0))],
        wv=[0, "randomize", 20, 3.0, "euler", "normal", 1])

    t.node(9, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l9), conn_input("vae", "VAE", l10)],
        [make_output("IMAGE", "IMAGE", t.outs(9, 0))])

    t.node(10, "SaveAnimatedWEBP", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l11), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_LTXV", 25, False, 85, "default"])

    return t.build()


# ============================================================
# LTXV Image-to-Video
# ============================================================

def build_ltxv_img2vid():
    t = TB()
    l1 = t.L(2, 0, 5, 0, "CLIP")
    l2 = t.L(2, 0, 6, 0, "CLIP")
    l3 = t.L(5, 0, 7, 0, "CONDITIONING")
    l4 = t.L(6, 0, 7, 1, "CONDITIONING")
    l5 = t.L(3, 0, 7, 2, "VAE")
    l6 = t.L(4, 0, 7, 3, "IMAGE")        # start image
    l7 = t.L(7, 0, 8, 1, "CONDITIONING")  # LTXVImgToVideo pos -> KSampler
    l8 = t.L(7, 1, 8, 2, "CONDITIONING")
    l9 = t.L(7, 2, 8, 3, "LATENT")
    l10 = t.L(1, 0, 8, 0, "MODEL")
    l11 = t.L(8, 0, 9, 0, "LATENT")
    l12 = t.L(3, 0, 9, 1, "VAE")
    l13 = t.L(9, 0, 10, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load LTXV Model", wv=["ltxv_2b_0.9.7_dev_fp8.safetensors", "default"])

    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load CLIP (LTXV)", wv=["t5xxl_fp16.safetensors", "ltxv", "default"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["ltxv_vae.safetensors"])

    t.node(4, "LoadImage", [0, 430], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(4, 0)), null_output("MASK", "MASK", 1)],
        title="Load Start Image", wv=["start_frame.png"])

    t.node(5, "CLIPTextEncode", [380, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Positive Prompt",
        wv=["the scene comes alive with gentle motion, camera pans right, high quality, smooth"],
        color="#232", bgcolor="#353")

    t.node(6, "CLIPTextEncode", [380, 170], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(6, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static, jittery"],
        color="#322", bgcolor="#533")

    t.node(7, "LTXVImgToVideo", [380, 340], [280, 220],
        [conn_input("positive", "CONDITIONING", l3), conn_input("negative", "CONDITIONING", l4),
         conn_input("vae", "VAE", l5), conn_input("image", "IMAGE", l6),
         widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT"),
         widget_input("strength", "FLOAT")],
        [make_output("positive", "CONDITIONING", t.outs(7, 0)),
         make_output("negative", "CONDITIONING", t.outs(7, 1), 1),
         make_output("latent", "LATENT", t.outs(7, 2), 2)],
        title="LTXV Image to Video", wv=[768, 512, 97, 1, 1.0])

    t.node(8, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l10), conn_input("positive", "CONDITIONING", l7),
         conn_input("negative", "CONDITIONING", l8), conn_input("latent_image", "LATENT", l9),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(8, 0))],
        wv=[0, "randomize", 20, 3.0, "euler", "normal", 1])

    t.node(9, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l11), conn_input("vae", "VAE", l12)],
        [make_output("IMAGE", "IMAGE", t.outs(9, 0))])

    t.node(10, "SaveAnimatedWEBP", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l13), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_LTXV_I2V", 25, False, 85, "default"])

    return t.build()


# ============================================================
# Mochi Text-to-Video
# ============================================================

def build_mochi_txt2vid():
    t = TB()
    l1 = t.L(2, 0, 4, 0, "CLIP")
    l2 = t.L(2, 0, 5, 0, "CLIP")
    l3 = t.L(4, 0, 7, 1, "CONDITIONING")
    l4 = t.L(5, 0, 7, 2, "CONDITIONING")
    l5 = t.L(1, 0, 7, 0, "MODEL")
    l6 = t.L(6, 0, 7, 3, "LATENT")
    l7 = t.L(7, 0, 8, 0, "LATENT")
    l8 = t.L(3, 0, 8, 1, "VAE")
    l9 = t.L(8, 0, 9, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load Mochi Model", wv=["mochi_preview_bf16.safetensors", "default"])

    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load CLIP (Mochi)", wv=["t5xxl_fp16.safetensors", "mochi", "default"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["mochi_vae.safetensors"])

    t.node(4, "CLIPTextEncode", [400, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Positive Prompt",
        wv=["a beautiful sunset over the ocean with waves crashing, cinematic, smooth camera motion"],
        color="#232", bgcolor="#353")

    t.node(5, "CLIPTextEncode", [400, 170], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static, jittery"],
        color="#322", bgcolor="#533")

    t.node(6, "EmptyMochiLatentVideo", [400, 340], [225, 130],
        [widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        title="Empty Mochi Latent", wv=[848, 480, 25, 1])

    t.node(7, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l5), conn_input("positive", "CONDITIONING", l3),
         conn_input("negative", "CONDITIONING", l4), conn_input("latent_image", "LATENT", l6),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(7, 0))],
        wv=[0, "randomize", 30, 4.5, "euler", "normal", 1])

    t.node(8, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l7), conn_input("vae", "VAE", l8)],
        [make_output("IMAGE", "IMAGE", t.outs(8, 0))])

    t.node(9, "SaveAnimatedWEBP", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l9), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_Mochi", 24, False, 85, "default"])

    return t.build()


# ============================================================
# Cosmos Image-to-Video
# ============================================================

def build_cosmos_img2vid():
    t = TB()
    l1 = t.L(2, 0, 5, 0, "CLIP")
    l2 = t.L(2, 0, 6, 0, "CLIP")
    l3 = t.L(5, 0, 8, 1, "CONDITIONING")
    l4 = t.L(6, 0, 8, 2, "CONDITIONING")
    l5 = t.L(3, 0, 7, 0, "VAE")          # VAE -> CosmosI2V
    l6 = t.L(4, 0, 7, 5, "IMAGE")        # image -> start_image (slot 5 in optional)
    l7 = t.L(7, 0, 8, 3, "LATENT")       # CosmosI2V -> KSampler latent
    l8 = t.L(1, 0, 8, 0, "MODEL")
    l9 = t.L(8, 0, 9, 0, "LATENT")
    l10 = t.L(3, 0, 9, 1, "VAE")
    l11 = t.L(9, 0, 10, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load Cosmos Model", wv=["cosmos_cv8x8x8_1.0_text2world_7b.safetensors", "default"])

    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load CLIP (Cosmos)", wv=["t5xxl_fp16.safetensors", "cosmos", "default"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["cosmos_cv8x8x8_1.0_decoder.safetensors"])

    t.node(4, "LoadImage", [0, 430], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(4, 0)), null_output("MASK", "MASK", 1)],
        title="Load Start Image", wv=["start_frame.png"])

    t.node(5, "CLIPTextEncode", [380, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Positive Prompt",
        wv=["the scene comes alive, camera slowly moves forward, cinematic, smooth motion"],
        color="#232", bgcolor="#353")

    t.node(6, "CLIPTextEncode", [380, 170], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(6, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static, jittery"],
        color="#322", bgcolor="#533")

    t.node(7, "CosmosImageToVideoLatent", [380, 340], [280, 220],
        [conn_input("vae", "VAE", l5),
         widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT"),
         opt_conn_input("start_image", "IMAGE", l6)],
        [make_output("LATENT", "LATENT", t.outs(7, 0))],
        title="Cosmos Image to Video Latent", wv=[1280, 704, 121, 1])

    t.node(8, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l8), conn_input("positive", "CONDITIONING", l3),
         conn_input("negative", "CONDITIONING", l4), conn_input("latent_image", "LATENT", l7),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(8, 0))],
        wv=[0, "randomize", 35, 7, "euler", "normal", 1])

    t.node(9, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l9), conn_input("vae", "VAE", l10)],
        [make_output("IMAGE", "IMAGE", t.outs(9, 0))])

    t.node(10, "SaveAnimatedWEBP", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l11), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_Cosmos", 24, False, 85, "default"])

    return t.build()


# ============================================================
# HunyuanVideo Image-to-Video
# ============================================================

def build_hunyuan_video_i2v():
    t = TB()
    # Uses HunyuanImageToVideo node
    l1 = t.L(2, 0, 5, 0, "CLIP")     # CLIP -> pos encode
    l2 = t.L(5, 0, 7, 0, "CONDITIONING")  # pos -> HunyuanI2V
    l3 = t.L(3, 0, 7, 1, "VAE")
    l4 = t.L(4, 0, 7, 7, "IMAGE")    # start image -> HunyuanI2V
    l5 = t.L(7, 0, 8, 1, "CONDITIONING")  # HunyuanI2V pos -> KSampler
    l6 = t.L(7, 1, 8, 3, "LATENT")   # HunyuanI2V latent -> KSampler
    l7 = t.L(1, 0, 8, 0, "MODEL")
    l8 = t.L(6, 0, 8, 2, "CONDITIONING")  # empty neg cond
    l9 = t.L(8, 0, 9, 0, "LATENT")
    l10 = t.L(3, 0, 9, 1, "VAE")
    l11 = t.L(9, 0, 10, 0, "IMAGE")
    l12 = t.L(2, 0, 6, 0, "CLIP")    # CLIP -> neg encode

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load HunyuanVideo Model",
        wv=["hunyuan_video_t2v_720p_bf16.safetensors", "default"])

    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load CLIP (HunyuanVideo)",
        wv=["llava_llama3_fp16.safetensors", "hunyuan_video", "default"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["hunyuan_video_vae_bf16.safetensors"])

    t.node(4, "LoadImage", [0, 430], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(4, 0)), null_output("MASK", "MASK", 1)],
        title="Load Start Image", wv=["start_frame.png"])

    t.node(5, "CLIPTextEncode", [400, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Positive Prompt",
        wv=["the scene comes alive with gentle motion, cinematic, smooth camera movement, high quality"],
        color="#232", bgcolor="#353")

    t.node(6, "CLIPTextEncode", [400, 170], [280, 120],
        [conn_input("clip", "CLIP", l12), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(6, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static"],
        color="#322", bgcolor="#533")

    t.node(7, "HunyuanImageToVideo", [400, 340], [280, 250],
        [conn_input("positive", "CONDITIONING", l2), conn_input("vae", "VAE", l3),
         widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT"),
         widget_input("guidance_type", "COMBO"),
         opt_conn_input("start_image", "IMAGE", l4)],
        [make_output("positive", "CONDITIONING", t.outs(7, 0)),
         make_output("latent", "LATENT", t.outs(7, 1), 1)],
        title="Hunyuan Image to Video", wv=[848, 480, 53, 1, "v1"])

    t.node(8, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l7), conn_input("positive", "CONDITIONING", l5),
         conn_input("negative", "CONDITIONING", l8), conn_input("latent_image", "LATENT", l6),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(8, 0))],
        wv=[0, "randomize", 30, 6, "euler", "normal", 1])

    t.node(9, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l9), conn_input("vae", "VAE", l10)],
        [make_output("IMAGE", "IMAGE", t.outs(9, 0))])

    t.node(10, "SaveAnimatedWEBP", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l11), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_HV_I2V", 24, False, 85, "default"])

    return t.build()


# ============================================================
# Stable Audio Generation
# ============================================================

def build_stable_audio():
    t = TB()
    l1 = t.L(1, 1, 3, 0, "CLIP")
    l2 = t.L(1, 1, 4, 0, "CLIP")
    l3 = t.L(3, 0, 5, 0, "CONDITIONING")
    l4 = t.L(4, 0, 5, 1, "CONDITIONING")
    l5 = t.L(5, 0, 7, 1, "CONDITIONING")  # CondStableAudio pos -> KSampler
    l6 = t.L(5, 1, 7, 2, "CONDITIONING")
    l7 = t.L(1, 0, 7, 0, "MODEL")
    l8 = t.L(6, 0, 7, 3, "LATENT")
    l9 = t.L(7, 0, 8, 0, "LATENT")
    l10 = t.L(1, 2, 8, 1, "VAE")
    l11 = t.L(8, 0, 9, 0, "AUDIO")

    t.node(1, "CheckpointLoaderSimple", [0, 0], [315, 98],
        [widget_input("ckpt_name", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0)),
         make_output("CLIP", "CLIP", t.outs(1, 1), 1),
         make_output("VAE", "VAE", t.outs(1, 2), 2)],
        title="Load Stable Audio Model", wv=["stable_audio_open_1.0.safetensors"])

    t.node(3, "CLIPTextEncode", [400, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(3, 0))],
        title="Positive Prompt",
        wv=["ambient electronic music, soft pads, gentle melody, relaxing atmosphere"],
        color="#232", bgcolor="#353")

    t.node(4, "CLIPTextEncode", [400, 170], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Negative Prompt",
        wv=["noise, distortion, low quality"],
        color="#322", bgcolor="#533")

    t.node(5, "ConditioningStableAudio", [400, 340], [280, 100],
        [conn_input("positive", "CONDITIONING", l3), conn_input("negative", "CONDITIONING", l4),
         widget_input("seconds_start", "FLOAT"), widget_input("seconds_total", "FLOAT")],
        [make_output("positive", "CONDITIONING", t.outs(5, 0)),
         make_output("negative", "CONDITIONING", t.outs(5, 1), 1)],
        title="Stable Audio Conditioning", wv=[0.0, 47.0])

    t.node(6, "EmptyLatentAudio", [400, 490], [225, 82],
        [widget_input("seconds", "FLOAT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        title="Empty Audio Latent", wv=[47.6, 1])

    t.node(7, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l7), conn_input("positive", "CONDITIONING", l5),
         conn_input("negative", "CONDITIONING", l6), conn_input("latent_image", "LATENT", l8),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(7, 0))],
        wv=[0, "randomize", 100, 7, "dpmpp_2m", "sgm_uniform", 1])

    t.node(8, "VAEDecodeAudio", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l9), conn_input("vae", "VAE", l10)],
        [make_output("AUDIO", "AUDIO", t.outs(8, 0))])

    t.node(9, "SaveAudio", [1100, 120], [320, 150],
        [conn_input("audio", "AUDIO", l11), widget_input("filename_prefix", "STRING")],
        [], title="Save Audio", wv=["audio/ComfyUI_StableAudio"])

    return t.build()


# ============================================================
# Hunyuan3D v2
# ============================================================

def build_hunyuan3d_v2():
    t = TB()
    l1 = t.L(2, 0, 4, 0, "CLIP_VISION")  # CLIPVision -> encode
    l2 = t.L(3, 0, 4, 1, "IMAGE")         # image -> encode
    l3 = t.L(4, 0, 5, 0, "CLIP_VISION_OUTPUT")  # encode -> conditioning
    l4 = t.L(5, 0, 7, 1, "CONDITIONING")  # pos -> KSampler
    l5 = t.L(5, 1, 7, 2, "CONDITIONING")  # neg -> KSampler
    l6 = t.L(1, 0, 7, 0, "MODEL")
    l7 = t.L(6, 0, 7, 3, "LATENT")
    l8 = t.L(7, 0, 8, 0, "LATENT")
    l9 = t.L(9, 0, 8, 1, "VAE")
    l10 = t.L(8, 0, 10, 0, "VOXEL")
    l11 = t.L(10, 0, 11, 0, "MESH")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load Hunyuan3D Model", wv=["hunyuan3d_v2_turbo.safetensors", "default"])

    t.node(2, "CLIPVisionLoader", [0, 130], [290, 82],
        [widget_input("clip_name", "COMBO")],
        [make_output("CLIP_VISION", "CLIP_VISION", t.outs(2, 0))],
        title="Load CLIP Vision", wv=["clip_vision_h.safetensors"])

    t.node(3, "LoadImage", [0, 260], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(3, 0)), null_output("MASK", "MASK", 1)],
        title="Load Input Image", wv=["input.png"])

    t.node(4, "CLIPVisionEncode", [380, 130], [250, 100],
        [conn_input("clip_vision", "CLIP_VISION", l1), conn_input("image", "IMAGE", l2),
         widget_input("crop", "COMBO")],
        [make_output("CLIP_VISION_OUTPUT", "CLIP_VISION_OUTPUT", t.outs(4, 0))],
        title="Encode Vision", wv=["center"])

    t.node(5, "Hunyuan3Dv2Conditioning", [380, 280], [280, 80],
        [conn_input("clip_vision_output", "CLIP_VISION_OUTPUT", l3)],
        [make_output("positive", "CONDITIONING", t.outs(5, 0)),
         make_output("negative", "CONDITIONING", t.outs(5, 1), 1)],
        title="Hunyuan3D Conditioning")

    t.node(6, "EmptyLatentHunyuan3Dv2", [380, 410], [225, 82],
        [widget_input("resolution", "INT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        title="Empty 3D Latent", wv=[3072, 1])

    t.node(7, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l6), conn_input("positive", "CONDITIONING", l4),
         conn_input("negative", "CONDITIONING", l5), conn_input("latent_image", "LATENT", l7),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(7, 0))],
        wv=[0, "randomize", 30, 7, "euler", "normal", 1])

    t.node(9, "VAELoader", [750, 390], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(9, 0))],
        title="Load 3D VAE", wv=["hunyuan3d_v2_vae.safetensors"])

    t.node(8, "VAEDecodeHunyuan3D", [1100, 0], [300, 106],
        [conn_input("samples", "LATENT", l8), conn_input("vae", "VAE", l9),
         widget_input("num_chunks", "INT"), widget_input("octree_resolution", "INT")],
        [make_output("VOXEL", "VOXEL", t.outs(8, 0))],
        title="Decode to Voxel", wv=[8000, 256])

    t.node(10, "VoxelToMeshBasic", [1100, 160], [265, 82],
        [conn_input("voxel", "VOXEL", l10), widget_input("threshold", "FLOAT")],
        [make_output("MESH", "MESH", t.outs(10, 0))],
        title="Voxel to Mesh", wv=[0.6])

    t.node(11, "SaveGLB", [1100, 300], [320, 150],
        [conn_input("mesh", "MESH", l11), widget_input("filename_prefix", "STRING")],
        [], title="Save 3D Model", wv=["mesh/ComfyUI_3D"])

    return t.build()


# ============================================================
# Stable Cascade
# ============================================================

def build_stable_cascade():
    t = TB()
    # Stage C
    l1 = t.L(1, 1, 3, 0, "CLIP")
    l2 = t.L(1, 1, 4, 0, "CLIP")
    l3 = t.L(3, 0, 6, 1, "CONDITIONING")
    l4 = t.L(4, 0, 6, 2, "CONDITIONING")
    l5 = t.L(1, 0, 6, 0, "MODEL")
    l6 = t.L(5, 0, 6, 3, "LATENT")     # stage_c latent -> KSampler
    # Stage B
    l7 = t.L(6, 0, 8, 0, "LATENT")     # stage_c output -> StageB conditioning
    l8 = t.L(3, 0, 8, 1, "CONDITIONING")  # reuse pos conditioning (stage_c encoded)
    # Wait, StableCascade_StageB_Conditioning takes: conditioning + stage_c
    # Actually it takes the KSampler output as stage_c
    # Let me reconsider...

    # StableCascade_StageB_Conditioning(conditioning, stage_c) -> CONDITIONING
    # conditioning = the text conditioning (from CLIPTextEncode)
    # stage_c = the output of KSampler (Stage C denoised latent)

    # So: stage_c KSampler output -> StageB_Conditioning
    #     pos conditioning -> StageB_Conditioning
    # Then: StageB_Conditioning output -> Stage B KSampler

    # StableCascade_EmptyLatentImage -> stage_c LATENT, stage_b LATENT

    t = TB()  # reset

    # Stage C loaders + encode
    l_clip_pos = t.L(1, 1, 3, 0, "CLIP")
    l_clip_neg = t.L(1, 1, 4, 0, "CLIP")
    # EmptyLatent -> stage_c, stage_b
    # Stage C sampling
    l_pos_to_ksc = t.L(3, 0, 6, 1, "CONDITIONING")
    l_neg_to_ksc = t.L(4, 0, 6, 2, "CONDITIONING")
    l_model_c = t.L(1, 0, 6, 0, "MODEL")
    l_latent_c = t.L(5, 0, 6, 3, "LATENT")  # stage_c latent

    # Stage B conditioning
    l_ksc_to_stageb_cond = t.L(6, 0, 8, 1, "LATENT")  # KSampler output -> StageB conditioning stage_c input
    # Wait, StableCascade_StageB_Conditioning inputs: conditioning (CONDITIONING), stage_c (LATENT)
    # So slot 0 = conditioning, slot 1 = stage_c (LATENT)
    l_pos_to_stageb = t.L(3, 0, 8, 0, "CONDITIONING")

    # Stage B sampling
    l_stageb_cond = t.L(8, 0, 9, 1, "CONDITIONING")  # StageB cond -> KSampler pos
    l_neg_to_ksb = t.L(4, 0, 9, 2, "CONDITIONING")    # neg -> KSampler
    l_model_b = t.L(2, 0, 9, 0, "MODEL")
    l_latent_b = t.L(5, 1, 9, 3, "LATENT")  # stage_b latent from EmptyLatent slot 1

    # Decode
    l_ksb_to_dec = t.L(9, 0, 10, 0, "LATENT")
    l_vae_to_dec = t.L(2, 2, 10, 1, "VAE")
    l_dec_to_save = t.L(10, 0, 11, 0, "IMAGE")

    t.node(1, "CheckpointLoaderSimple", [0, 0], [315, 98],
        [widget_input("ckpt_name", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0)),
         make_output("CLIP", "CLIP", t.outs(1, 1), 1),
         make_output("VAE", "VAE", [], 2)],
        title="Load Stage C Model", wv=["stable_cascade_stage_c.safetensors"])

    t.node(2, "CheckpointLoaderSimple", [0, 150], [315, 98],
        [widget_input("ckpt_name", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(2, 0)),
         make_output("CLIP", "CLIP", [], 1),
         make_output("VAE", "VAE", t.outs(2, 2), 2)],
        title="Load Stage B Model", wv=["stable_cascade_stage_b.safetensors"])

    t.node(3, "CLIPTextEncode", [400, 0], [280, 120],
        [conn_input("clip", "CLIP", l_clip_pos), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(3, 0))],
        title="Positive Prompt",
        wv=["masterpiece, best quality, a beautiful landscape with mountains"],
        color="#232", bgcolor="#353")

    t.node(4, "CLIPTextEncode", [400, 170], [280, 120],
        [conn_input("clip", "CLIP", l_clip_neg), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Negative Prompt",
        wv=["worst quality, low quality, blurry, deformed"],
        color="#322", bgcolor="#533")

    t.node(5, "StableCascade_EmptyLatentImage", [400, 340], [225, 130],
        [widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("compression", "INT"), widget_input("batch_size", "INT")],
        [make_output("stage_c", "LATENT", t.outs(5, 0)),
         make_output("stage_b", "LATENT", t.outs(5, 1), 1)],
        title="Cascade Empty Latent", wv=[1024, 1024, 42, 1])

    t.node(6, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l_model_c), conn_input("positive", "CONDITIONING", l_pos_to_ksc),
         conn_input("negative", "CONDITIONING", l_neg_to_ksc), conn_input("latent_image", "LATENT", l_latent_c),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        title="Stage C Sampler", wv=[0, "randomize", 20, 4.0, "euler", "sgm_uniform", 1])

    t.node(8, "StableCascade_StageB_Conditioning", [1100, 0], [300, 80],
        [conn_input("conditioning", "CONDITIONING", l_pos_to_stageb),
         conn_input("stage_c", "LATENT", l_ksc_to_stageb_cond)],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(8, 0))],
        title="Stage B Conditioning")

    t.node(9, "KSampler", [1100, 130], [300, 340],
        [conn_input("model", "MODEL", l_model_b), conn_input("positive", "CONDITIONING", l_stageb_cond),
         conn_input("negative", "CONDITIONING", l_neg_to_ksb), conn_input("latent_image", "LATENT", l_latent_b),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(9, 0))],
        title="Stage B Sampler", wv=[0, "randomize", 10, 1.1, "euler", "sgm_uniform", 1])

    t.node(10, "VAEDecode", [1450, 0], [265, 72],
        [conn_input("samples", "LATENT", l_ksb_to_dec), conn_input("vae", "VAE", l_vae_to_dec)],
        [make_output("IMAGE", "IMAGE", t.outs(10, 0))])

    t.node(11, "SaveImage", [1450, 120], [320, 270],
        [conn_input("images", "IMAGE", l_dec_to_save), widget_input("filename_prefix", "STRING")],
        [], title="Save Image", wv=["ComfyUI_Cascade"])

    return t.build()


# ============================================================
# Cosmos Text-to-Video
# ============================================================

def build_cosmos_txt2vid():
    t = TB()
    l1 = t.L(2, 0, 4, 0, "CLIP")
    l2 = t.L(2, 0, 5, 0, "CLIP")
    l3 = t.L(4, 0, 7, 1, "CONDITIONING")
    l4 = t.L(5, 0, 7, 2, "CONDITIONING")
    l5 = t.L(1, 0, 7, 0, "MODEL")
    l6 = t.L(6, 0, 7, 3, "LATENT")
    l7 = t.L(7, 0, 8, 0, "LATENT")
    l8 = t.L(3, 0, 8, 1, "VAE")
    l9 = t.L(8, 0, 9, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load Cosmos Model", wv=["cosmos_cv8x8x8_1.0_text2world_7b.safetensors", "default"])

    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Load CLIP (Cosmos)", wv=["t5xxl_fp16.safetensors", "cosmos", "default"])

    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Load VAE", wv=["cosmos_cv8x8x8_1.0_decoder.safetensors"])

    t.node(4, "CLIPTextEncode", [400, 0], [280, 120],
        [conn_input("clip", "CLIP", l1), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(4, 0))],
        title="Positive Prompt",
        wv=["a futuristic city at night with neon lights, flying cars, cinematic, smooth camera motion"],
        color="#232", bgcolor="#353")

    t.node(5, "CLIPTextEncode", [400, 170], [280, 120],
        [conn_input("clip", "CLIP", l2), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static, jittery"],
        color="#322", bgcolor="#533")

    t.node(6, "EmptyCosmosLatentVideo", [400, 340], [225, 130],
        [widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT")],
        [make_output("LATENT", "LATENT", t.outs(6, 0))],
        title="Empty Cosmos Latent", wv=[1280, 704, 121, 1])

    t.node(7, "KSampler", [750, 0], [300, 340],
        [conn_input("model", "MODEL", l5), conn_input("positive", "CONDITIONING", l3),
         conn_input("negative", "CONDITIONING", l4), conn_input("latent_image", "LATENT", l6),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(7, 0))],
        wv=[0, "randomize", 35, 7, "euler", "normal", 1])

    t.node(8, "VAEDecode", [1100, 0], [265, 72],
        [conn_input("samples", "LATENT", l7), conn_input("vae", "VAE", l8)],
        [make_output("IMAGE", "IMAGE", t.outs(8, 0))])

    t.node(9, "SaveAnimatedWEBP", [1100, 120], [320, 270],
        [conn_input("images", "IMAGE", l9), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_Cosmos_T2V", 24, False, 85, "default"])

    return t.build()


# ============================================================
# Wan 2.2 First-Last Frame to Video
# ============================================================

def build_wan22_first_last():
    """Wan 2.2 first+last frame to video interpolation."""
    t = TB()
    # Loaders
    l1 = t.L(2, 0, 5, 0, "CLIP"); l2 = t.L(2, 0, 6, 0, "CLIP")
    # Vision encoding for start + end
    l3 = t.L(4, 0, 8, 0, "CLIP_VISION"); l4 = t.L(3, 0, 8, 1, "IMAGE")  # start -> cv_enc_start
    l5 = t.L(4, 0, 9, 0, "CLIP_VISION"); l6 = t.L(10, 0, 9, 1, "IMAGE") # end -> cv_enc_end
    # Encode -> WanFirstLastFrame
    l7 = t.L(5, 0, 11, 0, "CONDITIONING"); l8 = t.L(6, 0, 11, 1, "CONDITIONING")
    l9 = t.L(1, 2, 11, 2, "VAE")
    l10 = t.L(8, 0, 11, 3, "CLIP_VISION_OUTPUT")  # start vision
    l11 = t.L(9, 0, 11, 4, "CLIP_VISION_OUTPUT")  # end vision
    l12 = t.L(3, 0, 11, 5, "IMAGE")  # start_image
    l13 = t.L(10, 0, 11, 6, "IMAGE") # end_image
    # Sampling
    l14 = t.L(1, 0, 12, 0, "MODEL"); l15 = t.L(11, 0, 12, 1, "CONDITIONING")
    l16 = t.L(11, 1, 12, 2, "CONDITIONING"); l17 = t.L(11, 2, 12, 3, "LATENT")
    l18 = t.L(12, 0, 13, 0, "LATENT"); l19 = t.L(1, 2, 13, 1, "VAE")
    l20 = t.L(13, 0, 14, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0)),
         None,  # placeholder
         make_output("VAE", "VAE", t.outs(1, 2), 2)],  # won't work - UNET only has MODEL
        title="Load Wan I2V Model", wv=["wan2.2_i2v_480p_14b.safetensors", "default"])

    # Actually UNETLoader only has 1 output: MODEL. I need separate VAELoader.
    # Let me redo this properly.
    t = TB()
    l_clip_pos = t.L(2, 0, 6, 0, "CLIP")
    l_clip_neg = t.L(2, 0, 7, 0, "CLIP")
    l_cv_start = t.L(4, 0, 8, 0, "CLIP_VISION")
    l_img_start_to_cv = t.L(5, 0, 8, 1, "IMAGE")
    l_cv_end = t.L(4, 0, 9, 0, "CLIP_VISION")
    l_img_end_to_cv = t.L(10, 0, 9, 1, "IMAGE")
    l_pos = t.L(6, 0, 11, 0, "CONDITIONING")
    l_neg = t.L(7, 0, 11, 1, "CONDITIONING")
    l_vae_wan = t.L(3, 0, 11, 2, "VAE")
    l_cvs = t.L(8, 0, 11, 3, "CLIP_VISION_OUTPUT")
    l_cve = t.L(9, 0, 11, 4, "CLIP_VISION_OUTPUT")
    l_starts = t.L(5, 0, 11, 5, "IMAGE")
    l_ends = t.L(10, 0, 11, 6, "IMAGE")
    l_model = t.L(1, 0, 12, 0, "MODEL")
    l_p = t.L(11, 0, 12, 1, "CONDITIONING")
    l_n = t.L(11, 1, 12, 2, "CONDITIONING")
    l_lat = t.L(11, 2, 12, 3, "LATENT")
    l_ks = t.L(12, 0, 13, 0, "LATENT")
    l_vd = t.L(3, 0, 13, 1, "VAE")
    l_save = t.L(13, 0, 14, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load Wan I2V Model", wv=["wan2.2_i2v_480p_14b.safetensors", "default"])
    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Wan CLIP", wv=["umt5_xxl_fp16.safetensors", "wan", "default"])
    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Wan VAE", wv=["wan_2.1_vae.safetensors"])
    t.node(4, "CLIPVisionLoader", [0, 430], [290, 82],
        [widget_input("clip_name", "COMBO")],
        [make_output("CLIP_VISION", "CLIP_VISION", t.outs(4, 0))],
        title="CLIP Vision", wv=["clip_vision_h.safetensors"])
    t.node(5, "LoadImage", [0, 560], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(5, 0)), null_output("MASK", "MASK", 1)],
        title="Start Frame", wv=["start_frame.png"])
    t.node(10, "LoadImage", [0, 920], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(10, 0)), null_output("MASK", "MASK", 1)],
        title="End Frame", wv=["end_frame.png"])
    t.node(6, "CLIPTextEncode", [380, 0], [280, 120],
        [conn_input("clip", "CLIP", l_clip_pos), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(6, 0))],
        title="Positive Prompt",
        wv=["smooth transition between two scenes, cinematic, high quality, fluid motion"],
        color="#232", bgcolor="#353")
    t.node(7, "CLIPTextEncode", [380, 170], [280, 120],
        [conn_input("clip", "CLIP", l_clip_neg), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(7, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static, jittery"],
        color="#322", bgcolor="#533")
    t.node(8, "CLIPVisionEncode", [380, 560], [250, 100],
        [conn_input("clip_vision", "CLIP_VISION", l_cv_start), conn_input("image", "IMAGE", l_img_start_to_cv),
         widget_input("crop", "COMBO")],
        [make_output("CLIP_VISION_OUTPUT", "CLIP_VISION_OUTPUT", t.outs(8, 0))],
        title="Encode Start Vision", wv=["center"])
    t.node(9, "CLIPVisionEncode", [380, 710], [250, 100],
        [conn_input("clip_vision", "CLIP_VISION", l_cv_end), conn_input("image", "IMAGE", l_img_end_to_cv),
         widget_input("crop", "COMBO")],
        [make_output("CLIP_VISION_OUTPUT", "CLIP_VISION_OUTPUT", t.outs(9, 0))],
        title="Encode End Vision", wv=["center"])
    t.node(11, "WanFirstLastFrameToVideo", [700, 0], [260, 300],
        [conn_input("positive", "CONDITIONING", l_pos), conn_input("negative", "CONDITIONING", l_neg),
         conn_input("vae", "VAE", l_vae_wan),
         opt_conn_input("clip_vision_start_image", "CLIP_VISION_OUTPUT", l_cvs),
         opt_conn_input("clip_vision_end_image", "CLIP_VISION_OUTPUT", l_cve),
         opt_conn_input("start_image", "IMAGE", l_starts),
         opt_conn_input("end_image", "IMAGE", l_ends),
         widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT")],
        [make_output("positive", "CONDITIONING", t.outs(11, 0)),
         make_output("negative", "CONDITIONING", t.outs(11, 1), 1),
         make_output("latent", "LATENT", t.outs(11, 2), 2)],
        title="Wan First-Last Frame to Video", wv=[832, 480, 81, 1])
    t.node(12, "KSampler", [1050, 0], [300, 340],
        [conn_input("model", "MODEL", l_model), conn_input("positive", "CONDITIONING", l_p),
         conn_input("negative", "CONDITIONING", l_n), conn_input("latent_image", "LATENT", l_lat),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(12, 0))],
        wv=[0, "randomize", 25, 6, "euler", "normal", 1])
    t.node(13, "VAEDecode", [1400, 0], [265, 72],
        [conn_input("samples", "LATENT", l_ks), conn_input("vae", "VAE", l_vd)],
        [make_output("IMAGE", "IMAGE", t.outs(13, 0))])
    t.node(14, "SaveAnimatedWEBP", [1400, 120], [320, 270],
        [conn_input("images", "IMAGE", l_save), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_Wan_FL", 16, False, 85, "default"])
    return t.build()


# ============================================================
# Wan 2.2 Fun Control to Video
# ============================================================

def build_wan22_fun_control():
    """Wan 2.2 Fun Control - uses control video + optional ref image."""
    t = TB()
    l_clip_pos = t.L(2, 0, 5, 0, "CLIP")
    l_clip_neg = t.L(2, 0, 6, 0, "CLIP")
    l_pos = t.L(5, 0, 8, 0, "CONDITIONING")
    l_neg = t.L(6, 0, 8, 1, "CONDITIONING")
    l_vae = t.L(3, 0, 8, 2, "VAE")
    l_ref = t.L(4, 0, 8, 3, "IMAGE")      # ref_image
    l_ctrl = t.L(7, 0, 8, 4, "IMAGE")     # control_video
    l_model = t.L(1, 0, 9, 0, "MODEL")
    l_p = t.L(8, 0, 9, 1, "CONDITIONING")
    l_n = t.L(8, 1, 9, 2, "CONDITIONING")
    l_lat = t.L(8, 2, 9, 3, "LATENT")
    l_ks = t.L(9, 0, 10, 0, "LATENT")
    l_vd = t.L(3, 0, 10, 1, "VAE")
    l_save = t.L(10, 0, 11, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load Wan Fun Control Model", wv=["wan2.2_fun_control.safetensors", "default"])
    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Wan CLIP", wv=["umt5_xxl_fp16.safetensors", "wan", "default"])
    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Wan VAE", wv=["wan_2.1_vae.safetensors"])
    t.node(4, "LoadImage", [0, 430], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(4, 0)), null_output("MASK", "MASK", 1)],
        title="Reference Image", wv=["ref_image.png"])
    t.node(7, "LoadImage", [0, 790], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(7, 0)), null_output("MASK", "MASK", 1)],
        title="Control Video Frames", wv=["control_video.png"])
    t.node(5, "CLIPTextEncode", [380, 0], [280, 120],
        [conn_input("clip", "CLIP", l_clip_pos), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(5, 0))],
        title="Positive Prompt",
        wv=["a person dancing gracefully, smooth motion, high quality, cinematic"],
        color="#232", bgcolor="#353")
    t.node(6, "CLIPTextEncode", [380, 170], [280, 120],
        [conn_input("clip", "CLIP", l_clip_neg), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(6, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static, jittery"],
        color="#322", bgcolor="#533")
    t.node(8, "Wan22FunControlToVideo", [700, 0], [260, 300],
        [conn_input("positive", "CONDITIONING", l_pos), conn_input("negative", "CONDITIONING", l_neg),
         conn_input("vae", "VAE", l_vae),
         opt_conn_input("ref_image", "IMAGE", l_ref),
         opt_conn_input("control_video", "IMAGE", l_ctrl),
         widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT")],
        [make_output("positive", "CONDITIONING", t.outs(8, 0)),
         make_output("negative", "CONDITIONING", t.outs(8, 1), 1),
         make_output("latent", "LATENT", t.outs(8, 2), 2)],
        title="Wan Fun Control to Video", wv=[832, 480, 81, 1])
    t.node(9, "KSampler", [1050, 0], [300, 340],
        [conn_input("model", "MODEL", l_model), conn_input("positive", "CONDITIONING", l_p),
         conn_input("negative", "CONDITIONING", l_n), conn_input("latent_image", "LATENT", l_lat),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(9, 0))],
        wv=[0, "randomize", 25, 6, "euler", "normal", 1])
    t.node(10, "VAEDecode", [1400, 0], [265, 72],
        [conn_input("samples", "LATENT", l_ks), conn_input("vae", "VAE", l_vd)],
        [make_output("IMAGE", "IMAGE", t.outs(10, 0))])
    t.node(11, "SaveAnimatedWEBP", [1400, 120], [320, 270],
        [conn_input("images", "IMAGE", l_save), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_Wan_FunCtrl", 16, False, 85, "default"])
    return t.build()


# ============================================================
# Wan 2.2 Camera Control
# ============================================================

def build_wan22_camera():
    """Wan 2.2 Camera - image-to-video with camera motion control."""
    t = TB()
    l_clip_pos = t.L(2, 0, 6, 0, "CLIP")
    l_clip_neg = t.L(2, 0, 7, 0, "CLIP")
    l_cv = t.L(4, 0, 8, 0, "CLIP_VISION")
    l_img_cv = t.L(5, 0, 8, 1, "IMAGE")
    l_pos = t.L(6, 0, 9, 0, "CONDITIONING")
    l_neg = t.L(7, 0, 9, 1, "CONDITIONING")
    l_vae = t.L(3, 0, 9, 2, "VAE")
    l_cvout = t.L(8, 0, 9, 3, "CLIP_VISION_OUTPUT")
    l_start = t.L(5, 0, 9, 4, "IMAGE")
    # camera_conditions is optional - user provides WanCameraEmbedding externally
    l_model = t.L(1, 0, 10, 0, "MODEL")
    l_p = t.L(9, 0, 10, 1, "CONDITIONING")
    l_n = t.L(9, 1, 10, 2, "CONDITIONING")
    l_lat = t.L(9, 2, 10, 3, "LATENT")
    l_ks = t.L(10, 0, 11, 0, "LATENT")
    l_vd = t.L(3, 0, 11, 1, "VAE")
    l_save = t.L(11, 0, 12, 0, "IMAGE")

    t.node(1, "UNETLoader", [0, 0], [350, 82],
        [widget_input("unet_name", "COMBO"), widget_input("weight_dtype", "COMBO")],
        [make_output("MODEL", "MODEL", t.outs(1, 0))],
        title="Load Wan Camera Model", wv=["wan2.2_i2v_480p_14b.safetensors", "default"])
    t.node(2, "CLIPLoader", [0, 130], [290, 120],
        [widget_input("clip_name", "COMBO"), widget_input("type", "COMBO"), widget_input("device", "COMBO")],
        [make_output("CLIP", "CLIP", t.outs(2, 0))],
        title="Wan CLIP", wv=["umt5_xxl_fp16.safetensors", "wan", "default"])
    t.node(3, "VAELoader", [0, 300], [290, 82],
        [widget_input("vae_name", "COMBO")],
        [make_output("VAE", "VAE", t.outs(3, 0))],
        title="Wan VAE", wv=["wan_2.1_vae.safetensors"])
    t.node(4, "CLIPVisionLoader", [0, 430], [290, 82],
        [widget_input("clip_name", "COMBO")],
        [make_output("CLIP_VISION", "CLIP_VISION", t.outs(4, 0))],
        title="CLIP Vision", wv=["clip_vision_h.safetensors"])
    t.node(5, "LoadImage", [0, 560], [280, 310],
        [widget_input("image", "COMBO"), widget_input("upload", "IMAGEUPLOAD")],
        [make_output("IMAGE", "IMAGE", t.outs(5, 0)), null_output("MASK", "MASK", 1)],
        title="Start Image", wv=["start_frame.png"])
    t.node(6, "CLIPTextEncode", [380, 0], [280, 120],
        [conn_input("clip", "CLIP", l_clip_pos), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(6, 0))],
        title="Positive Prompt",
        wv=["camera orbits around a beautiful castle, cinematic drone shot, smooth motion"],
        color="#232", bgcolor="#353")
    t.node(7, "CLIPTextEncode", [380, 170], [280, 120],
        [conn_input("clip", "CLIP", l_clip_neg), widget_input("text", "STRING")],
        [make_output("CONDITIONING", "CONDITIONING", t.outs(7, 0))],
        title="Negative Prompt",
        wv=["worst quality, blurry, distorted, static, jittery"],
        color="#322", bgcolor="#533")
    t.node(8, "CLIPVisionEncode", [380, 430], [250, 100],
        [conn_input("clip_vision", "CLIP_VISION", l_cv), conn_input("image", "IMAGE", l_img_cv),
         widget_input("crop", "COMBO")],
        [make_output("CLIP_VISION_OUTPUT", "CLIP_VISION_OUTPUT", t.outs(8, 0))],
        title="Encode Vision", wv=["center"])
    t.node(9, "WanCameraImageToVideo", [700, 0], [260, 300],
        [conn_input("positive", "CONDITIONING", l_pos), conn_input("negative", "CONDITIONING", l_neg),
         conn_input("vae", "VAE", l_vae),
         opt_conn_input("clip_vision_output", "CLIP_VISION_OUTPUT", l_cvout),
         opt_conn_input("start_image", "IMAGE", l_start),
         widget_input("width", "INT"), widget_input("height", "INT"),
         widget_input("length", "INT"), widget_input("batch_size", "INT")],
        [make_output("positive", "CONDITIONING", t.outs(9, 0)),
         make_output("negative", "CONDITIONING", t.outs(9, 1), 1),
         make_output("latent", "LATENT", t.outs(9, 2), 2)],
        title="Wan Camera I2V (connect camera_conditions)", wv=[832, 480, 81, 1])
    t.node(10, "KSampler", [1050, 0], [300, 340],
        [conn_input("model", "MODEL", l_model), conn_input("positive", "CONDITIONING", l_p),
         conn_input("negative", "CONDITIONING", l_n), conn_input("latent_image", "LATENT", l_lat),
         widget_input("seed", "INT"), widget_input("control_after_generate", "COMBO"),
         widget_input("steps", "INT"), widget_input("cfg", "FLOAT"),
         widget_input("sampler_name", "COMBO"), widget_input("scheduler", "COMBO"),
         widget_input("denoise", "FLOAT")],
        [make_output("LATENT", "LATENT", t.outs(10, 0))],
        wv=[0, "randomize", 25, 6, "euler", "normal", 1])
    t.node(11, "VAEDecode", [1400, 0], [265, 72],
        [conn_input("samples", "LATENT", l_ks), conn_input("vae", "VAE", l_vd)],
        [make_output("IMAGE", "IMAGE", t.outs(11, 0))])
    t.node(12, "SaveAnimatedWEBP", [1400, 120], [320, 270],
        [conn_input("images", "IMAGE", l_save), widget_input("filename_prefix", "STRING"),
         widget_input("fps", "FLOAT"), widget_input("lossless", "BOOLEAN"),
         widget_input("quality", "INT"), widget_input("method", "COMBO")],
        [], title="Save Video", wv=["ComfyUI_Wan_Camera", 16, False, 85, "default"])
    return t.build()


# ============================================================
# Main
# ============================================================

TEMPLATES = {
    "sd3-txt2img.json": build_sd3_txt2img,
    "sd15-img2img.json": build_sd15_img2img,
    "sd15-lora.json": build_sd15_lora,
    "sdxl-controlnet.json": build_sdxl_controlnet,
    "sdxl-inpaint.json": build_sdxl_inpaint,
    "sdxl-img2img.json": build_sdxl_img2img,
    "flux-img2img.json": build_flux_img2img,
    "flux-lora.json": build_flux_lora,
    "ltxv-txt2vid.json": build_ltxv_txt2vid,
    "ltxv-img2vid.json": build_ltxv_img2vid,
    "mochi-txt2vid.json": build_mochi_txt2vid,
    "cosmos-img2vid.json": build_cosmos_img2vid,
    "hunyuan-video-i2v.json": build_hunyuan_video_i2v,
    "stable-audio.json": build_stable_audio,
    "hunyuan3d-v2.json": build_hunyuan3d_v2,
    "stable-cascade.json": build_stable_cascade,
    "cosmos-txt2vid.json": build_cosmos_txt2vid,
    "wan22-first-last.json": build_wan22_first_last,
    "wan22-fun-control.json": build_wan22_fun_control,
    "wan22-camera.json": build_wan22_camera,
}


if __name__ == "__main__":
    os.makedirs(TEMPLATES_DIR, exist_ok=True)
    print(f"Generating {len(TEMPLATES)} templates to {TEMPLATES_DIR}/")
    for name, builder in TEMPLATES.items():
        try:
            workflow = builder()
            save(name, workflow)
        except Exception as e:
            print(f"  ERROR {name}: {e}")
            import traceback; traceback.print_exc()
    print("Done!")
