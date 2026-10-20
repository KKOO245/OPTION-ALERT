# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 13P ΔOI +5（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 12P ΔOI -125 占该期限总 OI 12.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 12.66 → 收盘 12.96（+2.4%） ｜ 今日高 13.29 ｜ 低 12.56 ｜ 昨收 13.01 → 收盘 12.96（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.26 | OI比 0.27 | ATM IV 81.6% | Skew 1.1pp | Term 0.90 | ExpMove ±7.7%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常（Term 0.90）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.27×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±7.7% ｜ 10-30（10D）±10.0% ｜ 11-06（17D）±14.3% ｜ 11-13（24D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 727,422 | GEX Change vs 上次快照 134,851 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 186 / LOW 81 / INVALID 135
结构观察区: NO_CROSS
Put Wall 14（现价低于该位 7.4%）
最近结构参考: Put Wall 14（现价低于该位 7.4%）
量化视角： 正 Gamma（73万，无历史分位）｜正 Gamma 增强（+13万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 14（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0.7k / P +43 ｜ Activity MEDIUM △ ｜ 3D
10-30  C +0.4k / P +18 ｜ Activity MEDIUM △ ｜ 10D
11-06  C +6 / P +11 ｜ Activity MEDIUM △ ｜ 17D
11-13  C +17 / P -74 ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 6.5k / P 1.7k，今日变化ΔOI: C +0.7k / P +43，平值价格ATM: C $0.47 / P $0.53 ｜ ATM IV 81.6%，净 delta 敞口 16k shares
Top ΔOI: C 14 +305 ｜ C 13 +286 ｜ C 13 +51
仓位参考: Max Pain 14 ｜ Put Wall 14（+8.0%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 81.6%｜历史 Rank 13%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,911 股

10-30（MEDIUM △）Top ΔOI: 14C +42
10-30（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 14（+8.0%）（OI 0.4k）

11-06（MEDIUM △）Top ΔOI: 13P +5
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（+0.3%，弱）（OI 77）

📆 11-13 Forward Structure
存量OI: C 0.6k / P 0.4k，今日变化ΔOI: C +17 / P -74，平值价格ATM: C $1.28 / P $1.00 ｜ ATM IV 75.2%，净 delta 敞口 3k shares
Top ΔOI: P 12 -125 ｜ P 13 +50
仓位参考: Max Pain 14 ｜ Call Wall 13.5（+4.2%，弱）（OI 50） ｜ Put Wall 12.5（-3.5%）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 75.2%｜历史 Rank 13%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 正 2,752 股

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 81.6% vs 10-30 75.6%（差 +6.0pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/NNE_evening.json