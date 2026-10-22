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
🟡 **近现价集中开仓**: 10-23 769P ΔOI -6,478（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-27 767P ΔOI +36,716 占该期限总 OI 23.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 766.37 → 收盘 763.96（-0.3%） ｜ 今日高 767.71 ｜ 低 761.17 ｜ 昨收 773.09 → 收盘 763.96（-1.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-29，窗口结束前不做对错判定）

Options: P/C成交量 1.15 | OI比 1.09 | ATM IV 24.5% | Skew 0.4pp | Term 0.61 | ExpMove ±0.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜当日成交偏 Put（P/C量 1.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 22% ｜ P/C OI(近端) 4%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 22%）｜近端持仓极端 Call 重（P/C OI 分位 4%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-23（1D）±0.8% ｜ 10-26（4D）±1.1% ｜ 10-27（5D）±1.3% ｜ 10-28（6D）±1.6%
   ⇒ IV–VIX Spread: +5.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,617,041,885 | GEX Change vs 上次快照 -326,796,665 | Flip: Primary Flip: 775.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 3090 / LOW 401 / INVALID 1807
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 775.06（全链重定价，覆盖 93%）
最近结构参考: Flip 775（现价低于该位 1.4%）
量化视角： 负 Gamma（16.17亿，历史分位偏负区，比 78% 的交易日更负）｜负 Gamma 加深（3.27亿）｜现价位于 Flip 下方 1.43%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 771（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +12.0k / P -5.8k ｜ Activity MEDIUM △ ｜ 1D
10-26  C +5.8k / P +20.4k ｜ Activity HIGH ｜ 4D
10-27  C +9.3k / P +60.4k ｜ Activity HIGH ｜ 5D
10-28  C +4.2k / P +13.5k ｜ Activity HIGH ｜ 6D

📆 10-23 Forward Structure
存量OI: C 339.8k / P 568.5k，今日变化ΔOI: C +12.0k / P -5.8k，平值价格ATM: C $3.01 / P $2.71 ｜ ATM IV 17.8%，净 delta 敞口 -354k shares
Top ΔOI: P 769 -6,478 ｜ P 774 +4,911 ｜ C 780 +4,046
仓位参考: Max Pain 770 ｜ Call Wall 780（+2.1%，弱）（OI 24.5k） ｜ Put Wall 745（-2.5%，弱）（OI 37.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 17.8%｜历史 Rank 94%（近端代理）｜IV/RV 2.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 354,191 股

📆 10-26 Forward Structure
存量OI: C 75.4k / P 127.5k，今日变化ΔOI: C +5.8k / P +20.4k，平值价格ATM: C $4.36 / P $3.98 ｜ ATM IV 13.0%，净 delta 敞口 -707k shares
Top ΔOI: P 766 +5,005 ｜ P 757 +2,368 ｜ P 767 +1,981
仓位参考: Max Pain 769 ｜ Call Wall 780（+2.1%，弱）（OI 3.6k） ｜ Put Wall 766（+0.3%，弱）（OI 25.1k）
量化解读： 存量 Put 重｜ATM IV 13.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.59×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 707,438 股

📆 10-27 Forward Structure
存量OI: C 50.8k / P 103.4k，今日变化ΔOI: C +9.3k / P +60.4k，平值价格ATM: C $5.16 / P $4.66 ｜ ATM IV 13.6%，净 delta 敞口 -2.4M shares
Top ΔOI: P 767 +36,716
仓位参考: Max Pain 769 ｜ Call Wall 785（+2.8%，弱）（OI 1.8k） ｜ Put Wall 767（+0.4%）（OI 37.2k）
量化解读： 存量 Put 重｜ATM IV 13.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,386,581 股

📆 10-28 Forward Structure
存量OI: C 37.7k / P 59.0k，今日变化ΔOI: C +4.2k / P +13.5k，平值价格ATM: C $6.25 / P $5.71 ｜ ATM IV 15.2%，净 delta 敞口 -285k shares
Top ΔOI: P 760 +2,257 ｜ P 740 +1,934 ｜ P 715 +1,000
仓位参考: Max Pain 770 ｜ Call Wall 785（+2.8%，弱）（OI 2.6k） ｜ Put Wall 760（-0.5%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 15.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.87×（近似）｜净 delta 敞口 负 284,560 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/SPY_evening.json