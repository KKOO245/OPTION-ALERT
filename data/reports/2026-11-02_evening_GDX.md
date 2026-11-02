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
🟡 **近现价集中开仓**: 11-04 81C ΔOI +2,548（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 81C ΔOI +2,548 占该期限总 OI 38.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 78.92 → 收盘 79.15（+0.3%） ｜ 今日高 80.41 ｜ 低 78.62 ｜ 昨收 77.09 → 收盘 79.15（+2.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.46 | OI比 0.88 | ATM IV 67.3% | Skew -8.7pp | Term 0.62 | ExpMove ±3.2%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（2D）±3.2% ｜ 11-06（4D）±4.5% ｜ 11-09（7D）±4.6% ｜ 11-11（9D）±10.6%
   ⇒ IV–VIX Spread: +46.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 21,978,346 | GEX Change vs 上次快照 -7,464,059 | Flip: Primary Flip: 76.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 506 / LOW 119 / INVALID 535
结构观察区: Primary Flip 76.52（全链重定价，覆盖 99%）
Call Wall 81（弱结构｜现价低于该位 2.3%）
最近结构参考: Call Wall 81（现价低于该位 2.3%）
量化视角： 正 Gamma（2198万，无历史分位）｜正 Gamma 减弱（746万）｜现价位于 Flip 上方 3.44%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 80（MaxPain，仅结算参考） / 81（Call Wall，弱结构）。
• Gamma 区域：切换参考 77（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 81.0C — Vol 1,370 | 最新价 $1.09 | OI 291→22029 (ΔOI +21738张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21738张（+7470.1% vs前日OI），连续性待观察（方向未知）
11-06 78.0C — Vol 168 | 最新价 $2.57 | OI 7→19869 (ΔOI +19862张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19862张（+283742.9% vs前日OI），连续性待观察（方向未知）
11-06 82.0C — Vol 328 | 最新价 $0.79 | OI 167→15547 (ΔOI +15380张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15380张（+9209.6% vs前日OI），连续性待观察（方向未知）
11-06 79.0C — Vol 268 | 最新价 $1.89 | OI 26→15037 (ΔOI +15011张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15011张（+57734.6% vs前日OI），连续性待观察（方向未知）
11-06 72.0P — Vol 5 | 最新价 $0.15 | OI 0→6420 (ΔOI +6420张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增6420张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 78,411 张（Put 6,420 / Call 71,991），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-04  C +4.7k / P +0.8k ｜ Activity HIGH ｜ 2D
11-06  C +76.5k / P +15.6k ｜ Activity HIGH ｜ 4D
11-09  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 7D
11-11  C +0.5k / P +1.1k ｜ Activity HIGH ｜ 9D

📆 11-04 Forward Structure
存量OI: C 5.6k / P 1.0k，今日变化ΔOI: C +4.7k / P +0.8k，平值价格ATM: C $1.54 / P $1.02 ｜ ATM IV 58.5%，净 delta 敞口 202k shares
Top ΔOI: C 81 +2,548 ｜ C 78 +2,007 ｜ P 75 +201
仓位参考: Max Pain 78 ｜ Call Wall 81（+2.3%，弱）（OI 2.6k） ｜ Put Wall 75（-5.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 58.5%｜历史 Rank 97%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 202,118 股

📆 11-06 Forward Structure
存量OI: C 90.1k / P 29.0k，今日变化ΔOI: C +76.5k / P +15.6k，平值价格ATM: C $1.89 / P $1.71 ｜ ATM IV 55.4%，净 delta 敞口 3.3M shares
Top ΔOI: C 81 +21,738 ｜ C 78 +19,862 ｜ C 82 +15,380
仓位参考: Max Pain 78 ｜ Call Wall 81（+2.3%，弱）（OI 22.0k） ｜ Put Wall 75（-5.2%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 55.4%｜历史 Rank 97%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,270,821 股

📆 11-09 Forward Structure
存量OI: C 0.5k / P 0.4k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $2.02 / P $1.65 ｜ ATM IV 46.6%，净 delta 敞口 9k shares
Top ΔOI: C 78 +124 ｜ P 73 +75 ｜ C 82 +62
仓位参考: Max Pain 78 ｜ Call Wall 78（-1.5%，弱）（OI 0.1k） ｜ Put Wall 78（-1.5%，弱）（OI 80）
量化解读： 存量 Call 重｜ATM IV 46.6%｜历史 Rank 97%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 9,108 股

📆 11-11 Forward Structure
存量OI: C 0.6k / P 1.3k，今日变化ΔOI: C +0.5k / P +1.1k，平值价格ATM: C $4.15 / P $4.21 ｜ ATM IV 46.8%，净 delta 敞口 -9k shares
Top ΔOI: P 77 +1,004 ｜ C 78 +240 ｜ C 80 +220
仓位参考: Max Pain 78 ｜ Call Wall 78（-1.5%，弱）（OI 0.2k） ｜ Put Wall 77（-2.7%）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 46.8%｜历史 Rank 97%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 8,906 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/GDX_evening.json