# 期权晚报 2026-10-06（快照 16:40 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 235P ΔOI +17,943（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 242.08 → 收盘 239.24（-1.2%） ｜ 今日高 243.37 ｜ 低 238.93 ｜ 昨收 238.90 → 收盘 239.24（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 1.20 | ATM IV 27.7% | Skew 1.8pp | Term 1.03 | ExpMove ±1.2%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 1.03）｜保护溢价薄（Skew 1.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-07（1D）±1.2% ｜ 10-09（3D）±2.0% ｜ 10-12（6D）±2.5% ｜ 10-14（8D）±3.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 572,802,647 | GEX Change vs 上次快照 -100,927,996 | Flip: Primary Flip: 226.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 672 / LOW 160 / INVALID 642
结构观察区: Primary Flip 226.76（全链重定价，覆盖 99%）
Put Wall 220（弱结构｜现价高于该位 8.7%） | Call Wall 240（弱结构｜现价低于该位 0.3%）
最近结构参考: Call Wall 240（现价低于该位 0.3%）
量化视角： 正 Gamma（5.73亿，无历史分位）｜正 Gamma 减弱（1.01亿）｜现价位于 Flip 上方 5.50%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 235（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 227（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-07  C +47.0k / P +85.8k ｜ Activity HIGH ｜ 1D
10-09  C +53.7k / P +64.2k ｜ Activity HIGH ｜ 3D
10-12  C +12.3k / P +10.2k ｜ Activity HIGH ｜ 6D
10-14  C +5.3k / P +2.4k ｜ Activity HIGH ｜ 8D

📆 10-07 Forward Structure
存量OI: C 106.4k / P 127.4k，今日变化ΔOI: C +47.0k / P +85.8k，平值价格ATM: C $1.06 / P $1.82 ｜ ATM IV 27.7%，净 delta 敞口 71k shares
Top ΔOI: P 235 +17,943 ｜ C 245 +8,359 ｜ C 250 +7,461
仓位参考: Max Pain 235 ｜ Call Wall 250（+4.5%，弱）（OI 14.8k） ｜ Put Wall 235（-1.8%，弱）（OI 20.7k）
量化解读： 存量 Put 重｜ATM IV 27.7%｜历史 Rank 5%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 71,037 股

📆 10-09 Forward Structure
存量OI: C 395.9k / P 421.0k，今日变化ΔOI: C +53.7k / P +64.2k，平值价格ATM: C $2.12 / P $2.72 ｜ ATM IV 27.6%，净 delta 敞口 40k shares
Top ΔOI: P 217 +14,201 ｜ P 230 +13,727 ｜ C 247 +12,102
仓位参考: Max Pain 230 ｜ Call Wall 240（+0.3%，弱）（OI 77.3k） ｜ Put Wall 230（-3.9%，弱）（OI 40.2k）
量化解读： 存量两侧均衡｜ATM IV 27.6%｜历史 Rank 5%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 40,457 股

📆 10-12 Forward Structure
存量OI: C 25.6k / P 18.2k，今日变化ΔOI: C +12.3k / P +10.2k，平值价格ATM: C $2.60 / P $3.25 ｜ ATM IV 23.7%，净 delta 敞口 65k shares
Top ΔOI: P 237 +2,884 ｜ C 237 +2,139 ｜ C 257 +1,728
仓位参考: Max Pain 235 ｜ Call Wall 240（+0.3%）（OI 6.2k） ｜ Put Wall 237.5（-0.7%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 23.7%｜历史 Rank 5%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 65,482 股

📆 10-14 Forward Structure
存量OI: C 11.3k / P 5.6k，今日变化ΔOI: C +5.3k / P +2.4k，平值价格ATM: C $3.40 / P $3.94 ｜ ATM IV 25.9%，净 delta 敞口 50k shares
Top ΔOI: C 260 +1,165 ｜ P 237 +856
仓位参考: Max Pain 235 ｜ Call Wall 250（+4.5%，弱）（OI 1.6k） ｜ Put Wall 237.5（-0.7%）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 25.9%｜历史 Rank 5%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 49,599 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/NVDA_evening.json