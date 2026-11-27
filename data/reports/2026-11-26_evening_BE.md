# 期权晚报 2026-11-26（快照 21:00 ET）

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


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 144.82 → 收盘 152.89（+5.6%） ｜ 今日高 155.54 ｜ 低 136.88 ｜ 昨收 152.89 → 收盘 152.89（+0.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-12-01，窗口结束前不做对错判定）

Options: P/C成交量 0.56 | OI比 0.62 | ATM IV 108.4% | Skew 9.8pp | Term 1.00 | ExpMove ±6.2%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 1.00）｜保护溢价显著（Skew 9.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（1D）±6.2% ｜ 12-04（8D）±15.3% ｜ 12-11（15D）±19.2% ｜ 12-18（22D）±22.5%
   ⇒ IV–VIX Spread: +81.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,213,582 | GEX Change vs 上次快照 -1,826,995 | Flip: Primary Flip: 170.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 595 / LOW 127 / INVALID 240
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 170.22（全链重定价，覆盖 98%）
Put Wall 150（弱结构｜现价高于该位 1.9%）
最近结构参考: Put Wall 150（现价高于该位 1.9%）
量化视角： 负 Gamma（721万，无历史分位）｜负 Gamma 加深（183万）｜现价位于 Flip 下方 10.18%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 162（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 170（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 8D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 15D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 11-27 Forward Structure
存量OI: C 51.9k / P 32.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.00 / P $4.40 ｜ ATM IV 108.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 162 ｜ Call Wall 150（-1.9%，弱）（OI 2.3k） ｜ Put Wall 155（+1.4%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 108.4%｜历史 Rank 66%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 185 ｜ Call Wall 165（+7.9%，弱）（OI 0.4k） ｜ Put Wall 140（-8.4%）（OI 3.0k）

12-11（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 155（+1.4%，弱）（OI 0.2k） ｜ Put Wall 150（-1.9%，弱）（OI 0.4k）

12-18（Activity LOW）仓位参考: Max Pain 200 ｜ Call Wall 150（-1.9%，弱）（OI 1.7k） ｜ Put Wall 150（-1.9%，弱）（OI 6.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=108 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=108）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-26/BE_evening.json