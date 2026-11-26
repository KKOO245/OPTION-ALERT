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


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 118.47 → 收盘 127.44（+7.6%） ｜ 今日高 128.45 ｜ 低 112.93 ｜ 昨收 127.44 → 收盘 127.44（+0.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-12-01，窗口结束前不做对错判定）

Options: P/C成交量 0.57 | OI比 0.47 | ATM IV 67.8% | Skew 8.4pp | Term 0.99 | ExpMove ±3.9%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 0.99）｜保护溢价显著（Skew 8.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（1D）±3.9% ｜ 11-30（4D）±5.7% ｜ 12-02（6D）±7.6% ｜ 12-04（8D）±8.9%
   ⇒ IV–VIX Spread: +41.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -27,498,202 | GEX Change vs 上次快照 -12,720,808 | Flip: Primary Flip: 130.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 811 / LOW 148 / INVALID 533
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 130.53（全链重定价，覆盖 100%）
Put Wall 115（弱结构｜现价高于该位 10.8%）
最近结构参考: Flip 131（现价低于该位 2.4%）
量化视角： 负 Gamma（2750万，无历史分位）｜负 Gamma 加深（1272万）｜现价位于 Flip 下方 2.37%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 115（Put Wall，弱结构）；上方 133（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 6D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 11-27 Forward Structure
存量OI: C 216.5k / P 101.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.67 / P $2.30 ｜ ATM IV 67.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 133 ｜ Call Wall 140（+9.9%，弱）（OI 9.1k） ｜ Put Wall 120（-5.8%，弱）（OI 7.8k）
量化解读： 存量 Call 重｜ATM IV 67.8%｜历史 Rank 66%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-30（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 140（+9.9%）（OI 6.4k） ｜ Put Wall 115（-9.8%）（OI 5.2k）

12-02（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 135（+5.9%，弱）（OI 1.0k） ｜ Put Wall 115（-9.8%，弱）（OI 0.4k）

12-04（Activity LOW）仓位参考: Max Pain 137 ｜ Call Wall 137（+7.5%，弱）（OI 10.3k） ｜ Put Wall 140（+9.9%，弱）（OI 11.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-26/SPCX_evening.json