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
🟡 **近现价集中开仓**: 08-31 64C ΔOI +1,522（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-02 60P ΔOI +2,199 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 62.77 → 今晨 62.77（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 64.29 ｜ 低 61.62

Options: P/C量 0.64 | OI比 0.57 | ATM IV 50.6% | Skew -4.2pp | Term 0.86 | ExpMove ±1.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-31（3D）±2.2% ｜ 09-02（5D）±3.5% ｜ 09-04（7D）±4.6% ｜ 09-09（12D）±6.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 55.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1100 / LOW 287 / INVALID 493
结构观察区: Primary Flip 55.06（全链重定价，覆盖 96%）
Put Wall 50（现价高于该位 25.5%） | Call Wall 70（现价低于该位 10.3%）
最近结构参考: Call Wall 70（现价低于该位 10.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall）；上方 70（Call Wall）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 60.0P — Vol 964 | 最新价 $1.27 | OI 13346→17436 (ΔOI +4090张) | ΔOI/Volume 424.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4090张（+30.6% vs前日OI），连续性待观察（方向未知）
09-04 69.0C — Vol 451 | 最新价 $0.20 | OI 319→4379 (ΔOI +4060张) | ΔOI/Volume 900.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4060张（+1272.7% vs前日OI），连续性待观察（方向未知）
09-04 67.0C — Vol 308 | 最新价 $0.37 | OI 1067→5093 (ΔOI +4026张) | ΔOI/Volume 1307.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4026张（+377.3% vs前日OI），连续性待观察（方向未知）
08-28 60.0P — Vol 1,967 | 最新价 $0.01 | OI 4433→7212 (ΔOI +2779张) | ΔOI/Volume 141.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2779张（+62.7% vs前日OI），连续性待观察（方向未知）
09-30 63.0C — Vol 149 | 最新价 $3.25 | OI 2141→4753 (ΔOI +2612张) | ΔOI/Volume 1753.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2612张（+122.0% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C +4.8k / P +1.3k ｜ Activity HIGH ｜ 3D
09-02  C +4.6k / P +3.0k ｜ Activity HIGH ｜ 5D
09-04  C +11.3k / P +3.0k ｜ Activity HIGH ｜ 7D
09-09  C +1.1k / P +0.4k ｜ Activity HIGH ｜ 12D

📆 08-31 Forward Structure
OI:       C 55.8k / P 9.9k
ΔOI:      C +4.8k / P +1.3k
ATM:      C 0.55 / P 0.82
ATM IV:   31.3%
ΔOI Δ Exposure*: 58k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 64 ｜ +1,522 ｜ $0.30 ｜ 名义 $45.7k* ｜ +2.0%
C 74 ｜ +931 ｜ $0.01 ｜ 名义 $931* ｜ +17.9%
P 62 ｜ +549 ｜ $0.38 ｜ 名义 $20.9k* ｜ -1.2%
结构参考：64（+2.0%）上方 / 62（-1.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 14.8k / P 7.0k
ΔOI:      C +4.6k / P +3.0k
ATM:      C 0.92 / P 1.29
ATM IV:   36.8%
ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 60 ｜ +2,199 ｜ $0.17 ｜ 名义 $37.4k* ｜ -4.4%
C 69 ｜ +1,945 ｜ $0.07 ｜ 名义 $13.6k* ｜ +9.9%
C 67 ｜ +547 ｜ $0.23 ｜ 名义 $12.6k* ｜ +6.7%
结构参考：69（+9.9%）上方 / 60（-4.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 70.7k / P 33.4k
ΔOI:      C +11.3k / P +3.0k
ATM:      C 1.33 / P 1.53
ATM IV:   40.8%
ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 69 ｜ +4,060 ｜ $0.20 ｜ 名义 $81.2k* ｜ +9.9%
C 67 ｜ +4,026 ｜ $0.37 ｜ 名义 $149.0k* ｜ +6.7%
P 63 ｜ +1,566 ｜ $1.87 ｜ 名义 $292.8k* ｜ +1.2%
结构参考：69（+9.9%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 2.4k / P 1.1k
ΔOI:      C +1.1k / P +0.4k
ATM:      C 1.68 / P 2.19
ATM IV:   38.1%
ΔOI Δ Exposure*: 37k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 63 ｜ +262 ｜ $1.62 ｜ 名义 $42.4k* ｜ +1.2%
C 62 ｜ +146 ｜ $1.86 ｜ 名义 $27.2k* ｜ -0.4%
C 62 ｜ +138 ｜ $2.07 ｜ 名义 $28.6k* ｜ -1.2%
结构参考：63（+1.2%）上方 / 62（-0.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/SLV_morning.json