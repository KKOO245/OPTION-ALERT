# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-23（3D）ATM IV 145.9% vs 10-30 106.8%（差 +39.1pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 220.15 → 收盘 222.65（+1.1%） ｜ 今日高 228.79 ｜ 低 213.14 ｜ 昨收 226.22 → 收盘 222.65（-1.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.73 | OI比 0.86 | ATM IV 145.9% | Skew 4.0pp | Term 0.59 | ExpMove ±10.6%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±10.6% ｜ 10-30（10D）±14.2% ｜ 11-06（17D）±16.2% ｜ 11-13（24D）±19.0%
   ⇒ IV–VIX Spread: +128.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,736,816 | GEX Change vs 上次快照 1,406,843 | Flip: Primary Flip: 246.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 644 / LOW 51 / INVALID 161
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 246.97（全链重定价，覆盖 100%）
最近结构参考: Flip 247（现价低于该位 9.8%）
量化视角： 负 Gamma（674万，无历史分位）｜负 Gamma 缓解（+141万）｜现价位于 Flip 下方 9.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 245（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 247（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +9.7k / P +2.7k ｜ Activity HIGH ｜ 3D
10-30  C +1.0k / P +2.2k ｜ Activity HIGH ｜ 10D
11-06  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 17D
11-13  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 47.6k / P 40.8k，今日变化ΔOI: C +9.7k / P +2.7k，平值价格ATM: C $11.98 / P $11.65 ｜ ATM IV 145.9%，净 delta 敞口 148k shares
Top ΔOI: C 250 +770
仓位参考: Max Pain 245 ｜ Call Wall 230（+3.3%，弱）（OI 1.7k） ｜ Put Wall 230（+3.3%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 145.9%｜历史 Rank 90%（近端代理）｜IV/RV 1.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 147,795 股

📆 10-30 Forward Structure
存量OI: C 19.1k / P 24.8k，今日变化ΔOI: C +1.0k / P +2.2k，平值价格ATM: C $16.60 / P $15.05 ｜ ATM IV 106.8%，净 delta 敞口 -6k shares
Top ΔOI: P 165 +642 ｜ P 255 +251
仓位参考: Max Pain 250 ｜ Call Wall 240（+7.8%，弱）（OI 1.4k） ｜ Put Wall 240（+7.8%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 106.8%｜历史 Rank 90%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,908 股

📆 11-06 Forward Structure
存量OI: C 7.0k / P 12.0k，今日变化ΔOI: C +0.8k / P +0.2k，平值价格ATM: C $17.89 / P $18.23 ｜ ATM IV 96.6%，净 delta 敞口 7k shares
Top ΔOI: C 270 +108
仓位参考: Max Pain 260 ｜ Call Wall 240（+7.8%，弱）（OI 0.2k） ｜ Put Wall 235（+5.5%）（OI 2.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 96.6%｜历史 Rank 90%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,145 股

📆 11-13 Forward Structure
存量OI: C 4.5k / P 8.0k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $20.54 / P $21.80 ｜ ATM IV 90.2%，净 delta 敞口 7k shares
Top ΔOI: C 240 +272 ｜ P 225 +84 ｜ P 205 +30
仓位参考: Max Pain 260 ｜ Call Wall 240（+7.8%，弱）（OI 0.6k） ｜ Put Wall 230（+3.3%）（OI 2.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 90.2%｜历史 Rank 90%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 正 7,291 股

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 145.9% vs 10-30 106.8%（差 +39.1pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/BE_evening.json