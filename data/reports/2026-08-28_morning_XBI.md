# 期权晨报 2026-08-28

📊 市场环境

SPY $774.48 ｜ QQQ $723.01
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 56.4（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 168P ΔOI +254（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 168.23 → 今晨 164.25（-2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 167.12 ｜ 低 163.71

Options: P/C量 1.89 | OI比 1.50 | ATM IV 46.1% | Skew -2.8pp | Term 0.69 | ExpMove ±0.9%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.89×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.50×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±4.9% ｜ 09-11（14D）±6.0% ｜ 09-18（21D）±5.6% ｜ 09-25（28D）±7.4%
   ⇒ IV–VIX Spread: +31.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 166.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 452 / LOW 141 / INVALID 315
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 166.59（全链重定价，覆盖 93%）
Put Wall 150（现价高于该位 9.5%） | Call Wall 170（现价低于该位 3.4%）
最近结构参考: Flip 167（现价低于该位 1.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 170（Call Wall）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 168.0P — Vol 3 | 最新价 $3.83 | OI 22→1029 (ΔOI +1007张) | ΔOI/Volume 33566.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1007张（+4577.3% vs前日OI），连续性待观察（方向未知）
08-28 165.0P — Vol 4,182 | 最新价 $0.88 | OI 1670→2595 (ΔOI +925张) | ΔOI/Volume 22.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增925张（+55.4% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 446 | 最新价 $1.29 | OI 8772→9084 (ΔOI +312张) | ΔOI/Volume 70.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增312张（+3.6% vs前日OI），值得跟踪（方向未知）
09-04 168.0P — Vol 263 | 最新价 $4.35 | OI 22→276 (ΔOI +254张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增254张（+1154.5% vs前日OI），连续性待观察（方向未知）
09-18 177.0C — Vol 0 | 最新价 $2.11 | OI 211→403 (ΔOI +192张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增192张（+91.0% vs前日OI），值得跟踪（方向未知）
📆 Forward Expiration Structure

09-04  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 7D
09-11  C +0.1k / P -15 ｜ Activity HIGH ｜ 14D
09-18  C +0.5k / P -1.4k ｜ Activity HIGH ｜ 21D
09-25  C +22 / P +24 ｜ Activity MEDIUM △ ｜ 28D

   Top ΔOI: 168P +254 ｜ 166P +132

📆 09-11 Forward Structure
OI:       C 1.2k / P 1.4k
ΔOI:      C +0.1k / P -15
ATM:      C 7.55 / P 2.35
ATM IV:   29.8%
ΔOI Δ Exposure*: 7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 155 ｜ +42 ｜ $13.85 ｜ 名义 $58.2k* ｜ -5.6%
C 175 ｜ +32 ｜ $1.35 ｜ 名义 $4.3k* ｜ +6.5%
P 154 ｜ -26 ｜ $0.59 ｜ 名义 $-1.5k* ｜ -6.2%
结构参考：175（+6.5%）上方 / 155（-5.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 71.4k / P 101.1k
ΔOI:      C +0.5k / P -1.4k
ATM:      C 5.00 / P 4.18
ATM IV:   31.0%
ΔOI Δ Exposure*: 31k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 155 ｜ -1,547 ｜ $1.36 ｜ 名义 $-210.4k* ｜ -5.6%
C 175 ｜ +312 ｜ $1.29 ｜ 名义 $40.2k* ｜ +6.5%
C 177 ｜ +192 ｜ $2.11 ｜ 名义 $40.5k* ｜ +7.8%
结构参考：175（+6.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 190C +15 ｜ 170P +11

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/XBI_morning.json