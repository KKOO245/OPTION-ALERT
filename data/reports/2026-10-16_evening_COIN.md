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


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 181.11 → 收盘 173.16（-4.4%） ｜ 今日高 183.40 ｜ 低 168.86 ｜ 昨收 183.81 → 收盘 173.16（-5.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 0.84 | ATM IV 66.7% | Skew 3.9pp | Term 1.13 | ExpMove ±7.4%（近端） | Rank 25%
量化视角： IV 历史低位（Rank 25%，期权偏便宜）｜期限结构正常（Term 1.13）｜保护溢价中性（Skew 3.9pp）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（7D）±7.4% ｜ 10-30（14D）±12.4% ｜ 11-06（21D）±14.3% ｜ 11-13（28D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,064,339 | GEX Change vs 上次快照 -25,041,938 | Flip: Primary Flip: 166.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 398 / LOW 95 / INVALID 179
结构观察区: Primary Flip 166.01（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价高于该位 1.9%）
最近结构参考: Call Wall 170（现价高于该位 1.9%）
量化视角： 正 Gamma（406万，无历史分位）｜正 Gamma 减弱（2504万）｜现价位于 Flip 上方 4.31%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Call Wall，弱结构）；上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 100%）。
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
存量OI: C 30.7k / P 25.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.80 / P $5.95 ｜ ATM IV 66.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 180 ｜ Call Wall 190（+9.7%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 66.7%｜历史 Rank 25%（近端代理）｜IV/RV 1.52×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 182 ｜ Call Wall 185（+6.8%，弱）（OI 1.6k） ｜ Put Wall 180（+4.0%，弱）（OI 0.9k）

11-06（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 175（+1.1%，弱）（OI 0.2k）

11-13（Activity LOW）仓位参考: Max Pain 182 ｜ Call Wall 185（+6.8%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/COIN_evening.json