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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 98.75 → 收盘 99.26（+0.5%） ｜ 今日高 100.10 ｜ 低 98.01 ｜ 昨收 99.26 → 收盘 99.26（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.36 | OI比 0.52 | ATM IV 40.8% | Skew -0.4pp | Term 1.08 | ExpMove ±4.5%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -0.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（4D）±4.5% ｜ 09-18（11D）±6.9% ｜ 09-25（18D）±8.2% ｜ 10-02（25D）±9.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 42,890,184 | GEX Change vs 上次快照 0 | Flip: Primary Flip: 96.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 644 / LOW 141 / INVALID 165
结构观察区: Primary Flip 96.88（全链重定价，覆盖 100%）
Call Wall 100（弱结构｜现价低于该位 0.7%）
最近结构参考: Call Wall 100（现价低于该位 0.7%）
量化视角： 正 Gamma（4289万，无历史分位）｜正 Gamma 减弱（0万）｜现价位于 Flip 上方 2.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 98（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 97（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 101.0C — Vol 16,830 | 最新价 $1.56 | OI 481→16228 (ΔOI +15747张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15747张（+3273.8% vs前日OI），连续性待观察（方向未知）
09-11 104.0C — Vol 15,863 | 最新价 $0.65 | OI 3406→17123 (ΔOI +13717张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13717张（+402.7% vs前日OI），连续性待观察（方向未知）
09-11 102.0C — Vol 9,329 | 最新价 $1.16 | OI 5513→14014 (ΔOI +8501张) | ΔOI/Volume 91.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8501张（+154.2% vs前日OI），连续性待观察（方向未知）
09-11 106.0C — Vol 7,885 | 最新价 $0.39 | OI 5226→11833 (ΔOI +6607张) | ΔOI/Volume 83.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6607张（+126.4% vs前日OI），连续性待观察（方向未知）
09-11 95.0P — Vol 5,548 | 最新价 $0.64 | OI 2164→6659 (ΔOI +4495张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4495张（+207.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 49,067 张（Put 4,495 / Call 44,572），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 11D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 102.6k / P 52.8k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.39 / P 2.10
隐含波动率 ATM IV:  40.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 98（结算参考） ｜ Call Wall 104（+4.8%，弱）（OI 17.1k） ｜ Put Wall 90（-9.3%，弱）（OI 9.8k）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 62%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 90（结算参考） ｜ Call Wall 100（+0.7%，弱）（OI 23.8k）

09-25（Activity LOW）仓位参考: Max Pain 96（结算参考） ｜ Call Wall 105（+5.8%，弱）（OI 0.7k）

10-02（Activity LOW）仓位参考: Max Pain 99（结算参考） ｜ Put Wall 97（-2.3%）（OI 15.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/GDX_evening.json