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
🟡 **近现价集中开仓**: 09-11 215P ΔOI +78（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
BE: 今晨 218.16 → 收盘 215.90（-1.0%） ｜ 今日高 227.99 ｜ 低 214.75
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.65 | OI比 0.87 | ATM IV 87.2% | Skew -5.0pp | Term 0.98 | ExpMove ±3.8%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-28（1D）±3.9% ｜ 09-04（8D）±10.4% ｜ 09-11（15D）±13.8% ｜ 09-18（22D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 205.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 593 / LOW 84 / INVALID 175
结构观察区: ≈206（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 180: +19.9% | 距 Call Wall 250: -13.6%
最近结构参考: Flip 206（距现价 +4.8%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 206（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 235.0C — Vol 1,381 | 最新价 $0.33 | OI 1334→2617 (ΔOI +1283张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1283张（+96.2% vs前日OI），连续性待观察（方向未知）
08-28 255.0C — Vol 577 | 最新价 $0.03 | OI 336→1292 (ΔOI +956张) | ΔOI/Volume 165.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增956张（+284.5% vs前日OI），连续性待观察（方向未知）
09-11 130.0P — Vol 24 | 最新价 $0.12 | OI 92→961 (ΔOI +869张) | ΔOI/Volume 3620.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增869张（+944.6% vs前日OI），连续性待观察（方向未知）
09-04 145.0P — Vol 7 | 最新价 $0.13 | OI 331→1148 (ΔOI +817张) | ΔOI/Volume 11671.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增817张（+246.8% vs前日OI），连续性待观察（方向未知）
09-18 125.0P — Vol 10 | 最新价 $0.17 | OI 671→1380 (ΔOI +709张) | ΔOI/Volume 7090.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增709张（+105.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +6.1k / P +0.8k ｜ Activity HIGH ｜ 1D
09-04  C +0.7k / P +2.9k ｜ Activity HIGH ｜ 8D
09-11  C +0.3k / P +1.3k ｜ Activity HIGH ｜ 15D
09-18  C +1.5k / P +1.2k ｜ Activity MEDIUM △ ｜ 22D

📆 08-28 Forward Structure
OI:       C 53.6k / P 46.6k
ΔOI:      C +6.1k / P +0.8k
ATM:      C 5.70 / P 2.71
ATM IV:   87.2%
ΔOI Δ Exposure*: 64k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +1,283 ｜ $0.33 ｜ 名义 $42.3k* ｜ +8.8%
C 255 ｜ +956 ｜ $0.03 ｜ 名义 $2.9k* ｜ +18.1%
C 230 ｜ +697 ｜ $0.75 ｜ 名义 $52.3k* ｜ +6.5%
结构参考：235（+8.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 16.4k / P 26.3k
ΔOI:      C +0.7k / P +2.9k
ATM:      C 12.75 / P 9.73
ATM IV:   86.7%
ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 145 ｜ +817 ｜ $0.13 ｜ 名义 $10.6k* ｜ -32.8%
C 355 ｜ -775 ｜ $0.05 ｜ 名义 $-3.9k* ｜ +64.4%
P 180 ｜ +408 ｜ $0.78 ｜ 名义 $31.8k* ｜ -16.6%
结构参考：145（-32.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 13.3k / P 10.5k
ΔOI:      C +0.3k / P +1.3k
ATM:      C 16.80 / P 13.05
ATM IV:   85.5%
ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 130 ｜ +869 ｜ $0.12 ｜ 名义 $10.4k* ｜ -39.8%
P 165 ｜ +101 ｜ $0.75 ｜ 名义 $7.6k* ｜ -23.6%
P 215 ｜ +78 ｜ $13.05 ｜ 名义 $101.8k* ｜ -0.4%
结构参考：130（-39.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 125P +709 ｜ 460C +301

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/BE_evening.json