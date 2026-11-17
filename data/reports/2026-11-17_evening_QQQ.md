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
🟡 **近现价集中开仓**: 11-18 630P ΔOI +3,826（距现价 -4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 663.05 → 收盘 656.95（-0.9%） ｜ 今日高 663.36 ｜ 低 646.65 ｜ 昨收 661.75 → 收盘 656.95（-0.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 1.25 | OI比 1.40 | ATM IV 119.0% | Skew 7.1pp | Term 0.26 | ExpMove ±1.9%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.26，近月 IV 高于远月）｜保护溢价显著（Skew 7.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 18% ｜ P/C OI(近端) 28%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 18%）｜近端持仓结构中性（P/C OI 分位 28%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-18（1D）±1.9% ｜ 11-19（2D）±2.8% ｜ 11-20（3D）±3.4% ｜ 11-23（6D）±3.8%
   ⇒ IV–VIX Spread: +93.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -553,872,415 | GEX Change vs 上次快照 26,606,450 | Flip: Primary Flip: 679.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3196 / LOW 484 / INVALID 1500
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 679.97（全链重定价，覆盖 95%）
最近结构参考: Flip 680（现价低于该位 3.4%）
量化视角： 负 Gamma（5.54亿，历史分位偏负区，比 82% 的交易日更负）｜负 Gamma 缓解（+2661万）｜现价位于 Flip 下方 3.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 669（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 680（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +19.7k / P +19.0k ｜ Activity HIGH ｜ 1D
11-19  C +8.5k / P +5.0k ｜ Activity HIGH ｜ 2D
11-20  C +58.2k / P +13.3k ｜ Activity HIGH ｜ 3D
11-23  C +7.9k / P +6.9k ｜ Activity HIGH ｜ 6D

📆 11-18 Forward Structure
存量OI: C 57.1k / P 97.7k，今日变化ΔOI: C +19.7k / P +19.0k，平值价格ATM: C $6.40 / P $6.18 ｜ ATM IV 44.8%，净 delta 敞口 -265k shares
Top ΔOI: P 630 +3,826 ｜ P 660 +2,729 ｜ C 680 +1,690
仓位参考: Max Pain 671 ｜ Call Wall 670（+2.0%，弱）（OI 1.6k） ｜ Put Wall 650（-1.1%，弱）（OI 7.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 264,724 股

📆 11-19 Forward Structure
存量OI: C 39.7k / P 60.0k，今日变化ΔOI: C +8.5k / P +5.0k，平值价格ATM: C $9.10 / P $8.99 ｜ ATM IV 46.6%，净 delta 敞口 -9k shares
Top ΔOI: C 690 +1,074 ｜ C 682 +639
仓位参考: Max Pain 675 ｜ Put Wall 664（+1.1%，弱）（OI 5.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,605 股

📆 11-20 Forward Structure
存量OI: C 1113.2k / P 1045.7k，今日变化ΔOI: C +58.2k / P +13.3k，平值价格ATM: C $11.31 / P $10.71 ｜ ATM IV 45.5%，净 delta 敞口 4.9M shares
Top ΔOI: P 577 +24,609 ｜ P 720 -12,787 ｜ C 694 +10,146
仓位参考: Max Pain 690 ｜ Call Wall 670（+2.0%，弱）（OI 19.6k） ｜ Put Wall 650（-1.1%，弱）（OI 48.0k）
量化解读： 存量两侧均衡｜ATM IV 45.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,856,187 股

📆 11-23 Forward Structure
存量OI: C 36.6k / P 26.3k，今日变化ΔOI: C +7.9k / P +6.9k，平值价格ATM: C $13.62 / P $11.52 ｜ ATM IV 36.8%，净 delta 敞口 -11k shares
Top ΔOI: C 666 +1,365 ｜ P 645 +942 ｜ P 620 +586
仓位参考: Max Pain 675 ｜ Put Wall 645（-1.8%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 36.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 11,356 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/QQQ_evening.json