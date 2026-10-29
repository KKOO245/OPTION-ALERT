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
🟡 **近现价集中开仓**: 10-30 222C ΔOI +5,531（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 214.35 → 收盘 213.66（-0.3%） ｜ 今日高 215.32 ｜ 低 212.08 ｜ 昨收 215.38 → 收盘 213.66（-0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.71 | OI比 0.66 | ATM IV 34.8% | Skew 1.8pp | Term 1.16 | ExpMove ±1.5%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构正常偏陡（Term 1.16）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±1.5% ｜ 11-02（4D）±2.3% ｜ 11-04（6D）±3.3% ｜ 11-06（8D）±4.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 130,326,661 | GEX Change vs 上次快照 12,027,621 | Flip: Primary Flip: 211.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 599 / LOW 225 / INVALID 538
结构观察区: Primary Flip 211.63（全链重定价，覆盖 97%）
Put Wall 200（弱结构｜现价高于该位 6.8%） | Call Wall 230（现价低于该位 7.1%）
最近结构参考: Flip 212（现价高于该位 1.0%）
量化视角： 正 Gamma（1.30亿，无历史分位）｜正 Gamma 增强（+1203万）｜现价位于 Flip 上方 0.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 215（MaxPain，仅结算参考） / 230（Call Wall）。
• Gamma 区域：切换参考 212（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +34.3k / P +39.4k ｜ Activity HIGH ｜ 1D
11-02  C +7.3k / P +11.6k ｜ Activity HIGH ｜ 4D
11-04  C +3.0k / P +4.1k ｜ Activity HIGH ｜ 6D
11-06  C +6.5k / P +7.8k ｜ Activity HIGH ｜ 8D

📆 10-30 Forward Structure
存量OI: C 517.1k / P 343.7k，今日变化ΔOI: C +34.3k / P +39.4k，平值价格ATM: C $2.28 / P $1.02 ｜ ATM IV 34.8%，净 delta 敞口 75k shares
Top ΔOI: C 222 +5,531
仓位参考: Max Pain 215 ｜ Call Wall 225（+5.3%，弱）（OI 62.1k） ｜ Put Wall 210（-1.7%，弱）（OI 26.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.8%｜历史 Rank 21%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 75,374 股

📆 11-02 Forward Structure
存量OI: C 27.5k / P 31.8k，今日变化ΔOI: C +7.3k / P +11.6k，平值价格ATM: C $3.05 / P $1.82 ｜ ATM IV 26.7%，净 delta 敞口 -83k shares
Top ΔOI: P 212 +1,738 ｜ C 220 +1,686
仓位参考: Max Pain 215 ｜ Call Wall 230（+7.6%，弱）（OI 4.8k） ｜ Put Wall 200（-6.4%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 26.7%｜历史 Rank 21%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 82,552 股

📆 11-04 Forward Structure
存量OI: C 14.9k / P 12.1k，今日变化ΔOI: C +3.0k / P +4.1k，平值价格ATM: C $4.20 / P $2.89 ｜ ATM IV 32.0%，净 delta 敞口 -41k shares
Top ΔOI: P 212 +923 ｜ C 220 +744 ｜ P 205 +613
仓位参考: Max Pain 215 ｜ Call Wall 225（+5.3%）（OI 3.9k） ｜ Put Wall 205（-4.1%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.0%｜历史 Rank 21%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 41,081 股

📆 11-06 Forward Structure
存量OI: C 116.0k / P 159.9k，今日变化ΔOI: C +6.5k / P +7.8k，平值价格ATM: C $4.97 / P $3.60 ｜ ATM IV 33.5%，净 delta 敞口 40k shares
Top ΔOI: C 220 +2,249 ｜ C 217 +1,372
仓位参考: Max Pain 220 ｜ Call Wall 230（+7.6%，弱）（OI 12.8k） ｜ Put Wall 200（-6.4%）（OI 12.1k）
量化解读： 存量 Put 重｜ATM IV 33.5%｜历史 Rank 21%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 正 39,580 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 34.8% vs 11-02 26.7%（差 +8.1pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/NVDA_evening.json