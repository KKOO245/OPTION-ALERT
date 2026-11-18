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
🟡 **事件差分**: 11-20 ATM IV 55.2% vs 11-23 44.9%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-23 72P ΔOI +605（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-23 72P ΔOI +605 占该期限总 OI 28.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 76.81 → 收盘 74.82（-2.6%） ｜ 今日高 76.82 ｜ 低 73.32 ｜ 昨收 79.57 → 收盘 74.82（-6.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.51 | OI比 0.96 | ATM IV 72.8% | Skew 2.3pp | Term 0.64 | ExpMove ±3.3%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价中性（Skew 2.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（2D）±3.3% ｜ 11-23（5D）±4.3% ｜ 11-25（7D）±5.4% ｜ 11-27（9D）±6.3%
   ⇒ IV–VIX Spread: +48.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -80,735,000 | GEX Change vs 上次快照 -11,854,269 | Flip: Primary Flip: 80.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 544 / LOW 248 / INVALID 498
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 80.93（全链重定价，覆盖 91%）
Put Wall 75（弱结构｜现价低于该位 0.2%）
最近结构参考: Put Wall 75（现价低于该位 0.2%）
量化视角： 负 Gamma（8073万，无历史分位）｜负 Gamma 加深（1185万）｜现价位于 Flip 下方 7.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 75（Put Wall，弱结构） / 80（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 81（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +6.8k / P -1.4k ｜ Activity MEDIUM △ ｜ 2D
11-23  C +0.4k / P +0.7k ｜ Activity HIGH ｜ 5D
11-25  C +0.3k / P +26 ｜ Activity HIGH ｜ 7D
11-27  C +1.9k / P +0.2k ｜ Activity HIGH ｜ 9D

📆 11-20 Forward Structure
存量OI: C 176.9k / P 180.2k，今日变化ΔOI: C +6.8k / P -1.4k，平值价格ATM: C $1.26 / P $1.24 ｜ ATM IV 55.2%，净 delta 敞口 261k shares
Top ΔOI: C 81 +4,769 ｜ P 70 +901 ｜ P 79 -610
仓位参考: Max Pain 84 ｜ Put Wall 70（-6.4%，弱）（OI 26.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 55.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 260,965 股

📆 11-23 Forward Structure
存量OI: C 0.9k / P 1.2k，今日变化ΔOI: C +0.4k / P +0.7k，平值价格ATM: C $1.56 / P $1.68 ｜ ATM IV 44.9%，净 delta 敞口 -16k shares
Top ΔOI: P 72 +605
仓位参考: Max Pain 83 ｜ Put Wall 72（-3.8%）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 44.9%｜历史 Rank 98%（近端代理）｜IV/RV 0.83×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 16,388 股

📆 11-25 Forward Structure
存量OI: C 0.7k / P 0.5k，今日变化ΔOI: C +0.3k / P +26，平值价格ATM: C $2.08 / P $1.98 ｜ ATM IV 49.1%，净 delta 敞口 921 shares
Top ΔOI: C 82 +134
仓位参考: Max Pain 83 ｜ Put Wall 78（+4.3%，弱）（OI 81）
量化解读： 存量 Call 重｜ATM IV 49.1%｜历史 Rank 98%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 921 股

📆 11-27 Forward Structure
存量OI: C 13.9k / P 7.6k，今日变化ΔOI: C +1.9k / P +0.2k，平值价格ATM: C $2.31 / P $2.37 ｜ ATM IV 47.6%，净 delta 敞口 -587 shares
仓位参考: Max Pain 83 ｜ Put Wall 70（-6.4%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 47.6%｜历史 Rank 98%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 负 587 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 55.2% vs 11-23 44.9%（差 +10.3pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/GDX_evening.json