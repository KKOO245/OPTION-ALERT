# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $659.51
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 97.5% vs 11-27 75.0%（差 +22.5pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 105P ΔOI +4,084（距现价 -5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 115.20 → 收盘 110.51（-4.1%） ｜ 今日高 115.70 ｜ 低 109.94 ｜ 昨收 115.02 → 收盘 110.51（-3.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.43 | OI比 0.46 | ATM IV 97.5% | Skew 5.5pp | Term 0.76 | ExpMove ±5.8%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 5.5pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±5.8% ｜ 11-27（9D）±9.3% ｜ 12-04（16D）±12.4% ｜ 12-11（23D）±16.1%
   ⇒ IV–VIX Spread: +72.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,321,953 | GEX Change vs 上次快照 -1,272,807 | Flip: Primary Flip: 117.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 318 / LOW 241 / INVALID 349
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 117.70（全链重定价，覆盖 94%）
Put Wall 110（现价高于该位 0.5%）
最近结构参考: Put Wall 110（现价高于该位 0.5%）
量化视角： 负 Gamma（932万，无历史分位）｜负 Gamma 加深（127万）｜现价位于 Flip 下方 6.11%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 110（Put Wall）；上方 131（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 118（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -0.8k / P +4.9k ｜ Activity HIGH ｜ 2D
11-27  C +2.5k / P +0.4k ｜ Activity HIGH ｜ 9D
12-04  C +1.4k / P +1.7k ｜ Activity HIGH ｜ 16D
12-11  C +0.1k / P +65 ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 138.7k / P 63.7k，今日变化ΔOI: C -0.8k / P +4.9k，平值价格ATM: C $3.50 / P $2.90 ｜ ATM IV 97.5%，净 delta 敞口 15k shares
Top ΔOI: P 105 +4,084 ｜ P 110 +2,476
仓位参考: Max Pain 131 ｜ Put Wall 120（+8.6%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 97.5%｜历史 Rank 86%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,393 股

📆 11-27 Forward Structure
存量OI: C 12.2k / P 9.9k，今日变化ΔOI: C +2.5k / P +0.4k，平值价格ATM: C $5.40 / P $4.87 ｜ ATM IV 75.0%，净 delta 敞口 47k shares
仓位参考: Max Pain 126 ｜ Call Wall 116（+5.0%，弱）（OI 0.2k） ｜ Put Wall 100（-9.5%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 75.0%｜历史 Rank 86%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 46,709 股

📆 12-04 Forward Structure
存量OI: C 8.3k / P 11.5k，今日变化ΔOI: C +1.4k / P +1.7k，平值价格ATM: C $7.34 / P $6.40 ｜ ATM IV 76.2%，净 delta 敞口 -352 shares
Top ΔOI: P 120 +198
仓位参考: Max Pain 135 ｜ Put Wall 100（-9.5%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 76.2%｜历史 Rank 86%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 352 股

12-11（MEDIUM △）Top ΔOI: 120P +35 ｜ 110P +21
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 100（-9.5%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 97.5% vs 11-27 75.0%（差 +22.5pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/COIN_evening.json