# 期权晨报 2026-08-27

📊 市场环境

SPY $770.63 ｜ QQQ $719.17
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.3（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## BE

🔍 重点速览
🟡 **单日价格波动**: -3.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 215P ΔOI +78（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 226.99 → 今晨 218.16（-3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 227.99 ｜ 低 214.75

Options: P/C量 0.58 | OI比 0.87 | ATM IV 94.1% | Skew -6.1pp | Term 0.92 | ExpMove ±4.4%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-28（1D）±4.3% ｜ 09-04（8D）±11.2% ｜ 09-11（15D）±14.2% ｜ 09-18（22D）±16.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 203.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 635 / LOW 72 / INVALID 145
结构观察区: ≈204（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 180: +21.2% | 距 Call Wall 250: -12.7%
最近结构参考: Flip 204（距现价 +7.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 204（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 235.0C — Vol 864 | 最新价 $0.67 | OI 1334→2617 (ΔOI +1283张) | ΔOI/Volume 148.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1283张（+96.2% vs前日OI），连续性待观察（方向未知）
08-28 255.0C — Vol 401 | 最新价 $0.05 | OI 336→1292 (ΔOI +956张) | ΔOI/Volume 238.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增956张（+284.5% vs前日OI），连续性待观察（方向未知）
09-11 130.0P — Vol 23 | 最新价 $0.11 | OI 92→961 (ΔOI +869张) | ΔOI/Volume 3778.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增869张（+944.6% vs前日OI），连续性待观察（方向未知）
09-04 145.0P — Vol 3 | 最新价 $0.13 | OI 331→1148 (ΔOI +817张) | ΔOI/Volume 27233.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增817张（+246.8% vs前日OI），连续性待观察（方向未知）
09-18 125.0P — Vol 1 | 最新价 $0.20 | OI 671→1380 (ΔOI +709张) | ΔOI/Volume 70900.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增709张（+105.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +6.1k / P +0.8k ｜ Activity HIGH ｜ 1D
09-04  C +0.7k / P +2.9k ｜ Activity HIGH ｜ 8D
09-11  C +0.3k / P +1.3k ｜ Activity HIGH ｜ 15D
09-18  C +1.5k / P +1.2k ｜ Activity HIGH ｜ 22D

📆 08-28 Forward Structure
OI:       C 53.6k / P 46.6k
ΔOI:      C +6.1k / P +0.8k
ATM:      C 4.98 / P 4.50
ATM IV:   94.1%
ΔOI Δ Exposure*: 73k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +1,283 ｜ $0.67 ｜ 名义 $86.0k* ｜ +7.7%
C 255 ｜ +956 ｜ $0.05 ｜ 名义 $4.8k* ｜ +16.9%
C 230 ｜ +697 ｜ $1.25 ｜ 名义 $87.1k* ｜ +5.4%
结构参考：235（+7.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 16.4k / P 26.3k
ΔOI:      C +0.7k / P +2.9k
ATM:      C 12.52 / P 11.85
ATM IV:   90.5%
ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 145 ｜ +817 ｜ $0.13 ｜ 名义 $10.6k* ｜ -33.5%
C 355 ｜ -775 ｜ $0.09 ｜ 名义 $-7.0k* ｜ +62.7%
P 180 ｜ +408 ｜ $1.02 ｜ 名义 $41.6k* ｜ -17.5%
结构参考：145（-33.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 13.3k / P 10.5k
ΔOI:      C +0.3k / P +1.3k
ATM:      C 15.70 / P 15.29
ATM IV:   88.7%
ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 130 ｜ +869 ｜ $0.11 ｜ 名义 $9.6k* ｜ -40.4%
P 165 ｜ +101 ｜ $0.95 ｜ 名义 $9.6k* ｜ -24.4%
P 215 ｜ +78 ｜ $14.05 ｜ 名义 $109.6k* ｜ -1.4%
结构参考：130（-40.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 114.9k / P 91.4k
ΔOI:      C +1.5k / P +1.2k
ATM:      C 19.45 / P 17.50
ATM IV:   86.3%
ΔOI Δ Exposure*: 14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 125 ｜ +709 ｜ $0.20 ｜ 名义 $14.2k* ｜ -42.7%
C 460 ｜ +301 ｜ $0.10 ｜ 名义 $3.0k* ｜ +110.9%
C 250 ｜ +282 ｜ $8.50 ｜ 名义 $239.7k* ｜ +14.6%
结构参考：460（+110.9%）上方 / 125（-42.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/BE_morning.json