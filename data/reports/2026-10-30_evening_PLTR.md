# 期权晚报 2026-10-30（快照 21:00 ET）

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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 193.76 → 收盘 184.11（-5.0%） ｜ 今日高 193.92 ｜ 低 183.68 ｜ 昨收 196.42 → 收盘 184.11（-6.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-06，窗口结束前不做对错判定）

Options: P/C成交量 0.93 | OI比 0.84 | ATM IV 119.9% | Skew 11.2pp | Term 0.61 | ExpMove ±13.3%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 11.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（7D）±13.3% ｜ 11-13（14D）±14.6% ｜ 11-20（21D）±15.6% ｜ 11-27（28D）±16.1%
   ⇒ IV–VIX Spread: +100.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,007,793 | GEX Change vs 上次快照 1,264,108 | Flip: Primary Flip: 178.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 663 / LOW 11 / INVALID 108
结构观察区: Primary Flip 178.98（全链重定价，覆盖 100%）
Put Wall 180（弱结构｜现价高于该位 2.3%） | Call Wall 200（弱结构｜现价低于该位 7.9%）
最近结构参考: Put Wall 180（现价高于该位 2.3%）
量化视角： 正 Gamma（401万，无历史分位）｜正 Gamma 增强（+126万）｜现价位于 Flip 上方 2.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构）；上方 195（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 179（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 11-06 Forward Structure
存量OI: C 76.0k / P 63.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $11.93 / P $12.60 ｜ ATM IV 119.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 195 ｜ Call Wall 202.5（+10.0%，弱）（OI 5.9k） ｜ Put Wall 190（+3.2%，弱）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 119.9%｜历史 Rank 100%（近端代理）｜IV/RV 2.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 195 ｜ Call Wall 197.5（+7.3%，弱）（OI 0.7k） ｜ Put Wall 180（-2.2%，弱）（OI 1.9k）

11-20（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 200（+8.6%，弱）（OI 13.0k） ｜ Put Wall 180（-2.2%，弱）（OI 10.6k）

11-27（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 200（+8.6%，弱）（OI 0.5k） ｜ Put Wall 180（-2.2%，弱）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/PLTR_evening.json