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
🟡 **事件差分**: 09-04 ATM IV 76.0% vs 09-11 61.9%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 57C ΔOI +169（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 53.71 → 收盘 54.70（+1.9%） ｜ 今日高 55.19 ｜ 低 53.52
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 0.75 | ATM IV 76.0% | Skew -3.5pp | Term 0.85 | ExpMove ±4.5%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±4.5% ｜ 09-11（9D）±8.3% ｜ 09-18（16D）±10.7% ｜ 09-25（23D）±12.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -524,877 | GEX Change vs 上次快照 1,113,019 | Flip: Primary Flip: 54.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 276 / LOW 66 / INVALID 148
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 54.98（全链重定价，覆盖 98%）
Put Wall 55（弱结构｜现价低于该位 0.5%） | Call Wall 60（弱结构｜现价低于该位 8.8%）
最近结构参考: Flip 55（现价低于该位 0.5%）
量化视角： 负 Gamma（52万，无历史分位）｜负 Gamma 缓解（+111万）｜现价位于 Flip 下方 0.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall，弱结构）；上方 55（MaxPain，仅结算参考） / 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 57.0C — Vol 186 | 最新价 $0.48 | OI 349→518 (ΔOI +169张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增169张（+48.4% vs前日OI），连续性待观察（方向未知）
09-04 50.0P — Vol 24 | 最新价 $0.06 | OI 551→703 (ΔOI +152张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增152张（+27.6% vs前日OI），值得跟踪（方向未知）
09-04 54.0C — Vol 351 | 最新价 $1.49 | OI 279→410 (ΔOI +131张) | ΔOI/Volume 37.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增131张（+47.0% vs前日OI），连续性待观察（方向未知）
09-04 75.0C — Vol 119 | 最新价 $0.02 | OI 303→422 (ΔOI +119张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增119张（+39.3% vs前日OI），连续性待观察（方向未知）
09-04 46.0P — Vol 23 | 最新价 $0.01 | OI 358→470 (ΔOI +112张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增112张（+31.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 683 张（Put 264 / Call 419），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.7k / P +0.5k ｜ Activity HIGH ｜ 2D
09-11  C +0.2k / P +0.2k ｜ Activity HIGH ｜ 9D
09-18  C +0.2k / P -0.3k ｜ Activity MEDIUM △ ｜ 16D
09-25  C +0.2k / P +88 ｜ Activity MEDIUM △ ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 12.4k / P 9.2k
今日变化ΔOI: C +0.7k / P +0.5k
平值价格ATM:  C 1.05 / P 1.43
隐含波动率 ATM IV:  76.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 28k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 57 ｜ +169 ｜ $0.48 ｜ 名义 $8.1k* ｜ +4.2%
P 50 ｜ +152 ｜ $0.06 ｜ 名义 $912* ｜ -8.6%
C 54 ｜ +131 ｜ $1.49 ｜ 名义 $19.5k* ｜ -1.3%
结构参考：57（+4.2%） / 50（-8.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 76.0%｜历史 Rank 64%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 27,585 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 3.6k / P 3.9k
今日变化ΔOI: C +0.2k / P +0.2k
平值价格ATM:  C 1.99 / P 2.55
隐含波动率 ATM IV:  61.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 60 ｜ +65 ｜ $0.55 ｜ 名义 $3.6k* ｜ +9.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：60（+9.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 61.9%｜历史 Rank 64%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 4,586 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 60P -265 ｜ 55C +110

09-25（MEDIUM △）Top ΔOI: 53P +34

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 76.0% vs 09-11 61.9%（差 +14.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/MP_evening.json