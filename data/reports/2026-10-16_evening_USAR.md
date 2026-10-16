# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
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


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 10.97 → 收盘 10.54（-3.9%） ｜ 今日高 11.22 ｜ 低 10.41 ｜ 昨收 11.09 → 收盘 10.54（-5.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 1.34 | OI比 0.18 | ATM IV 141.6% | Skew 4.5pp | Term 0.60 | ExpMove ±8.2%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价中性（Skew 4.5pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.18）+ 当日成交偏 Put（P/C量 1.34）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.34×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.18×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±8.2% ｜ 10-30（14D）±11.9% ｜ 11-06（21D）±16.1% ｜ 11-13（28D）±18.8%
   ⇒ IV–VIX Spread: +121.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -761,958 | GEX Change vs 上次快照 -4,216,222 | Flip: Primary Flip: 11.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 158 / LOW 79 / INVALID 175
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.29（全链重定价，覆盖 85%）
最近结构参考: Flip 11（现价低于该位 6.6%）
量化视角： 负 Gamma（76万，无历史分位）｜由正转负（422万）｜现价位于 Flip 下方 6.61%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 7D
10-30  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
11-06  C +78 / P -77 ｜ Activity MEDIUM △ ｜ 21D
11-13  C +0.5k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-23 Forward Structure
存量OI: C 16.4k / P 6.1k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $0.43 / P $0.44 ｜ ATM IV 74.5%，净 delta 敞口 36k shares
Top ΔOI: P 17 -196 ｜ P 9 +173 ｜ C 11 +118
仓位参考: Max Pain 12 ｜ Put Wall 9.5（-9.9%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 74.5%｜历史 Rank 76%（近端代理）｜IV/RV 1.34×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 36,092 股

10-30（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 11（+4.4%，弱）（OI 0.2k）

11-06（MEDIUM △）Top ΔOI: 11C +27
11-06（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 10（-5.1%，弱）（OI 0.8k）

11-13（MEDIUM △）Top ΔOI: 11C +64
11-13（MEDIUM △）仓位参考: Max Pain 16 ｜ Call Wall 10.5（-0.4%，弱）（OI 0.2k） ｜ Put Wall 11（+4.4%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/USAR_evening.json