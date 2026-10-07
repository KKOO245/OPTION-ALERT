# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.46 ｜ QQQ $754.56
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　⏰ 今日
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **事件差分**: 10-09 ATM IV 47.5% vs 10-16 35.4%（差 +12.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 420C ΔOI +513（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 420C ΔOI +513 占该期限总 OI 11.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 404.76 → 今开 405.23（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 416.81 ｜ 低 404.20

Options: P/C成交量 0.05 | OI比 0.44 | ATM IV 47.5% | Skew 30.7pp | Term 0.95 | ExpMove ±6.3%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构正常（Term 0.95）｜保护溢价显著（Skew 30.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.05×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±6.3% ｜ 10-16（9D）±6.5% ｜ 10-23（16D）±9.6% ｜ 10-30（23D）±9.7%
   ⇒ IV–VIX Spread: +31.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,174,568 | GEX Change vs 上次快照 2,326,226 | Flip: Primary Flip: 393.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 269 / LOW 133 / INVALID 452
结构观察区: Primary Flip 393.79（全链重定价，覆盖 92%）
Call Wall 420（弱结构｜现价低于该位 1.1%）
最近结构参考: Call Wall 420（现价低于该位 1.1%）
量化视角： 正 Gamma（417万，无历史分位）｜正 Gamma 增强（+233万）｜现价位于 Flip 上方 5.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 394（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 420.0C — Vol 541 | 最新价 $1.34 | OI 258→771 (ΔOI +513张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增513张（+198.8% vs前日OI），连续性待观察（方向未知）
10-09 415.0C — Vol 538 | 最新价 $2.12 | OI 88→582 (ΔOI +494张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增494张（+561.4% vs前日OI），连续性待观察（方向未知）
10-23 460.0C — Vol 187 | 最新价 $3.10 | OI 90→224 (ΔOI +134张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增134张（+148.9% vs前日OI），连续性待观察（方向未知）
10-23 445.0C — Vol 61 | 最新价 $5.30 | OI 29→90 (ΔOI +61张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增61张（+210.3% vs前日OI），连续性待观察（方向未知）
10-09 427.5C — Vol 51 | 最新价 $0.60 | OI 0→51 (ΔOI +51张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增51张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,253 张（Put 0 / Call 1,253），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +1.1k / P +19 ｜ Activity HIGH ｜ 2D
10-16  C +69 / P +87 ｜ Activity MEDIUM △ ｜ 9D
10-23  C +0.2k / P +22 ｜ Activity HIGH ｜ 16D
10-30  C +14 / P +95 ｜ Activity MEDIUM △ ｜ 23D

📆 10-09 Forward Structure
存量OI: C 3.0k / P 1.3k，今日变化ΔOI: C +1.1k / P +19，平值价格ATM: C $5.65 / P $20.43 ｜ ATM IV 47.5%，净 delta 敞口 48k shares
Top ΔOI: C 420 +513 ｜ C 415 +494 ｜ C 427 +51
仓位参考: Max Pain 390 ｜ Call Wall 420（+1.1%，弱）（OI 0.8k） ｜ Put Wall 390（-6.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 47.5%｜历史 Rank 82%（近端代理）｜IV/RV 2.02×（近似）｜净 delta 敞口 正 47,939 股

10-16（MEDIUM △）Top ΔOI: 430C +27 ｜ 425C +24
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-3.7%，弱）（OI 0.9k） ｜ Put Wall 380（-8.5%，弱）（OI 0.6k）

📆 10-23 Forward Structure
存量OI: C 1.7k / P 1.4k，今日变化ΔOI: C +0.2k / P +22，平值价格ATM: C $14.30 / P $25.40 ｜ ATM IV 50.9%，净 delta 敞口 5k shares
Top ΔOI: C 445 +61 ｜ C 430 +7
仓位参考: Max Pain 415 ｜ Call Wall 425（+2.3%）（OI 0.5k） ｜ Put Wall 415（-0.1%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 50.9%｜历史 Rank 82%（近端代理）｜IV/RV 2.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,749 股

10-30（MEDIUM △）Top ΔOI: 405P +39 ｜ 400P +16
10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 450（+8.4%，弱）（OI 74） ｜ Put Wall 375（-9.7%，弱）（OI 52）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 47.5% vs 10-16 35.4%（差 +12.1pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/ISRG_morning.json