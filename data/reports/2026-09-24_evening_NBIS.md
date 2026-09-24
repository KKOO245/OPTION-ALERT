# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 250C ΔOI +1,801（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 232.03 → 收盘 243.48（+4.9%） ｜ 今日高 249.19 ｜ 低 229.50 ｜ 昨收 226.61 → 收盘 243.48（+7.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.90 | ATM IV 88.7% | Skew -6.9pp | Term 0.92 | ExpMove ±3.8%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -6.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（1D）±3.8% ｜ 10-02（8D）±9.6% ｜ 10-09（15D）±13.8% ｜ 10-16（22D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,409,436 | GEX Change vs 上次快照 5,973,090 | Flip: Primary Flip: 225.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 585 / LOW 35 / INVALID 134
结构观察区: Primary Flip 225.47（全链重定价，覆盖 99%）
Call Wall 250（弱结构｜现价低于该位 2.6%）
最近结构参考: Call Wall 250（现价低于该位 2.6%）
量化视角： 正 Gamma（2441万，无历史分位）｜正 Gamma 增强（+597万）｜现价位于 Flip 上方 7.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 225（MaxPain，仅结算参考）；上方 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 225（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +3.9k / P +5.9k ｜ Activity HIGH ｜ 1D
10-02  C +12.2k / P +6.3k ｜ Activity HIGH ｜ 8D（新行权价 C 61）
10-09  C +2.4k / P +1.5k ｜ Activity HIGH ｜ 15D
10-16  C +2.5k / P +4.2k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 64.5k / P 57.9k，今日变化ΔOI: C +3.9k / P +5.9k，平值价格ATM: C $5.20 / P $4.16 ｜ ATM IV 88.7%，净 delta 敞口 -171k shares
Top ΔOI: C 230 -2,415 ｜ C 250 +1,801
仓位参考: Max Pain 225 ｜ Call Wall 250（+2.7%）（OI 8.4k） ｜ Put Wall 220（-9.6%，弱）（OI 5.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 88.7%｜历史 Rank 23%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 170,657 股

📆 10-02 Forward Structure
存量OI: C 34.0k / P 23.0k，今日变化ΔOI: C +12.2k / P +6.3k（新行权价 C 61），平值价格ATM: C $12.36 / P $11.05 ｜ ATM IV 83.9%，净 delta 敞口 499k shares
Top ΔOI: C 235 +4,050 ｜ P 210 +2,223 ｜ C 205 +1,768
仓位参考: Max Pain 220 ｜ Call Wall 235（-3.5%，弱）（OI 4.4k） ｜ Put Wall 220（-9.6%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 83.9%｜历史 Rank 23%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 498,643 股

📆 10-09 Forward Structure
存量OI: C 13.0k / P 11.7k，今日变化ΔOI: C +2.4k / P +1.5k，平值价格ATM: C $18.58 / P $15.00 ｜ ATM IV 77.5%，净 delta 敞口 49k shares
Top ΔOI: P 200 +405 ｜ C 290 +388 ｜ C 310 +356
仓位参考: Max Pain 220 ｜ Call Wall 240（-1.4%）（OI 2.0k） ｜ Put Wall 225（-7.6%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 77.5%｜历史 Rank 23%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 正 48,615 股

📆 10-16 Forward Structure
存量OI: C 55.7k / P 78.6k，今日变化ΔOI: C +2.5k / P +4.2k，平值价格ATM: C $19.89 / P $18.35 ｜ ATM IV 79.5%，净 delta 敞口 23k shares
Top ΔOI: P 190 +989 ｜ P 220 +920 ｜ P 200 +782
仓位参考: Max Pain 210 ｜ Call Wall 240（-1.4%，弱）（OI 4.8k） ｜ Put Wall 220（-9.6%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 79.5%｜历史 Rank 23%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 正 23,163 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/NBIS_evening.json