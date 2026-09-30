# 期权晚报 2026-09-30（快照 16:40 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $739.77
VIX 16.34 ↑1.9%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 83P ΔOI +1,527（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 89.72 → 收盘 87.80（-2.1%） ｜ 今日高 89.75 ｜ 低 87.80 ｜ 昨收 89.07 → 收盘 87.80（-1.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-05，窗口结束前不做对错判定）

Options: P/C成交量 0.06 | OI比 0.49 | ATM IV 41.8% | Skew -1.7pp | Term 0.97 | ExpMove ±2.5%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -1.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.06×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.5% ｜ 10-09（9D）±4.9% ｜ 10-16（16D）±6.7% ｜ 10-23（23D）±7.5%
   ⇒ IV–VIX Spread: +25.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -24,579,206 | GEX Change vs 上次快照 -6,746,623 | Flip: Primary Flip: 89.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 435 / LOW 119 / INVALID 258
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 89.32（全链重定价，覆盖 87%）
Put Wall 90（弱结构｜现价低于该位 2.4%）
最近结构参考: Flip 89（现价低于该位 1.7%）
量化视角： 负 Gamma（2458万，无历史分位）｜负 Gamma 加深（675万）｜现价位于 Flip 下方 1.71%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 93（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 89（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0.3k / P +1.8k ｜ Activity HIGH ｜ 2D
10-09  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 9D
10-16  C -33 / P +3.4k ｜ Activity MEDIUM △ ｜ 16D
10-23  C +73 / P +83 ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 130.1k / P 63.5k，今日变化ΔOI: C +0.3k / P +1.8k，平值价格ATM: C $1.08 / P $1.07 ｜ ATM IV 41.8%，净 delta 敞口 52k shares
Top ΔOI: C 95 -1,720 ｜ P 83 +1,527 ｜ P 86 -1,517
仓位参考: Max Pain 93 ｜ Put Wall 90（+2.5%，弱）（OI 9.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.8%｜历史 Rank 63%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 52,023 股

📆 10-09 Forward Structure
存量OI: C 9.2k / P 15.7k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $2.15 / P $2.17 ｜ ATM IV 40.5%，净 delta 敞口 -6k shares
Top ΔOI: P 88 +221 ｜ C 90 +191 ｜ P 85 +78
仓位参考: Max Pain 94 ｜ Call Wall 90（+2.5%，弱）（OI 0.3k） ｜ Put Wall 90（+2.5%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 40.5%｜历史 Rank 63%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,752 股

10-16（MEDIUM △）Top ΔOI: 86P +2,978 ｜ 89P +277
10-16（MEDIUM △）仓位参考: Max Pain 92 ｜ Call Wall 90（+2.5%，弱）（OI 5.2k） ｜ Put Wall 90（+2.5%，弱）（OI 10.9k）

10-23（MEDIUM △）Top ΔOI: 85P +66 ｜ 80P -34
10-23（MEDIUM △）仓位参考: Max Pain 95 ｜ Call Wall 91（+3.6%，弱）（OI 0.2k） ｜ Put Wall 85（-3.2%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/GDX_evening.json