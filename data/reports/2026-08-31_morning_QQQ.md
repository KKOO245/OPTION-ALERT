# 期权晨报 2026-08-31

📊 市场环境

SPY $767.25 ｜ QQQ $716.76
VIX 15.16 ↑5.1%（5D -4.3%） ｜ Vol Regime: NORMAL
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-01 725C ΔOI +6,213（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 716.43 → 今晨 715.11（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 717.00 ｜ 低 713.16

Options: P/C量 1.18 | OI比 0.91 | ATM IV 15.0% | Skew 1.7pp | Term 1.12 | ExpMove ±0.7%（近端） | Rank 28%
   ⇒ Put/Call Volume: 1.18×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 38% ｜ P/C OI(近端) 3%
   ExpMove 期限化（expmove_v1）: 09-01（1D）±0.7% ｜ 09-02（2D）±0.9% ｜ 09-03（3D）±1.1% ｜ 09-04（4D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -186,907,179 | GEX Change vs 上次快照 -224,065,704 | Flip: Primary Flip: 717.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 2742 / LOW 584 / INVALID 2326
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 717.35（全链重定价，覆盖 91%）
Put Wall 700（弱结构｜现价高于该位 2.2%） | Call Wall 750（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 717（现价低于该位 0.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 717（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 687.0P — Vol 8 | 最新价 $6.12 | OI 225→14228 (ΔOI +14003张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14003张（+6223.6% vs前日OI），连续性待观察（方向未知）
09-30 681.0P — Vol 6 | 最新价 $4.88 | OI 159→14159 (ΔOI +14000张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14000张（+8805.0% vs前日OI），连续性待观察（方向未知）
09-11 500.0P — Vol 0 | 最新价 $0.03 | OI 140→13203 (ΔOI +13063张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13063张（+9330.7% vs前日OI），连续性待观察（方向未知）
08-31 695.0P — Vol 1,590 | 最新价 $0.03 | OI 8797→20112 (ΔOI +11315张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11315张（+128.6% vs前日OI），连续性待观察（方向未知）
09-01 500.0P — Vol 0 | 最新价 $0.01 | OI 12257→22256 (ΔOI +9999张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9999张（+81.6% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-01  C +20.0k / P +24.1k ｜ Activity HIGH ｜ 1D
09-02  C +6.8k / P +12.6k ｜ Activity HIGH ｜ 2D
09-03  C +5.3k / P +14.3k ｜ Activity HIGH ｜ 3D
09-04  C +23.2k / P +26.6k ｜ Activity HIGH ｜ 4D

📆 09-01 Forward Structure
OI:       C 52.8k / P 112.7k
ΔOI:      C +20.0k / P +24.1k
ATM:      C 2.42 / P 2.35
ATM IV:   14.7%
ΔOI Δ Exposure*: -65k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 500 ｜ +9,999 ｜ $0.01 ｜ 名义 $10.0k* ｜ -30.1%
C 725 ｜ +6,213 ｜ $0.10 ｜ 名义 $62.1k* ｜ +1.4%
P 525 ｜ +5,310 ｜ $0.01 ｜ 名义 $5.3k* ｜ -26.6%
结构参考：725（+1.4%）上方 / 500（-30.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 22.7k / P 63.0k
ΔOI:      C +6.8k / P +12.6k
ATM:      C 3.36 / P 3.19
ATM IV:   15.0%
ΔOI Δ Exposure*: -146k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 700 ｜ +4,535 ｜ $0.33 ｜ 名义 $149.7k* ｜ -2.1%
P 690 ｜ +2,015 ｜ $0.11 ｜ 名义 $22.2k* ｜ -3.5%
C 730 ｜ +1,394 ｜ $0.09 ｜ 名义 $12.5k* ｜ +2.1%
结构参考：730（+2.1%）上方 / 700（-2.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-03 Forward Structure
OI:       C 20.6k / P 40.8k
ΔOI:      C +5.3k / P +14.3k
ATM:      C 4.27 / P 3.98
ATM IV:   15.6%
ΔOI Δ Exposure*: 59k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 655 ｜ +6,066 ｜ $0.04 ｜ 名义 $24.3k* ｜ -8.4%
P 660 ｜ +5,503 ｜ $0.05 ｜ 名义 $27.5k* ｜ -7.7%
C 720 ｜ +2,701 ｜ $2.03 ｜ 名义 $548.3k* ｜ +0.7%
结构参考：720（+0.7%）上方 / 655（-8.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 166.3k / P 189.2k
ΔOI:      C +23.2k / P +26.6k
ATM:      C 5.27 / P 4.77
ATM IV:   16.4%
ΔOI Δ Exposure*: 82k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 722 ｜ +3,171 ｜ $2.06 ｜ 名义 $653.2k* ｜ +1.0%
P 710 ｜ +1,743 ｜ $2.92 ｜ 名义 $509.0k* ｜ -0.7%
C 725 ｜ +1,684 ｜ $1.38 ｜ 名义 $232.4k* ｜ +1.4%
结构参考：722（+1.0%）上方 / 710（-0.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/QQQ_morning.json