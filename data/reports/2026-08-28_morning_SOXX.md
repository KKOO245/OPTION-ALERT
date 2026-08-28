# 期权晨报 2026-08-28

📊 市场环境

SPY $774.48 ｜ QQQ $723.26
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 56.4（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 495P ΔOI +375（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 520.65 → 今晨 517.88（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 522.65 ｜ 低 515.91

Options: P/C量 3.05 | OI比 0.77 | ATM IV 42.7% | Skew 1.1pp | Term 0.90 | ExpMove ±0.8%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 3.05×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±4.1% ｜ 09-11（14D）±5.6% ｜ 09-18（21D）±7.2% ｜ 09-25（28D）±6.2%
   ⇒ IV–VIX Spread: +28.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 521.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 565 / LOW 351 / INVALID 706
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 521.83（全链重定价，覆盖 86%）
Put Wall 500（现价高于该位 3.6%） | Call Wall 575（现价低于该位 9.9%）
最近结构参考: Flip 522（现价低于该位 0.8%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall）；上方 575（Call Wall）。
• Gamma 区域：切换参考 522（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 522.5C — Vol 16 | 最新价 $1.30 | OI 24→1388 (ΔOI +1364张) | ΔOI/Volume 8525.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1364张（+5683.3% vs前日OI），连续性待观察（方向未知）
08-28 537.5C — Vol 2 | 最新价 $0.15 | OI 250→1356 (ΔOI +1106张) | ΔOI/Volume 55300.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1106张（+442.4% vs前日OI），连续性待观察（方向未知）
08-28 540.0C — Vol 15 | 最新价 $0.04 | OI 355→1336 (ΔOI +981张) | ΔOI/Volume 6540.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增981张（+276.3% vs前日OI），连续性待观察（方向未知）
08-28 525.0C — Vol 28 | 最新价 $0.32 | OI 449→1377 (ΔOI +928张) | ΔOI/Volume 3314.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增928张（+206.7% vs前日OI），连续性待观察（方向未知）
08-28 520.0P — Vol 68 | 最新价 $2.00 | OI 582→1284 (ΔOI +702张) | ΔOI/Volume 1032.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增702张（+120.6% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +0.7k / P +0.7k ｜ Activity HIGH ｜ 7D
09-11  C +45 / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
09-18  C +1.0k / P -0.3k ｜ Activity HIGH ｜ 21D
09-25  C +0.2k / P +37 ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 25.4k / P 18.3k
ΔOI:      C +0.7k / P +0.7k
ATM:      C 11.19 / P 10.13
ATM IV:   35.2%
ΔOI Δ Exposure*: -7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 490 ｜ +257 ｜ $1.85 ｜ 名义 $47.5k* ｜ -5.4%
C 570 ｜ +255 ｜ $0.75 ｜ 名义 $19.1k* ｜ +10.1%
C 547 ｜ +240 ｜ $2.20 ｜ 名义 $52.8k* ｜ +5.7%
结构参考：570（+10.1%）上方 / 490（-5.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 435P +70 ｜ 430P +50

📆 09-18 Forward Structure
OI:       C 78.6k / P 75.6k
ΔOI:      C +1.0k / P -0.3k
ATM:      C 18.90 / P 18.38
ATM IV:   36.9%
ΔOI Δ Exposure*: 64k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 470 ｜ -403 ｜ $3.80 ｜ 名义 $-153.1k* ｜ -9.2%
P 495 ｜ +375 ｜ $8.30 ｜ 名义 $311.3k* ｜ -4.4%
C 540 ｜ +279 ｜ $11.50 ｜ 名义 $320.9k* ｜ +4.3%
结构参考：540（+4.3%）上方 / 495（-4.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 4.2k / P 4.1k
ΔOI:      C +0.2k / P +37
ATM:      C 0.00 / P 32.10
ATM IV:   38.2%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 630 ｜ +166 ｜ $0.99 ｜ 名义 $16.4k* ｜ +21.6%
P 410 ｜ +28 ｜ $1.17 ｜ 名义 $3.3k* ｜ -20.8%
C 575 ｜ +19 ｜ $5.30 ｜ 名义 $10.1k* ｜ +11.0%
结构参考：630（+21.6%）上方 / 410（-20.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/SOXX_morning.json