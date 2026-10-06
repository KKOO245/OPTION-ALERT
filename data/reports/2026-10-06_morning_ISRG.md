# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.74 ｜ QQQ $760.83
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 406.48 → 今开 406.13（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 409.29 ｜ 低 402.00

Options: P/C成交量 0.57 | OI比 0.69 | ATM IV 38.1% | Skew 10.5pp | Term 1.15 | ExpMove ±4.1%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 1.15）｜保护溢价显著（Skew 10.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.1% ｜ 10-16（10D）±4.1% ｜ 10-23（17D）±7.0% ｜ 10-30（24D）±10.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,587,654 | GEX Change vs 上次快照 -138,977 | Flip: Primary Flip: 393.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 305 / LOW 125 / INVALID 406
结构观察区: Primary Flip 393.86（全链重定价，覆盖 94%）
Call Wall 400（弱结构｜现价高于该位 1.3%）
最近结构参考: Call Wall 400（现价高于该位 1.3%）
量化视角： 正 Gamma（159万，无历史分位）｜正 Gamma 减弱（14万）｜现价位于 Flip 上方 2.91%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 394（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 420.0C — Vol 98 | 最新价 $2.00 | OI 171→258 (ΔOI +87张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增87张（+50.9% vs前日OI），连续性待观察（方向未知）
10-09 410.0C — Vol 116 | 最新价 $5.10 | OI 111→184 (ΔOI +73张) | ΔOI/Volume 62.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增73张（+65.8% vs前日OI），连续性待观察（方向未知）
10-16 425.0C — Vol 63 | 最新价 $3.20 | OI 222→261 (ΔOI +39张) | ΔOI/Volume 61.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增39张（+17.6% vs前日OI），值得跟踪（方向未知）
10-09 430.0C — Vol 53 | 最新价 $0.60 | OI 132→160 (ΔOI +28张) | ΔOI/Volume 52.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28张（+21.2% vs前日OI），连续性待观察（方向未知）
10-09 425.0C — Vol 36 | 最新价 $1.15 | OI 125→149 (ΔOI +24张) | ΔOI/Volume 66.7% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增24张（+19.2% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 251 张（Put 0 / Call 251），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.4k / P +79 ｜ Activity MEDIUM △ ｜ 3D
10-16  C +0.1k / P -56 ｜ Activity LOW ｜ 10D
10-23  C +52 / P +10 ｜ Activity LOW ｜ 17D
10-30  C +53 / P +7 ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 1.9k / P 1.3k，今日变化ΔOI: C +0.4k / P +79，平值价格ATM: C $11.00 / P $5.60 ｜ ATM IV 38.1%，净 delta 敞口 9k shares
Top ΔOI: C 420 +87 ｜ C 410 +73 ｜ C 430 +28
仓位参考: Max Pain 390 ｜ Call Wall 420（+3.6%，弱）（OI 0.3k） ｜ Put Wall 370（-8.7%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 38.1%｜历史 Rank 36%（近端代理）｜IV/RV 1.56×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 9,483 股

10-16（Activity LOW）仓位参考: Max Pain 390 ｜ Call Wall 400（-1.3%，弱）（OI 0.9k） ｜ Put Wall 380（-6.2%，弱）（OI 0.6k）

10-23（Activity LOW）仓位参考: Max Pain 415 ｜ Call Wall 425（+4.9%）（OI 0.5k） ｜ Put Wall 415（+2.4%）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 385C +9
10-30（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 375（-7.5%，弱）（OI 59） ｜ Put Wall 375（-7.5%，弱）（OI 52）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 38.1% vs 10-16 32.7%（差 +5.5pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/ISRG_morning.json