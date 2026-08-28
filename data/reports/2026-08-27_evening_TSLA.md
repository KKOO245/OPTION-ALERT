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
🟡 **事件差分**: 08-28 ATM IV 42.5% vs 08-31 32.2%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 08-28 345P ΔOI +4,819（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
TSLA: 今晨 353.55 → 收盘 354.65（+0.3%） ｜ 今日高 355.74 ｜ 低 345.45
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.60 | OI比 0.82 | ATM IV 42.5% | Skew -0.9pp | Term 0.92 | ExpMove ±1.8%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-28（1D）±1.8% ｜ 08-31（4D）±2.7% ｜ 09-02（6D）±3.8% ｜ 09-04（8D）±4.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 343.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1199 / LOW 242 / INVALID 731
结构观察区: ≈344（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 200: +77.3% | 距 Call Wall 400: -11.3%
最近结构参考: Flip 344（距现价 +3.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 400（Call Wall）。
• Gamma 区域：切换参考 344（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 345.0P — Vol 53,720 | 最新价 $0.45 | OI 3637→8456 (ΔOI +4819张) | ΔOI/Volume 9.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4819张（+132.5% vs前日OI），连续性待观察（方向未知）
09-18 400.0C — Vol 9,219 | 最新价 $2.35 | OI 21314→24948 (ΔOI +3634张) | ΔOI/Volume 39.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3634张（+17.1% vs前日OI），连续性待观察（方向未知）
08-28 350.0C — Vol 75,659 | 最新价 $6.00 | OI 6894→10383 (ΔOI +3489张) | ΔOI/Volume 4.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3489张（+50.6% vs前日OI），连续性待观察（方向未知）
08-28 355.0C — Vol 119,389 | 最新价 $3.09 | OI 6393→9842 (ΔOI +3449张) | ΔOI/Volume 2.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3449张（+54.0% vs前日OI），连续性待观察（方向未知）
08-28 360.0C — Vol 114,755 | 最新价 $1.36 | OI 10154→13582 (ΔOI +3428张) | ΔOI/Volume 3.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3428张（+33.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +20.7k / P +12.7k ｜ Activity MEDIUM △ ｜ 1D
08-31  C +4.8k / P +4.1k ｜ Activity HIGH ｜ 4D
09-02  C +3.8k / P +1.7k ｜ Activity HIGH ｜ 6D
09-04  C +7.8k / P +7.8k ｜ Activity HIGH ｜ 8D

   Top ΔOI: 345P +4,819 ｜ 350C +3,489

📆 08-31 Forward Structure
OI:       C 47.0k / P 18.1k
ΔOI:      C +4.8k / P +4.1k
ATM:      C 4.70 / P 4.85
ATM IV:   32.2%
ΔOI Δ Exposure*: 130k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 345 ｜ +1,764 ｜ $1.38 ｜ 名义 $243.4k* ｜ -2.7%
C 350 ｜ +682 ｜ $7.60 ｜ 名义 $518.3k* ｜ -1.3%
C 370 ｜ +552 ｜ $0.77 ｜ 名义 $42.5k* ｜ +4.3%
结构参考：370（+4.3%）上方 / 345（-2.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 18.6k / P 10.1k
ΔOI:      C +3.8k / P +1.7k
ATM:      C 6.70 / P 6.80
ATM IV:   36.8%
ΔOI Δ Exposure*: 136k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 350 ｜ +1,251 ｜ $9.30 ｜ 名义 $1.16M* ｜ -1.3%
C 355 ｜ +663 ｜ $6.70 ｜ 名义 $444.2k* ｜ +0.1%
C 440 ｜ +407 ｜ $0.05 ｜ 名义 $2.0k* ｜ +24.1%
结构参考：355（+0.1%）上方 / 350（-1.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 74.7k / P 63.8k
ΔOI:      C +7.8k / P +7.8k
ATM:      C 8.40 / P 8.38
ATM IV:   39.8%
ΔOI Δ Exposure*: 296k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 140 ｜ +1,975 ｜ $0.02 ｜ 名义 $4.0k* ｜ -60.5%
C 360 ｜ +1,481 ｜ $6.25 ｜ 名义 $925.6k* ｜ +1.5%
P 110 ｜ +1,226 ｜ $0.01 ｜ 名义 $1.2k* ｜ -69.0%
结构参考：360（+1.5%）上方 / 140（-60.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 42.5% vs 08-31 32.2%（差 +10.3pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/TSLA_evening.json