# 期权晨报 2026-09-23（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $738.38
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 36.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　⏰ 今日
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 201.07 → 今开 197.71（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 204.50 ｜ 低 197.10

Options: P/C成交量 0.29 | OI比 0.57 | ATM IV 70.1% | Skew -6.9pp | Term 0.92 | ExpMove ±5.1%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -6.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±5.1% ｜ 10-02（9D）±8.7% ｜ 10-09（16D）±11.4% ｜ 10-16（23D）±13.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 34,842,519 | GEX Change vs 上次快照 -301,258 | Flip: Primary Flip: 177.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 579 / LOW 104 / INVALID 197
结构观察区: Primary Flip 177.65（全链重定价，覆盖 100%）
Call Wall 220（弱结构｜现价低于该位 8.7%）
最近结构参考: Call Wall 220（现价低于该位 8.7%）
量化视角： 正 Gamma（3484万，无历史分位）｜正 Gamma 减弱（30万）｜现价位于 Flip 上方 13.02%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 182（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 178（全链重定价，覆盖 100%）。
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
存量OI: C 87.0k / P 49.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.77 / P $4.50 ｜ ATM IV 70.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 182 ｜ Call Wall 212.5（+5.8%，弱）（OI 7.9k） ｜ Put Wall 190（-5.4%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 70.1%｜历史 Rank 32%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 188 ｜ Call Wall 220（+9.6%，弱）（OI 1.5k） ｜ Put Wall 187.5（-6.6%，弱）（OI 1.1k）

10-09（Activity LOW）仓位参考: Max Pain 185 ｜ Call Wall 220（+9.6%，弱）（OI 0.4k）

10-16（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 220（+9.6%，弱）（OI 6.2k） ｜ Put Wall 200（-0.4%，弱）（OI 2.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/COIN_morning.json