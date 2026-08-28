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
🟡 **近现价集中开仓**: 08-28 778C ΔOI +3,347（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SPY: 今晨 770.53 → 收盘 771.10（+0.1%） ｜ 今日高 772.35 ｜ 低 767.16
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 1.08 | OI比 1.36 | ATM IV 13.1% | Skew 2.7pp | Term 0.88 | ExpMove ±0.6%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.36×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±0.6% ｜ 08-31（4D）±0.8% ｜ 09-01（5D）±0.9% ｜ 09-02（6D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 769.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3335 / LOW 459 / INVALID 1704
结构观察区: ≈769（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 535: +44.1% | 距 Call Wall 800: -3.6%
最近结构参考: Flip 769（距现价 +0.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 535（Put Wall）；上方 800（Call Wall）。
• Gamma 区域：切换参考 769（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 800.0C — Vol 4,150 | 最新价 $1.54 | OI 50235→64519 (ΔOI +14284张) | ΔOI/Volume 344.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14284张（+28.4% vs前日OI），连续性待观察（方向未知）
09-04 760.0P — Vol 51,184 | 最新价 $1.70 | OI 44755→57595 (ΔOI +12840张) | ΔOI/Volume 25.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12840张（+28.7% vs前日OI），连续性待观察（方向未知）
08-31 745.0P — Vol 15,289 | 最新价 $0.07 | OI 10095→22058 (ΔOI +11963张) | ΔOI/Volume 78.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11963张（+118.5% vs前日OI），连续性待观察（方向未知）
09-04 747.0P — Vol 17,061 | 最新价 $0.56 | OI 785→11075 (ΔOI +10290张) | ΔOI/Volume 60.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10290张（+1310.8% vs前日OI），连续性待观察（方向未知）
10-02 795.0C — Vol 132 | 最新价 $2.63 | OI 321→7649 (ΔOI +7328张) | ΔOI/Volume 5551.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7328张（+2282.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +16.2k / P +12.1k ｜ Activity MEDIUM △ ｜ 1D
08-31  C +13.0k / P +23.3k ｜ Activity MEDIUM △ ｜ 4D
09-01  C +9.1k / P +8.2k ｜ Activity HIGH ｜ 5D
09-02  C +6.4k / P +9.6k ｜ Activity HIGH ｜ 6D

   Top ΔOI: 712P +4,985 ｜ 713P +4,146

   Top ΔOI: 745P +11,963 ｜ 769C +3,699

📆 09-01 Forward Structure
OI:       C 45.9k / P 40.4k
ΔOI:      C +9.1k / P +8.2k
ATM:      C 3.27 / P 3.45
ATM IV:   9.3%
ΔOI Δ Exposure*: 217k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 782 ｜ +3,564 ｜ $0.21 ｜ 名义 $74.8k* ｜ +1.4%
P 739 ｜ +2,147 ｜ $0.11 ｜ 名义 $23.6k* ｜ -4.2%
P 761 ｜ +2,063 ｜ $0.89 ｜ 名义 $183.6k* ｜ -1.3%
结构参考：782（+1.4%）上方 / 739（-4.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 24.6k / P 31.9k
ΔOI:      C +6.4k / P +9.6k
ATM:      C 3.76 / P 3.92
ATM IV:   9.7%
ΔOI Δ Exposure*: 202k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 750 ｜ +1,325 ｜ $0.35 ｜ 名义 $46.4k* ｜ -2.7%
P 766 ｜ +1,003 ｜ $2.14 ｜ 名义 $214.6k* ｜ -0.7%
C 775 ｜ +988 ｜ $1.90 ｜ 名义 $187.7k* ｜ +0.5%
结构参考：775（+0.5%）上方 / 750（-2.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/SPY_evening.json