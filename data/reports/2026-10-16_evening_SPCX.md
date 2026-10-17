# 期权晚报 2026-10-16（快照 21:00 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 147.82 → 收盘 146.03（-1.2%） ｜ 今日高 147.92 ｜ 低 142.96 ｜ 昨收 148.62 → 收盘 146.03（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 1.07 | OI比 0.77 | ATM IV 40.3% | Skew 6.6pp | Term 1.47 | ExpMove ±2.9%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常偏陡（Term 1.47）｜保护溢价显著（Skew 6.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.9% ｜ 10-21（5D）±7.8% ｜ 10-23（7D）±8.7% ｜ 10-26（10D）±9.8%
   ⇒ IV–VIX Spread: +20.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -24,146,537 | GEX Change vs 上次快照 -16,699,715 | Flip: Primary Flip: 150.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 733 / LOW 72 / INVALID 369
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 150.83（全链重定价，覆盖 100%）
Put Wall 140（弱结构｜现价高于该位 4.3%）
最近结构参考: Flip 151（现价低于该位 3.2%）
量化视角： 负 Gamma（2415万，无历史分位）｜负 Gamma 加深（1670万）｜现价位于 Flip 下方 3.18%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-26  C +0 / P +0 ｜ Activity LOW ｜ 10D

📆 10-19 Forward Structure
存量OI: C 45.2k / P 34.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.17 / P $2.09 ｜ ATM IV 40.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 155 ｜ Call Wall 157.5（+7.9%，弱）（OI 4.6k） ｜ Put Wall 148（+1.3%）（OI 8.6k）
量化解读： 存量 Call 重｜ATM IV 40.3%｜历史 Rank 4%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-21（Activity LOW）仓位参考: Max Pain 150 ｜ Call Wall 150（+2.7%，弱）（OI 2.0k） ｜ Put Wall 147（+0.7%，弱）（OI 1.4k）

10-23（Activity LOW）仓位参考: Max Pain 155 ｜ Call Wall 155（+6.1%，弱）（OI 7.8k） ｜ Put Wall 140（-4.1%，弱）（OI 7.8k）

10-26（Activity LOW）仓位参考: Max Pain 150 ｜ Call Wall 155（+6.1%，弱）（OI 0.8k） ｜ Put Wall 144（-1.4%）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SPCX_evening.json