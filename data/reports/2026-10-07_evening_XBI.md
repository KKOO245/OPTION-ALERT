# 期权晚报 2026-10-07（快照 16:40 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.08 ↑0.5%（5D -7.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 148P ΔOI +1,281（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 149.37 → 收盘 150.23（+0.6%） ｜ 今日高 152.40 ｜ 低 148.64 ｜ 昨收 150.90 → 收盘 150.23（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.36 | OI比 2.37 | ATM IV 30.1% | Skew 4.0pp | Term 1.09 | ExpMove ±2.0%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 1.09）｜保护溢价中性（Skew 4.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.0% ｜ 10-16（9D）±4.3% ｜ 10-23（16D）±8.0% ｜ 10-30（23D）±6.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -55,062,016 | GEX Change N/A | Flip: Primary Flip: 162.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 300 / LOW 101 / INVALID 339
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 162.92（全链重定价，覆盖 88%）
Put Wall 150（现价高于该位 0.2%）
最近结构参考: Put Wall 150（现价高于该位 0.2%）
量化视角： 负 Gamma（5506万，无历史分位）｜现价位于 Flip 下方 7.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +1.3k / P +2.3k ｜ Activity HIGH ｜ 2D
10-16  C +2.7k / P +0.2k ｜ Activity HIGH ｜ 9D
10-23  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 16D
10-30  C +0.2k / P +27 ｜ Activity HIGH ｜ 23D

📆 10-09 Forward Structure
存量OI: C 5.5k / P 13.1k，今日变化ΔOI: C +1.3k / P +2.3k，平值价格ATM: C $1.69 / P $1.28 ｜ ATM IV 30.1%，净 delta 敞口 -42k shares
Top ΔOI: P 148 +1,281 ｜ P 150 +487 ｜ C 158 +358
仓位参考: Max Pain 155 ｜ Call Wall 145（-3.5%）（OI 1.0k） ｜ Put Wall 148（-1.5%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 30.1%｜历史 Rank 32%（近端代理）｜IV/RV 1.11×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 41,733 股

📆 10-16 Forward Structure
存量OI: C 42.2k / P 78.8k，今日变化ΔOI: C +2.7k / P +0.2k，平值价格ATM: C $3.60 / P $2.80 ｜ ATM IV 31.0%，净 delta 敞口 141k shares
Top ΔOI: C 155 +1,563 ｜ C 145 +975
仓位参考: Max Pain 160 ｜ Call Wall 155（+3.2%，弱）（OI 2.7k） ｜ Put Wall 150（-0.2%）（OI 22.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.0%｜历史 Rank 32%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 140,663 股

📆 10-23 Forward Structure
存量OI: C 1.2k / P 2.2k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $7.75 / P $4.20 ｜ ATM IV 32.2%，净 delta 敞口 -3k shares
Top ΔOI: P 149 +107 ｜ C 156 +49
仓位参考: Max Pain 155 ｜ Call Wall 154（+2.5%，弱）（OI 89） ｜ Put Wall 153（+1.8%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 32.2%｜历史 Rank 32%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,606 股

📆 10-30 Forward Structure
存量OI: C 2.4k / P 18.0k，今日变化ΔOI: C +0.2k / P +27，平值价格ATM: C $5.12 / P $4.36 ｜ ATM IV 31.7%，净 delta 敞口 -3k shares
Top ΔOI: P 140 -612 ｜ P 149 +347
仓位参考: Max Pain 154 ｜ Call Wall 159（+5.8%，弱）（OI 0.4k） ｜ Put Wall 150（-0.2%，弱）（OI 7.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.7%｜历史 Rank 32%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 3,262 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/XBI_evening.json