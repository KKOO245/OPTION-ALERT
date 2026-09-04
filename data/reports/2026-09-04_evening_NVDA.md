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


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 231.14 → 收盘 230.36（-0.3%） ｜ 今日高 234.76 ｜ 低 229.63 ｜ 昨收 228.45 → 收盘 230.36（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.51 | OI比 1.12 | ATM IV 19.0% | Skew -13.3pp | Term 1.75 | ExpMove ±2.4%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.75）｜Put 保护异常便宜（Skew -13.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-09（5D）±2.4% ｜ 09-11（7D）±3.4% ｜ 09-14（10D）±3.8% ｜ 09-16（12D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 812,100,726 | GEX Change vs 上次快照 -60,180,222 | Flip: Primary Flip: 211.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 559 / LOW 180 / INVALID 399
结构观察区: Primary Flip 211.78（全链重定价，覆盖 84%）
Call Wall 230（弱结构｜现价高于该位 0.2%）
最近结构参考: Call Wall 230（现价高于该位 0.2%）
量化视角： 正 Gamma（8.12亿，无历史分位）｜正 Gamma 减弱（6018万）｜现价位于 Flip 上方 8.77%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 212（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 145.0P — Vol 5 | 最新价 $0.01 | OI 2035→55388 (ΔOI +53353张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增53353张（+2621.8% vs前日OI），连续性待观察（方向未知）
09-04 140.0P — Vol 33,126（Yahoo补） | 最新价 $0.01 | OI 2702→34769 (ΔOI +32067张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32067张（+1186.8% vs前日OI），连续性待观察（方向未知）
10-02 250.0C — Vol 9,902 | 最新价 $2.23 | OI 11081→28489 (ΔOI +17408张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17408张（+157.1% vs前日OI），连续性待观察（方向未知）
09-11 240.0C — Vol 28,923 | 最新价 $0.82 | OI 20813→37503 (ΔOI +16690张) | ΔOI/Volume 57.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16690张（+80.2% vs前日OI），连续性待观察（方向未知）
09-04 135.0P — Vol 1 | 最新价 $0.01 | OI 3251→18354 (ΔOI +15103张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15103张（+464.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 134,621 张（Put 100,523 / Call 34,098），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-09  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 10D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 12D

📆 09-09 Forward Structure
存量OI:      C 128.1k / P 53.2k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.00 / P 2.59
隐含波动率 ATM IV:  25.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 222（结算参考） ｜ Call Wall 240（+4.2%）（OI 36.2k）
量化解读： 存量 Call 重｜ATM IV 25.8%｜历史 Rank 0%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（Activity LOW）仓位参考: Max Pain 220（结算参考） ｜ Call Wall 240（+4.2%，弱）（OI 37.5k） ｜ Put Wall 210（-8.8%，弱）（OI 11.3k）

09-14（Activity LOW）仓位参考: Max Pain 225（结算参考） ｜ Call Wall 230（-0.2%）（OI 7.7k） ｜ Put Wall 220（-4.5%，弱）（OI 1.1k）

09-16（Activity LOW）仓位参考: Max Pain 225（结算参考） ｜ Call Wall 245（+6.4%）（OI 4.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/NVDA_evening.json