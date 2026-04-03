#!/usr/bin/env python3
"""Generate LLM workflow templates using comfyui_LLM_party nodes.

All INPUT_TYPES, RETURN_TYPES, widget orders, and defaults are extracted
directly from the source code at comfyui_LLM_party/*.py.

Templates:
  1. llm-chat-api.json       - API LLM chat (OpenAI/Gemini/DeepSeek/etc.)
  2. llm-chat-ollama.json    - Local Ollama LLM chat
  3. llm-prompt-enhance.json - LLM enhances prompt → FLUX generates image
  4. llm-script-to-video.json - LLM script → characters → storyboard pipeline
"""

import json, uuid, os

TEMPLATES_DIR = os.path.join(os.path.dirname(__file__), "templates", "comfyui_LLM_party")


# ============================================================
# Node builders — exact INPUT_TYPES from source code
# ============================================================

def node_LLM_api_loader(nid, pos, links_out, title=None, wv_override=None):
    """Source: llm.py line 1208. Exact INPUT_TYPES order."""
    wv = wv_override or ["gpt-4o-mini", "", "", False]
    # widgets_values order: [model_name, base_url, api_key, is_ollama]
    # required: model_name(STRING)
    # optional: base_url(STRING), api_key(STRING), is_ollama(BOOLEAN)
    return {
        "id": nid, "type": "LLM_api_loader", "pos": pos, "size": [400, 150],
        "flags": {}, "order": 0, "mode": 0,
        "inputs": [
            _w("model_name", "STRING"),
            _w("base_url", "STRING"),
            _w("api_key", "STRING"),
            _w("is_ollama", "BOOLEAN"),
        ],
        "outputs": [_o("model", "CUSTOM", links_out, 0)],
        "properties": {"Node name for S&R": "LLM_api_loader"},
        "title": title or "API LLM Loader",
        "widgets_values": wv,
    }


def node_LLM(nid, pos, model_link, links_out, title=None, wv_override=None,
             sys_prompt_input_link=None, user_prompt_input_link=None):
    """Source: llm.py line 1428. Exact INPUT_TYPES order.

    Required widgets order: system_prompt, user_prompt, model(conn), temperature,
    is_memory, is_tools_in_sys_prompt, is_locked, main_brain, max_length

    widgets_values contains ONLY widget values (not connection values).
    Order: system_prompt, user_prompt, temperature, is_memory,
           is_tools_in_sys_prompt, is_locked, main_brain, max_length,
           imgbb_api_key, conversation_rounds, historical_record, is_enable, stream
    """
    wv = wv_override or [
        "You are a helpful AI assistant.",  # system_prompt
        "Hello",                             # user_prompt
        0.7,                                 # temperature
        "enable",                            # is_memory
        "disable",                           # is_tools_in_sys_prompt
        "disable",                           # is_locked
        "enable",                            # main_brain
        1920,                                # max_length
        "",                                  # imgbb_api_key
        100,                                 # conversation_rounds
        "",                                  # historical_record
        True,                                # is_enable
        False,                               # stream
    ]

    inputs = [
        _w("system_prompt", "STRING"),
        _w("user_prompt", "STRING"),
        _c("model", "CUSTOM", model_link),
        _w("temperature", "FLOAT"),
        _w("is_memory", "COMBO"),
        _w("is_tools_in_sys_prompt", "COMBO"),
        _w("is_locked", "COMBO"),
        _w("main_brain", "COMBO"),
        _w("max_length", "INT"),
    ]

    # Optional forceInput connections
    if sys_prompt_input_link is not None:
        inputs.append(_fi("system_prompt_input", "STRING", sys_prompt_input_link))
    if user_prompt_input_link is not None:
        inputs.append(_fi("user_prompt_input", "STRING", user_prompt_input_link))

    out_response = links_out.get(0, [])
    out_history = links_out.get(1, [])
    out_tool = links_out.get(2, [])

    return {
        "id": nid, "type": "LLM", "pos": pos, "size": [450, 400],
        "flags": {}, "order": 0, "mode": 0,
        "inputs": inputs,
        "outputs": [
            _o("assistant_response", "STRING", out_response, 0),
            _o("history", "STRING", out_history, 1),
            _o("tool", "STRING", out_tool, 2),
            _on("image", "IMAGE", 3),
            _on("reasoning_content", "STRING", 4),
        ],
        "properties": {"Node name for S&R": "LLM"},
        "title": title or "LLM Chat",
        "widgets_values": wv,
    }


def node_show_text_party(nid, pos, text_link, title=None):
    """Source: tools/show_text.py. INPUT_IS_LIST=True, OUTPUT_NODE=True."""
    return {
        "id": nid, "type": "show_text_party", "pos": pos, "size": [400, 200],
        "flags": {}, "order": 0, "mode": 0,
        "inputs": [_fi("text", "STRING", text_link)],
        "outputs": [_o("text", "STRING", [], 0)],
        "properties": {"Node name for S&R": "show_text_party"},
        "title": title or "Show Text",
        "widgets_values": [],
    }


def node_CLIPTextEncode_party(nid, pos, clip_link, text_link, links_out, title=None):
    """Source: tools/image.py line 60. required: clip(CLIP), optional: text(STRING)."""
    return {
        "id": nid, "type": "CLIPTextEncode_party", "pos": pos, "size": [300, 100],
        "flags": {}, "order": 0, "mode": 0,
        "inputs": [
            _c("clip", "CLIP", clip_link),
            _fi("text", "STRING", text_link),
        ],
        "outputs": [_o("CONDITIONING", "CONDITIONING", links_out, 0)],
        "properties": {"Node name for S&R": "CLIPTextEncode_party"},
        "title": title or "CLIP Encode (from LLM)",
    }


def node_json_extractor(nid, pos, input_link, links_out, title=None):
    """Source: custom_tool/json_extractor.py line 31. required: input(STRING forceInput), is_enable(BOOLEAN)."""
    return {
        "id": nid, "type": "json_extractor", "pos": pos, "size": [300, 80],
        "flags": {}, "order": 0, "mode": 0,
        "inputs": [
            _fi("input", "STRING", input_link),
            _w("is_enable", "BOOLEAN"),
        ],
        "outputs": [_o("json_output", "STRING", links_out, 0)],
        "properties": {"Node name for S&R": "json_extractor"},
        "title": title or "JSON Extractor",
        "widgets_values": [True],
    }


def node_json_get_value(nid, pos, text_link, key_val, links_out, title=None):
    """Source: custom_tool/json_parser.py line 90. required: text(STRING forceInput), key(STRING), is_enable(BOOLEAN)."""
    return {
        "id": nid, "type": "json_get_value", "pos": pos, "size": [300, 100],
        "flags": {}, "order": 0, "mode": 0,
        "inputs": [
            _fi("text", "STRING", text_link),
            _w("key", "STRING"),
            _w("is_enable", "BOOLEAN"),
        ],
        "outputs": [_o("any", "*", links_out, 0)],
        "properties": {"Node name for S&R": "json_get_value"},
        "title": title or f"Get JSON [{key_val}]",
        "widgets_values": [key_val, True],
    }


# ============================================================
# Input helpers
# ============================================================

def _w(name, typ):
    """Widget input (editable value, no connection)."""
    return {"label": name, "localized_name": name, "name": name, "type": typ,
            "widget": {"name": name}, "link": None}

def _c(name, typ, link):
    """Connection input (from another node)."""
    return {"name": name, "type": typ, "link": link, "label": name, "localized_name": name}

def _fi(name, typ, link):
    """forceInput widget (receives connection, acts as widget)."""
    return {"name": name, "type": typ, "link": link, "label": name, "localized_name": name,
            "widget": {"name": name}}

def _o(name, typ, links, slot=0):
    """Output slot with links."""
    return {"name": name, "type": typ, "links": links or [], "slot_index": slot,
            "label": name, "localized_name": name}

def _on(name, typ, slot=0):
    """Output slot with no links (null)."""
    return {"name": name, "type": typ, "links": None, "slot_index": slot,
            "label": name, "localized_name": name}


# ============================================================
# Workflow builder
# ============================================================

class WF:
    def __init__(self):
        self.nodes = []
        self.links = []
        self._lid = 0
        self._outs = {}

    def L(self, src, ss, tgt, ts, typ):
        self._lid += 1
        self.links.append([self._lid, src, ss, tgt, ts, typ])
        self._outs.setdefault((src, ss), []).append(self._lid)
        return self._lid

    def outs(self, nid, slot):
        return self._outs.get((nid, slot)) or []

    def add(self, node_dict):
        self.nodes.append(node_dict)
        # Fix order
        node_dict["order"] = len(self.nodes) - 1

    def build(self, groups=None):
        return {
            "id": str(uuid.uuid4()), "revision": 0,
            "last_node_id": max(n["id"] for n in self.nodes),
            "last_link_id": self._lid,
            "nodes": self.nodes, "links": self.links,
            "groups": groups or [], "config": {}, "extra": {}, "version": 0.4
        }


def save(name, workflow):
    path = os.path.join(TEMPLATES_DIR, name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(workflow, f, indent=2, ensure_ascii=False)
    print(f"  {name} ({len(workflow['nodes'])} nodes, {len(workflow['links'])} links)")


# ============================================================
# Template 1: LLM Chat (API)
# ============================================================

def build_llm_chat_api():
    w = WF()
    l_model = w.L(1, 0, 2, 2, "CUSTOM")
    l_resp = w.L(2, 0, 3, 0, "STRING")

    w.add(node_LLM_api_loader(1, [0, 0], w.outs(1, 0),
        title="API LLM Loader (change model/url/key)",
        wv_override=["gpt-4o-mini", "https://api.openai.com/v1", "", False]))

    w.add(node_LLM(2, [450, 0], l_model, {0: w.outs(2, 0)},
        title="LLM Chat",
        wv_override=[
            "You are a helpful AI assistant.",
            "Hello, tell me about yourself.",
            0.7, "enable", "disable", "disable", "enable", 1920,
            "", 100, "", True, False,
        ]))

    w.add(node_show_text_party(3, [950, 0], l_resp, "Show Response"))
    return w.build()


# ============================================================
# Template 2: LLM Chat (Ollama)
# ============================================================

def build_llm_chat_ollama():
    w = WF()
    l_model = w.L(1, 0, 2, 2, "CUSTOM")
    l_resp = w.L(2, 0, 3, 0, "STRING")

    w.add(node_LLM_api_loader(1, [0, 0], w.outs(1, 0),
        title="Ollama LLM Loader",
        wv_override=["qwen2.5:14b", "http://127.0.0.1:11434/v1/", "", True]))

    w.add(node_LLM(2, [450, 0], l_model, {0: w.outs(2, 0)},
        title="LLM Chat (Ollama)",
        wv_override=[
            "You are a helpful AI assistant.",
            "Hello, tell me about yourself.",
            0.7, "enable", "disable", "disable", "enable", 4096,
            "", 100, "", True, False,
        ]))

    w.add(node_show_text_party(3, [950, 0], l_resp, "Show Response"))
    return w.build()


# ============================================================
# Template 3: LLM Prompt Enhance → FLUX Image
# ============================================================

def build_llm_prompt_enhance():
    w = WF()

    # LLM chain
    l_model = w.L(1, 0, 2, 2, "CUSTOM")
    l_resp = w.L(2, 0, 5, 1, "STRING")  # LLM response → CLIPTextEncode_party text

    # FLUX chain
    l_clip = w.L(4, 0, 5, 0, "CLIP")
    l_unet_g = w.L(3, 0, 8, 0, "MODEL")
    l_unet_s = w.L(3, 0, 9, 0, "MODEL")
    l_cond = w.L(5, 0, 8, 1, "CONDITIONING")
    l_guider = w.L(8, 0, 12, 1, "GUIDER")
    l_sampler = w.L(10, 0, 12, 2, "SAMPLER")
    l_sigmas = w.L(9, 0, 12, 3, "SIGMAS")
    l_noise = w.L(11, 0, 12, 0, "NOISE")
    l_latent = w.L(7, 0, 12, 4, "LATENT")
    l_sca = w.L(12, 0, 13, 0, "LATENT")
    l_vae = w.L(14, 0, 13, 1, "VAE")
    l_save = w.L(13, 0, 15, 0, "IMAGE")

    # LLM
    w.add(node_LLM_api_loader(1, [0, 0], w.outs(1, 0),
        title="LLM Loader",
        wv_override=["gpt-4o-mini", "https://api.openai.com/v1", "", False]))

    w.add(node_LLM(2, [0, 200], l_model, {0: w.outs(2, 0)},
        title="Prompt Enhancer",
        wv_override=[
            "You are an expert prompt engineer for FLUX image generation. Given a simple description, output ONLY an enhanced detailed prompt in English. Include: subject details, lighting, composition, style, quality tags. Output the prompt only, no explanation.",
            "a cat sitting on a windowsill",
            0.7, "disable", "disable", "disable", "enable", 1920,
            "", 100, "", True, False,
        ]))

    # FLUX loaders
    w.add({"id": 3, "type": "UNETLoader", "pos": [500, 0], "size": [350, 82],
        "flags": {}, "order": 2, "mode": 0,
        "inputs": [_w("unet_name", "COMBO"), _w("weight_dtype", "COMBO")],
        "outputs": [_o("MODEL", "MODEL", w.outs(3, 0))],
        "properties": {"Node name for S&R": "UNETLoader"},
        "title": "FLUX Model", "widgets_values": ["flux1-dev.safetensors", "default"]})

    w.add({"id": 4, "type": "DualCLIPLoader", "pos": [500, 130], "size": [315, 120],
        "flags": {}, "order": 3, "mode": 0,
        "inputs": [_w("clip_name1", "COMBO"), _w("clip_name2", "COMBO"), _w("type", "COMBO")],
        "outputs": [_o("CLIP", "CLIP", w.outs(4, 0))],
        "properties": {"Node name for S&R": "DualCLIPLoader"},
        "title": "FLUX CLIP", "widgets_values": ["clip_l.safetensors", "t5xxl_fp16.safetensors", "flux"]})

    # CLIPTextEncode_party (bridges LLM STRING → CONDITIONING)
    w.add(node_CLIPTextEncode_party(5, [500, 300], l_clip, l_resp, w.outs(5, 0),
        title="Positive (from LLM)"))

    # Empty latent
    w.add({"id": 7, "type": "EmptyLatentImage", "pos": [850, 400], "size": [225, 106],
        "flags": {}, "order": 5, "mode": 0,
        "inputs": [_w("width", "INT"), _w("height", "INT"), _w("batch_size", "INT")],
        "outputs": [_o("LATENT", "LATENT", w.outs(7, 0))],
        "properties": {"Node name for S&R": "EmptyLatentImage"},
        "widgets_values": [1024, 1024, 1]})

    # FLUX advanced sampling
    w.add({"id": 8, "type": "BasicGuider", "pos": [850, 0], "size": [225, 72],
        "flags": {}, "order": 6, "mode": 0,
        "inputs": [_c("model", "MODEL", l_unet_g), _c("conditioning", "CONDITIONING", l_cond)],
        "outputs": [_o("GUIDER", "GUIDER", w.outs(8, 0))],
        "properties": {"Node name for S&R": "BasicGuider"}})

    w.add({"id": 9, "type": "BasicScheduler", "pos": [850, 120], "size": [225, 106],
        "flags": {}, "order": 7, "mode": 0,
        "inputs": [_c("model", "MODEL", l_unet_s), _w("scheduler", "COMBO"),
                   _w("steps", "INT"), _w("denoise", "FLOAT")],
        "outputs": [_o("SIGMAS", "SIGMAS", w.outs(9, 0))],
        "properties": {"Node name for S&R": "BasicScheduler"},
        "widgets_values": ["simple", 20, 1.0]})

    w.add({"id": 10, "type": "KSamplerSelect", "pos": [850, 275], "size": [225, 58],
        "flags": {}, "order": 8, "mode": 0,
        "inputs": [_w("sampler_name", "COMBO")],
        "outputs": [_o("SAMPLER", "SAMPLER", w.outs(10, 0))],
        "properties": {"Node name for S&R": "KSamplerSelect"},
        "widgets_values": ["euler"]})

    w.add({"id": 11, "type": "RandomNoise", "pos": [850, 340], "size": [225, 82],
        "flags": {}, "order": 9, "mode": 0,
        "inputs": [_w("noise_seed", "INT"), _w("control_after_generate", "COMBO")],
        "outputs": [_o("NOISE", "NOISE", w.outs(11, 0))],
        "properties": {"Node name for S&R": "RandomNoise"},
        "widgets_values": [0, "randomize"]})

    w.add({"id": 12, "type": "SamplerCustomAdvanced", "pos": [1150, 0], "size": [280, 160],
        "flags": {}, "order": 10, "mode": 0,
        "inputs": [_c("noise", "NOISE", l_noise), _c("guider", "GUIDER", l_guider),
                   _c("sampler", "SAMPLER", l_sampler), _c("sigmas", "SIGMAS", l_sigmas),
                   _c("latent_image", "LATENT", l_latent)],
        "outputs": [_o("output", "LATENT", w.outs(12, 0)), _on("denoised_output", "LATENT", 1)],
        "properties": {"Node name for S&R": "SamplerCustomAdvanced"}})

    w.add({"id": 14, "type": "VAELoader", "pos": [1150, 200], "size": [290, 82],
        "flags": {}, "order": 11, "mode": 0,
        "inputs": [_w("vae_name", "COMBO")],
        "outputs": [_o("VAE", "VAE", w.outs(14, 0))],
        "properties": {"Node name for S&R": "VAELoader"},
        "title": "FLUX VAE", "widgets_values": ["ae.safetensors"]})

    w.add({"id": 13, "type": "VAEDecode", "pos": [1500, 0], "size": [265, 72],
        "flags": {}, "order": 12, "mode": 0,
        "inputs": [_c("samples", "LATENT", l_sca), _c("vae", "VAE", l_vae)],
        "outputs": [_o("IMAGE", "IMAGE", w.outs(13, 0))],
        "properties": {"Node name for S&R": "VAEDecode"}})

    w.add({"id": 15, "type": "SaveImage", "pos": [1500, 120], "size": [320, 270],
        "flags": {}, "order": 13, "mode": 0,
        "inputs": [_c("images", "IMAGE", l_save), _w("filename_prefix", "STRING")],
        "outputs": [],
        "properties": {"Node name for S&R": "SaveImage"},
        "title": "Save Image", "widgets_values": ["ComfyUI_LLM_Enhanced"]})

    return w.build(groups=[
        {"title": "LLM Prompt Enhancement", "bounding": [-30, -50, 500, 620], "color": "#2A2", "font_size": 24},
        {"title": "FLUX Image Generation", "bounding": [470, -50, 1100, 530], "color": "#28A", "font_size": 24},
    ])


# ============================================================
# Template 4: LLM Script → Characters → Storyboard Pipeline
# ============================================================

def build_llm_script_to_video():
    w = WF()

    # LLM loader shared by all 3 LLM nodes
    l_m1 = w.L(1, 0, 2, 2, "CUSTOM")
    l_m2 = w.L(1, 0, 3, 2, "CUSTOM")
    l_m3 = w.L(1, 0, 4, 2, "CUSTOM")

    # Script → char LLM (via user_prompt_input forceInput)
    l_script_to_char = w.L(2, 0, 3, 9, "STRING")  # slot 9 = user_prompt_input
    l_script_to_story = w.L(2, 0, 4, 9, "STRING")

    # Show outputs
    l_script_show = w.L(2, 0, 20, 0, "STRING")
    l_char_show = w.L(3, 0, 21, 0, "STRING")
    l_story_show = w.L(4, 0, 22, 0, "STRING")

    # LLM Loader
    w.add(node_LLM_api_loader(1, [0, 0], w.outs(1, 0),
        title="LLM Loader (set your provider)",
        wv_override=["gpt-4o-mini", "https://api.openai.com/v1", "", False]))

    # Stage 1: Script
    w.add(node_LLM(2, [0, 200], l_m1, {0: w.outs(2, 0)},
        title="Stage 1: Generate Script",
        wv_override=[
            "You are a professional screenwriter. Write a short cinematic script (3 scenes) based on the user's input. Include vivid scene descriptions, character actions, and dialogue. Keep it concise.",
            "A warrior princess must retrieve a stolen artifact from a dragon's lair",
            0.7, "disable", "disable", "disable", "enable", 4096,
            "", 100, "", True, False,
        ]))

    # Stage 2: Characters
    w.add(node_LLM(3, [500, 200], l_m2, {0: w.outs(3, 0)},
        title="Stage 2: Extract Characters",
        user_prompt_input_link=l_script_to_char,
        wv_override=[
            "From the script below, extract the main character. Output ONLY a detailed visual description suitable for AI image generation: appearance, clothing, expression, pose. English only, single paragraph, no JSON.",
            "",
            0.7, "disable", "disable", "disable", "enable", 2048,
            "", 100, "", True, False,
        ]))

    # Stage 3: Storyboard
    w.add(node_LLM(4, [1000, 200], l_m3, {0: w.outs(4, 0)},
        title="Stage 3: Generate Storyboard",
        user_prompt_input_link=l_script_to_story,
        wv_override=[
            "From the script below, create exactly 3 video shots. For each shot, output ONE line with a detailed video generation prompt describing scene action, camera movement, lighting, mood. English only, one line per shot, no numbering.",
            "",
            0.7, "disable", "disable", "disable", "enable", 2048,
            "", 100, "", True, False,
        ]))

    # Show outputs
    w.add(node_show_text_party(20, [0, 680], l_script_show, "Script Output"))
    w.add(node_show_text_party(21, [500, 680], l_char_show, "Character Description"))
    w.add(node_show_text_party(22, [1000, 680], l_story_show, "Storyboard Shots"))

    return w.build(groups=[
        {"title": "LLM Script Pipeline (connect outputs to FLUX + Wan2.2 for full video)", "bounding": [-30, -50, 1500, 920], "color": "#88A", "font_size": 24},
    ])


# ============================================================
# Main
# ============================================================

TEMPLATES = {
    "llm-chat-api.json": build_llm_chat_api,
    "llm-chat-ollama.json": build_llm_chat_ollama,
    "llm-prompt-enhance.json": build_llm_prompt_enhance,
    "llm-script-to-video.json": build_llm_script_to_video,
}

if __name__ == "__main__":
    os.makedirs(TEMPLATES_DIR, exist_ok=True)
    print(f"Generating {len(TEMPLATES)} LLM templates to {TEMPLATES_DIR}/:")
    for name, builder in TEMPLATES.items():
        try:
            save(name, builder())
        except Exception as e:
            print(f"  ERROR {name}: {e}")
            import traceback; traceback.print_exc()
    print("Done!")
