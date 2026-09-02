# 期权晚报 2026-09-02（快照 17:13 ET）

📊 市场环境

SPY $765.16 ｜ QQQ $709.24
VIX 15.20 ↓7.0%（5D -1.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-03 760P ΔOI +2,480（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 762.45 → 收盘 765.16（+0.4%） ｜ 今日高 766.43 ｜ 低 761.73
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-09，窗口结束前不做对错判定）

Options: P/C成交量 1.19 | OI比 1.58 | ATM IV 34.3% | Skew -1.8pp | Term 0.35 | ExpMove ±0.5%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.35，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.19）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.19×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.58×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 45% ｜ P/C OI(近端) 29%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 45%）｜近端持仓结构中性（P/C OI 分位 29%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-03（1D）±0.5% ｜ 09-04（2D）±0.7% ｜ 09-08（6D）±1.0% ｜ 09-09（7D）±1.1%
   ⇒ IV–VIX Spread: +19.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -469,006,944 | GEX Change vs 上次快照 -102,882,721 | Flip: Primary Flip: 768.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 2583 / LOW 666 / INVALID 1799
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.67（全链重定价，覆盖 92%）
Call Wall 800（弱结构｜现价低于该位 4.4%）
最近结构参考: Flip 769（现价低于该位 0.5%）
量化视角： 负 Gamma（4.69亿，历史分位 45%，中性区）｜负 Gamma 加深（1.03亿）｜现价位于 Flip 下方 0.46%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 769（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-02 729.0P — Vol 12,170 | 最新价 $0.01 | OI 72→13019 (ΔOI +12947张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12947张（+17981.9% vs前日OI），连续性待观察（方向未知）
09-02 765.0C — Vol 565,376 | 最新价 $0.95 | OI 1921→12261 (ΔOI +10340张) | ΔOI/Volume 1.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10340张（+538.3% vs前日OI），连续性待观察（方向未知）
09-11 739.0P — Vol 353 | 最新价 $0.59 | OI 1098→10769 (ΔOI +9671张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9671张（+880.8% vs前日OI），连续性待观察（方向未知）
09-02 759.0P — Vol 163,240 | 最新价 $0.01 | OI 740→10130 (ΔOI +9390张) | ΔOI/Volume 5.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9390张（+1268.9% vs前日OI），连续性待观察（方向未知）
09-30 700.0P — Vol 3,799 | 最新价 $1.14 | OI 8516→17670 (ΔOI +9154张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9154张（+107.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 51,502 张（Put 41,162 / Call 10,340），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜彩票/名义 2 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-03  C +21.1k / P +18.4k ｜ Activity HIGH ｜ 1D
09-04  C +25.5k / P +3.4k ｜ Activity HIGH ｜ 2D
09-08  C +11.5k / P +12.4k ｜ Activity HIGH ｜ 6D
09-09  C +8.3k / P +10.0k ｜ Activity HIGH ｜ 7D

📆 09-03 Forward Structure
存量OI:      C 69.2k / P 84.9k
今日变化ΔOI: C +21.1k / P +18.4k
平值价格ATM:  C 2.21 / P 1.70
隐含波动率 ATM IV:  12.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 869k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 760 ｜ +2,480 ｜ $0.42 ｜ 名义 $104.2k* ｜ -0.7%
C 766 ｜ +2,458 ｜ $1.68 ｜ 名义 $412.9k* ｜ +0.1%
C 765 ｜ +2,390 ｜ $2.21 ｜ 名义 $528.2k* ｜ -0.0%
结构参考：766（+0.1%） / 760（-0.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.2%｜历史 Rank 98%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 869,118 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-04 Forward Structure
存量OI:      C 355.1k / P 386.2k
今日变化ΔOI: C +25.5k / P +3.4k
平值价格ATM:  C 3.25 / P 2.40
隐含波动率 ATM IV:  12.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 2.6M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 765 ｜ -11,356 ｜ $2.40 ｜ 名义 $-2.73M* ｜ -0.0%
P 747 ｜ -6,794 ｜ $0.09 ｜ 名义 $-61.1k* ｜ -2.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.0%｜历史 Rank 98%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,571,225 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-08 Forward Structure
存量OI:      C 45.2k / P 43.3k
今日变化ΔOI: C +11.5k / P +12.4k
平值价格ATM:  C 4.14 / P 3.23
隐含波动率 ATM IV:  9.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 328k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 780 ｜ +1,698 ｜ $0.10 ｜ 名义 $17.0k* ｜ +1.9%
C 775 ｜ +1,224 ｜ $0.51 ｜ 名义 $62.4k* ｜ +1.3%
P 736 ｜ +1,096 ｜ $0.12 ｜ 名义 $13.2k* ｜ -3.8%
结构参考：780（+1.9%） / 736（-3.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 9.4%｜历史 Rank 98%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 327,912 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-09 Forward Structure
存量OI:      C 26.0k / P 30.4k
今日变化ΔOI: C +8.3k / P +10.0k
平值价格ATM:  C 4.58 / P 3.70
隐含波动率 ATM IV:  10.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 201k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 763 ｜ +1,879 ｜ $6.00 ｜ 名义 $1.13M* ｜ -0.3%
P 760 ｜ +1,342 ｜ $2.16 ｜ 名义 $289.9k* ｜ -0.7%
C 765 ｜ +973 ｜ $4.58 ｜ 名义 $445.6k* ｜ -0.0%
结构参考：763（-0.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 10.0%｜历史 Rank 98%（近端代理）｜净 delta 敞口 正 201,038 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/SPY_evening.json