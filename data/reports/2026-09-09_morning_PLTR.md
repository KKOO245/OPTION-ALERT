# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $763.57 ｜ QQQ $717.24
VIX 16.06 ↑2.2%（5D +5.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 40.9（fear）
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

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 170.30 → 今开 171.32（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 171.86 ｜ 低 168.61

Options: P/C成交量 0.47 | OI比 0.72 | ATM IV 53.6% | Skew -0.4pp | Term 0.89 | ExpMove ±3.3%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±3.3% ｜ 09-18（9D）±6.2% ｜ 09-25（16D）±8.0% ｜ 10-02（23D）±9.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,745,433 | GEX Change vs 上次快照 18,005,030 | Flip: Primary Flip: 166.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 569 / LOW 90 / INVALID 193
结构观察区: Primary Flip 166.01（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 0.5%）
最近结构参考: Put Wall 170（现价高于该位 0.5%）
量化视角： 正 Gamma（3875万，无历史分位）｜正 Gamma 增强（+1801万）｜现价位于 Flip 上方 2.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构）；上方 172（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 180.0C — Vol 21,967 | 最新价 $0.57 | OI 4453→15238 (ΔOI +10785张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10785张（+242.2% vs前日OI），连续性待观察（方向未知）
09-11 185.0C — Vol 14,123 | 最新价 $0.23 | OI 6768→13572 (ΔOI +6804张) | ΔOI/Volume 48.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6804张（+100.5% vs前日OI），连续性待观察（方向未知）
09-11 187.5C — Vol 12,413 | 最新价 $0.15 | OI 10405→16069 (ΔOI +5664张) | ΔOI/Volume 45.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5664张（+54.4% vs前日OI），连续性待观察（方向未知）
09-11 172.5C — Vol 11,515 | 最新价 $2.35 | OI 4803→9427 (ΔOI +4624张) | ΔOI/Volume 40.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4624张（+96.3% vs前日OI），连续性待观察（方向未知）
09-11 177.5C — Vol 8,300 | 最新价 $0.94 | OI 10730→14408 (ΔOI +3678张) | ΔOI/Volume 44.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3678张（+34.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 31,555 张（Put 0 / Call 31,555），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +41.7k / P +12.8k ｜ Activity HIGH ｜ 2D
09-18  C +6.1k / P +2.9k ｜ Activity HIGH ｜ 9D
09-25  C +1.6k / P +1.3k ｜ Activity HIGH ｜ 16D
10-02  C +0.6k / P -2.9k ｜ Activity HIGH ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 147.7k / P 106.9k
今日变化ΔOI: C +41.7k / P +12.8k
平值价格ATM:  C 3.20 / P 2.44
隐含波动率 ATM IV:  53.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 452k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +10,785 ｜ $0.45 ｜ 名义 $485.3k* ｜ +5.4%
C 185 ｜ +6,804 ｜ $0.17 ｜ 名义 $115.7k* ｜ +8.3%
C 187 ｜ +5,664 ｜ $0.12 ｜ 名义 $68.0k* ｜ +9.8%
结构参考：180（+5.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 172（结算参考） ｜ Call Wall 187.5（+9.8%，弱）（OI 16.1k）
量化解读： 存量 Call 重｜ATM IV 53.6%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 451,627 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 271.1k / P 239.5k
今日变化ΔOI: C +6.1k / P +2.9k
平值价格ATM:  C 5.70 / P 4.85
隐含波动率 ATM IV:  48.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 163k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +1,237 ｜ $2.07 ｜ 名义 $256.1k* ｜ +5.4%
P 157 ｜ +1,095 ｜ $1.12 ｜ 名义 $122.6k* ｜ -7.8%
C 187 ｜ +904 ｜ $0.94 ｜ 名义 $85.0k* ｜ +9.8%
结构参考：180（+5.4%） / 157（-7.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 150（结算参考）
量化解读： 存量两侧均衡｜ATM IV 48.7%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 163,147 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 21.0k / P 31.1k
今日变化ΔOI: C +1.6k / P +1.3k
平值价格ATM:  C 7.37 / P 6.35
隐含波动率 ATM IV:  47.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 72k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 160 ｜ -745 ｜ $2.48 ｜ 名义 $-184.8k* ｜ -6.3%
P 155 ｜ -525 ｜ $1.71 ｜ 名义 $-89.8k* ｜ -9.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 175（结算参考） ｜ Put Wall 170（-0.5%）（OI 7.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.7%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 71,935 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 15.4k / P 18.0k
今日变化ΔOI: C +0.6k / P -2.9k
平值价格ATM:  C 8.69 / P 7.32
隐含波动率 ATM IV:  47.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 94k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 157 ｜ -1,918 ｜ $3.40 ｜ 名义 $-652.1k* ｜ -7.8%
P 152 ｜ -423 ｜ $2.15 ｜ 名义 $-90.9k* ｜ -10.7%
P 155 ｜ -400 ｜ $2.45 ｜ 名义 $-98.0k* ｜ -9.3%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 175（结算参考） ｜ Call Wall 180（+5.4%，弱）（OI 2.5k） ｜ Put Wall 160（-6.3%，弱）（OI 2.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.5%｜净 delta 敞口 正 93,968 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/PLTR_morning.json