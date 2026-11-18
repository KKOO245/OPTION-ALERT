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
🔴 **事件差分**: 11-18（1D）ATM IV 193.1% vs 11-20 122.8%（差 +70.3pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 156.91 → 收盘 155.46（-0.9%） ｜ 今日高 158.19 ｜ 低 150.33 ｜ 昨收 156.14 → 收盘 155.46（-0.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 0.77 | OI比 0.81 | ATM IV 193.1% | Skew 3.8pp | Term 0.27 | ExpMove ±8.1%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.27，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（1D）±8.1% ｜ 11-20（3D）±0.6% ｜ 11-23（6D）±10.2% ｜ 11-25（8D）±11.4%
   ⇒ IV–VIX Spread: +167.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -39,735,269 | GEX Change vs 上次快照 -18,202,172 | Flip: Primary Flip: 158.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1155 / LOW 229 / INVALID 690
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 158.71（全链重定价，覆盖 100%）
最近结构参考: Flip 159（现价低于该位 2.0%）
量化视角： 负 Gamma（3974万，无历史分位）｜负 Gamma 加深（1820万）｜现价位于 Flip 下方 2.05%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-23  C +0 / P +0 ｜ Activity LOW ｜ 6D
11-25  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 11-18 Forward Structure
存量OI: C 244.2k / P 196.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.65 / P $6.00 ｜ ATM IV 193.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 160 ｜ Call Wall 170（+9.4%，弱）（OI 16.2k） ｜ Put Wall 150（-3.5%，弱）（OI 18.6k）
量化解读： 存量 Call 重｜ATM IV 193.1%｜历史 Rank 100%（近端代理）｜IV/RV 3.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 182 ｜ Call Wall 170（+9.4%，弱）（OI 56.6k） ｜ Put Wall 150（-3.5%，弱）（OI 49.0k）

11-23（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 160（+2.9%，弱）（OI 3.2k） ｜ Put Wall 145（-6.7%，弱）（OI 2.6k）

11-25（Activity LOW）仓位参考: Max Pain 158 ｜ Call Wall 165（+6.1%，弱）（OI 3.2k） ｜ Put Wall 150（-3.5%，弱）（OI 0.9k）

📅 事件差分（观察，非因果）: 11-18（1D）ATM IV 193.1% vs 11-20 122.8%（差 +70.3pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/NVDA_evening.json