# 期权晚报 2026-10-28（快照 21:00 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **事件差分**: 10-30 ATM IV 59.4% vs 11-02 46.1%（差 +13.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 147.29 → 收盘 145.23（-1.4%） ｜ 今日高 147.57 ｜ 低 142.13 ｜ 昨收 148.58 → 收盘 145.23（-2.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-02，窗口结束前不做对错判定）

Options: P/C成交量 0.42 | OI比 0.70 | ATM IV 59.4% | Skew 1.9pp | Term 0.82 | ExpMove ±3.5%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±3.5% ｜ 11-02（5D）±4.4% ｜ 11-04（7D）±5.7% ｜ 11-06（9D）±6.6%
   ⇒ IV–VIX Spread: +42.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -54,466,584 | GEX Change vs 上次快照 -7,191,345 | Flip: Primary Flip: 148.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 717 / LOW 153 / INVALID 560
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 148.93（全链重定价，覆盖 99%）
Put Wall 135（弱结构｜现价高于该位 7.6%）
最近结构参考: Flip 149（现价低于该位 2.5%）
量化视角： 负 Gamma（5447万，无历史分位）｜负 Gamma 加深（719万）｜现价位于 Flip 下方 2.48%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构）；上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 149（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-30 Forward Structure
存量OI: C 275.5k / P 194.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.69 / P $2.44 ｜ ATM IV 59.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 150 ｜ Call Wall 155（+6.7%，弱）（OI 20.8k） ｜ Put Wall 150（+3.3%）（OI 20.3k）
量化解读： 存量 Call 重｜ATM IV 59.4%｜历史 Rank 68%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-02（Activity LOW）仓位参考: Max Pain 148 ｜ Call Wall 152.5（+5.0%，弱）（OI 2.1k） ｜ Put Wall 145（-0.2%）（OI 2.8k）

11-04（Activity LOW）仓位参考: Max Pain 150 ｜ Call Wall 155（+6.7%，弱）（OI 0.8k） ｜ Put Wall 135（-7.0%，弱）（OI 0.7k）

11-06（Activity LOW）仓位参考: Max Pain 150 ｜ Put Wall 140（-3.6%，弱）（OI 10.4k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 59.4% vs 11-02 46.1%（差 +13.3pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SPCX_evening.json