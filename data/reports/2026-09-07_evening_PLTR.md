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


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 180.01 → 收盘 174.33（-3.2%） ｜ 今日高 182.19 ｜ 低 173.67 ｜ 昨收 174.33 → 收盘 174.33（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.83 | OI比 0.89 | ATM IV 41.4% | Skew 1.2pp | Term 1.11 | ExpMove ±4.6%（近端） | Rank — (历史不足)
量化视角： 期限结构正常（Term 1.11）｜保护溢价薄（Skew 1.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（4D）±4.6% ｜ 09-18（11D）±6.9% ｜ 09-25（18D）±8.5% ｜ 10-02（25D）±10.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,383,147 | GEX Change vs 上次快照 -363,694 | Flip: Primary Flip: 166.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 593 / LOW 87 / INVALID 172
结构观察区: Primary Flip 166.85（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 2.5%）
最近结构参考: Put Wall 170（现价高于该位 2.5%）
量化视角： 正 Gamma（3938万，无历史分位）｜正 Gamma 减弱（36万）｜现价位于 Flip 上方 4.49%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 172（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 187.5C — Vol 6,595 | 最新价 $0.58 | OI 5531→10405 (ΔOI +4874张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4874张（+88.1% vs前日OI），连续性待观察（方向未知）
09-11 175.0C — Vol 7,678 | 最新价 $3.69 | OI 5060→9197 (ΔOI +4137张) | ΔOI/Volume 53.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4137张（+81.8% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 6,326 | 最新价 $1.40 | OI 6428→10182 (ΔOI +3754张) | ΔOI/Volume 59.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3754张（+58.4% vs前日OI），连续性待观察（方向未知）
09-18 95.0P — Vol 3,714 | 最新价 $0.02 | OI 6059→9529 (ΔOI +3470张) | ΔOI/Volume 93.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3470张（+57.3% vs前日OI），连续性待观察（方向未知）
09-11 180.0C — Vol 9,416 | 最新价 $1.85 | OI 1728→4453 (ΔOI +2725张) | ΔOI/Volume 28.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2725张（+157.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,960 张（Put 7,224 / Call 11,736），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 11D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 106.0k / P 94.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.69 / P 4.33
隐含波动率 ATM IV:  41.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 172（结算参考） ｜ Call Wall 177.5（+1.8%，弱）（OI 10.7k）
量化解读： 存量两侧均衡｜ATM IV 41.4%｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 150（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 175（结算参考） ｜ Put Wall 170（-2.5%）（OI 7.4k）

10-02（Activity LOW）仓位参考: Max Pain 175（结算参考） ｜ Call Wall 180（+3.3%，弱）（OI 2.4k） ｜ Put Wall 160（-8.2%，弱）（OI 2.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/PLTR_evening.json