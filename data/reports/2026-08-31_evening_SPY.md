# 期权晚报 2026-08-31

📊 市场环境

SPY $767.05 ｜ QQQ $716.76
VIX 14.92 ↑3.4%（5D -5.9%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 待公布 ｜ 前值 7.359
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 待公布 ｜ 前值 55.6
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-01 775C ΔOI +5,086（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 767.33 → 收盘 767.05（-0.0%） ｜ 今日高 767.99 ｜ 低 764.72
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 1.16 | OI比 2.03 | ATM IV 12.9% | Skew 1.7pp | Term 0.91 | ExpMove ±0.4%（近端） | Rank 50%
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.03×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 40% ｜ P/C OI(近端) 64%
   ExpMove 期限化（expmove_v1）: 09-01（1D）±0.4% ｜ 09-02（2D）±0.6% ｜ 09-03（3D）±0.8% ｜ 09-04（4D）±1.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -690,463,518 | GEX Change vs 上次快照 163,602,460 | Flip: Primary Flip: 771.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 3187 / LOW 591 / INVALID 2038
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 771.94（全链重定价，覆盖 88%）
Call Wall 800（弱结构｜现价低于该位 4.1%）
最近结构参考: Flip 772（现价低于该位 0.6%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 772（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 761.0P — Vol 353 | 最新价 $7.81 | OI 208→22115 (ΔOI +21907张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21907张（+10532.2% vs前日OI），连续性待观察（方向未知）
09-11 580.0P — Vol 107 | 最新价 $0.03 | OI 191→18136 (ΔOI +17945张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17945张（+9395.3% vs前日OI），连续性待观察（方向未知）
09-18 790.0C — Vol 5,226 | 最新价 $0.78 | OI 46965→62043 (ΔOI +15078张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15078张（+32.1% vs前日OI），连续性待观察（方向未知）
09-04 765.0P — Vol 27,407 | 最新价 $2.49 | OI 52483→63684 (ΔOI +11201张) | ΔOI/Volume 40.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11201张（+21.3% vs前日OI），连续性待观察（方向未知）
09-04 800.0C — Vol 358 | 最新价 $0.02 | OI 5424→15535 (ΔOI +10111张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10111张（+186.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-01  C +21.1k / P +16.8k ｜ Activity HIGH ｜ 1D
09-02  C +10.2k / P +17.7k ｜ Activity HIGH ｜ 2D
09-03  C +11.1k / P +21.4k ｜ Activity HIGH ｜ 3D
09-04  C +52.2k / P +40.9k ｜ Activity HIGH ｜ 4D

📆 09-01 Forward Structure
OI:       C 75.0k / P 65.5k
ΔOI:      C +21.1k / P +16.8k
ATM:      C 1.79 / P 1.43
ATM IV:   10.0%
ΔOI Δ Exposure*: -477k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 775 ｜ +5,086 ｜ $0.04 ｜ 名义 $20.3k* ｜ +1.0%
C 776 ｜ +2,009 ｜ $0.03 ｜ 名义 $6.0k* ｜ +1.2%
C 773 ｜ +1,777 ｜ $0.11 ｜ 名义 $19.5k* ｜ +0.8%
结构参考：775（+1.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 45.7k / P 80.5k
ΔOI:      C +10.2k / P +17.7k
ATM:      C 2.59 / P 2.10
ATM IV:   10.3%
ΔOI Δ Exposure*: -241k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 766 ｜ +2,756 ｜ $1.71 ｜ 名义 $471.3k* ｜ -0.1%
P 695 ｜ +2,117 ｜ $0.03 ｜ 名义 $6.4k* ｜ -9.4%
P 769 ｜ +1,347 ｜ $3.07 ｜ 名义 $413.5k* ｜ +0.3%
结构参考：769（+0.3%）上方 / 766（-0.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-03 Forward Structure
OI:       C 38.7k / P 50.0k
ΔOI:      C +11.1k / P +21.4k
ATM:      C 3.22 / P 2.69
ATM IV:   10.6%
ΔOI Δ Exposure*: -110k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 720 ｜ +7,609 ｜ $0.03 ｜ 名义 $22.8k* ｜ -6.1%
P 710 ｜ +6,143 ｜ $0.03 ｜ 名义 $18.4k* ｜ -7.4%
C 784 ｜ +1,924 ｜ $0.02 ｜ 名义 $3.8k* ｜ +2.2%
结构参考：784（+2.2%）上方 / 720（-6.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 308.6k / P 342.9k
ΔOI:      C +52.2k / P +40.9k
ATM:      C 4.11 / P 3.24
ATM IV:   11.3%
ΔOI Δ Exposure*: -716k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 765 ｜ +11,201 ｜ $2.49 ｜ 名义 $2.79M* ｜ -0.3%
C 800 ｜ +10,111 ｜ $0.02 ｜ 名义 $20.2k* ｜ +4.3%
P 760 ｜ -10,052 ｜ $1.28 ｜ 名义 $-1.29M* ｜ -0.9%
结构参考：800（+4.3%）上方 / 765（-0.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/SPY_evening.json