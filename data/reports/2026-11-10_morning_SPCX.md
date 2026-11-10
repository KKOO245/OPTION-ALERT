# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.57
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-11 150C ΔOI +3,110（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 150C ΔOI +1,277 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 142.07 → 今开 139.05（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 144.89 ｜ 低 137.65

Options: P/C成交量 0.58 | OI比 0.81 | ATM IV 73.4% | Skew 5.5pp | Term 0.78 | ExpMove ±3.5%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 5.5pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-11（1D）±3.5% ｜ 11-13（3D）±5.2% ｜ 11-16（6D）±6.6% ｜ 11-18（8D）±7.8%
   ⇒ IV–VIX Spread: +53.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 71,934,271 | GEX Change vs 上次快照 39,891,991 | Flip: Primary Flip: 137.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 849 / LOW 155 / INVALID 674
结构观察区: Primary Flip 137.80（全链重定价，覆盖 100%）
Put Wall 130（弱结构｜现价高于该位 11.0%）
最近结构参考: Flip 138（现价高于该位 4.7%）
量化视角： 正 Gamma（7193万，无历史分位）｜正 Gamma 增强（+3989万）｜现价位于 Flip 上方 4.68%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（Put Wall，弱结构） / 138（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 138（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 157.5C — Vol 26,125 | 最新价 $0.40 | OI 2595→26281 (ΔOI +23686张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23686张（+912.8% vs前日OI），连续性待观察（方向未知）
11-13 160.0C — Vol 29,866 | 最新价 $0.27 | OI 9339→27446 (ΔOI +18107张) | ΔOI/Volume 60.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18107张（+193.9% vs前日OI），连续性待观察（方向未知）
11-13 150.0C — Vol 17,573 | 最新价 $1.36 | OI 6486→15800 (ΔOI +9314张) | ΔOI/Volume 53.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9314张（+143.6% vs前日OI），连续性待观察（方向未知）
11-13 50.0P — Vol 6,724 | 最新价 $0.01 | OI 104→6746 (ΔOI +6642张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6642张（+6386.5% vs前日OI），连续性待观察（方向未知）
12-04 140.0P — Vol 5,416 | 最新价 $7.20 | OI 1077→6070 (ΔOI +4993张) | ΔOI/Volume 92.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4993张（+463.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 62,742 张（Put 11,635 / Call 51,107），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-11  C +21.0k / P +17.5k ｜ Activity HIGH ｜ 1D
11-13  C +68.8k / P +22.7k ｜ Activity HIGH ｜ 3D
11-16  C +3.8k / P +1.8k ｜ Activity HIGH ｜ 6D
11-18  C +2.5k / P +0.4k ｜ Activity HIGH ｜ 8D

📆 11-11 Forward Structure
存量OI: C 38.9k / P 31.4k，今日变化ΔOI: C +21.0k / P +17.5k，平值价格ATM: C $2.64 / P $2.40 ｜ ATM IV 73.4%，净 delta 敞口 402k shares
Top ΔOI: C 152 +3,918 ｜ C 150 +3,110 ｜ P 140 +2,816
仓位参考: Max Pain 138 ｜ Call Wall 150（+4.0%，弱）（OI 4.4k） ｜ Put Wall 140（-2.9%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 73.4%｜历史 Rank 86%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 402,449 股

📆 11-13 Forward Structure
存量OI: C 185.1k / P 134.8k，今日变化ΔOI: C +68.8k / P +22.7k，平值价格ATM: C $3.99 / P $3.55 ｜ ATM IV 70.6%，净 delta 敞口 1.0M shares
Top ΔOI: C 157 +23,686 ｜ C 160 +18,107 ｜ C 150 +9,314
仓位参考: Max Pain 140 ｜ Call Wall 157.5（+9.2%，弱）（OI 26.3k） ｜ Put Wall 135（-6.4%，弱）（OI 7.0k）
量化解读： 存量 Call 重｜ATM IV 70.6%｜历史 Rank 86%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,015,417 股

📆 11-16 Forward Structure
存量OI: C 8.9k / P 3.8k，今日变化ΔOI: C +3.8k / P +1.8k，平值价格ATM: C $4.75 / P $4.80 ｜ ATM IV 62.6%，净 delta 敞口 96k shares
Top ΔOI: C 150 +1,277 ｜ C 155 +288
仓位参考: Max Pain 137 ｜ Call Wall 150（+4.0%）（OI 2.3k） ｜ Put Wall 135（-6.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 62.6%｜历史 Rank 86%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 95,902 股

📆 11-18 Forward Structure
存量OI: C 5.2k / P 2.2k，今日变化ΔOI: C +2.5k / P +0.4k，平值价格ATM: C $5.77 / P $5.44 ｜ ATM IV 62.4%，净 delta 敞口 48k shares
Top ΔOI: C 155 +154
仓位参考: Max Pain 130 ｜ Call Wall 145（+0.5%，弱）（OI 0.5k） ｜ Put Wall 130（-9.9%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 62.4%｜历史 Rank 86%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 正 48,143 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SPCX_morning.json