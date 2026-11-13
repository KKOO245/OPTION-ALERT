# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 110P ΔOI +978（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 112.00 → 收盘 111.62（-0.3%） ｜ 今日高 113.08 ｜ 低 108.25 ｜ 昨收 114.41 → 收盘 111.62（-2.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 1.10 | OI比 0.75 | ATM IV 78.0% | Skew 6.5pp | Term 0.96 | ExpMove ±8.6%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构正常（Term 0.96）｜保护溢价显著（Skew 6.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±8.6% ｜ 11-27（14D）±11.2% ｜ 12-04（21D）±14.0% ｜ 12-11（28D）±16.9%
   ⇒ IV–VIX Spread: +58.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,004,122 | GEX Change vs 上次快照 3,141,925 | Flip: Primary Flip: 113.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 412 / LOW 193 / INVALID 427
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 113.62（全链重定价，覆盖 86%）
最近结构参考: Flip 114（现价低于该位 1.8%）
量化视角： 负 Gamma（700万，无历史分位）｜负 Gamma 缓解（+314万）｜现价位于 Flip 下方 1.76%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 120（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 114（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +84.8k / P -4.7k ｜ Activity HIGH ｜ 7D
11-27  C +2.1k / P +4.8k ｜ Activity HIGH ｜ 14D
12-04  C -3.6k / P +4.6k ｜ Activity HIGH ｜ 21D
12-11  C +0.5k / P +4.3k ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 257.2k / P 155.8k，今日变化ΔOI: C +84.8k / P -4.7k，平值价格ATM: C $4.55 / P $4.99 ｜ ATM IV 77.3%，净 delta 敞口 2.9M shares
Top ΔOI: C 126 +17,888 ｜ C 120 +17,278 ｜ C 127 +13,931
仓位参考: Max Pain 121 ｜ Call Wall 120（+7.5%，弱）（OI 19.4k） ｜ Put Wall 110（-1.5%，弱）（OI 15.2k）
量化解读： 存量 Call 重｜ATM IV 77.3%｜历史 Rank 45%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,935,241 股

📆 11-27 Forward Structure
存量OI: C 20.7k / P 55.3k，今日变化ΔOI: C +2.1k / P +4.8k，平值价格ATM: C $6.10 / P $6.35 ｜ ATM IV 72.1%，净 delta 敞口 120k shares
Top ΔOI: P 165 -1,175 ｜ P 110 +978 ｜ P 80 +886
仓位参考: Max Pain 145 ｜ Put Wall 115（+3.0%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 72.1%｜历史 Rank 45%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 119,780 股

📆 12-04 Forward Structure
存量OI: C 13.7k / P 37.5k，今日变化ΔOI: C -3.6k / P +4.6k，平值价格ATM: C $8.85 / P $6.80 ｜ ATM IV 74.0%，净 delta 敞口 -42k shares
Top ΔOI: P 80 +718
仓位参考: Max Pain 150 ｜ Put Wall 120（+7.5%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 74.0%｜历史 Rank 45%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 42,117 股

📆 12-11 Forward Structure
存量OI: C 6.2k / P 23.1k，今日变化ΔOI: C +0.5k / P +4.3k，平值价格ATM: C $11.00 / P $7.90 ｜ ATM IV 75.1%，净 delta 敞口 -95k shares
Top ΔOI: P 75 +546 ｜ P 80 +512
仓位参考: Max Pain 155 ｜ Call Wall 120（+7.5%，弱）（OI 0.5k） ｜ Put Wall 120（+7.5%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 75.1%｜历史 Rank 45%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 94,869 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 77.3% vs 11-27 72.1%（差 +5.2pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/MSTR_evening.json