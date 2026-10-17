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


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 505.01 → 收盘 493.39（-2.3%） ｜ 今日高 509.60 ｜ 低 492.88 ｜ 昨收 514.71 → 收盘 493.39（-4.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 2.27 | ATM IV 46.5% | Skew 4.2pp | Term 0.92 | ExpMove ±5.2%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构正常（Term 0.92）｜保护溢价中性（Skew 4.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±5.2% ｜ 10-30（14D）±3.0% ｜ 11-06（21D）±7.9% ｜ 11-13（28D）±4.5%
   ⇒ IV–VIX Spread: +26.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -26,600,244 | GEX Change vs 上次快照 25,074,276 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 537 / LOW 215 / INVALID 510
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 500（现价低于该位 1.3%）
最近结构参考: Put Wall 500（现价低于该位 1.3%）
量化视角： 负 Gamma（2660万，无历史分位）｜负 Gamma 缓解（+2507万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 500（Put Wall） / 548（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 10-23 Forward Structure
存量OI: C 6.9k / P 15.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $14.11 / P $11.64 ｜ ATM IV 46.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 548 ｜ Call Wall 500（+1.3%，弱）（OI 1.1k） ｜ Put Wall 510（+3.4%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 46.5%｜历史 Rank 82%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 550 ｜ Put Wall 500（+1.3%）（OI 12.0k）

11-06（Activity LOW）仓位参考: Max Pain 550 ｜ Put Wall 500（+1.3%，弱）（OI 0.2k）

11-13（Activity LOW）仓位参考: Max Pain 560 ｜ Put Wall 520（+5.4%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SOXX_evening.json