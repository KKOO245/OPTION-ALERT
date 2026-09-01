# 期权晚报 2026-09-01（快照 16:40 ET）

📊 市场环境

SPY $761.78 ｜ QQQ $707.64
VIX 16.34 ↑9.5%（5D +5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 09-04 ATM IV 90.8% vs 09-11 76.8%（差 +14.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 17.50 → 收盘 17.47（-0.2%） ｜ 今日高 17.80 ｜ 低 17.02
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.83 | OI比 0.64 | ATM IV 90.8% | Skew 4.7pp | Term 0.87 | ExpMove ±5.8%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 4.7pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.64）+ 当日成交偏 Put（P/C量 2.83）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.83×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（3D）±5.8% ｜ 09-11（10D）±13.2% ｜ 09-18（17D）±5.8% ｜ 09-25（24D）±20.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 288,952 | GEX Change vs 上次快照 141,670 | Flip: Primary Flip: 17.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 216 / LOW 79 / INVALID 171
结构观察区: Primary Flip 17.16（全链重定价，覆盖 97%）
Put Wall 16（弱结构｜现价高于该位 9.2%）
最近结构参考: Flip 17（现价高于该位 1.8%）
量化视角： 正 Gamma（29万，无历史分位）｜正 Gamma 增强（+14万）｜现价位于 Flip 上方 1.80%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 19.0C — Vol 17 | 最新价 $0.15 | OI 316→542 (ΔOI +226张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增226张（+71.5% vs前日OI），值得跟踪（方向未知）
09-04 20.0C — Vol 16 | 最新价 $0.09 | OI 281→506 (ΔOI +225张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增225张（+80.1% vs前日OI），值得跟踪（方向未知）
09-04 19.5C — Vol 7 | 最新价 $0.08 | OI 199→410 (ΔOI +211张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增211张（+106.0% vs前日OI），值得跟踪（方向未知）
09-04 17.0P — Vol 114 | 最新价 $0.28 | OI 194→361 (ΔOI +167张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增167张（+86.1% vs前日OI），值得跟踪（方向未知）
09-04 21.0C — Vol 5 | 最新价 $0.06 | OI 482→614 (ΔOI +132张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增132张（+27.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 961 张（Put 167 / Call 794），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 3D
09-11  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 10D
09-18  C +79 / P +34 ｜ Activity MEDIUM △ ｜ 17D
09-25  C +0.1k / P +13 ｜ Activity LOW ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 3.3k / P 2.1k
今日变化ΔOI: C +0.9k / P +0.3k
平值价格ATM:  C 0.52 / P 0.49
隐含波动率 ATM IV:  90.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +226 ｜ $0.15 ｜ 名义 $3.4k* ｜ +8.8%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+8.8%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 90.8%｜历史 Rank 17%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,036 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-11（MEDIUM △）Top ΔOI: 16P +126 ｜ 18P +54

09-18（MEDIUM △）Top ΔOI: 16P +39

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 90.8% vs 09-11 76.8%（差 +14.0pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/NNE_evening.json