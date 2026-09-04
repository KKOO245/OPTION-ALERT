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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 719.36 → 收盘 718.96（-0.1%） ｜ 今日高 721.86 ｜ 低 716.56 ｜ 昨收 717.67 → 收盘 718.96（+0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.93 | OI比 1.28 | ATM IV 9.8% | Skew 4.1pp | Term 1.73 | ExpMove ±0.7%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常偏陡（Term 1.73）｜保护溢价中性（Skew 4.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.28×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 61% ｜ P/C OI(近端) 20%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 61%）｜近端持仓结构中性（P/C OI 分位 20%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-08（4D）±0.7% ｜ 09-09（5D）±1.0% ｜ 09-10（6D）±1.2% ｜ 09-11（7D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 96,045,399 | GEX Change vs 上次快照 -54,719,909 | Flip: Primary Flip: 717.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 2408 / LOW 512 / INVALID 1886
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 717.29（全链重定价，覆盖 91%）
Put Wall 700（弱结构｜现价高于该位 2.7%） | Call Wall 730（弱结构｜现价低于该位 1.5%）
最近结构参考: Flip 717（现价高于该位 0.2%）
量化视角： 正 Gamma（9605万，历史分位 61%，中性区）｜正 Gamma 减弱（5472万）｜现价位于 Flip 上方 0.23%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构） / 715（MaxPain，仅结算参考）；上方 730（Call Wall，弱结构）。
• Gamma 区域：切换参考 717（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 730.0C — Vol 17,231 | 最新价 $0.01 | OI 6652→19541 (ΔOI +12889张) | ΔOI/Volume 74.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12889张（+193.8% vs前日OI），连续性待观察（方向未知）
09-04 725.0C — Vol 55,683 | 最新价 $0.01 | OI 7558→19262 (ΔOI +11704张) | ΔOI/Volume 21.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11704张（+154.9% vs前日OI），连续性待观察（方向未知）
09-30 700.0P — Vol 1,862 | 最新价 $6.50 | OI 22215→32305 (ΔOI +10090张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10090张（+45.4% vs前日OI），连续性待观察（方向未知）
09-09 575.0P — Vol 0 | 最新价 $0.01 | OI 0→10000 (ΔOI +10000张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增10000张（前日OI缺失），值得跟踪（方向未知）
09-11 700.0P — Vol 4,545 | 最新价 $1.10 | OI 4800→12910 (ΔOI +8110张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8110张（+169.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 52,793 张（Put 28,200 / Call 24,593），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $7M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-08  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-09  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-10  C +0 / P +0 ｜ Activity LOW ｜ 6D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D

📆 09-08 Forward Structure
存量OI:      C 50.7k / P 97.7k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.20 / P 2.80
隐含波动率 ATM IV:  8.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 715（结算参考） ｜ Call Wall 730（+1.5%，弱）（OI 3.9k） ｜ Put Wall 710（-1.2%，弱）（OI 7.4k）
量化解读： 存量 Put 重｜ATM IV 8.3%｜历史 Rank 8%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-09（Activity LOW）仓位参考: Max Pain 713（结算参考） ｜ Call Wall 722（+0.4%）（OI 5.6k）

09-10（Activity LOW）仓位参考: Max Pain 713（结算参考） ｜ Call Wall 725（+0.8%）（OI 2.5k） ｜ Put Wall 678（-5.7%，弱）（OI 2.0k）

09-11（Activity LOW）仓位参考: Max Pain 714（结算参考） ｜ Call Wall 750（+4.3%，弱）（OI 14.7k） ｜ Put Wall 705（-1.9%，弱）（OI 20.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/QQQ_evening.json