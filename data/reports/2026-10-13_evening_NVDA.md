# 期权晚报 2026-10-13（快照 16:40 ET）

📊 市场环境

SPY $778.01 ｜ QQQ $743.57
VIX 15.27 ↑0.4%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 225C ΔOI +10,584（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 242C ΔOI +34,141 占该期限总 OI 14.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 224.27 → 收盘 228.52（+1.9%） ｜ 今日高 228.64 ｜ 低 223.06 ｜ 昨收 226.32 → 收盘 228.52（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.92 | OI比 0.90 | ATM IV 39.0% | Skew 2.2pp | Term 0.80 | ExpMove ±1.7%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-14（1D）±1.7% ｜ 10-16（3D）±2.7% ｜ 10-19（6D）±3.1% ｜ 10-21（8D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 408,361,262 | GEX Change vs 上次快照 102,193,729 | Flip: Primary Flip: 217.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 622 / LOW 207 / INVALID 709
结构观察区: Primary Flip 217.53（全链重定价，覆盖 97%）
Call Wall 240（弱结构｜现价低于该位 4.8%）
最近结构参考: Call Wall 240（现价低于该位 4.8%）
量化视角： 正 Gamma（4.08亿，无历史分位）｜正 Gamma 增强（+1.02亿）｜现价位于 Flip 上方 5.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 225（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 218（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-14  C +74.8k / P +72.7k ｜ Activity HIGH ｜ 1D
10-16  C +21.1k / P +12.2k ｜ Activity MEDIUM △ ｜ 3D
10-19  C +6.9k / P +8.8k ｜ Activity HIGH ｜ 6D
10-21  C +3.2k / P +4.1k ｜ Activity HIGH ｜ 8D

📆 10-14 Forward Structure
存量OI: C 122.8k / P 110.2k，今日变化ΔOI: C +74.8k / P +72.7k，平值价格ATM: C $2.45 / P $1.41 ｜ ATM IV 39.0%，净 delta 敞口 1.5M shares
Top ΔOI: C 242 +34,141 ｜ C 225 +10,584
仓位参考: Max Pain 225 ｜ Call Wall 242.5（+6.1%）（OI 36.0k） ｜ Put Wall 225（-1.5%，弱）（OI 8.1k）
量化解读： 存量两侧均衡｜ATM IV 39.0%｜历史 Rank 36%（近端代理）｜IV/RV 1.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,492,812 股

10-16（MEDIUM △）Top ΔOI: 232C +6,584 ｜ 220P +4,674
10-16（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 220（-3.7%，弱）（OI 99.2k） ｜ Put Wall 220（-3.7%，弱）（OI 64.6k）

📆 10-19 Forward Structure
存量OI: C 37.3k / P 14.9k，今日变化ΔOI: C +6.9k / P +8.8k，平值价格ATM: C $4.17 / P $2.98 ｜ ATM IV 30.4%，净 delta 敞口 -55k shares
Top ΔOI: P 230 +3,619 ｜ C 240 +1,279 ｜ C 230 +840
仓位参考: Max Pain 230 ｜ Call Wall 250（+9.4%，弱）（OI 9.4k） ｜ Put Wall 230（+0.6%）（OI 4.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.4%｜历史 Rank 36%（近端代理）｜IV/RV 1.52×（近似）｜净 delta 敞口 负 55,178 股

📆 10-21 Forward Structure
存量OI: C 9.9k / P 6.5k，今日变化ΔOI: C +3.2k / P +4.1k，平值价格ATM: C $4.80 / P $3.75 ｜ ATM IV 31.5%，净 delta 敞口 2k shares
Top ΔOI: P 225 +1,551 ｜ C 235 +950
仓位参考: Max Pain 230 ｜ Call Wall 240（+5.0%）（OI 3.7k） ｜ Put Wall 225（-1.5%）（OI 1.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 31.5%｜历史 Rank 36%（近端代理）｜IV/RV 1.57×（近似）｜净 delta 敞口 正 2,404 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/NVDA_evening.json