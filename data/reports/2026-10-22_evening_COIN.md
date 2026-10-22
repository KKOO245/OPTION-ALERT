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
🟡 **近现价集中开仓**: 10-23 175P ΔOI +578（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 170.45 → 收盘 169.09（-0.8%） ｜ 今日高 173.64 ｜ 低 166.74 ｜ 昨收 177.08 → 收盘 169.09（-4.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.24 | OI比 0.62 | ATM IV 74.8% | Skew 1.4pp | Term 0.95 | ExpMove ±3.1%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 1.4pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±3.1% ｜ 10-30（8D）±10.2% ｜ 11-06（15D）±12.9% ｜ 11-13（22D）±14.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,654,494 | GEX Change vs 上次快照 -9,406,496 | Flip: Primary Flip: 167.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 433 / LOW 140 / INVALID 273
结构观察区: Primary Flip 167.53（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 0.5%）
最近结构参考: Call Wall 170（现价低于该位 0.5%）
量化视角： 正 Gamma（365万，无历史分位）｜正 Gamma 减弱（941万）｜现价位于 Flip 上方 0.93%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 175（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 168（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +1.0k / P +1.0k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +2.8k / P +1.4k ｜ Activity HIGH ｜ 8D
11-06  C +0.4k / P +1.1k ｜ Activity HIGH ｜ 15D
11-13  C +0.3k / P +44 ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 67.9k / P 42.4k，今日变化ΔOI: C +1.0k / P +1.0k，平值价格ATM: C $2.28 / P $3.05 ｜ ATM IV 74.8%，净 delta 敞口 -21k shares
Top ΔOI: P 175 +578 ｜ C 172 -551
仓位参考: Max Pain 175 ｜ Call Wall 180（+6.5%，弱）（OI 7.5k） ｜ Put Wall 165（-2.4%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.8%｜历史 Rank 48%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 20,797 股

📆 10-30 Forward Structure
存量OI: C 20.6k / P 20.0k，今日变化ΔOI: C +2.8k / P +1.4k，平值价格ATM: C $8.10 / P $9.11 ｜ ATM IV 85.9%，净 delta 敞口 6k shares
Top ΔOI: C 187 +452 ｜ C 180 +395
仓位参考: Max Pain 180 ｜ Call Wall 185（+9.4%，弱）（OI 1.9k） ｜ Put Wall 170（+0.5%，弱）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 85.9%｜历史 Rank 48%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,501 股

📆 11-06 Forward Structure
存量OI: C 6.8k / P 11.9k，今日变化ΔOI: C +0.4k / P +1.1k，平值价格ATM: C $10.18 / P $11.64 ｜ ATM IV 78.2%，净 delta 敞口 6k shares
仓位参考: Max Pain 175 ｜ Call Wall 175（+3.5%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 78.2%｜历史 Rank 48%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,204 股

📆 11-13 Forward Structure
存量OI: C 5.8k / P 7.6k，今日变化ΔOI: C +0.3k / P +44，平值价格ATM: C $11.60 / P $12.31 ｜ ATM IV 72.7%，净 delta 敞口 5k shares
仓位参考: Max Pain 178 ｜ Call Wall 177.5（+5.0%）（OI 1.1k） ｜ Put Wall 160（-5.4%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.7%｜历史 Rank 48%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 4,922 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/COIN_evening.json