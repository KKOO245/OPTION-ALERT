# 期权晨报 2026-09-24（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $737.10
VIX 15.64 ↑3.0%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 225.51 → 今开 222.12（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 223.23 ｜ 低 221.09

Options: P/C成交量 0.50 | OI比 0.68 | ATM IV 31.5% | Skew 0.4pp | Term 0.99 | ExpMove ±2.4%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 0.99）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±2.4% ｜ 09-28（4D）±2.8% ｜ 09-30（6D）±3.5% ｜ 10-02（8D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 661,184,368 | GEX Change vs 上次快照 88,999,249 | Flip: Primary Flip: 214.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 679 / LOW 179 / INVALID 388
结构观察区: Primary Flip 214.44（全链重定价，覆盖 100%）
Call Wall 230（弱结构｜现价低于该位 0.6%）
最近结构参考: Call Wall 230（现价低于该位 0.6%）
量化视角： 正 Gamma（6.61亿，无历史分位）｜正 Gamma 增强（+8900万）｜现价位于 Flip 上方 6.58%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 214（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-30  C +0 / P +0 ｜ Activity LOW ｜ 6D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 09-25 Forward Structure
存量OI: C 478.0k / P 327.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.45 / P $1.93 ｜ ATM IV 31.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 220 ｜ Call Wall 230（+0.6%，弱）（OI 78.8k） ｜ Put Wall 210（-8.1%，弱）（OI 19.9k）
量化解读： 存量 Call 重｜ATM IV 31.5%｜历史 Rank 10%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-28（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 235（+2.8%，弱）（OI 10.1k） ｜ Put Wall 210（-8.1%，弱）（OI 3.1k）

09-30（Activity LOW）仓位参考: Max Pain 218 ｜ Call Wall 240（+5.0%）（OI 3.0k） ｜ Put Wall 212.5（-7.0%，弱）（OI 3.4k）

10-02（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 250（+9.4%）（OI 37.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/NVDA_morning.json