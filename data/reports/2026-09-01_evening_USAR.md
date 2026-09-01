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
🟡 **近现价集中开仓**: 09-04 16P ΔOI +530（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 17.12 → 收盘 17.26（+0.8%） ｜ 今日高 17.80 ｜ 低 16.96
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.62 | OI比 0.30 | ATM IV 82.3% | Skew -7.5pp | Term 0.98 | ExpMove ±6.3%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -7.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（3D）±6.3% ｜ 09-11（10D）±10.8% ｜ 09-18（17D）±13.7% ｜ 09-25（24D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,830,685 | GEX Change vs 上次快照 1,219,889 | Flip: Primary Flip: 16.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 239 / LOW 110 / INVALID 179
结构观察区: Primary Flip 16.76（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 3.0%）
量化视角： 正 Gamma（283万，无历史分位）｜正 Gamma 增强（+122万）｜现价位于 Flip 上方 2.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 18.0P — Vol 630 | 最新价 $1.55 | OI 5178→6452 (ΔOI +1274张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1274张（+24.6% vs前日OI），连续性待观察（方向未知）
09-11 20.5C — Vol 111 | 最新价 $0.13 | OI 243→1052 (ΔOI +809张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增809张（+332.9% vs前日OI），连续性待观察（方向未知）
09-11 21.5C — Vol 13 | 最新价 $0.08 | OI 74→849 (ΔOI +775张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增775张（+1047.3% vs前日OI），连续性待观察（方向未知）
09-18 21.5C — Vol 20 | 最新价 $0.22 | OI 771→1492 (ΔOI +721张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增721张（+93.5% vs前日OI），连续性待观察（方向未知）
09-18 22.5C — Vol 2 | 最新价 $0.15 | OI 139→838 (ΔOI +699张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增699张（+502.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,278 张（Put 1,274 / Call 3,004），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +3.5k / P +1.6k ｜ Activity HIGH ｜ 3D
09-11  C +2.0k / P +0.7k ｜ Activity HIGH ｜ 10D
09-18  C +2.4k / P +1.6k ｜ Activity HIGH ｜ 17D
09-25  C +1.0k / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 32.0k / P 9.7k
今日变化ΔOI: C +3.5k / P +1.6k
平值价格ATM:  C 0.44 / P 0.65
隐含波动率 ATM IV:  82.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -17k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +530 ｜ $0.22 ｜ 名义 $11.7k* ｜ -4.4%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：16（-4.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 82.3%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,932 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 11.9k / P 2.9k
今日变化ΔOI: C +2.0k / P +0.7k
平值价格ATM:  C 0.86 / P 1.01
隐含波动率 ATM IV:  76.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 19 ｜ +285 ｜ $1.97 ｜ 名义 $56.1k* ｜ +10.1%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+10.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 76.6%｜历史 Rank 3%（近端代理）｜净 delta 敞口 负 4,290 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 111.4k / P 65.5k
今日变化ΔOI: C +2.4k / P +1.6k
平值价格ATM:  C 1.14 / P 1.22
隐含波动率 ATM IV:  73.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -41k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ +1,274 ｜ $1.55 ｜ 名义 $197.5k* ｜ +4.3%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：18（+4.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 73.0%｜历史 Rank 3%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 41,115 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 82.3% vs 09-11 76.6%（差 +5.7pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/USAR_evening.json