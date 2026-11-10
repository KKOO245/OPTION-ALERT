# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
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
🟡 **近现价集中开仓**: 11-10 640P ΔOI +4,092（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 656.10 → 今开 662.68（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 674.94 ｜ 低 662.02

Options: P/C成交量 0.74 | OI比 1.30 | ATM IV 36.7% | Skew 6.2pp | Term 0.71 | ExpMove ±1.6%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价显著（Skew 6.2pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.30×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 31% ｜ P/C OI(近端) 21%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 31%）｜近端持仓结构中性（P/C OI 分位 21%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-10（1D）±1.6% ｜ 11-11（2D）±2.1% ｜ 11-12（3D）±2.5% ｜ 11-13（4D）±2.8%
   ⇒ IV–VIX Spread: +15.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -285,571,932 | GEX Change vs 上次快照 137,483,677 | Flip: Primary Flip: 685.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 4015 / LOW 250 / INVALID 1883
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 685.17（全链重定价，覆盖 97%）
Put Wall 680（弱结构｜现价低于该位 1.0%）
最近结构参考: Put Wall 680（现价低于该位 1.0%）
量化视角： 负 Gamma（2.86亿，历史分位 31%，中性区）｜负 Gamma 缓解（+1.37亿）｜现价位于 Flip 下方 1.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 660（MaxPain，仅结算参考）；上方 680（Put Wall，弱结构）。
• Gamma 区域：切换参考 685（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-09 500.0P — Vol 24,450 | 最新价 $0.02 | OI 446→20055 (ΔOI +19609张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19609张（+4396.6% vs前日OI），连续性待观察（方向未知）
11-27 640.0P — Vol 8,803 | 最新价 $12.94 | OI 1188→9414 (ΔOI +8226张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8226张（+692.4% vs前日OI），连续性待观察（方向未知）
11-27 665.0C — Vol 8,448 | 最新价 $15.30 | OI 502→8557 (ΔOI +8055张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8055张（+1604.6% vs前日OI），连续性待观察（方向未知）
11-09 650.0P — Vol 33,556 | 最新价 $4.00 | OI 3988→11722 (ΔOI +7734张) | ΔOI/Volume 23.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7734张（+193.9% vs前日OI），连续性待观察（方向未知）
11-20 680.0C — Vol 19,400 | 最新价 $6.52 | OI 23996→31350 (ΔOI +7354张) | ΔOI/Volume 37.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7354张（+30.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 50,978 张（Put 35,569 / Call 15,409），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $14M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 152.0k / P 198.3k，今日成交量: C 558.0k / P 412.0k，平值价格ATM: C $2.49 / P $2.85 ｜ ATM IV 36.7%，预期波动 ±0.8%，Max Pain 660
Top ΔOI: P 500 +19,609 ｜ P 650 +7,734 ｜ P 655 +4,407

📆 Forward Expiration Structure

11-10  C +16.0k / P +21.6k ｜ Activity HIGH ｜ 1D
11-11  C +17.2k / P +14.0k ｜ Activity HIGH ｜ 2D
11-12  C +8.1k / P +4.9k ｜ Activity HIGH ｜ 3D
11-13  C +27.7k / P +5.3k ｜ Activity HIGH ｜ 4D

📆 11-10 Forward Structure
存量OI: C 75.1k / P 49.7k，今日变化ΔOI: C +16.0k / P +21.6k，平值价格ATM: C $5.28 / P $5.64 ｜ ATM IV 34.7%，净 delta 敞口 403k shares
Top ΔOI: P 640 +4,092 ｜ C 678 +3,122 ｜ P 660 +2,424
仓位参考: Max Pain 667 ｜ Call Wall 672（-0.1%，弱）（OI 3.7k） ｜ Put Wall 660（-1.9%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.7%｜历史 Rank 94%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 402,972 股

📆 11-11 Forward Structure
存量OI: C 50.6k / P 43.9k，今日变化ΔOI: C +17.2k / P +14.0k，平值价格ATM: C $7.05 / P $7.27 ｜ ATM IV 33.6%，净 delta 敞口 529k shares
Top ΔOI: C 660 +2,196 ｜ P 621 +2,136 ｜ C 656 +1,022
仓位参考: Max Pain 668 ｜ Call Wall 690（+2.5%，弱）（OI 2.5k） ｜ Put Wall 656（-2.5%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 33.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 528,882 股

📆 11-12 Forward Structure
存量OI: C 45.8k / P 30.9k，今日变化ΔOI: C +8.1k / P +4.9k，平值价格ATM: C $8.24 / P $8.68 ｜ ATM IV 32.8%，净 delta 敞口 71k shares
Top ΔOI: C 685 -1,654 ｜ C 695 -1,302 ｜ C 693 +1,254
仓位参考: Max Pain 666 ｜ Call Wall 690（+2.5%，弱）（OI 1.4k） ｜ Put Wall 660（-1.9%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 32.8%｜历史 Rank 94%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 71,259 股

📆 11-13 Forward Structure
存量OI: C 248.5k / P 261.7k，今日变化ΔOI: C +27.7k / P +5.3k，平值价格ATM: C $9.43 / P $9.44 ｜ ATM IV 32.3%，净 delta 敞口 1.3M shares
Top ΔOI: P 650 -12,138 ｜ C 700 +6,273 ｜ P 605 -6,256
仓位参考: Max Pain 685 ｜ Call Wall 675（+0.3%，弱）（OI 7.0k） ｜ Put Wall 685（+1.8%，弱）（OI 24.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 32.3%｜历史 Rank 94%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 1,295,531 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/QQQ_morning.json