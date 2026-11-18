# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $659.51
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
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
🔴 **事件差分**: 11-20（2D）ATM IV 152.3% vs 11-27 116.2%（差 +36.1pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-27 110P ΔOI +337（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 125C ΔOI +2,913 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 109.79 → 收盘 106.96（-2.6%） ｜ 今日高 110.09 ｜ 低 100.80 ｜ 昨收 106.04 → 收盘 106.96（+0.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.39 | OI比 0.55 | ATM IV 152.3% | Skew 9.8pp | Term 0.73 | ExpMove ±9.3%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 9.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±9.3% ｜ 11-27（9D）±14.4% ｜ 12-04（16D）±19.4% ｜ 12-11（23D）±22.9%
   ⇒ IV–VIX Spread: +127.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -863,050 | GEX Change vs 上次快照 508,414 | Flip: Primary Flip: 107.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 538 / LOW 99 / INVALID 169
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 107.75（全链重定价，覆盖 100%）
Put Wall 100（弱结构｜现价高于该位 7.0%）
最近结构参考: Flip 108（现价低于该位 0.7%）
量化视角： 负 Gamma（86万，无历史分位）｜负 Gamma 缓解（+51万）｜现价位于 Flip 下方 0.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 125（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 108（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +12.8k / P +0.3k ｜ Activity HIGH ｜ 2D
11-27  C +3.3k / P +1.8k ｜ Activity HIGH ｜ 9D
12-04  C +3.8k / P +0.3k ｜ Activity HIGH ｜ 16D
12-11  C +0.7k / P +0.1k ｜ Activity HIGH ｜ 23D

📆 11-20 Forward Structure
存量OI: C 200.5k / P 110.4k，今日变化ΔOI: C +12.8k / P +0.3k，平值价格ATM: C $4.99 / P $4.95 ｜ ATM IV 152.3%，净 delta 敞口 497k shares
Top ΔOI: C 120 +3,427 ｜ C 125 -2,437 ｜ C 122 +1,906
仓位参考: Max Pain 125 ｜ Call Wall 115（+7.5%，弱）（OI 6.6k） ｜ Put Wall 115（+7.5%，弱）（OI 9.8k）
量化解读： 存量 Call 重｜ATM IV 152.3%｜历史 Rank 91%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 496,779 股

📆 11-27 Forward Structure
存量OI: C 38.6k / P 20.5k，今日变化ΔOI: C +3.3k / P +1.8k，平值价格ATM: C $7.77 / P $7.65 ｜ ATM IV 116.2%，净 delta 敞口 54k shares
Top ΔOI: C 130 +431 ｜ P 110 +337
仓位参考: Max Pain 130 ｜ Call Wall 110（+2.8%，弱）（OI 1.5k） ｜ Put Wall 100（-6.5%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 116.2%｜历史 Rank 91%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 54,074 股

📆 12-04 Forward Structure
存量OI: C 14.7k / P 8.2k，今日变化ΔOI: C +3.8k / P +0.3k，平值价格ATM: C $10.50 / P $10.30 ｜ ATM IV 110.8%，净 delta 敞口 104k shares
Top ΔOI: C 125 +2,913 ｜ P 95 +161
仓位参考: Max Pain 125 ｜ Put Wall 100（-6.5%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 110.8%｜历史 Rank 91%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 正 103,730 股

📆 12-11 Forward Structure
存量OI: C 6.3k / P 8.3k，今日变化ΔOI: C +0.7k / P +0.1k，平值价格ATM: C $13.59 / P $10.93 ｜ ATM IV 113.6%，净 delta 敞口 5k shares
仓位参考: Max Pain 135 ｜ Put Wall 100（-6.5%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 113.6%｜历史 Rank 91%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 4,735 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 152.3% vs 11-27 116.2%（差 +36.1pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/NBIS_evening.json