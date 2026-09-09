# 期权晨报 2026-09-09（快照 11:03 ET）

📊 市场环境

SPY $762.70 ｜ QQQ $716.31
VIX 16.06 ↑2.2%（5D +5.7%） ｜ Vol Regime: NORMAL
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

🔍 重点速览
🟡 **近现价集中开仓**: 09-11 510P ΔOI +719（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 480P ΔOI +1,799 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 528.40 → 今开 525.85（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 535.48 ｜ 低 525.27

Options: P/C成交量 2.69 | OI比 1.39 | ATM IV 46.6% | Skew 2.2pp | Term 0.86 | ExpMove ±2.9%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜当日成交偏 Put（P/C量 2.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.69×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.39×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±2.9% ｜ 09-18（9D）±5.6% ｜ 09-25（16D）±8.8% ｜ 10-02（23D）±9.2%
   ⇒ IV–VIX Spread: +30.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,581,430 | GEX Change vs 上次快照 14,246,793 | Flip: Primary Flip: 522.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 628 / LOW 336 / INVALID 616
结构观察区: Primary Flip 522.80（全链重定价，覆盖 100%）
Call Wall 575（弱结构｜现价低于该位 7.3%）
最近结构参考: Flip 523（现价高于该位 1.9%）
量化视角： 正 Gamma（1558万，无历史分位）｜正 Gamma 增强（+1425万）｜现价位于 Flip 上方 1.94%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 510（MaxPain，仅结算参考）；上方 575（Call Wall，弱结构）。
• Gamma 区域：切换参考 523（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 560.0C — Vol 14,276 | 最新价 $4.10 | OI 1571→14572 (ΔOI +13001张) | ΔOI/Volume 91.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13001张（+827.6% vs前日OI），连续性待观察（方向未知）
09-18 535.0C — Vol 3,735 | 最新价 $11.38 | OI 130→3671 (ΔOI +3541张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3541张（+2723.8% vs前日OI），连续性待观察（方向未知）
10-02 542.5C — Vol 2,802 | 最新价 $15.34 | OI 1→2801 (ΔOI +2800张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2800张（+280000.0% vs前日OI），连续性待观察（方向未知）
09-25 480.0P — Vol 2,040 | 最新价 $3.40 | OI 103→1902 (ΔOI +1799张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1799张（+1746.6% vs前日OI），连续性待观察（方向未知）
10-02 475.0P — Vol 1,404 | 最新价 $5.31 | OI 85→1466 (ΔOI +1381张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1381张（+1624.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,522 张（Put 3,180 / Call 19,342），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.6k / P +2.4k ｜ Activity HIGH ｜ 2D
09-18  C +17.1k / P +2.5k ｜ Activity HIGH ｜ 9D
09-25  C +0.4k / P +2.7k ｜ Activity HIGH ｜ 16D
10-02  C +2.8k / P +1.5k ｜ Activity HIGH ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 13.6k / P 18.9k
今日变化ΔOI: C +0.6k / P +2.4k
平值价格ATM:  C 6.80 / P 8.37
隐含波动率 ATM IV:  46.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -27k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 490 ｜ +778 ｜ $0.53 ｜ 名义 $41.2k* ｜ -8.1%
P 510 ｜ +719 ｜ $2.45 ｜ 名义 $176.2k* ｜ -4.3%
P 530 ｜ +180 ｜ $9.50 ｜ 名义 $171.0k* ｜ -0.5%
结构参考：490（-8.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 510（结算参考） ｜ Call Wall 530（-0.5%）（OI 3.2k） ｜ Put Wall 500（-6.2%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 46.6%｜历史 Rank 82%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,262 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 100.7k / P 93.2k
今日变化ΔOI: C +17.1k / P +2.5k
平值价格ATM:  C 14.83 / P 14.80
隐含波动率 ATM IV:  44.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 405k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 560 ｜ +13,001 ｜ $4.10 ｜ 名义 $5.33M* ｜ +5.1%
C 535 ｜ +3,541 ｜ $11.38 ｜ 名义 $4.03M* ｜ +0.4%
P 500 ｜ +1,087 ｜ $4.90 ｜ 名义 $532.6k* ｜ -6.2%
结构参考：560（+5.1%） / 500（-6.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 525（结算参考） ｜ Call Wall 575（+7.9%，弱）（OI 15.9k）
量化解读： 存量两侧均衡｜ATM IV 44.5%｜历史 Rank 82%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 405,093 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 8.2k / P 8.9k
今日变化ΔOI: C +0.4k / P +2.7k
平值价格ATM:  C 17.86 / P 29.22
隐含波动率 ATM IV:  40.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -19k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 480 ｜ +1,799 ｜ $3.40 ｜ 名义 $611.7k* ｜ -9.9%
P 490 ｜ +718 ｜ $5.70 ｜ 名义 $409.3k* ｜ -8.1%
C 580 ｜ +272 ｜ $3.94 ｜ 名义 $107.2k* ｜ +8.8%
结构参考：580（+8.8%） / 480（-9.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 530（结算参考） ｜ Call Wall 580（+8.8%，弱）（OI 2.2k） ｜ Put Wall 480（-9.9%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜ATM IV 40.9%｜历史 Rank 82%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,518 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 10.6k / P 8.2k
今日变化ΔOI: C +2.8k / P +1.5k
平值价格ATM:  C 20.87 / P 28.40
隐含波动率 ATM IV:  40.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 100k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 542 ｜ +2,800 ｜ $15.34 ｜ 名义 $4.30M* ｜ +1.8%
P 475 ｜ +1,381 ｜ $5.31 ｜ 名义 $733.3k* ｜ -10.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：542（+1.8%） / 475（-10.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 520（结算参考） ｜ Call Wall 542.5（+1.8%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 40.6%｜历史 Rank 82%（近端代理）｜净 delta 敞口 正 100,079 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/SOXX_morning.json