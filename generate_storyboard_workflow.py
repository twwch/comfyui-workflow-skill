#!/usr/bin/env python3
"""Generate a complete ComfyUI workflow for the storyboard video pipeline.

Pipeline (no JSON parsing nodes needed):
1. LLM generates script from user input
2. LLM directly outputs character appearance prompt (English)
3. LLM directly outputs scene image prompt (English)
4. LLM directly outputs video motion prompt (English)
5. FLUX generates character reference image
6. FLUX generates storyboard reference image
7. Wan 2.2 I2V generates 10s video from reference image

Uses comfyui_LLM_party nodes: LLM_api_loader, LLM
"""

import json
import uuid


def make_input(name, type_, widget=False, link=None, shape=None):
    inp = {
        "name": name,
        "type": type_,
        "link": link,
        "label": name,
        "localized_name": name,
    }
    if widget:
        inp["widget"] = {"name": name}
    if shape is not None:
        inp["shape"] = shape
    return inp


def make_output(name, type_, links=None, slot_index=0):
    return {
        "name": name,
        "type": type_,
        "links": links or [],
        "slot_index": slot_index,
        "label": name,
        "localized_name": name,
    }


def make_node(id_, type_, pos, size, order, title=None, inputs=None, outputs=None,
              widgets_values=None, properties=None, color=None, bgcolor=None, mode=0):
    node = {
        "id": id_,
        "type": type_,
        "pos": pos,
        "size": size,
        "flags": {},
        "order": order,
        "mode": mode,
        "inputs": inputs or [],
        "outputs": outputs or [],
        "properties": properties or {"Node name for S&R": type_},
        "widgets_values": widgets_values or [],
    }
    if title:
        node["title"] = title
    if color:
        node["color"] = color
        node["bgcolor"] = bgcolor
    return node


def make_llm_outputs():
    """Standard LLM node outputs."""
    return [
        make_output("assistant_response", "STRING", slot_index=0),
        make_output("history", "STRING", slot_index=1),
        make_output("tool", "STRING", slot_index=2),
        make_output("image", "IMAGE", slot_index=3),
    ]


def build_workflow():
    nodes = []
    links = []
    link_id = 0

    def add_link(src_node, src_slot, tgt_node, tgt_slot, type_):
        nonlocal link_id
        link_id += 1
        links.append([link_id, src_node, src_slot, tgt_node, tgt_slot, type_])
        return link_id

    # ============================================================
    # GROUP 1: LLM Pipeline (Nodes 1-5)
    #   No JSON parsing — each LLM directly outputs usable text
    # ============================================================

    # Node 1: LLM_api_loader (Gemini)
    nodes.append(make_node(
        1, "LLM_api_loader", [0, 0], [400, 150], 0,
        title="1. Load Gemini LLM",
        inputs=[
            make_input("model_name", "STRING", widget=True),
            make_input("base_url", "STRING", widget=True),
            make_input("api_key", "STRING", widget=True),
            make_input("is_ollama", "BOOLEAN", widget=True),
        ],
        outputs=[make_output("model", "CUSTOM", slot_index=0)],
        widgets_values=[
            "gemini-3-pro-preview",
            "https://generativelanguage.googleapis.com/v1beta/openai",
            "YOUR_GEMINI_API_KEY",
            False,
        ],
    ))

    # Node 2: LLM - Script Generation
    l_m1 = add_link(1, 0, 2, 2, "CUSTOM")
    nodes.append(make_node(
        2, "LLM", [500, 0], [450, 300], 1,
        title="2. Generate Script",
        inputs=[
            make_input("system_prompt", "STRING", widget=True),
            make_input("user_prompt", "STRING", widget=True),
            make_input("model", "CUSTOM", link=l_m1),
            make_input("temperature", "FLOAT", widget=True),
            make_input("max_length", "INT", widget=True),
        ],
        outputs=make_llm_outputs(),
        widgets_values=[
            "你是一位专业编剧。根据用户提供的主题，创作一个完整的短视频剧本（约100秒，10个场景）。\n剧本应包含：场景描述、角色动作、情绪变化、镜头提示。\n要求：画面感强，适合AI视频生成，每个场景约10秒。\n输出纯文本剧本。",
            "请在此输入你的故事主题，例如：一个孤独的宇航员在火星上发现了一朵花",
            0.8,
            4096,
        ],
        color="#232", bgcolor="#353",
    ))

    # Node 3: LLM - Generate Character Appearance Prompt (直接输出英文提示词)
    l_m2 = add_link(1, 0, 3, 2, "CUSTOM")
    l_script_to_char = add_link(2, 0, 3, 5, "STRING")
    nodes.append(make_node(
        3, "LLM", [1050, 0], [450, 300], 2,
        title="3. Character Prompt (English)",
        inputs=[
            make_input("system_prompt", "STRING", widget=True),
            make_input("user_prompt", "STRING", widget=True),
            make_input("model", "CUSTOM", link=l_m2),
            make_input("temperature", "FLOAT", widget=True),
            make_input("max_length", "INT", widget=True),
            make_input("user_prompt_input", "STRING", link=l_script_to_char),
        ],
        outputs=make_llm_outputs(),
        widgets_values=[
            "你是角色设计专家。阅读剧本后，为主角生成一段详细的英文外观描述，直接用于AI绘图。\n\n要求：\n- 只输出一段英文描述，不要JSON，不要中文，不要任何格式标记\n- 描述内容包括：gender, age, hair color and style, eye color, skin tone, clothing details, accessories, body type, distinctive features\n- 末尾加上：full body portrait, white background, character concept art, high detail, 8k\n- 只输出一个主角的描述\n\n示例输出：\nA young woman in her mid-20s with long flowing black hair, bright amber eyes, fair skin, wearing a fitted dark blue space suit with silver accents, slim athletic build, determined expression, full body portrait, white background, character concept art, high detail, 8k",
            "请为以下剧本的主角生成绘图提示词：",
            0.4,
            1024,
        ],
    ))

    # Node 4: LLM - Generate Scene Image Prompt (直接输出英文提示词)
    l_m3 = add_link(1, 0, 4, 2, "CUSTOM")
    l_script_to_scene = add_link(2, 0, 4, 5, "STRING")
    nodes.append(make_node(
        4, "LLM", [1050, 380], [450, 300], 3,
        title="4. Scene Image Prompt (English)",
        inputs=[
            make_input("system_prompt", "STRING", widget=True),
            make_input("user_prompt", "STRING", widget=True),
            make_input("model", "CUSTOM", link=l_m3),
            make_input("temperature", "FLOAT", widget=True),
            make_input("max_length", "INT", widget=True),
            make_input("user_prompt_input", "STRING", link=l_script_to_scene),
        ],
        outputs=make_llm_outputs(),
        widgets_values=[
            "你是专业分镜师。阅读剧本后，为第1个分镜（前10秒）生成一段英文场景图片描述，直接用于AI绘图。\n\n要求：\n- 只输出一段英文描述，不要JSON，不要中文，不要格式标记\n- 描述场景构图、光影、人物位置、环境细节\n- 末尾加上：cinematic composition, dramatic lighting, high detail, 8k, photorealistic\n- 适合生成16:9画面(832x480)\n\n示例输出：\nA lone astronaut stands at the edge of a vast Martian canyon, red dust swirling around their boots, Earth visible as a tiny blue dot in the amber sky, wide establishing shot, cinematic composition, dramatic lighting, high detail, 8k, photorealistic",
            "请为以下剧本的第1个分镜生成场景图片提示词：",
            0.5,
            1024,
        ],
    ))

    # Node 5: LLM - Generate Video Motion Prompt (直接输出英文提示词)
    l_m4 = add_link(1, 0, 5, 2, "CUSTOM")
    l_script_to_vid = add_link(2, 0, 5, 5, "STRING")
    nodes.append(make_node(
        5, "LLM", [1050, 760], [450, 300], 4,
        title="5. Video Motion Prompt (English)",
        inputs=[
            make_input("system_prompt", "STRING", widget=True),
            make_input("user_prompt", "STRING", widget=True),
            make_input("model", "CUSTOM", link=l_m4),
            make_input("temperature", "FLOAT", widget=True),
            make_input("max_length", "INT", widget=True),
            make_input("user_prompt_input", "STRING", link=l_script_to_vid),
        ],
        outputs=make_llm_outputs(),
        widgets_values=[
            "你是视频导演。阅读剧本后，为第1个分镜（前10秒）生成一段英文视频运动描述，用于AI视频生成。\n\n要求：\n- 只输出一段英文描述，不要JSON，不要中文，不要格式标记\n- 重点描述：动作、运动方向、镜头移动（pan, zoom, dolly, tracking shot等）、速度节奏\n- 末尾加上：cinematic quality, smooth motion, high detail\n\n示例输出：\nThe camera slowly dollies forward toward the astronaut as wind picks up red dust around them, the astronaut takes a tentative step forward and reaches down, camera tilts down to follow the movement, gentle and contemplative pacing, cinematic quality, smooth motion, high detail",
            "请为以下剧本的第1个分镜生成视频运动提示词：",
            0.5,
            1024,
        ],
    ))

    # ============================================================
    # GROUP 2: FLUX Character Reference Image (Nodes 10-21)
    # ============================================================

    # Node 10: UNETLoader (FLUX)
    nodes.append(make_node(
        10, "UNETLoader", [1700, 0], [350, 82], 5,
        title="Load FLUX Model",
        inputs=[
            make_input("unet_name", "COMBO", widget=True),
            make_input("weight_dtype", "COMBO", widget=True),
        ],
        outputs=[make_output("MODEL", "MODEL", slot_index=0)],
        widgets_values=["flux1-dev.safetensors", "default"],
    ))

    # Node 11: DualCLIPLoader (FLUX)
    nodes.append(make_node(
        11, "DualCLIPLoader", [1700, 130], [350, 120], 6,
        title="Load CLIP (FLUX)",
        inputs=[
            make_input("clip_name1", "COMBO", widget=True),
            make_input("clip_name2", "COMBO", widget=True),
            make_input("type", "COMBO", widget=True),
        ],
        outputs=[make_output("CLIP", "CLIP", slot_index=0)],
        widgets_values=["clip_l.safetensors", "t5xxl_fp16.safetensors", "flux"],
    ))

    # Node 12: VAELoader (FLUX)
    nodes.append(make_node(
        12, "VAELoader", [1700, 300], [290, 82], 7,
        title="Load VAE (FLUX)",
        inputs=[make_input("vae_name", "COMBO", widget=True)],
        outputs=[make_output("VAE", "VAE", slot_index=0)],
        widgets_values=["ae.safetensors"],
    ))

    # Node 13: CLIPTextEncodeFlux (character prompt from LLM Node 3)
    l_clip_to_enc1 = add_link(11, 0, 13, 0, "CLIP")
    l_char_to_l = add_link(3, 0, 13, 1, "STRING")  # LLM output → clip_l
    l_char_to_t5 = add_link(3, 0, 13, 2, "STRING")  # LLM output → t5xxl
    nodes.append(make_node(
        13, "CLIPTextEncodeFlux", [2150, 0], [350, 180], 8,
        title="Encode Character Prompt",
        inputs=[
            make_input("clip", "CLIP", link=l_clip_to_enc1),
            make_input("clip_l", "STRING", widget=True, link=l_char_to_l),
            make_input("t5xxl", "STRING", widget=True, link=l_char_to_t5),
            make_input("guidance", "FLOAT", widget=True),
        ],
        outputs=[make_output("CONDITIONING", "CONDITIONING", slot_index=0)],
        widgets_values=["character concept art", "character concept art, full body portrait, white background, high detail", 3.5],
        color="#232", bgcolor="#353",
    ))

    # Node 14: EmptyLatentImage (1024x1024 for character)
    nodes.append(make_node(
        14, "EmptyLatentImage", [2150, 230], [225, 106], 9,
        title="Character Latent (1024x1024)",
        inputs=[
            make_input("width", "INT", widget=True),
            make_input("height", "INT", widget=True),
            make_input("batch_size", "INT", widget=True),
        ],
        outputs=[make_output("LATENT", "LATENT", slot_index=0)],
        widgets_values=[1024, 1024, 1],
    ))

    # Node 15: BasicGuider
    l_model_g1 = add_link(10, 0, 15, 0, "MODEL")
    l_cond_g1 = add_link(13, 0, 15, 1, "CONDITIONING")
    nodes.append(make_node(
        15, "BasicGuider", [2550, 0], [225, 72], 10,
        title="Guider (Character)",
        inputs=[
            make_input("model", "MODEL", link=l_model_g1),
            make_input("conditioning", "CONDITIONING", link=l_cond_g1),
        ],
        outputs=[make_output("GUIDER", "GUIDER", slot_index=0)],
    ))

    # Node 16: KSamplerSelect
    nodes.append(make_node(
        16, "KSamplerSelect", [2550, 120], [225, 58], 11,
        inputs=[make_input("sampler_name", "COMBO", widget=True)],
        outputs=[make_output("SAMPLER", "SAMPLER", slot_index=0)],
        widgets_values=["euler"],
    ))

    # Node 17: BasicScheduler
    l_model_s1 = add_link(10, 0, 17, 0, "MODEL")
    nodes.append(make_node(
        17, "BasicScheduler", [2550, 230], [225, 106], 12,
        title="Scheduler (Character)",
        inputs=[
            make_input("model", "MODEL", link=l_model_s1),
            make_input("scheduler", "COMBO", widget=True),
            make_input("steps", "INT", widget=True),
            make_input("denoise", "FLOAT", widget=True),
        ],
        outputs=[make_output("SIGMAS", "SIGMAS", slot_index=0)],
        widgets_values=["simple", 20, 1.0],
    ))

    # Node 18: RandomNoise
    nodes.append(make_node(
        18, "RandomNoise", [2550, 390], [225, 58], 13,
        inputs=[
            make_input("noise_seed", "INT", widget=True),
            make_input("control_after_generate", "COMBO", widget=True),
        ],
        outputs=[make_output("NOISE", "NOISE", slot_index=0)],
        widgets_values=[0, "randomize"],
    ))

    # Node 19: SamplerCustomAdvanced (Character)
    l_n1 = add_link(18, 0, 19, 0, "NOISE")
    l_g1 = add_link(15, 0, 19, 1, "GUIDER")
    l_sp1 = add_link(16, 0, 19, 2, "SAMPLER")
    l_sg1 = add_link(17, 0, 19, 3, "SIGMAS")
    l_lt1 = add_link(14, 0, 19, 4, "LATENT")
    nodes.append(make_node(
        19, "SamplerCustomAdvanced", [2850, 0], [280, 160], 14,
        title="Sample (Character)",
        inputs=[
            make_input("noise", "NOISE", link=l_n1),
            make_input("guider", "GUIDER", link=l_g1),
            make_input("sampler", "SAMPLER", link=l_sp1),
            make_input("sigmas", "SIGMAS", link=l_sg1),
            make_input("latent_image", "LATENT", link=l_lt1),
        ],
        outputs=[
            make_output("output", "LATENT", slot_index=0),
            make_output("denoised_output", "LATENT", slot_index=1),
        ],
    ))

    # Node 20: VAEDecode (Character)
    l_lo1 = add_link(19, 0, 20, 0, "LATENT")
    l_v1 = add_link(12, 0, 20, 1, "VAE")
    nodes.append(make_node(
        20, "VAEDecode", [3200, 0], [265, 72], 15,
        title="Decode (Character)",
        inputs=[
            make_input("samples", "LATENT", link=l_lo1),
            make_input("vae", "VAE", link=l_v1),
        ],
        outputs=[make_output("IMAGE", "IMAGE", slot_index=0)],
    ))

    # Node 21: SaveImage (Character Reference)
    l_ic = add_link(20, 0, 21, 0, "IMAGE")
    nodes.append(make_node(
        21, "SaveImage", [3200, 130], [320, 270], 16,
        title="Save Character Reference",
        inputs=[
            make_input("images", "IMAGE", link=l_ic),
            make_input("filename_prefix", "STRING", widget=True),
        ],
        outputs=[],
        widgets_values=["character_ref"],
    ))

    # ============================================================
    # GROUP 3: FLUX Storyboard Reference Image (Nodes 22-29)
    # ============================================================

    # Node 22: CLIPTextEncodeFlux (scene prompt from LLM Node 4)
    l_clip_to_enc2 = add_link(11, 0, 22, 0, "CLIP")
    l_scene_to_l = add_link(4, 0, 22, 1, "STRING")
    l_scene_to_t5 = add_link(4, 0, 22, 2, "STRING")
    nodes.append(make_node(
        22, "CLIPTextEncodeFlux", [2150, 500], [350, 180], 17,
        title="Encode Scene Prompt",
        inputs=[
            make_input("clip", "CLIP", link=l_clip_to_enc2),
            make_input("clip_l", "STRING", widget=True, link=l_scene_to_l),
            make_input("t5xxl", "STRING", widget=True, link=l_scene_to_t5),
            make_input("guidance", "FLOAT", widget=True),
        ],
        outputs=[make_output("CONDITIONING", "CONDITIONING", slot_index=0)],
        widgets_values=["cinematic scene", "cinematic scene, detailed, high quality", 3.5],
        color="#232", bgcolor="#353",
    ))

    # Node 23: EmptyLatentImage (832x480)
    nodes.append(make_node(
        23, "EmptyLatentImage", [2150, 730], [225, 106], 18,
        title="Storyboard Latent (832x480)",
        inputs=[
            make_input("width", "INT", widget=True),
            make_input("height", "INT", widget=True),
            make_input("batch_size", "INT", widget=True),
        ],
        outputs=[make_output("LATENT", "LATENT", slot_index=0)],
        widgets_values=[832, 480, 1],
    ))

    # Node 24: BasicGuider (Storyboard)
    l_model_g2 = add_link(10, 0, 24, 0, "MODEL")
    l_cond_g2 = add_link(22, 0, 24, 1, "CONDITIONING")
    nodes.append(make_node(
        24, "BasicGuider", [2550, 500], [225, 72], 19,
        title="Guider (Storyboard)",
        inputs=[
            make_input("model", "MODEL", link=l_model_g2),
            make_input("conditioning", "CONDITIONING", link=l_cond_g2),
        ],
        outputs=[make_output("GUIDER", "GUIDER", slot_index=0)],
    ))

    # Node 25: BasicScheduler (Storyboard)
    l_model_s2 = add_link(10, 0, 25, 0, "MODEL")
    nodes.append(make_node(
        25, "BasicScheduler", [2550, 620], [225, 106], 20,
        title="Scheduler (Storyboard)",
        inputs=[
            make_input("model", "MODEL", link=l_model_s2),
            make_input("scheduler", "COMBO", widget=True),
            make_input("steps", "INT", widget=True),
            make_input("denoise", "FLOAT", widget=True),
        ],
        outputs=[make_output("SIGMAS", "SIGMAS", slot_index=0)],
        widgets_values=["simple", 20, 1.0],
    ))

    # Node 26: RandomNoise (Storyboard)
    nodes.append(make_node(
        26, "RandomNoise", [2550, 780], [225, 58], 21,
        inputs=[
            make_input("noise_seed", "INT", widget=True),
            make_input("control_after_generate", "COMBO", widget=True),
        ],
        outputs=[make_output("NOISE", "NOISE", slot_index=0)],
        widgets_values=[0, "randomize"],
    ))

    # Node 27: SamplerCustomAdvanced (Storyboard)
    l_n2 = add_link(26, 0, 27, 0, "NOISE")
    l_g2 = add_link(24, 0, 27, 1, "GUIDER")
    l_sp2 = add_link(16, 0, 27, 2, "SAMPLER")  # reuse sampler
    l_sg2 = add_link(25, 0, 27, 3, "SIGMAS")
    l_lt2 = add_link(23, 0, 27, 4, "LATENT")
    nodes.append(make_node(
        27, "SamplerCustomAdvanced", [2850, 500], [280, 160], 22,
        title="Sample (Storyboard)",
        inputs=[
            make_input("noise", "NOISE", link=l_n2),
            make_input("guider", "GUIDER", link=l_g2),
            make_input("sampler", "SAMPLER", link=l_sp2),
            make_input("sigmas", "SIGMAS", link=l_sg2),
            make_input("latent_image", "LATENT", link=l_lt2),
        ],
        outputs=[
            make_output("output", "LATENT", slot_index=0),
            make_output("denoised_output", "LATENT", slot_index=1),
        ],
    ))

    # Node 28: VAEDecode (Storyboard)
    l_lo2 = add_link(27, 0, 28, 0, "LATENT")
    l_v2 = add_link(12, 0, 28, 1, "VAE")
    nodes.append(make_node(
        28, "VAEDecode", [3200, 500], [265, 72], 23,
        title="Decode (Storyboard)",
        inputs=[
            make_input("samples", "LATENT", link=l_lo2),
            make_input("vae", "VAE", link=l_v2),
        ],
        outputs=[make_output("IMAGE", "IMAGE", slot_index=0)],
    ))

    # Node 29: SaveImage (Storyboard Reference)
    l_is = add_link(28, 0, 29, 0, "IMAGE")
    nodes.append(make_node(
        29, "SaveImage", [3200, 630], [320, 270], 24,
        title="Save Storyboard Reference",
        inputs=[
            make_input("images", "IMAGE", link=l_is),
            make_input("filename_prefix", "STRING", widget=True),
        ],
        outputs=[],
        widgets_values=["storyboard_ref_shot1"],
    ))

    # ============================================================
    # GROUP 4: Wan 2.2 I2V Video Generation (Nodes 30-40)
    # ============================================================

    # Node 30: UNETLoader (Wan 2.2 I2V)
    nodes.append(make_node(
        30, "UNETLoader", [3700, 0], [350, 82], 25,
        title="Load Wan 2.2 I2V Model",
        inputs=[
            make_input("unet_name", "COMBO", widget=True),
            make_input("weight_dtype", "COMBO", widget=True),
        ],
        outputs=[make_output("MODEL", "MODEL", slot_index=0)],
        widgets_values=["wan2.2_i2v_480p_14b.safetensors", "default"],
    ))

    # Node 31: CLIPLoader (Wan)
    nodes.append(make_node(
        31, "CLIPLoader", [3700, 130], [290, 120], 26,
        title="Load CLIP (Wan)",
        inputs=[
            make_input("clip_name", "COMBO", widget=True),
            make_input("type", "COMBO", widget=True),
            make_input("device", "COMBO", widget=True),
        ],
        outputs=[make_output("CLIP", "CLIP", slot_index=0)],
        widgets_values=["umt5_xxl_fp16.safetensors", "wan", "default"],
    ))

    # Node 32: VAELoader (Wan)
    nodes.append(make_node(
        32, "VAELoader", [3700, 300], [290, 82], 27,
        title="Load VAE (Wan)",
        inputs=[make_input("vae_name", "COMBO", widget=True)],
        outputs=[make_output("VAE", "VAE", slot_index=0)],
        widgets_values=["wan_2.1_vae.safetensors"],
    ))

    # Node 33: CLIPVisionLoader
    nodes.append(make_node(
        33, "CLIPVisionLoader", [3700, 430], [290, 82], 28,
        title="Load CLIP Vision",
        inputs=[make_input("clip_name", "COMBO", widget=True)],
        outputs=[make_output("CLIP_VISION", "CLIP_VISION", slot_index=0)],
        widgets_values=["clip_vision_h.safetensors"],
    ))

    # Node 34: CLIPVisionEncode
    l_cv = add_link(33, 0, 34, 0, "CLIP_VISION")
    l_si = add_link(28, 0, 34, 1, "IMAGE")  # storyboard image → clip vision
    nodes.append(make_node(
        34, "CLIPVisionEncode", [4100, 430], [250, 100], 29,
        title="Encode Storyboard for Video",
        inputs=[
            make_input("clip_vision", "CLIP_VISION", link=l_cv),
            make_input("image", "IMAGE", link=l_si),
            make_input("crop", "COMBO", widget=True),
        ],
        outputs=[make_output("CLIP_VISION_OUTPUT", "CLIP_VISION_OUTPUT", slot_index=0)],
        widgets_values=["center"],
    ))

    # Node 35: CLIPTextEncode (Wan positive - video prompt from LLM Node 5)
    l_wcp = add_link(31, 0, 35, 0, "CLIP")
    l_vp = add_link(5, 0, 35, 1, "STRING")  # LLM video prompt → text
    nodes.append(make_node(
        35, "CLIPTextEncode", [4100, 0], [350, 120], 30,
        title="Video Positive Prompt",
        inputs=[
            make_input("clip", "CLIP", link=l_wcp),
            make_input("text", "STRING", widget=True, link=l_vp),
        ],
        outputs=[make_output("CONDITIONING", "CONDITIONING", slot_index=0)],
        widgets_values=["cinematic motion, smooth camera, high quality video"],
        color="#232", bgcolor="#353",
    ))

    # Node 36: CLIPTextEncode (Wan negative)
    l_wcn = add_link(31, 0, 36, 0, "CLIP")
    nodes.append(make_node(
        36, "CLIPTextEncode", [4100, 170], [350, 120], 31,
        title="Video Negative Prompt",
        inputs=[
            make_input("clip", "CLIP", link=l_wcn),
            make_input("text", "STRING", widget=True),
        ],
        outputs=[make_output("CONDITIONING", "CONDITIONING", slot_index=0)],
        widgets_values=["worst quality, blurry, distorted, static, watermark, jittery, low resolution"],
        color="#322", bgcolor="#533",
    ))

    # Node 37: WanImageToVideo
    l_pw = add_link(35, 0, 37, 0, "CONDITIONING")
    l_nw = add_link(36, 0, 37, 1, "CONDITIONING")
    l_vw = add_link(32, 0, 37, 2, "VAE")
    l_co = add_link(34, 0, 37, 3, "CLIP_VISION_OUTPUT")
    l_sw = add_link(28, 0, 37, 4, "IMAGE")  # storyboard ref as start_image
    nodes.append(make_node(
        37, "WanImageToVideo", [4550, 0], [280, 300], 32,
        title="Wan 2.2 I2V (10s Video)",
        inputs=[
            make_input("positive", "CONDITIONING", link=l_pw),
            make_input("negative", "CONDITIONING", link=l_nw),
            make_input("vae", "VAE", link=l_vw),
            make_input("clip_vision_output", "CLIP_VISION_OUTPUT", link=l_co, shape=7),
            make_input("start_image", "IMAGE", link=l_sw, shape=7),
            make_input("width", "INT", widget=True),
            make_input("height", "INT", widget=True),
            make_input("length", "INT", widget=True),
            make_input("batch_size", "INT", widget=True),
        ],
        outputs=[
            make_output("positive", "CONDITIONING", slot_index=0),
            make_output("negative", "CONDITIONING", slot_index=1),
            make_output("latent", "LATENT", slot_index=2),
        ],
        widgets_values=[832, 480, 161, 1],  # 161 frames ≈ 10s at 16fps
    ))

    # Node 38: KSampler (Wan video)
    l_wm = add_link(30, 0, 38, 0, "MODEL")
    l_wp = add_link(37, 0, 38, 1, "CONDITIONING")
    l_wn = add_link(37, 1, 38, 2, "CONDITIONING")
    l_wl = add_link(37, 2, 38, 3, "LATENT")
    nodes.append(make_node(
        38, "KSampler", [4900, 0], [300, 340], 33,
        title="Sample Video",
        inputs=[
            make_input("model", "MODEL", link=l_wm),
            make_input("positive", "CONDITIONING", link=l_wp),
            make_input("negative", "CONDITIONING", link=l_wn),
            make_input("latent_image", "LATENT", link=l_wl),
            make_input("seed", "INT", widget=True),
            make_input("control_after_generate", "COMBO", widget=True),
            make_input("steps", "INT", widget=True),
            make_input("cfg", "FLOAT", widget=True),
            make_input("sampler_name", "COMBO", widget=True),
            make_input("scheduler", "COMBO", widget=True),
            make_input("denoise", "FLOAT", widget=True),
        ],
        outputs=[make_output("LATENT", "LATENT", slot_index=0)],
        widgets_values=[0, "randomize", 25, 6.0, "euler", "normal", 1.0],
    ))

    # Node 39: VAEDecode (Video)
    l_vl = add_link(38, 0, 39, 0, "LATENT")
    l_vv = add_link(32, 0, 39, 1, "VAE")
    nodes.append(make_node(
        39, "VAEDecode", [5250, 0], [265, 72], 34,
        title="Decode Video",
        inputs=[
            make_input("samples", "LATENT", link=l_vl),
            make_input("vae", "VAE", link=l_vv),
        ],
        outputs=[make_output("IMAGE", "IMAGE", slot_index=0)],
    ))

    # Node 40: SaveAnimatedWEBP
    l_vi = add_link(39, 0, 40, 0, "IMAGE")
    nodes.append(make_node(
        40, "SaveAnimatedWEBP", [5250, 130], [320, 270], 35,
        title="Save Video (10s WEBP)",
        inputs=[
            make_input("images", "IMAGE", link=l_vi),
            make_input("filename_prefix", "STRING", widget=True),
            make_input("fps", "FLOAT", widget=True),
            make_input("lossless", "BOOLEAN", widget=True),
            make_input("quality", "INT", widget=True),
            make_input("method", "COMBO", widget=True),
        ],
        outputs=[],
        widgets_values=["storyboard_video_shot1", 16.0, False, 85, "default"],
    ))

    # ============================================================
    # Fix output link lists and input link values
    # ============================================================
    output_links = {}
    for lnk in links:
        lid, src, src_s, tgt, tgt_s, tp = lnk
        key = (src, src_s)
        if key not in output_links:
            output_links[key] = []
        output_links[key].append(lid)

    for node in nodes:
        for out in node["outputs"]:
            key = (node["id"], out["slot_index"])
            out["links"] = output_links.get(key, [])

    input_links = {}
    for lnk in links:
        lid, src, src_s, tgt, tgt_s, tp = lnk
        key = (tgt, tgt_s)
        input_links[key] = lid

    for node in nodes:
        for idx, inp in enumerate(node["inputs"]):
            key = (node["id"], idx)
            if key in input_links:
                inp["link"] = input_links[key]

    groups = [
        {
            "title": "Stage 1: LLM (Text → Script → Prompts)",
            "bounding": [-50, -80, 1600, 1150],
            "color": "#3f789e",
            "font_size": 24,
            "flags": {}
        },
        {
            "title": "Stage 2: FLUX Character Reference",
            "bounding": [1650, -80, 1650, 500],
            "color": "#88A",
            "font_size": 24,
            "flags": {}
        },
        {
            "title": "Stage 3: FLUX Storyboard Reference",
            "bounding": [1650, 420, 1650, 530],
            "color": "#8A8",
            "font_size": 24,
            "flags": {}
        },
        {
            "title": "Stage 4: Wan 2.2 I2V Video (10s)",
            "bounding": [3650, -80, 2000, 600],
            "color": "#A88",
            "font_size": 24,
            "flags": {}
        },
    ]

    workflow = {
        "id": str(uuid.uuid4()),
        "revision": 0,
        "last_node_id": max(n["id"] for n in nodes),
        "last_link_id": link_id,
        "nodes": nodes,
        "links": links,
        "groups": groups,
        "config": {},
        "extra": {
            "info": {
                "name": "Storyboard Video Pipeline",
                "description": "Text → LLM Script → LLM Prompts → FLUX Images → Wan 2.2 Video",
            }
        },
        "version": 0.4,
        "models": [
            {"name": "flux1-dev.safetensors", "url": "https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/flux1-dev.safetensors", "directory": "diffusion_models"},
            {"name": "clip_l.safetensors", "url": "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors", "directory": "text_encoders"},
            {"name": "t5xxl_fp16.safetensors", "url": "https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors", "directory": "text_encoders"},
            {"name": "ae.safetensors", "url": "https://huggingface.co/black-forest-labs/FLUX.1-dev/resolve/main/ae.safetensors", "directory": "vae"},
            {"name": "wan2.2_i2v_480p_14b.safetensors", "url": "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_480p_14b.safetensors", "directory": "diffusion_models"},
            {"name": "umt5_xxl_fp16.safetensors", "url": "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors", "directory": "text_encoders"},
            {"name": "wan_2.1_vae.safetensors", "url": "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors", "directory": "vae"},
            {"name": "clip_vision_h.safetensors", "url": "https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors", "directory": "clip_vision"},
        ],
    }

    return workflow


if __name__ == "__main__":
    wf = build_workflow()
    output_path = "storyboard-video-pipeline.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(wf, f, indent=2, ensure_ascii=False)
    print(f"Workflow saved to {output_path}")
    print(f"Nodes: {len(wf['nodes'])}, Links: {len(wf['links'])}")
