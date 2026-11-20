# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 141.85 → 今开 146.28（+3.1%） | 较昨收变动（含盘初走势） ｜ 今日高 148.59 ｜ 低 144.89

Options: P/C成交量 1.71 | OI比 1.68 | ATM IV 92.6% | Skew 23.4pp | Term 0.57 | ExpMove ±8.8%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价显著（Skew 23.4pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.71×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.68×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±8.8% ｜ 11-27（8D）±7.8% ｜ 12-04（15D）±14.1% ｜ 12-11（22D）±12.6%
   ⇒ IV–VIX Spread: +69.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -41,356,669 | GEX Change vs 上次快照 23,113,724 | Flip: Primary Flip: 152.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 597 / LOW 370 / INVALID 659
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.86（全链重定价，覆盖 96%）
Call Wall 155（弱结构｜现价低于该位 4.5%）
最近结构参考: Flip 153（现价低于该位 3.1%）
量化视角： 负 Gamma（4136万，无历史分位）｜负 Gamma 缓解（+2311万）｜现价位于 Flip 下方 3.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 155（MaxPain，仅结算参考） / 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 110.0P — Vol 5,632 | 最新价 $1.30 | OI 952→6342 (ΔOI +5390张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5390张（+566.2% vs前日OI），连续性待观察（方向未知）
12-18 130.0P — Vol 6,225 | 最新价 $4.76 | OI 5677→10374 (ΔOI +4697张) | ΔOI/Volume 75.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4697张（+82.7% vs前日OI），连续性待观察（方向未知）
11-20 149.0C — Vol 1,158 | 最新价 $0.84 | OI 122→1125 (ΔOI +1003张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1003张（+822.1% vs前日OI），连续性待观察（方向未知）
12-18 150.0C — Vol 2,063 | 最新价 $4.80 | OI 2502→3365 (ΔOI +863张) | ΔOI/Volume 41.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增863张（+34.5% vs前日OI），连续性待观察（方向未知）
12-18 135.0P — Vol 2,469 | 最新价 $6.40 | OI 2781→3360 (ΔOI +579张) | ΔOI/Volume 23.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增579张（+20.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,532 张（Put 10,666 / Call 1,866），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -0.3k / P -17.4k ｜ Activity MEDIUM △ ｜ 1D
11-27  C +0.4k / P -1.2k ｜ Activity MEDIUM △ ｜ 8D
12-04  C -1.2k / P -0.1k ｜ Activity MEDIUM △ ｜ 15D
12-11  C +0.1k / P +75 ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 201.6k / P 339.2k，今日变化ΔOI: C -0.3k / P -17.4k，平值价格ATM: C $3.00 / P $10.00 ｜ ATM IV 92.6%，净 delta 敞口 1.3M shares
Top ΔOI: P 166 -3,307 ｜ P 171 -2,448
仓位参考: Max Pain 155 ｜ Call Wall 155（+4.7%）（OI 18.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 92.6%｜历史 Rank 99%（近端代理）｜IV/RV 0.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,291,733 股

11-27（MEDIUM △）Top ΔOI: 163P -203 ｜ 135P -192
11-27（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 150（+1.3%，弱）（OI 3.5k）

12-04（MEDIUM △）Top ΔOI: 165C -655 ｜ 140P -151
12-04（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 145（-2.1%，弱）（OI 1.2k） ｜ Put Wall 140（-5.5%，弱）（OI 5.1k）

12-11（MEDIUM △）Top ΔOI: 150C +88
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 150（+1.3%，弱）（OI 0.3k） ｜ Put Wall 140（-5.5%）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SOXX_morning.json