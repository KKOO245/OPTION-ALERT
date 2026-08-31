# 期权晨报 2026-08-31

📊 市场环境

SPY $765.66 ｜ QQQ $715.06
VIX 15.22 ↑5.5%（5D -4.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.9（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 待公布 ｜ 前值 7.359
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 待公布 ｜ 前值 55.6
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **单日价格波动**: -2.1%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 210P ΔOI +504（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 209.18 → 今晨 204.74（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 208.88 ｜ 低 201.53

Options: P/C量 0.62 | OI比 0.96 | ATM IV 83.8% | Skew -1.0pp | Term 0.95 | ExpMove ±7.2%（近端） | Rank 12%
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（4D）±7.2% ｜ 09-11（11D）±10.7% ｜ 09-18（18D）±13.8% ｜ 09-25（25D）±16.8%
   ⇒ IV–VIX Spread: +68.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,341,693 | GEX Change vs 上次快照 -4,415,143 | Flip: Primary Flip: 223.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 586 / LOW 47 / INVALID 171
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 223.13（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 2.4%）
最近结构参考: Put Wall 200（现价高于该位 2.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 223（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 220.0P — Vol 230 | 最新价 $18.57 | OI 966→4394 (ΔOI +3428张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3428张（+354.9% vs前日OI），连续性待观察（方向未知）
09-04 240.0C — Vol 283 | 最新价 $0.65 | OI 2534→4322 (ΔOI +1788张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1788张（+70.6% vs前日OI），连续性待观察（方向未知）
09-04 220.0C — Vol 426 | 最新价 $2.53 | OI 1471→3141 (ΔOI +1670张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1670张（+113.5% vs前日OI），连续性待观察（方向未知）
09-04 200.0P — Vol 477 | 最新价 $5.85 | OI 4011→5436 (ΔOI +1425张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1425张（+35.5% vs前日OI），连续性待观察（方向未知）
09-04 190.0P — Vol 277 | 最新价 $2.60 | OI 1567→2694 (ΔOI +1127张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1127张（+71.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +7.5k / P +14.7k ｜ Activity HIGH ｜ 4D
09-11  C +3.3k / P +1.6k ｜ Activity HIGH ｜ 11D
09-18  C +0.3k / P +2.4k ｜ Activity HIGH ｜ 18D
09-25  C -41 / P +1.1k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 46.6k / P 44.6k
ΔOI:      C +7.5k / P +14.7k
ATM:      C 7.33 / P 7.30
ATM IV:   83.8%
ΔOI Δ Exposure*: -438k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 220 ｜ +3,428 ｜ $17.38 ｜ 名义 $5.96M* ｜ +7.5%
C 240 ｜ +1,788 ｜ $0.50 ｜ 名义 $89.4k* ｜ +17.2%
C 220 ｜ +1,670 ｜ $2.36 ｜ 名义 $394.1k* ｜ +7.5%
结构参考：220（+7.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 13.8k / P 13.8k
ΔOI:      C +3.3k / P +1.6k
ATM:      C 10.90 / P 10.95
ATM IV:   75.8%
ΔOI Δ Exposure*: 5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 300 ｜ +667 ｜ $0.24 ｜ 名义 $16.0k* ｜ +46.5%
C 270 ｜ +507 ｜ $0.58 ｜ 名义 $29.4k* ｜ +31.9%
P 210 ｜ +504 ｜ $13.70 ｜ 名义 $690.5k* ｜ +2.6%
结构参考：300（+46.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 95.9k / P 150.5k
ΔOI:      C +0.3k / P +2.4k
ATM:      C 14.00 / P 14.22
ATM IV:   77.5%
ΔOI Δ Exposure*: 328 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 100 ｜ +901 ｜ $0.10 ｜ 名义 $9.0k* ｜ -51.2%
C 210 ｜ +671 ｜ $12.05 ｜ 名义 $808.6k* ｜ +2.6%
P 190 ｜ +372 ｜ $7.40 ｜ 名义 $275.3k* ｜ -7.2%
结构参考：210（+2.6%）上方 / 100（-51.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 6.8k / P 10.7k
ΔOI:      C -41 / P +1.1k
ATM:      C 16.62 / P 17.74
ATM IV:   78.9%
ΔOI Δ Exposure*: -24k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 280 ｜ +586 ｜ $2.07 ｜ 名义 $121.3k* ｜ +36.8%
C 300 ｜ -482 ｜ $1.25 ｜ 名义 $-60.2k* ｜ +46.5%
P 200 ｜ +288 ｜ $14.04 ｜ 名义 $404.4k* ｜ -2.3%
结构参考：280（+36.8%）上方 / 200（-2.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 83.8% vs 09-11 75.8%（差 +8.0pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=3 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=3）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/NBIS_morning.json