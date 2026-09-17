# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.89
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-18 93P ΔOI -5,863（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 90P ΔOI +1,747 占该期限总 OI 21.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 92.80 → 今开 95.85（+3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 96.68 ｜ 低 94.45

Options: P/C成交量 0.11 | OI比 1.25 | ATM IV 52.7% | Skew -0.5pp | Term 0.83 | ExpMove ±2.4%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.25×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.4% ｜ 09-25（8D）±5.4% ｜ 10-02（15D）±7.3% ｜ 10-09（22D）±11.0%
   ⇒ IV–VIX Spread: +36.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,798,852 | GEX Change vs 上次快照 94,011,541 | Flip: Primary Flip: 95.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 523 / LOW 148 / INVALID 239
结构观察区: Primary Flip 95.10（全链重定价，覆盖 95%）
Call Wall 100（弱结构｜现价低于该位 4.2%）
最近结构参考: Flip 95（现价高于该位 0.7%）
量化视角： 正 Gamma（1980万，无历史分位）｜由负转正（+9401万）｜现价位于 Flip 上方 0.73%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 91（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 95（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 99.0C — Vol 5,124 | 最新价 $0.14 | OI 12094→16224 (ΔOI +4130张) | ΔOI/Volume 80.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4130张（+34.1% vs前日OI），连续性待观察（方向未知）
09-25 97.0C — Vol 3,169 | 最新价 $1.21 | OI 100→3219 (ΔOI +3119张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3119张（+3119.0% vs前日OI），连续性待观察（方向未知）
09-25 86.0P — Vol 3,151 | 最新价 $0.83 | OI 562→3639 (ΔOI +3077张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3077张（+547.5% vs前日OI），连续性待观察（方向未知）
09-18 100.0C — Vol 10,443 | 最新价 $0.11 | OI 29597→32235 (ΔOI +2638张) | ΔOI/Volume 25.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2638张（+8.9% vs前日OI），连续性待观察（方向未知）
09-18 95.0C — Vol 8,355 | 最新价 $0.80 | OI 13666→15826 (ΔOI +2160张) | ΔOI/Volume 25.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2160张（+15.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,124 张（Put 3,077 / Call 12,047），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C -0.5k / P -13.6k ｜ Activity MEDIUM △ ｜ 1D
09-25  C +5.1k / P +3.0k ｜ Activity MEDIUM △ ｜ 8D
10-02  C +1.4k / P +1.2k ｜ Activity MEDIUM △ ｜ 15D
10-09  C +0.8k / P +1.7k ｜ Activity HIGH ｜ 22D

📆 09-18 Forward Structure
存量OI: C 341.1k / P 424.7k，今日变化ΔOI: C -0.5k / P -13.6k，平值价格ATM: C $1.06 / P $1.25 ｜ ATM IV 52.7%，净 delta 敞口 708k shares
Top ΔOI: C 101 -11,282 ｜ P 93 -5,863 ｜ C 99 +4,130
仓位参考: Max Pain 91 ｜ Call Wall 100（+4.4%，弱）（OI 32.2k） ｜ Put Wall 90（-6.1%，弱）（OI 40.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 52.7%｜历史 Rank 85%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 708,335 股

09-25（MEDIUM △）Top ΔOI: 97C +3,119 ｜ 86P +3,077
09-25（MEDIUM △）仓位参考: Max Pain 95 ｜ Call Wall 105（+9.6%，弱）（OI 8.1k） ｜ Put Wall 93（-2.9%，弱）（OI 3.9k）

10-02（MEDIUM △）Top ΔOI: 102C +1,075 ｜ 89P +622
10-02（MEDIUM △）仓位参考: Max Pain 99 ｜ Call Wall 100（+4.4%，弱）（OI 3.1k） ｜ Put Wall 97（+1.3%）（OI 11.3k）

📆 10-09 Forward Structure
存量OI: C 3.4k / P 4.9k，今日变化ΔOI: C +0.8k / P +1.7k，平值价格ATM: C $4.38 / P $6.17 ｜ ATM IV 44.4%，净 delta 敞口 4k shares
Top ΔOI: P 90 +1,747 ｜ C 96 +601 ｜ P 100 -65
仓位参考: Max Pain 94 ｜ Call Wall 94（-1.9%，弱）（OI 0.7k） ｜ Put Wall 90（-6.1%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 44.4%｜历史 Rank 85%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 正 3,865 股

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 52.7% vs 09-25 45.2%（差 +7.5pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/GDX_morning.json