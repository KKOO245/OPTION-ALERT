# 期权晨报 2026-09-24（快照 10:20 ET）

📊 市场环境

SPY $765.80 ｜ QQQ $741.10
VIX 15.64 ↑3.0%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 741.21 → 今开 735.16（-0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 737.77 ｜ 低 734.63

Options: P/C成交量 0.75 | OI比 1.28 | ATM IV 15.3% | Skew 1.9pp | Term 1.16 | ExpMove ±1.2%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构正常偏陡（Term 1.16）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.28×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 93% ｜ P/C OI(近端) 20%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 93%）｜近端持仓结构中性（P/C OI 分位 20%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-25（1D）±1.2% ｜ 09-28（4D）±1.4% ｜ 09-29（5D）±1.6% ｜ 09-30（6D）±1.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 626,596,473 | GEX Change vs 上次快照 204,559,274 | Flip: Primary Flip: 729.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 3040 / LOW 146 / INVALID 1622
结构观察区: Primary Flip 729.53（全链重定价，覆盖 100%）
最近结构参考: Flip 730（现价高于该位 2.6%）
量化视角： 正 Gamma（6.27亿，历史分位偏正区，比 93% 的交易日更正）｜正 Gamma 增强（+2.05亿）｜现价位于 Flip 上方 2.58%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 728（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 730（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
🎯 今日到期（0DTE）
存量OI: C 42.1k / P 53.8k，今日成交量: C 87.0k / P 65.3k，平值价格ATM: C $3.06 / P $3.71 ｜ ATM IV 15.3%，预期波动 ±0.9%，Max Pain 728

📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-29  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-30  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-25 Forward Structure
存量OI: C 175.9k / P 438.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.20 / P $4.52 ｜ ATM IV 15.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 726 ｜ Call Wall 755（+0.9%，弱）（OI 13.0k）
量化解读： 存量 Put 重｜ATM IV 15.9%｜历史 Rank 31%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-28（Activity LOW）仓位参考: Max Pain 730 ｜ Call Wall 750（+0.2%，弱）（OI 1.9k） ｜ Put Wall 730（-2.4%，弱）（OI 2.9k）

09-29（Activity LOW）仓位参考: Max Pain 725 ｜ Call Wall 740（-1.1%，弱）（OI 0.9k）

09-30（Activity LOW）仓位参考: Max Pain 720 ｜ Call Wall 735（-1.8%，弱）（OI 13.7k） ｜ Put Wall 730（-2.4%，弱）（OI 32.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/QQQ_morning.json