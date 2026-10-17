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


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 275.52 → 收盘 270.44（-1.8%） ｜ 今日高 275.91 ｜ 低 269.88 ｜ 昨收 275.08 → 收盘 270.44（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 1.27 | OI比 0.89 | ATM IV 14.7% | Skew 2.9pp | Term 1.36 | ExpMove ±1.1%（近端） | Rank — (历史不足)
量化视角： 期限结构正常偏陡（Term 1.36）｜保护溢价中性（Skew 2.9pp）｜当日成交偏 Put（P/C量 1.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-19（3D）±1.1% ｜ 10-20（4D）±1.4% ｜ 10-21（5D）±1.6% ｜ 10-22（6D）±1.9%
   ⇒ IV–VIX Spread: -5.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -796,644,490 | GEX Change vs 上次快照 570,377,838 | Flip: Primary Flip: 283.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1083 / LOW 226 / INVALID 1291
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.01（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 0.2%） | Call Wall 290（弱结构｜现价低于该位 6.7%）
最近结构参考: Put Wall 270（现价高于该位 0.2%）
量化视角： 负 Gamma（7.97亿，无历史分位）｜负 Gamma 缓解（+5.70亿）｜现价位于 Flip 下方 4.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 275（MaxPain，仅结算参考） / 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 283（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-20  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-22  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-19 Forward Structure
存量OI: C 24.9k / P 22.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.67 / P $1.23 ｜ ATM IV 14.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 275 ｜ Call Wall 278（+2.8%）（OI 3.9k） ｜ Put Wall 272（+0.6%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 14.7%｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-20（Activity LOW）仓位参考: Max Pain 275 ｜ Call Wall 277（+2.4%，弱）（OI 1.6k） ｜ Put Wall 269（-0.5%，弱）（OI 1.4k）

10-21（Activity LOW）仓位参考: Max Pain 276 ｜ Call Wall 285（+5.4%，弱）（OI 1.4k） ｜ Put Wall 260（-3.9%，弱）（OI 1.2k）

10-22（Activity LOW）仓位参考: Max Pain 275 ｜ Call Wall 283（+4.6%，弱）（OI 1.0k） ｜ Put Wall 265（-2.0%，弱）（OI 1.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/IWM_evening.json