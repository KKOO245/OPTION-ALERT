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
🟡 **近现价集中开仓**: 09-25 145C ΔOI +590（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 142.80 → 今开 137.35（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 144.40 ｜ 低 137.07

Options: P/C成交量 0.65 | OI比 0.68 | ATM IV 70.8% | Skew -9.5pp | Term 1.04 | ExpMove ±7.8%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构正常（Term 1.04）｜Put 保护异常便宜（Skew -9.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（4D）±7.8% ｜ 09-18（11D）±11.5% ｜ 09-25（18D）±14.2% ｜ 10-02（25D）±16.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 95,388,415 | GEX Change vs 上次快照 10,013,171 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 918 / LOW 87 / INVALID 189
结构观察区: NO_CROSS
Call Wall 150（弱结构｜现价低于该位 4.9%）
最近结构参考: Call Wall 150（现价低于该位 4.9%）
量化视角： 正 Gamma（9539万，无历史分位）｜正 Gamma 增强（+1001万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 70.0P — Vol 13,849 | 最新价 $0.01 | OI 3685→17202 (ΔOI +13517张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13517张（+366.8% vs前日OI），连续性待观察（方向未知）
09-11 150.0C — Vol 19,791 | 最新价 $3.10 | OI 12012→24102 (ΔOI +12090张) | ΔOI/Volume 61.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12090张（+100.7% vs前日OI），连续性待观察（方向未知）
09-11 80.0P — Vol 10,121 | 最新价 $0.03 | OI 22554→32631 (ΔOI +10077张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10077张（+44.7% vs前日OI），连续性待观察（方向未知）
09-11 152.5C — Vol 9,223 | 最新价 $2.55 | OI 13965→20592 (ΔOI +6627张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6627张（+47.5% vs前日OI），连续性待观察（方向未知）
09-11 144.0C — Vol 12,475 | 最新价 $5.10 | OI 5143→11522 (ΔOI +6379张) | ΔOI/Volume 51.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6379张（+124.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 48,690 张（Put 23,594 / Call 25,096），跨 1 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +70.3k / P +45.2k ｜ Activity HIGH ｜ 4D
09-18  C +6.2k / P +6.4k ｜ Activity HIGH ｜ 11D
09-25  C +2.1k / P +2.5k ｜ Activity HIGH ｜ 18D
10-02  C +3.4k / P +1.7k ｜ Activity HIGH ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 227.2k / P 155.2k
今日变化ΔOI: C +70.3k / P +45.2k
平值价格ATM:  C 5.45 / P 5.72
隐含波动率 ATM IV:  70.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 2.7M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 150 ｜ +12,090 ｜ $3.10 ｜ 名义 $3.75M* ｜ +5.2%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：150（+5.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 130（结算参考） ｜ Call Wall 150（+5.2%，弱）（OI 24.1k）
量化解读： 存量 Call 重｜ATM IV 70.8%｜历史 Rank 30%（近端代理）｜净 delta 敞口 正 2,694,485 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 272.3k / P 199.9k
今日变化ΔOI: C +6.2k / P +6.4k
平值价格ATM:  C 7.20 / P 9.20
隐含波动率 ATM IV:  73.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 26k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +2,266 ｜ $0.55 ｜ 名义 $124.6k* ｜ +40.3%
C 165 ｜ +1,878 ｜ $2.56 ｜ 名义 $480.8k* ｜ +15.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：200（+40.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 108（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.5%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 25,964 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 19.2k / P 30.2k
今日变化ΔOI: C +2.1k / P +2.5k
平值价格ATM:  C 10.15 / P 10.06
隐含波动率 ATM IV:  72.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 35k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 160 ｜ +615 ｜ $4.85 ｜ 名义 $298.3k* ｜ +12.2%
C 145 ｜ +590 ｜ $9.55 ｜ 名义 $563.5k* ｜ +1.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：160（+12.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 125（结算参考） ｜ Call Wall 140（-1.8%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 72.7%｜历史 Rank 30%（近端代理）｜净 delta 敞口 正 34,859 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 19.0k / P 22.7k
今日变化ΔOI: C +3.4k / P +1.7k
平值价格ATM:  C 12.05 / P 11.30
隐含波动率 ATM IV:  72.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 108k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 145 ｜ +2,332 ｜ $10.80 ｜ 名义 $2.52M* ｜ +1.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：145（+1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 128（结算参考） ｜ Call Wall 145（+1.7%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.9%｜历史 Rank 30%（近端代理）｜净 delta 敞口 正 107,963 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/MSTR_morning.json