# 期权晚报 2026-11-25（快照 21:00 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 71.32 → 收盘 73.61（+3.2%） ｜ 今日高 73.77 ｜ 低 67.02 ｜ 昨收 77.95 → 收盘 73.61（-5.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 0.44 | ATM IV 114.4% | Skew 6.8pp | Term 1.02 | ExpMove ±6.7%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 1.02）｜保护溢价显著（Skew 6.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±6.7% ｜ 12-04（9D）±16.2% ｜ 12-11（16D）±21.1% ｜ 12-18（23D）±24.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -43,317,603 | GEX Change vs 上次快照 -6,864,921 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1123 / LOW 1023 / INVALID 3824
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 75（现价低于该位 1.9%）
最近结构参考: Put Wall 75（现价低于该位 1.9%）
量化视角： 负 Gamma（4332万，无历史分位）｜负 Gamma 加深（686万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 75（Put Wall） / 90（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 2D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 9D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 16D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 11-27 Forward Structure
存量OI: C 308.6k / P 135.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.37 / P $2.55 ｜ ATM IV 114.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 90 ｜ Put Wall 75（+1.9%）（OI 10.7k）
量化解读： 存量 Call 重｜ATM IV 114.4%｜历史 Rank 70%（近端代理）｜IV/RV 0.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 100 ｜ Put Wall 71.25（-3.2%，弱）（OI 2.8k）

12-11（Activity LOW）仓位参考: Max Pain 102 ｜ Call Wall 80（+8.7%，弱）（OI 2.4k） ｜ Put Wall 80（+8.7%）（OI 10.5k）

12-18（Activity LOW）仓位参考: Max Pain 111 ｜ Put Wall 75（+1.9%，弱）（OI 44.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SNDK_evening.json