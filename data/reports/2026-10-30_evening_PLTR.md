# 期权晚报 2026-10-30（快照 16:40 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 193.76 → 收盘 184.11（-5.0%） ｜ 今日高 193.92 ｜ 低 183.68 ｜ 昨收 196.42 → 收盘 184.11（-6.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.84 | OI比 1.06 | ATM IV 61.7% | Skew 9.6pp | Term 1.18 | ExpMove ±13.3%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构正常偏陡（Term 1.18）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.06×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（7D）±13.3% ｜ 11-13（14D）±14.6% ｜ 11-20（21D）±15.6% ｜ 11-27（28D）±16.1%
   ⇒ IV–VIX Spread: +42.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,940,414 | GEX Change vs 上次快照 -10,684,100 | Flip: Primary Flip: 189.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 676 / LOW 37 / INVALID 231
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 189.21（全链重定价，覆盖 85%）
Put Wall 180（弱结构｜现价高于该位 2.3%） | Call Wall 200（弱结构｜现价低于该位 7.9%）
最近结构参考: Put Wall 180（现价高于该位 2.3%）
量化视角： 负 Gamma（794万，无历史分位）｜由正转负（1068万）｜现价位于 Flip 下方 2.69%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构）；上方 195（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 189（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +19.1k / P +7.0k ｜ Activity HIGH ｜ 7D
11-13  C +2.1k / P +1.4k ｜ Activity HIGH ｜ 14D
11-20  C +2.2k / P -1.4k ｜ Activity MEDIUM △ ｜ 21D
11-27  C +1.0k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 11-06 Forward Structure
存量OI: C 76.0k / P 63.8k，今日变化ΔOI: C +19.1k / P +7.0k，平值价格ATM: C $11.93 / P $12.60 ｜ ATM IV 119.9%，净 delta 敞口 109k shares
Top ΔOI: C 202 +4,304 ｜ C 212 +3,127
仓位参考: Max Pain 195 ｜ Call Wall 202.5（+10.0%，弱）（OI 5.9k） ｜ Put Wall 190（+3.2%，弱）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 119.9%｜历史 Rank 91%（近端代理）｜IV/RV 2.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 109,079 股

📆 11-13 Forward Structure
存量OI: C 19.3k / P 19.8k，今日变化ΔOI: C +2.1k / P +1.4k，平值价格ATM: C $13.30 / P $13.63 ｜ ATM IV 92.3%，净 delta 敞口 15k shares
Top ΔOI: P 147 +756 ｜ C 242 +593
仓位参考: Max Pain 195 ｜ Call Wall 197.5（+7.3%，弱）（OI 0.7k） ｜ Put Wall 180（-2.2%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 92.3%｜历史 Rank 91%（近端代理）｜IV/RV 2.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,512 股

11-20（MEDIUM △）Top ΔOI: 230C +1,716 ｜ 155P -1,510
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+8.6%，弱）（OI 13.0k） ｜ Put Wall 180（-2.2%，弱）（OI 10.6k）

📆 11-27 Forward Structure
存量OI: C 9.8k / P 10.3k，今日变化ΔOI: C +1.0k / P +0.9k，平值价格ATM: C $14.72 / P $15.00 ｜ ATM IV 73.0%，净 delta 敞口 -21k shares
Top ΔOI: C 220 +491 ｜ P 190 +220
仓位参考: Max Pain 190 ｜ Call Wall 200（+8.6%，弱）（OI 0.5k） ｜ Put Wall 180（-2.2%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.0%｜历史 Rank 91%（近端代理）｜IV/RV 1.63×（近似）｜净 delta 敞口 负 20,618 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/PLTR_evening.json