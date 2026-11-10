# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $750.86 ｜ QQQ $674.76
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-11 747P ΔOI +2,763（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-12 744P ΔOI +18,981 占该期限总 OI 11.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 752.69 → 今开 747.94（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 752.14 ｜ 低 747.05

Options: P/C成交量 1.02 | OI比 1.59 | ATM IV 25.9% | Skew 2.9pp | Term 0.62 | ExpMove ±0.9%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.59×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 35% ｜ P/C OI(近端) 30%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 35%）｜近端持仓结构中性（P/C OI 分位 30%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-11（1D）±0.9% ｜ 11-12（2D）±1.2% ｜ 11-13（3D）±1.4% ｜ 11-16（6D）±1.7%
   ⇒ IV–VIX Spread: +6.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -951,277,589 | GEX Change vs 上次快照 -209,994,280 | Flip: Primary Flip: 759.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3164 / LOW 278 / INVALID 1870
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 759.16（全链重定价，覆盖 98%）
最近结构参考: Flip 759（现价低于该位 1.0%）
量化视角： 负 Gamma（9.51亿，历史分位 35%，中性区）｜负 Gamma 加深（2.10亿）｜现价位于 Flip 下方 1.01%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 749（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 759（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-10 735.0P — Vol 92,836 | 最新价 $0.19 | OI 2315→67109 (ΔOI +64794张) | ΔOI/Volume 69.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增64794张（+2798.9% vs前日OI），连续性待观察（方向未知）
11-10 710.0P — Vol 78,154 | 最新价 $0.03 | OI 818→55870 (ΔOI +55052张) | ΔOI/Volume 70.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55052张（+6730.1% vs前日OI），连续性待观察（方向未知）
11-13 580.0P — Vol 51,628 | 最新价 $0.04 | OI 2225→51770 (ΔOI +49545张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增49545张（+2226.7% vs前日OI），连续性待观察（方向未知）
11-12 744.0P — Vol 20,775 | 最新价 $2.13 | OI 207→19188 (ΔOI +18981张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18981张（+9169.6% vs前日OI），连续性待观察（方向未知）
11-10 740.0P — Vol 48,080 | 最新价 $0.40 | OI 1258→14700 (ΔOI +13442张) | ΔOI/Volume 28.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13442张（+1068.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 201,814 张（Put 201,814 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 220.1k / P 350.5k，今日成交量: C 647.2k / P 658.7k，平值价格ATM: C $2.56 / P $1.71 ｜ ATM IV 25.9%，预期波动 ±0.6%，Max Pain 749
Top ΔOI: P 735 +64,794 ｜ P 710 +55,052 ｜ P 740 +13,442

📆 Forward Expiration Structure

11-11  C +14.8k / P +34.1k ｜ Activity HIGH ｜ 1D
11-12  C +11.3k / P +37.8k ｜ Activity HIGH ｜ 2D
11-13  C +32.0k / P +12.6k ｜ Activity HIGH ｜ 3D
11-16  C +19.8k / P +23.1k ｜ Activity HIGH ｜ 6D

📆 11-11 Forward Structure
存量OI: C 91.1k / P 114.5k，今日变化ΔOI: C +14.8k / P +34.1k，平值价格ATM: C $3.90 / P $3.17 ｜ ATM IV 19.8%，净 delta 敞口 -534k shares
Top ΔOI: P 747 +2,763 ｜ P 740 +2,696 ｜ P 753 +2,528
仓位参考: Max Pain 750 ｜ Call Wall 770（+2.5%，弱）（OI 7.2k） ｜ Put Wall 740（-1.5%，弱）（OI 5.4k）
量化解读： 存量 Put 重｜ATM IV 19.8%｜历史 Rank 94%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 534,180 股

📆 11-12 Forward Structure
存量OI: C 66.7k / P 96.2k，今日变化ΔOI: C +11.3k / P +37.8k，平值价格ATM: C $5.00 / P $4.07 ｜ ATM IV 19.1%，净 delta 敞口 -825k shares
Top ΔOI: P 744 +18,981 ｜ P 730 +7,285 ｜ C 789 +1,973
仓位参考: Max Pain 750 ｜ Call Wall 770（+2.5%，弱）（OI 2.8k） ｜ Put Wall 744（-1.0%）（OI 19.2k）
量化解读： 存量 Put 重｜ATM IV 19.1%｜历史 Rank 94%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 824,613 股

📆 11-13 Forward Structure
存量OI: C 316.7k / P 500.9k，今日变化ΔOI: C +32.0k / P +12.6k，平值价格ATM: C $5.94 / P $4.86 ｜ ATM IV 18.9%，净 delta 敞口 -567k shares
Top ΔOI: P 580 +49,545 ｜ P 715 -47,746 ｜ P 730 -43,226
仓位参考: Max Pain 753 ｜ Call Wall 760（+1.1%，弱）（OI 13.3k） ｜ Put Wall 745（-0.9%，弱）（OI 29.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 18.9%｜历史 Rank 94%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 567,355 股

📆 11-16 Forward Structure
存量OI: C 64.6k / P 65.4k，今日变化ΔOI: C +19.8k / P +23.1k，平值价格ATM: C $6.70 / P $5.80 ｜ ATM IV 15.7%，净 delta 敞口 -94k shares
Top ΔOI: C 794 +2,992 ｜ C 770 +2,777 ｜ C 795 +2,555
仓位参考: Max Pain 750 ｜ Call Wall 770（+2.5%）（OI 6.5k） ｜ Put Wall 740（-1.5%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 15.7%｜历史 Rank 94%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 负 94,295 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SPY_morning.json