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
🟡 **近现价集中开仓**: 11-19 632P ΔOI +2,511（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 661.07 → 收盘 659.51（-0.2%） ｜ 今日高 662.80 ｜ 低 653.08 ｜ 昨收 656.95 → 收盘 659.51（+0.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 1.06 | OI比 1.29 | ATM IV 33.1% | Skew 3.0pp | Term 0.88 | ExpMove ±1.8%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 23% ｜ P/C OI(近端) 21%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 23%）｜近端持仓结构中性（P/C OI 分位 21%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-19（1D）±1.8% ｜ 11-20（2D）±2.5% ｜ 11-23（5D）±3.1% ｜ 11-24（6D）±3.5%
   ⇒ IV–VIX Spread: +8.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -425,838,245 | GEX Change vs 上次快照 -51,315,491 | Flip: Primary Flip: 676.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3262 / LOW 445 / INVALID 1447
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 676.02（全链重定价，覆盖 96%）
最近结构参考: Flip 676（现价低于该位 2.4%）
量化视角： 负 Gamma（4.26亿，历史分位偏负区，比 77% 的交易日更负）｜负 Gamma 加深（5132万）｜现价位于 Flip 下方 2.44%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 660（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 676（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-19  C +19.6k / P +13.5k ｜ Activity HIGH ｜ 1D
11-20  C +101.6k / P +58.3k ｜ Activity HIGH ｜ 2D
11-23  C +6.9k / P +10.6k ｜ Activity HIGH ｜ 5D
11-24  C +13.3k / P +1.3k ｜ Activity HIGH ｜ 6D

📆 11-19 Forward Structure
存量OI: C 59.3k / P 73.5k，今日变化ΔOI: C +19.6k / P +13.5k，平值价格ATM: C $5.83 / P $6.31 ｜ ATM IV 43.3%，净 delta 敞口 288k shares
Top ΔOI: P 632 +2,511 ｜ C 680 +2,137 ｜ P 607 +1,042
仓位参考: Max Pain 666 ｜ Put Wall 664（+0.7%，弱）（OI 5.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.3%｜历史 Rank 91%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 288,309 股

📆 11-20 Forward Structure
存量OI: C 1214.8k / P 1103.9k，今日变化ΔOI: C +101.6k / P +58.3k，平值价格ATM: C $8.35 / P $8.48 ｜ ATM IV 43.0%，净 delta 敞口 3.7M shares
Top ΔOI: P 592 +21,611 ｜ C 679 +19,557 ｜ C 665 +10,917
仓位参考: Max Pain 685 ｜ Call Wall 670（+1.6%，弱）（OI 22.6k） ｜ Put Wall 640（-3.0%，弱）（OI 44.7k）
量化解读： 存量两侧均衡｜ATM IV 43.0%｜历史 Rank 91%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,743,282 股

📆 11-23 Forward Structure
存量OI: C 43.5k / P 36.9k，今日变化ΔOI: C +6.9k / P +10.6k，平值价格ATM: C $10.30 / P $10.47 ｜ ATM IV 33.7%，净 delta 敞口 -28k shares
Top ΔOI: P 645 +4,279
仓位参考: Max Pain 670 ｜ Put Wall 645（-2.2%）（OI 5.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.7%｜历史 Rank 91%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 负 28,338 股

📆 11-24 Forward Structure
存量OI: C 28.7k / P 28.4k，今日变化ΔOI: C +13.3k / P +1.3k，平值价格ATM: C $11.57 / P $11.85 ｜ ATM IV 34.2%，净 delta 敞口 273k shares
Top ΔOI: C 685 +3,705 ｜ C 695 +3,035 ｜ P 660 -1,760
仓位参考: Max Pain 670 ｜ Put Wall 660（+0.1%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜ATM IV 34.2%｜历史 Rank 91%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 272,536 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/QQQ_evening.json