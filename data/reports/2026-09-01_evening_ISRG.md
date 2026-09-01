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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 晨报缺失（当日未生成），只报收盘事实
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.35 | OI比 0.67 | ATM IV 34.2% | Skew 0.7pp | Term 0.92 | ExpMove ±2.5%（近端） | Rank — (历史不足)
量化视角： 期限结构正常（Term 0.92）｜保护溢价薄（Skew 0.7pp）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（3D）±2.5% ｜ 09-11（10D）±4.3% ｜ 09-18（17D）±5.8% ｜ 09-25（24D）±7.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,728,000 | GEX Change N/A | Flip: Primary Flip: 377.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 231 / LOW 154 / INVALID 509
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 377.87（全链重定价，覆盖 97%）
Call Wall 400（现价低于该位 7.7%）
最近结构参考: Flip 378（现价低于该位 2.3%）
量化视角： 负 Gamma（173万，无历史分位）｜现价位于 Flip 下方 2.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 378（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-04  C N/A / P N/A ｜ Activity LOW ｜ 3D（新上架）
09-11  C N/A / P N/A ｜ Activity LOW ｜ 10D（新上架）
09-18  C N/A / P N/A ｜ Activity LOW ｜ 17D（新上架）
09-25  C N/A / P N/A ｜ Activity LOW ｜ 24D（新上架）

📆 09-04 Forward Structure
存量OI:      C 1.6k / P 1.1k
今日变化ΔOI: C N/A / P N/A
平值价格ATM:  C 3.35 / P 5.75
隐含波动率 ATM IV:  34.2%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 34.2%｜期限倒挂（近端 IV > 远月）——方向不可观测，观察点，非方向信号

数据质量: 行情 C ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/ISRG_evening.json