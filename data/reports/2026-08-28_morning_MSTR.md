# 期权晨报 2026-08-28

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: -2.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-25 130P ΔOI +305（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 139.06 → 今晨 132.85（-4.5%） | 较昨收变动（含盘初走势） ｜ 今日高 135.96 ｜ 低 130.88

Options: P/C量 0.35 | OI比 0.83 | ATM IV 95.6% | Skew -6.0pp | Term 0.72 | ExpMove ±1.9%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（7D）±7.6% ｜ 09-11（14D）±10.3% ｜ 09-18（21D）±13.0% ｜ 09-25（28D）±15.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 881 / LOW 107 / INVALID 366
结构观察区: NO_CROSS
Put Wall 60（现价高于该位 121.4%） | Call Wall 100（现价高于该位 32.9%）
最近结构参考: Call Wall 100（现价高于该位 32.9%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 60（Put Wall）；上方 100（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 140.0C — Vol 7,639 | 最新价 $2.65 | OI 1519→19657 (ΔOI +18138张) | ΔOI/Volume 237.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18138张（+1194.1% vs前日OI），连续性待观察（方向未知）
09-04 146.0C — Vol 3,707 | 最新价 $1.48 | OI 120→16574 (ΔOI +16454张) | ΔOI/Volume 443.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16454张（+13711.7% vs前日OI），连续性待观察（方向未知）
08-28 134.0C — Vol 15,328 | 最新价 $0.70 | OI 1536→11106 (ΔOI +9570张) | ΔOI/Volume 62.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9570张（+623.0% vs前日OI），连续性待观察（方向未知）
09-04 147.0C — Vol 174 | 最新价 $1.36 | OI 51→8339 (ΔOI +8288张) | ΔOI/Volume 4763.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8288张（+16251.0% vs前日OI），连续性待观察（方向未知）
08-28 138.0C — Vol 7,554 | 最新价 $0.13 | OI 492→7720 (ΔOI +7228张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7228张（+1469.1% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +81.5k / P +21.4k ｜ Activity HIGH ｜ 7D
09-11  C +2.8k / P +3.4k ｜ Activity HIGH ｜ 14D
09-18  C +8.6k / P +3.4k ｜ Activity HIGH ｜ 21D
09-25  C +0.6k / P +1.0k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 133.7k / P 128.1k
ΔOI:      C +81.5k / P +21.4k
ATM:      C 5.00 / P 5.08
ATM IV:   68.4%
ΔOI Δ Exposure*: 1.3M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 140 ｜ +18,138 ｜ $2.65 ｜ 名义 $4.81M* ｜ +5.4%
C 146 ｜ +16,454 ｜ $1.48 ｜ 名义 $2.44M* ｜ +9.9%
C 147 ｜ +8,288 ｜ $1.36 ｜ 名义 $1.13M* ｜ +10.7%
结构参考：140（+5.4%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 23.4k / P 50.4k
ΔOI:      C +2.8k / P +3.4k
ATM:      C 6.90 / P 6.85
ATM IV:   65.7%
ΔOI Δ Exposure*: 37k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 85 ｜ +1,683 ｜ $0.16 ｜ 名义 $26.9k* ｜ -36.0%
C 140 ｜ +843 ｜ $4.35 ｜ 名义 $366.7k* ｜ +5.4%
C 124 ｜ +646 ｜ $12.05 ｜ 名义 $778.4k* ｜ -6.7%
结构参考：140（+5.4%）上方 / 85（-36.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 257.7k / P 176.0k
ΔOI:      C +8.6k / P +3.4k
ATM:      C 8.62 / P 8.60
ATM IV:   68.0%
ΔOI Δ Exposure*: -165k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +3,657 ｜ $0.49 ｜ 名义 $179.2k* ｜ +50.5%
C 180 ｜ +2,838 ｜ $0.94 ｜ 名义 $266.8k* ｜ +35.5%
C 220 ｜ +2,651 ｜ $0.27 ｜ 名义 $71.6k* ｜ +65.6%
结构参考：200（+50.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 13.9k / P 17.3k
ΔOI:      C +0.6k / P +1.0k
ATM:      C 10.35 / P 9.53
ATM IV:   68.7%
ΔOI Δ Exposure*: -33k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 140 ｜ -393 ｜ $7.55 ｜ 名义 $-296.7k* ｜ +5.4%
P 130 ｜ +305 ｜ $8.40 ｜ 名义 $256.2k* ｜ -2.1%
P 120 ｜ +255 ｜ $4.35 ｜ 名义 $110.9k* ｜ -9.7%
结构参考：130（-2.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/MSTR_morning.json