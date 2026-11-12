# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 928.24 → 收盘 977.69（+5.3%） ｜ 今日高 1011.05 ｜ 低 920.18 ｜ 昨收 859.99 → 收盘 977.69（+13.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.56 | OI比 0.63 | ATM IV 107.8% | Skew 4.8pp | Term 0.80 | ExpMove ±6.4%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±6.4% ｜ 11-20（9D）±12.4% ｜ 11-27（16D）±14.9% ｜ 12-04（23D）±17.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,221,507 | GEX Change vs 上次快照 625,085 | Flip: Primary Flip: 903.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2071 / LOW 701 / INVALID 1238
结构观察区: Primary Flip 903.48（全链重定价，覆盖 100%）
最近结构参考: Flip 903（现价高于该位 8.2%）
量化视角： 正 Gamma（522万，无历史分位）｜正 Gamma 增强（+63万）｜现价位于 Flip 上方 8.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 900（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 903（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +3.3k / P +2.6k ｜ Activity HIGH ｜ 2D
11-20  C +3.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 9D
11-27  C +0.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
12-04  C +0.8k / P +0.3k ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 48.3k / P 30.6k，今日变化ΔOI: C +3.3k / P +2.6k，平值价格ATM: C $30.30 / P $32.40 ｜ ATM IV 107.8%，净 delta 敞口 214k shares
Top ΔOI: C 1100 +344 ｜ C 880 +331 ｜ C 900 +284
仓位参考: Max Pain 900 ｜ Call Wall 1000（+2.3%，弱）（OI 2.6k） ｜ Put Wall 900（-7.9%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 107.8%｜历史 Rank 64%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 213,532 股

11-20（MEDIUM △）Top ΔOI: 1250C +398 ｜ 1080C +296
11-20（MEDIUM △）仓位参考: Max Pain 1,100 ｜ Call Wall 1000（+2.3%，弱）（OI 2.1k） ｜ Put Wall 1000（+2.3%，弱）（OI 2.3k）

11-27（MEDIUM △）Top ΔOI: 740C +109 ｜ 770C +100
11-27（MEDIUM △）仓位参考: Max Pain 1,150 ｜ Put Wall 930（-4.9%，弱）（OI 0.2k）

📆 12-04 Forward Structure
存量OI: C 7.9k / P 5.7k，今日变化ΔOI: C +0.8k / P +0.3k，平值价格ATM: C $89.00 / P $77.41 ｜ ATM IV 86.3%，净 delta 敞口 13k shares
Top ΔOI: C 1455 +103 ｜ P 700 +74
仓位参考: Max Pain 1,000 ｜ Call Wall 950（-2.8%，弱）（OI 0.2k） ｜ Put Wall 970（-0.8%，弱）（OI 95）
量化解读： 存量 Call 重｜ATM IV 86.3%｜历史 Rank 64%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 正 12,511 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 107.8% vs 11-20 99.0%（差 +8.8pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SNDK_evening.json