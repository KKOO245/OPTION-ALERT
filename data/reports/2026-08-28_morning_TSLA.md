# 期权晨报 2026-08-28

📊 市场环境

SPY $774.48 ｜ QQQ $722.97
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 56.4（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 08-31 355C ΔOI +1,403（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 354.65 → 今晨 353.89（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 358.80 ｜ 低 351.21

Options: P/C量 0.49 | OI比 0.84 | ATM IV 45.8% | Skew -0.7pp | Term 0.82 | ExpMove ±1.0%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-31（3D）±2.1% ｜ 09-02（5D）±3.1% ｜ 09-04（7D）±4.2% ｜ 09-09（12D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 342.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1285 / LOW 160 / INVALID 767
结构观察区: Primary Flip 342.99（全链重定价，覆盖 97%）
Put Wall 340（现价高于该位 4.1%） | Call Wall 400（现价低于该位 11.5%）
最近结构参考: Flip 343（现价高于该位 3.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall）；上方 400（Call Wall）。
• Gamma 区域：切换参考 343（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 372.5C — Vol 2,650 | 最新价 $1.80 | OI 328→5778 (ΔOI +5450张) | ΔOI/Volume 205.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5450张（+1661.6% vs前日OI），连续性待观察（方向未知）
08-31 315.0P — Vol 6 | 最新价 $0.04 | OI 232→5241 (ΔOI +5009张) | ΔOI/Volume 83483.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5009张（+2159.1% vs前日OI），连续性待观察（方向未知）
08-28 360.0C — Vol 138,535 | 最新价 $0.17 | OI 13582→18413 (ΔOI +4831张) | ΔOI/Volume 3.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4831张（+35.6% vs前日OI），连续性待观察（方向未知）
08-28 370.0C — Vol 15,580 | 最新价 $0.03 | OI 12178→16897 (ΔOI +4719张) | ΔOI/Volume 30.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4719张（+38.8% vs前日OI），连续性待观察（方向未知）
09-04 360.0C — Vol 10,743 | 最新价 $4.72 | OI 5511→8859 (ΔOI +3348张) | ΔOI/Volume 31.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3348张（+60.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C +8.8k / P +8.2k ｜ Activity HIGH ｜ 3D
09-02  C +1.6k / P +2.3k ｜ Activity HIGH ｜ 5D
09-04  C +27.1k / P +13.9k ｜ Activity HIGH ｜ 7D
09-09  C +2.4k / P +0.6k ｜ Activity HIGH ｜ 12D

📆 08-31 Forward Structure
OI:       C 55.8k / P 26.3k
ΔOI:      C +8.8k / P +8.2k
ATM:      C 2.89 / P 4.42
ATM IV:   27.0%
ΔOI Δ Exposure*: 91k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 315 ｜ +5,009 ｜ $0.04 ｜ 名义 $20.0k* ｜ -11.0%
C 355 ｜ +1,403 ｜ $2.89 ｜ 名义 $405.5k* ｜ +0.3%
C 370 ｜ +862 ｜ $0.24 ｜ 名义 $20.7k* ｜ +4.6%
结构参考：355（+0.3%）上方 / 315（-11.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 20.2k / P 12.4k
ΔOI:      C +1.6k / P +2.3k
ATM:      C 4.91 / P 6.25
ATM IV:   33.4%
ΔOI Δ Exposure*: -67k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 355 ｜ -681 ｜ $4.91 ｜ 名义 $-334.4k* ｜ +0.3%
C 380 ｜ +415 ｜ $0.42 ｜ 名义 $17.4k* ｜ +7.4%
P 335 ｜ +326 ｜ $0.70 ｜ 名义 $22.8k* ｜ -5.3%
结构参考：380（+7.4%）上方 / 335（-5.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 101.8k / P 77.7k
ΔOI:      C +27.1k / P +13.9k
ATM:      C 6.75 / P 8.10
ATM IV:   37.1%
ΔOI Δ Exposure*: 413k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 372 ｜ +5,450 ｜ $1.80 ｜ 名义 $981.0k* ｜ +5.3%
C 360 ｜ +3,348 ｜ $4.72 ｜ 名义 $1.58M* ｜ +1.7%
C 375 ｜ +2,595 ｜ $1.47 ｜ 名义 $381.5k* ｜ +6.0%
结构参考：372（+5.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 5.3k / P 1.9k
ΔOI:      C +2.4k / P +0.6k
ATM:      C 8.38 / P 9.25
ATM IV:   34.3%
ΔOI Δ Exposure*: 19k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 375 ｜ +407 ｜ $2.59 ｜ 名义 $105.4k* ｜ +6.0%
C 400 ｜ +354 ｜ $0.54 ｜ 名义 $19.1k* ｜ +13.0%
C 420 ｜ +327 ｜ $0.25 ｜ 名义 $8.2k* ｜ +18.7%
结构参考：375（+6.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/TSLA_morning.json