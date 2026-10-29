# 期权晚报 2026-10-28（快照 21:00 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **事件差分**: 10-30（2D）ATM IV 138.7% vs 11-06 87.2%（差 +51.5pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 156.64 → 收盘 162.32（+3.6%） ｜ 今日高 162.46 ｜ 低 156.64 ｜ 昨收 161.09 → 收盘 162.32（+0.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 1.97 | OI比 0.49 | ATM IV 138.7% | Skew 1.1pp | Term 0.48 | ExpMove ±8.4%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.49）+ 当日成交偏 Put（P/C量 1.97）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.97×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±8.4% ｜ 11-06（9D）±11.0% ｜ 11-13（16D）±12.6% ｜ 11-20（23D）±15.0%
   ⇒ IV–VIX Spread: +121.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,159,465 | GEX Change vs 上次快照 2,488,190 | Flip: Primary Flip: 155.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 449 / LOW 125 / INVALID 316
结构观察区: Primary Flip 155.17（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 4.5%）
最近结构参考: Call Wall 170（现价低于该位 4.5%）
量化视角： 正 Gamma（1116万，无历史分位）｜正 Gamma 增强（+249万）｜现价位于 Flip 上方 4.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 9D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 16D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 10-30 Forward Structure
存量OI: C 71.7k / P 35.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.60 / P $7.05 ｜ ATM IV 138.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+6.3%，弱）（OI 11.8k） ｜ Put Wall 155（-4.5%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 138.7%｜历史 Rank 97%（近端代理）｜IV/RV 2.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 175（+7.8%，弱）（OI 0.9k）

11-13（Activity LOW）仓位参考: Max Pain 172 ｜ Call Wall 177.5（+9.4%）（OI 1.2k） ｜ Put Wall 155（-4.5%，弱）（OI 1.0k）

11-20（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 170（+4.7%）（OI 13.6k） ｜ Put Wall 150（-7.6%，弱）（OI 3.1k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 138.7% vs 11-06 87.2%（差 +51.5pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/COIN_evening.json