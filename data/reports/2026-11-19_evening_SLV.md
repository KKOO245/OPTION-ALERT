# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $nan
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
🟡 **近现价集中开仓**: 11-23 41C ΔOI +1,320（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 46C ΔOI +8,468 占该期限总 OI 37.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 40.79 → 收盘 39.64（-2.8%） ｜ 今日高 41.10 ｜ 低 39.59 ｜ 昨收 40.70 → 收盘 39.64（-2.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 1.69 | OI比 0.21 | ATM IV 63.2% | Skew 6.4pp | Term 0.76 | ExpMove ±2.8%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 6.4pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.21）+ 当日成交偏 Put（P/C量 1.69）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.69×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.21×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±2.8% ｜ 11-23（4D）±3.8% ｜ 11-25（6D）±5.2% ｜ 11-27（8D）±5.7%
   ⇒ IV–VIX Spread: +34.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -38,848,747 | GEX Change vs 上次快照 -12,834,003 | Flip: Primary Flip: 41.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 602 / LOW 217 / INVALID 475
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 41.14（全链重定价，覆盖 94%）
Put Wall 40（现价低于该位 0.9%）
最近结构参考: Put Wall 40（现价低于该位 0.9%）
量化视角： 负 Gamma（3885万，无历史分位）｜负 Gamma 加深（1283万）｜现价位于 Flip 下方 3.64%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall） / 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 41（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +7.4k / P -26.2k ｜ Activity HIGH ｜ 1D
11-23  C +3.7k / P +1.6k ｜ Activity HIGH ｜ 4D
11-25  C +10.6k / P +3.8k ｜ Activity HIGH ｜ 6D
11-27  C +18.8k / P -65 ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 608.1k / P 128.8k，今日变化ΔOI: C +7.4k / P -26.2k，平值价格ATM: C $0.62 / P $0.48 ｜ ATM IV 63.2%，净 delta 敞口 3.2M shares
Top ΔOI: P 49 -10,339 ｜ P 50 -6,683 ｜ P 48 -4,492
仓位参考: Max Pain 45 ｜ Put Wall 40（+0.9%，弱）（OI 19.2k）
量化解读： 存量 Call 重｜ATM IV 63.2%｜历史 Rank 92%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,242,755 股

📆 11-23 Forward Structure
存量OI: C 19.6k / P 6.5k，今日变化ΔOI: C +3.7k / P +1.6k，平值价格ATM: C $0.82 / P $0.68 ｜ ATM IV 45.8%，净 delta 敞口 13k shares
Top ΔOI: C 41 +1,320 ｜ C 41 +1,156 ｜ P 40 +850
仓位参考: Max Pain 42 ｜ Call Wall 41（+3.4%，弱）（OI 1.4k） ｜ Put Wall 40（+0.9%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 45.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.06×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 12,900 股

📆 11-25 Forward Structure
存量OI: C 15.6k / P 7.1k，今日变化ΔOI: C +10.6k / P +3.8k，平值价格ATM: C $1.15 / P $0.93 ｜ ATM IV 50.3%，净 delta 敞口 -99k shares
Top ΔOI: P 39 +2,452
仓位参考: Max Pain 42 ｜ Put Wall 39（-1.6%）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 50.3%｜历史 Rank 92%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 99,041 股

📆 11-27 Forward Structure
存量OI: C 87.9k / P 30.6k，今日变化ΔOI: C +18.8k / P -65，平值价格ATM: C $1.24 / P $1.00 ｜ ATM IV 49.0%，净 delta 敞口 335k shares
Top ΔOI: C 41 +2,349
仓位参考: Max Pain 44 ｜ Call Wall 41.5（+4.7%，弱）（OI 2.4k） ｜ Put Wall 40（+0.9%）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 49.0%｜历史 Rank 92%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 正 335,148 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SLV_evening.json