# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-22 736C ΔOI +16,949（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-27 740C ΔOI +9,796 占该期限总 OI 14.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 722.22 → 收盘 725.20（+0.4%） ｜ 今日高 727.95 ｜ 低 719.72 ｜ 昨收 717.63 → 收盘 725.20（+1.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.95 | OI比 1.71 | ATM IV 46.8% | Skew -0.5pp | Term 0.46 | ExpMove ±1.0%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.46，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.71×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 30% ｜ P/C OI(近端) 57%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 30%）｜近端持仓结构中性（P/C OI 分位 57%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-22（1D）±1.0% ｜ 10-23（2D）±1.4% ｜ 10-26（5D）±1.8% ｜ 10-27（6D）±2.0%
   ⇒ IV–VIX Spread: +30.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -298,502,710 | GEX Change vs 上次快照 100,517,381 | Flip: Primary Flip: 730.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3128 / LOW 419 / INVALID 1731
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 730.03（全链重定价，覆盖 96%）
最近结构参考: Flip 730（现价低于该位 0.7%）
量化视角： 负 Gamma（2.99亿，历史分位 30%，中性区）｜负 Gamma 缓解（+1.01亿）｜现价位于 Flip 下方 0.66%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 719（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 730（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-22  C +57.8k / P +50.4k ｜ Activity HIGH ｜ 1D
10-23  C +17.6k / P +13.9k ｜ Activity HIGH ｜ 2D
10-26  C +8.0k / P +14.0k ｜ Activity HIGH ｜ 5D
10-27  C +13.3k / P +10.1k ｜ Activity HIGH ｜ 6D

📆 10-22 Forward Structure
存量OI: C 93.3k / P 113.3k，今日变化ΔOI: C +57.8k / P +50.4k，平值价格ATM: C $3.24 / P $3.73 ｜ ATM IV 22.8%，净 delta 敞口 1.4M shares
Top ΔOI: C 736 +16,949 ｜ C 733 +15,195
仓位参考: Max Pain 720 ｜ Call Wall 736（+1.5%，弱）（OI 17.3k） ｜ Put Wall 708（-2.4%，弱）（OI 10.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 22.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,417,162 股

📆 10-23 Forward Structure
存量OI: C 276.2k / P 420.7k，今日变化ΔOI: C +17.6k / P +13.9k，平值价格ATM: C $4.85 / P $5.10 ｜ ATM IV 23.0%，净 delta 敞口 683k shares
Top ΔOI: P 710 +5,637 ｜ P 720 -4,104 ｜ C 720 +3,290
仓位参考: Max Pain 725 ｜ Call Wall 735（+1.4%）（OI 25.6k） ｜ Put Wall 710（-2.1%，弱）（OI 45.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 23.0%｜历史 Rank 99%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 682,571 股

📆 10-26 Forward Structure
存量OI: C 34.0k / P 57.5k，今日变化ΔOI: C +8.0k / P +14.0k，平值价格ATM: C $6.30 / P $6.42 ｜ ATM IV 18.9%，净 delta 敞口 61k shares
Top ΔOI: C 762 +2,126
仓位参考: Max Pain 725 ｜ Call Wall 740（+2.0%，弱）（OI 1.2k） ｜ Put Wall 720（-0.7%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 18.9%｜历史 Rank 99%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 正 61,258 股

📆 10-27 Forward Structure
存量OI: C 27.6k / P 38.3k，今日变化ΔOI: C +13.3k / P +10.1k，平值价格ATM: C $7.57 / P $7.31 ｜ ATM IV 19.7%，净 delta 敞口 37k shares
Top ΔOI: C 740 +9,796 ｜ P 729 +1,689 ｜ P 722 +1,675
仓位参考: Max Pain 728 ｜ Call Wall 740（+2.0%）（OI 10.4k） ｜ Put Wall 722（-0.4%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 19.7%｜历史 Rank 99%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 正 36,800 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/QQQ_evening.json