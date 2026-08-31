# 期权晨报 2026-08-31

📊 市场环境

SPY $765.58 ｜ QQQ $714.41
VIX 15.33 ↑6.2%（5D -3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 50.1（neutral）
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
🟡 **单日价格波动**: +3.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 360C ΔOI +5,341（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 348.75 → 今晨 360.46（+3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 363.04 ｜ 低 347.15

Options: P/C量 0.45 | OI比 0.50 | ATM IV 72.1% | Skew -0.0pp | Term 0.58 | ExpMove ±1.6%（近端） | Rank 85%
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-02（2D）±3.1% ｜ 09-04（4D）±4.3% ｜ 09-09（9D）±5.2% ｜ 09-11（11D）±5.8%
   ⇒ IV–VIX Spread: +56.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 340.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1254 / LOW 184 / INVALID 756
结构观察区: Primary Flip 340.07（全链重定价，覆盖 99%）
Put Wall 340（弱结构｜现价高于该位 6.0%）
最近结构参考: Flip 340（现价高于该位 6.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 340（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 130.0P — Vol 1 | 最新价 $0.01 | OI 1000→22347 (ΔOI +21347张) | ΔOI/Volume 2134700.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21347张（+2134.7% vs前日OI），连续性待观察（方向未知）
09-11 220.0P — Vol 0 | 最新价 $0.08 | OI 606→14187 (ΔOI +13581张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13581张（+2241.1% vs前日OI），连续性待观察（方向未知）
09-11 180.0P — Vol 0 | 最新价 $0.05 | OI 16→12508 (ΔOI +12492张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12492张（+78075.0% vs前日OI），连续性待观察（方向未知）
09-02 165.0P — Vol 0 | 最新价 $0.01 | OI 22→7022 (ΔOI +7000张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7000张（+31818.2% vs前日OI），连续性待观察（方向未知）
08-31 347.5P — Vol 20,657 | 最新价 $0.16 | OI 1189→7145 (ΔOI +5956张) | ΔOI/Volume 28.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5956张（+500.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-02  C +16.6k / P +25.0k ｜ Activity HIGH ｜ 2D
09-04  C +46.3k / P +54.4k ｜ Activity HIGH ｜ 4D
09-09  C +3.1k / P +1.0k ｜ Activity HIGH ｜ 9D
09-11  C +6.9k / P +28.2k ｜ Activity HIGH ｜ 11D

📆 09-02 Forward Structure
OI:       C 36.8k / P 37.4k
ΔOI:      C +16.6k / P +25.0k
ATM:      C 6.10 / P 5.23
ATM IV:   49.6%
ΔOI Δ Exposure*: 485k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 165 ｜ +7,000 ｜ $0.01 ｜ 名义 $7.0k* ｜ -54.2%
C 400 ｜ +3,518 ｜ $0.15 ｜ 名义 $52.8k* ｜ +11.0%
P 310 ｜ +3,007 ｜ $0.04 ｜ 名义 $12.0k* ｜ -14.0%
结构参考：400（+11.0%）上方 / 165（-54.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 148.1k / P 132.1k
ΔOI:      C +46.3k / P +54.4k
ATM:      C 8.20 / P 7.27
ATM IV:   48.9%
ΔOI Δ Exposure*: 1.4M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 130 ｜ +21,347 ｜ $0.01 ｜ 名义 $21.3k* ｜ -63.9%
P 200 ｜ +5,775 ｜ $0.01 ｜ 名义 $5.8k* ｜ -44.5%
C 360 ｜ +5,341 ｜ $8.20 ｜ 名义 $4.38M* ｜ -0.1%
结构参考：130（-63.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 8.3k / P 2.9k
ΔOI:      C +3.1k / P +1.0k
ATM:      C 9.90 / P 8.90
ATM IV:   40.5%
ΔOI Δ Exposure*: 96k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +680 ｜ $1.00 ｜ 名义 $68.0k* ｜ +11.0%
C 380 ｜ +527 ｜ $3.15 ｜ 名义 $166.0k* ｜ +5.4%
C 355 ｜ +334 ｜ $12.39 ｜ 名义 $413.8k* ｜ -1.5%
结构参考：400（+11.0%）上方 / 355（-1.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 60.3k / P 52.8k
ΔOI:      C +6.9k / P +28.2k
ATM:      C 11.00 / P 9.98
ATM IV:   41.7%
ΔOI Δ Exposure*: 138k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 220 ｜ +13,581 ｜ $0.08 ｜ 名义 $108.6k* ｜ -39.0%
P 180 ｜ +12,492 ｜ $0.05 ｜ 名义 $62.5k* ｜ -50.1%
C 510 ｜ +1,971 ｜ $0.15 ｜ 名义 $29.6k* ｜ +41.5%
结构参考：510（+41.5%）上方 / 220（-39.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/TSLA_morning.json