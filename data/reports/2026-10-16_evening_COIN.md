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
🟡 **近现价集中开仓**: 10-30 180C ΔOI +215（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 160.7）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 181.11 → 收盘 173.16（-4.4%） ｜ 今日高 183.40 ｜ 低 168.86 ｜ 昨收 183.81 → 收盘 173.16（-5.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.67 | OI比 0.81 | ATM IV 71.0% | Skew 11.3pp | Term 1.07 | ExpMove ±7.4%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 1.07）｜保护溢价显著（Skew 11.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（7D）±7.4% ｜ 10-30（14D）±12.4% ｜ 11-06（21D）±14.3% ｜ 11-13（28D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 10,172,996 | GEX Change vs 上次快照 -18,933,281 | Flip: Candidates 160.72 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 73%（带内） ｜ IV 有效性: VALID 404 / LOW 117 / INVALID 301
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈161（全链重定价，覆盖 73%，CONDITIONAL）
最近结构参考: Flip 161（现价高于该位 7.7%）
量化视角： 正 Gamma（1017万，无历史分位）｜正 Gamma 减弱（1893万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 178（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 73%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +15.3k / P +5.0k ｜ Activity HIGH ｜ 7D
10-30  C +1.1k / P +1.8k ｜ Activity HIGH ｜ 14D
11-06  C +0.5k / P +9 ｜ Activity HIGH ｜ 21D
11-13  C +0.1k / P +0.6k ｜ Activity HIGH ｜ 28D

📆 10-23 Forward Structure
存量OI: C 30.7k / P 25.9k，今日变化ΔOI: C +15.3k / P +5.0k，平值价格ATM: C $6.80 / P $5.95 ｜ ATM IV 66.7%，净 delta 敞口 143k shares
Top ΔOI: C 197 +4,996 ｜ C 190 +4,350
仓位参考: Max Pain 180 ｜ Call Wall 190（+9.7%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 66.7%｜历史 Rank 36%（近端代理）｜IV/RV 1.52×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 142,963 股

📆 10-30 Forward Structure
存量OI: C 14.4k / P 13.7k，今日变化ΔOI: C +1.1k / P +1.8k，平值价格ATM: C $11.03 / P $10.49 ｜ ATM IV 79.2%，净 delta 敞口 6k shares
Top ΔOI: C 180 +215 ｜ C 185 +188
仓位参考: Max Pain 182 ｜ Call Wall 185（+6.8%，弱）（OI 1.6k） ｜ Put Wall 180（+4.0%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.2%｜历史 Rank 36%（近端代理）｜IV/RV 1.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,075 股

📆 11-06 Forward Structure
存量OI: C 5.0k / P 7.4k，今日变化ΔOI: C +0.5k / P +9，平值价格ATM: C $12.70 / P $12.05 ｜ ATM IV 74.8%，净 delta 敞口 26k shares
Top ΔOI: C 125 +94 ｜ P 180 -51
仓位参考: Max Pain 175 ｜ Call Wall 175（+1.1%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.8%｜历史 Rank 36%（近端代理）｜IV/RV 1.71×（近似）｜净 delta 敞口 正 25,692 股

📆 11-13 Forward Structure
存量OI: C 2.6k / P 6.1k，今日变化ΔOI: C +0.1k / P +0.6k，平值价格ATM: C $14.53 / P $14.60 ｜ ATM IV 75.8%，净 delta 敞口 -13k shares
Top ΔOI: P 155 +157 ｜ P 167 +127 ｜ P 165 +79
仓位参考: Max Pain 182 ｜ Call Wall 185（+6.8%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 75.8%｜历史 Rank 36%（近端代理）｜IV/RV 1.73×（近似）｜净 delta 敞口 负 12,689 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/COIN_evening.json