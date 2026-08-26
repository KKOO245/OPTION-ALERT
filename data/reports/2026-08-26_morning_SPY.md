# 期权晨报 2026-08-26

📊 市场环境

SPY $769.98 ｜ QQQ $711.37
VIX 15.62 ↑1.1%（5D +4.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 55.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 08-26 08:30　【高】Personal Spending MoM　预测 0.1 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周三 08-26 08:30　【高】Personal Income MoM　预测 0.2 ｜ 实际 0.4 ｜ 前值 0.2　✅ 今日已公布
- 周三 08-26 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 1.5 ｜ 实际 1.5 ｜ 前值 2.1　✅ 今日已公布
- 周三 08-26 08:30　【高】耐用品订单 Orders MoM　预测 0.5 ｜ 实际 1.1 ｜ 前值 0.5　✅ 今日已公布
- 周三 08-26 08:30　【高】PCE 物价 Price Index MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## SPY

🔍 重点速览
🟡 **近现价集中开仓**: 08-27 765P ΔOI +2,215（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-01 685P ΔOI +7,679 占该期限总 OI 11.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 765.95 → 今晨 764.88（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 766.96 ｜ 低 763.93

Options: P/C量 1.10 | OI比 1.70 | ATM IV 20.0% | Skew 3.0pp | Term 0.63 | ExpMove ±0.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.70×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 08-27（1D）±0.7% ｜ 08-28（2D）±0.9% ｜ 08-31（5D）±1.1% ｜ 09-01（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_FLIP_IN_RANGE
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: 待审计
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: NO_FLIP_IN_RANGE
距 Put Wall 535: +43.0% | 距 Call Wall 800: -4.4%
最近结构参考: Call Wall 800（距现价 -4.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 535（Put Wall）；上方 800（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 728.0P — Vol N/A | OI 17566→35832 (ΔOI +18266张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增18266张（+104.0% vs前日OI），连续性待观察（方向未知）
09-04 760.0P — Vol N/A | OI 27360→44755 (ΔOI +17395张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增17395张（+63.6% vs前日OI），连续性待观察（方向未知）
08-26 742.0P — Vol N/A | OI 326→8370 (ΔOI +8044张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增8044张（+2467.5% vs前日OI），连续性待观察（方向未知）
09-01 685.0P — Vol N/A | OI 16→7695 (ΔOI +7679张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增7679张（+47993.8% vs前日OI），连续性待观察（方向未知）
09-30 754.0P — Vol N/A | OI 6816→14345 (ΔOI +7529张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增7529张（+110.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-27  C +14.6k / P +14.0k ｜ Activity HIGH ｜ 1D
08-28  C +16.8k / P +19.5k ｜ Activity HIGH ｜ 2D
08-31  C +4.6k / P +19.9k ｜ Activity HIGH ｜ 5D
09-01  C +12.2k / P +14.9k ｜ Activity HIGH ｜ 6D

📆 08-27 Forward Structure
OI:       C 63.6k / P 75.5k
ΔOI:      C +14.6k / P +14.0k
ATM:      C 2.62 / P 2.73
ATM IV:   15.5%
ΔOI Δ Exposure*: -26k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 765 ｜ +2,215 ｜ $2.73 ｜ 名义 $604.7k* ｜ +0.0%
P 760 ｜ +1,715 ｜ $1.05 ｜ 名义 $180.1k* ｜ -0.6%
C 775 ｜ +1,698 ｜ $0.15 ｜ 名义 $25.5k* ｜ +1.3%
结构参考：775（+1.3%）上方 / 760（-0.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-28 Forward Structure
OI:       C 220.1k / P 308.5k
ΔOI:      C +16.8k / P +19.5k
ATM:      C 3.67 / P 3.60
ATM IV:   15.4%
ΔOI Δ Exposure*: 294k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 720 ｜ +4,086 ｜ $0.03 ｜ 名义 $12.3k* ｜ -5.9%
P 721 ｜ +3,094 ｜ $0.04 ｜ 名义 $12.4k* ｜ -5.7%
C 766 ｜ +2,900 ｜ $3.15 ｜ 名义 $913.5k* ｜ +0.1%
结构参考：766（+0.1%）上方 / 720（-5.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 318.3k / P 700.0k
ΔOI:      C +4.6k / P +19.9k
ATM:      C 4.36 / P 4.20
ATM IV:   11.8%
ΔOI Δ Exposure*: 46k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 701 ｜ +6,378 ｜ $0.05 ｜ 名义 $31.9k* ｜ -8.4%
P 682 ｜ +3,879 ｜ $0.02 ｜ 名义 $7.8k* ｜ -10.8%
P 681 ｜ +3,274 ｜ $0.02 ｜ 名义 $6.5k* ｜ -11.0%
结构参考：701（-8.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-01 Forward Structure
OI:       C 36.8k / P 32.2k
ΔOI:      C +12.2k / P +14.9k
ATM:      C 4.91 / P 4.59
ATM IV:   11.9%
ΔOI Δ Exposure*: 73k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 685 ｜ +7,679 ｜ $0.03 ｜ 名义 $23.0k* ｜ -10.4%
C 799 ｜ +2,077 ｜ $0.01 ｜ 名义 $2.1k* ｜ +4.5%
C 800 ｜ +1,636 ｜ $0.03 ｜ 名义 $4.9k* ｜ +4.6%
结构参考：799（+4.5%）上方 / 685（-10.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-26/SPY_morning.json