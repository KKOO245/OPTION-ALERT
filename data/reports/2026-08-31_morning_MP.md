# 期权晨报 2026-08-31

📊 市场环境

SPY $766.17 ｜ QQQ $713.51
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
🟡 **近现价集中开仓**: 09-04 55P ΔOI +446（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 56.13 → 今晨 55.51（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 56.00 ｜ 低 54.94

Options: P/C量 0.94 | OI比 0.78 | ATM IV 66.0% | Skew -8.0pp | Term 1.03 | ExpMove ±7.4%（近端） | Rank 49%
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±7.4% ｜ 09-11（11D）±10.4% ｜ 09-18（18D）±12.0% ｜ 09-25（25D）±15.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 55.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 315 / LOW 43 / INVALID 132
结构观察区: Primary Flip 55.68（全链重定价，覆盖 100%）
Put Wall 55（弱结构｜现价高于该位 0.9%） | Call Wall 60（弱结构｜现价低于该位 7.5%）
最近结构参考: Flip 56（现价低于该位 0.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall，弱结构）；上方 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 61.0C — Vol 854 | 最新价 $1.90 | OI 37→876 (ΔOI +839张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增839张（+2267.6% vs前日OI），连续性待观察（方向未知）
09-04 55.0P — Vol 754 | 最新价 $1.34 | OI 344→790 (ΔOI +446张) | ΔOI/Volume 59.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增446张（+129.7% vs前日OI），连续性待观察（方向未知）
09-18 57.0C — Vol 530 | 最新价 $3.20 | OI 11→250 (ΔOI +239张) | ΔOI/Volume 45.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增239张（+2172.7% vs前日OI），连续性待观察（方向未知）
09-04 53.0P — Vol 269 | 最新价 $0.71 | OI 442→663 (ΔOI +221张) | ΔOI/Volume 82.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增221张（+50.0% vs前日OI），连续性待观察（方向未知）
09-04 58.0C — Vol 205 | 最新价 $1.25 | OI 403→589 (ΔOI +186张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增186张（+46.1% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +0.9k / P +1.3k ｜ Activity HIGH ｜ 4D
09-11  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 11D
09-18  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
09-25  C +67 / P +0.2k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 9.6k / P 7.5k
ΔOI:      C +0.9k / P +1.3k
ATM:      C 2.18 / P 1.95
ATM IV:   66.0%
ΔOI Δ Exposure*: -13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 55 ｜ +446 ｜ $1.34 ｜ 名义 $59.8k* ｜ -0.9%
P 53 ｜ +221 ｜ $0.71 ｜ 名义 $15.7k* ｜ -4.5%
C 58 ｜ +186 ｜ $1.25 ｜ 名义 $23.2k* ｜ +4.5%
结构参考：58（+4.5%）上方 / 55（-0.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.9k / P 3.4k
ΔOI:      C +0.1k / P +0.2k
ATM:      C 3.10 / P 2.65
ATM IV:   65.5%
ΔOI Δ Exposure*: -1k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 52 ｜ +59 ｜ $1.05 ｜ 名义 $6.2k* ｜ -6.3%
P 50 ｜ +58 ｜ $0.52 ｜ 名义 $3.0k* ｜ -9.9%
C 60 ｜ +57 ｜ $1.45 ｜ 名义 $8.3k* ｜ +8.1%
结构参考：60（+8.1%）上方 / 52（-6.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 61C +839 ｜ 70C -243

📆 09-25 Forward Structure
OI:       C 3.2k / P 3.5k
ΔOI:      C +67 / P +0.2k
ATM:      C 4.40 / P 4.00
ATM IV:   65.8%
ΔOI Δ Exposure*: -6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 62 ｜ +51 ｜ $2.10 ｜ 名义 $10.7k* ｜ +11.7%
P 58 ｜ +50 ｜ $4.57 ｜ 名义 $22.9k* ｜ +4.5%
P 59 ｜ +35 ｜ $5.15 ｜ 名义 $18.0k* ｜ +6.3%
结构参考：62（+11.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/MP_morning.json