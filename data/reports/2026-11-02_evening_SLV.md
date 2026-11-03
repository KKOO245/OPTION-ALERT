# 期权晚报 2026-11-02（快照 21:00 ET）

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
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　✅ 今日已公布
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 44.99 → 收盘 45.57（+1.3%） ｜ 今日高 46.13 ｜ 低 45.49 ｜ 昨收 44.60 → 收盘 45.57（+2.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.43 | OI比 0.38 | ATM IV 50.6% | Skew 3.9pp | Term 0.80 | ExpMove ±3.0%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜存量 Call 偏重（OI比 0.38）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.38×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-04（2D）±3.0% ｜ 11-06（4D）±4.3% ｜ 11-09（7D）±4.7% ｜ 11-11（9D）±5.6%
   ⇒ IV–VIX Spread: +29.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -1,094,425 | GEX Change vs 上次快照 -24,710,414 | Flip: Primary Flip: 45.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 640 / LOW 109 / INVALID 339
结构观察区: Primary Flip 45.64（全链重定价，覆盖 99%）
Put Wall 45（弱结构｜现价高于该位 1.3%）
最近结构参考: Flip 46（现价低于该位 0.2%）
量化视角： 负 Gamma（109万，无历史分位）｜由正转负（2471万）｜现价位于 Flip 下方 0.16%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall，弱结构） / 44（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 46（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-04  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-09  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-11  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 11-04 Forward Structure
存量OI: C 24.2k / P 9.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.74 / P $0.64 ｜ ATM IV 50.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 44 ｜ Call Wall 50（+9.7%，弱）（OI 3.2k） ｜ Put Wall 44（-3.4%）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 50.6%｜历史 Rank 84%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 48 ｜ Call Wall 50（+9.7%，弱）（OI 12.9k） ｜ Put Wall 45（-1.3%，弱）（OI 4.2k）

11-09（Activity LOW）仓位参考: Max Pain 46 ｜ Call Wall 47（+3.1%，弱）（OI 0.4k） ｜ Put Wall 43（-5.6%）（OI 0.7k）

11-11（Activity LOW）仓位参考: Max Pain 45 ｜ Call Wall 50（+9.7%，弱）（OI 0.7k） ｜ Put Wall 45（-1.3%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SLV_evening.json