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
🟡 **事件差分**: 11-20 ATM IV 61.7% vs 11-27 50.8%（差 +10.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 12-11 150P ΔOI +112（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 153.26 → 收盘 149.30（-2.6%） ｜ 今日高 154.37 ｜ 低 144.65 ｜ 昨收 154.99 → 收盘 149.30（-3.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 3.76 | OI比 2.14 | ATM IV N/A | Skew 29.6pp | Term N/A | ExpMove ±7.3%（近端） | Rank — (历史不足)
量化视角： 保护溢价显著（Skew 29.6pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 3.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.76×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.14×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±7.3% ｜ 11-27（14D）±8.8% ｜ 12-04（21D）±6.1% ｜ 12-11（28D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -15,236,575 | GEX Change vs 上次快照 15,405,894 | Flip: Primary Flip: 154.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 81%（带内） ｜ IV 有效性: VALID 427 / LOW 479 / INVALID 898
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 154.14（全链重定价，覆盖 81%）
Call Wall 155（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 154（现价低于该位 3.1%）
量化视角： 负 Gamma（1524万，无历史分位）｜负 Gamma 缓解（+1541万）｜现价位于 Flip 下方 3.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 153（MaxPain，仅结算参考） / 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 154（全链重定价，覆盖 81%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -8.0k / P -3.7k ｜ Activity HIGH ｜ 7D
11-27  C +2.1k / P +0.6k ｜ Activity HIGH ｜ 14D
12-04  C +0.9k / P +0.7k ｜ Activity HIGH ｜ 21D
12-11  C +76 / P -98 ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 199.2k / P 248.1k，今日变化ΔOI: C -8.0k / P -3.7k，平值价格ATM: C $5.60 / P $5.30 ｜ ATM IV 61.7%，净 delta 敞口 36k shares
Top ΔOI: C 166 -8,887 ｜ P 140 -3,641 ｜ P 125 -3,482
仓位参考: Max Pain 158 ｜ Call Wall 155（+3.8%，弱）（OI 17.9k） ｜ Put Wall 153.33（+2.7%，弱）（OI 17.3k）
量化解读： 存量 Put 重｜ATM IV 61.7%｜IV/RV 0.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,686 股

📆 11-27 Forward Structure
存量OI: C 32.1k / P 26.0k，今日变化ΔOI: C +2.1k / P +0.6k，平值价格ATM: C $7.20 / P $5.90 ｜ ATM IV 50.8%，净 delta 敞口 181 shares
Top ΔOI: C 167 +1,004 ｜ C 175 +934 ｜ P 150 +266
仓位参考: Max Pain 162 ｜ Put Wall 150（+0.5%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 50.8%｜IV/RV 0.12×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 181 股

📆 12-04 Forward Structure
存量OI: C 10.8k / P 10.0k，今日变化ΔOI: C +0.9k / P +0.7k，平值价格ATM: C $0.00 / P $9.10 ｜ ATM IV 55.2%，净 delta 敞口 -6k shares
Top ΔOI: C 175 +503 ｜ P 135 +464
仓位参考: Max Pain 158 ｜ Call Wall 153.33（+2.7%，弱）（OI 0.4k） ｜ Put Wall 150（+0.5%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 55.2%｜IV/RV 0.13×（近似）｜净 delta 敞口 负 5,695 股

12-11（MEDIUM △）Top ΔOI: 147C -367 ｜ 150P +112
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 155（+3.8%，弱）（OI 0.2k） ｜ Put Wall 140（-6.2%）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 61.7% vs 11-27 50.8%（差 +10.9pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SOXX_evening.json