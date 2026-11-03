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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 9.79 → 收盘 8.85（-9.6%） ｜ 今日高 9.88 ｜ 低 8.82 ｜ 昨收 9.62 → 收盘 8.85（-8.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.50 | OI比 0.57 | ATM IV 114.1% | Skew 7.9pp | Term 0.80 | ExpMove ±9.8%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 7.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±9.8% ｜ 11-13（11D）±15.7% ｜ 11-20（18D）±18.9% ｜ 11-27（25D）±19.4%
   ⇒ IV–VIX Spread: +92.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -543,295 | GEX Change vs 上次快照 -982,547 | Flip: Primary Flip: 9.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 197 / LOW 57 / INVALID 142
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.24（全链重定价，覆盖 100%）
最近结构参考: Flip 9（现价低于该位 4.2%）
量化视角： 负 Gamma（54万，无历史分位）｜由正转负（98万）｜现价位于 Flip 下方 4.20%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 11-06 Forward Structure
存量OI: C 10.7k / P 6.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.37 / P $0.50 ｜ ATM IV 114.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 10 ｜ Call Wall 9（+1.6%，弱）（OI 0.3k） ｜ Put Wall 9（+1.6%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 114.1%｜历史 Rank 50%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 10 ｜ Put Wall 9（+1.6%，弱）（OI 0.4k）

11-20（Activity LOW）仓位参考: Max Pain 13 ｜ Call Wall 9.5（+7.3%，弱）（OI 1.5k） ｜ Put Wall 9（+1.6%，弱）（OI 3.1k）

11-27（Activity LOW）仓位参考: Max Pain 10 ｜ Put Wall 9.5（+7.3%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 114.1% vs 11-13 104.8%（差 +9.3pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/USAR_evening.json