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
🟡 **事件差分**: 11-20 ATM IV 101.4% vs 11-27 90.2%（差 +11.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 12-11 850P ΔOI +46（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 915.86 → 收盘 885.01（-3.4%） ｜ 今日高 939.53 ｜ 低 848.50 ｜ 昨收 937.46 → 收盘 885.01（-5.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.73 | OI比 0.64 | ATM IV 117.1% | Skew 40.6pp | Term 0.76 | ExpMove ±11.2%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 40.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±11.2% ｜ 11-27（14D）±15.3% ｜ 12-04（21D）±17.2% ｜ 12-11（28D）±20.5%
   ⇒ IV–VIX Spread: +97.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,002,062 | GEX Change vs 上次快照 2,271,130 | Flip: Primary Flip: 905.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 1746 / LOW 710 / INVALID 1576
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 905.97（全链重定价，覆盖 82%）
最近结构参考: Flip 906（现价低于该位 2.3%）
量化视角： 负 Gamma（100万，无历史分位）｜负 Gamma 缓解（+227万）｜现价位于 Flip 下方 2.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 920（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 906（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +1.9k / P +4.0k ｜ Activity HIGH ｜ 7D
11-27  C +1.6k / P +0.2k ｜ Activity HIGH ｜ 14D
12-04  C +1.1k / P +0.3k ｜ Activity HIGH ｜ 21D
12-11  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 79.0k / P 58.7k，今日变化ΔOI: C +1.9k / P +4.0k，平值价格ATM: C $49.95 / P $49.51 ｜ ATM IV 101.4%，净 delta 敞口 36k shares
Top ΔOI: P 600 +1,115
仓位参考: Max Pain 1,080 ｜ Call Wall 900（+1.7%，弱）（OI 1.5k） ｜ Put Wall 870（-1.7%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 101.4%｜历史 Rank 74%（近端代理）｜IV/RV 0.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,537 股

📆 11-27 Forward Structure
存量OI: C 18.1k / P 9.8k，今日变化ΔOI: C +1.6k / P +0.2k，平值价格ATM: C $62.00 / P $73.41 ｜ ATM IV 90.2%，净 delta 敞口 54k shares
Top ΔOI: C 940 +106 ｜ C 810 +100 ｜ C 815 +100
仓位参考: Max Pain 1,090 ｜ Put Wall 800（-9.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 90.2%｜历史 Rank 74%（近端代理）｜IV/RV 0.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 54,254 股

📆 12-04 Forward Structure
存量OI: C 9.7k / P 6.2k，今日变化ΔOI: C +1.1k / P +0.3k，平值价格ATM: C $76.00 / P $76.20 ｜ ATM IV 90.0%，净 delta 敞口 11k shares
Top ΔOI: C 1200 +417 ｜ C 1100 +101
仓位参考: Max Pain 980 ｜ Call Wall 950（+7.3%，弱）（OI 0.3k） ｜ Put Wall 820（-7.3%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 90.0%｜历史 Rank 74%（近端代理）｜IV/RV 0.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,006 股

📆 12-11 Forward Structure
存量OI: C 5.2k / P 3.2k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $87.60 / P $94.01 ｜ ATM IV 88.9%，净 delta 敞口 5k shares
Top ΔOI: C 1345 +64 ｜ P 850 +46
仓位参考: Max Pain 930 ｜ Call Wall 840（-5.1%，弱）（OI 53） ｜ Put Wall 830（-6.2%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 88.9%｜历史 Rank 74%（近端代理）｜IV/RV 0.67×（近似）｜净 delta 敞口 正 4,924 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 101.4% vs 11-27 90.2%（差 +11.1pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SNDK_evening.json