# 期权晨报 2026-08-31

📊 市场环境

SPY $767.25 ｜ QQQ $716.76
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-04 102C ΔOI +17,329（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 99.65 → 今晨 98.15（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 99.63 ｜ 低 96.99

Options: P/C量 1.09 | OI比 0.84 | ATM IV 46.5% | Skew -0.9pp | Term 0.93 | ExpMove ±3.9%（近端） | Rank 77%
   ⇒ Put/Call Volume: 1.09×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（4D）±3.9% ｜ 09-11（11D）±5.8% ｜ 09-18（18D）±7.5% ｜ 09-25（25D）±8.9%
   ⇒ IV–VIX Spread: +31.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -1,510,248 | GEX Change N/A | Flip: Primary Flip: 98.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 494 / LOW 145 / INVALID 337
结构观察区: Primary Flip 98.27（全链重定价，覆盖 100%）
最近结构参考: Flip 98（现价低于该位 0.1%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 98（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 106.0C — Vol 1,053 | 最新价 $0.21 | OI 314→18030 (ΔOI +17716张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17716张（+5642.0% vs前日OI），连续性待观察（方向未知）
09-04 102.0C — Vol 303 | 最新价 $0.64 | OI 298→17627 (ΔOI +17329张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17329张（+5815.1% vs前日OI），连续性待观察（方向未知）
09-04 105.0C — Vol 3,210 | 最新价 $0.33 | OI 613→13484 (ΔOI +12871张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12871张（+2099.7% vs前日OI），连续性待观察（方向未知）
09-04 101.0C — Vol 170 | 最新价 $0.92 | OI 191→10802 (ΔOI +10611张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10611张（+5555.5% vs前日OI），连续性待观察（方向未知）
09-04 104.0C — Vol 500 | 最新价 $0.35 | OI 1020→8147 (ΔOI +7127张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7127张（+698.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +74.6k / P +17.4k ｜ Activity HIGH ｜ 4D
09-11  C +3.6k / P +3.4k ｜ Activity HIGH ｜ 11D
09-18  C -10.1k / P +9.0k ｜ Activity HIGH ｜ 18D
09-25  C +0.2k / P +0.7k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 91.4k / P 76.7k
ΔOI:      C +74.6k / P +17.4k
ATM:      C 1.99 / P 1.86
ATM IV:   46.5%
ΔOI Δ Exposure*: 560k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 106 ｜ +17,716 ｜ $0.18 ｜ 名义 $318.9k* ｜ +8.0%
C 102 ｜ +17,329 ｜ $0.66 ｜ 名义 $1.14M* ｜ +3.9%
C 105 ｜ +12,871 ｜ $0.23 ｜ 名义 $296.0k* ｜ +7.0%
结构参考：106（+8.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 14.2k / P 23.3k
ΔOI:      C +3.6k / P +3.4k
ATM:      C 2.98 / P 2.72
ATM IV:   41.8%
ΔOI Δ Exposure*: 14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 104 ｜ +2,258 ｜ $1.01 ｜ 名义 $228.1k* ｜ +6.0%
P 86 ｜ +1,432 ｜ $0.27 ｜ 名义 $38.7k* ｜ -12.4%
P 98 ｜ +1,425 ｜ $2.72 ｜ 名义 $387.6k* ｜ -0.2%
结构参考：104（+6.0%）上方 / 86（-12.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 241.3k / P 390.6k
ΔOI:      C -10.1k / P +9.0k
ATM:      C 3.85 / P 3.55
ATM IV:   42.3%
ΔOI Δ Exposure*: -716k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 100 ｜ -2,719 ｜ $2.95 ｜ 名义 $-802.1k* ｜ +1.9%
P 96 ｜ +2,697 ｜ $2.70 ｜ 名义 $728.2k* ｜ -2.2%
C 115 ｜ -2,642 ｜ $0.31 ｜ 名义 $-81.9k* ｜ +17.2%
结构参考：96（-2.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 5.2k / P 6.1k
ΔOI:      C +0.2k / P +0.7k
ATM:      C 4.54 / P 4.20
ATM IV:   42.9%
ΔOI Δ Exposure*: -6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 88 ｜ +152 ｜ $1.03 ｜ 名义 $15.7k* ｜ -10.3%
P 90 ｜ +144 ｜ $1.31 ｜ 名义 $18.9k* ｜ -8.3%
P 95 ｜ +106 ｜ $2.77 ｜ 名义 $29.4k* ｜ -3.2%
结构参考：88（-10.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/GDX_morning.json