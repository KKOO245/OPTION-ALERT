# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $735.61 ｜ QQQ $nan
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 165.9% vs 11-27 123.9%（差 +42.0pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 12-04 125C ΔOI +2,913 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 106.04 → 今开 109.79（+3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 110.09 ｜ 低 100.80

Options: P/C成交量 0.26 | OI比 0.55 | ATM IV 165.9% | Skew 13.8pp | Term 0.70 | ExpMove ±10.3%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 13.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±10.3% ｜ 11-27（9D）±15.4% ｜ 12-04（16D）±20.2% ｜ 12-11（23D）±24.1%
   ⇒ IV–VIX Spread: +141.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,371,464 | GEX Change vs 上次快照 3,755,216 | Flip: Primary Flip: 108.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 624 / LOW 76 / INVALID 106
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 108.93（全链重定价，覆盖 100%）
Put Wall 100（弱结构｜现价高于该位 7.4%）
最近结构参考: Flip 109（现价低于该位 1.4%）
量化视角： 负 Gamma（137万，无历史分位）｜负 Gamma 缓解（+376万）｜现价位于 Flip 下方 1.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 125（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 109（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 120.0C — Vol 7,940 | 最新价 $2.23 | OI 5598→9025 (ΔOI +3427张) | ΔOI/Volume 43.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3427张（+61.2% vs前日OI），连续性待观察（方向未知）
12-04 125.0C — Vol 3,085 | 最新价 $4.65 | OI 198→3111 (ΔOI +2913张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2913张（+1471.2% vs前日OI），连续性待观察（方向未知）
12-18 135.0C — Vol 3,574 | 最新价 $5.00 | OI 971→3812 (ΔOI +2841张) | ΔOI/Volume 79.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2841张（+292.6% vs前日OI），连续性待观察（方向未知）
11-20 122.0C — Vol 2,816 | 最新价 $1.85 | OI 1190→3096 (ΔOI +1906张) | ΔOI/Volume 67.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1906张（+160.2% vs前日OI），连续性待观察（方向未知）
11-20 115.0C — Vol 4,979 | 最新价 $3.46 | OI 5233→6627 (ΔOI +1394张) | ΔOI/Volume 28.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1394张（+26.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,481 张（Put 0 / Call 12,481），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +12.8k / P +0.3k ｜ Activity HIGH ｜ 2D
11-27  C +3.3k / P +1.8k ｜ Activity HIGH ｜ 9D
12-04  C +3.8k / P +0.3k ｜ Activity HIGH ｜ 16D
12-11  C +0.7k / P +0.1k ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 200.5k / P 110.4k，今日变化ΔOI: C +12.8k / P +0.3k，平值价格ATM: C $5.72 / P $5.39 ｜ ATM IV 165.9%，净 delta 敞口 532k shares
Top ΔOI: C 120 +3,427 ｜ C 125 -2,437 ｜ C 122 +1,906
仓位参考: Max Pain 125 ｜ Call Wall 115（+7.1%，弱）（OI 6.6k） ｜ Put Wall 115（+7.1%，弱）（OI 9.8k）
量化解读： 存量 Call 重｜ATM IV 165.9%｜历史 Rank 95%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 531,603 股

📆 11-27 Forward Structure
存量OI: C 38.6k / P 20.5k，今日变化ΔOI: C +3.3k / P +1.8k，平值价格ATM: C $8.53 / P $8.00 ｜ ATM IV 123.9%，净 delta 敞口 57k shares
Top ΔOI: C 130 +431 ｜ P 110 +337
仓位参考: Max Pain 130 ｜ Call Wall 110（+2.4%，弱）（OI 1.5k） ｜ Put Wall 100（-6.9%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 123.9%｜历史 Rank 95%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 57,009 股

📆 12-04 Forward Structure
存量OI: C 14.7k / P 8.2k，今日变化ΔOI: C +3.8k / P +0.3k，平值价格ATM: C $10.90 / P $10.85 ｜ ATM IV 119.8%，净 delta 敞口 110k shares
Top ΔOI: C 125 +2,913 ｜ P 95 +161
仓位参考: Max Pain 125 ｜ Put Wall 100（-6.9%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 119.8%｜历史 Rank 95%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 109,806 股

12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 100（-6.9%，弱）（OI 1.3k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 165.9% vs 11-27 123.9%（差 +42.0pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/NBIS_morning.json