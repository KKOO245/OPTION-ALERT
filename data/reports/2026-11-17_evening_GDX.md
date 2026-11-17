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
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-18 80P ΔOI +1,460（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 80P ΔOI +1,460 占该期限总 OI 21.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 79.22 → 收盘 79.57（+0.4%） ｜ 今日高 81.27 ｜ 低 78.82 ｜ 昨收 78.95 → 收盘 79.57（+0.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 1.54 | OI比 1.29 | ATM IV 59.8% | Skew 11.4pp | Term 0.76 | ExpMove ±2.6%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 11.4pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.54×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-18（1D）±2.6% ｜ 11-20（3D）±3.9% ｜ 11-23（6D）±4.9% ｜ 11-25（8D）±5.5%
   ⇒ IV–VIX Spread: +34.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -48,068,704 | GEX Change vs 上次快照 -18,377,131 | Flip: Primary Flip: 82.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 556 / LOW 211 / INVALID 513
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 82.03（全链重定价，覆盖 96%）
Put Wall 75（弱结构｜现价高于该位 6.1%）
最近结构参考: Flip 82（现价低于该位 3.0%）
量化视角： 负 Gamma（4807万，无历史分位）｜负 Gamma 加深（1838万）｜现价位于 Flip 下方 3.00%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall，弱结构）；上方 80（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 82（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +1.3k / P +2.4k ｜ Activity HIGH ｜ 1D
11-20  C +2.3k / P -2.1k ｜ Activity HIGH ｜ 3D
11-23  C +0.1k / P +0.3k ｜ Activity HIGH ｜ 6D
11-25  C +0.1k / P +0.1k ｜ Activity HIGH ｜ 8D

📆 11-18 Forward Structure
存量OI: C 2.9k / P 3.8k，今日变化ΔOI: C +1.3k / P +2.4k，平值价格ATM: C $0.85 / P $1.19 ｜ ATM IV 59.8%，净 delta 敞口 -54k shares
Top ΔOI: P 80 +1,460 ｜ P 79 +632 ｜ C 80 +335
仓位参考: Max Pain 80 ｜ Call Wall 80（+0.5%，弱）（OI 0.3k） ｜ Put Wall 80（+0.5%）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 59.8%｜历史 Rank 94%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 54,484 股

📆 11-20 Forward Structure
存量OI: C 170.1k / P 181.6k，今日变化ΔOI: C +2.3k / P -2.1k，平值价格ATM: C $1.37 / P $1.71 ｜ ATM IV 53.1%，净 delta 敞口 218k shares
Top ΔOI: P 80 -1,468 ｜ P 90 -603 ｜ C 85 +419
仓位参考: Max Pain 84 ｜ Call Wall 84（+5.6%，弱）（OI 22.2k） ｜ Put Wall 80（+0.5%，弱）（OI 22.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.1%｜历史 Rank 94%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 217,532 股

📆 11-23 Forward Structure
存量OI: C 0.5k / P 0.5k，今日变化ΔOI: C +0.1k / P +0.3k，平值价格ATM: C $1.72 / P $2.19 ｜ ATM IV 45.7%，净 delta 敞口 -11k shares
Top ΔOI: P 78 +74 ｜ P 82 +65 ｜ P 79 +58
仓位参考: Max Pain 84 ｜ Put Wall 78（-2.0%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 45.7%｜历史 Rank 94%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 负 10,613 股

📆 11-25 Forward Structure
存量OI: C 0.4k / P 0.5k，今日变化ΔOI: C +0.1k / P +0.1k，平值价格ATM: C $1.95 / P $2.45 ｜ ATM IV 47.1%，净 delta 敞口 -2k shares
Top ΔOI: P 78 +68 ｜ C 85 +66 ｜ P 77 +34
仓位参考: Max Pain 83 ｜ Call Wall 83（+4.3%）（OI 0.2k） ｜ Put Wall 80（+0.5%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 47.1%｜历史 Rank 94%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 负 2,048 股

📅 事件差分（观察，非因果）: 11-18（1D）ATM IV 59.8% vs 11-20 53.1%（差 +6.7pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/GDX_evening.json