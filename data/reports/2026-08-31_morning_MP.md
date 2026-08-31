# 期权晨报 2026-08-31

📊 市场环境

SPY $765.41 ｜ QQQ $714.99
VIX 15.19 ↑5.3%（5D -4.2%） ｜ Vol Regime: NORMAL
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 56.13 → 今晨 55.22（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 56.00 ｜ 低 54.94

Options: P/C量 0.65 | OI比 0.78 | ATM IV 72.8% | Skew -5.4pp | Term 0.93 | ExpMove ±6.2%（近端） | Rank 58%
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±6.2% ｜ 09-11（11D）±9.2% ｜ 09-18（18D）±11.8% ｜ 09-25（25D）±13.4%
   ⇒ IV–VIX Spread: +57.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,560 | GEX Change vs 上次快照 -837,720 | Flip: Primary Flip: 55.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 310 / LOW 41 / INVALID 139
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 55.24（全链重定价，覆盖 100%）
Put Wall 55（弱结构｜现价高于该位 0.4%） | Call Wall 60（弱结构｜现价低于该位 8.0%）
最近结构参考: Flip 55（现价低于该位 0.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall，弱结构）；上方 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 100%）。
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
09-11  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 11D
09-18  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
09-25  C +67 / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 09-04 Forward Structure
OI:       C 9.6k / P 7.5k
ΔOI:      C +0.9k / P +1.3k
ATM:      C 1.80 / P 1.60
ATM IV:   72.8%
ΔOI Δ Exposure*: -27k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 55 ｜ +446 ｜ $1.60 ｜ 名义 $71.4k* ｜ -0.4%
P 53 ｜ +221 ｜ $0.77 ｜ 名义 $17.0k* ｜ -4.0%
C 58 ｜ +186 ｜ $0.74 ｜ 名义 $13.8k* ｜ +5.0%
结构参考：58（+5.0%）上方 / 55（-0.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 52P +59 ｜ 50P +58

   Top ΔOI: 61C +839 ｜ 70C -243

   Top ΔOI: 62C +51 ｜ 58P +50

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 72.8% vs 09-11 65.9%（差 +6.8pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=3 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=3）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/MP_morning.json