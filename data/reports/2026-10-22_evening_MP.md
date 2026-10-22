# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 40C ΔOI +735（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 38.01 → 收盘 38.56（+1.4%） ｜ 今日高 38.96 ｜ 低 37.57 ｜ 昨收 39.50 → 收盘 38.56（-2.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.16 | OI比 0.74 | ATM IV 66.9% | Skew 1.4pp | Term 0.98 | ExpMove ±3.5%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 0.98）｜保护溢价薄（Skew 1.4pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.74）+ 当日成交偏 Put（P/C量 1.16）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±3.5% ｜ 10-30（8D）±7.9% ｜ 11-06（15D）±11.6% ｜ 11-13（22D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,273,962 | GEX Change vs 上次快照 480,775 | Flip: Primary Flip: 39.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 323 / LOW 82 / INVALID 119
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 39.33（全链重定价，覆盖 89%）
Put Wall 40（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 39（现价低于该位 2.0%）
量化视角： 负 Gamma（227万，无历史分位）｜负 Gamma 缓解（+48万）｜现价位于 Flip 下方 1.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 39（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +1.2k / P -0.5k ｜ Activity HIGH ｜ 1D
10-30  C +0.9k / P +0.2k ｜ Activity HIGH ｜ 8D
11-06  C +0.3k / P +70 ｜ Activity HIGH ｜ 15D
11-13  C +58 / P +9 ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 10.7k / P 7.9k，今日变化ΔOI: C +1.2k / P -0.5k，平值价格ATM: C $0.60 / P $0.73 ｜ ATM IV 66.9%，净 delta 敞口 62k shares
Top ΔOI: C 40 +735 ｜ C 41 +363
仓位参考: Max Pain 40 ｜ Call Wall 42（+8.9%，弱）（OI 1.1k） ｜ Put Wall 36.5（-5.3%）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 66.9%｜历史 Rank 51%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 62,097 股

📆 10-30 Forward Structure
存量OI: C 8.3k / P 6.9k，今日变化ΔOI: C +0.9k / P +0.2k，平值价格ATM: C $1.31 / P $1.72 ｜ ATM IV 59.7%，净 delta 敞口 -1k shares
Top ΔOI: C 42 +429
仓位参考: Max Pain 44 ｜ Call Wall 42（+8.9%，弱）（OI 0.5k） ｜ Put Wall 42（+8.9%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 59.7%｜历史 Rank 51%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,339 股

📆 11-06 Forward Structure
存量OI: C 6.0k / P 3.7k，今日变化ΔOI: C +0.3k / P +70，平值价格ATM: C $1.85 / P $2.63 ｜ ATM IV 71.9%，净 delta 敞口 76 shares
仓位参考: Max Pain 43 ｜ Call Wall 40（+3.7%，弱）（OI 0.4k） ｜ Put Wall 38（-1.5%）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 71.9%｜历史 Rank 51%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 76 股

11-13（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 35（-9.2%，弱）（OI 0.5k） ｜ Put Wall 39（+1.1%）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/MP_evening.json