# 期权晨报 2026-09-04（快照 10:52 ET）

📊 市场环境

SPY $771.00 ｜ QQQ $717.82
VIX 14.12 ↓1.4%（5D -2.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: +2.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-09 240C ΔOI +6,217（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 228.45 → 今开 231.14（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 234.76 ｜ 低 229.82

Options: P/C成交量 0.37 | OI比 1.12 | ATM IV 46.2% | Skew -1.9pp | Term 0.73 | ExpMove ±2.6%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-09（5D）±2.6% ｜ 09-11（7D）±3.6% ｜ 09-14（10D）±4.0% ｜ 09-16（12D）±4.7%
   ⇒ IV–VIX Spread: +32.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 872,280,949 | GEX Change vs 上次快照 158,477,994 | Flip: Primary Flip: 214.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 652 / LOW 129 / INVALID 357
结构观察区: Primary Flip 214.77（全链重定价，覆盖 98%）
Call Wall 230（弱结构｜现价高于该位 1.6%）
最近结构参考: Call Wall 230（现价高于该位 1.6%）
量化视角： 正 Gamma（8.72亿，无历史分位）｜正 Gamma 增强（+1.58亿）｜现价位于 Flip 上方 8.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 215（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 145.0P — Vol 54,757（Yahoo补） | 最新价 $0.01 | OI 2035→55388 (ΔOI +53353张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增53353张（+2621.8% vs前日OI），连续性待观察（方向未知）
09-04 140.0P — Vol 33,126（Yahoo补） | 最新价 $0.01 | OI 2702→34769 (ΔOI +32067张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32067张（+1186.8% vs前日OI），连续性待观察（方向未知）
10-02 250.0C — Vol 6,745 | 最新价 $3.25 | OI 11081→28489 (ΔOI +17408张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17408张（+157.1% vs前日OI），连续性待观察（方向未知）
09-11 240.0C — Vol 8,638 | 最新价 $1.84 | OI 20813→37503 (ΔOI +16690张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16690张（+80.2% vs前日OI），连续性待观察（方向未知）
09-04 135.0P — Vol 1 | 最新价 $0.01 | OI 3251→18354 (ΔOI +15103张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15103张（+464.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 134,621 张（Put 100,523 / Call 34,098），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-09  C +26.1k / P +17.3k ｜ Activity HIGH ｜ 5D
09-11  C +62.5k / P +51.7k ｜ Activity HIGH ｜ 7D
09-14  C +1.5k / P +1.2k ｜ Activity HIGH ｜ 10D
09-16  C +2.1k / P +1.1k ｜ Activity HIGH ｜ 12D

📆 09-09 Forward Structure
存量OI:      C 128.1k / P 53.2k
今日变化ΔOI: C +26.1k / P +17.3k
平值价格ATM:  C 2.53 / P 3.65
隐含波动率 ATM IV:  27.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 864k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +6,217 ｜ $0.96 ｜ 名义 $596.8k* ｜ +2.7%
C 230 ｜ +5,740 ｜ $5.40 ｜ 名义 $3.10M* ｜ -1.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：240（+2.7%） / 230（-1.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 27.5%｜历史 Rank 60%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 864,138 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 282.8k / P 177.1k
今日变化ΔOI: C +62.5k / P +51.7k
平值价格ATM:  C 3.53 / P 4.85
隐含波动率 ATM IV:  31.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 2.1M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +16,690 ｜ $1.79 ｜ 名义 $2.99M* ｜ +2.7%
C 232 ｜ +12,649 ｜ $4.79 ｜ 名义 $6.06M* ｜ -0.5%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：240（+2.7%） / 232（-0.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 31.4%｜历史 Rank 60%（近端代理）｜净 delta 敞口 正 2,120,047 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-14 Forward Structure
存量OI:      C 16.4k / P 5.1k
今日变化ΔOI: C +1.5k / P +1.2k
平值价格ATM:  C 4.05 / P 5.20
隐含波动率 ATM IV:  29.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 250 ｜ +718 ｜ $0.59 ｜ 名义 $42.4k* ｜ +6.9%
P 220 ｜ +395 ｜ $0.90 ｜ 名义 $35.5k* ｜ -5.9%
C 235 ｜ +331 ｜ $4.05 ｜ 名义 $134.1k* ｜ +0.5%
结构参考：250（+6.9%） / 220（-5.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 29.8%｜历史 Rank 60%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 9,355 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-16 Forward Structure
存量OI:      C 9.3k / P 4.1k
今日变化ΔOI: C +2.1k / P +1.1k
平值价格ATM:  C 4.95 / P 6.00
隐含波动率 ATM IV:  32.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 65k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 230 ｜ +376 ｜ $7.45 ｜ 名义 $280.1k* ｜ -1.6%
C 245 ｜ +348 ｜ $1.67 ｜ 名义 $58.1k* ｜ +4.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：245（+4.8%） / 230（-1.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 32.2%｜历史 Rank 60%（近端代理）｜净 delta 敞口 正 65,177 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/NVDA_morning.json