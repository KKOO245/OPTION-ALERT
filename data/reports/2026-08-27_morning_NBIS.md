# 期权晨报 2026-08-27

📊 市场环境

SPY $771.10 ｜ QQQ $721.11
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -3.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 08-28 ATM IV 100.6% vs 09-04 86.9%（差 +13.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 228.19 → 今晨 219.56（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 228.50 ｜ 低 216.80

Options: P/C量 0.47 | OI比 0.87 | ATM IV 100.6% | Skew -2.9pp | Term 0.88 | ExpMove ±4.7%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-28（1D）±4.7% ｜ 09-04（8D）±10.2% ｜ 09-11（15D）±14.6% ｜ 09-18（22D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 218.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 667 / LOW 61 / INVALID 130
结构观察区: ≈218（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 200: +9.8% | 距 Call Wall 250: -12.2%
最近结构参考: Flip 218（距现价 +0.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 218（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 180.0P — Vol 193 | 最新价 $0.03 | OI 2063→2679 (ΔOI +616张) | ΔOI/Volume 319.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增616张（+29.9% vs前日OI），连续性待观察（方向未知）
08-28 235.0C — Vol 1,858 | 最新价 $0.94 | OI 1687→2244 (ΔOI +557张) | ΔOI/Volume 30.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增557张（+33.0% vs前日OI），连续性待观察（方向未知）
08-28 300.0C — Vol 124 | 最新价 $0.01 | OI 3394→3914 (ΔOI +520张) | ΔOI/Volume 419.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增520张（+15.3% vs前日OI），连续性待观察（方向未知）
08-28 245.0C — Vol 1,156 | 最新价 $0.30 | OI 1792→2288 (ΔOI +496张) | ΔOI/Volume 42.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增496张（+27.7% vs前日OI），连续性待观察（方向未知）
08-28 155.0P — Vol 254 | 最新价 $0.02 | OI 2000→2429 (ΔOI +429张) | ΔOI/Volume 168.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增429张（+21.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +3.2k / P +0.9k ｜ Activity MEDIUM △ ｜ 1D
09-04  C +1.3k / P +1.7k ｜ Activity HIGH ｜ 8D
09-11  C +0.4k / P +0.6k ｜ Activity HIGH ｜ 15D
09-18  C +0.2k / P +0.1k ｜ Activity LOW ｜ 22D

   Top ΔOI: 190P -719 ｜ 180P +616

📆 09-04 Forward Structure
OI:       C 32.0k / P 22.6k
ΔOI:      C +1.3k / P +1.7k
ATM:      C 11.30 / P 11.10
ATM IV:   86.9%
ΔOI Δ Exposure*: -10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 180 ｜ +247 ｜ $0.80 ｜ 名义 $19.8k* ｜ -18.0%
C 215 ｜ +203 ｜ $14.20 ｜ 名义 $288.3k* ｜ -2.1%
C 300 ｜ +144 ｜ $0.35 ｜ 名义 $5.0k* ｜ +36.6%
结构参考：300（+36.6%）上方 / 180（-18.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 7.6k / P 11.7k
ΔOI:      C +0.4k / P +0.6k
ATM:      C 17.00 / P 15.00
ATM IV:   83.7%
ΔOI Δ Exposure*: 846 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 300 ｜ +224 ｜ $1.20 ｜ 名义 $26.9k* ｜ +36.6%
P 100 ｜ +83 ｜ $0.07 ｜ 名义 $581* ｜ -54.5%
P 165 ｜ +62 ｜ $0.81 ｜ 名义 $5.0k* ｜ -24.8%
结构参考：300（+36.6%）上方 / 100（-54.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 100.6% vs 09-04 86.9%（差 +13.6pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/NBIS_morning.json