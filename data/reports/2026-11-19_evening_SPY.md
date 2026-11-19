# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $645.04
VIX 28.44 ↑15.8%（5D +52.1%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-23 709P ΔOI +7,967（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 737.46 → 收盘 715.87（-2.9%） ｜ 今日高 739.90 ｜ 低 715.65 ｜ 昨收 730.20 → 收盘 715.87（-2.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 1.21 | OI比 1.15 | ATM IV 41.6% | Skew 1.9pp | Term 0.56 | ExpMove ±1.4%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜当日成交偏 Put（P/C量 1.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 14% ｜ P/C OI(近端) 5%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 14%）｜近端持仓极端 Call 重（P/C OI 分位 5%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-20（1D）±1.4% ｜ 11-23（4D）±2.0% ｜ 11-24（5D）±2.4% ｜ 11-25（6D）±2.8%
   ⇒ IV–VIX Spread: +13.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,179,185,953 | GEX Change vs 上次快照 -824,021,234 | Flip: Primary Flip: 744.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 2930 / LOW 303 / INVALID 1703
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 744.07（全链重定价，覆盖 92%）
最近结构参考: Flip 744（现价低于该位 3.8%）
量化视角： 负 Gamma（21.79亿，历史分位偏负区，比 86% 的交易日更负）｜负 Gamma 加深（8.24亿）｜现价位于 Flip 下方 3.79%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 733（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 744（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +49.1k / P -90.4k ｜ Activity MEDIUM △ ｜ 1D
11-23  C +24.1k / P +14.0k ｜ Activity HIGH ｜ 4D
11-24  C +15.6k / P +10.7k ｜ Activity HIGH ｜ 5D
11-25  C +11.9k / P +8.6k ｜ Activity HIGH ｜ 6D

📆 11-20 Forward Structure
存量OI: C 1035.2k / P 2849.2k，今日变化ΔOI: C +49.1k / P -90.4k，平值价格ATM: C $5.36 / P $4.82 ｜ ATM IV 33.8%，净 delta 敞口 10.5M shares
Top ΔOI: P 757 -19,395 ｜ P 760 -13,991 ｜ P 755 -12,809
仓位参考: Max Pain 745 ｜ Put Wall 725（+1.3%，弱）（OI 71.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,486,793 股

📆 11-23 Forward Structure
存量OI: C 93.1k / P 71.0k，今日变化ΔOI: C +24.1k / P +14.0k，平值价格ATM: C $7.71 / P $6.94 ｜ ATM IV 24.5%，净 delta 敞口 -316k shares
Top ΔOI: P 709 +7,967 ｜ C 750 +3,272
仓位参考: Max Pain 738 ｜ Call Wall 735（+2.7%，弱）（OI 1.8k） ｜ Put Wall 709（-1.0%）（OI 8.3k）
量化解读： 存量 Call 重｜ATM IV 24.5%｜历史 Rank 99%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 316,182 股

📆 11-24 Forward Structure
存量OI: C 52.5k / P 45.5k，今日变化ΔOI: C +15.6k / P +10.7k，平值价格ATM: C $8.93 / P $8.38 ｜ ATM IV 25.8%，净 delta 敞口 -641k shares
Top ΔOI: P 740 +6,813 ｜ C 758 +1,904 ｜ C 765 +1,004
仓位参考: Max Pain 740 ｜ Call Wall 732（+2.3%，弱）（OI 0.8k） ｜ Put Wall 725（+1.3%，弱）（OI 3.7k）
量化解读： 存量两侧均衡｜ATM IV 25.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 640,602 股

📆 11-25 Forward Structure
存量OI: C 47.9k / P 39.6k，今日变化ΔOI: C +11.9k / P +8.6k，平值价格ATM: C $10.22 / P $9.80 ｜ ATM IV 26.5%，净 delta 敞口 -183k shares
Top ΔOI: C 750 +1,029 ｜ P 670 +994 ｜ P 680 +871
仓位参考: Max Pain 740 ｜ Call Wall 731（+2.1%，弱）（OI 0.8k） ｜ Put Wall 695（-2.9%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 26.5%｜历史 Rank 99%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 183,157 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SPY_evening.json