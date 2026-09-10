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
🟡 **近现价集中开仓**: 09-11 159P ΔOI +3,224（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-11 159P ΔOI +3,224 占该期限总 OI 11.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 157.59 → 收盘 156.82（-0.5%） ｜ 今日高 158.70 ｜ 低 155.82 ｜ 昨收 159.38 → 收盘 156.82（-1.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 6.59 | OI比 2.51 | ATM IV 34.5% | Skew 1.0pp | Term 0.88 | ExpMove ±1.5%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜当日成交偏 Put（P/C量 6.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 6.59×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.51×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（1D）±1.5% ｜ 09-18（8D）±3.8% ｜ 09-25（15D）±4.7% ｜ 10-02（22D）±2.9%
   ⇒ IV–VIX Spread: +16.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -56,158,702 | GEX Change vs 上次快照 299,857 | Flip: Primary Flip: 164.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 405 / LOW 126 / INVALID 329
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.50（全链重定价，覆盖 95%）
Put Wall 155（弱结构｜现价高于该位 1.2%） | Call Wall 170（弱结构｜现价低于该位 7.8%）
最近结构参考: Put Wall 155（现价高于该位 1.2%）
量化视角： 负 Gamma（5616万，无历史分位）｜负 Gamma 缓解（+30万）｜现价位于 Flip 下方 4.67%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（Put Wall，弱结构）；上方 162（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 155.0P — Vol 1,704 | 最新价 $2.21 | OI 12360→15738 (ΔOI +3378张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3378张（+27.3% vs前日OI），连续性待观察（方向未知）
09-11 159.0P — Vol 3,826 | 最新价 $2.67 | OI 922→4146 (ΔOI +3224张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3224张（+349.7% vs前日OI），连续性待观察（方向未知）
09-25 154.0P — Vol 21 | 最新价 $2.39 | OI 99→1189 (ΔOI +1090张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1090张（+1101.0% vs前日OI），连续性待观察（方向未知）
09-11 161.0C — Vol 261 | 最新价 $0.08 | OI 193→1139 (ΔOI +946张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增946张（+490.2% vs前日OI），连续性待观察（方向未知）
09-11 157.5P — Vol 14 | 最新价 $1.48 | OI 77→762 (ΔOI +685张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增685张（+889.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,323 张（Put 8,377 / Call 946），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +1.0k / P +3.2k ｜ Activity HIGH ｜ 1D
09-18  C -0.5k / P +3.7k ｜ Activity HIGH ｜ 8D
09-25  C +49 / P +1.1k ｜ Activity HIGH ｜ 15D
10-02  C +47 / P -4 ｜ Activity LOW ｜ 22D

📆 09-11 Forward Structure
存量OI:      C 8.2k / P 20.5k
今日变化ΔOI: C +1.0k / P +3.2k
平值价格ATM:  C 1.06 / P 1.23
隐含波动率 ATM IV:  34.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -192k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 159 ｜ +3,224 ｜ $2.67 ｜ 名义 $860.8k* ｜ +1.4%
P 161 ｜ -962 ｜ $4.07 ｜ 名义 $-391.5k* ｜ +2.7%
C 161 ｜ +946 ｜ $0.08 ｜ 名义 $7.6k* ｜ +2.7%
结构参考：159（+1.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 162（结算参考） ｜ Call Wall 164（+4.6%，弱）（OI 1.6k） ｜ Put Wall 159（+1.4%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 34.5%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 191,817 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 70.6k / P 118.8k
今日变化ΔOI: C -0.5k / P +3.7k
平值价格ATM:  C 2.87 / P 3.10
隐含波动率 ATM IV:  32.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -156k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 155 ｜ +3,378 ｜ $2.21 ｜ 名义 $746.5k* ｜ -1.2%
P 161 ｜ +251 ｜ $5.21 ｜ 名义 $130.8k* ｜ +2.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：161（+2.7%） / 155（-1.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 158（结算参考） ｜ Call Wall 155（-1.2%，弱）（OI 10.8k） ｜ Put Wall 158（+0.8%，弱）（OI 16.8k）
量化解读： 存量 Put 重｜ATM IV 32.1%｜历史 Rank 58%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 155,804 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 3.0k / P 2.4k
今日变化ΔOI: C +49 / P +1.1k
平值价格ATM:  C 3.75 / P 3.60
隐含波动率 ATM IV:  30.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -38k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 154 ｜ +1,090 ｜ $2.39 ｜ 名义 $260.5k* ｜ -1.8%
C 150 ｜ +20 ｜ $10.74 ｜ 名义 $21.5k* ｜ -4.3%
C 149 ｜ +17 ｜ $12.45 ｜ 名义 $21.2k* ｜ -5.0%
结构参考：154（-1.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 160（结算参考） ｜ Call Wall 167（+6.5%）（OI 1.4k） ｜ Put Wall 154（-1.8%）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.0%｜历史 Rank 58%（近端代理）｜净 delta 敞口 负 38,106 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（Activity LOW）仓位参考: Max Pain 161（结算参考） ｜ Call Wall 165（+5.2%）（OI 0.2k） ｜ Put Wall 150（-4.3%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-10/XBI_evening.json