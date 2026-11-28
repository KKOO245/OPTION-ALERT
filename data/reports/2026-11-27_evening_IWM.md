# 期权晚报 2026-11-27（快照 21:00 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 271.82 → 收盘 273.79（+0.7%） ｜ 今日高 273.92 ｜ 低 270.68 ｜ 昨收 268.87 → 收盘 273.79（+1.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.16 | OI比 2.77 | ATM IV 15.4% | Skew 3.4pp | Term 1.40 | ExpMove ±1.2%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常偏陡（Term 1.40）｜保护溢价中性（Skew 3.4pp）｜当日成交偏 Put（P/C量 1.16）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.77×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±1.2% ｜ 12-01（4D）±1.5% ｜ 12-02（5D）±1.8% ｜ 12-03（6D）±2.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -387,675,240 | GEX Change vs 上次快照 215,347,070 | Flip: Primary Flip: 284.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1160 / LOW 176 / INVALID 1160
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.63（全链重定价，覆盖 98%）
Put Wall 250（弱结构｜现价高于该位 9.5%） | Call Wall 300（弱结构｜现价低于该位 8.7%）
最近结构参考: Flip 285（现价低于该位 3.8%）
量化视角： 负 Gamma（3.88亿，无历史分位）｜负 Gamma 缓解（+2.15亿）｜现价位于 Flip 下方 3.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（Put Wall，弱结构） / 269（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 285（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +0 / P +0 ｜ Activity LOW ｜ 3D
12-01  C +0 / P +0 ｜ Activity LOW ｜ 4D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 5D
12-03  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 11-30 Forward Structure
存量OI: C 32.0k / P 88.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.20 / P $2.07 ｜ ATM IV 15.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 269 ｜ Call Wall 276（+0.8%，弱）（OI 4.1k） ｜ Put Wall 262（-4.3%，弱）（OI 11.0k）
量化解读： 存量 Put 重｜ATM IV 15.4%｜历史 Rank 7%（近端代理）｜IV/RV 0.51×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

12-01（Activity LOW）仓位参考: Max Pain 265 ｜ Call Wall 277（+1.2%，弱）（OI 3.6k） ｜ Put Wall 260（-5.0%）（OI 6.2k）

12-02（Activity LOW）仓位参考: Max Pain 265 ｜ Call Wall 275（+0.4%）（OI 1.6k） ｜ Put Wall 260（-5.0%）（OI 2.5k）

12-03（Activity LOW）仓位参考: Max Pain 266 ｜ Call Wall 269（-1.7%，弱）（OI 0.9k） ｜ Put Wall 250（-8.7%）（OI 4.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/IWM_evening.json