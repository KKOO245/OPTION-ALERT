# 期权晚报 2026-09-03（快照 17:36 ET）

📊 市场环境

SPY $773.17 ｜ QQQ $717.67
VIX 14.32 ↓5.8%（5D -1.3%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 09-04 ATM IV 43.3% vs 09-11 31.2%（差 +12.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 374.75 → 收盘 369.83（-1.3%） ｜ 今日高 378.99 ｜ 低 365.42
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.25 | OI比 0.58 | ATM IV 43.3% | Skew -1.6pp | Term 0.77 | ExpMove ±1.7%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.25×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±1.7% ｜ 09-11（8D）±3.7% ｜ 09-18（15D）±5.2% ｜ 09-25（22D）±7.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,272,741 | GEX Change vs 上次快照 18,200 | Flip: Primary Flip: 375.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 213 / LOW 188 / INVALID 493
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 375.48（全链重定价，覆盖 94%）
Call Wall 400（现价低于该位 7.5%）
最近结构参考: Flip 375（现价低于该位 1.5%）
量化视角： 负 Gamma（127万，无历史分位）｜负 Gamma 缓解（+2万）｜现价位于 Flip 下方 1.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 375（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 370.0P — Vol 14 | 最新价 $6.66 | OI 14→103 (ΔOI +89张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增89张（+635.7% vs前日OI），值得跟踪（方向未知）
09-04 390.0C — Vol 8 | 最新价 $0.10 | OI 136→195 (ΔOI +59张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增59张（+43.4% vs前日OI），值得跟踪（方向未知）
09-04 400.0C — Vol 1 | 最新价 $0.10 | OI 75→106 (ΔOI +31张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增31张（+41.3% vs前日OI），值得跟踪（方向未知）
09-25 400.0C — Vol 4 | 最新价 $2.70 | OI 24→52 (ΔOI +28张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增28张（+116.7% vs前日OI），值得跟踪（方向未知）
09-04 380.0C — Vol 233 | 最新价 $1.42 | OI 209→235 (ΔOI +26张) | ΔOI/Volume 11.2% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增26张（+12.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 233 张（Put 89 / Call 144），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.1k / P +29 ｜ Activity MEDIUM △ ｜ 1D
09-11  C +89 / P +0.1k ｜ Activity HIGH ｜ 8D
09-18  C +15 / P -12 ｜ Activity LOW ｜ 15D
09-25  C +57 / P -3 ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 2.2k / P 1.2k
今日变化ΔOI: C +0.1k / P +29
平值价格ATM:  C 3.61 / P 2.79
隐含波动率 ATM IV:  43.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 40 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 390 ｜ +59 ｜ $0.10 ｜ 名义 $590* ｜ +5.5%
C 400 ｜ +31 ｜ $0.10 ｜ 名义 $310* ｜ +8.2%
C 380 ｜ +26 ｜ $1.42 ｜ 名义 $3.7k* ｜ +2.7%
结构参考：390（+5.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 43.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 40 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 0.8k / P 0.6k
今日变化ΔOI: C +89 / P +0.1k
平值价格ATM:  C 7.05 / P 6.66
隐含波动率 ATM IV:  31.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 370 ｜ +89 ｜ $6.66 ｜ 名义 $59.3k* ｜ +0.0%
C 400 ｜ +21 ｜ $1.00 ｜ 名义 $2.1k* ｜ +8.2%
C 390 ｜ +19 ｜ $1.19 ｜ 名义 $2.3k* ｜ +5.5%
结构参考：400（+8.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 31.2%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,975 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 400C +28 ｜ 380C +9

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 43.3% vs 09-11 31.2%（差 +12.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/ISRG_evening.json