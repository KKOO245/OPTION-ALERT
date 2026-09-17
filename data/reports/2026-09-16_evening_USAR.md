# 期权晚报 2026-09-16（快照 21:12 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 17.71 ↑3.0%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 15.60 → 收盘 15.10（-3.2%） ｜ 今日高 15.69 ｜ 低 14.88 ｜ 昨收 15.40 → 收盘 15.10（-1.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-21，窗口结束前不做对错判定）

Options: P/C成交量 0.52 | OI比 0.53 | ATM IV 79.4% | Skew 0.6pp | Term 0.92 | ExpMove ±4.4%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 0.6pp）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±4.4% ｜ 09-25（9D）±9.4% ｜ 10-02（16D）±12.1% ｜ 10-09（23D）±14.7%
   ⇒ IV–VIX Spread: +61.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,857,034 | GEX Change vs 上次快照 -3,790,361 | Flip: Primary Flip: 16.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 249 / LOW 93 / INVALID 126
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.19（全链重定价，覆盖 99%）
Put Wall 15（弱结构｜现价高于该位 0.7%）
最近结构参考: Put Wall 15（现价高于该位 0.7%）
量化视角： 负 Gamma（1086万，无历史分位）｜负 Gamma 加深（379万）｜现价位于 Flip 下方 6.73%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-18 Forward Structure
存量OI: C 122.1k / P 64.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.38 / P $0.29 ｜ ATM IV 79.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 19 ｜ Put Wall 15（-0.7%，弱）（OI 9.5k）
量化解读： 存量 Call 重｜ATM IV 79.4%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 17 ｜ Call Wall 16.5（+9.3%，弱）（OI 1.1k） ｜ Put Wall 16.5（+9.3%，弱）（OI 1.1k）

10-02（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 16（+6.0%，弱）（OI 0.6k）

10-09（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 16（+6.0%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/USAR_evening.json