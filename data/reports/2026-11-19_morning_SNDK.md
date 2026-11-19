# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $735.18 ｜ QQQ $663.48
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-20 800C ΔOI +1,082（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 776.22 → 今开 811.47（+4.5%） | 较昨收变动（含盘初走势） ｜ 今日高 846.76 ｜ 低 802.20

Options: P/C成交量 0.53 | OI比 0.58 | ATM IV 137.2% | Skew 6.1pp | Term 0.69 | ExpMove ±6.5%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 6.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±6.5% ｜ 11-27（8D）±11.9% ｜ 12-04（15D）±15.6% ｜ 12-11（22D）±19.6%
   ⇒ IV–VIX Spread: +114.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -83,518 | GEX Change vs 上次快照 4,726,922 | Flip: Primary Flip: 830.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1691 / LOW 784 / INVALID 1057
结构观察区: Primary Flip 830.47（全链重定价，覆盖 100%）
最近结构参考: Flip 830（现价低于该位 0.1%）
量化视角： 负 Gamma（8万，无历史分位）｜负 Gamma 缓解（+473万）｜现价位于 Flip 下方 0.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 870（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 830（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 800.0C — Vol 2,627 | 最新价 $41.17 | OI 238→2121 (ΔOI +1883张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1883张（+791.2% vs前日OI），连续性待观察（方向未知）
11-20 800.0C — Vol 5,317 | 最新价 $21.25 | OI 1821→2903 (ΔOI +1082张) | ΔOI/Volume 20.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1082张（+59.4% vs前日OI），连续性待观察（方向未知）
11-20 850.0C — Vol 3,644 | 最新价 $7.86 | OI 1455→2258 (ΔOI +803张) | ΔOI/Volume 22.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增803张（+55.2% vs前日OI），连续性待观察（方向未知）
11-20 900.0C — Vol 3,379 | 最新价 $2.45 | OI 1667→2187 (ΔOI +520张) | ΔOI/Volume 15.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增520张（+31.2% vs前日OI），连续性待观察（方向未知）
11-20 695.0P — Vol 508 | 最新价 $8.50 | OI 112→560 (ΔOI +448张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增448张（+400.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,736 张（Put 448 / Call 4,288），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +2.6k / P -1.0k ｜ Activity MEDIUM △ ｜ 1D
11-27  C +4.3k / P +0.4k ｜ Activity HIGH ｜ 8D
12-04  C +1.6k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
12-11  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 102.8k / P 59.9k，今日变化ΔOI: C +2.6k / P -1.0k，平值价格ATM: C $28.78 / P $24.90 ｜ ATM IV 137.2%，净 delta 敞口 733k shares
Top ΔOI: C 1000 -1,553 ｜ C 800 +1,082 ｜ P 1100 -820
仓位参考: Max Pain 870 ｜ Call Wall 800（-3.5%，弱）（OI 2.9k） ｜ Put Wall 870（+4.9%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 137.2%｜历史 Rank 87%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 733,027 股

📆 11-27 Forward Structure
存量OI: C 27.9k / P 13.7k，今日变化ΔOI: C +4.3k / P +0.4k，平值价格ATM: C $51.41 / P $47.00 ｜ ATM IV 98.7%，净 delta 敞口 286k shares
Top ΔOI: C 800 +1,883 ｜ C 825 +303 ｜ P 850 +239
仓位参考: Max Pain 850 ｜ Call Wall 800（-3.5%，弱）（OI 2.1k） ｜ Put Wall 800（-3.5%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 98.7%｜历史 Rank 87%（近端代理）｜IV/RV 0.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 286,038 股

12-04（MEDIUM △）Top ΔOI: 800C +232
12-04（MEDIUM △）仓位参考: Max Pain 880 ｜ Call Wall 800（-3.5%，弱）（OI 0.3k） ｜ Put Wall 820（-1.1%，弱）（OI 0.4k）

12-11（MEDIUM △）Top ΔOI: 780C +90 ｜ 770P +76
12-11（MEDIUM △）仓位参考: Max Pain 870 ｜ Call Wall 780（-5.9%，弱）（OI 97） ｜ Put Wall 830（+0.1%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SNDK_morning.json