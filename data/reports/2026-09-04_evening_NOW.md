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


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 143.32 → 收盘 141.26（-1.4%） ｜ 今日高 145.20 ｜ 低 138.80 ｜ 昨收 145.59 → 收盘 141.26（-3.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.37 | OI比 0.85 | ATM IV 47.8% | Skew 7.7pp | Term 1.06 | ExpMove ±5.1%（近端） | Rank — (历史不足)
量化视角： 期限结构正常（Term 1.06）｜保护溢价显著（Skew 7.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（7D）±5.1% ｜ 09-18（14D）±7.7% ｜ 09-25（21D）±9.3% ｜ 10-02（28D）±11.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,812,730 | GEX Change vs 上次快照 -5,107,583 | Flip: Primary Flip: 123.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 565 / LOW 89 / INVALID 276
结构观察区: Primary Flip 123.07（全链重定价，覆盖 83%）
Call Wall 150（弱结构｜现价低于该位 5.8%）
最近结构参考: Call Wall 150（现价低于该位 5.8%）
量化视角： 正 Gamma（1181万，无历史分位）｜正 Gamma 减弱（511万）｜现价位于 Flip 上方 14.78%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 139（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 123（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 137.0P — Vol 513 | 最新价 $0.01 | OI 666→1563 (ΔOI +897张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增897张（+134.7% vs前日OI），连续性待观察（方向未知）
09-04 144.0P — Vol 141 | 最新价 $2.95 | OI 555→1423 (ΔOI +868张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增868张（+156.4% vs前日OI），连续性待观察（方向未知）
10-09 140.0P — Vol 554 | 最新价 $7.80 | OI 402→931 (ΔOI +529张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增529张（+131.6% vs前日OI），连续性待观察（方向未知）
09-18 150.0C — Vol 1,240 | 最新价 $2.35 | OI 6403→6896 (ΔOI +493张) | ΔOI/Volume 39.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增493张（+7.7% vs前日OI），连续性待观察（方向未知）
09-11 147.0C — Vol 913 | 最新价 $1.48 | OI 128→609 (ΔOI +481张) | ΔOI/Volume 52.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增481张（+375.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,268 张（Put 2,294 / Call 974），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 16.3k / P 13.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.70 / P 3.45
隐含波动率 ATM IV:  46.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 140（结算参考） ｜ Call Wall 150（+6.2%，弱）（OI 1.8k） ｜ Put Wall 140（-0.9%）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 46.3%｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 120（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 130（结算参考） ｜ Call Wall 150（+6.2%）（OI 0.8k）

10-02（Activity LOW）仓位参考: Max Pain 130（结算参考） ｜ Call Wall 150（+6.2%，弱）（OI 1.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/NOW_evening.json