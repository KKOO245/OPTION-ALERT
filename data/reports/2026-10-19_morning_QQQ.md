# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-20 700P ΔOI +5,465（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-22 695P ΔOI +10,130 占该期限总 OI 13.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 709.80 → 今开 719.61（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 721.73 ｜ 低 716.57

Options: P/C成交量 1.16 | OI比 1.38 | ATM IV 28.3% | Skew 4.9pp | Term 0.76 | ExpMove ±1.1%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 4.9pp）｜当日成交偏 Put（P/C量 1.16）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 13% ｜ P/C OI(近端) 27%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 13%）｜近端持仓结构中性（P/C OI 分位 27%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-20（1D）±1.1% ｜ 10-21（2D）±1.5% ｜ 10-22（3D）±1.8% ｜ 10-23（4D）±2.1%
   ⇒ IV–VIX Spread: +9.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -691,204,972 | GEX Change vs 上次快照 247,326,807 | Flip: Primary Flip: 729.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2970 / LOW 332 / INVALID 1740
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 729.35（全链重定价，覆盖 98%）
Put Wall 700（弱结构｜现价高于该位 2.4%）
最近结构参考: Flip 729（现价低于该位 1.7%）
量化视角： 负 Gamma（6.91亿，历史分位偏负区，比 87% 的交易日更负）｜负 Gamma 缓解（+2.47亿）｜现价位于 Flip 下方 1.71%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 717（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 729（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 675.0P — Vol 59,522 | 最新价 $4.53 | OI 11732→66889 (ΔOI +55157张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55157张（+470.1% vs前日OI），连续性待观察（方向未知）
10-30 690.0P — Vol 93,485 | 最新价 $7.08 | OI 42111→69818 (ΔOI +27707张) | ΔOI/Volume 29.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27707张（+65.8% vs前日OI），连续性待观察（方向未知）
11-20 705.0P — Vol 24,282 | 最新价 $16.77 | OI 10324→34872 (ΔOI +24548张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24548张（+237.8% vs前日OI），连续性待观察（方向未知）
10-19 710.0P — Vol 65,937 | 最新价 $5.14 | OI 4209→21331 (ΔOI +17122张) | ΔOI/Volume 26.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17122张（+406.8% vs前日OI），连续性待观察（方向未知）
11-06 769.0C — Vol 15,130 | 最新价 $0.57 | OI 15342→30308 (ΔOI +14966张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14966张（+97.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 139,500 张（Put 124,534 / Call 14,966），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $95M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 201.1k / P 276.8k，今日成交量: C 358.3k / P 416.1k，平值价格ATM: C $2.28 / P $2.12 ｜ ATM IV 28.3%，预期波动 ±0.6%，Max Pain 717
Top ΔOI: P 710 +17,122 ｜ P 700 +14,112 ｜ C 730 +11,254

📆 Forward Expiration Structure

10-20  C +41.5k / P +47.1k ｜ Activity HIGH ｜ 1D
10-21  C +26.3k / P +17.3k ｜ Activity HIGH ｜ 2D
10-22  C +7.5k / P +16.4k ｜ Activity HIGH ｜ 3D
10-23  C +59.2k / P +97.6k ｜ Activity HIGH ｜ 4D

📆 10-20 Forward Structure
存量OI: C 99.2k / P 106.5k，今日变化ΔOI: C +41.5k / P +47.1k，平值价格ATM: C $4.24 / P $3.99 ｜ ATM IV 24.4%，净 delta 敞口 1.0M shares
Top ΔOI: P 700 +5,465 ｜ P 705 +4,001
仓位参考: Max Pain 719 ｜ Call Wall 733（+2.2%，弱）（OI 7.4k） ｜ Put Wall 705（-1.7%，弱）（OI 10.8k）
量化解读： 存量两侧均衡｜ATM IV 24.4%｜历史 Rank 88%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,026,716 股

📆 10-21 Forward Structure
存量OI: C 57.8k / P 56.7k，今日变化ΔOI: C +26.3k / P +17.3k，平值价格ATM: C $5.41 / P $5.31 ｜ ATM IV 24.0%，净 delta 敞口 610k shares
Top ΔOI: P 700 +4,861 ｜ C 743 +2,233 ｜ C 742 +2,055
仓位参考: Max Pain 720 ｜ Call Wall 730（+1.8%，弱）（OI 2.1k） ｜ Put Wall 700（-2.4%）（OI 5.8k）
量化解读： 存量两侧均衡｜ATM IV 24.0%｜历史 Rank 88%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 610,429 股

📆 10-22 Forward Structure
存量OI: C 28.1k / P 45.7k，今日变化ΔOI: C +7.5k / P +16.4k，平值价格ATM: C $6.59 / P $6.33 ｜ ATM IV 24.2%，净 delta 敞口 -43k shares
Top ΔOI: P 695 +10,130 ｜ P 718 +1,454 ｜ P 705 -1,210
仓位参考: Max Pain 724 ｜ Call Wall 730（+1.8%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 24.2%｜历史 Rank 88%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 42,969 股

📆 10-23 Forward Structure
存量OI: C 252.9k / P 350.8k，今日变化ΔOI: C +59.2k / P +97.6k，平值价格ATM: C $7.72 / P $7.10 ｜ ATM IV 23.9%，净 delta 敞口 648k shares
Top ΔOI: P 711 +12,262 ｜ C 740 +8,588 ｜ P 690 +8,020
仓位参考: Max Pain 727 ｜ Call Wall 735（+2.5%，弱）（OI 22.4k） ｜ Put Wall 711（-0.8%，弱）（OI 40.4k）
量化解读： 存量 Put 重｜ATM IV 23.9%｜历史 Rank 88%（近端代理）｜IV/RV 1.55×（近似）｜净 delta 敞口 正 647,512 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/QQQ_morning.json