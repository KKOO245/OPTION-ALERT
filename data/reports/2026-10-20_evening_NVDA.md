# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 225C ΔOI +7,320（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 215.97 → 收盘 216.47（+0.2%） ｜ 今日高 218.46 ｜ 低 212.77 ｜ 昨收 217.09 → 收盘 216.47（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.66 | OI比 0.82 | ATM IV 40.7% | Skew 2.4pp | Term 0.98 | ExpMove ±1.8%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常（Term 0.98）｜保护溢价中性（Skew 2.4pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-21（1D）±1.8% ｜ 10-23（3D）±3.0% ｜ 10-26（6D）±3.5% ｜ 10-28（8D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 129,802,245 | GEX Change vs 上次快照 58,715,876 | Flip: Primary Flip: 212.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 741 / LOW 198 / INVALID 577
结构观察区: Primary Flip 212.71（全链重定价，覆盖 99%）
Call Wall 230（弱结构｜现价低于该位 5.9%）
最近结构参考: Flip 213（现价高于该位 1.8%）
量化视角： 正 Gamma（1.30亿，无历史分位）｜正 Gamma 增强（+5872万）｜现价位于 Flip 上方 1.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 220（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-21  C +35.3k / P +38.6k ｜ Activity HIGH ｜ 1D
10-23  C +38.1k / P +29.4k ｜ Activity HIGH ｜ 3D
10-26  C +7.5k / P +8.6k ｜ Activity HIGH ｜ 6D
10-28  C +2.5k / P +1.9k ｜ Activity HIGH ｜ 8D

📆 10-21 Forward Structure
存量OI: C 97.3k / P 80.2k，今日变化ΔOI: C +35.3k / P +38.6k，平值价格ATM: C $1.38 / P $2.57 ｜ ATM IV 40.7%，净 delta 敞口 89k shares
Top ΔOI: C 225 +7,320 ｜ C 227 +7,291
仓位参考: Max Pain 220 ｜ Call Wall 222.5（+2.8%，弱）（OI 11.9k） ｜ Put Wall 200（-7.6%，弱）（OI 8.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.7%｜历史 Rank 44%（近端代理）｜IV/RV 1.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 89,192 股

📆 10-23 Forward Structure
存量OI: C 420.0k / P 344.4k，今日变化ΔOI: C +38.1k / P +29.4k，平值价格ATM: C $2.71 / P $3.78 ｜ ATM IV 40.6%，净 delta 敞口 846k shares
Top ΔOI: C 230 +6,309 ｜ P 195 +5,921
仓位参考: Max Pain 220 ｜ Call Wall 230（+6.3%，弱）（OI 53.7k） ｜ Put Wall 210（-3.0%，弱）（OI 16.1k）
量化解读： 存量 Call 重｜ATM IV 40.6%｜历史 Rank 44%（近端代理）｜IV/RV 1.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 845,931 股

📆 10-26 Forward Structure
存量OI: C 30.0k / P 20.6k，今日变化ΔOI: C +7.5k / P +8.6k，平值价格ATM: C $3.24 / P $4.30 ｜ ATM IV 33.7%，净 delta 敞口 -62k shares
Top ΔOI: P 200 +3,078 ｜ C 230 +1,385 ｜ C 225 +1,378
仓位参考: Max Pain 218 ｜ Call Wall 237.5（+9.7%）（OI 9.2k） ｜ Put Wall 200（-7.6%）（OI 5.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.7%｜历史 Rank 44%（近端代理）｜IV/RV 1.46×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 61,975 股

📆 10-28 Forward Structure
存量OI: C 10.3k / P 9.1k，今日变化ΔOI: C +2.5k / P +1.9k，平值价格ATM: C $4.06 / P $5.11 ｜ ATM IV 35.7%，净 delta 敞口 25k shares
Top ΔOI: P 207 +406 ｜ C 225 +384 ｜ C 217 +356
仓位参考: Max Pain 218 ｜ Call Wall 230（+6.3%）（OI 4.6k） ｜ Put Wall 215（-0.7%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜ATM IV 35.7%｜历史 Rank 44%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 正 25,432 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/NVDA_evening.json