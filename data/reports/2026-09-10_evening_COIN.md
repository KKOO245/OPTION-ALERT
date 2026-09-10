# 期权晚报 2026-09-10（快照 17:04 ET）

📊 市场环境

SPY $757.83 ｜ QQQ $708.69
VIX 17.84 ↑8.4%（5D +24.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 3.98 ｜ 前值 4.06　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览
🟡 **事件差分**: 09-11 ATM IV 77.9% vs 09-18 67.2%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 170C ΔOI -4,567（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 170.84 → 收盘 172.28（+0.8%） ｜ 今日高 174.46 ｜ 低 170.39 ｜ 昨收 174.72 → 收盘 172.28（-1.4%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 0.35 | OI比 0.56 | ATM IV 77.9% | Skew -9.6pp | Term 0.85 | ExpMove ±3.1%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.1% ｜ 09-18（8D）±8.1% ｜ 09-25（15D）±10.9% ｜ 10-02（22D）±12.7%
   ⇒ IV–VIX Spread: +60.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,832,836 | GEX Change vs 上次快照 956,466 | Flip: Primary Flip: 167.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 515 / LOW 169 / INVALID 324
结构观察区: Primary Flip 167.14（全链重定价，覆盖 98%）
Put Wall 160（弱结构｜现价高于该位 7.7%）
最近结构参考: Flip 167（现价高于该位 3.1%）
量化视角： 正 Gamma（983万，无历史分位）｜正 Gamma 增强（+96万）｜现价位于 Flip 上方 3.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（Put Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 182.5C — Vol 5,075 | 最新价 $3.65 | OI 280→4373 (ΔOI +4093张) | ΔOI/Volume 80.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4093张（+1461.8% vs前日OI），连续性待观察（方向未知）
09-18 192.5C — Vol 574 | 最新价 $1.62 | OI 379→4278 (ΔOI +3899张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3899张（+1028.8% vs前日OI），连续性待观察（方向未知）
09-18 185.0C — Vol 4,019 | 最新价 $2.88 | OI 1835→5721 (ΔOI +3886张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3886张（+211.8% vs前日OI），连续性待观察（方向未知）
09-18 190.0C — Vol 3,102 | 最新价 $1.97 | OI 3798→7298 (ΔOI +3500张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3500张（+92.2% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 991 | 最新价 $2.11 | OI 7930→9830 (ΔOI +1900张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1900张（+24.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,278 张（Put 1,900 / Call 15,378），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C -2.9k / P +2.0k ｜ Activity HIGH ｜ 1D
09-18  C +11.3k / P +6.5k ｜ Activity HIGH ｜ 8D
09-25  C +0.6k / P +0.3k ｜ Activity HIGH ｜ 15D
10-02  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 58.3k / P 32.9k
今日变化ΔOI: C -2.9k / P +2.0k
平值价格ATM:  C 2.55 / P 2.87
隐含波动率 ATM IV:  77.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -36k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 180（结算参考） ｜ Call Wall 180（+4.5%，弱）（OI 7.0k） ｜ Put Wall 175（+1.6%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.9%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 35,570 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 188.4k / P 97.8k
今日变化ΔOI: C +11.3k / P +6.5k
平值价格ATM:  C 7.30 / P 6.60
隐含波动率 ATM IV:  67.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -153k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 170 ｜ -4,567 ｜ $8.77 ｜ 名义 $-4.01M* ｜ -1.3%
C 182 ｜ +4,093 ｜ $3.65 ｜ 名义 $1.49M* ｜ +5.9%
C 192 ｜ +3,899 ｜ $1.62 ｜ 名义 $631.6k* ｜ +11.7%
结构参考：182（+5.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 175（结算参考） ｜ Call Wall 170（-1.3%，弱）（OI 11.5k） ｜ Put Wall 160（-7.1%，弱）（OI 9.8k）
量化解读： 存量 Call 重｜ATM IV 67.2%｜历史 Rank 54%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 152,716 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 10.8k / P 8.8k
今日变化ΔOI: C +0.6k / P +0.3k
平值价格ATM:  C 9.89 / P 8.90
隐含波动率 ATM IV:  63.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 18k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +383 ｜ $6.55 ｜ 名义 $250.9k* ｜ +4.5%
C 190 ｜ +199 ｜ $3.74 ｜ 名义 $74.4k* ｜ +10.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：180（+4.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Call Wall 185（+7.4%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 63.8%｜历史 Rank 54%（近端代理）｜净 delta 敞口 正 17,858 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 180C +202 ｜ 175C +51
10-02（MEDIUM △）仓位参考: Max Pain 188（结算参考） ｜ Put Wall 172.5（+0.1%，弱）（OI 1.1k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 77.9% vs 09-18 67.2%（差 +10.7pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/COIN_evening.json