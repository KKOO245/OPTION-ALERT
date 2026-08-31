# 期权晨报 2026-08-31

📊 市场环境

SPY $767.44 ｜ QQQ $716.76
VIX 15.16 ↑5.1%（5D -4.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 待公布 ｜ 前值 7.359
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 待公布 ｜ 前值 55.6
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **单日价格波动**: -3.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 210.77 → 今晨 204.11（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 210.00 ｜ 低 202.88

Options: P/C量 0.76 | OI比 1.27 | ATM IV 93.2% | Skew -8.4pp | Term 0.84 | ExpMove ±8.0%（近端） | Rank 55%
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±8.0% ｜ 09-11（11D）±11.7% ｜ 09-18（18D）±14.5% ｜ 09-25（25D）±16.4%
   ⇒ IV–VIX Spread: +78.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -619,323 | GEX Change vs 上次快照 -5,497,098 | Flip: Primary Flip: 205.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 567 / LOW 60 / INVALID 171
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 205.05（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 2.1%）
最近结构参考: Flip 205（现价低于该位 0.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 205（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 180.0C — Vol 0 | 最新价 $32.81 | OI 84→1595 (ΔOI +1511张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1511张（+1798.8% vs前日OI），连续性待观察（方向未知）
09-04 190.0P — Vol 335 | 最新价 $2.78 | OI 1200→2206 (ΔOI +1006张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1006张（+83.8% vs前日OI），连续性待观察（方向未知）
09-04 200.0P — Vol 329 | 最新价 $6.55 | OI 1370→2258 (ΔOI +888张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增888张（+64.8% vs前日OI），连续性待观察（方向未知）
09-18 145.0P — Vol 2 | 最新价 $0.47 | OI 4172→5018 (ΔOI +846张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增846张（+20.3% vs前日OI），连续性待观察（方向未知）
09-04 250.0C — Vol 1,158 | 最新价 $0.47 | OI 2801→3440 (ΔOI +639张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增639张（+22.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +6.2k / P +8.5k ｜ Activity HIGH ｜ 4D
09-11  C +0.8k / P +1.6k ｜ Activity HIGH ｜ 11D
09-18  C -2.9k / P +1.0k ｜ Activity HIGH ｜ 18D
09-25  C +0.4k / P +0.6k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 29.3k / P 37.3k
ΔOI:      C +6.2k / P +8.5k
ATM:      C 7.80 / P 8.45
ATM IV:   93.2%
ΔOI Δ Exposure*: -32k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +1,511 ｜ $25.11 ｜ 名义 $3.79M* ｜ -11.8%
P 190 ｜ +1,006 ｜ $2.46 ｜ 名义 $247.5k* ｜ -6.9%
P 200 ｜ +888 ｜ $5.94 ｜ 名义 $527.5k* ｜ -2.0%
结构参考：180（-11.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 12.6k / P 11.3k
ΔOI:      C +0.8k / P +1.6k
ATM:      C 11.45 / P 12.50
ATM IV:   81.7%
ΔOI Δ Exposure*: -12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 175 ｜ +309 ｜ $1.89 ｜ 名义 $58.4k* ｜ -14.3%
P 110 ｜ +247 ｜ $0.09 ｜ 名义 $2.2k* ｜ -46.1%
P 100 ｜ +241 ｜ $0.02 ｜ 名义 $482* ｜ -51.0%
结构参考：175（-14.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 115.4k / P 94.1k
ΔOI:      C -2.9k / P +1.0k
ATM:      C 14.35 / P 15.30
ATM IV:   79.8%
ΔOI Δ Exposure*: -151k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 210 ｜ -2,801 ｜ $12.33 ｜ 名义 $-3.45M* ｜ +2.9%
C 260 ｜ -1,092 ｜ $2.31 ｜ 名义 $-252.3k* ｜ +27.4%
C 230 ｜ -882 ｜ $6.50 ｜ 名义 $-573.3k* ｜ +12.7%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 7.2k / P 6.5k
ΔOI:      C +0.4k / P +0.6k
ATM:      C 16.20 / P 17.35
ATM IV:   77.7%
ΔOI Δ Exposure*: -13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ +237 ｜ $9.65 ｜ 名义 $228.7k* ｜ +10.2%
P 225 ｜ +199 ｜ $26.29 ｜ 名义 $523.2k* ｜ +10.2%
P 180 ｜ +125 ｜ $6.20 ｜ 名义 $77.5k* ｜ -11.8%
结构参考：225（+10.2%）上方 / 180（-11.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 93.2% vs 09-11 81.7%（差 +11.6pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=3 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=3）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/BE_morning.json