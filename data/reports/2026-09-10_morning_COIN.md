# 期权晨报 2026-09-10（快照 10:56 ET）

📊 市场环境

SPY $759.44 ｜ QQQ $711.33
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
🟡 **近现价集中开仓**: 09-18 170C ΔOI -4,567（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 174.72 → 今开 170.84（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 174.46 ｜ 低 170.39

Options: P/C成交量 0.23 | OI比 0.56 | ATM IV 75.2% | Skew -6.6pp | Term 0.89 | ExpMove ±3.4%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±3.4% ｜ 09-18（8D）±8.1% ｜ 09-25（15D）±10.7% ｜ 10-02（22D）±12.8%
   ⇒ IV–VIX Spread: +57.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,876,370 | GEX Change vs 上次快照 -6,006,202 | Flip: Primary Flip: 167.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 530 / LOW 165 / INVALID 313
结构观察区: Primary Flip 167.93（全链重定价，覆盖 100%）
Put Wall 160（弱结构｜现价高于该位 7.9%）
最近结构参考: Flip 168（现价高于该位 2.8%）
量化视角： 正 Gamma（888万，无历史分位）｜正 Gamma 减弱（601万）｜现价位于 Flip 上方 2.81%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（Put Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 168（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 182.5C — Vol 4,387 | 最新价 $4.54 | OI 280→4373 (ΔOI +4093张) | ΔOI/Volume 93.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4093张（+1461.8% vs前日OI），连续性待观察（方向未知）
09-18 192.5C — Vol 4,136 | 最新价 $2.33 | OI 379→4278 (ΔOI +3899张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3899张（+1028.8% vs前日OI），连续性待观察（方向未知）
09-18 185.0C — Vol 5,867 | 最新价 $3.92 | OI 1835→5721 (ΔOI +3886张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3886张（+211.8% vs前日OI），连续性待观察（方向未知）
09-18 190.0C — Vol 4,397 | 最新价 $2.75 | OI 3798→7298 (ΔOI +3500张) | ΔOI/Volume 79.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3500张（+92.2% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 2,636 | 最新价 $1.82 | OI 7930→9830 (ΔOI +1900张) | ΔOI/Volume 72.1% | Magnitude: HIGH | 完整度: HIGH
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
平值价格ATM:  C 3.05 / P 2.81
隐含波动率 ATM IV:  75.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -28k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 190 ｜ -1,964 ｜ $0.15 ｜ 名义 $-29.5k* ｜ +10.0%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 180（结算参考） ｜ Call Wall 180（+4.3%，弱）（OI 7.0k） ｜ Put Wall 175（+1.4%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 75.2%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,995 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 188.4k / P 97.8k
今日变化ΔOI: C +11.3k / P +6.5k
平值价格ATM:  C 7.18 / P 6.74
隐含波动率 ATM IV:  66.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -139k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 170 ｜ -4,567 ｜ $8.40 ｜ 名义 $-3.84M* ｜ -1.5%
C 182 ｜ +4,093 ｜ $3.53 ｜ 名义 $1.44M* ｜ +5.7%
C 192 ｜ +3,899 ｜ $1.66 ｜ 名义 $647.2k* ｜ +11.5%
结构参考：182（+5.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 175（结算参考） ｜ Call Wall 170（-1.5%，弱）（OI 11.5k） ｜ Put Wall 160（-7.3%，弱）（OI 9.8k）
量化解读： 存量 Call 重｜ATM IV 66.6%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 139,176 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 10.8k / P 8.8k
今日变化ΔOI: C +0.6k / P +0.3k
平值价格ATM:  C 9.46 / P 8.93
隐含波动率 ATM IV:  66.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 19k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +383 ｜ $6.50 ｜ 名义 $248.9k* ｜ +4.3%
C 190 ｜ +199 ｜ $3.79 ｜ 名义 $75.4k* ｜ +10.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：180（+4.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Call Wall 185（+7.2%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 66.2%｜历史 Rank 46%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,776 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 180C +202 ｜ 175C +51
10-02（MEDIUM △）仓位参考: Max Pain 188（结算参考） ｜ Put Wall 172.5（-0.1%，弱）（OI 1.1k）

📅 事件差分（观察，非因果）: 09-11（1D）ATM IV 75.2% vs 09-18 66.6%（差 +8.6pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate YoY、Inflation Rate MoM、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/COIN_morning.json