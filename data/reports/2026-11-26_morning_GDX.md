# 期权晨报 2026-11-26（快照 10:20 ET）

📊 市场环境

SPY $720.30 ｜ QQQ $633.93
VIX 26.96 ↓4.7%（5D -5.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 73.89 → 今开 68.76（-6.9%） | 较昨收变动（含盘初走势） ｜ 今日高 74.26 ｜ 低 67.93

Options: P/C成交量 0.18 | OI比 0.18 | ATM IV 53.8% | Skew 0.8pp | Term 0.96 | ExpMove ±3.3%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构正常（Term 0.96）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.18×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（1D）±3.3% ｜ 11-30（4D）±5.5% ｜ 12-02（6D）±5.9% ｜ 12-04（8D）±6.8%
   ⇒ IV–VIX Spread: +26.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,634,006 | GEX Change vs 上次快照 5,061,500 | Flip: Primary Flip: 72.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 543 / LOW 191 / INVALID 492
结构观察区: Primary Flip 72.59（全链重定价，覆盖 98%）
Put Wall 75（弱结构｜现价低于该位 0.6%）
最近结构参考: Put Wall 75（现价低于该位 0.6%）
量化视角： 正 Gamma（1963万，无历史分位）｜正 Gamma 增强（+506万）｜现价位于 Flip 上方 2.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 71（MaxPain，仅结算参考）；上方 75（Put Wall，弱结构）。
• Gamma 区域：切换参考 73（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 6D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 11-27 Forward Structure
存量OI: C 85.0k / P 15.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.75 / P $1.70 ｜ ATM IV 53.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 71 ｜ Call Wall 71（-4.8%，弱）（OI 15.0k） ｜ Put Wall 70（-6.1%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 53.8%｜历史 Rank 85%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-30（Activity LOW）仓位参考: Max Pain 72 ｜ Call Wall 75（+0.6%，弱）（OI 0.8k） ｜ Put Wall 70（-6.1%，弱）（OI 0.4k）

12-02（Activity LOW）仓位参考: Max Pain 73 ｜ Call Wall 75（+0.6%）（OI 0.3k） ｜ Put Wall 71（-4.8%）（OI 0.3k）

12-04（Activity LOW）仓位参考: Max Pain 76 ｜ Call Wall 76（+1.9%）（OI 3.0k） ｜ Put Wall 70（-6.1%）（OI 6.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-26/GDX_morning.json