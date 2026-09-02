# 期权晚报 2026-09-02（快照 18:14 ET）

📊 市场环境

SPY $765.16 ｜ QQQ $709.24
VIX 15.20 ↓7.0%（5D -1.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（2D）ATM IV 89.0% vs 09-11 73.0%（差 +16.1pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 17.36 → 收盘 17.85（+2.8%） ｜ 今日高 17.90 ｜ 低 17.28
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.31 | OI比 0.31 | ATM IV 89.0% | Skew 1.6pp | Term 0.93 | ExpMove ±5.2%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常（Term 0.93）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±5.2% ｜ 09-11（9D）±9.2% ｜ 09-18（16D）±13.1% ｜ 09-25（23D）±15.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,093,170 | GEX Change vs 上次快照 2,170,303 | Flip: Primary Flip: 17.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 264 / LOW 112 / INVALID 152
结构观察区: Primary Flip 17.06（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 4.6%）
量化视角： 正 Gamma（609万，无历史分位）｜正 Gamma 增强（+217万）｜现价位于 Flip 上方 4.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 19.0C — Vol 404 | 最新价 $0.70 | OI 3557→4123 (ΔOI +566张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增566张（+15.9% vs前日OI），值得跟踪（方向未知）
09-04 17.0P — Vol 258 | 最新价 $0.17 | OI 1538→1907 (ΔOI +369张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增369张（+24.0% vs前日OI），值得跟踪（方向未知）
09-04 16.5P — Vol 168 | 最新价 $0.09 | OI 1599→1956 (ΔOI +357张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增357张（+22.3% vs前日OI），值得跟踪（方向未知）
09-11 17.5P — Vol 90 | 最新价 $0.66 | OI 137→430 (ΔOI +293张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增293张（+213.9% vs前日OI），值得跟踪（方向未知）
10-02 24.0C — Vol 73 | 最新价 $0.27 | OI 149→426 (ΔOI +277张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增277张（+185.9% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,862 张（Put 1,019 / Call 843），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 16D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 32.4k / P 10.0k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 0.38 / P 0.55
隐含波动率 ATM IV:  89.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 89.0%｜历史 Rank 7%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 89.0% vs 09-11 73.0%（差 +16.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/USAR_evening.json