# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 760C ΔOI +4,234（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 753.94 → 收盘 747.58（-0.8%） ｜ 今日高 757.18 ｜ 低 743.23 ｜ 昨收 757.73 → 收盘 747.58（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.93 | OI比 2.30 | ATM IV 15.9% | Skew -0.1pp | Term 1.20 | ExpMove ±0.8%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常偏陡（Term 1.20）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 27% ｜ P/C OI(近端) 88%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 27%）｜近端持仓结构中性（P/C OI 分位 88%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-09（1D）±0.8% ｜ 10-12（4D）±1.1% ｜ 10-13（5D）±1.3% ｜ 10-14（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -344,896,343 | GEX Change vs 上次快照 -184,248,005 | Flip: Primary Flip: 752.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2966 / LOW 278 / INVALID 1806
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 752.44（全链重定价，覆盖 94%）
Call Wall 760（现价低于该位 1.6%）
最近结构参考: Flip 752（现价低于该位 0.6%）
量化视角： 负 Gamma（3.45亿，历史分位 27%，中性区）｜负 Gamma 加深（1.84亿）｜现价位于 Flip 下方 0.65%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 757（MaxPain，仅结算参考） / 760（Call Wall）。
• Gamma 区域：切换参考 752（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +15.7k / P +39.5k ｜ Activity MEDIUM △ ｜ 1D
10-12  C +4.6k / P +32.6k ｜ Activity HIGH ｜ 4D
10-13  C +3.0k / P +8.1k ｜ Activity HIGH ｜ 5D
10-14  C +3.1k / P +9.8k ｜ Activity HIGH ｜ 6D

📆 10-09 Forward Structure
存量OI: C 202.3k / P 394.8k，今日变化ΔOI: C +15.7k / P +39.5k，平值价格ATM: C $2.95 / P $2.65 ｜ ATM IV 17.7%，净 delta 敞口 -888k shares
Top ΔOI: C 760 +4,234 ｜ P 738 +3,297
仓位参考: Max Pain 751 ｜ Call Wall 754（+0.9%，弱）（OI 20.2k） ｜ Put Wall 730（-2.4%）（OI 36.2k）
量化解读： 存量 Put 重｜ATM IV 17.7%｜历史 Rank 36%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 888,460 股

📆 10-12 Forward Structure
存量OI: C 30.8k / P 126.8k，今日变化ΔOI: C +4.6k / P +32.6k，平值价格ATM: C $4.30 / P $4.07 ｜ ATM IV 13.2%，净 delta 敞口 -398k shares
Top ΔOI: P 742 +6,162 ｜ P 755 +1,545
仓位参考: Max Pain 754 ｜ Call Wall 765（+2.3%，弱）（OI 1.8k） ｜ Put Wall 738（-1.3%，弱）（OI 12.7k）
量化解读： 存量 Put 重｜ATM IV 13.2%｜历史 Rank 36%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 398,040 股

📆 10-13 Forward Structure
存量OI: C 17.3k / P 77.1k，今日变化ΔOI: C +3.0k / P +8.1k，平值价格ATM: C $5.15 / P $4.83 ｜ ATM IV 14.2%，净 delta 敞口 -69k shares
Top ΔOI: P 726 +2,321 ｜ C 773 +600
仓位参考: Max Pain 753 ｜ Call Wall 765（+2.3%，弱）（OI 1.0k） ｜ Put Wall 740（-1.0%，弱）（OI 11.1k）
量化解读： 存量 Put 重｜ATM IV 14.2%｜历史 Rank 36%（近端代理）｜IV/RV 1.07×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 68,730 股

📆 10-14 Forward Structure
存量OI: C 14.7k / P 36.1k，今日变化ΔOI: C +3.1k / P +9.8k，平值价格ATM: C $6.20 / P $5.80 ｜ ATM IV 15.7%，净 delta 敞口 -209k shares
Top ΔOI: P 730 +1,948 ｜ P 720 +1,468 ｜ C 771 +1,167
仓位参考: Max Pain 753 ｜ Call Wall 755（+1.0%，弱）（OI 2.3k） ｜ Put Wall 730（-2.4%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 15.7%｜历史 Rank 36%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 209,336 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/QQQ_evening.json