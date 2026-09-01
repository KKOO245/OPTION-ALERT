# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $762.01 ｜ QQQ $707.64
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
🟡 **单日价格波动**: -4.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 206.32 → 今开 199.15（-3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 200.64 ｜ 低 194.80

Options: P/C成交量 0.80 | OI比 0.92 | ATM IV 84.6% | Skew -2.4pp | Term 0.93 | ExpMove ±6.4%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（3D）±6.4% ｜ 09-11（10D）±10.3% ｜ 09-18（17D）±13.9% ｜ 09-25（24D）±15.9%
   ⇒ IV–VIX Spread: +68.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,897,455 | GEX Change vs 上次快照 -4,441,374 | Flip: Primary Flip: 215.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 560 / LOW 78 / INVALID 166
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 215.87（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价低于该位 1.4%）
最近结构参考: Put Wall 200（现价低于该位 1.4%）
量化视角： 负 Gamma（1290万，无历史分位）｜负 Gamma 加深（444万）｜现价位于 Flip 下方 8.66%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 216（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 230.0C — Vol 350 | 最新价 $0.38 | OI 2148→3056 (ΔOI +908张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增908张（+42.3% vs前日OI），连续性待观察（方向未知）
09-11 270.0C — Vol 452 | 最新价 $0.40 | OI 889→1776 (ΔOI +887张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增887张（+99.8% vs前日OI），连续性待观察（方向未知）
09-04 235.0C — Vol 57 | 最新价 $0.25 | OI 668→1505 (ΔOI +837张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增837张（+125.3% vs前日OI），连续性待观察（方向未知）
09-04 185.0P — Vol 754 | 最新价 $1.89 | OI 1181→1969 (ΔOI +788张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增788张（+66.7% vs前日OI），连续性待观察（方向未知）
09-18 95.0P — Vol 5 | 最新价 $0.10 | OI 707→1422 (ΔOI +715张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增715张（+101.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,135 张（Put 1,503 / Call 2,632），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +7.1k / P +4.9k ｜ Activity HIGH ｜ 3D
09-11  C +3.0k / P +1.7k ｜ Activity HIGH ｜ 10D
09-18  C +0.3k / P +1.1k ｜ Activity HIGH ｜ 17D
09-25  C +0.7k / P +1.3k ｜ Activity MEDIUM △ ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 53.7k / P 49.5k
今日变化ΔOI: C +7.1k / P +4.9k
平值价格ATM:  C 6.18 / P 6.45
隐含波动率 ATM IV:  84.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 65k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 185 ｜ +788 ｜ $1.89 ｜ 名义 $148.9k* ｜ -6.2%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：185（-6.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 84.6%｜历史 Rank 14%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 65,245 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 16.8k / P 15.5k
今日变化ΔOI: C +3.0k / P +1.7k
平值价格ATM:  C 9.93 / P 10.44
隐含波动率 ATM IV:  75.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -14k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 75.3%｜历史 Rank 14%（近端代理）｜净 delta 敞口 负 13,524 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 96.2k / P 151.6k
今日变化ΔOI: C +0.3k / P +1.1k
平值价格ATM:  C 13.35 / P 14.10
隐含波动率 ATM IV:  76.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 24k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +370 ｜ $2.58 ｜ 名义 $95.5k* ｜ +21.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：240（+21.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 76.3%｜历史 Rank 14%（近端代理）｜净 delta 敞口 正 24,192 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 220C +195 ｜ 200P +169

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 84.6% vs 09-11 75.3%（差 +9.3pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/NBIS_morning.json