# 期权晨报 2026-08-31

📊 市场环境

SPY $765.41 ｜ QQQ $715.09
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
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-01 775C ΔOI +5,086（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 769.35 → 今晨 765.41（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 767.61 ｜ 低 764.72

Options: P/C量 1.24 | OI比 2.03 | ATM IV 12.3% | Skew 0.9pp | Term 0.98 | ExpMove ±0.5%（近端） | Rank 46%
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.03×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 32% ｜ P/C OI(近端) 64%
   ExpMove 期限化（expmove_v1）: 09-01（1D）±0.5% ｜ 09-02（2D）±0.7% ｜ 09-03（3D）±0.8% ｜ 09-04（4D）±1.0%
   ⇒ IV–VIX Spread: -2.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,061,262,464 | GEX Change vs 上次快照 -819,127,856 | Flip: Primary Flip: 770.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 3321 / LOW 591 / INVALID 1904
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.92（全链重定价，覆盖 91%）
Call Wall 800（弱结构｜现价低于该位 4.3%）
最近结构参考: Flip 771（现价低于该位 0.7%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 771（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 761.0P — Vol 191 | 最新价 $8.52 | OI 208→22115 (ΔOI +21907张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21907张（+10532.2% vs前日OI），连续性待观察（方向未知）
09-11 580.0P — Vol 0 | 最新价 $0.04 | OI 191→18136 (ΔOI +17945张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17945张（+9395.3% vs前日OI），连续性待观察（方向未知）
09-18 790.0C — Vol 1,693 | 最新价 $0.68 | OI 46965→62043 (ΔOI +15078张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15078张（+32.1% vs前日OI），连续性待观察（方向未知）
09-04 765.0P — Vol 6,959 | 最新价 $3.36 | OI 52483→63684 (ΔOI +11201张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11201张（+21.3% vs前日OI），连续性待观察（方向未知）
09-04 800.0C — Vol 162 | 最新价 $0.01 | OI 5424→15535 (ΔOI +10111张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10111张（+186.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-01  C +21.1k / P +16.8k ｜ Activity HIGH ｜ 1D
09-02  C +10.2k / P +17.7k ｜ Activity HIGH ｜ 2D
09-03  C +11.1k / P +21.4k ｜ Activity HIGH ｜ 3D
09-04  C +52.2k / P +40.9k ｜ Activity HIGH ｜ 4D

📆 09-01 Forward Structure
OI:       C 75.0k / P 65.5k
ΔOI:      C +21.1k / P +16.8k
ATM:      C 2.16 / P 1.57
ATM IV:   10.8%
ΔOI Δ Exposure*: -614k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 775 ｜ +5,086 ｜ $0.03 ｜ 名义 $15.3k* ｜ +1.3%
C 776 ｜ +2,009 ｜ $0.03 ｜ 名义 $6.0k* ｜ +1.4%
C 773 ｜ +1,777 ｜ $0.09 ｜ 名义 $16.0k* ｜ +1.0%
结构参考：775（+1.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 45.7k / P 80.5k
ΔOI:      C +10.2k / P +17.7k
ATM:      C 2.88 / P 2.22
ATM IV:   10.8%
ΔOI Δ Exposure*: -376k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 766 ｜ +2,756 ｜ $2.65 ｜ 名义 $730.3k* ｜ +0.1%
P 695 ｜ +2,117 ｜ $0.03 ｜ 名义 $6.4k* ｜ -9.2%
P 769 ｜ +1,347 ｜ $4.49 ｜ 名义 $604.8k* ｜ +0.5%
结构参考：766（+0.1%）上方 / 695（-9.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-03 Forward Structure
OI:       C 38.7k / P 50.0k
ΔOI:      C +11.1k / P +21.4k
ATM:      C 3.51 / P 2.78
ATM IV:   11.0%
ΔOI Δ Exposure*: -154k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 720 ｜ +7,609 ｜ $0.06 ｜ 名义 $45.7k* ｜ -5.9%
P 710 ｜ +6,143 ｜ $0.03 ｜ 名义 $18.4k* ｜ -7.2%
C 784 ｜ +1,924 ｜ $0.02 ｜ 名义 $3.8k* ｜ +2.4%
结构参考：784（+2.4%）上方 / 720（-5.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 308.6k / P 342.9k
ΔOI:      C +52.2k / P +40.9k
ATM:      C 4.38 / P 3.34
ATM IV:   11.6%
ΔOI Δ Exposure*: -1.0M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 765 ｜ +11,201 ｜ $3.34 ｜ 名义 $3.74M* ｜ -0.1%
C 800 ｜ +10,111 ｜ $0.02 ｜ 名义 $20.2k* ｜ +4.5%
P 760 ｜ -10,052 ｜ $1.75 ｜ 名义 $-1.76M* ｜ -0.7%
结构参考：800（+4.5%）上方 / 765（-0.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=3 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=3）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/SPY_morning.json