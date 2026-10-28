# 期权晚报 2026-10-28（快照 16:40 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-29 288C ΔOI +13,820（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-29 288C ΔOI +13,820 占该期限总 OI 13.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 280.35 → 收盘 281.29（+0.3%） ｜ 今日高 281.47 ｜ 低 279.05 ｜ 昨收 280.18 → 收盘 281.29（+0.4%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-02，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 1.23 | ATM IV 22.2% | Skew 2.4pp | Term 0.81 | ExpMove ±0.8%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-29（1D）±0.8% ｜ 10-30（2D）±1.2% ｜ 11-02（5D）±1.5% ｜ 11-03（6D）±1.5%
   ⇒ IV–VIX Spread: +5.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,048,534 | GEX Change vs 上次快照 71,167,574 | Flip: Primary Flip: 281.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1190 / LOW 211 / INVALID 1115
结构观察区: Primary Flip 281.12（全链重定价，覆盖 96%）
Put Wall 260（弱结构｜现价高于该位 8.2%） | Call Wall 290（弱结构｜现价低于该位 3.0%）
最近结构参考: Flip 281（现价高于该位 0.1%）
量化视角： 正 Gamma（2205万，无历史分位）｜由负转正（+7117万）｜现价位于 Flip 上方 0.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 278（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-29  C +32.2k / P +8.0k ｜ Activity HIGH ｜ 1D
10-30  C -5.4k / P -6.8k ｜ Activity MEDIUM △ ｜ 2D
11-02  C +1.7k / P +1.9k ｜ Activity HIGH ｜ 5D
11-03  C +2.2k / P +3.3k ｜ Activity HIGH ｜ 6D

📆 10-29 Forward Structure
存量OI: C 80.0k / P 26.0k，今日变化ΔOI: C +32.2k / P +8.0k，平值价格ATM: C $1.46 / P $0.89 ｜ ATM IV 19.6%，净 delta 敞口 439k shares
Top ΔOI: C 288 +13,820 ｜ C 286 +9,781 ｜ C 282 +7,674
仓位参考: Max Pain 276 ｜ Call Wall 282（+0.3%，弱）（OI 18.3k） ｜ Put Wall 265（-5.8%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 19.6%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 439,164 股

10-30（MEDIUM △）Top ΔOI: 259P -10,435 ｜ 278C -7,924
10-30（MEDIUM △）仓位参考: Max Pain 278 ｜ Call Wall 278（-1.2%，弱）（OI 20.9k） ｜ Put Wall 260（-7.6%）（OI 86.1k）

📆 11-02 Forward Structure
存量OI: C 10.3k / P 10.7k，今日变化ΔOI: C +1.7k / P +1.9k，平值价格ATM: C $2.70 / P $1.62 ｜ ATM IV 15.0%，净 delta 敞口 16k shares
Top ΔOI: P 275 +998 ｜ C 284 +439 ｜ C 286 +386
仓位参考: Max Pain 276 ｜ Call Wall 287（+2.0%，弱）（OI 1.3k） ｜ Put Wall 270（-4.0%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 15.0%｜历史 Rank 60%（近端代理）｜净 delta 敞口 正 15,813 股

📆 11-03 Forward Structure
存量OI: C 7.4k / P 11.5k，今日变化ΔOI: C +2.2k / P +3.3k，平值价格ATM: C $2.41 / P $1.72 ｜ ATM IV 15.6%，净 delta 敞口 3k shares
Top ΔOI: C 282 +972 ｜ P 279 +830 ｜ P 275 +751
仓位参考: Max Pain 277 ｜ Call Wall 282（+0.3%，弱）（OI 1.2k） ｜ Put Wall 270（-4.0%）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 15.6%｜历史 Rank 60%（近端代理）｜净 delta 敞口 正 3,386 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/IWM_evening.json