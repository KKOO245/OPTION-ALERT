# 期权晚报 2026-11-26（快照 16:40 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 26.80 ↓5.3%（5D -5.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 617.10 → 收盘 633.93（+2.7%） ｜ 今日高 634.89 ｜ 低 607.74 ｜ 昨收 633.93 → 收盘 633.93（+0.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-03，窗口结束前不做对错判定）

Options: P/C成交量 1.15 | OI比 0.90 | ATM IV 36.5% | Skew 6.4pp | Term 0.94 | ExpMove ±2.1%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构正常（Term 0.94）｜保护溢价显著（Skew 6.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 24% ｜ P/C OI(近端) 3%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 24%）｜近端持仓极端 Call 重（P/C OI 分位 3%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-27（1D）±2.1% ｜ 11-30（4D）±3.2% ｜ 12-01（5D）±4.0% ｜ 12-02（6D）±4.3%
   ⇒ IV–VIX Spread: +9.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -406,188,138 | GEX Change vs 上次快照 -48,668,791 | Flip: Primary Flip: 652.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2979 / LOW 447 / INVALID 1866
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 652.30（全链重定价，覆盖 97%）
最近结构参考: Flip 652（现价低于该位 2.8%）
量化视角： 负 Gamma（4.06亿，历史分位偏负区，比 76% 的交易日更负）｜负 Gamma 加深（4867万）｜现价位于 Flip 下方 2.82%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 644（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 652（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
12-01  C +0 / P +0 ｜ Activity LOW ｜ 5D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 11-27 Forward Structure
存量OI: C 291.5k / P 263.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.32 / P $6.91 ｜ ATM IV 36.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 644 ｜ Call Wall 650（+2.5%，弱）（OI 11.3k） ｜ Put Wall 640（+1.0%，弱）（OI 14.9k）
量化解读： 存量两侧均衡｜ATM IV 36.5%｜历史 Rank 92%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 0 股

11-30（Activity LOW）仓位参考: Max Pain 660 ｜ Call Wall 650（+2.5%，弱）（OI 19.2k） ｜ Put Wall 650（+2.5%，弱）（OI 19.8k）

12-01（Activity LOW）仓位参考: Max Pain 640 ｜ Call Wall 630（-0.6%，弱）（OI 1.0k）

12-02（Activity LOW）仓位参考: Max Pain 643 ｜ Call Wall 650（+2.5%，弱）（OI 1.3k） ｜ Put Wall 620（-2.2%，弱）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-26/QQQ_evening.json