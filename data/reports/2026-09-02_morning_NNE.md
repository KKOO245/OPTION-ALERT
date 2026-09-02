# 期权晨报 2026-09-02（快照 11:19 ET）

📊 市场环境

SPY $764.94 ｜ QQQ $709.24
VIX 15.51 ↓5.1%（5D +0.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（2D）ATM IV 86.5% vs 09-11 68.7%（差 +17.8pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.47 → 今开 17.43（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 17.70 ｜ 低 17.17

Options: P/C成交量 0.27 | OI比 0.69 | ATM IV 86.5% | Skew 6.2pp | Term 0.88 | ExpMove ±5.8%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 6.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±5.8% ｜ 09-11（9D）±9.0% ｜ 09-18（16D）±13.3% ｜ 09-25（23D）±14.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 190,928 | GEX Change vs 上次快照 -98,024 | Flip: Primary Flip: 17.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 220 / LOW 87 / INVALID 159
结构观察区: Primary Flip 17.11（全链重定价，覆盖 93%）
Put Wall 16（弱结构｜现价高于该位 8.0%）
最近结构参考: Flip 17（现价高于该位 1.0%）
量化视角： 正 Gamma（19万，无历史分位）｜正 Gamma 减弱（10万）｜现价位于 Flip 上方 0.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 15.0P — Vol 194（Yahoo补） | 最新价 $0.37 | OI 27→197 (ΔOI +170张) | ΔOI/Volume 87.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增170张（+629.6% vs前日OI），连续性待观察（方向未知）
09-04 17.0P — Vol 42 | 最新价 $0.25 | OI 361→519 (ΔOI +158张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增158张（+43.8% vs前日OI），值得跟踪（方向未知）
10-02 17.0P — Vol 110（Yahoo补） | 最新价 $1.26 | OI 14→123 (ΔOI +109张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增109张（+778.6% vs前日OI），连续性待观察（方向未知）
09-18 15.0P — Vol 1 | 最新价 $0.30 | OI 244→352 (ΔOI +108张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增108张（+44.3% vs前日OI），值得跟踪（方向未知）
09-18 18.0C — Vol 2 | 最新价 $0.83 | OI 145→245 (ΔOI +100张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增100张（+69.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 645 张（Put 545 / Call 100），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +84 / P +0.2k ｜ Activity MEDIUM △ ｜ 2D
09-11  C +46 / P +48 ｜ Activity LOW ｜ 9D
09-18  C +0.1k / P +0.1k ｜ Activity LOW ｜ 16D
09-25  C +36 / P +0.2k ｜ Activity HIGH ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 3.4k / P 2.4k
今日变化ΔOI: C +84 / P +0.2k
平值价格ATM:  C 0.55 / P 0.45
隐含波动率 ATM IV:  86.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 641 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +158 ｜ $0.25 ｜ 名义 $4.0k* ｜ -1.6%
C 18 ｜ +59 ｜ $0.20 ｜ 名义 $1.2k* ｜ +7.1%
C 17 ｜ +51 ｜ $0.55 ｜ 名义 $2.8k* ｜ +1.3%
结构参考：18（+7.1%） / 17（-1.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 86.5%｜历史 Rank 12%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 641 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 4.3k / P 0.8k
今日变化ΔOI: C +36 / P +0.2k
平值价格ATM:  C 1.20 / P 1.23
隐含波动率 ATM IV:  71.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 71.9%｜历史 Rank 12%（近端代理）｜净 delta 敞口 负 2,433 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 86.5% vs 09-11 68.7%（差 +17.8pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/NNE_morning.json