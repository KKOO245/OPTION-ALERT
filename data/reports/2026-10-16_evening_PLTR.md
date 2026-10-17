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


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 202.36 → 收盘 186.03（-8.1%） ｜ 今日高 203.55 ｜ 低 184.45 ｜ 昨收 200.50 → 收盘 186.03（-7.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 0.71 | OI比 1.40 | ATM IV 49.9% | Skew 4.9pp | Term 1.32 | ExpMove ±5.4%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常偏陡（Term 1.32）｜保护溢价中性（Skew 4.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±5.4% ｜ 10-30（14D）±7.8% ｜ 11-06（21D）±13.7% ｜ 11-13（28D）±14.3%
   ⇒ IV–VIX Spread: +29.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,418,819 | GEX Change vs 上次快照 -22,399,266 | Flip: Primary Flip: 187.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 541 / LOW 49 / INVALID 164
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 187.34（全链重定价，覆盖 100%）
最近结构参考: Flip 187（现价低于该位 0.7%）
量化视角： 负 Gamma（142万，无历史分位）｜由正转负（2240万）｜现价位于 Flip 下方 0.70%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 195（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 187（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 10-23 Forward Structure
存量OI: C 50.4k / P 70.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.60 / P $4.40 ｜ ATM IV 49.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 195 ｜ Call Wall 180（-3.2%，弱）（OI 4.7k） ｜ Put Wall 190（+2.1%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 49.9%｜历史 Rank 58%（近端代理）｜IV/RV 1.70×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 192 ｜ Call Wall 200（+7.5%，弱）（OI 3.0k） ｜ Put Wall 190（+2.1%，弱）（OI 4.3k）

11-06（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 200（+7.5%，弱）（OI 1.1k） ｜ Put Wall 190（+2.1%）（OI 3.0k）

11-13（Activity LOW）仓位参考: Max Pain 195 ｜ Call Wall 200（+7.5%，弱）（OI 0.4k） ｜ Put Wall 180（-3.2%，弱）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/PLTR_evening.json