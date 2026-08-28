# 期权晚报 2026-08-27

📊 市场环境

SPY $771.10 ｜ QQQ $721.11
VIX 14.51 ↓4.6%（5D -9.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 08-28 ATM IV 97.5% vs 09-04 84.1%（差 +13.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NBIS

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
NBIS: 今晨 219.56 → 收盘 214.44（-2.3%） ｜ 今日高 228.50 ｜ 低 215.41
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.52 | OI比 0.87 | ATM IV 97.5% | Skew -1.0pp | Term 0.87 | ExpMove ±4.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-28（1D）±4.3% ｜ 09-04（8D）±10.1% ｜ 09-11（15D）±12.9% ｜ 09-18（22D）±17.1%
   ⇒ IV–VIX Spread: +83.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 219.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 681 / LOW 60 / INVALID 117
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈220（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 200: +7.2% | 距 Call Wall 250: -14.2%
最近结构参考: Flip 220（距现价 -2.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 220（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 180.0P — Vol 413 | 最新价 $0.03 | OI 2063→2679 (ΔOI +616张) | ΔOI/Volume 149.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增616张（+29.9% vs前日OI），连续性待观察（方向未知）
08-28 235.0C — Vol 3,258 | 最新价 $0.55 | OI 1687→2244 (ΔOI +557张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增557张（+33.0% vs前日OI），连续性待观察（方向未知）
08-28 300.0C — Vol 754 | 最新价 $0.01 | OI 3394→3914 (ΔOI +520张) | ΔOI/Volume 69.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增520张（+15.3% vs前日OI），连续性待观察（方向未知）
08-28 245.0C — Vol 2,828 | 最新价 $0.13 | OI 1792→2288 (ΔOI +496张) | ΔOI/Volume 17.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增496张（+27.7% vs前日OI），连续性待观察（方向未知）
08-28 155.0P — Vol 342 | 最新价 $0.01 | OI 2000→2429 (ΔOI +429张) | ΔOI/Volume 125.4% | Magnitude: HIGH | 完整度: HIGH
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
ATM:      C 12.70 / P 8.95
ATM IV:   84.1%
ΔOI Δ Exposure*: -14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 180 ｜ +247 ｜ $0.85 ｜ 名义 $21.0k* ｜ -16.1%
C 215 ｜ +203 ｜ $12.70 ｜ 名义 $257.8k* ｜ +0.3%
C 300 ｜ +144 ｜ $0.24 ｜ 名义 $3.5k* ｜ +39.9%
结构参考：215（+0.3%）上方 / 180（-16.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 7.6k / P 11.7k
ΔOI:      C +0.4k / P +0.6k
ATM:      C 15.05 / P 12.62
ATM IV:   82.4%
ΔOI Δ Exposure*: 104 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 300 ｜ +224 ｜ $0.80 ｜ 名义 $17.9k* ｜ +39.9%
P 100 ｜ +83 ｜ $0.07 ｜ 名义 $581* ｜ -53.4%
P 165 ｜ +62 ｜ $0.87 ｜ 名义 $5.4k* ｜ -23.1%
结构参考：300（+39.9%）上方 / 100（-53.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 97.5% vs 09-04 84.1%（差 +13.5pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/NBIS_evening.json