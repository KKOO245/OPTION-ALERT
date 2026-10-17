# 期权晚报 2026-10-16（快照 21:00 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 369.04 → 收盘 354.72（-3.9%） ｜ 今日高 370.50 ｜ 低 349.33 ｜ 昨收 362.44 → 收盘 354.72（-2.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 0.53 | OI比 0.49 | ATM IV 34.1% | Skew 0.9pp | Term 1.41 | ExpMove ±2.5%（近端） | Rank 6%
量化视角： IV 历史低位（Rank 6%，期权偏便宜）｜期限结构正常偏陡（Term 1.41）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.5% ｜ 10-23（7D）±7.4% ｜ 10-26（10D）±7.8% ｜ 10-28（12D）±8.7%
   ⇒ IV–VIX Spread: +14.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,294,972 | GEX Change vs 上次快照 -57,140,814 | Flip: Primary Flip: 356.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1116 / LOW 46 / INVALID 378
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 356.37（全链重定价，覆盖 100%）
最近结构参考: Flip 356（现价低于该位 0.5%）
量化视角： 负 Gamma（429万，无历史分位）｜由正转负（5714万）｜现价位于 Flip 下方 0.46%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 365（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 356（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-26  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-28  C +0 / P +0 ｜ Activity LOW ｜ 12D

📆 10-19 Forward Structure
存量OI: C 73.3k / P 35.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.20 / P $4.53 ｜ ATM IV 34.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 365 ｜ Call Wall 390（+9.9%，弱）（OI 4.7k） ｜ Put Wall 360（+1.5%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 34.1%｜历史 Rank 6%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 370 ｜ Call Wall 390（+9.9%，弱）（OI 6.3k） ｜ Put Wall 350（-1.3%，弱）（OI 3.6k）

10-26（Activity LOW）仓位参考: Max Pain 368 ｜ Call Wall 380（+7.1%，弱）（OI 0.4k） ｜ Put Wall 347.5（-2.0%，弱）（OI 0.8k）

10-28（Activity LOW）仓位参考: Max Pain 365 ｜ Call Wall 357.5（+0.8%，弱）（OI 0.2k） ｜ Put Wall 375（+5.7%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/TSLA_evening.json