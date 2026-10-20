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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 166.06 → 收盘 170.85（+2.9%） ｜ 今日高 176.30 ｜ 低 165.90 ｜ 昨收 168.45 → 收盘 170.85（+1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.31 | OI比 0.67 | ATM IV 67.2% | Skew -0.1pp | Term 1.02 | ExpMove ±4.9%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±4.9% ｜ 10-30（10D）±10.1% ｜ 11-06（17D）±13.0% ｜ 11-13（24D）±14.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,007,918 | GEX Change vs 上次快照 1,904,704 | Flip: Primary Flip: 164.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 471 / LOW 120 / INVALID 251
结构观察区: Primary Flip 164.81（全链重定价，覆盖 99%）
Call Wall 170（弱结构｜现价高于该位 0.5%）
最近结构参考: Call Wall 170（现价高于该位 0.5%）
量化视角： 正 Gamma（901万，无历史分位）｜正 Gamma 增强（+190万）｜现价位于 Flip 上方 3.67%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Call Wall，弱结构）；上方 178（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +6.5k / P +2.9k ｜ Activity HIGH ｜ 3D
10-30  C +1.7k / P +1.1k ｜ Activity HIGH ｜ 10D
11-06  C +0.7k / P +51 ｜ Activity HIGH ｜ 17D
11-13  C +0.4k / P +0.5k ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 60.5k / P 40.7k，今日变化ΔOI: C +6.5k / P +2.9k，平值价格ATM: C $4.60 / P $3.82 ｜ ATM IV 67.2%，净 delta 敞口 123k shares
Top ΔOI: C 192 +2,442 ｜ C 180 +1,173
仓位参考: Max Pain 178 ｜ Call Wall 180（+5.4%，弱）（OI 7.1k）
量化解读： 存量 Call 重｜ATM IV 67.2%｜历史 Rank 26%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 123,070 股

📆 10-30 Forward Structure
存量OI: C 17.3k / P 17.4k，今日变化ΔOI: C +1.7k / P +1.1k，平值价格ATM: C $9.00 / P $8.25 ｜ ATM IV 78.8%，净 delta 敞口 40k shares
Top ΔOI: P 150 +457
仓位参考: Max Pain 180 ｜ Call Wall 185（+8.3%，弱）（OI 1.8k） ｜ Put Wall 160（-6.4%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.8%｜历史 Rank 26%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 40,259 股

📆 11-06 Forward Structure
存量OI: C 6.2k / P 10.6k，今日变化ΔOI: C +0.7k / P +51，平值价格ATM: C $11.50 / P $10.75 ｜ ATM IV 74.3%，净 delta 敞口 14k shares
Top ΔOI: C 175 +97
仓位参考: Max Pain 175 ｜ Call Wall 175（+2.4%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.3%｜历史 Rank 26%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,464 股

📆 11-13 Forward Structure
存量OI: C 5.1k / P 7.1k，今日变化ΔOI: C +0.4k / P +0.5k，平值价格ATM: C $12.70 / P $11.95 ｜ ATM IV 70.2%，净 delta 敞口 -9k shares
Top ΔOI: P 170 +231
仓位参考: Max Pain 178 ｜ Call Wall 177.5（+3.9%）（OI 1.1k） ｜ Put Wall 170（-0.5%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 70.2%｜历史 Rank 26%（近端代理）｜IV/RV 1.46×（近似）｜净 delta 敞口 负 9,144 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/COIN_evening.json