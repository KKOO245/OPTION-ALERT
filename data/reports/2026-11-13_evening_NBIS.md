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
🟡 **事件差分**: 11-20 ATM IV 112.5% vs 11-27 102.4%（差 +10.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 12-04 130C ΔOI +1,797 占该期限总 OI 11.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 123.52 → 收盘 115.88（-6.2%） ｜ 今日高 123.97 ｜ 低 109.00 ｜ 昨收 128.64 → 收盘 115.88（-9.9%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.83 | OI比 0.47 | ATM IV 114.3% | Skew 4.8pp | Term 0.89 | ExpMove ±12.3%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±12.3% ｜ 11-27（14D）±16.4% ｜ 12-04（21D）±19.5% ｜ 12-11（28D）±23.0%
   ⇒ IV–VIX Spread: +95.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -11,592,750 | GEX Change vs 上次快照 -271,194 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 466 / LOW 97 / INVALID 337
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（1159万，无历史分位）｜负 Gamma 加深（27万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +12.0k / P -0.9k ｜ Activity HIGH ｜ 7D
11-27  C +5.6k / P -1.0k ｜ Activity HIGH ｜ 14D
12-04  C +3.9k / P +1.0k ｜ Activity HIGH ｜ 21D
12-11  C +1.0k / P +1.2k ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 145.3k / P 113.4k，今日变化ΔOI: C +12.0k / P -0.9k，平值价格ATM: C $7.21 / P $7.06 ｜ ATM IV 112.5%，净 delta 敞口 792k shares
Top ΔOI: C 125 +2,746 ｜ P 230 -2,432
仓位参考: Max Pain 160 ｜ Call Wall 125（+7.9%，弱）（OI 3.5k） ｜ Put Wall 115（-0.8%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 112.5%｜历史 Rank 64%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 792,104 股

📆 11-27 Forward Structure
存量OI: C 23.1k / P 18.6k，今日变化ΔOI: C +5.6k / P -1.0k，平值价格ATM: C $9.76 / P $9.20 ｜ ATM IV 102.4%，净 delta 敞口 214k shares
Top ΔOI: P 230 -1,308 ｜ C 150 +800
仓位参考: Max Pain 160 ｜ Call Wall 125（+7.9%，弱）（OI 0.5k） ｜ Put Wall 115（-0.8%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 102.4%｜历史 Rank 64%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 213,924 股

📆 12-04 Forward Structure
存量OI: C 8.4k / P 7.6k，今日变化ΔOI: C +3.9k / P +1.0k，平值价格ATM: C $11.80 / P $10.80 ｜ ATM IV 102.9%，净 delta 敞口 105k shares
Top ΔOI: C 130 +1,797 ｜ P 80 +1,286 ｜ P 100 -731
仓位参考: Max Pain 130 ｜ Call Wall 120（+3.6%，弱）（OI 0.6k） ｜ Put Wall 115（-0.8%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 102.9%｜历史 Rank 64%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 105,474 股

📆 12-11 Forward Structure
存量OI: C 3.8k / P 5.4k，今日变化ΔOI: C +1.0k / P +1.2k，平值价格ATM: C $14.34 / P $12.35 ｜ ATM IV 101.5%，净 delta 敞口 -15k shares
Top ΔOI: C 130 +429 ｜ P 130 +304
仓位参考: Max Pain 145 ｜ Call Wall 125（+7.9%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 101.5%｜历史 Rank 64%（近端代理）｜IV/RV 0.72×（近似）｜净 delta 敞口 负 15,082 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 112.5% vs 11-27 102.4%（差 +10.1pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/NBIS_evening.json