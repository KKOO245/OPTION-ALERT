# 期权晨报 2026-09-07（快照 12:20 ET）

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
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-11 17P ΔOI +599（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 17.61 → 今开 18.65（+5.9%） | 较昨收变动（含盘初走势） ｜ 今日高 19.30 ｜ 低 17.25

Options: P/C成交量 0.53 | OI比 0.34 | ATM IV 67.2% | Skew -4.8pp | Term 1.19 | ExpMove ±7.9%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构正常偏陡（Term 1.19）｜Put 保护异常便宜（Skew -4.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（4D）±7.9% ｜ 09-18（11D）±12.2% ｜ 09-25（18D）±14.7% ｜ 10-02（25D）±18.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,822,826 | GEX Change vs 上次快照 -1,881,081 | Flip: Primary Flip: 16.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 272 / LOW 78 / INVALID 126
结构观察区: Primary Flip 16.79（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 3.9%）
量化视角： 正 Gamma（382万，无历史分位）｜正 Gamma 减弱（188万）｜现价位于 Flip 上方 3.88%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 22.0C — Vol 1,397 | 最新价 $0.12 | OI 14393→15456 (ΔOI +1063张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1063张（+7.4% vs前日OI），连续性待观察（方向未知）
09-18 21.5C — Vol 852 | 最新价 $0.14 | OI 1575→2389 (ΔOI +814张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增814张（+51.7% vs前日OI），连续性待观察（方向未知）
09-18 22.5C — Vol 1,228 | 最新价 $0.09 | OI 878→1538 (ΔOI +660张) | ΔOI/Volume 53.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增660张（+75.2% vs前日OI），连续性待观察（方向未知）
09-11 17.0P — Vol 1,030 | 最新价 $0.39 | OI 966→1565 (ΔOI +599张) | ΔOI/Volume 58.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增599张（+62.0% vs前日OI），连续性待观察（方向未知）
09-11 19.0C — Vol 1,264 | 最新价 $0.24 | OI 493→1043 (ΔOI +550张) | ΔOI/Volume 43.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增550张（+111.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,686 张（Put 599 / Call 3,087），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +2.5k / P +2.0k ｜ Activity HIGH ｜ 4D
09-18  C +2.7k / P +0.5k ｜ Activity HIGH ｜ 11D
09-25  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 18D
10-02  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 19.0k / P 6.6k
今日变化ΔOI: C +2.5k / P +2.0k
平值价格ATM:  C 0.78 / P 0.60
隐含波动率 ATM IV:  67.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 29k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +599 ｜ $0.39 ｜ 名义 $23.4k* ｜ -2.5%
C 19 ｜ +550 ｜ $0.24 ｜ 名义 $13.2k* ｜ +9.0%
C 18 ｜ +437 ｜ $0.55 ｜ 名义 $24.0k* ｜ +3.2%
结构参考：19（+9.0%） / 17（-2.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 17（-2.5%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 67.2%｜历史 Rank 80%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 28,709 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 116.6k / P 64.4k
今日变化ΔOI: C +2.7k / P +0.5k
平值价格ATM:  C 1.11 / P 1.02
隐含波动率 ATM IV:  74.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 25k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 20（结算参考）
量化解读： 存量 Call 重｜ATM IV 74.4%｜历史 Rank 80%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 25,450 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 9.0k / P 3.2k
今日变化ΔOI: C +0.3k / P +0.2k
平值价格ATM:  C 1.30 / P 1.27
隐含波动率 ATM IV:  80.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 3k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考）
量化解读： 存量 Call 重｜ATM IV 80.1%｜历史 Rank 80%（近端代理）｜净 delta 敞口 正 3,023 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 7.2k / P 2.3k
今日变化ΔOI: C +0.2k / P +0.3k
平值价格ATM:  C 1.64 / P 1.61
隐含波动率 ATM IV:  81.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +146 ｜ $0.75 ｜ 名义 $10.9k* ｜ -8.2%
C 17 ｜ +76 ｜ $1.64 ｜ 名义 $12.5k* ｜ +0.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：17（+0.4%） / 16（-8.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.1%｜历史 Rank 80%（近端代理）｜净 delta 敞口 负 2,235 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/USAR_morning.json