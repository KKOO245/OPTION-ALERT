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


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 171.32 → 收盘 169.53（-1.0%） ｜ 今日高 171.86 ｜ 低 168.61 ｜ 昨收 170.30 → 收盘 169.53（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.72 | ATM IV 52.9% | Skew -0.4pp | Term 0.89 | ExpMove ±3.1%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±3.1% ｜ 09-18（9D）±6.0% ｜ 09-25（16D）±7.8% ｜ 10-02（23D）±9.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,629,708 | GEX Change vs 上次快照 -9,115,725 | Flip: Primary Flip: 165.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 593 / LOW 106 / INVALID 153
结构观察区: Primary Flip 165.79（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价低于该位 0.3%）
最近结构参考: Put Wall 170（现价低于该位 0.3%）
量化视角： 正 Gamma（2963万，无历史分位）｜正 Gamma 减弱（912万）｜现价位于 Flip 上方 2.26%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（Put Wall，弱结构） / 172（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 180.0C — Vol 16,626 | 最新价 $0.29 | OI 4453→15238 (ΔOI +10785张) | ΔOI/Volume 64.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10785张（+242.2% vs前日OI），连续性待观察（方向未知）
09-11 185.0C — Vol 4,802 | 最新价 $0.11 | OI 6768→13572 (ΔOI +6804张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6804张（+100.5% vs前日OI），连续性待观察（方向未知）
09-11 187.5C — Vol 7,712 | 最新价 $0.09 | OI 10405→16069 (ΔOI +5664张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5664张（+54.4% vs前日OI），连续性待观察（方向未知）
09-11 172.5C — Vol 16,843 | 最新价 $1.49 | OI 4803→9427 (ΔOI +4624张) | ΔOI/Volume 27.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4624张（+96.3% vs前日OI），连续性待观察（方向未知）
09-11 177.5C — Vol 9,705 | 最新价 $0.49 | OI 10730→14408 (ΔOI +3678张) | ΔOI/Volume 37.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3678张（+34.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 31,555 张（Put 0 / Call 31,555），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 147.7k / P 106.9k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.45 / P 2.87
隐含波动率 ATM IV:  52.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 172（结算参考）
量化解读： 存量 Call 重｜ATM IV 52.9%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 150（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 175（结算参考） ｜ Put Wall 170（+0.3%）（OI 7.4k）

10-02（Activity LOW）仓位参考: Max Pain 175（结算参考） ｜ Call Wall 180（+6.2%，弱）（OI 2.5k） ｜ Put Wall 160（-5.6%，弱）（OI 2.6k）

📅 事件差分（观察，非因果）: 09-11（2D）ATM IV 52.9% vs 09-18 47.7%（差 +5.2pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/PLTR_evening.json