# -*- coding: utf-8 -*-
"""LLM 深度分析层（可选）：把算好的指标 JSON 交给 OpenAI 模型生成专业中文分析。
失败或未配置 key 时返回 None，主流程自动退回规则版分析。"""

import os

DEFAULT_MODEL = "gpt-5.2"  # 均衡档；可在 GitHub 仓库变量 OPENAI_MODEL 里改

SYSTEM_PROMPT = """你是一名资深美股期权分析师。你只被允许基于用户提供的数据做解读和推理，\
禁止编造任何数字、合约或事件。你的输出是给一位独立投资者的参考分析，分四节，用 Markdown：

## 市场背景
2-4 句，结合提供的指数/VIX 与各标的的整体期权氛围，讲清今天的市场基调。

## 逐标的要点
每个监控标的一段：期权结构说明了什么（持仓倾向、IV 水平、异动、最大痛点、预期波动），\
标的数据与板块/市场的关系。只讲数据支持的结论，拿不准就明确说"数据不足以判断"。

## 风险提示
列出 2-4 条今天的实际风险点（基于 IV 分位、期限结构、偏度、事件日历等，不写空话）。

## 明日关注
给出 2-4 条明天值得盯的具体事项（具体到标的和观察指标）。

要求：全文用简体中文；克制、专业、不夸张；不预测涨跌方向，只描述概率与结构；\
结尾加一行：本分析由 AI 基于公开期权数据生成，仅供研究参考，不构成投资建议。"""


def generate_deep_analysis(payload_json, api_key=None, model=None,
                           temperature=0.3, max_tokens=2500):
    api_key = api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("[提示] 未配置 OPENAI_API_KEY，跳过 AI 深度分析，使用规则版分析。")
        return None
    model = model or os.environ.get("OPENAI_MODEL") or DEFAULT_MODEL
    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)
        resp = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": payload_json},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        content = resp.choices[0].message.content
        return content if content and content.strip() else None
    except Exception as e:
        print(f"[警告] AI 深度分析失败，退回规则版: {type(e).__name__}: {e}")
        return None
