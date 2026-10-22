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

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 150P ΔOI +3,993（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 145.08 → 收盘 145.80（+0.5%） ｜ 今日高 149.40 ｜ 低 143.42 ｜ 昨收 153.48 → 收盘 145.80（-5.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.67 | OI比 0.83 | ATM IV 86.9% | Skew 2.3pp | Term 0.83 | ExpMove ±3.7%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 2.3pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±3.7% ｜ 10-30（8D）±9.3% ｜ 11-06（15D）±11.8% ｜ 11-13（22D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 67,433,420 | GEX Change vs 上次快照 -11,845,833 | Flip: Primary Flip: 136.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 633 / LOW 94 / INVALID 177
结构观察区: Primary Flip 136.77（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 8.0%）
最近结构参考: Flip 137（现价高于该位 6.6%）
量化视角： 正 Gamma（6743万，无历史分位）｜正 Gamma 减弱（1185万）｜现价位于 Flip 上方 6.60%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 142（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +4.9k / P +15.5k ｜ Activity HIGH ｜ 1D
10-30  C +4.7k / P +8.9k ｜ Activity HIGH ｜ 8D
11-06  C +2.1k / P +4.6k ｜ Activity HIGH ｜ 15D
11-13  C +0.9k / P +3.9k ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 233.8k / P 194.5k，今日变化ΔOI: C +4.9k / P +15.5k，平值价格ATM: C $2.66 / P $2.74 ｜ ATM IV 86.9%，净 delta 敞口 -872k shares
Top ΔOI: P 150 +3,993 ｜ C 148 -2,675
仓位参考: Max Pain 142 ｜ Call Wall 155（+6.3%，弱）（OI 29.0k） ｜ Put Wall 150（+2.9%，弱）（OI 7.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 86.9%｜历史 Rank 62%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 871,658 股

📆 10-30 Forward Structure
存量OI: C 55.2k / P 96.0k，今日变化ΔOI: C +4.7k / P +8.9k，平值价格ATM: C $6.74 / P $6.80 ｜ ATM IV 78.3%，净 delta 敞口 -61k shares
Top ΔOI: P 125 +1,347 ｜ C 170 +867
仓位参考: Max Pain 152 ｜ Call Wall 160（+9.7%，弱）（OI 3.9k） ｜ Put Wall 155（+6.3%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 78.3%｜历史 Rank 62%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 61,032 股

📆 11-06 Forward Structure
存量OI: C 16.7k / P 37.5k，今日变化ΔOI: C +2.1k / P +4.6k，平值价格ATM: C $7.98 / P $9.30 ｜ ATM IV 75.1%，净 delta 敞口 4k shares
仓位参考: Max Pain 160 ｜ Call Wall 160（+9.7%）（OI 2.0k） ｜ Put Wall 160（+9.7%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 75.1%｜历史 Rank 62%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,349 股

📆 11-13 Forward Structure
存量OI: C 14.0k / P 31.3k，今日变化ΔOI: C +0.9k / P +3.9k，平值价格ATM: C $10.44 / P $10.38 ｜ ATM IV 73.2%，净 delta 敞口 -62k shares
Top ΔOI: P 110 +475
仓位参考: Max Pain 160 ｜ Call Wall 144（-1.2%，弱）（OI 0.8k） ｜ Put Wall 160（+9.7%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 73.2%｜历史 Rank 62%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 负 61,954 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/MSTR_evening.json