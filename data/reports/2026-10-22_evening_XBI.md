# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 148P ΔOI -243（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 152.25 → 收盘 151.64（-0.4%） ｜ 今日高 154.44 ｜ 低 149.71 ｜ 昨收 152.78 → 收盘 151.64（-0.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 3.53 | OI比 1.32 | ATM IV 50.7% | Skew 24.1pp | Term 0.62 | ExpMove ±2.4%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价显著（Skew 24.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 3.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.53×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.4% ｜ 10-30（8D）±4.5% ｜ 11-06（15D）±7.3% ｜ 11-13（22D）±3.3%
   ⇒ IV–VIX Spread: +31.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,582,017 | GEX Change vs 上次快照 -2,068,927 | Flip: Primary Flip: 159.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 347 / LOW 103 / INVALID 326
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.80（全链重定价，覆盖 87%）
最近结构参考: Flip 160（现价低于该位 5.1%）
量化视角： 负 Gamma（1658万，无历史分位）｜负 Gamma 加深（207万）｜现价位于 Flip 下方 5.11%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0.2k / P -0.5k ｜ Activity MEDIUM △ ｜ 1D
10-30  C +0.4k / P +2.5k ｜ Activity HIGH ｜ 8D
11-06  C -72 / P -0.4k ｜ Activity HIGH ｜ 15D
11-13  C +0.1k / P -0.1k ｜ Activity HIGH ｜ 22D

📆 10-23 Forward Structure
存量OI: C 17.5k / P 23.2k，今日变化ΔOI: C +0.2k / P -0.5k，平值价格ATM: C $1.11 / P $2.49 ｜ ATM IV 50.7%，净 delta 敞口 17k shares
Top ΔOI: P 150 +359 ｜ P 152 -330 ｜ P 148 -243
仓位参考: Max Pain 148 ｜ Call Wall 148（-2.4%，弱）（OI 3.0k） ｜ Put Wall 144（-5.0%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.7%｜历史 Rank 97%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,767 股

📆 10-30 Forward Structure
存量OI: C 7.2k / P 54.2k，今日变化ΔOI: C +0.4k / P +2.5k，平值价格ATM: C $2.85 / P $3.95 ｜ ATM IV 36.4%，净 delta 敞口 -100k shares
Top ΔOI: P 142 +3,281 ｜ P 140 -3,259 ｜ P 150 +2,200
仓位参考: Max Pain 152 ｜ Call Wall 155（+2.2%）（OI 1.7k） ｜ Put Wall 150（-1.1%，弱）（OI 9.5k）
量化解读： 存量 Put 重｜ATM IV 36.4%｜历史 Rank 97%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 100,049 股

📆 11-06 Forward Structure
存量OI: C 1.2k / P 2.2k，今日变化ΔOI: C -72 / P -0.4k，平值价格ATM: C $3.70 / P $7.45 ｜ ATM IV 35.2%，净 delta 敞口 2k shares
Top ΔOI: P 145 -253 ｜ C 155 -192 ｜ P 140 -180
仓位参考: Max Pain 152 ｜ Call Wall 154（+1.6%，弱）（OI 0.1k） ｜ Put Wall 151（-0.4%）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.2%｜历史 Rank 97%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,213 股

📆 11-13 Forward Structure
存量OI: C 0.6k / P 1.5k，今日变化ΔOI: C +0.1k / P -0.1k，平值价格ATM: C $0.00 / P $4.94 ｜ ATM IV 34.4%，净 delta 敞口 13k shares
Top ΔOI: C 150 +133 ｜ P 151 -31 ｜ P 159 -30
仓位参考: Max Pain 153 ｜ Call Wall 150（-1.1%）（OI 0.1k） ｜ Put Wall 153（+0.9%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.4%｜历史 Rank 97%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 13,097 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/XBI_evening.json