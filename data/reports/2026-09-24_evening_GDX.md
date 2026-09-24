# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-25 96C ΔOI +2,264（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 80P ΔOI +2,370 占该期限总 OI 16.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 92.52 → 收盘 92.35（-0.2%） ｜ 今日高 92.64 ｜ 低 90.85 ｜ 昨收 93.56 → 收盘 92.35（-1.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-29，窗口结束前不做对错判定）

Options: P/C成交量 0.24 | OI比 0.47 | ATM IV 42.4% | Skew 4.3pp | Term 0.99 | ExpMove ±1.9%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构正常（Term 0.99）｜保护溢价中性（Skew 4.3pp）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±1.9% ｜ 10-02（8D）±5.2% ｜ 10-09（15D）±7.0% ｜ 10-16（22D）±8.0%
   ⇒ IV–VIX Spread: +26.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,234,418 | GEX Change vs 上次快照 -120,607,701 | Flip: Primary Flip: 93.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 440 / LOW 131 / INVALID 291
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 93.27（全链重定价，覆盖 88%）
Put Wall 90（弱结构｜现价高于该位 2.6%）
最近结构参考: Flip 93（现价低于该位 1.0%）
量化视角： 负 Gamma（2023万，无历史分位）｜由正转负（1.21亿）｜现价位于 Flip 下方 0.98%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构）；上方 95（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 93（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +8.4k / P +9.6k ｜ Activity HIGH ｜ 1D
10-02  C +10.3k / P +4.7k ｜ Activity HIGH ｜ 8D
10-09  C +1.3k / P +2.8k ｜ Activity HIGH ｜ 15D
10-16  C +6.7k / P +4.5k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 125.9k / P 59.7k，今日变化ΔOI: C +8.4k / P +9.6k，平值价格ATM: C $1.00 / P $0.72 ｜ ATM IV 42.4%，净 delta 敞口 19k shares
Top ΔOI: C 96 +2,264 ｜ C 99 +2,090
仓位参考: Max Pain 95 ｜ Call Wall 97（+5.0%，弱）（OI 19.8k） ｜ Put Wall 93（+0.7%，弱）（OI 7.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.4%｜历史 Rank 65%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,369 股

📆 10-02 Forward Structure
存量OI: C 33.3k / P 39.4k，今日变化ΔOI: C +10.3k / P +4.7k，平值价格ATM: C $2.25 / P $2.60 ｜ ATM IV 42.7%，净 delta 敞口 237k shares
Top ΔOI: P 90 +4,151 ｜ P 97 -3,263 ｜ C 101 +3,128
仓位参考: Max Pain 97 ｜ Call Wall 98（+6.1%，弱）（OI 2.7k） ｜ Put Wall 97（+5.0%，弱）（OI 8.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.7%｜历史 Rank 65%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 237,459 股

📆 10-09 Forward Structure
存量OI: C 5.5k / P 9.1k，今日变化ΔOI: C +1.3k / P +2.8k，平值价格ATM: C $2.94 / P $3.50 ｜ ATM IV 41.8%，净 delta 敞口 -8k shares
仓位参考: Max Pain 94 ｜ Call Wall 94（+1.8%，弱）（OI 0.7k） ｜ Put Wall 90（-2.5%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 41.8%｜历史 Rank 65%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,332 股

📆 10-16 Forward Structure
存量OI: C 91.1k / P 97.0k，今日变化ΔOI: C +6.7k / P +4.5k，平值价格ATM: C $3.65 / P $3.75 ｜ ATM IV 40.9%，净 delta 敞口 -32k shares
Top ΔOI: C 105 +2,384 ｜ P 84 +2,180
仓位参考: Max Pain 93 ｜ Call Wall 95（+2.9%，弱）（OI 6.0k） ｜ Put Wall 90（-2.5%，弱）（OI 10.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.9%｜历史 Rank 65%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 32,281 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/GDX_evening.json