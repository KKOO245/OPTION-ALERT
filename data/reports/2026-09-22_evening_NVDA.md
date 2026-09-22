# 期权晚报 2026-09-22（快照 16:40 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $747.46
VIX 14.21 ↓4.4%（5D -17.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-23 230C ΔOI +47,481（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-23 230C ΔOI +47,481 占该期限总 OI 20.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 226.91 → 收盘 228.87（+0.9%） ｜ 今日高 229.98 ｜ 低 226.50 ｜ 昨收 227.38 → 收盘 228.87（+0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.34 | OI比 0.74 | ATM IV 31.1% | Skew 0.2pp | Term 1.00 | ExpMove ±1.4%（近端） | Rank 9%
量化视角： IV 历史低位（Rank 9%，期权偏便宜）｜期限结构正常（Term 1.00）｜保护溢价薄（Skew 0.2pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-23（1D）±1.4% ｜ 09-25（3D）±2.3% ｜ 09-28（6D）±2.8% ｜ 09-30（8D）±3.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 748,616,381 | GEX Change vs 上次快照 48,576,233 | Flip: Primary Flip: 213.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 743 / LOW 204 / INVALID 429
结构观察区: Primary Flip 213.27（全链重定价，覆盖 100%）
Call Wall 230（现价低于该位 0.5%）
最近结构参考: Call Wall 230（现价低于该位 0.5%）
量化视角： 正 Gamma（7.49亿，无历史分位）｜正 Gamma 增强（+4858万）｜现价位于 Flip 上方 7.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 222（MaxPain，仅结算参考）；上方 230（Call Wall）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-23  C +80.4k / P +64.1k ｜ Activity HIGH ｜ 1D
09-25  C +69.1k / P +23.5k ｜ Activity HIGH ｜ 3D
09-28  C +16.6k / P +7.7k ｜ Activity HIGH ｜ 6D
09-30  C +6.3k / P +1.7k ｜ Activity HIGH ｜ 8D

📆 09-23 Forward Structure
存量OI: C 130.9k / P 96.6k，今日变化ΔOI: C +80.4k / P +64.1k，平值价格ATM: C $1.03 / P $2.13 ｜ ATM IV 31.1%，净 delta 敞口 1.9M shares
Top ΔOI: C 230 +47,481 ｜ C 235 +11,749
仓位参考: Max Pain 222 ｜ Call Wall 230（+0.5%）（OI 57.6k） ｜ Put Wall 225（-1.7%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜ATM IV 31.1%｜历史 Rank 9%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,922,391 股

📆 09-25 Forward Structure
存量OI: C 478.0k / P 327.0k，今日变化ΔOI: C +69.1k / P +23.5k，平值价格ATM: C $2.15 / P $3.15 ｜ ATM IV 31.3%，净 delta 敞口 672k shares
Top ΔOI: C 235 +23,900 ｜ C 230 +15,926 ｜ C 237 +13,384
仓位参考: Max Pain 220 ｜ Call Wall 230（+0.5%，弱）（OI 78.8k） ｜ Put Wall 210（-8.2%，弱）（OI 19.9k）
量化解读： 存量 Call 重｜ATM IV 31.3%｜历史 Rank 9%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 672,425 股

📆 09-28 Forward Structure
存量OI: C 38.9k / P 22.3k，今日变化ΔOI: C +16.6k / P +7.7k，平值价格ATM: C $2.70 / P $3.70 ｜ ATM IV 26.8%，净 delta 敞口 393k shares
Top ΔOI: C 235 +8,637 ｜ C 230 +3,798 ｜ P 225 +1,564
仓位参考: Max Pain 220 ｜ Call Wall 235（+2.7%，弱）（OI 10.1k） ｜ Put Wall 210（-8.2%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 26.8%｜历史 Rank 9%（近端代理）｜IV/RV 0.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 393,087 股

📆 09-30 Forward Structure
存量OI: C 15.0k / P 12.4k，今日变化ΔOI: C +6.3k / P +1.7k，平值价格ATM: C $3.60 / P $4.40 ｜ ATM IV 29.7%，净 delta 敞口 145k shares
Top ΔOI: C 240 +2,550 ｜ C 237 +539 ｜ C 225 +465
仓位参考: Max Pain 218 ｜ Call Wall 240（+4.9%）（OI 3.0k） ｜ Put Wall 212.5（-7.2%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜ATM IV 29.7%｜历史 Rank 9%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 正 145,481 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/NVDA_evening.json