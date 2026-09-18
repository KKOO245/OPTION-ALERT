# 期权晚报 2026-09-17（快照 21:08 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.44 ↓12.8%（5D -13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 44.4% vs 09-21 31.0%（差 +13.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 59.04 → 收盘 58.97（-0.1%） ｜ 今日高 59.74 ｜ 低 58.89 ｜ 昨收 57.05 → 收盘 58.97（+3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.45 | OI比 0.45 | ATM IV 44.4% | Skew -2.5pp | Term 0.87 | ExpMove ±1.8%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.45）+ 当日成交偏 Put（P/C量 1.45）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.45×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±1.8% ｜ 09-21（4D）±2.6% ｜ 09-23（6D）±3.5% ｜ 09-25（8D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 102,651,393 | GEX Change vs 上次快照 -8,395,106 | Flip: Primary Flip: 57.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 925 / LOW 235 / INVALID 356
结构观察区: Primary Flip 57.36（全链重定价，覆盖 94%）
最近结构参考: Flip 57（现价高于该位 2.8%）
量化视角： 正 Gamma（1.03亿，无历史分位）｜正 Gamma 减弱（840万）｜现价位于 Flip 上方 2.80%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 58（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 6D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 09-18 Forward Structure
存量OI: C 976.1k / P 443.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.54 / P $0.54 ｜ ATM IV 44.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 58 ｜ Call Wall 60（+1.7%，弱）（OI 43.8k） ｜ Put Wall 55（-6.7%，弱）（OI 22.1k）
量化解读： 存量 Call 重｜ATM IV 44.4%｜历史 Rank 74%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-21（Activity LOW）仓位参考: Max Pain 57 ｜ Call Wall 57（-3.3%）（OI 3.4k） ｜ Put Wall 58（-1.6%，弱）（OI 2.2k）

09-23（Activity LOW）仓位参考: Max Pain 59 ｜ Call Wall 61.5（+4.3%，弱）（OI 0.5k） ｜ Put Wall 55（-6.7%，弱）（OI 1.5k）

09-25（Activity LOW）仓位参考: Max Pain 60 ｜ Put Wall 55（-6.7%）（OI 6.0k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 44.4% vs 09-21 31.0%（差 +13.4pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SLV_evening.json