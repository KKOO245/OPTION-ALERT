# 期权晨报 2026-09-23（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $741.21
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　⏰ 今日
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,887.04 → 今开 1,895.00（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 1902.22 ｜ 低 1823.06

Options: P/C成交量 0.52 | OI比 1.24 | ATM IV 81.3% | Skew -6.5pp | Term 0.94 | ExpMove ±5.9%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±5.9% ｜ 10-02（9D）±10.8% ｜ 10-09（16D）±13.5% ｜ 10-16（23D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,205,752 | GEX Change vs 上次快照 341,636 | Flip: Primary Flip: 1698.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2104 / LOW 303 / INVALID 737
结构观察区: Primary Flip 1698.92（全链重定价，覆盖 100%）
Call Wall 2,000（弱结构｜现价低于该位 5.1%）
最近结构参考: Call Wall 2000（现价低于该位 5.1%）
量化视角： 正 Gamma（1321万，无历史分位）｜正 Gamma 增强（+34万）｜现价位于 Flip 上方 11.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）；上方 2,000（Call Wall，弱结构）。
• Gamma 区域：切换参考 1699（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-25 Forward Structure
存量OI: C 39.4k / P 48.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $50.00 / P $62.29 ｜ ATM IV 81.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,700 ｜ Call Wall 2000（+5.3%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜ATM IV 81.3%｜历史 Rank 36%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 1,600 ｜ Call Wall 2000（+5.3%，弱）（OI 1.0k） ｜ Put Wall 1800（-5.2%，弱）（OI 0.2k）

10-09（Activity LOW）仓位参考: Max Pain 1,500

10-16（Activity LOW）仓位参考: Max Pain 1,610 ｜ Call Wall 2000（+5.3%，弱）（OI 2.1k） ｜ Put Wall 1800（-5.2%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/SNDK_morning.json