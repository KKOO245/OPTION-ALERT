# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $721.45
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 139.71 → 收盘 135.47（-3.0%） ｜ 今日高 139.94 ｜ 低 135.07 ｜ 昨收 138.47 → 收盘 135.47（-2.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.57 | OI比 0.99 | ATM IV 60.2% | Skew -1.5pp | Term 0.83 | ExpMove ±5.4%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±5.4% ｜ 10-02（14D）±7.9% ｜ 10-09（21D）±10.1% ｜ 10-16（28D）±11.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,375,397 | GEX Change vs 上次快照 -5,153,909 | Flip: Primary Flip: 124.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 522 / LOW 77 / INVALID 221
结构观察区: Primary Flip 124.55（全链重定价，覆盖 82%）
最近结构参考: Flip 125（现价高于该位 8.8%）
量化视角： 正 Gamma（1638万，无历史分位）｜正 Gamma 减弱（515万）｜现价位于 Flip 上方 8.77%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 123（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 125（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +5.5k / P +2.2k ｜ Activity HIGH ｜ 7D
10-02  C +0.8k / P +0.8k ｜ Activity HIGH ｜ 14D
10-09  C +0.2k / P +0.4k ｜ Activity HIGH ｜ 21D
10-16  C +1.4k / P +6.4k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 21.4k / P 13.6k，今日变化ΔOI: C +5.5k / P +2.2k，平值价格ATM: C $4.47 / P $2.86 ｜ ATM IV 47.6%，净 delta 敞口 7k shares
Top ΔOI: C 150 +3,240 ｜ C 145 +642 ｜ P 139 +420
仓位参考: Max Pain 137 ｜ Call Wall 145（+7.0%，弱）（OI 3.0k） ｜ Put Wall 130（-4.0%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 47.6%｜历史 Rank 22%（近端代理）｜净 delta 敞口 正 6,684 股

📆 10-02 Forward Structure
存量OI: C 10.0k / P 9.3k，今日变化ΔOI: C +0.8k / P +0.8k，平值价格ATM: C $6.40 / P $4.30 ｜ ATM IV 49.1%，净 delta 敞口 14k shares
仓位参考: Max Pain 132 ｜ Call Wall 125（-7.7%，弱）（OI 1.0k） ｜ Put Wall 130（-4.0%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 49.1%｜历史 Rank 22%（近端代理）｜净 delta 敞口 正 14,052 股

📆 10-09 Forward Structure
存量OI: C 3.0k / P 4.4k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $7.80 / P $5.94 ｜ ATM IV 49.6%，净 delta 敞口 -9k shares
Top ΔOI: P 144 +216 ｜ C 140 +44
仓位参考: Max Pain 140 ｜ Call Wall 145（+7.0%，弱）（OI 0.2k） ｜ Put Wall 140（+3.3%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 49.6%｜历史 Rank 22%（近端代理）｜净 delta 敞口 负 8,977 股

📆 10-16 Forward Structure
存量OI: C 64.2k / P 53.2k，今日变化ΔOI: C +1.4k / P +6.4k，平值价格ATM: C $8.57 / P $6.42 ｜ ATM IV 49.8%，净 delta 敞口 14k shares
Top ΔOI: C 155 +502 ｜ C 150 +442
仓位参考: Max Pain 125 ｜ Call Wall 145（+7.0%，弱）（OI 3.4k） ｜ Put Wall 130（-4.0%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 49.8%｜历史 Rank 22%（近端代理）｜净 delta 敞口 正 13,763 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/NOW_evening.json