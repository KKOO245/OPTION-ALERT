# 期权晨报 2026-09-03（快照 11:17 ET）

📊 市场环境

SPY $769.44 ｜ QQQ $716.10
VIX 14.85 ↓2.3%（5D -2.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 46.3% vs 09-11 31.1%（差 +15.1pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 371.88 → 今开 374.75（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 378.99 ｜ 低 365.42

Options: P/C成交量 0.76 | OI比 0.58 | ATM IV 46.3% | Skew 6.1pp | Term 0.69 | ExpMove ±1.7%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 6.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±1.7% ｜ 09-11（8D）±0.9% ｜ 09-18（15D）±6.5% ｜ 09-25（22D）±7.0%
   ⇒ IV–VIX Spread: +31.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,721,163 | GEX Change vs 上次快照 -497,569 | Flip: Primary Flip: 374.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 240 / LOW 159 / INVALID 495
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 374.40（全链重定价，覆盖 93%）
Call Wall 400（现价低于该位 8.2%）
最近结构参考: Flip 374（现价低于该位 1.9%）
量化视角： 负 Gamma（172万，无历史分位）｜负 Gamma 加深（50万）｜现价位于 Flip 下方 1.93%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 374（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 370.0P — Vol 112 | 最新价 $6.63 | OI 14→103 (ΔOI +89张) | ΔOI/Volume 79.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增89张（+635.7% vs前日OI），连续性待观察（方向未知）
09-04 390.0C — Vol 102 | 最新价 $0.30 | OI 136→195 (ΔOI +59张) | ΔOI/Volume 57.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增59张（+43.4% vs前日OI），连续性待观察（方向未知）
09-04 400.0C — Vol 42 | 最新价 $0.20 | OI 75→106 (ΔOI +31张) | ΔOI/Volume 73.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31张（+41.3% vs前日OI），连续性待观察（方向未知）
09-25 400.0C — Vol 28 | 最新价 $3.50 | OI 24→52 (ΔOI +28张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28张（+116.7% vs前日OI），连续性待观察（方向未知）
09-04 380.0C — Vol 70 | 最新价 $1.25 | OI 209→235 (ΔOI +26张) | ΔOI/Volume 37.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增26张（+12.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 233 张（Put 89 / Call 144），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.1k / P +29 ｜ Activity MEDIUM △ ｜ 1D
09-11  C +89 / P +0.1k ｜ Activity MEDIUM △ ｜ 8D
09-18  C +15 / P -12 ｜ Activity MEDIUM △ ｜ 15D
09-25  C +57 / P -3 ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 2.2k / P 1.2k
今日变化ΔOI: C +0.1k / P +29
平值价格ATM:  C 3.25 / P 3.15
隐含波动率 ATM IV:  46.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -542 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 390 ｜ +59 ｜ $0.10 ｜ 名义 $590* ｜ +6.2%
C 400 ｜ +31 ｜ $0.20 ｜ 名义 $620* ｜ +8.9%
C 380 ｜ +26 ｜ $0.10 ｜ 名义 $260* ｜ +3.5%
结构参考：390（+6.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 46.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 542 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（MEDIUM △）Top ΔOI: 370P +89 ｜ 400C +21

09-18（MEDIUM △）Top ΔOI: 400C -27 ｜ 430P -20

09-25（MEDIUM △）Top ΔOI: 400C +28 ｜ 380C +9

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 46.3% vs 09-11 31.1%（差 +15.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=10 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=10）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/ISRG_morning.json