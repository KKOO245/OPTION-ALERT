# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🔴 **事件差分**: 10-21（2D）ATM IV 116.5% vs 10-23 93.7%（差 +22.8pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-21 155C ΔOI +3,200（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 148P ΔOI +998 占该期限总 OI 11.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 146.03 → 今开 149.25（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 150.44 ｜ 低 147.31

Options: P/C成交量 0.41 | OI比 1.24 | ATM IV 70.9% | Skew 3.7pp | Term 0.81 | ExpMove ±7.4%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-21（2D）±7.4% ｜ 10-23（4D）±8.2% ｜ 10-26（7D）±8.7% ｜ 10-28（9D）±9.5%
   ⇒ IV–VIX Spread: +52.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -18,516,691 | GEX Change vs 上次快照 5,629,845 | Flip: Primary Flip: 149.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 834 / LOW 83 / INVALID 455
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 149.88（全链重定价，覆盖 98%）
Put Wall 140（弱结构｜现价高于该位 5.5%）
最近结构参考: Flip 150（现价低于该位 1.5%）
量化视角： 负 Gamma（1852万，无历史分位）｜负 Gamma 缓解（+563万）｜现价位于 Flip 下方 1.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-19 120.0P — Vol 10,613 | 最新价 $0.03 | OI 155→10370 (ΔOI +10215张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10215张（+6590.3% vs前日OI），连续性待观察（方向未知）
10-19 140.0P — Vol 18,447 | 最新价 $0.50 | OI 1677→11541 (ΔOI +9864张) | ΔOI/Volume 53.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9864张（+588.2% vs前日OI），连续性待观察（方向未知）
10-23 146.0C — Vol 10,069 | 最新价 $6.43 | OI 634→7701 (ΔOI +7067张) | ΔOI/Volume 70.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7067张（+1114.7% vs前日OI），连续性待观察（方向未知）
10-23 80.0P — Vol 11,107 | 最新价 $0.05 | OI 89→6594 (ΔOI +6505张) | ΔOI/Volume 58.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6505张（+7309.0% vs前日OI），连续性待观察（方向未知）
10-19 144.0P — Vol 18,113 | 最新价 $1.34 | OI 716→6734 (ΔOI +6018张) | ΔOI/Volume 33.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6018张（+840.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 39,669 张（Put 32,602 / Call 7,067），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 63.0k / P 78.3k，今日成交量: C 56.0k / P 23.1k，平值价格ATM: C $1.24 / P $1.04 ｜ ATM IV 70.9%，预期波动 ±1.5%，Max Pain 148
Top ΔOI: P 120 +10,215 ｜ P 140 +9,864 ｜ P 144 +6,018

📆 Forward Expiration Structure

10-21  C +10.2k / P +19.8k ｜ Activity HIGH ｜ 2D
10-23  C +27.1k / P +38.8k ｜ Activity HIGH ｜ 4D
10-26  C +1.9k / P +0.9k ｜ Activity HIGH ｜ 7D
10-28  C +0.9k / P +1.8k ｜ Activity HIGH ｜ 9D

📆 10-21 Forward Structure
存量OI: C 30.9k / P 30.8k，今日变化ΔOI: C +10.2k / P +19.8k，平值价格ATM: C $5.53 / P $5.34 ｜ ATM IV 116.5%，净 delta 敞口 -132k shares
Top ΔOI: P 135 +4,375 ｜ P 140 +3,680 ｜ C 155 +3,200
仓位参考: Max Pain 149 ｜ Call Wall 155（+5.0%）（OI 4.2k） ｜ Put Wall 135（-8.6%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 116.5%｜历史 Rank 90%（近端代理）｜IV/RV 2.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 131,584 股

📆 10-23 Forward Structure
存量OI: C 107.2k / P 129.8k，今日变化ΔOI: C +27.1k / P +38.8k，平值价格ATM: C $6.10 / P $6.00 ｜ ATM IV 93.7%，净 delta 敞口 406k shares
Top ΔOI: C 146 +7,067 ｜ P 135 +4,906
仓位参考: Max Pain 150 ｜ Call Wall 155（+5.0%，弱）（OI 8.0k） ｜ Put Wall 140（-5.2%，弱）（OI 11.2k）
量化解读： 存量 Put 重｜ATM IV 93.7%｜历史 Rank 90%（近端代理）｜IV/RV 1.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 405,748 股

📆 10-26 Forward Structure
存量OI: C 6.1k / P 3.6k，今日变化ΔOI: C +1.9k / P +0.9k，平值价格ATM: C $6.52 / P $6.35 ｜ ATM IV 75.0%，净 delta 敞口 34k shares
Top ΔOI: C 147 +463
仓位参考: Max Pain 150 ｜ Call Wall 155（+5.0%，弱）（OI 0.8k） ｜ Put Wall 144（-2.5%）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 75.0%｜历史 Rank 90%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,770 股

📆 10-28 Forward Structure
存量OI: C 2.3k / P 6.3k，今日变化ΔOI: C +0.9k / P +1.8k，平值价格ATM: C $5.30 / P $8.75 ｜ ATM IV 74.8%，净 delta 敞口 -39k shares
Top ΔOI: P 148 +998 ｜ P 142 +304
仓位参考: Max Pain 150 ｜ Call Wall 160（+8.3%，弱）（OI 0.4k） ｜ Put Wall 148（+0.2%）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 74.8%｜历史 Rank 90%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 负 39,383 股

📅 事件差分（观察，非因果）: 10-21（2D）ATM IV 116.5% vs 10-23 93.7%（差 +22.8pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SPCX_morning.json