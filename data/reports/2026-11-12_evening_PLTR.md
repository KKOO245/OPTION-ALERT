# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 170C ΔOI -1,765（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 169.94 → 收盘 171.58（+1.0%） ｜ 今日高 173.05 ｜ 低 168.25 ｜ 昨收 172.40 → 收盘 171.58（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.82 | OI比 0.63 | ATM IV 56.3% | Skew 3.3pp | Term 0.88 | ExpMove ±2.4%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.4% ｜ 11-20（8D）±6.1% ｜ 11-27（15D）±7.8% ｜ 12-04（22D）±9.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 56,748,673 | GEX Change vs 上次快照 3,516,914 | Flip: Primary Flip: 161.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 451 / LOW 223 / INVALID 266
结构观察区: Primary Flip 161.46（全链重定价，覆盖 100%）
Call Wall 185（弱结构｜现价低于该位 7.3%）
最近结构参考: Flip 161（现价高于该位 6.3%）
量化视角： 正 Gamma（5675万，无历史分位）｜正 Gamma 增强（+352万）｜现价位于 Flip 上方 6.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）；上方 185（Call Wall，弱结构）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +1.4k / P +2.4k ｜ Activity MEDIUM △ ｜ 1D
11-20  C +6.8k / P +1.5k ｜ Activity HIGH ｜ 8D
11-27  C +0.9k / P -72 ｜ Activity HIGH ｜ 15D
12-04  C +0.2k / P +3.2k ｜ Activity HIGH ｜ 22D

📆 11-13 Forward Structure
存量OI: C 139.8k / P 88.2k，今日变化ΔOI: C +1.4k / P +2.4k，平值价格ATM: C $1.62 / P $2.45 ｜ ATM IV 56.3%，净 delta 敞口 -133k shares
Top ΔOI: C 170 -1,765 ｜ P 162 +1,560 ｜ C 175 +1,431
仓位参考: Max Pain 162 ｜ Call Wall 165（-3.8%，弱）（OI 12.8k） ｜ Put Wall 165（-3.8%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 56.3%｜历史 Rank 66%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 133,072 股

📆 11-20 Forward Structure
存量OI: C 186.2k / P 189.9k，今日变化ΔOI: C +6.8k / P +1.5k，平值价格ATM: C $4.90 / P $5.60 ｜ ATM IV 51.5%，净 delta 敞口 210k shares
Top ΔOI: C 177 +2,935 ｜ C 182 +2,619 ｜ P 162 +1,384
仓位参考: Max Pain 175 ｜ Call Wall 180（+4.9%，弱）（OI 11.2k） ｜ Put Wall 185（+7.8%，弱）（OI 9.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.5%｜历史 Rank 66%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 210,135 股

📆 11-27 Forward Structure
存量OI: C 18.2k / P 21.9k，今日变化ΔOI: C +0.9k / P -72，平值价格ATM: C $6.25 / P $7.15 ｜ ATM IV 48.0%，净 delta 敞口 29k shares
Top ΔOI: C 172 +250
仓位参考: Max Pain 175 ｜ Call Wall 180（+4.9%，弱）（OI 1.4k） ｜ Put Wall 170（-0.9%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.0%｜历史 Rank 66%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 29,404 股

📆 12-04 Forward Structure
存量OI: C 15.9k / P 12.9k，今日变化ΔOI: C +0.2k / P +3.2k，平值价格ATM: C $9.20 / P $7.20 ｜ ATM IV 48.6%，净 delta 敞口 -40k shares
Top ΔOI: P 155 +2,044
仓位参考: Max Pain 175 ｜ Call Wall 185（+7.8%，弱）（OI 1.2k） ｜ Put Wall 155（-9.7%）（OI 2.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.6%｜历史 Rank 66%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 负 40,002 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/PLTR_evening.json