# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-10 678C ΔOI +3,122（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 662.68 → 收盘 679.35（+2.5%） ｜ 今日高 681.70 ｜ 低 662.02 ｜ 昨收 656.10 → 收盘 679.35（+3.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-16，窗口结束前不做对错判定）

Options: P/C成交量 1.11 | OI比 1.30 | ATM IV 25.6% | Skew -6.0pp | Term 0.97 | ExpMove ±1.2%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -6.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 37% ｜ P/C OI(近端) 21%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 37%）｜近端持仓结构中性（P/C OI 分位 21%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-10（1D）±1.2% ｜ 11-11（2D）±1.7% ｜ 11-12（3D）±2.2% ｜ 11-13（4D）±2.5%
   ⇒ IV–VIX Spread: +5.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -203,036,728 | GEX Change vs 上次快照 82,535,204 | Flip: Primary Flip: 688.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3839 / LOW 334 / INVALID 1975
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 688.91（全链重定价，覆盖 97%）
Put Wall 680（弱结构｜现价低于该位 0.1%）
最近结构参考: Put Wall 680（现价低于该位 0.1%）
量化视角： 负 Gamma（2.03亿，历史分位 37%，中性区）｜负 Gamma 缓解（+8254万）｜现价位于 Flip 下方 1.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 660（MaxPain，仅结算参考）；上方 680（Put Wall，弱结构）。
• Gamma 区域：切换参考 689（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 640.0P — Vol 7,888 | 最新价 $4.81 | OI 1188→9414 (ΔOI +8226张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8226张（+692.4% vs前日OI），连续性待观察（方向未知）
11-27 665.0C — Vol 224 | 最新价 $26.28 | OI 502→8557 (ΔOI +8055张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8055张（+1604.6% vs前日OI），连续性待观察（方向未知）
11-20 680.0C — Vol 12,421 | 最新价 $12.96 | OI 23996→31350 (ΔOI +7354张) | ΔOI/Volume 59.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7354张（+30.6% vs前日OI），连续性待观察（方向未知）
量化视角： 3 个事件合计 ΔOI ≈ 23,635 张（Put 8,226 / Call 15,409），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-10  C +16.0k / P +21.6k ｜ Activity HIGH ｜ 1D
11-11  C +17.2k / P +14.0k ｜ Activity HIGH ｜ 2D
11-12  C +8.1k / P +4.9k ｜ Activity HIGH ｜ 3D
11-13  C +27.7k / P +5.3k ｜ Activity HIGH ｜ 4D

📆 11-10 Forward Structure
存量OI: C 75.1k / P 49.7k，今日变化ΔOI: C +16.0k / P +21.6k，平值价格ATM: C $4.18 / P $4.31 ｜ ATM IV 29.8%，净 delta 敞口 702k shares
Top ΔOI: P 640 +4,092 ｜ C 678 +3,122 ｜ P 660 +2,424
仓位参考: Max Pain 667 ｜ Call Wall 672（-1.1%，弱）（OI 3.7k） ｜ Put Wall 660（-2.8%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.8%｜历史 Rank 80%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 701,856 股

📆 11-11 Forward Structure
存量OI: C 50.6k / P 43.9k，今日变化ΔOI: C +17.2k / P +14.0k，平值价格ATM: C $5.84 / P $5.95 ｜ ATM IV 29.5%，净 delta 敞口 707k shares
Top ΔOI: C 660 +2,196 ｜ P 621 +2,136 ｜ C 656 +1,022
仓位参考: Max Pain 668 ｜ Call Wall 690（+1.6%，弱）（OI 2.5k） ｜ Put Wall 660（-2.8%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜ATM IV 29.5%｜历史 Rank 80%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 707,466 股

📆 11-12 Forward Structure
存量OI: C 45.8k / P 30.9k，今日变化ΔOI: C +8.1k / P +4.9k，平值价格ATM: C $7.60 / P $7.21 ｜ ATM IV 29.5%，净 delta 敞口 109k shares
Top ΔOI: C 685 -1,654 ｜ C 695 -1,302 ｜ C 693 +1,254
仓位参考: Max Pain 666 ｜ Call Wall 695（+2.3%，弱）（OI 1.4k） ｜ Put Wall 660（-2.8%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 29.5%｜历史 Rank 80%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 109,083 股

📆 11-13 Forward Structure
存量OI: C 248.5k / P 261.7k，今日变化ΔOI: C +27.7k / P +5.3k，平值价格ATM: C $8.53 / P $8.22 ｜ ATM IV 29.4%，净 delta 敞口 1.4M shares
Top ΔOI: P 650 -12,138 ｜ C 700 +6,273 ｜ P 605 -6,256
仓位参考: Max Pain 685 ｜ Call Wall 675（-0.6%，弱）（OI 7.0k） ｜ Put Wall 685（+0.8%，弱）（OI 24.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 29.4%｜历史 Rank 80%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 1,441,092 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/QQQ_evening.json