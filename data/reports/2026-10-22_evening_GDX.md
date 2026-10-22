# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 83.85 → 收盘 81.69（-2.6%） ｜ 今日高 83.89 ｜ 低 81.26 ｜ 昨收 86.72 → 收盘 81.69（-5.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.32 | OI比 0.34 | ATM IV 47.9% | Skew -3.4pp | Term 0.90 | ExpMove ±2.4%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.4% ｜ 10-26（4D）±3.1% ｜ 10-28（6D）±4.2% ｜ 10-30（8D）±5.3%
   ⇒ IV–VIX Spread: +28.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -30,300,543 | GEX Change vs 上次快照 -6,135,742 | Flip: Primary Flip: 83.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 535 / LOW 161 / INVALID 452
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 83.71（全链重定价，覆盖 84%）
Put Wall 80（弱结构｜现价高于该位 2.1%）
最近结构参考: Put Wall 80（现价高于该位 2.1%）
量化视角： 负 Gamma（3030万，无历史分位）｜负 Gamma 加深（614万）｜现价位于 Flip 下方 2.42%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 86（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 84（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C -1.8k / P -0.7k ｜ Activity MEDIUM △ ｜ 1D
10-26  C +0.4k / P +81 ｜ Activity HIGH ｜ 4D
10-28  C +0.2k / P +0.2k ｜ Activity HIGH ｜ 6D
10-30  C +0.1k / P +3.2k ｜ Activity HIGH ｜ 8D

📆 10-23 Forward Structure
存量OI: C 95.7k / P 32.8k，今日变化ΔOI: C -1.8k / P -0.7k，平值价格ATM: C $0.80 / P $1.14 ｜ ATM IV 47.9%，净 delta 敞口 37k shares
Top ΔOI: C 87 +1,283
仓位参考: Max Pain 86 ｜ Call Wall 86（+5.3%，弱）（OI 3.5k） ｜ Put Wall 85（+4.1%，弱）（OI 5.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 47.9%｜历史 Rank 77%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,592 股

📆 10-26 Forward Structure
存量OI: C 4.7k / P 1.7k，今日变化ΔOI: C +0.4k / P +81，平值价格ATM: C $1.06 / P $1.48 ｜ ATM IV 37.1%，净 delta 敞口 -4k shares
Top ΔOI: C 89 +144 ｜ C 88 +99
仓位参考: Max Pain 86 ｜ Put Wall 85（+4.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 37.1%｜历史 Rank 77%（近端代理）｜IV/RV 1.19×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 3,718 股

📆 10-28 Forward Structure
存量OI: C 0.9k / P 3.4k，今日变化ΔOI: C +0.2k / P +0.2k，平值价格ATM: C $1.60 / P $1.81 ｜ ATM IV 42.3%，净 delta 敞口 -7k shares
Top ΔOI: P 77 +149 ｜ C 89 +101 ｜ P 85 +49
仓位参考: Max Pain 87 ｜ Put Wall 84（+2.8%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 42.3%｜历史 Rank 77%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 7,358 股

📆 10-30 Forward Structure
存量OI: C 40.1k / P 19.0k，今日变化ΔOI: C +0.1k / P +3.2k，平值价格ATM: C $2.08 / P $2.28 ｜ ATM IV 44.9%，净 delta 敞口 -18k shares
Top ΔOI: P 84 +221
仓位参考: Max Pain 87 ｜ Put Wall 85（+4.1%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.9%｜历史 Rank 77%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 负 17,547 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/GDX_evening.json