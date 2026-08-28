# 期权晨报 2026-08-28

📊 市场环境

SPY $769.10 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 08-31 235C ΔOI +7,817（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-04 235C ΔOI +125,068 占该期限总 OI 13.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 226.14 → 今晨 224.01（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 229.26 ｜ 低 223.26

Options: P/C量 0.59 | OI比 0.73 | ATM IV 45.2% | Skew 0.8pp | Term 0.72 | ExpMove ±0.9%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-31（3D）±2.0% ｜ 09-02（5D）±3.0% ｜ 09-04（7D）±3.8% ｜ 09-09（12D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 210.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 695 / LOW 241 / INVALID 372
结构观察区: Primary Flip 210.34（全链重定价，覆盖 96%）
Put Wall 190（现价高于该位 17.9%） | Call Wall 240（现价低于该位 6.7%）
最近结构参考: Flip 210（现价高于该位 6.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall）；上方 240（Call Wall）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 235.0C — Vol 9,536 | 最新价 $0.98 | OI 12849→137917 (ΔOI +125068张) | ΔOI/Volume 1311.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增125068张（+973.4% vs前日OI），连续性待观察（方向未知）
09-04 245.0C — Vol 4,101 | 最新价 $0.22 | OI 8630→119067 (ΔOI +110437张) | ΔOI/Volume 2692.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增110437张（+1279.7% vs前日OI），连续性待观察（方向未知）
09-04 225.0C — Vol 11,965 | 最新价 $3.83 | OI 13259→60417 (ΔOI +47158张) | ΔOI/Volume 394.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47158张（+355.7% vs前日OI），连续性待观察（方向未知）
09-18 265.0C — Vol 510 | 最新价 $0.22 | OI 10779→51468 (ΔOI +40689张) | ΔOI/Volume 7978.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40689张（+377.5% vs前日OI），连续性待观察（方向未知）
08-28 170.0P — Vol 22 | 最新价 $0.01 | OI 30149→62451 (ΔOI +32302张) | ΔOI/Volume 146827.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32302张（+107.1% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-31  C +24.6k / P +27.5k ｜ Activity HIGH ｜ 3D
09-02  C +5.4k / P +22.9k ｜ Activity HIGH ｜ 5D
09-04  C +365.3k / P +74.9k ｜ Activity HIGH ｜ 7D
09-09  C +30.5k / P +4.7k ｜ Activity HIGH ｜ 12D

📆 08-31 Forward Structure
OI:       C 141.7k / P 90.3k
ΔOI:      C +24.6k / P +27.5k
ATM:      C 1.75 / P 2.73
ATM IV:   26.2%
ΔOI Δ Exposure*: -1.4M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +7,817 ｜ $0.13 ｜ 名义 $101.6k* ｜ +4.9%
C 225 ｜ +6,754 ｜ $1.75 ｜ 名义 $1.18M* ｜ +0.4%
C 230 ｜ +4,566 ｜ $0.47 ｜ 名义 $214.6k* ｜ +2.7%
结构参考：235（+4.9%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 56.3k / P 43.5k
ΔOI:      C +5.4k / P +22.9k
ATM:      C 2.95 / P 3.80
ATM IV:   31.5%
ΔOI Δ Exposure*: -701k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 202 ｜ +3,455 ｜ $0.15 ｜ 名义 $51.8k* ｜ -9.6%
P 220 ｜ +3,329 ｜ $1.66 ｜ 名义 $552.6k* ｜ -1.8%
P 207 ｜ +3,190 ｜ $0.22 ｜ 名义 $70.2k* ｜ -7.4%
结构参考：202（-9.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 577.4k / P 324.6k
ΔOI:      C +365.3k / P +74.9k
ATM:      C 3.83 / P 4.60
ATM IV:   33.4%
ΔOI Δ Exposure*: 3.0M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 235 ｜ +125,068 ｜ $0.98 ｜ 名义 $12.26M* ｜ +4.9%
C 245 ｜ +110,437 ｜ $0.22 ｜ 名义 $2.43M* ｜ +9.4%
C 225 ｜ +47,158 ｜ $3.83 ｜ 名义 $18.06M* ｜ +0.4%
结构参考：235（+4.9%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-09 Forward Structure
OI:       C 44.8k / P 8.5k
ΔOI:      C +30.5k / P +4.7k
ATM:      C 4.68 / P 5.40
ATM IV:   30.7%
ΔOI Δ Exposure*: 339k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 240 ｜ +11,671 ｜ $0.90 ｜ 名义 $1.05M* ｜ +7.1%
C 230 ｜ +8,891 ｜ $2.80 ｜ 名义 $2.49M* ｜ +2.7%
C 250 ｜ +6,481 ｜ $0.25 ｜ 名义 $162.0k* ｜ +11.6%
结构参考：240（+7.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/NVDA_morning.json