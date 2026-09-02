# 期权晚报 2026-09-02（快照 17:13 ET）

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
🟡 **近现价集中开仓**: 09-04 510C ΔOI +1,108（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 498.18 → 收盘 501.44（+0.7%） ｜ 今日高 504.02 ｜ 低 493.31
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.33 | OI比 0.85 | ATM IV 38.9% | Skew 6.0pp | Term 0.94 | ExpMove ±2.3%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 6.0pp）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（2D）±2.3% ｜ 09-11（9D）±4.6% ｜ 09-18（16D）±7.2% ｜ 09-25（23D）±8.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -24,345,867 | GEX Change vs 上次快照 4,903,197 | Flip: Primary Flip: 516.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 501 / LOW 320 / INVALID 711
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 516.99（全链重定价，覆盖 89%）
Put Wall 500（弱结构｜现价高于该位 0.3%）
最近结构参考: Put Wall 500（现价高于该位 0.3%）
量化视角： 负 Gamma（2435万，无历史分位）｜负 Gamma 缓解（+490万）｜现价位于 Flip 下方 3.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall，弱结构）；上方 510（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 517（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 510.0C — Vol 64 | 最新价 $2.58 | OI 75→1183 (ΔOI +1108张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1108张（+1477.3% vs前日OI），连续性待观察（方向未知）
09-11 500.0C — Vol 24 | 最新价 $10.00 | OI 7→1006 (ΔOI +999张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增999张（+14271.4% vs前日OI），连续性待观察（方向未知）
09-25 440.0P — Vol 1 | 最新价 $2.78 | OI 70→786 (ΔOI +716张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增716张（+1022.9% vs前日OI），连续性待观察（方向未知）
09-04 520.0C — Vol 679 | 最新价 $0.75 | OI 169→736 (ΔOI +567张) | ΔOI/Volume 83.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增567张（+335.5% vs前日OI），连续性待观察（方向未知）
09-11 497.5P — Vol 1 | 最新价 $8.90 | OI 10→409 (ΔOI +399张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增399张（+3990.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,789 张（Put 1,115 / Call 2,674），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +1.4k / P -0.1k ｜ Activity HIGH ｜ 2D
09-11  C +1.2k / P +0.6k ｜ Activity MEDIUM △ ｜ 9D
09-18  C -0.8k / P -1.0k ｜ Activity HIGH ｜ 16D
09-25  C +0.1k / P +1.0k ｜ Activity MEDIUM △ ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 28.9k / P 24.5k
今日变化ΔOI: C +1.4k / P -0.1k
平值价格ATM:  C 5.18 / P 6.43
隐含波动率 ATM IV:  38.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 70k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 510 ｜ +1,108 ｜ $2.58 ｜ 名义 $285.9k* ｜ +1.7%
C 535 ｜ -863 ｜ $0.30 ｜ 名义 $-25.9k* ｜ +6.7%
C 520 ｜ +567 ｜ $0.75 ｜ 名义 $42.5k* ｜ +3.7%
结构参考：510（+1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 38.9%｜历史 Rank 68%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 69,810 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（MEDIUM △）Top ΔOI: 500C +999 ｜ 497P +399

📆 09-18 Forward Structure
存量OI:      C 80.2k / P 86.4k
今日变化ΔOI: C -0.8k / P -1.0k
平值价格ATM:  C 20.50 / P 15.45
隐含波动率 ATM IV:  33.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 57k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 560 ｜ -611 ｜ $1.10 ｜ 名义 $-67.2k* ｜ +11.7%
P 485 ｜ -531 ｜ $8.40 ｜ 名义 $-446.0k* ｜ -3.3%
P 490 ｜ -289 ｜ $9.80 ｜ 名义 $-283.2k* ｜ -2.3%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.5%｜历史 Rank 68%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 57,284 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 440P +716 ｜ 475P +186

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 38.9% vs 09-11 32.7%（差 +6.2pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/SOXX_evening.json