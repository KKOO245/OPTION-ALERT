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
🟡 **近现价集中开仓**: 10-29 748P ΔOI -3,882（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 771.43 → 收盘 772.31（+0.1%） ｜ 今日高 773.35 ｜ 低 769.25 ｜ 昨收 769.66 → 收盘 772.31（+0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 1.00 | OI比 1.35 | ATM IV 35.9% | Skew 0.2pp | Term 0.38 | ExpMove ±0.7%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.38，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.35×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 52% ｜ P/C OI(近端) 14%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 52%）｜近端持仓结构中性（P/C OI 分位 14%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-29（1D）±0.7% ｜ 10-30（2D）±0.9% ｜ 11-02（5D）±1.1% ｜ 11-03（6D）±1.2%
   ⇒ IV–VIX Spread: +19.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -176,502,058 | GEX Change vs 上次快照 259,401,351 | Flip: Primary Flip: 773.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 2784 / LOW 434 / INVALID 1340
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.59（全链重定价，覆盖 92%）
最近结构参考: Flip 774（现价低于该位 0.2%）
量化视角： 负 Gamma（1.77亿，历史分位 52%，中性区）｜负 Gamma 缓解（+2.59亿）｜现价位于 Flip 下方 0.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 768（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-29  C +14.3k / P +10.1k ｜ Activity HIGH ｜ 1D
10-30  C +27.2k / P +32.8k ｜ Activity MEDIUM △ ｜ 2D
11-02  C +2.7k / P +10.7k ｜ Activity HIGH ｜ 5D
11-03  C +3.8k / P +10.5k ｜ Activity HIGH ｜ 6D

📆 10-29 Forward Structure
存量OI: C 57.9k / P 130.9k，今日变化ΔOI: C +14.3k / P +10.1k，平值价格ATM: C $2.61 / P $2.67 ｜ ATM IV 16.3%，净 delta 敞口 37k shares
Top ΔOI: P 748 -3,882 ｜ C 790 +1,820 ｜ P 770 +1,764
仓位参考: Max Pain 768 ｜ Call Wall 790（+2.3%）（OI 4.8k） ｜ Put Wall 758（-1.9%，弱）（OI 16.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.3%｜历史 Rank 99%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,403 股

10-30（MEDIUM △）Top ΔOI: 755P -55,762 ｜ 745P -43,733
10-30（MEDIUM △）仓位参考: Max Pain 765 ｜ Call Wall 780（+1.0%，弱）（OI 29.1k） ｜ Put Wall 750（-2.9%，弱）（OI 68.6k）

📆 11-02 Forward Structure
存量OI: C 30.3k / P 51.7k，今日变化ΔOI: C +2.7k / P +10.7k，平值价格ATM: C $4.38 / P $4.04 ｜ ATM IV 11.7%，净 delta 敞口 -61k shares
Top ΔOI: P 750 +2,477 ｜ P 705 +1,373 ｜ C 802 +895
仓位参考: Max Pain 767 ｜ Call Wall 775（+0.3%，弱）（OI 1.4k） ｜ Put Wall 750（-2.9%）（OI 7.3k）
量化解读： 存量 Put 重｜ATM IV 11.7%｜历史 Rank 99%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 负 61,206 股

📆 11-03 Forward Structure
存量OI: C 17.1k / P 30.5k，今日变化ΔOI: C +3.8k / P +10.5k，平值价格ATM: C $5.00 / P $4.65 ｜ ATM IV 12.0%，净 delta 敞口 -55k shares
Top ΔOI: P 715 +943 ｜ P 760 +811 ｜ P 741 +806
仓位参考: Max Pain 768 ｜ Call Wall 770（-0.3%，弱）（OI 0.9k） ｜ Put Wall 755（-2.2%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 12.0%｜历史 Rank 99%（近端代理）｜IV/RV 1.33×（近似）｜净 delta 敞口 负 55,347 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SPY_evening.json