# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-19 278C ΔOI +2,218（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 275.52 → 收盘 270.44（-1.8%） ｜ 今日高 275.91 ｜ 低 269.88 ｜ 昨收 275.08 → 收盘 270.44（-1.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 1.53 | OI比 1.37 | ATM IV 37.3% | Skew -0.7pp | Term 0.54 | ExpMove ±1.1%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.54，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.53×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±1.1% ｜ 10-20（4D）±1.4% ｜ 10-21（5D）±1.6% ｜ 10-22（6D）±1.9%
   ⇒ IV–VIX Spread: +17.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,530,336,655 | GEX Change vs 上次快照 -163,314,327 | Flip: Primary Flip: 285.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 1114 / LOW 288 / INVALID 1436
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 285.53（全链重定价，覆盖 84%）
Put Wall 270（弱结构｜现价高于该位 0.2%） | Call Wall 285（弱结构｜现价低于该位 5.1%）
最近结构参考: Put Wall 270（现价高于该位 0.2%）
量化视角： 负 Gamma（15.30亿，无历史分位）｜负 Gamma 加深（1.63亿）｜现价位于 Flip 下方 5.28%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 279（MaxPain，仅结算参考） / 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 286（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +9.0k / P +4.7k ｜ Activity HIGH ｜ 3D
10-20  C +2.0k / P +1.4k ｜ Activity HIGH ｜ 4D
10-21  C +1.9k / P +0.8k ｜ Activity HIGH ｜ 5D
10-22  C +0.7k / P +1.5k ｜ Activity HIGH ｜ 6D

📆 10-19 Forward Structure
存量OI: C 24.9k / P 22.2k，今日变化ΔOI: C +9.0k / P +4.7k，平值价格ATM: C $1.67 / P $1.23 ｜ ATM IV 14.7%，净 delta 敞口 -237k shares
Top ΔOI: C 278 +2,218 ｜ C 281 +1,649 ｜ C 279 +1,600
仓位参考: Max Pain 275 ｜ Call Wall 278（+2.8%）（OI 3.9k） ｜ Put Wall 272（+0.6%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜ATM IV 14.7%｜期限正常（远月高于近端）｜净 delta 敞口 负 236,715 股

📆 10-20 Forward Structure
存量OI: C 11.3k / P 14.0k，今日变化ΔOI: C +2.0k / P +1.4k，平值价格ATM: C $2.10 / P $1.66 ｜ ATM IV 16.5%，净 delta 敞口 -33k shares
Top ΔOI: C 276 +339 ｜ C 279 +262 ｜ P 267 +245
仓位参考: Max Pain 275 ｜ Call Wall 277（+2.4%，弱）（OI 1.6k） ｜ Put Wall 269（-0.5%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.5%｜期限正常（远月高于近端）｜净 delta 敞口 负 32,860 股

📆 10-21 Forward Structure
存量OI: C 8.2k / P 10.0k，今日变化ΔOI: C +1.9k / P +0.8k，平值价格ATM: C $2.49 / P $1.97 ｜ ATM IV 17.4%，净 delta 敞口 -4k shares
Top ΔOI: C 285 +452 ｜ C 284 +439 ｜ C 279 +287
仓位参考: Max Pain 276 ｜ Call Wall 285（+5.4%，弱）（OI 1.4k） ｜ Put Wall 260（-3.9%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 17.4%｜净 delta 敞口 负 4,070 股

📆 10-22 Forward Structure
存量OI: C 6.5k / P 14.6k，今日变化ΔOI: C +0.7k / P +1.5k，平值价格ATM: C $2.80 / P $2.21 ｜ ATM IV 18.2%，净 delta 敞口 -56k shares
Top ΔOI: P 275 +367 ｜ P 271 +354 ｜ C 278 +339
仓位参考: Max Pain 275 ｜ Call Wall 283（+4.6%，弱）（OI 1.0k） ｜ Put Wall 265（-2.0%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 18.2%｜净 delta 敞口 负 56,456 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/IWM_evening.json