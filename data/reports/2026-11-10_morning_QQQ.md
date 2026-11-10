# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.27
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
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
🟡 **近现价集中开仓**: 11-11 675P ΔOI +6,036（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 679.35 → 今开 672.55（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 680.95 ｜ 低 669.92

Options: P/C成交量 0.93 | OI比 1.14 | ATM IV 38.5% | Skew 4.1pp | Term 0.64 | ExpMove ±1.5%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价中性（Skew 4.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.14×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 32% ｜ P/C OI(近端) 12%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 32%）｜近端持仓结构中性（P/C OI 分位 12%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-11（1D）±1.5% ｜ 11-12（2D）±1.9% ｜ 11-13（3D）±2.3% ｜ 11-16（6D）±2.6%
   ⇒ IV–VIX Spread: +18.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -270,449,699 | GEX Change vs 上次快照 15,711,581 | Flip: Primary Flip: 687.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3928 / LOW 303 / INVALID 1861
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 687.29（全链重定价，覆盖 99%）
Call Wall 700（弱结构｜现价低于该位 2.9%）
最近结构参考: Flip 687（现价低于该位 1.1%）
量化视角： 负 Gamma（2.70亿，历史分位 32%，中性区）｜负 Gamma 缓解（+1571万）｜现价位于 Flip 下方 1.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 675（MaxPain，仅结算参考）；上方 700（Call Wall，弱结构）。
• Gamma 区域：切换参考 687（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 570.0P — Vol 25,820 | 最新价 $0.07 | OI 1434→25953 (ΔOI +24519张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24519张（+1709.8% vs前日OI），连续性待观察（方向未知）
11-13 405.0P — Vol 20,830 | 最新价 $0.01 | OI 0→20619 (ΔOI +20619张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20619张（前日OI缺失），连续性待观察（方向未知）
11-13 660.0P — Vol 29,080 | 最新价 $2.92 | OI 7659→24570 (ΔOI +16911张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16911张（+220.8% vs前日OI），连续性待观察（方向未知）
11-20 655.0P — Vol 21,925 | 最新价 $5.61 | OI 17847→31315 (ΔOI +13468张) | ΔOI/Volume 61.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13468张（+75.5% vs前日OI），连续性待观察（方向未知）
11-13 696.0C — Vol 10,760 | 最新价 $1.85 | OI 521→10466 (ΔOI +9945张) | ΔOI/Volume 92.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9945张（+1908.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 85,462 张（Put 75,517 / Call 9,945），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $12M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 141.2k / P 160.7k，今日成交量: C 562.1k / P 522.5k，平值价格ATM: C $2.88 / P $2.79 ｜ ATM IV 38.5%，预期波动 ±0.8%，Max Pain 675
Top ΔOI: P 675 +5,895 ｜ P 535 +5,681 ｜ C 700 +5,160

📆 Forward Expiration Structure

11-11  C +16.1k / P +54.8k ｜ Activity HIGH ｜ 1D
11-12  C +6.8k / P +10.1k ｜ Activity HIGH ｜ 2D
11-13  C +38.7k / P +121.7k ｜ Activity HIGH ｜ 3D
11-16  C +13.9k / P +19.2k ｜ Activity HIGH ｜ 6D

📆 11-11 Forward Structure
存量OI: C 66.8k / P 98.7k，今日变化ΔOI: C +16.1k / P +54.8k，平值价格ATM: C $5.07 / P $4.89 ｜ ATM IV 31.1%，净 delta 敞口 -258k shares
Top ΔOI: P 675 +6,036 ｜ P 670 +5,347 ｜ P 650 +4,820
仓位参考: Max Pain 675 ｜ Call Wall 700（+2.9%，弱）（OI 3.1k） ｜ Put Wall 675（-0.7%，弱）（OI 6.7k）
量化解读： 存量 Put 重｜ATM IV 31.1%｜历史 Rank 96%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 257,656 股

📆 11-12 Forward Structure
存量OI: C 52.6k / P 41.0k，今日变化ΔOI: C +6.8k / P +10.1k，平值价格ATM: C $6.65 / P $6.43 ｜ ATM IV 30.4%，净 delta 敞口 -60k shares
Top ΔOI: C 710 +1,555 ｜ P 618 +1,014
仓位参考: Max Pain 672 ｜ Call Wall 685（+0.7%，弱）（OI 1.9k） ｜ Put Wall 670（-1.5%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.4%｜历史 Rank 96%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 59,563 股

📆 11-13 Forward Structure
存量OI: C 287.2k / P 383.4k，今日变化ΔOI: C +38.7k / P +121.7k，平值价格ATM: C $7.87 / P $7.53 ｜ ATM IV 29.8%，净 delta 敞口 -121k shares
Top ΔOI: P 570 +24,519 ｜ P 660 +16,911
仓位参考: Max Pain 685 ｜ Call Wall 700（+2.9%，弱）（OI 14.1k） ｜ Put Wall 660（-2.9%，弱）（OI 24.6k）
量化解读： 存量 Put 重｜ATM IV 29.8%｜历史 Rank 96%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 121,196 股

📆 11-16 Forward Structure
存量OI: C 40.2k / P 38.0k，今日变化ΔOI: C +13.9k / P +19.2k，平值价格ATM: C $9.20 / P $8.80 ｜ ATM IV 25.1%，净 delta 敞口 -86k shares
Top ΔOI: C 702 +1,743
仓位参考: Max Pain 677 ｜ Call Wall 700（+2.9%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 25.1%｜历史 Rank 96%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 负 85,908 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/QQQ_morning.json