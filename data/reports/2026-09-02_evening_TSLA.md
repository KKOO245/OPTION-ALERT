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
🔴 **事件差分**: 09-04（2D）ATM IV 55.7% vs 09-09 40.6%（差 +15.1pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 360.61 → 收盘 357.01（-1.0%） ｜ 今日高 360.62 ｜ 低 349.92
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.77 | OI比 0.91 | ATM IV 22.5% | Skew 9.6pp | Term 1.83 | ExpMove ±3.4%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.83）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（2D）±3.4% ｜ 09-09（7D）±4.5% ｜ 09-11（9D）±5.3% ｜ 09-14（12D）±5.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 81,418,818 | GEX Change vs 上次快照 42,713,528 | Flip: Primary Flip: 345.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 1032 / LOW 212 / INVALID 774
结构观察区: Primary Flip 345.87（全链重定价，覆盖 90%）
Put Wall 340（弱结构｜现价高于该位 5.0%）
最近结构参考: Flip 346（现价高于该位 3.2%）
量化视角： 正 Gamma（8142万，无历史分位）｜正 Gamma 增强（+4271万）｜现价位于 Flip 上方 3.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 340（Put Wall，弱结构）；上方 358（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 346（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-02 360.0C — Vol 160,093 | 最新价 $0.01 | OI 2691→10801 (ΔOI +8110张) | ΔOI/Volume 5.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8110张（+301.4% vs前日OI），连续性待观察（方向未知）
09-18 450.0C — Vol 357 | 最新价 $0.44 | OI 15194→21055 (ΔOI +5861张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5861张（+38.6% vs前日OI），连续性待观察（方向未知）
09-02 362.5C — Vol 57,045 | 最新价 $0.01 | OI 877→5950 (ΔOI +5073张) | ΔOI/Volume 8.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5073张（+578.5% vs前日OI），连续性待观察（方向未知）
09-02 400.0C — Vol 4,985 | 最新价 $0.02 | OI 12892→17690 (ΔOI +4798张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4798张（+37.2% vs前日OI），连续性待观察（方向未知）
09-11 400.0C — Vol 8,456 | 最新价 $0.94 | OI 11148→15916 (ΔOI +4768张) | ΔOI/Volume 56.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4768张（+42.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 28,610 张（Put 0 / Call 28,610），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-09  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 12D

📆 09-04 Forward Structure
存量OI:      C 232.9k / P 178.2k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 5.75 / P 6.25
隐含波动率 ATM IV:  55.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 55.7%｜历史 Rank 0%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 55.7% vs 09-09 40.6%（差 +15.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/TSLA_evening.json