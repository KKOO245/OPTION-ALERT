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
🔴 **事件差分**: 11-06（4D）ATM IV 154.2% vs 11-13 102.2%（差 +52.0pp），覆盖 ISM 制造业 PMI、Midterm Elections 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-27 175P ΔOI +369（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 186.52 → 收盘 178.34（-4.4%） ｜ 今日高 187.55 ｜ 低 178.13 ｜ 昨收 184.11 → 收盘 178.34（-3.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 1.58 | OI比 0.86 | ATM IV 154.2% | Skew 18.6pp | Term 0.46 | ExpMove ±12.9%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.46，近月 IV 高于远月）｜保护溢价显著（Skew 18.6pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.58×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（4D）±12.9% ｜ 11-13（11D）±14.2% ｜ 11-20（18D）±15.1% ｜ 11-27（25D）±15.7%
   ⇒ IV–VIX Spread: +133.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,895,929 | GEX Change vs 上次快照 -6,195,530 | Flip: Primary Flip: 171.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 760 / LOW 9 / INVALID 137
结构观察区: Primary Flip 171.34（全链重定价，覆盖 100%）
最近结构参考: Flip 171（现价高于该位 4.1%）
量化视角： 正 Gamma（690万，无历史分位）｜正 Gamma 减弱（620万）｜现价位于 Flip 上方 4.09%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 171（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 100.0P — Vol 10,977 | 最新价 $0.24 | OI 7196→22816 (ΔOI +15620张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15620张（+217.1% vs前日OI），连续性待观察（方向未知）
11-06 195.0C — Vol 3,525 | 最新价 $5.10 | OI 2180→12961 (ΔOI +10781张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10781张（+494.5% vs前日OI），连续性待观察（方向未知）
11-06 187.5C — Vol 3,289 | 最新价 $7.52 | OI 400→11004 (ΔOI +10604张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10604张（+2651.0% vs前日OI），连续性待观察（方向未知）
11-06 190.0C — Vol 4,865 | 最新价 $6.65 | OI 981→7160 (ΔOI +6179张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6179张（+629.9% vs前日OI），连续性待观察（方向未知）
11-06 197.5C — Vol 1,907 | 最新价 $4.30 | OI 1406→6647 (ΔOI +5241张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5241张（+372.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 48,425 张（Put 15,620 / Call 32,805），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +45.5k / P +41.0k ｜ Activity HIGH ｜ 4D
11-13  C +4.7k / P +3.7k ｜ Activity HIGH ｜ 11D
11-20  C -0.6k / P +3.1k ｜ Activity MEDIUM △ ｜ 18D
11-27  C +0.5k / P +1.5k ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 121.6k / P 104.7k，今日变化ΔOI: C +45.5k / P +41.0k，平值价格ATM: C $12.08 / P $10.94 ｜ ATM IV 154.2%，净 delta 敞口 1.1M shares
Top ΔOI: P 100 +15,620 ｜ C 195 +10,781 ｜ C 187 +10,604
仓位参考: Max Pain 188 ｜ Call Wall 195（+9.3%，弱）（OI 13.0k）
量化解读： 存量两侧均衡｜ATM IV 154.2%｜历史 Rank 100%（近端代理）｜IV/RV 3.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,077,943 股

📆 11-13 Forward Structure
存量OI: C 24.1k / P 23.4k，今日变化ΔOI: C +4.7k / P +3.7k，平值价格ATM: C $13.25 / P $12.00 ｜ ATM IV 102.2%，净 delta 敞口 33k shares
仓位参考: Max Pain 192 ｜ Call Wall 190（+6.5%，弱）（OI 0.7k） ｜ Put Wall 180（+0.9%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 102.2%｜历史 Rank 100%（近端代理）｜IV/RV 2.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 32,992 股

11-20（MEDIUM △）Top ΔOI: 160P +1,750 ｜ 230C -772
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 165（-7.5%，弱）（OI 11.7k） ｜ Put Wall 180（+0.9%，弱）（OI 10.5k）

📆 11-27 Forward Structure
存量OI: C 10.4k / P 11.8k，今日变化ΔOI: C +0.5k / P +1.5k，平值价格ATM: C $13.45 / P $14.56 ｜ ATM IV 75.7%，净 delta 敞口 -34k shares
Top ΔOI: P 175 +369
仓位参考: Max Pain 195 ｜ Call Wall 195（+9.3%，弱）（OI 0.5k） ｜ Put Wall 180（+0.9%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 75.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 负 34,427 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 154.2% vs 11-13 102.2%（差 +52.0pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/PLTR_evening.json