# 期权晚报 2026-10-29（快照 16:40 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 195C ΔOI +892（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 198.37 → 收盘 196.42（-1.0%） ｜ 今日高 198.51 ｜ 低 190.36 ｜ 昨收 196.81 → 收盘 196.42（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.50 | OI比 1.01 | ATM IV 55.2% | Skew 2.5pp | Term 1.19 | ExpMove ±2.3%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构正常偏陡（Term 1.19）｜保护溢价中性（Skew 2.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.3% ｜ 11-06（8D）±12.2% ｜ 11-13（15D）±13.6% ｜ 11-20（22D）±13.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 34,368,730 | GEX Change vs 上次快照 3,456,183 | Flip: Primary Flip: 192.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 652 / LOW 92 / INVALID 194
结构观察区: Primary Flip 192.25（全链重定价，覆盖 100%）
Put Wall 180（弱结构｜现价高于该位 9.1%） | Call Wall 210（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 192（现价高于该位 2.2%）
量化视角： 正 Gamma（3437万，无历史分位）｜正 Gamma 增强（+346万）｜现价位于 Flip 上方 2.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 195（MaxPain，仅结算参考）；上方 210（Call Wall，弱结构）。
• Gamma 区域：切换参考 192（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C -1.6k / P +0.9k ｜ Activity MEDIUM △ ｜ 1D
11-06  C +8.2k / P +3.9k ｜ Activity HIGH ｜ 8D
11-13  C +1.0k / P +0.8k ｜ Activity HIGH ｜ 15D
11-20  C -83 / P +0.2k ｜ Activity LOW ｜ 22D

📆 10-30 Forward Structure
存量OI: C 128.3k / P 130.1k，今日变化ΔOI: C -1.6k / P +0.9k，平值价格ATM: C $1.80 / P $2.80 ｜ ATM IV 55.1%，净 delta 敞口 66k shares
Top ΔOI: C 195 +892 ｜ C 197 +887 ｜ C 212 -854
仓位参考: Max Pain 195 ｜ Call Wall 210（+6.9%，弱）（OI 16.8k） ｜ Put Wall 180（-8.4%，弱）（OI 9.6k）
量化解读： 存量两侧均衡｜ATM IV 55.1%｜历史 Rank 75%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 65,961 股

📆 11-06 Forward Structure
存量OI: C 56.9k / P 56.8k，今日变化ΔOI: C +8.2k / P +3.9k，平值价格ATM: C $11.47 / P $12.49 ｜ ATM IV 101.8%，净 delta 敞口 24k shares
Top ΔOI: C 215 +539 ｜ P 195 +524
仓位参考: Max Pain 195 ｜ Call Wall 215（+9.5%，弱）（OI 3.8k） ｜ Put Wall 190（-3.3%，弱）（OI 3.7k）
量化解读： 存量两侧均衡｜ATM IV 101.8%｜历史 Rank 75%（近端代理）｜IV/RV 2.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,217 股

📆 11-13 Forward Structure
存量OI: C 17.2k / P 18.3k，今日变化ΔOI: C +1.0k / P +0.8k，平值价格ATM: C $12.44 / P $14.24 ｜ ATM IV 79.6%，净 delta 敞口 34k shares
Top ΔOI: C 205 +327 ｜ C 197 +174 ｜ P 180 +166
仓位参考: Max Pain 195 ｜ Call Wall 210（+6.9%，弱）（OI 1.4k） ｜ Put Wall 180（-8.4%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.6%｜历史 Rank 75%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,877 股

11-20（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 200（+1.8%，弱）（OI 13.0k） ｜ Put Wall 180（-8.4%，弱）（OI 10.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/PLTR_evening.json