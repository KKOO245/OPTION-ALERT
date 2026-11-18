# 期权晚报 2026-11-17（快照 21:00 ET）

📊 市场环境

SPY $732.44 ｜ QQQ $nan
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
🔴 **事件差分**: 11-20（3D）ATM IV 94.8% vs 11-27 69.5%（差 +25.3pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 142.84 → 收盘 141.46（-1.0%） ｜ 今日高 142.99 ｜ 低 136.17 ｜ 昨收 141.22 → 收盘 141.46（+0.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 2.48 | OI比 1.81 | ATM IV 94.8% | Skew 22.6pp | Term 0.64 | ExpMove ±6.7%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价显著（Skew 22.6pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.48×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.81×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±6.7% ｜ 11-27（10D）±9.3% ｜ 12-04（17D）±14.3% ｜ 12-11（24D）±19.4%
   ⇒ IV–VIX Spread: +69.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -63,745,757 | GEX Change vs 上次快照 -3,886,525 | Flip: Primary Flip: 153.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 606 / LOW 376 / INVALID 644
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 153.40（全链重定价，覆盖 100%）
最近结构参考: Flip 153（现价低于该位 7.8%）
量化视角： 负 Gamma（6375万，无历史分位）｜负 Gamma 加深（389万）｜现价位于 Flip 下方 7.78%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 10D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 17D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 11-20 Forward Structure
存量OI: C 199.7k / P 362.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.70 / P $5.80 ｜ ATM IV 94.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 157 ｜ Call Wall 145（+2.5%，弱）（OI 5.8k） ｜ Put Wall 140（-1.0%，弱）（OI 22.0k）
量化解读： 存量 Put 重｜ATM IV 94.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-27（Activity LOW）仓位参考: Max Pain 160 ｜ Put Wall 150（+6.0%，弱）（OI 3.6k）

12-04（Activity LOW）仓位参考: Max Pain 157 ｜ Call Wall 150（+6.0%，弱）（OI 0.3k） ｜ Put Wall 140（-1.0%，弱）（OI 5.2k）

12-11（Activity LOW）仓位参考: Max Pain 148 ｜ Call Wall 147（+3.9%，弱）（OI 0.2k） ｜ Put Wall 140（-1.0%）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 94.8% vs 11-27 69.5%（差 +25.3pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/SOXX_evening.json