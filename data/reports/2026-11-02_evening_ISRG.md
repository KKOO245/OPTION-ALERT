# 期权晚报 2026-11-02（快照 16:40 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 21.15 ↑8.9%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 439.79 → 收盘 436.87（-0.7%） ｜ 今日高 446.45 ｜ 低 436.04 ｜ 昨收 432.01 → 收盘 436.87（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.24 | OI比 0.86 | ATM IV 41.2% | Skew -1.0pp | Term 0.86 | ExpMove ±4.4%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（4D）±4.4% ｜ 11-13（11D）±0.0% ｜ 11-20（18D）±5.8% ｜ 11-27（25D）±6.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,398,483 | GEX Change vs 上次快照 -291,671 | Flip: Primary Flip: 418.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 237 / LOW 138 / INVALID 537
结构观察区: Primary Flip 418.22（全链重定价，覆盖 94%）
Call Wall 420（弱结构｜现价高于该位 4.0%）
最近结构参考: Call Wall 420（现价高于该位 4.0%）
量化视角： 正 Gamma（140万，无历史分位）｜正 Gamma 减弱（29万）｜现价位于 Flip 上方 4.46%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 430（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 418（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 415.0P — Vol 25 | 最新价 $0.73 | OI 18→209 (ΔOI +191张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增191张（+1061.1% vs前日OI），值得跟踪（方向未知）
11-06 432.5C — Vol 1 | 最新价 $11.06 | OI 10→125 (ΔOI +115张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增115张（+1150.0% vs前日OI），值得跟踪（方向未知）
11-06 422.5P — Vol 25 | 最新价 $2.55 | OI 44→145 (ΔOI +101张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增101张（+229.6% vs前日OI），值得跟踪（方向未知）
11-06 420.0P — Vol 30 | 最新价 $1.15 | OI 180→236 (ΔOI +56张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增56张（+31.1% vs前日OI），值得跟踪（方向未知）
11-27 430.0C — Vol 4 | 最新价 $24.20 | OI 10→64 (ΔOI +54张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增54张（+540.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 517 张（Put 348 / Call 169），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.3k / P +0.5k ｜ Activity HIGH ｜ 4D
11-13  C +20 / P +0.1k ｜ Activity MEDIUM △ ｜ 11D
11-20  C +62 / P +5 ｜ Activity MEDIUM △ ｜ 18D
11-27  C +0.1k / P +18 ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 1.8k / P 1.5k，今日变化ΔOI: C +0.3k / P +0.5k，平值价格ATM: C $11.55 / P $7.80 ｜ ATM IV 41.2%，净 delta 敞口 2k shares
Top ΔOI: P 415 +191 ｜ C 432 +115 ｜ P 422 +101
仓位参考: Max Pain 430 ｜ Call Wall 430（-1.6%，弱）（OI 0.1k） ｜ Put Wall 420（-3.9%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.2%｜历史 Rank 57%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,621 股

11-13（MEDIUM △）Top ΔOI: 402P +52 ｜ 405P +50
11-13（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 440（+0.7%，弱）（OI 0.1k） ｜ Put Wall 420（-3.9%，弱）（OI 83）

11-20（MEDIUM △）Top ΔOI: 480C +20 ｜ 455C +18
11-20（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 420（-3.9%，弱）（OI 0.8k） ｜ Put Wall 410（-6.2%，弱）（OI 0.5k）

11-27（MEDIUM △）Top ΔOI: 430C +54 ｜ 445C +38
11-27（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 430（-1.6%，弱）（OI 64） ｜ Put Wall 395（-9.6%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 41.2% vs 11-13 34.5%（差 +6.7pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/ISRG_evening.json