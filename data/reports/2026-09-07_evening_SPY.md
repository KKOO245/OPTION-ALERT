# 期权晚报 2026-09-07（快照 19:08 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 15.30 ↑5.3%（5D +2.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.99 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 772.01 → 收盘 770.19（-0.2%） ｜ 今日高 772.87 ｜ 低 769.00 ｜ 昨收 770.19 → 收盘 770.19（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.47 | OI比 2.40 | ATM IV 5.8% | Skew 1.2pp | Term 2.05 | ExpMove ±0.5%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 2.05）｜保护溢价薄（Skew 1.2pp）｜当日成交偏 Put（P/C量 1.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.47×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 51% ｜ P/C OI(近端) 84%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 51%）｜近端持仓结构中性（P/C OI 分位 84%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-08（1D）±0.5% ｜ 09-09（2D）±0.7% ｜ 09-10（3D）±0.8% ｜ 09-11（4D）±1.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -255,203,332 | GEX Change vs 上次快照 0 | Flip: Primary Flip: 771.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 3147 / LOW 204 / INVALID 1137
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 771.17（全链重定价，覆盖 100%）
Call Wall 800（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 771（现价低于该位 0.1%）
量化视角： 负 Gamma（2.55亿，历史分位 51%，中性区）｜负 Gamma 加深（0万）｜现价位于 Flip 下方 0.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 770（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 771（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 760.0P — Vol 54,980 | 最新价 $3.60 | OI 70613→114364 (ΔOI +43751张) | ΔOI/Volume 79.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43751张（+62.0% vs前日OI），连续性待观察（方向未知）
09-18 745.0P — Vol 39,829 | 最新价 $1.45 | OI 20766→56931 (ΔOI +36165张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36165张（+174.2% vs前日OI），连续性待观察（方向未知）
09-11 777.0C — Vol 17,858 | 最新价 $1.26 | OI 2789→17836 (ΔOI +15047张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15047张（+539.5% vs前日OI），连续性待观察（方向未知）
09-08 739.0P — Vol 15,936 | 最新价 $0.05 | OI 684→15253 (ΔOI +14569张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14569张（+2130.0% vs前日OI），连续性待观察（方向未知）
09-08 735.0P — Vol 14,142 | 最新价 $0.05 | OI 1113→14439 (ΔOI +13326张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13326张（+1197.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 122,858 张（Put 107,811 / Call 15,047），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $21M，买/卖方向不可观测）｜彩票/名义 2 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-08  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-09  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-10  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 09-08 Forward Structure
存量OI:      C 121.1k / P 290.9k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 1.76 / P 1.95
隐含波动率 ATM IV:  5.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 770（结算参考） ｜ Call Wall 775（+0.6%，弱）（OI 12.7k） ｜ Put Wall 739（-4.0%，弱）（OI 15.3k）
量化解读： 存量 Put 重｜ATM IV 5.8%｜历史 Rank 3%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-09（Activity LOW）仓位参考: Max Pain 768（结算参考） ｜ Call Wall 785（+1.9%）（OI 5.1k） ｜ Put Wall 710（-7.8%，弱）（OI 8.1k）

09-10（Activity LOW）仓位参考: Max Pain 768（结算参考） ｜ Call Wall 770（-0.0%，弱）（OI 3.7k） ｜ Put Wall 695（-9.8%，弱）（OI 8.0k）

09-11（Activity LOW）仓位参考: Max Pain 769（结算参考） ｜ Call Wall 777（+0.9%，弱）（OI 17.8k） ｜ Put Wall 760（-1.3%）（OI 55.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/SPY_evening.json