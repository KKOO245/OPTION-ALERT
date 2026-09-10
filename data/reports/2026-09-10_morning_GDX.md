# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $759.44 ｜ QQQ $711.26
VIX 17.34 ↑5.3%（5D +21.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 3.98 ｜ 前值 4.06　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-11 ATM IV 59.7% vs 09-18 48.7%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 99.47 → 今开 96.53（-3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 97.37 ｜ 低 95.62

Options: P/C成交量 2.89 | OI比 0.65 | ATM IV 59.7% | Skew 3.2pp | Term 0.76 | ExpMove ±2.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 3.2pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.65）+ 当日成交偏 Put（P/C量 2.89）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.89×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±2.8% ｜ 09-18（8D）±6.0% ｜ 09-25（15D）±9.7% ｜ 10-02（22D）±8.8%
   ⇒ IV–VIX Spread: +42.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -15,582,656 | GEX Change vs 上次快照 -67,182,552 | Flip: Primary Flip: 97.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 502 / LOW 168 / INVALID 280
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 97.63（全链重定价，覆盖 97%）
Call Wall 100（弱结构｜现价低于该位 2.9%）
最近结构参考: Flip 98（现价低于该位 0.6%）
量化视角： 负 Gamma（1558万，无历史分位）｜由正转负（6718万）｜现价位于 Flip 下方 0.58%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 98（MaxPain，仅结算参考） / 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 98（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 96.0P — Vol 9,681 | 最新价 $0.45 | OI 843→7880 (ΔOI +7037张) | ΔOI/Volume 72.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7037张（+834.8% vs前日OI），连续性待观察（方向未知）
09-11 103.0C — Vol 5,432 | 最新价 $0.53 | OI 6081→10310 (ΔOI +4229张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4229张（+69.5% vs前日OI），连续性待观察（方向未知）
09-11 97.0P — Vol 4,774 | 最新价 $0.69 | OI 565→4517 (ΔOI +3952张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3952张（+699.5% vs前日OI），连续性待观察（方向未知）
09-18 108.0C — Vol 3,926 | 最新价 $0.52 | OI 5663→9444 (ΔOI +3781张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3781张（+66.8% vs前日OI），连续性待观察（方向未知）
09-18 105.0C — Vol 3,834 | 最新价 $1.14 | OI 7871→10882 (ΔOI +3011张) | ΔOI/Volume 78.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3011张（+38.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,010 张（Put 10,989 / Call 11,021），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +8.3k / P +16.5k ｜ Activity HIGH ｜ 1D
09-18  C +7.3k / P -2.0k ｜ Activity HIGH ｜ 8D
09-25  C +74 / P -11 ｜ Activity MEDIUM △ ｜ 15D
10-02  C +0.3k / P +0.2k ｜ Activity LOW ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 113.7k / P 74.0k
今日变化ΔOI: C +8.3k / P +16.5k
平值价格ATM:  C 1.31 / P 1.43
隐含波动率 ATM IV:  59.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -553k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 96 ｜ +7,037 ｜ $0.93 ｜ 名义 $654.4k* ｜ -1.1%
C 103 ｜ +4,229 ｜ $0.06 ｜ 名义 $25.4k* ｜ +6.1%
P 97 ｜ +3,952 ｜ $1.43 ｜ 名义 $565.1k* ｜ -0.1%
结构参考：103（+6.1%） / 96（-1.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 98（结算参考） ｜ Call Wall 104（+7.2%，弱）（OI 18.2k） ｜ Put Wall 90（-7.3%，弱）（OI 11.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.7%｜历史 Rank 94%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 552,907 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 255.1k / P 416.7k
今日变化ΔOI: C +7.3k / P -2.0k
平值价格ATM:  C 2.95 / P 2.83
隐含波动率 ATM IV:  48.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 113k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 108 ｜ +3,781 ｜ $0.34 ｜ 名义 $128.6k* ｜ +11.3%
C 105 ｜ +3,011 ｜ $0.59 ｜ 名义 $177.6k* ｜ +8.2%
P 95 ｜ -1,370 ｜ $1.97 ｜ 名义 $-269.9k* ｜ -2.1%
结构参考：108（+11.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 90（结算参考） ｜ Call Wall 100（+3.0%，弱）（OI 23.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.7%｜历史 Rank 94%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 113,145 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 89P +39 ｜ 99P -33
09-25（MEDIUM △）仓位参考: Max Pain 96（结算参考） ｜ Call Wall 105（+8.2%）（OI 1.0k）

10-02（Activity LOW）仓位参考: Max Pain 99（结算参考） ｜ Put Wall 97（-0.1%）（OI 15.1k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 59.7% vs 09-18 48.7%（差 +11.0pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate YoY、Inflation Rate MoM、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/GDX_morning.json