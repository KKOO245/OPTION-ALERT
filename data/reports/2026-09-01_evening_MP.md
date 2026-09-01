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
🟡 **近现价集中开仓**: 09-04 55C ΔOI +543（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 53.50 → 收盘 53.74（+0.4%） ｜ 今日高 54.50 ｜ 低 52.35
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.51 | OI比 0.75 | ATM IV 72.1% | Skew -5.3pp | Term 0.91 | ExpMove ±5.4%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -5.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（3D）±5.4% ｜ 09-11（10D）±8.4% ｜ 09-18（17D）±11.5% ｜ 09-25（24D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,903,004 | GEX Change vs 上次快照 101,424 | Flip: Primary Flip: 55.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 316 / LOW 49 / INVALID 125
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 55.03（全链重定价，覆盖 100%）
Put Wall 55（弱结构｜现价低于该位 2.3%）
最近结构参考: Put Wall 55（现价低于该位 2.3%）
量化视角： 负 Gamma（190万，无历史分位）｜负 Gamma 缓解（+10万）｜现价位于 Flip 下方 2.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall，弱结构）；上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 55.0C — Vol 312 | 最新价 $0.94 | OI 585→1128 (ΔOI +543张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增543张（+92.8% vs前日OI），连续性待观察（方向未知）
09-04 52.0P — Vol 59 | 最新价 $0.66 | OI 553→904 (ΔOI +351张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增351张（+63.5% vs前日OI），值得跟踪（方向未知）
09-04 60.0C — Vol 306 | 最新价 $0.14 | OI 2068→2406 (ΔOI +338张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增338张（+16.3% vs前日OI），值得跟踪（方向未知）
09-04 50.0P — Vol 185 | 最新价 $0.23 | OI 338→551 (ΔOI +213张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增213张（+63.0% vs前日OI），值得跟踪（方向未知）
09-04 54.0P — Vol 57 | 最新价 $1.62 | OI 392→568 (ΔOI +176张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增176张（+44.9% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,621 张（Put 740 / Call 881），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +2.1k / P +1.3k ｜ Activity HIGH ｜ 3D
09-11  C +0.5k / P +0.3k ｜ Activity HIGH ｜ 10D
09-18  C -16 / P +14 ｜ Activity LOW ｜ 17D
09-25  C +25 / P +39 ｜ Activity MEDIUM △ ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 11.7k / P 8.8k
今日变化ΔOI: C +2.1k / P +1.3k
平值价格ATM:  C 1.29 / P 1.62
隐含波动率 ATM IV:  72.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 11k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 55 ｜ +543 ｜ $0.94 ｜ 名义 $51.0k* ｜ +2.3%
P 52 ｜ +351 ｜ $0.66 ｜ 名义 $23.2k* ｜ -3.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：55（+2.3%） / 52（-3.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 72.1%｜历史 Rank 57%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,924 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 3.4k / P 3.6k
今日变化ΔOI: C +0.5k / P +0.3k
平值价格ATM:  C 2.10 / P 2.40
隐含波动率 ATM IV:  63.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 55 ｜ +68 ｜ $2.88 ｜ 名义 $19.6k* ｜ +2.3%
P 50 ｜ +61 ｜ $0.75 ｜ 名义 $4.6k* ｜ -7.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：55（+2.3%） / 50（-7.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.2%｜历史 Rank 57%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,067 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 50P +16

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 72.1% vs 09-11 63.2%（差 +8.9pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/MP_evening.json