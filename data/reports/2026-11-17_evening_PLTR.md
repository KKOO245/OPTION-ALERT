# 期权晚报 2026-11-17（快照 16:40 ET）

📊 市场环境

SPY $732.44 ｜ QQQ $656.95
VIX 25.46 ↑11.1%（5D +30.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（3D）ATM IV 84.8% vs 11-27 64.0%（差 +20.8pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-27 150P ΔOI +2,670（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 159.97 → 收盘 156.56（-2.1%） ｜ 今日高 162.59 ｜ 低 153.91 ｜ 昨收 160.39 → 收盘 156.56（-2.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 0.70 | OI比 0.84 | ATM IV 84.8% | Skew 11.5pp | Term 0.69 | ExpMove ±6.2%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 11.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（3D）±6.2% ｜ 11-27（10D）±8.4% ｜ 12-04（17D）±10.4% ｜ 12-11（24D）±12.3%
   ⇒ IV–VIX Spread: +59.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -18,082,609 | GEX Change vs 上次快照 -10,029,252 | Flip: Primary Flip: 161.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 420 / LOW 161 / INVALID 217
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 161.84（全链重定价，覆盖 100%）
最近结构参考: Flip 162（现价低于该位 3.3%）
量化视角： 负 Gamma（1808万，无历史分位）｜负 Gamma 加深（1003万）｜现价位于 Flip 下方 3.26%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 162（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +20.7k / P -4.8k ｜ Activity HIGH ｜ 3D
11-27  C +2.4k / P +5.1k ｜ Activity HIGH ｜ 10D
12-04  C +1.1k / P -0.3k ｜ Activity HIGH ｜ 17D
12-11  C +0.2k / P +0.6k ｜ Activity HIGH ｜ 24D

📆 11-20 Forward Structure
存量OI: C 240.8k / P 202.6k，今日变化ΔOI: C +20.7k / P -4.8k，平值价格ATM: C $4.35 / P $5.35 ｜ ATM IV 84.8%，净 delta 敞口 885k shares
Top ΔOI: C 180 +8,550 ｜ C 177 +6,255 ｜ P 200 -4,433
仓位参考: Max Pain 170 ｜ Call Wall 170（+8.6%，弱）（OI 10.3k） ｜ Put Wall 150（-4.2%，弱）（OI 8.7k）
量化解读： 存量 Call 重｜ATM IV 84.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 884,629 股

📆 11-27 Forward Structure
存量OI: C 23.0k / P 35.6k，今日变化ΔOI: C +2.4k / P +5.1k，平值价格ATM: C $6.00 / P $7.22 ｜ ATM IV 64.0%，净 delta 敞口 -125k shares
Top ΔOI: P 150 +2,670 ｜ P 149 +553
仓位参考: Max Pain 172 ｜ Call Wall 165（+5.4%，弱）（OI 0.7k） ｜ Put Wall 150（-4.2%，弱）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 64.0%｜历史 Rank 92%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 125,425 股

📆 12-04 Forward Structure
存量OI: C 17.6k / P 13.3k，今日变化ΔOI: C +1.1k / P -0.3k，平值价格ATM: C $7.90 / P $8.46 ｜ ATM IV 60.8%，净 delta 敞口 49k shares
Top ΔOI: P 155 -850 ｜ P 140 +241
仓位参考: Max Pain 175 ｜ Put Wall 155（-1.0%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 60.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,855 股

📆 12-11 Forward Structure
存量OI: C 9.0k / P 11.5k，今日变化ΔOI: C +0.2k / P +0.6k，平值价格ATM: C $10.84 / P $8.40 ｜ ATM IV 60.0%，净 delta 敞口 -6k shares
Top ΔOI: P 145 +87 ｜ P 150 +70
仓位参考: Max Pain 170 ｜ Call Wall 170（+8.6%，弱）（OI 0.5k） ｜ Put Wall 150（-4.2%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 60.0%｜历史 Rank 92%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 5,915 股

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 84.8% vs 11-27 64.0%（差 +20.8pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/PLTR_evening.json