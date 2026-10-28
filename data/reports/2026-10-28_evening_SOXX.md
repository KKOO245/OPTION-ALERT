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
🟡 **近现价集中开仓**: 10-30 500C ΔOI -1,893（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 550C ΔOI +8,406 占该期限总 OI 26.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 515.71 → 收盘 521.94（+1.2%） ｜ 今日高 523.93 ｜ 低 511.66 ｜ 昨收 511.06 → 收盘 521.94（+2.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 4.68 | OI比 6.20 | ATM IV 52.0% | Skew 0.2pp | Term 0.78 | ExpMove ±3.6%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜当日成交偏 Put（P/C量 4.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.68×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 6.20×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±3.6% ｜ 11-06（9D）±7.4% ｜ 11-13（16D）±9.5% ｜ 11-20（23D）±9.9%
   ⇒ IV–VIX Spread: +35.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,542,135 | GEX Change vs 上次快照 6,021,647 | Flip: Primary Flip: 514.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 595 / LOW 280 / INVALID 717
结构观察区: Primary Flip 514.67（全链重定价，覆盖 96%）
Call Wall 550（弱结构｜现价低于该位 5.1%）
最近结构参考: Flip 515（现价高于该位 1.4%）
量化视角： 正 Gamma（854万，无历史分位）｜正 Gamma 增强（+602万）｜现价位于 Flip 上方 1.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 515（MaxPain，仅结算参考）；上方 550（Call Wall，弱结构）。
• Gamma 区域：切换参考 515（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C -1.0k / P +0.5k ｜ Activity MEDIUM △ ｜ 2D
11-06  C +15.2k / P +0.9k ｜ Activity HIGH ｜ 9D
11-13  C +1.1k / P +0.6k ｜ Activity MEDIUM △ ｜ 16D
11-20  C +4.6k / P +0.1k ｜ Activity HIGH ｜ 23D

📆 10-30 Forward Structure
存量OI: C 28.2k / P 174.7k，今日变化ΔOI: C -1.0k / P +0.5k，平值价格ATM: C $8.00 / P $10.70 ｜ ATM IV 52.0%，净 delta 敞口 -115k shares
Top ΔOI: C 500 -1,893 ｜ P 470 +1,160 ｜ C 525 -721
仓位参考: Max Pain 515 ｜ Call Wall 500（-4.2%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 52.0%｜历史 Rank 88%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 115,280 股

📆 11-06 Forward Structure
存量OI: C 22.9k / P 8.5k，今日变化ΔOI: C +15.2k / P +0.9k，平值价格ATM: C $14.00 / P $24.47 ｜ ATM IV 43.7%，净 delta 敞口 374k shares
Top ΔOI: C 550 +8,406 ｜ C 540 +6,543 ｜ P 500 +407
仓位参考: Max Pain 505 ｜ Call Wall 550（+5.4%，弱）（OI 9.0k） ｜ Put Wall 495（-5.2%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 43.7%｜历史 Rank 88%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 374,316 股

11-13（MEDIUM △）Top ΔOI: 530C +327 ｜ 500C +313
11-13（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 510（-2.3%，弱）（OI 9.6k）

📆 11-20 Forward Structure
存量OI: C 40.4k / P 64.6k，今日变化ΔOI: C +4.6k / P +0.1k，平值价格ATM: C $22.85 / P $28.70 ｜ ATM IV 42.5%，净 delta 敞口 85k shares
Top ΔOI: C 580 +2,082 ｜ C 540 +1,977 ｜ C 555 +1,277
仓位参考: Max Pain 535 ｜ Call Wall 540（+3.5%，弱）（OI 3.0k） ｜ Put Wall 490（-6.1%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.5%｜历史 Rank 88%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 84,521 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 52.0% vs 11-06 43.7%（差 +8.3pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SOXX_evening.json