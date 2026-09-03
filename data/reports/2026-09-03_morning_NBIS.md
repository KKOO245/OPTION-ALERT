# 期权晨报 2026-09-03（快照 10:16 ET）

📊 市场环境

SPY $768.34 ｜ QQQ $712.38
VIX 15.00 ↓1.3%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 90.8% vs 09-11 74.7%（差 +16.1pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-04 200C ΔOI +580（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 204.09 → 今开 202.79（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 203.55 ｜ 低 196.63

Options: P/C成交量 0.31 | OI比 0.92 | ATM IV 90.8% | Skew 0.4pp | Term 0.87 | ExpMove ±4.2%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（1D）±4.2% ｜ 09-11（8D）±9.1% ｜ 09-18（15D）±12.2% ｜ 09-25（22D）±15.4%
   ⇒ IV–VIX Spread: +75.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,555,811 | GEX Change vs 上次快照 -391,385 | Flip: Primary Flip: 206.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 533 / LOW 108 / INVALID 163
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 206.75（全链重定价，覆盖 97%）
Put Wall 200（弱结构｜现价高于该位 0.4%）
最近结构参考: Put Wall 200（现价高于该位 0.4%）
量化视角： 负 Gamma（856万，无历史分位）｜负 Gamma 加深（39万）｜现价位于 Flip 下方 2.90%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 208（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 207（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 157.5P — Vol 1,838（Yahoo补） | 最新价 $0.04 | OI 171→1802 (ΔOI +1631张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1631张（+953.8% vs前日OI），连续性待观察（方向未知）
09-11 125.0P — Vol 1,005（Yahoo补） | 最新价 $0.05 | OI 243→1242 (ΔOI +999张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增999张（+411.1% vs前日OI），连续性待观察（方向未知）
09-11 315.0C — Vol 886（Yahoo补） | 最新价 $0.04 | OI 74→907 (ΔOI +833张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增833张（+1125.7% vs前日OI），连续性待观察（方向未知）
09-18 200.0C — Vol 47 | 最新价 $12.50 | OI 5619→6284 (ΔOI +665张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增665张（+11.8% vs前日OI），值得跟踪（方向未知）
09-04 200.0C — Vol 229 | 最新价 $4.00 | OI 1739→2319 (ΔOI +580张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增580张（+33.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,708 张（Put 2,630 / Call 2,078），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +1.6k / P +0.6k ｜ Activity HIGH ｜ 1D
09-11  C +3.4k / P +2.9k ｜ Activity MEDIUM △ ｜ 8D
09-18  C +0.8k / P +0.6k ｜ Activity HIGH ｜ 15D
09-25  C +0.4k / P +0.6k ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 58.5k / P 53.5k
今日变化ΔOI: C +1.6k / P +0.6k
平值价格ATM:  C 4.00 / P 4.50
隐含波动率 ATM IV:  90.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 210k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +580 ｜ $4.00 ｜ 名义 $232.0k* ｜ -0.4%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：200（-0.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 90.8%｜历史 Rank 23%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 210,499 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 98.8k / P 153.9k
今日变化ΔOI: C +0.8k / P +0.6k
平值价格ATM:  C 12.50 / P 11.96
隐含波动率 ATM IV:  76.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 46k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +665 ｜ $12.50 ｜ 名义 $831.2k* ｜ -0.4%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：200（-0.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.5%｜历史 Rank 23%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,094 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 205C +100 ｜ 220C +74

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 90.8% vs 09-11 74.7%（差 +16.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=10 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=10）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/NBIS_morning.json