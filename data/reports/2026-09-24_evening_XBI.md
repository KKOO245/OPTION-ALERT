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
🟡 **近现价集中开仓**: 09-25 154P ΔOI +2,703（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 148P ΔOI +9,985 占该期限总 OI 45.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 154.83 → 收盘 156.05（+0.8%） ｜ 今日高 156.79 ｜ 低 152.57 ｜ 昨收 155.20 → 收盘 156.05（+0.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-29，窗口结束前不做对错判定）

Options: P/C成交量 1.67 | OI比 3.27 | ATM IV 37.0% | Skew 5.5pp | Term 0.87 | ExpMove ±2.3%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 5.5pp）｜当日成交偏 Put（P/C量 1.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.67×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±2.3% ｜ 10-02（8D）±3.5% ｜ 10-09（15D）±4.6% ｜ 10-16（22D）±6.7%
   ⇒ IV–VIX Spread: +21.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -47,679,064 | GEX Change vs 上次快照 -44,914,217 | Flip: Primary Flip: 163.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 346 / LOW 103 / INVALID 331
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.71（全链重定价，覆盖 92%）
Put Wall 150（现价高于该位 4.0%）
最近结构参考: Put Wall 150（现价高于该位 4.0%）
量化视角： 负 Gamma（4768万，无历史分位）｜负 Gamma 加深（4491万）｜现价位于 Flip 下方 4.68%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +1.9k / P +1.6k ｜ Activity HIGH ｜ 1D
10-02  C +1.4k / P +16.7k ｜ Activity HIGH ｜ 8D
10-09  C +0.2k / P +1.5k ｜ Activity HIGH ｜ 15D
10-16  C +2.2k / P +8.4k ｜ Activity MEDIUM △ ｜ 22D

📆 09-25 Forward Structure
存量OI: C 13.8k / P 45.0k，今日变化ΔOI: C +1.9k / P +1.6k，平值价格ATM: C $1.04 / P $2.57 ｜ ATM IV 37.0%，净 delta 敞口 -62k shares
Top ΔOI: P 154 +2,703 ｜ P 150 -1,438 ｜ P 160 +1,396
仓位参考: Max Pain 157 ｜ Call Wall 160（+2.5%，弱）（OI 2.7k） ｜ Put Wall 150（-3.9%，弱）（OI 12.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.0%｜历史 Rank 71%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 62,233 股

📆 10-02 Forward Structure
存量OI: C 3.5k / P 18.4k，今日变化ΔOI: C +1.4k / P +16.7k，平值价格ATM: C $2.34 / P $3.05 ｜ ATM IV 32.8%，净 delta 敞口 -287k shares
Top ΔOI: P 148 +9,985 ｜ P 155 +3,081 ｜ P 145 +2,991
仓位参考: Max Pain 158 ｜ Call Wall 165（+5.7%，弱）（OI 1.0k） ｜ Put Wall 148（-5.2%）（OI 10.0k）
量化解读： 存量 Put 重｜ATM IV 32.8%｜历史 Rank 71%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 287,353 股

📆 10-09 Forward Structure
存量OI: C 0.5k / P 3.0k，今日变化ΔOI: C +0.2k / P +1.5k，平值价格ATM: C $3.40 / P $3.77 ｜ ATM IV 31.4%，净 delta 敞口 -13k shares
Top ΔOI: P 145 +944 ｜ P 146 +117
仓位参考: Max Pain 158 ｜ Call Wall 158（+1.2%，弱）（OI 55） ｜ Put Wall 150（-3.9%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 31.4%｜历史 Rank 71%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 负 13,315 股

10-16（MEDIUM △）Top ΔOI: 150P +2,837 ｜ 135P +2,087
10-16（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 165（+5.7%，弱）（OI 2.6k） ｜ Put Wall 150（-3.9%）（OI 20.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/XBI_evening.json