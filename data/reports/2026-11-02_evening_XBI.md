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


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 156.41 → 收盘 152.05（-2.8%） ｜ 今日高 157.12 ｜ 低 151.70 ｜ 昨收 155.98 → 收盘 152.05（-2.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 2.18 | OI比 1.64 | ATM IV 46.0% | Skew 1.3pp | Term 0.83 | ExpMove ±5.1%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜当日成交偏 Put（P/C量 2.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.18×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.64×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±5.1% ｜ 11-13（11D）±4.3% ｜ 11-20（18D）±6.9% ｜ 11-27（25D）±5.8%
   ⇒ IV–VIX Spread: +24.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -11,854,642 | GEX Change vs 上次快照 -4,620,359 | Flip: Primary Flip: 159.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 339 / LOW 50 / INVALID 383
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.32（全链重定价，覆盖 99%）
Put Wall 145（现价高于该位 4.9%）
最近结构参考: Flip 159（现价低于该位 4.6%）
量化视角： 负 Gamma（1185万，无历史分位）｜负 Gamma 加深（462万）｜现价位于 Flip 下方 4.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（Put Wall）；上方 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 99%）。
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
存量OI: C 5.4k / P 8.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.54 / P $2.15 ｜ ATM IV 46.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 153 ｜ Call Wall 159（+4.6%，弱）（OI 0.4k） ｜ Put Wall 153（+0.6%）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 46.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 153 ｜ Call Wall 160（+5.2%）（OI 0.4k） ｜ Put Wall 148（-2.7%，弱）（OI 0.3k）

11-20（Activity LOW）仓位参考: Max Pain 154 ｜ Call Wall 160（+5.2%，弱）（OI 2.1k） ｜ Put Wall 145（-4.6%）（OI 10.4k）

11-27（Activity LOW）仓位参考: Max Pain 158 ｜ Call Wall 157（+3.3%，弱）（OI 0.1k） ｜ Put Wall 156（+2.6%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 46.0% vs 11-13 39.9%（差 +6.1pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/XBI_evening.json