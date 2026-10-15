# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 52.4% vs 10-19 34.3%（差 +18.1pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 90C ΔOI -8,739（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 87C ΔOI +597 占该期限总 OI 17.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 84.78 → 收盘 87.02（+2.6%） ｜ 今日高 87.12 ｜ 低 84.12 ｜ 昨收 83.40 → 收盘 87.02（+4.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-22，窗口结束前不做对错判定）

Options: P/C成交量 1.51 | OI比 0.67 | ATM IV 52.4% | Skew 5.0pp | Term 0.78 | ExpMove ±2.2%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 5.0pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.67）+ 当日成交偏 Put（P/C量 1.51）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.51×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.2% ｜ 10-19（4D）±3.1% ｜ 10-21（6D）±3.5% ｜ 10-23（8D）±4.4%
   ⇒ IV–VIX Spread: +35.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,562,223 | GEX Change vs 上次快照 37,140,704 | Flip: Primary Flip: 87.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 553 / LOW 185 / INVALID 438
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 87.52（全链重定价，覆盖 88%）
最近结构参考: Flip 88（现价低于该位 0.6%）
量化视角： 负 Gamma（1356万，无历史分位）｜负 Gamma 缓解（+3714万）｜现价位于 Flip 下方 0.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 88（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 88（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C -19.9k / P -13.1k ｜ Activity HIGH ｜ 1D
10-19  C +0.9k / P +0.1k ｜ Activity HIGH ｜ 4D
10-21  C +0.3k / P +1.3k ｜ Activity HIGH ｜ 6D
10-23  C +4.4k / P +4.1k ｜ Activity HIGH ｜ 8D

📆 10-16 Forward Structure
存量OI: C 172.3k / P 115.2k，今日变化ΔOI: C -19.9k / P -13.1k，平值价格ATM: C $0.94 / P $0.95 ｜ ATM IV 52.4%，净 delta 敞口 1.2M shares
Top ΔOI: C 93 -8,771 ｜ C 90 -8,739 ｜ P 95 -5,099
仓位参考: Max Pain 88 ｜ Call Wall 90.5（+4.0%，弱）（OI 12.8k） ｜ Put Wall 85（-2.3%，弱）（OI 10.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.4%｜历史 Rank 86%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,200,841 股

📆 10-19 Forward Structure
存量OI: C 2.7k / P 0.8k，今日变化ΔOI: C +0.9k / P +0.1k，平值价格ATM: C $1.37 / P $1.32 ｜ ATM IV 34.3%，净 delta 敞口 48k shares
Top ΔOI: C 87 +597 ｜ C 89 +214 ｜ C 85 +129
仓位参考: Max Pain 87 ｜ Call Wall 90（+3.4%，弱）（OI 0.8k） ｜ Put Wall 89（+2.3%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 34.3%｜历史 Rank 86%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 47,933 股

📆 10-21 Forward Structure
存量OI: C 2.9k / P 3.8k，今日变化ΔOI: C +0.3k / P +1.3k，平值价格ATM: C $1.18 / P $1.85 ｜ ATM IV 37.9%，净 delta 敞口 8k shares
Top ΔOI: P 80 +1,112 ｜ C 87 +212
仓位参考: Max Pain 83
量化解读： 存量 Put 重｜ATM IV 37.9%｜历史 Rank 86%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 7,925 股

📆 10-23 Forward Structure
存量OI: C 15.4k / P 18.0k，今日变化ΔOI: C +4.4k / P +4.1k，平值价格ATM: C $1.80 / P $2.04 ｜ ATM IV 38.6%，净 delta 敞口 288k shares
Top ΔOI: C 86 +3,163 ｜ P 81 +565
仓位参考: Max Pain 86 ｜ Call Wall 86（-1.2%）（OI 3.3k） ｜ Put Wall 85（-2.3%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 288,159 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 52.4% vs 10-19 34.3%（差 +18.1pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/GDX_evening.json