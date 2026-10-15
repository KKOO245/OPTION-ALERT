# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 245C ΔOI +308（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 224.28 → 收盘 236.30（+5.4%） ｜ 今日高 239.85 ｜ 低 215.12 ｜ 昨收 239.34 → 收盘 236.30（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.88 | OI比 0.97 | ATM IV 101.1% | Skew 5.4pp | Term 0.86 | ExpMove ±4.2%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 5.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±4.2% ｜ 10-23（8D）±12.6% ｜ 10-30（15D）±16.0% ｜ 11-06（22D）±17.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,866,163 | GEX Change vs 上次快照 -1,620,347 | Flip: Primary Flip: 256.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 621 / LOW 87 / INVALID 186
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 256.22（全链重定价，覆盖 99%）
Put Wall 240（弱结构｜现价低于该位 1.5%）
最近结构参考: Put Wall 240（现价低于该位 1.5%）
量化视角： 负 Gamma（1687万，无历史分位）｜负 Gamma 加深（162万）｜现价位于 Flip 下方 7.78%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 240（Put Wall，弱结构） / 260（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 256（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +4.8k / P -3.6k ｜ Activity MEDIUM △ ｜ 1D
10-23  C +2.0k / P +1.2k ｜ Activity HIGH ｜ 8D
10-30  C +1.9k / P -0.2k ｜ Activity HIGH ｜ 15D
11-06  C +0.3k / P -54 ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 103.5k / P 100.7k，今日变化ΔOI: C +4.8k / P -3.6k，平值价格ATM: C $4.45 / P $5.55 ｜ ATM IV 101.1%，净 delta 敞口 671k shares
Top ΔOI: P 300 -1,245 ｜ C 250 +1,233 ｜ P 292 -951
仓位参考: Max Pain 260 ｜ Call Wall 250（+5.8%，弱）（OI 3.2k） ｜ Put Wall 240（+1.6%，弱）（OI 4.4k）
量化解读： 存量两侧均衡｜ATM IV 101.1%｜历史 Rank 63%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 671,359 股

📆 10-23 Forward Structure
存量OI: C 27.4k / P 27.3k，今日变化ΔOI: C +2.0k / P +1.2k，平值价格ATM: C $14.50 / P $15.25 ｜ ATM IV 106.1%，净 delta 敞口 77k shares
Top ΔOI: C 215 +996 ｜ C 250 +314 ｜ C 245 +308
仓位参考: Max Pain 260 ｜ Call Wall 215（-9.0%，弱）（OI 1.0k） ｜ Put Wall 230（-2.7%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 106.1%｜历史 Rank 63%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 77,311 股

📆 10-30 Forward Structure
存量OI: C 15.1k / P 21.4k，今日变化ΔOI: C +1.9k / P -0.2k，平值价格ATM: C $18.70 / P $19.03 ｜ ATM IV 97.8%，净 delta 敞口 110k shares
Top ΔOI: C 240 +1,165 ｜ P 240 -636 ｜ C 325 -485
仓位参考: Max Pain 268 ｜ Call Wall 240（+1.6%，弱）（OI 1.2k） ｜ Put Wall 230（-2.7%）（OI 3.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 97.8%｜历史 Rank 63%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 109,629 股

📆 11-06 Forward Structure
存量OI: C 5.4k / P 11.3k，今日变化ΔOI: C +0.3k / P -54，平值价格ATM: C $22.12 / P $20.17 ｜ ATM IV 90.7%，净 delta 敞口 17k shares
Top ΔOI: P 240 -396 ｜ P 235 +201 ｜ C 270 +52
仓位参考: Max Pain 270 ｜ Call Wall 240（+1.6%，弱）（OI 0.2k） ｜ Put Wall 235（-0.6%，弱）（OI 2.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 90.7%｜历史 Rank 63%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 16,982 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/BE_evening.json