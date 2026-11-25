# 期权晚报 2026-11-25（快照 16:40 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 735C ΔOI +13,533（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 665P ΔOI +11,509 占该期限总 OI 11.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 703.20 → 收盘 716.70（+1.9%） ｜ 今日高 718.43 ｜ 低 695.45 ｜ 昨收 718.78 → 收盘 716.70（-0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 1.08 | OI比 0.73 | ATM IV 37.7% | Skew 3.8pp | Term 0.61 | ExpMove ±1.4%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 36% ｜ P/C OI(近端) 0%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 36%）｜近端持仓极端 Call 重（P/C OI 分位 0%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-27（2D）±1.4% ｜ 11-30（5D）±2.1% ｜ 12-01（6D）±2.4% ｜ 12-02（7D）±2.7%
   ⇒ IV–VIX Spread: +9.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -863,719,809 | GEX Change vs 上次快照 401,838,816 | Flip: Primary Flip: 732.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3143 / LOW 541 / INVALID 1994
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 732.55（全链重定价，覆盖 95%）
Put Wall 700（弱结构｜现价高于该位 2.4%）
最近结构参考: Flip 733（现价低于该位 2.2%）
量化视角： 负 Gamma（8.64亿，历史分位 36%，中性区）｜负 Gamma 缓解（+4.02亿）｜现价位于 Flip 下方 2.16%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构） / 715（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 733（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +65.2k / P +16.9k ｜ Activity HIGH ｜ 2D
11-30  C +34.8k / P +36.5k ｜ Activity HIGH ｜ 5D
12-01  C +10.4k / P +16.7k ｜ Activity HIGH ｜ 6D
12-02  C +12.2k / P +29.1k ｜ Activity HIGH ｜ 7D

📆 11-27 Forward Structure
存量OI: C 477.7k / P 372.7k，今日变化ΔOI: C +65.2k / P +16.9k，平值价格ATM: C $4.90 / P $4.98 ｜ ATM IV 23.9%，净 delta 敞口 2.1M shares
Top ΔOI: C 735 +13,533 ｜ C 730 +9,991 ｜ P 657 +7,063
仓位参考: Max Pain 721 ｜ Call Wall 735（+2.6%，弱）（OI 26.4k） ｜ Put Wall 700（-2.3%，弱）（OI 35.1k）
量化解读： 存量 Call 重｜ATM IV 23.9%｜历史 Rank 98%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 正 2,055,775 股

📆 11-30 Forward Structure
存量OI: C 380.7k / P 718.1k，今日变化ΔOI: C +34.8k / P +36.5k，平值价格ATM: C $7.57 / P $7.57 ｜ ATM IV 22.4%，净 delta 敞口 1.7M shares
Top ΔOI: P 696 +10,163 ｜ P 639 +6,434 ｜ C 735 +6,425
仓位参考: Max Pain 730 ｜ Call Wall 735（+2.6%，弱）（OI 10.1k） ｜ Put Wall 700（-2.3%，弱）（OI 30.3k）
量化解读： 存量 Put 重｜ATM IV 22.4%｜历史 Rank 98%（近端代理）｜IV/RV 0.72×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,700,808 股

📆 12-01 Forward Structure
存量OI: C 62.9k / P 45.9k，今日变化ΔOI: C +10.4k / P +16.7k，平值价格ATM: C $8.71 / P $8.65 ｜ ATM IV 23.8%，净 delta 敞口 -21k shares
Top ΔOI: P 675 +3,158 ｜ P 685 +2,459 ｜ P 665 +1,571
仓位参考: Max Pain 720 ｜ Call Wall 725（+1.2%，弱）（OI 1.4k） ｜ Put Wall 703（-1.9%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 23.8%｜历史 Rank 98%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 负 20,991 股

📆 12-02 Forward Structure
存量OI: C 43.9k / P 59.3k，今日变化ΔOI: C +12.2k / P +29.1k，平值价格ATM: C $9.78 / P $9.62 ｜ ATM IV 24.5%，净 delta 敞口 -34k shares
Top ΔOI: P 665 +11,509 ｜ P 660 +5,635
仓位参考: Max Pain 715 ｜ Call Wall 717（+0.0%，弱）（OI 1.5k） ｜ Put Wall 700（-2.3%，弱）（OI 9.8k）
量化解读： 存量 Put 重｜ATM IV 24.5%｜历史 Rank 98%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 负 33,734 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SPY_evening.json