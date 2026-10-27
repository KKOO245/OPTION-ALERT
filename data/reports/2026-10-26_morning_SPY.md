# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-27 753P ΔOI +24,048（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-27 753P ΔOI +24,048 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 759.97 → 今开 759.90（-0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 763.47 ｜ 低 758.68

Options: P/C成交量 1.21 | OI比 2.31 | ATM IV 24.8% | Skew 4.4pp | Term 0.61 | ExpMove ±1.1%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价中性（Skew 4.4pp）｜当日成交偏 Put（P/C量 1.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.31×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 20% ｜ P/C OI(近端) 80%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 20%）｜近端持仓结构中性（P/C OI 分位 80%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-27（1D）±1.1% ｜ 10-28（2D）±1.4% ｜ 10-29（3D）±1.6% ｜ 10-30（4D）±1.8%
   ⇒ IV–VIX Spread: +5.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,769,096,856 | GEX Change vs 上次快照 214,210,004 | Flip: Primary Flip: 773.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3042 / LOW 549 / INVALID 1435
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.98（全链重定价，覆盖 95%）
最近结构参考: Flip 774（现价低于该位 1.5%）
量化视角： 负 Gamma（17.69亿，历史分位偏负区，比 80% 的交易日更负）｜负 Gamma 缓解（+2.14亿）｜现价位于 Flip 下方 1.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 763（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 755.0P — Vol 148,330 | 最新价 $4.53 | OI 23470→150938 (ΔOI +127468张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127468张（+543.1% vs前日OI），连续性待观察（方向未知）
10-30 745.0P — Vol 89,052 | 最新价 $2.29 | OI 81237→157799 (ΔOI +76562张) | ΔOI/Volume 86.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增76562张（+94.2% vs前日OI），连续性待观察（方向未知）
10-27 753.0P — Vol 25,511 | 最新价 $1.61 | OI 572→24620 (ΔOI +24048张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24048张（+4204.2% vs前日OI），连续性待观察（方向未知）
11-20 722.0P — Vol 41,708 | 最新价 $3.98 | OI 6260→24947 (ΔOI +18687张) | ΔOI/Volume 44.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18687张（+298.5% vs前日OI），连续性待观察（方向未知）
11-20 700.0P — Vol 40,808 | 最新价 $2.50 | OI 75322→87048 (ΔOI +11726张) | ΔOI/Volume 28.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11726张（+15.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 258,491 张（Put 258,491 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $90M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 169.5k / P 391.8k，今日成交量: C 467.8k / P 565.8k，平值价格ATM: C $2.34 / P $2.10 ｜ ATM IV 24.8%，预期波动 ±0.6%，Max Pain 763
Top ΔOI: P 739 +9,549 ｜ P 740 +9,399 ｜ P 645 +6,772

📆 Forward Expiration Structure

10-27  C +22.9k / P +30.6k ｜ Activity HIGH ｜ 1D
10-28  C +13.9k / P +14.8k ｜ Activity HIGH ｜ 2D
10-29  C +3.5k / P +40.7k ｜ Activity HIGH ｜ 3D
10-30  C +26.0k / P +192.0k ｜ Activity HIGH ｜ 4D

📆 10-27 Forward Structure
存量OI: C 83.2k / P 145.6k，今日变化ΔOI: C +22.9k / P +30.6k，平值价格ATM: C $3.32 / P $4.80 ｜ ATM IV 18.1%，净 delta 敞口 353k shares
Top ΔOI: P 753 +24,048 ｜ P 767 -7,389 ｜ C 777 +5,871
仓位参考: Max Pain 767 ｜ Call Wall 777（+1.9%）（OI 6.9k） ｜ Put Wall 753（-1.2%，弱）（OI 24.6k）
量化解读： 存量 Put 重｜ATM IV 18.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.92×（近似）｜净 delta 敞口 正 353,178 股

📆 10-28 Forward Structure
存量OI: C 61.8k / P 100.3k，今日变化ΔOI: C +13.9k / P +14.8k，平值价格ATM: C $4.61 / P $5.76 ｜ ATM IV 19.4%，净 delta 敞口 165k shares
Top ΔOI: P 734 +4,270 ｜ P 733 +2,700 ｜ P 745 +2,080
仓位参考: Max Pain 767 ｜ Call Wall 785（+3.0%，弱）（OI 3.5k） ｜ Put Wall 741（-2.8%）（OI 20.3k）
量化解读： 存量 Put 重｜ATM IV 19.4%｜历史 Rank 94%（近端代理）｜IV/RV 2.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 165,061 股

📆 10-29 Forward Structure
存量OI: C 38.0k / P 80.0k，今日变化ΔOI: C +3.5k / P +40.7k，平值价格ATM: C $5.35 / P $6.95 ｜ ATM IV 19.3%，净 delta 敞口 -128k shares
Top ΔOI: P 732 +7,481 ｜ P 729 +6,732 ｜ P 737 +5,475
仓位参考: Max Pain 766 ｜ Call Wall 763（+0.1%，弱）（OI 1.9k） ｜ Put Wall 744（-2.4%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 19.3%｜历史 Rank 94%（近端代理）｜IV/RV 2.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 127,987 股

📆 10-30 Forward Structure
存量OI: C 612.6k / P 1648.3k，今日变化ΔOI: C +26.0k / P +192.0k，平值价格ATM: C $6.35 / P $7.19 ｜ ATM IV 19.0%，净 delta 敞口 -2.7M shares
Top ΔOI: P 755 +127,468 ｜ P 745 +76,562 ｜ P 760 -42,109
仓位参考: Max Pain 765 ｜ Call Wall 780（+2.3%，弱）（OI 26.3k） ｜ Put Wall 745（-2.3%，弱）（OI 157.8k）
量化解读： 存量 Put 重｜ATM IV 19.0%｜历史 Rank 94%（近端代理）｜IV/RV 2.02×（近似）｜净 delta 敞口 负 2,718,008 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/SPY_morning.json