# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 12.64 → 收盘 12.53（-0.9%） ｜ 今日高 13.01 ｜ 低 12.33 ｜ 昨收 13.33 → 收盘 12.53（-6.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.34 | OI比 0.19 | ATM IV 92.9% | Skew 28.8pp | Term 0.84 | ExpMove ±3.4%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价显著（Skew 28.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.19）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.19×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±3.4% ｜ 10-30（8D）±9.3% ｜ 11-06（15D）±13.7% ｜ 11-13（22D）±18.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 892,274 | GEX Change vs 上次快照 229,225 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 130 / LOW 93 / INVALID 179
结构观察区: NO_CROSS
量化视角： 正 Gamma（89万，无历史分位）｜正 Gamma 增强（+23万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0.2k / P -0.2k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 8D
11-06  C +41 / P +5 ｜ Activity LOW ｜ 15D
11-13  C +15 / P +3 ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 7.0k / P 1.4k，今日变化ΔOI: C +0.2k / P -0.2k，平值价格ATM: C $0.35 / P $0.07 ｜ ATM IV 92.9%，净 delta 敞口 24k shares
仓位参考: Max Pain 14
量化解读： 存量 Call 重｜ATM IV 92.9%｜历史 Rank 30%（近端代理）｜IV/RV 1.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 23,607 股

10-30（MEDIUM △）Top ΔOI: 13P +171 ｜ 13P +149
10-30（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 13（+3.8%，弱）（OI 0.2k）

11-06（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 13（+3.8%，弱）（OI 77）

11-13（MEDIUM △）Top ΔOI: 12P +5 ｜ 13P -5
11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+7.7%，弱）（OI 51） ｜ Put Wall 12.5（-0.2%，弱）（OI 66）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/NNE_evening.json