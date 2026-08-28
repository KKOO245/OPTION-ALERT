# 期权晨报 2026-08-28

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 08-31 700P ΔOI +5,503（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-01 495P ΔOI +13,081 占该期限总 OI 10.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 718.75 → 今晨 723.02（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 724.12 ｜ 低 716.79

Options: P/C量 1.04 | OI比 1.03 | ATM IV 17.9% | Skew 2.9pp | Term 0.95 | ExpMove ±0.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-31（3D）±0.8% ｜ 09-01（4D）±1.0% ｜ 09-02（5D）±1.2% ｜ 09-03（6D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 715.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3173 / LOW 483 / INVALID 2026
结构观察区: Primary Flip 715.85（全链重定价，覆盖 94%）
Put Wall 700（现价高于该位 3.3%） | Call Wall 730（现价低于该位 1.0%）
最近结构参考: Call Wall 730（现价低于该位 1.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall）；上方 730（Call Wall）。
• Gamma 区域：切换参考 716（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 690.0P — Vol 7,384 | 最新价 $4.38 | OI 1040→14966 (ΔOI +13926张) | ΔOI/Volume 188.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13926张（+1339.0% vs前日OI），连续性待观察（方向未知）
09-01 495.0P — Vol 0 | 最新价 $0.01 | OI 20→13101 (ΔOI +13081张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13081张（+65405.0% vs前日OI），连续性待观察（方向未知）
09-01 500.0P — Vol 0 | 最新价 $0.01 | OI 1→12257 (ΔOI +12256张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12256张（+1225600.0% vs前日OI），连续性待观察（方向未知）
09-18 730.0C — Vol 4,899 | 最新价 $8.68 | OI 31073→42943 (ΔOI +11870张) | ΔOI/Volume 242.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11870张（+38.2% vs前日OI），连续性待观察（方向未知）
08-31 525.0P — Vol 0 | 最新价 $0.01 | OI 128→9657 (ΔOI +9529张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9529张（+7444.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C -6.8k / P +35.9k ｜ Activity HIGH ｜ 3D
09-01  C +3.6k / P +37.5k ｜ Activity HIGH ｜ 4D
09-02  C +2.6k / P +27.9k ｜ Activity HIGH ｜ 5D
09-03  C +6.1k / P +8.7k ｜ Activity HIGH ｜ 6D

📆 08-31 Forward Structure
OI:       C 381.2k / P 288.5k
ΔOI:      C -6.8k / P +35.9k
ATM:      C 2.76 / P 2.82
ATM IV:   10.2%
ΔOI Δ Exposure*: -821k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 525 ｜ +9,529 ｜ $0.01 ｜ 名义 $9.5k* ｜ -27.4%
P 700 ｜ +5,503 ｜ $0.09 ｜ 名义 $49.5k* ｜ -3.2%
P 650 ｜ +4,667 ｜ $0.03 ｜ 名义 $14.0k* ｜ -10.1%
结构参考：525（-27.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-01 Forward Structure
OI:       C 32.8k / P 88.5k
ΔOI:      C +3.6k / P +37.5k
ATM:      C 3.65 / P 3.71
ATM IV:   11.8%
ΔOI Δ Exposure*: 42k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 495 ｜ +13,081 ｜ $0.01 ｜ 名义 $13.1k* ｜ -31.5%
P 500 ｜ +12,256 ｜ $0.01 ｜ 名义 $12.3k* ｜ -30.8%
P 505 ｜ +3,840 ｜ $0.01 ｜ 名义 $3.8k* ｜ -30.2%
结构参考：495（-31.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 15.9k / P 50.3k
ΔOI:      C +2.6k / P +27.9k
ATM:      C 4.49 / P 4.38
ATM IV:   12.9%
ΔOI Δ Exposure*: -92k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 655 ｜ +9,395 ｜ $0.06 ｜ 名义 $56.4k* ｜ -9.4%
P 691 ｜ +7,681 ｜ $0.22 ｜ 名义 $169.0k* ｜ -4.4%
P 650 ｜ +5,892 ｜ $0.04 ｜ 名义 $23.6k* ｜ -10.1%
结构参考：655（-9.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-03 Forward Structure
OI:       C 15.3k / P 26.5k
ΔOI:      C +6.1k / P +8.7k
ATM:      C 5.47 / P 5.17
ATM IV:   13.7%
ΔOI Δ Exposure*: 55k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 733 ｜ +1,443 ｜ $1.49 ｜ 名义 $215.0k* ｜ +1.4%
P 703 ｜ +1,141 ｜ $0.79 ｜ 名义 $90.1k* ｜ -2.8%
P 710 ｜ +697 ｜ $1.58 ｜ 名义 $110.1k* ｜ -1.8%
结构参考：733（+1.4%）上方 / 703（-2.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/QQQ_morning.json