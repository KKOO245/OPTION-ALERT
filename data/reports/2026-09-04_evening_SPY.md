# 期权晚报 2026-09-04（快照 17:18 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 772.01 → 收盘 770.19（-0.2%） ｜ 今日高 772.87 ｜ 低 769.00 ｜ 昨收 773.17 → 收盘 770.19（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.11 | OI比 1.21 | ATM IV 6.7% | Skew 1.5pp | Term 1.73 | ExpMove ±0.5%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常偏陡（Term 1.73）｜保护溢价薄（Skew 1.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 48% ｜ P/C OI(近端) 7%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 48%）｜近端持仓极端 Call 重（P/C OI 分位 7%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-08（4D）±0.5% ｜ 09-09（5D）±0.7% ｜ 09-10（6D）±0.8% ｜ 09-11（7D）±1.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -375,977,118 | GEX Change vs 上次快照 -262,635,660 | Flip: Primary Flip: 772.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 2824 / LOW 385 / INVALID 1207
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 772.05（全链重定价，覆盖 91%）
Call Wall 800（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 772（现价低于该位 0.2%）
量化视角： 负 Gamma（3.76亿，历史分位 48%，中性区）｜负 Gamma 加深（2.63亿）｜现价位于 Flip 下方 0.24%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 768（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 772（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 779.0C — Vol 428 | 最新价 $2.42 | OI 3298→40048 (ΔOI +36750张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36750张（+1114.3% vs前日OI），连续性待观察（方向未知）
09-18 743.0P — Vol 4,478 | 最新价 $1.31 | OI 8170→29489 (ΔOI +21319张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21319张（+260.9% vs前日OI），连续性待观察（方向未知）
09-18 740.0P — Vol 4,259 | 最新价 $1.08 | OI 32186→50210 (ΔOI +18024张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18024张（+56.0% vs前日OI），连续性待观察（方向未知）
09-11 760.0P — Vol 13,286 | 最新价 $1.28 | OI 37267→54008 (ΔOI +16741张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16741张（+44.9% vs前日OI），连续性待观察（方向未知）
09-04 770.0P — Vol 942,331 | 最新价 $0.28 | OI 10532→25296 (ΔOI +14764张) | ΔOI/Volume 1.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14764张（+140.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 107,598 张（Put 70,848 / Call 36,750），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $7M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-08  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-09  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-10  C +0 / P +0 ｜ Activity LOW ｜ 6D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D

📆 09-08 Forward Structure
存量OI:      C 66.9k / P 95.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 1.76 / P 1.95
隐含波动率 ATM IV:  5.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 769（结算参考） ｜ Call Wall 770（-0.0%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜ATM IV 5.8%｜历史 Rank 8%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-09（Activity LOW）仓位参考: Max Pain 768（结算参考） ｜ Call Wall 785（+1.9%）（OI 4.0k） ｜ Put Wall 710（-7.8%，弱）（OI 8.0k）

09-10（Activity LOW）仓位参考: Max Pain 767（结算参考） ｜ Call Wall 781（+1.4%，弱）（OI 2.5k） ｜ Put Wall 752（-2.4%，弱）（OI 2.8k）

09-11（Activity LOW）仓位参考: Max Pain 770（结算参考） ｜ Call Wall 780（+1.3%）（OI 16.6k） ｜ Put Wall 760（-1.3%）（OI 54.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/SPY_evening.json