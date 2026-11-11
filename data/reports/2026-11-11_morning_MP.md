# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.90 ｜ QQQ $690.38
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 36.46 → 今开 37.20（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 38.05 ｜ 低 36.88

Options: P/C成交量 0.65 | OI比 0.35 | ATM IV 84.2% | Skew 12.7pp | Term 0.76 | ExpMove ±5.3%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 12.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±5.3% ｜ 11-20（9D）±9.9% ｜ 11-27（16D）±13.0% ｜ 12-04（23D）±20.4%
   ⇒ IV–VIX Spread: +65.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,363,636 | GEX Change vs 上次快照 2,345,906 | Flip: Primary Flip: 35.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 314 / LOW 82 / INVALID 96
结构观察区: Primary Flip 35.45（全链重定价，覆盖 99%）
Put Wall 35（现价高于该位 7.5%）
最近结构参考: Flip 35（现价高于该位 6.1%）
量化视角： 正 Gamma（436万，无历史分位）｜正 Gamma 增强（+235万）｜现价位于 Flip 上方 6.11%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall） / 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 38.0C — Vol 397 | 最新价 $0.45 | OI 773→993 (ΔOI +220张) | ΔOI/Volume 55.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增220张（+28.5% vs前日OI），连续性待观察（方向未知）
11-13 39.0C — Vol 187 | 最新价 $0.30 | OI 771→919 (ΔOI +148张) | ΔOI/Volume 79.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增148张（+19.2% vs前日OI），连续性待观察（方向未知）
11-13 41.0C — Vol 191 | 最新价 $0.07 | OI 544→676 (ΔOI +132张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增132张（+24.3% vs前日OI），连续性待观察（方向未知）
11-13 35.0P — Vol 137 | 最新价 $0.52 | OI 479→606 (ΔOI +127张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+26.5% vs前日OI），连续性待观察（方向未知）
11-13 39.5C — Vol 135 | 最新价 $0.13 | OI 186→308 (ΔOI +122张) | ΔOI/Volume 90.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增122张（+65.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 749 张（Put 127 / Call 622），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.7k / P +0.2k ｜ Activity MEDIUM △ ｜ 2D
11-20  C +97 / P -0.6k ｜ Activity MEDIUM △ ｜ 9D
11-27  C +39 / P +50 ｜ Activity MEDIUM △ ｜ 16D
12-04  C +0.1k / P +40 ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 14.5k / P 5.1k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $1.02 / P $0.97 ｜ ATM IV 84.2%，净 delta 敞口 35k shares
Top ΔOI: C 38 +220 ｜ C 39 +148 ｜ C 41 +132
仓位参考: Max Pain 37 ｜ Call Wall 40（+6.3%，弱）（OI 2.1k） ｜ Put Wall 34（-9.6%）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 84.2%｜历史 Rank 78%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,178 股

11-20（MEDIUM △）Top ΔOI: 50P -287 ｜ 55P -265
11-20（MEDIUM △）仓位参考: Max Pain 40 ｜ Call Wall 39.5（+5.0%，弱）（OI 1.5k） ｜ Put Wall 35（-7.0%）（OI 3.8k）

11-27（MEDIUM △）Top ΔOI: 39C +19
11-27（MEDIUM △）仓位参考: Max Pain 42 ｜ Put Wall 38（+1.0%，弱）（OI 82）

12-04（MEDIUM △）仓位参考: Max Pain 35 ｜ Call Wall 35（-7.0%）（OI 0.5k） ｜ Put Wall 34（-9.6%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 84.2% vs 11-20 74.6%（差 +9.7pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/MP_morning.json