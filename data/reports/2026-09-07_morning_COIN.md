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
🟡 **近现价集中开仓**: 09-11 192C ΔOI +3,399（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 184.64 → 今开 184.97（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 189.00 ｜ 低 182.87

Options: P/C成交量 0.48 | OI比 0.50 | ATM IV 59.6% | Skew -6.5pp | Term 1.10 | ExpMove ±6.7%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 1.10）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（4D）±6.7% ｜ 09-18（11D）±9.9% ｜ 09-25（18D）±12.1% ｜ 10-02（25D）±13.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 25,658,948 | GEX Change vs 上次快照 -4,293,467 | Flip: Primary Flip: 163.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 542 / LOW 155 / INVALID 275
结构观察区: Primary Flip 163.92（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价高于该位 8.7%）
最近结构参考: Call Wall 170（现价高于该位 8.7%）
量化视角： 正 Gamma（2566万，无历史分位）｜正 Gamma 减弱（429万）｜现价位于 Flip 上方 12.74%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 195.0C — Vol 5,333 | 最新价 $2.73 | OI 1552→5923 (ΔOI +4371张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4371张（+281.6% vs前日OI），连续性待观察（方向未知）
09-11 192.5C — Vol 3,920 | 最新价 $3.35 | OI 492→3891 (ΔOI +3399张) | ΔOI/Volume 86.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3399张（+690.9% vs前日OI），连续性待观察（方向未知）
09-11 187.5C — Vol 8,258 | 最新价 $4.75 | OI 5058→6448 (ΔOI +1390张) | ΔOI/Volume 16.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1390张（+27.5% vs前日OI），连续性待观察（方向未知）
09-11 185.0P — Vol 2,281 | 最新价 $6.40 | OI 650→1808 (ΔOI +1158张) | ΔOI/Volume 50.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1158张（+178.2% vs前日OI），连续性待观察（方向未知）
10-02 187.5C — Vol 1,192 | 最新价 $12.65 | OI 126→1054 (ΔOI +928张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增928张（+736.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,246 张（Put 1,158 / Call 10,088），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +12.4k / P +7.6k ｜ Activity HIGH ｜ 4D
09-18  C +0.9k / P +2.9k ｜ Activity HIGH ｜ 11D
09-25  C +0.8k / P +0.7k ｜ Activity HIGH ｜ 18D
10-02  C +1.3k / P +0.6k ｜ Activity HIGH ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 55.3k / P 27.6k
今日变化ΔOI: C +12.4k / P +7.6k
平值价格ATM:  C 5.95 / P 6.40
隐含波动率 ATM IV:  59.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 226k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 195 ｜ +4,371 ｜ $2.73 ｜ 名义 $1.19M* ｜ +5.5%
C 192 ｜ +3,399 ｜ $3.35 ｜ 名义 $1.14M* ｜ +4.2%
C 187 ｜ +1,390 ｜ $4.75 ｜ 名义 $660.2k* ｜ +1.5%
结构参考：195（+5.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 180（结算参考） ｜ Call Wall 187.5（+1.5%，弱）（OI 6.4k）
量化解读： 存量 Call 重｜ATM IV 59.6%｜历史 Rank 10%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 225,638 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 176.4k / P 89.8k
今日变化ΔOI: C +0.9k / P +2.9k
平值价格ATM:  C 9.10 / P 9.20
隐含波动率 ATM IV:  63.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 32k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Call Wall 170（-8.0%）（OI 16.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 63.4%｜历史 Rank 10%（近端代理）｜净 delta 敞口 正 32,043 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 9.4k / P 8.1k
今日变化ΔOI: C +0.8k / P +0.7k
平值价格ATM:  C 11.30 / P 11.00
隐含波动率 ATM IV:  63.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 33k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 185 ｜ +540 ｜ $11.30 ｜ 名义 $610.2k* ｜ +0.1%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：185（+0.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Call Wall 185（+0.1%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜ATM IV 63.7%｜历史 Rank 10%（近端代理）｜净 delta 敞口 正 33,105 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 8.5k / P 10.5k
今日变化ΔOI: C +1.3k / P +0.6k
平值价格ATM:  C 12.95 / P 12.37
隐含波动率 ATM IV:  63.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 48k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 187 ｜ +928 ｜ $12.65 ｜ 名义 $1.17M* ｜ +1.5%
P 170 ｜ +179 ｜ $6.50 ｜ 名义 $116.3k* ｜ -8.0%
C 200 ｜ +117 ｜ $7.80 ｜ 名义 $91.3k* ｜ +8.2%
结构参考：187（+1.5%） / 170（-8.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 188（结算参考） ｜ Put Wall 172.5（-6.7%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.7%｜历史 Rank 10%（近端代理）｜净 delta 敞口 正 48,285 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/COIN_morning.json