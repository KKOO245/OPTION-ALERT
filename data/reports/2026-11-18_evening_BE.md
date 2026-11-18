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
🔴 **事件差分**: 11-20（2D）ATM IV 133.9% vs 11-27 103.1%（差 +30.8pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 170C ΔOI +881（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 180.47 → 收盘 170.98（-5.3%） ｜ 今日高 180.47 ｜ 低 167.36 ｜ 昨收 173.46 → 收盘 170.98（-1.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.56 | OI比 0.85 | ATM IV 134.0% | Skew 13.2pp | Term 0.74 | ExpMove ±7.9%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 13.2pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（2D）±7.9% ｜ 11-27（9D）±12.7% ｜ 12-04（16D）±16.6% ｜ 12-11（23D）±20.1%
   ⇒ IV–VIX Spread: +109.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,654,713 | GEX Change vs 上次快照 -2,068,885 | Flip: Primary Flip: 189.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 521 / LOW 124 / INVALID 153
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 189.77（全链重定价，覆盖 100%）
最近结构参考: Flip 190（现价低于该位 9.9%）
量化视角： 负 Gamma（965万，无历史分位）｜负 Gamma 加深（207万）｜现价位于 Flip 下方 9.90%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 195（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 190（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +5.6k / P -1.9k ｜ Activity HIGH ｜ 2D
11-27  C +1.3k / P +0.7k ｜ Activity HIGH ｜ 9D
12-04  C +0.6k / P +0.4k ｜ Activity HIGH ｜ 16D
12-11  C +0.2k / P -0.5k ｜ Activity HIGH ｜ 23D

📆 11-20 Forward Structure
存量OI: C 105.4k / P 89.8k，今日变化ΔOI: C +5.6k / P -1.9k，平值价格ATM: C $7.25 / P $6.25 ｜ ATM IV 133.9%，净 delta 敞口 528k shares
Top ΔOI: P 250 -1,461 ｜ C 170 +881 ｜ C 180 +793
仓位参考: Max Pain 195 ｜ Call Wall 180（+5.3%，弱）（OI 2.9k） ｜ Put Wall 170（-0.6%，弱）（OI 5.0k）
量化解读： 存量两侧均衡｜ATM IV 133.9%｜历史 Rank 84%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 527,561 股

📆 11-27 Forward Structure
存量OI: C 15.9k / P 12.8k，今日变化ΔOI: C +1.3k / P +0.7k，平值价格ATM: C $11.45 / P $10.20 ｜ ATM IV 103.1%，净 delta 敞口 40k shares
Top ΔOI: C 195 +297 ｜ C 180 +267 ｜ C 167 +234
仓位参考: Max Pain 200 ｜ Call Wall 185（+8.2%，弱）（OI 0.8k） ｜ Put Wall 175（+2.4%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 103.1%｜历史 Rank 84%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,702 股

📆 12-04 Forward Structure
存量OI: C 8.7k / P 7.9k，今日变化ΔOI: C +0.6k / P +0.4k，平值价格ATM: C $14.95 / P $13.49 ｜ ATM IV 99.9%，净 delta 敞口 -2k shares
Top ΔOI: C 200 +163 ｜ C 185 +155
仓位参考: Max Pain 200 ｜ Call Wall 185（+8.2%，弱）（OI 0.4k） ｜ Put Wall 185（+8.2%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 99.9%｜历史 Rank 84%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 负 1,565 股

📆 12-11 Forward Structure
存量OI: C 3.7k / P 4.4k，今日变化ΔOI: C +0.2k / P -0.5k，平值价格ATM: C $18.00 / P $16.43 ｜ ATM IV 100.0%，净 delta 敞口 35k shares
Top ΔOI: P 175 -813 ｜ P 150 +205
仓位参考: Max Pain 210 ｜ Put Wall 175（+2.4%）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 100.0%｜历史 Rank 84%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 34,744 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 133.9% vs 11-27 103.1%（差 +30.8pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/BE_evening.json