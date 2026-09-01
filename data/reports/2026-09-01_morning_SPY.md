# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $761.99 ｜ QQQ $707.64
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-02 766P ΔOI -6,851（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 767.05 → 今开 762.01（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 763.52 ｜ 低 761.17

Options: P/C成交量 1.02 | OI比 1.20 | ATM IV 13.1% | Skew 1.6pp | Term 0.95 | ExpMove ±0.6%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 1.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 32% ｜ P/C OI(近端) 7%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 32%）｜近端持仓极端 Call 重（P/C OI 分位 7%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-02（1D）±0.6% ｜ 09-03（2D）±0.8% ｜ 09-04（3D）±1.0% ｜ 09-08（7D）±1.2%
   ⇒ IV–VIX Spread: -2.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,062,324,034 | GEX Change vs 上次快照 -371,860,517 | Flip: Primary Flip: 768.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3097 / LOW 485 / INVALID 1768
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.85（全链重定价，覆盖 96%）
Call Wall 800（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 769（现价低于该位 0.9%）
量化视角： 负 Gamma（10.62亿，历史分位 32%，中性区）｜负 Gamma 加深（3.72亿）｜现价位于 Flip 下方 0.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 769（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 733.0P — Vol 167 | 最新价 $2.03 | OI 6219→24992 (ΔOI +18773张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18773张（+301.9% vs前日OI），连续性待观察（方向未知）
09-18 760.0P — Vol 5,615 | 最新价 $7.33 | OI 46585→62463 (ΔOI +15878张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15878张（+34.1% vs前日OI），连续性待观察（方向未知）
09-01 766.0C — Vol 26,272 | 最新价 $0.12 | OI 1542→13650 (ΔOI +12108张) | ΔOI/Volume 46.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12108张（+785.2% vs前日OI），连续性待观察（方向未知）
09-01 730.0P — Vol 2 | 最新价 $0.01 | OI 515→11957 (ΔOI +11442张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11442张（+2221.8% vs前日OI），连续性待观察（方向未知）
09-01 767.0C — Vol 43,058 | 最新价 $0.08 | OI 1266→12333 (ΔOI +11067张) | ΔOI/Volume 25.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11067张（+874.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 69,268 张（Put 46,093 / Call 23,175），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $15M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-02  C +24.0k / P +18.3k ｜ Activity HIGH ｜ 1D
09-03  C +9.4k / P +16.6k ｜ Activity HIGH ｜ 2D
09-04  C +21.1k / P +39.9k ｜ Activity HIGH ｜ 3D
09-08  C +9.2k / P +12.5k ｜ Activity HIGH ｜ 7D

📆 09-02 Forward Structure
存量OI:      C 69.7k / P 98.9k
今日变化ΔOI: C +24.0k / P +18.3k
平值价格ATM:  C 2.45 / P 1.94
隐含波动率 ATM IV:  12.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 168k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 766 ｜ -6,851 ｜ $4.35 ｜ 名义 $-2.98M* ｜ +0.5%
C 771 ｜ +5,026 ｜ $0.10 ｜ 名义 $50.3k* ｜ +1.2%
C 770 ｜ +2,979 ｜ $0.15 ｜ 名义 $44.7k* ｜ +1.0%
结构参考：771（+1.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.2%｜历史 Rank 52%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 168,126 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-03 Forward Structure
存量OI:      C 48.2k / P 66.5k
今日变化ΔOI: C +9.4k / P +16.6k
平值价格ATM:  C 3.25 / P 2.67
隐含波动率 ATM IV:  12.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -54k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 718 ｜ +3,976 ｜ $0.03 ｜ 名义 $11.9k* ｜ -5.8%
P 715 ｜ +2,684 ｜ $0.04 ｜ 名义 $10.7k* ｜ -6.2%
P 751 ｜ +1,186 ｜ $0.52 ｜ 名义 $61.7k* ｜ -1.4%
结构参考：718（-5.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 12.3%｜历史 Rank 52%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 54,045 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-04 Forward Structure
存量OI:      C 329.7k / P 382.8k
今日变化ΔOI: C +21.1k / P +39.9k
平值价格ATM:  C 4.10 / P 3.37
隐含波动率 ATM IV:  12.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -61k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 765 ｜ -2,701 ｜ $4.86 ｜ 名义 $-1.31M* ｜ +0.4%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 12.8%｜历史 Rank 52%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 60,658 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-08 Forward Structure
存量OI:      C 33.6k / P 30.9k
今日变化ΔOI: C +9.2k / P +12.5k
平值价格ATM:  C 4.89 / P 4.00
隐含波动率 ATM IV:  10.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -168k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 770 ｜ +1,233 ｜ $1.44 ｜ 名义 $177.6k* ｜ +1.0%
P 710 ｜ +952 ｜ $0.10 ｜ 名义 $9.5k* ｜ -6.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：770（+1.0%） / 710（-6.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 10.4%｜历史 Rank 52%（近端代理）｜净 delta 敞口 负 167,536 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/SPY_morning.json