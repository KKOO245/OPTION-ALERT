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


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 281.64 → 收盘 279.14（-0.9%） ｜ 今日高 283.19 ｜ 低 278.88 ｜ 昨收 279.33 → 收盘 279.14（-0.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.88 | OI比 0.98 | ATM IV 26.2% | Skew 1.7pp | Term 0.80 | ExpMove ±1.1%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价薄（Skew 1.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-03（1D）±1.1% ｜ 11-04（2D）±1.8% ｜ 11-05（3D）±2.1% ｜ 11-06（4D）±2.4%
   ⇒ IV–VIX Spread: +5.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -505,969,000 | GEX Change vs 上次快照 -342,366,172 | Flip: Primary Flip: 286.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1249 / LOW 82 / INVALID 813
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 286.31（全链重定价，覆盖 100%）
Put Wall 270（弱结构｜现价高于该位 3.4%） | Call Wall 285（弱结构｜现价低于该位 2.1%）
最近结构参考: Call Wall 285（现价低于该位 2.1%）
量化视角： 负 Gamma（5.06亿，无历史分位）｜负 Gamma 加深（3.42亿）｜现价位于 Flip 下方 2.50%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 280（MaxPain，仅结算参考） / 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 286（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-03  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-05  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 11-03 Forward Structure
存量OI: C 20.8k / P 20.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.74 / P $1.34 ｜ ATM IV 26.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 280 ｜ Call Wall 287（+2.8%）（OI 3.4k） ｜ Put Wall 270（-3.3%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 26.2%｜历史 Rank 67%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-04（Activity LOW）仓位参考: Max Pain 280 ｜ Call Wall 288（+3.2%）（OI 6.2k） ｜ Put Wall 272（-2.6%，弱）（OI 3.5k）

11-05（Activity LOW）仓位参考: Max Pain 280 ｜ Call Wall 280（+0.3%，弱）（OI 1.4k） ｜ Put Wall 260（-6.9%，弱）（OI 1.3k）

11-06（Activity LOW）仓位参考: Max Pain 279 ｜ Call Wall 285（+2.1%，弱）（OI 10.6k） ｜ Put Wall 275（-1.5%，弱）（OI 23.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/IWM_evening.json