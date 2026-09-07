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
🟡 **近现价集中开仓**: 09-11 52P ΔOI +447（距现价 -4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 54.53 → 今开 56.57（+3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 58.52 ｜ 低 54.19

Options: P/C成交量 0.35 | OI比 0.81 | ATM IV 57.2% | Skew -3.9pp | Term 1.22 | ExpMove ±6.3%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构正常偏陡（Term 1.22）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（4D）±6.3% ｜ 09-18（11D）±9.4% ｜ 09-25（18D）±13.0% ｜ 10-02（25D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 223,501 | GEX Change vs 上次快照 -371,924 | Flip: Primary Flip: 54.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 277 / LOW 51 / INVALID 82
结构观察区: Primary Flip 54.33（全链重定价，覆盖 100%）
最近结构参考: Flip 54（现价高于该位 0.3%）
量化视角： 正 Gamma（22万，无历史分位）｜正 Gamma 减弱（37万）｜现价位于 Flip 上方 0.26%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 55.0C — Vol 1,017 | 最新价 $3.98 | OI 11→1013 (ΔOI +1002张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1002张（+9109.1% vs前日OI），连续性待观察（方向未知）
10-09 47.0P — Vol 1,004 | 最新价 $1.17 | OI 6→1007 (ΔOI +1001张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1001张（+16683.3% vs前日OI），连续性待观察（方向未知）
09-18 56.0C — Vol 950 | 最新价 $1.99 | OI 56→968 (ΔOI +912张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增912张（+1628.6% vs前日OI），连续性待观察（方向未知）
10-09 56.0C — Vol 850 | 最新价 $3.50 | OI 1→851 (ΔOI +850张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增850张（+85000.0% vs前日OI），连续性待观察（方向未知）
09-11 52.0P — Vol 464 | 最新价 $0.68 | OI 291→738 (ΔOI +447张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增447张（+153.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,212 张（Put 1,448 / Call 2,764），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +1.1k / P +1.4k ｜ Activity HIGH ｜ 4D
09-18  C +1.8k / P +0.1k ｜ Activity HIGH ｜ 11D
09-25  C +0.3k / P +82 ｜ Activity HIGH ｜ 18D
10-02  C +0.3k / P +31 ｜ Activity HIGH ｜ 25D

📆 09-11 Forward Structure
存量OI:      C 7.3k / P 5.9k
今日变化ΔOI: C +1.1k / P +1.4k
平值价格ATM:  C 2.00 / P 1.45
隐含波动率 ATM IV:  57.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 52 ｜ +447 ｜ $0.68 ｜ 名义 $30.4k* ｜ -4.5%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：52（-4.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 54（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.2%｜历史 Rank 31%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 11,020 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 49.6k / P 44.3k
今日变化ΔOI: C +1.8k / P +0.1k
平值价格ATM:  C 2.83 / P 2.29
隐含波动率 ATM IV:  58.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 72k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 56 ｜ +912 ｜ $1.99 ｜ 名义 $181.5k* ｜ +2.8%
C 59 ｜ +441 ｜ $1.17 ｜ 名义 $51.6k* ｜ +8.3%
C 57 ｜ +125 ｜ $1.70 ｜ 名义 $21.2k* ｜ +4.7%
结构参考：56（+2.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 55（结算参考） ｜ Put Wall 55（+1.0%，弱）（OI 9.1k）
量化解读： 存量两侧均衡｜ATM IV 58.6%｜历史 Rank 31%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 72,379 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 3.8k / P 3.8k
今日变化ΔOI: C +0.3k / P +82
平值价格ATM:  C 3.60 / P 3.49
隐含波动率 ATM IV:  63.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 58 ｜ +162 ｜ $2.23 ｜ 名义 $36.1k* ｜ +6.5%
C 56 ｜ +32 ｜ $2.73 ｜ 名义 $8.7k* ｜ +2.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：58（+6.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 52（结算参考）
量化解读： 存量两侧均衡｜ATM IV 63.2%｜历史 Rank 31%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,197 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 2.2k / P 2.8k
今日变化ΔOI: C +0.3k / P +31
平值价格ATM:  C 4.10 / P 3.45
隐含波动率 ATM IV:  62.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 6k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 59（结算参考） ｜ Put Wall 50（-8.2%）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.8%｜历史 Rank 31%（近端代理）｜净 delta 敞口 正 6,171 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-07/MP_morning.json