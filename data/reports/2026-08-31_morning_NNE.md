# 期权晨报 2026-08-31

📊 市场环境

SPY $765.79 ｜ QQQ $714.45
VIX 15.33 ↑6.2%（5D -3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 50.4（neutral）
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
🟡 **近现价集中开仓**: 09-04 17P ΔOI +121（距现价 -3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.97 → 今晨 18.15（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 18.38 ｜ 低 17.80

Options: P/C量 2.81 | OI比 0.76 | ATM IV 76.4% | Skew -0.0pp | Term 1.10 | ExpMove ±7.9%（近端） | Rank 4%
   ⇒ Put/Call Volume: 2.81×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±8.3% ｜ 09-11（11D）±10.4% ｜ 09-18（18D）±14.8% ｜ 09-25（25D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 17.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 194 / LOW 64 / INVALID 208
结构观察区: Primary Flip 17.15（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 5.8%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 22.5C — Vol 2,303 | 最新价 $0.55 | OI 44→2023 (ΔOI +1979张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1979张（+4497.7% vs前日OI），连续性待观察（方向未知）
09-11 16.0P — Vol 189 | 最新价 $0.25 | OI 194→383 (ΔOI +189张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增189张（+97.4% vs前日OI），连续性待观察（方向未知）
09-11 18.5P — Vol 189 | 最新价 $1.18 | OI 56→244 (ΔOI +188张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增188张（+335.7% vs前日OI），连续性待观察（方向未知）
09-04 16.0P — Vol 131 | 最新价 $0.11 | OI 470→600 (ΔOI +130张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增130张（+27.7% vs前日OI），连续性待观察（方向未知）
09-18 18.0P — Vol 167 | 最新价 $1.40 | OI 573→695 (ΔOI +122张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增122张（+21.3% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +0.1k / P +0.6k ｜ Activity HIGH ｜ 4D
09-11  C +68 / P +0.6k ｜ Activity HIGH ｜ 11D
09-18  C -31 / P +0.4k ｜ Activity HIGH ｜ 18D
09-25  C -6 / P +38 ｜ Activity MEDIUM △ ｜ 25D

📆 09-04 Forward Structure
OI:       C 2.4k / P 1.8k
ΔOI:      C +0.1k / P +0.6k
ATM:      C 0.75 / P 0.75
ATM IV:   76.4%
ΔOI Δ Exposure*: -16k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +130 ｜ $0.11 ｜ 名义 $1.4k* ｜ -11.8%
P 17 ｜ +121 ｜ $0.58 ｜ 名义 $7.0k* ｜ -3.6%
P 17 ｜ +69 ｜ $0.31 ｜ 名义 $2.1k* ｜ -6.3%
结构参考：16（-11.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.2k / P 1.5k
ΔOI:      C +68 / P +0.6k
ATM:      C 1.13 / P 0.75
ATM IV:   73.7%
ΔOI Δ Exposure*: -23k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +189 ｜ $0.25 ｜ 名义 $4.7k* ｜ -11.8%
P 18 ｜ +188 ｜ $1.18 ｜ 名义 $22.2k* ｜ +1.9%
P 20 ｜ +84 ｜ $2.52 ｜ 名义 $21.2k* ｜ +12.9%
结构参考：18（+1.9%）上方 / 16（-11.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 4.7k / P 3.0k
ΔOI:      C -31 / P +0.4k
ATM:      C 1.29 / P 1.40
ATM IV:   79.5%
ΔOI Δ Exposure*: -17k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ +122 ｜ $1.40 ｜ 名义 $17.1k* ｜ -0.8%
P 26 ｜ +94 ｜ $7.83 ｜ 名义 $73.6k* ｜ +43.3%
P 17 ｜ +40 ｜ $1.10 ｜ 名义 $4.4k* ｜ -3.6%
结构参考：26（+43.3%）上方 / 18（-0.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 17P +25 ｜ 22C -20

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/NNE_morning.json