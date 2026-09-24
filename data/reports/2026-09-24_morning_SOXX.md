# 期权晨报 2026-09-24（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $737.09
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


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 565.72 → 今开 554.97（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 561.91 ｜ 低 553.24

Options: P/C成交量 1.05 | OI比 1.49 | ATM IV 33.5% | Skew -0.8pp | Term 1.13 | ExpMove ±2.5%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 1.13）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.49×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±2.5% ｜ 10-02（8D）±2.4% ｜ 10-09（15D）±8.5% ｜ 10-16（22D）±7.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,857,116 | GEX Change vs 上次快照 4,960,436 | Flip: Primary Flip: 545.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 564 / LOW 266 / INVALID 676
结构观察区: Primary Flip 545.22（全链重定价，覆盖 98%）
Call Wall 600（现价低于该位 4.4%）
最近结构参考: Call Wall 600（现价低于该位 4.4%）
量化视角： 正 Gamma（1586万，无历史分位）｜正 Gamma 增强（+496万）｜现价位于 Flip 上方 5.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 530（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 545（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 8D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 15D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 09-25 Forward Structure
存量OI: C 11.5k / P 17.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.18 / P $7.40 ｜ ATM IV 33.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 530 ｜ Call Wall 580（+1.1%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 33.5%｜历史 Rank 51%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 520 ｜ Call Wall 542.5（-5.4%，弱）（OI 2.8k）

10-09（Activity LOW）仓位参考: Max Pain 518 ｜ Call Wall 537.5（-6.3%，弱）（OI 0.4k）

10-16（Activity LOW）仓位参考: Max Pain 525 ｜ Call Wall 600（+4.6%）（OI 13.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/SOXX_morning.json