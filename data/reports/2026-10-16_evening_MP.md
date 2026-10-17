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


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 41.30 → 收盘 40.17（-2.7%） ｜ 今日高 42.51 ｜ 低 39.88 ｜ 昨收 41.61 → 收盘 40.17（-3.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 2.38 | OI比 0.76 | ATM IV 59.8% | Skew -3.3pp | Term 1.13 | ExpMove ±6.8%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构正常（Term 1.13）｜Put 保护异常便宜（Skew -3.3pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.76）+ 当日成交偏 Put（P/C量 2.38）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.38×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±6.8% ｜ 10-30（14D）±8.7% ｜ 11-06（21D）±13.6% ｜ 11-13（28D）±15.5%
   ⇒ IV–VIX Spread: +39.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,205,168 | GEX Change vs 上次快照 -2,109,644 | Flip: Primary Flip: 43.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 205 / LOW 49 / INVALID 110
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 43.11（全链重定价，覆盖 99%）
最近结构参考: Flip 43（现价低于该位 6.8%）
量化视角： 负 Gamma（121万，无历史分位）｜由正转负（211万）｜现价位于 Flip 下方 6.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 43（全链重定价，覆盖 99%）。
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
存量OI: C 5.2k / P 3.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.54 / P $1.20 ｜ ATM IV 59.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 45 ｜ Call Wall 43（+7.0%，弱）（OI 0.2k） ｜ Put Wall 42（+4.6%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 59.8%｜历史 Rank 37%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 45 ｜ Put Wall 44（+9.5%）（OI 1.7k）

11-06（Activity LOW）仓位参考: Max Pain 43 ｜ Call Wall 43（+7.0%，弱）（OI 0.7k） ｜ Put Wall 38（-5.4%）（OI 0.8k）

11-13（Activity LOW）仓位参考: Max Pain 50 ｜ Put Wall 39（-2.9%）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/MP_evening.json