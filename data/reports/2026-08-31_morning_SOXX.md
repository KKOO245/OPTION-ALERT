# 期权晨报 2026-08-31

📊 市场环境

SPY $765.88 ｜ QQQ $713.50
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
🟡 **近现价集中开仓**: 09-04 535C ΔOI +966（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-25 595C ΔOI +1,400 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 508.62 → 今晨 511.08（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 514.33 ｜ 低 508.66

Options: P/C量 0.87 | OI比 0.77 | ATM IV 32.7% | Skew 1.5pp | Term 1.16 | ExpMove ±3.8%（近端） | Rank 48%
   ⇒ Put/Call Volume: 0.87×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±3.8% ｜ 09-11（11D）±5.6% ｜ 09-18（18D）±7.0% ｜ 09-25（25D）±8.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 524.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 527 / LOW 258 / INVALID 747
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 524.70（全链重定价，覆盖 98%）
Put Wall 500（弱结构｜现价高于该位 2.2%）
最近结构参考: Put Wall 500（现价高于该位 2.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 525（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 475.0P — Vol 4,831 | 最新价 $5.94 | OI 490→4961 (ΔOI +4471张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4471张（+912.5% vs前日OI），连续性待观察（方向未知）
09-18 490.0P — Vol 5,290 | 最新价 $9.50 | OI 4382→7116 (ΔOI +2734张) | ΔOI/Volume 51.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2734张（+62.4% vs前日OI），连续性待观察（方向未知）
09-18 575.0C — Vol 2,149 | 最新价 $1.65 | OI 14102→16188 (ΔOI +2086张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2086张（+14.8% vs前日OI），连续性待观察（方向未知）
09-25 595.0C — Vol 1,406 | 最新价 $1.35 | OI 8→1408 (ΔOI +1400张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1400张（+17500.0% vs前日OI），连续性待观察（方向未知）
09-18 450.0P — Vol 1,723 | 最新价 $2.51 | OI 5778→7157 (ΔOI +1379张) | ΔOI/Volume 80.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1379张（+23.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +1.4k / P +2.3k ｜ Activity HIGH ｜ 4D
09-11  C +1.4k / P -0.2k ｜ Activity HIGH ｜ 11D
09-18  C +2.3k / P +9.2k ｜ Activity HIGH ｜ 18D
09-25  C +2.4k / P +0.3k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 26.8k / P 20.6k
ΔOI:      C +1.4k / P +2.3k
ATM:      C 9.60 / P 9.68
ATM IV:   32.7%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 535 ｜ +966 ｜ $1.92 ｜ 名义 $185.5k* ｜ +4.7%
P 497 ｜ +906 ｜ $5.08 ｜ 名义 $460.2k* ｜ -2.7%
P 465 ｜ +864 ｜ $0.70 ｜ 名义 $60.5k* ｜ -9.0%
结构参考：535（+4.7%）上方 / 497（-2.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 3.3k / P 12.9k
ΔOI:      C +1.4k / P -0.2k
ATM:      C 13.81 / P 14.62
ATM IV:   34.9%
ΔOI Δ Exposure*: 24k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 557 ｜ +951 ｜ $1.43 ｜ 名义 $136.0k* ｜ +9.1%
P 490 ｜ -857 ｜ $6.39 ｜ 名义 $-547.6k* ｜ -4.1%
C 530 ｜ +242 ｜ $5.80 ｜ 名义 $140.4k* ｜ +3.7%
结构参考：557（+9.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 80.9k / P 84.8k
ΔOI:      C +2.3k / P +9.2k
ATM:      C 18.04 / P 18.00
ATM IV:   35.9%
ΔOI Δ Exposure*: -197k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 475 ｜ +4,471 ｜ $5.94 ｜ 名义 $2.66M* ｜ -7.1%
P 490 ｜ +2,734 ｜ $9.50 ｜ 名义 $2.60M* ｜ -4.1%
C 575 ｜ +2,086 ｜ $1.65 ｜ 名义 $344.2k* ｜ +12.5%
结构参考：575（+12.5%）上方 / 475（-7.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 6.6k / P 4.4k
ΔOI:      C +2.4k / P +0.3k
ATM:      C 22.30 / P 21.33
ATM IV:   37.1%
ΔOI Δ Exposure*: 13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 595 ｜ +1,400 ｜ $1.35 ｜ 名义 $189.0k* ｜ +16.4%
C 600 ｜ +987 ｜ $1.20 ｜ 名义 $118.4k* ｜ +17.4%
P 500 ｜ +66 ｜ $16.10 ｜ 名义 $106.3k* ｜ -2.2%
结构参考：595（+16.4%）上方 / 500（-2.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/SOXX_morning.json