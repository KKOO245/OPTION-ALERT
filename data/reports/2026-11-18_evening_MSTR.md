# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $nan
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
🔴 **事件差分**: 11-20（2D）ATM IV 122.2% vs 11-27 97.2%（差 +25.0pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 95.02 → 收盘 90.32（-4.9%） ｜ 今日高 95.51 ｜ 低 90.20 ｜ 昨收 96.50 → 收盘 90.32（-6.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-23，窗口结束前不做对错判定）

Options: P/C成交量 0.53 | OI比 0.58 | ATM IV 122.2% | Skew 13.5pp | Term 0.74 | ExpMove ±7.3%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 13.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±7.3% ｜ 11-27（9D）±12.0% ｜ 12-04（16D）±15.7% ｜ 12-11（23D）±18.6%
   ⇒ IV–VIX Spread: +97.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -38,358,566 | GEX Change vs 上次快照 -4,490,703 | Flip: Primary Flip: 101.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 481 / LOW 245 / INVALID 408
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 101.25（全链重定价，覆盖 100%）
Put Wall 90（弱结构｜现价高于该位 0.4%）
最近结构参考: Put Wall 90（现价高于该位 0.4%）
量化视角： 负 Gamma（3836万，无历史分位）｜负 Gamma 加深（449万）｜现价位于 Flip 下方 10.80%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构）；上方 110（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 101（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -11.3k / P -8.0k ｜ Activity MEDIUM △ ｜ 2D
11-27  C +6.4k / P +13.6k ｜ Activity HIGH ｜ 9D
12-04  C +3.3k / P +2.6k ｜ Activity HIGH ｜ 16D
12-11  C +0.3k / P +4.2k ｜ Activity HIGH ｜ 23D

📆 11-20 Forward Structure
存量OI: C 325.3k / P 188.1k，今日变化ΔOI: C -11.3k / P -8.0k，平值价格ATM: C $3.50 / P $3.10 ｜ ATM IV 122.2%，净 delta 敞口 1.0M shares
仓位参考: Max Pain 110 ｜ Put Wall 90（-0.4%，弱）（OI 14.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 122.2%｜历史 Rank 91%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,036,962 股

📆 11-27 Forward Structure
存量OI: C 43.3k / P 91.6k，今日变化ΔOI: C +6.4k / P +13.6k，平值价格ATM: C $5.65 / P $5.18 ｜ ATM IV 97.2%，净 delta 敞口 -74k shares
Top ΔOI: P 87 +4,426 ｜ P 93 +4,410 ｜ C 110 +1,479
仓位参考: Max Pain 112 ｜ Put Wall 90（-0.4%，弱）（OI 14.8k）
量化解读： 存量 Put 重｜ATM IV 97.2%｜历史 Rank 91%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 73,997 股

📆 12-04 Forward Structure
存量OI: C 20.6k / P 49.9k，今日变化ΔOI: C +3.3k / P +2.6k，平值价格ATM: C $7.40 / P $6.80 ｜ ATM IV 94.1%，净 delta 敞口 235k shares
Top ΔOI: P 160 -1,567 ｜ C 107 +775
仓位参考: Max Pain 135 ｜ Put Wall 85（-5.9%，弱）（OI 5.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 94.1%｜历史 Rank 91%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 234,642 股

📆 12-11 Forward Structure
存量OI: C 7.2k / P 35.7k，今日变化ΔOI: C +0.3k / P +4.2k，平值价格ATM: C $8.81 / P $7.97 ｜ ATM IV 92.4%，净 delta 敞口 -42k shares
Top ΔOI: P 65 +791 ｜ P 60 +709 ｜ P 55 +700
仓位参考: Max Pain 145 ｜ Put Wall 85（-5.9%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 92.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 负 41,505 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 122.2% vs 11-27 97.2%（差 +25.0pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/MSTR_evening.json