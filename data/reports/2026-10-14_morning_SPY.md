# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $773.15 ｜ QQQ $736.25
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-15 795C ΔOI +15,813（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 778.01 → 今开 774.92（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 776.30 ｜ 低 772.58

Options: P/C成交量 1.20 | OI比 1.82 | ATM IV 15.6% | Skew 1.5pp | Term 0.81 | ExpMove ±0.6%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜当日成交偏 Put（P/C量 1.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.20×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.82×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 34% ｜ P/C OI(近端) 49%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 34%）｜近端持仓结构中性（P/C OI 分位 49%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-15（1D）±0.6% ｜ 10-16（2D）±0.8% ｜ 10-19（5D）±0.9% ｜ 10-20（6D）±1.0%
   ⇒ IV–VIX Spread: -0.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -961,400,277 | GEX Change vs 上次快照 -1,090,206,936 | Flip: Primary Flip: 777.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2732 / LOW 425 / INVALID 1715
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 777.36（全链重定价，覆盖 95%）
最近结构参考: Flip 777（现价低于该位 0.5%）
量化视角： 负 Gamma（9.61亿，历史分位 34%，中性区）｜由正转负（10.90亿）｜现价位于 Flip 下方 0.48%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 777（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 777（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-14 736.0P — Vol 132,099 | 最新价 $0.02 | OI 2464→51580 (ΔOI +49116张) | ΔOI/Volume 37.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增49116张（+1993.3% vs前日OI），连续性待观察（方向未知）
10-30 834.0C — Vol 29,608 | 最新价 $0.03 | OI 10319→39909 (ΔOI +29590张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29590张（+286.8% vs前日OI），连续性待观察（方向未知）
10-30 833.0C — Vol 27,362 | 最新价 $0.03 | OI 420→27341 (ΔOI +26921张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26921张（+6409.8% vs前日OI），连续性待观察（方向未知）
10-14 738.0P — Vol 30,319 | 最新价 $0.02 | OI 517→27082 (ΔOI +26565张) | ΔOI/Volume 87.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26565张（+5138.3% vs前日OI），连续性待观察（方向未知）
10-16 773.0P — Vol 29,270 | 最新价 $1.41 | OI 5755→26545 (ΔOI +20790张) | ΔOI/Volume 71.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20790张（+361.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 152,982 张（Put 96,471 / Call 56,511），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜彩票/名义 2 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 214.2k / P 390.6k，今日成交量: C 667.3k / P 832.0k，平值价格ATM: C $0.96 / P $1.73 ｜ ATM IV 15.6%，预期波动 ±0.3%，Max Pain 777
Top ΔOI: P 736 +49,116 ｜ P 738 +26,565 ｜ P 748 +11,833

📆 Forward Expiration Structure

10-15  C +32.3k / P +28.8k ｜ Activity HIGH ｜ 1D
10-16  C +16.6k / P +56.0k ｜ Activity HIGH ｜ 2D
10-19  C +6.2k / P +13.3k ｜ Activity HIGH ｜ 5D
10-20  C +6.7k / P +9.7k ｜ Activity HIGH ｜ 6D

📆 10-15 Forward Structure
存量OI: C 70.2k / P 191.1k，今日变化ΔOI: C +32.3k / P +28.8k，平值价格ATM: C $2.01 / P $2.68 ｜ ATM IV 12.8%，净 delta 敞口 -408k shares
Top ΔOI: C 795 +15,813 ｜ P 766 +3,779 ｜ P 759 +2,799
仓位参考: Max Pain 777 ｜ Call Wall 795（+2.8%）（OI 16.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.8%｜历史 Rank 68%（近端代理）｜IV/RV 1.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 407,649 股

📆 10-16 Forward Structure
存量OI: C 723.5k / P 2451.8k，今日变化ΔOI: C +16.6k / P +56.0k，平值价格ATM: C $2.85 / P $3.29 ｜ ATM IV 12.4%，净 delta 敞口 -1.6M shares
Top ΔOI: P 773 +20,790 ｜ C 782 +7,204 ｜ P 772 +5,830
仓位参考: Max Pain 772 ｜ Call Wall 785（+1.5%）（OI 59.3k）
量化解读： 存量 Put 重｜ATM IV 12.4%｜历史 Rank 68%（近端代理）｜IV/RV 1.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,648,998 股

📆 10-19 Forward Structure
存量OI: C 41.3k / P 80.4k，今日变化ΔOI: C +6.2k / P +13.3k，平值价格ATM: C $3.43 / P $3.79 ｜ ATM IV 9.7%，净 delta 敞口 -219k shares
Top ΔOI: P 750 +4,517 ｜ P 777 +1,610 ｜ C 777 +1,602
仓位参考: Max Pain 777 ｜ Call Wall 790（+2.1%，弱）（OI 4.5k） ｜ Put Wall 770（-0.5%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 9.7%｜历史 Rank 68%（近端代理）｜IV/RV 1.45×（近似）｜净 delta 敞口 负 219,371 股

📆 10-20 Forward Structure
存量OI: C 18.3k / P 28.0k，今日变化ΔOI: C +6.7k / P +9.7k，平值价格ATM: C $4.08 / P $3.87 ｜ ATM IV 9.9%，净 delta 敞口 -63k shares
Top ΔOI: C 778 +1,117 ｜ P 735 +962 ｜ P 757 +886
仓位参考: Max Pain 777 ｜ Call Wall 778（+0.6%，弱）（OI 1.5k） ｜ Put Wall 759（-1.9%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 9.9%｜历史 Rank 68%（近端代理）｜IV/RV 1.49×（近似）｜净 delta 敞口 负 62,598 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/SPY_morning.json