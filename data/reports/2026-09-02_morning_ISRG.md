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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: +2.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 369.25 → 今开 369.00（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 382.24 ｜ 低 368.25

Options: P/C成交量 0.34 | OI比 0.61 | ATM IV 38.3% | Skew 1.6pp | Term 0.80 | ExpMove ±2.4%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±2.4% ｜ 09-11（9D）±4.3% ｜ 09-18（16D）±5.8% ｜ 09-25（23D）±6.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 429,134 | GEX Change vs 上次快照 2,157,135 | Flip: Primary Flip: 377.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 249 / LOW 162 / INVALID 483
结构观察区: Primary Flip 377.46（全链重定价，覆盖 96%）
Call Wall 400（现价低于该位 5.1%）
最近结构参考: Flip 377（现价高于该位 0.5%）
量化视角： 正 Gamma（43万，无历史分位）｜由负转正（+216万）｜现价位于 Flip 上方 0.55%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 377（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 390.0C — Vol 1 | 最新价 $3.22 | OI 412→521 (ΔOI +109张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增109张（+26.5% vs前日OI），值得跟踪（方向未知）
09-04 382.5C — Vol 7 | 最新价 $2.50 | OI 107→194 (ΔOI +87张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增87张（+81.3% vs前日OI），值得跟踪（方向未知）
09-04 505.0C — Vol 0 | 最新价 $1.43 | OI 20→96 (ΔOI +76张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增76张（+380.0% vs前日OI），值得跟踪（方向未知）
09-25 360.0P — Vol 1 | 最新价 $6.86 | OI 18→94 (ΔOI +76张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增76张（+422.2% vs前日OI），值得跟踪（方向未知）
09-04 352.5P — Vol 1 | 最新价 $0.88 | OI 1→49 (ΔOI +48张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增48张（+4800.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 396 张（Put 124 / Call 272），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 2D
09-11  C +98 / P +29 ｜ Activity HIGH ｜ 9D
09-18  C +53 / P +17 ｜ Activity MEDIUM △ ｜ 16D
09-25  C +21 / P +95 ｜ Activity MEDIUM △ ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 2.0k / P 1.2k
今日变化ΔOI: C +0.4k / P +0.1k
平值价格ATM:  C 4.60 / P 4.58
隐含波动率 ATM IV:  38.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 382 ｜ +87 ｜ $2.50 ｜ 名义 $21.8k* ｜ +0.8%
P 352 ｜ +48 ｜ $0.88 ｜ 名义 $4.2k* ｜ -7.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：382（+0.8%） / 352（-7.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 38.3%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,318 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 0.7k / P 0.5k
今日变化ΔOI: C +98 / P +29
平值价格ATM:  C 9.00 / P 7.39
隐含波动率 ATM IV:  32.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 397 ｜ +38 ｜ $2.00 ｜ 名义 $7.6k* ｜ +4.7%
C 392 ｜ +28 ｜ $3.52 ｜ 名义 $9.9k* ｜ +3.4%
P 352 ｜ +13 ｜ $1.40 ｜ 名义 $1.8k* ｜ -7.1%
结构参考：397（+4.7%） / 352（-7.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 32.6%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,675 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 390C +109 ｜ 400C -28

09-25（MEDIUM △）Top ΔOI: 360P +76 ｜ 350P +11

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 38.3% vs 09-11 32.6%（差 +5.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/ISRG_morning.json