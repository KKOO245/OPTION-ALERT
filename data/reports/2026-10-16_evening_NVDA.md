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
🟡 **近现价集中开仓**: 10-19 220C ΔOI +5,185（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 216.56 → 收盘 214.13（-1.1%） ｜ 今日高 218.68 ｜ 低 213.34 ｜ 昨收 217.23 → 收盘 214.13（-1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.69 | OI比 0.85 | ATM IV 48.6% | Skew 7.9pp | Term 0.73 | ExpMove ±2.2%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 7.9pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.2% ｜ 10-21（5D）±3.3% ｜ 10-23（7D）±4.1% ｜ 10-26（10D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 91,555,296 | GEX Change vs 上次快照 -49,427,520 | Flip: Primary Flip: 208.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 711 / LOW 163 / INVALID 608
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 208.93（全链重定价，覆盖 82%）
最近结构参考: Flip 209（现价高于该位 2.5%）
量化视角： 正 Gamma（9156万，无历史分位）｜正 Gamma 减弱（4943万）｜现价位于 Flip 上方 2.49%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 218（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 209（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +26.0k / P +11.9k ｜ Activity HIGH ｜ 3D
10-21  C +11.1k / P +9.1k ｜ Activity HIGH ｜ 5D
10-23  C +44.9k / P +32.1k ｜ Activity HIGH ｜ 7D
10-26  C +2.9k / P +3.8k ｜ Activity HIGH ｜ 10D

📆 10-19 Forward Structure
存量OI: C 84.1k / P 48.4k，今日变化ΔOI: C +26.0k / P +11.9k，平值价格ATM: C $1.82 / P $2.83 ｜ ATM IV 29.4%，净 delta 敞口 609k shares
Top ΔOI: C 225 +7,388 ｜ C 220 +5,185 ｜ P 210 +3,350
仓位参考: Max Pain 220 ｜ Call Wall 225（+5.1%，弱）（OI 12.0k） ｜ Put Wall 215（+0.4%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 29.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.31×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 608,908 股

📆 10-21 Forward Structure
存量OI: C 39.2k / P 26.1k，今日变化ΔOI: C +11.1k / P +9.1k，平值价格ATM: C $3.15 / P $3.95 ｜ ATM IV 35.1%，净 delta 敞口 116k shares
Top ΔOI: C 222 +3,148 ｜ P 200 +2,935
仓位参考: Max Pain 220 ｜ Call Wall 230（+7.4%，弱）（OI 5.6k） ｜ Put Wall 220（+2.7%，弱）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 35.1%｜历史 Rank 69%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 115,910 股

📆 10-23 Forward Structure
存量OI: C 237.1k / P 187.3k，今日变化ΔOI: C +44.9k / P +32.1k，平值价格ATM: C $4.03 / P $4.80 ｜ ATM IV 36.9%，净 delta 敞口 490k shares
Top ΔOI: C 225 +16,186 ｜ C 220 +9,348 ｜ C 230 +5,523
仓位参考: Max Pain 222 ｜ Call Wall 225（+5.1%，弱）（OI 26.6k） ｜ Put Wall 220（+2.7%，弱）（OI 14.4k）
量化解读： 存量 Call 重｜ATM IV 36.9%｜历史 Rank 69%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 490,142 股

📆 10-26 Forward Structure
存量OI: C 17.3k / P 5.9k，今日变化ΔOI: C +2.9k / P +3.8k，平值价格ATM: C $4.60 / P $5.20 ｜ ATM IV 33.7%，净 delta 敞口 -34k shares
Top ΔOI: P 200 +1,570 ｜ C 225 +1,246 ｜ P 215 +735
仓位参考: Max Pain 220 ｜ Put Wall 200（-6.6%）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.7%｜历史 Rank 69%（近端代理）｜IV/RV 1.50×（近似）｜净 delta 敞口 负 33,555 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/NVDA_evening.json