# 期权晨报 2026-09-02（快照 11:19 ET）

📊 市场环境

SPY $765.76 ｜ QQQ $709.03
VIX 15.51 ↓5.1%（5D +0.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 09-04 ATM IV 89.8% vs 09-11 76.4%（差 +13.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 17.26 → 今开 17.36（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 17.90 ｜ 低 17.28

Options: P/C成交量 0.29 | OI比 0.31 | ATM IV 89.8% | Skew -4.0pp | Term 0.92 | ExpMove ±6.1%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±6.1% ｜ 09-11（9D）±9.6% ｜ 09-18（16D）±13.1% ｜ 09-25（23D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,922,866 | GEX Change vs 上次快照 1,092,181 | Flip: Primary Flip: 17.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 246 / LOW 104 / INVALID 178
结构观察区: Primary Flip 17.03（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 3.2%）
量化视角： 正 Gamma（392万，无历史分位）｜正 Gamma 增强（+109万）｜现价位于 Flip 上方 3.23%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 19.0C — Vol 74 | 最新价 $0.71 | OI 3557→4123 (ΔOI +566张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增566张（+15.9% vs前日OI），值得跟踪（方向未知）
09-04 17.0P — Vol 87 | 最新价 $0.21 | OI 1538→1907 (ΔOI +369张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增369张（+24.0% vs前日OI），值得跟踪（方向未知）
09-04 16.5P — Vol 14 | 最新价 $0.07 | OI 1599→1956 (ΔOI +357张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增357张（+22.3% vs前日OI），值得跟踪（方向未知）
09-11 17.5P — Vol 38 | 最新价 $0.68 | OI 137→430 (ΔOI +293张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增293张（+213.9% vs前日OI），值得跟踪（方向未知）
10-02 24.0C — Vol 17 | 最新价 $0.28 | OI 149→426 (ΔOI +277张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增277张（+185.9% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,862 张（Put 1,019 / Call 843），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 2D
09-11  C +0.2k / P +0.6k ｜ Activity HIGH ｜ 9D
09-18  C +0.5k / P -1.0k ｜ Activity HIGH ｜ 16D
09-25  C -25 / P +0.1k ｜ Activity LOW ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 32.4k / P 10.0k
今日变化ΔOI: C +0.4k / P +0.3k
平值价格ATM:  C 0.67 / P 0.40
隐含波动率 ATM IV:  89.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 38k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ -407 ｜ $0.65 ｜ 名义 $-26.5k* ｜ +2.4%
P 17 ｜ +369 ｜ $0.20 ｜ 名义 $7.4k* ｜ -3.3%
P 16 ｜ +357 ｜ $0.10 ｜ 名义 $3.6k* ｜ -6.2%
结构参考：17（-3.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 89.8%｜历史 Rank 7%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 38,410 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 12.2k / P 3.5k
今日变化ΔOI: C +0.2k / P +0.6k
平值价格ATM:  C 0.96 / P 0.72
隐含波动率 ATM IV:  76.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -16k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +293 ｜ $0.72 ｜ 名义 $21.1k* ｜ -0.5%
P 16 ｜ +80 ｜ $0.31 ｜ 名义 $2.5k* ｜ -6.2%
C 18 ｜ +75 ｜ $0.52 ｜ 名义 $3.9k* ｜ +5.2%
结构参考：18（+5.2%） / 17（-0.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.4%｜历史 Rank 7%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 15,971 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 111.9k / P 64.5k
今日变化ΔOI: C +0.5k / P -1.0k
平值价格ATM:  C 1.23 / P 1.08
隐含波动率 ATM IV:  77.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 119k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +566 ｜ $0.67 ｜ 名义 $37.9k* ｜ +8.0%
P 27 ｜ -360 ｜ $9.08 ｜ 名义 $-326.9k* ｜ +53.5%
P 19 ｜ -243 ｜ $2.85 ｜ 名义 $-69.3k* ｜ +10.9%
结构参考：19（+8.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 77.8%｜历史 Rank 7%（近端代理）｜净 delta 敞口 正 118,967 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 89.8% vs 09-11 76.4%（差 +13.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/USAR_morning.json