# 期权晚报 2026-09-09（快照 18:23 ET）

📊 市场环境

SPY $762.40 ｜ QQQ $716.31
VIX 16.46 ↑4.7%（5D +8.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 350.21 → 收盘 353.24（+0.9%） ｜ 今日高 357.99 ｜ 低 349.86 ｜ 昨收 350.16 → 收盘 353.24（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.65 | OI比 0.59 | ATM IV 38.4% | Skew 2.2pp | Term 0.87 | ExpMove ±2.6%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±2.6% ｜ 09-18（9D）±4.7% ｜ 09-25（16D）±5.9% ｜ 10-02（23D）±13.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,044,289 | GEX Change vs 上次快照 -246,854 | Flip: Primary Flip: 373.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 283 / LOW 215 / INVALID 404
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 373.65（全链重定价，覆盖 91%）
最近结构参考: Flip 374（现价低于该位 5.5%）
量化视角： 负 Gamma（404万，无历史分位）｜负 Gamma 加深（25万）｜现价位于 Flip 下方 5.46%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 374（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 360.0C — Vol 36 | 最新价 $1.67 | OI 8→1257 (ΔOI +1249张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1249张（+15612.5% vs前日OI），连续性待观察（方向未知）
09-11 350.0C — Vol 13 | 最新价 $5.77 | OI 1→1076 (ΔOI +1075张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1075张（+107500.0% vs前日OI），连续性待观察（方向未知）
09-18 345.0P — Vol 6 | 最新价 $4.87 | OI 163→695 (ΔOI +532张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增532张（+326.4% vs前日OI），连续性待观察（方向未知）
09-18 330.0P — Vol 68 | 最新价 $1.45 | OI 375→896 (ΔOI +521张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增521张（+138.9% vs前日OI），连续性待观察（方向未知）
09-11 342.5P — Vol 5 | 最新价 $1.49 | OI 31→325 (ΔOI +294张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增294张（+948.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,671 张（Put 1,347 / Call 2,324），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 3.9k / P 2.3k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 4.36 / P 5.00
隐含波动率 ATM IV:  38.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 350（结算参考） ｜ Call Wall 360（+1.9%，弱）（OI 1.3k） ｜ Put Wall 342.5（-3.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 38.4%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 375（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 370（结算参考） ｜ Put Wall 360（+1.9%，弱）（OI 0.1k）

10-02（Activity LOW）仓位参考: Max Pain 365（结算参考） ｜ Put Wall 335（-5.2%）（OI 2.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/ISRG_evening.json