# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 146.2% vs 11-20 109.0%（差 +37.2pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 12-04 70P ΔOI +1,578 占该期限总 OI 14.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 119.88 → 收盘 128.64（+7.3%） ｜ 今日高 132.69 ｜ 低 118.81 ｜ 昨收 154.69 → 收盘 128.64（-16.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 0.54 | OI比 0.54 | ATM IV 146.2% | Skew 2.1pp | Term 0.68 | ExpMove ±6.3%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±6.3% ｜ 11-20（8D）±13.0% ｜ 11-27（15D）±15.4% ｜ 12-04（22D）±20.0%
   ⇒ IV–VIX Spread: +127.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,376,692 | GEX Change vs 上次快照 -2,716,154 | Flip: Primary Flip: 139.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 635 / LOW 109 / INVALID 156
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 139.68（全链重定价，覆盖 99%）
Put Wall 140（弱结构｜现价低于该位 8.1%）
最近结构参考: Flip 140（现价低于该位 7.9%）
量化视角： 负 Gamma（1338万，无历史分位）｜负 Gamma 加深（272万）｜现价位于 Flip 下方 7.90%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 140（Put Wall，弱结构） / 146（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 140（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +38.6k / P +16.2k ｜ Activity HIGH ｜ 1D
11-20  C +9.8k / P +5.3k ｜ Activity HIGH ｜ 8D
11-27  C +3.0k / P +2.7k ｜ Activity HIGH ｜ 15D
12-04  C +0.5k / P +1.6k ｜ Activity HIGH ｜ 22D

📆 11-13 Forward Structure
存量OI: C 121.6k / P 66.2k，今日变化ΔOI: C +38.6k / P +16.2k，平值价格ATM: C $3.70 / P $4.35 ｜ ATM IV 146.2%，净 delta 敞口 -864k shares
仓位参考: Max Pain 146 ｜ Call Wall 140（+8.8%，弱）（OI 5.5k） ｜ Put Wall 130（+1.1%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 146.2%｜历史 Rank 89%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 864,493 股

📆 11-20 Forward Structure
存量OI: C 133.4k / P 114.4k，今日变化ΔOI: C +9.8k / P +5.3k，平值价格ATM: C $7.76 / P $9.00 ｜ ATM IV 109.0%，净 delta 敞口 -56k shares
Top ΔOI: C 165 +1,354 ｜ C 160 +1,086
仓位参考: Max Pain 175 ｜ Call Wall 140（+8.8%，弱）（OI 2.2k） ｜ Put Wall 140（+8.8%，弱）（OI 5.1k）
量化解读： 存量两侧均衡｜ATM IV 109.0%｜历史 Rank 89%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 55,665 股

📆 11-27 Forward Structure
存量OI: C 17.5k / P 19.6k，今日变化ΔOI: C +3.0k / P +2.7k，平值价格ATM: C $9.70 / P $10.15 ｜ ATM IV 100.4%，净 delta 敞口 -17k shares
仓位参考: Max Pain 185 ｜ Put Wall 140（+8.8%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 100.4%｜历史 Rank 89%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 17,297 股

📆 12-04 Forward Structure
存量OI: C 4.5k / P 6.6k，今日变化ΔOI: C +0.5k / P +1.6k，平值价格ATM: C $11.91 / P $13.85 ｜ ATM IV 99.0%，净 delta 敞口 -8k shares
仓位参考: Max Pain 155 ｜ Call Wall 140（+8.8%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 99.0%｜历史 Rank 89%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 负 7,995 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 146.2% vs 11-20 109.0%（差 +37.2pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/NBIS_evening.json