# 期权晚报 2026-09-07（快照 16:40 ET）

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

🔍 重点速览
🟡 **近现价集中开仓**: 09-11 17P ΔOI +117（距现价 -4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 17.75 → 收盘 17.72（-0.2%） ｜ 今日高 18.01 ｜ 低 17.20 ｜ 昨收 17.72 → 收盘 17.72（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.05 | OI比 0.95 | ATM IV 62.3% | Skew -2.9pp | Term 1.23 | ExpMove ±6.5%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常偏陡（Term 1.23）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.05）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.05×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（4D）±6.5% ｜ 09-18（11D）±10.6% ｜ 09-25（18D）±13.2% ｜ 10-02（25D）±16.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 914,611 | GEX Change vs 上次快照 25,758 | Flip: Primary Flip: 16.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 229 / LOW 87 / INVALID 124
结构观察区: Primary Flip 16.96（全链重定价，覆盖 98%）
最近结构参考: Flip 17（现价高于该位 4.5%）
量化视角： 正 Gamma（91万，无历史分位）｜正 Gamma 增强（+3万）｜现价位于 Flip 上方 4.45%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 16.0P — Vol 365 | 最新价 $0.10 | OI 460→808 (ΔOI +348张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增348张（+75.7% vs前日OI），连续性待观察（方向未知）
09-11 17.0P — Vol 121 | 最新价 $0.30 | OI 156→273 (ΔOI +117张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增117张（+75.0% vs前日OI），连续性待观察（方向未知）
09-11 19.0C — Vol 90 | 最新价 $0.17 | OI 129→217 (ΔOI +88张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增88张（+68.2% vs前日OI），连续性待观察（方向未知）
09-11 18.5C — Vol 81 | 最新价 $0.29 | OI 100→180 (ΔOI +80张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增80张（+80.0% vs前日OI），连续性待观察（方向未知）
09-11 18.0C — Vol 80 | 最新价 $0.48 | OI 76→138 (ΔOI +62张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增62张（+81.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 695 张（Put 465 / Call 230），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.3k / P +0.6k ｜ Activity HIGH ｜ 4D
09-18  C +66 / P +23 ｜ Activity MEDIUM △ ｜ 11D
09-25  C +44 / P +35 ｜ Activity MEDIUM △ ｜ 18D
10-02  C +32 / P +52 ｜ Activity HIGH ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 3.0k / P 2.8k
今日变化ΔOI: C +0.3k / P +0.6k
平值价格ATM:  C 0.67 / P 0.49
隐含波动率 ATM IV:  62.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +348 ｜ $0.10 ｜ 名义 $3.5k* ｜ -9.7%
P 17 ｜ +117 ｜ $0.30 ｜ 名义 $3.5k* ｜ -4.1%
C 19 ｜ +88 ｜ $0.17 ｜ 名义 $1.5k* ｜ +7.2%
结构参考：19（+7.2%） / 16（-9.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Put Wall 16（-9.7%）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 62.3%｜历史 Rank 60%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,547 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 18C +39 ｜ 19C +34
09-18（MEDIUM △）仓位参考: Max Pain 19（结算参考） ｜ Put Wall 18（+1.6%）（OI 0.7k）

09-25（MEDIUM △）Top ΔOI: 19C +7
09-25（MEDIUM △）仓位参考: Max Pain 19（结算参考）

📆 10-02 Forward Structure
存量OI:      C 2.5k / P 0.6k
今日变化ΔOI: C +32 / P +52
平值价格ATM:  C 1.48 / P 1.41
隐含波动率 ATM IV:  74.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Put Wall 17（-4.1%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.1%｜历史 Rank 60%（近端代理）｜净 delta 敞口 负 2,288 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/NNE_evening.json