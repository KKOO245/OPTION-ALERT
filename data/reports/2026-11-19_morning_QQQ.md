# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $714.27 ｜ QQQ $645.04
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-20 678C ΔOI +14,930（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 725C ΔOI +9,953 占该期限总 OI 15.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 659.51 → 今开 671.05（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 675.30 ｜ 低 665.52

Options: P/C成交量 0.76 | OI比 1.01 | ATM IV 52.9% | Skew 5.8pp | Term 0.51 | ExpMove ±2.0%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.51，近月 IV 高于远月）｜保护溢价中性（Skew 5.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 56% ｜ P/C OI(近端) 6%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 56%）｜近端持仓极端 Call 重（P/C OI 分位 6%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-20（1D）±2.0% ｜ 11-23（4D）±2.6% ｜ 11-24（5D）±3.0% ｜ 11-25（6D）±3.2%
   ⇒ IV–VIX Spread: +30.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,363,052 | GEX Change vs 上次快照 496,350,095 | Flip: Primary Flip: 671.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3350 / LOW 283 / INVALID 1549
结构观察区: Primary Flip 671.47（全链重定价，覆盖 97%）
Put Wall 680（弱结构｜现价低于该位 1.1%）
最近结构参考: Flip 671（现价高于该位 0.2%）
量化视角： 正 Gamma（3936万，历史分位 56%，中性区）｜由负转正（+4.96亿）｜现价位于 Flip 上方 0.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 661（MaxPain，仅结算参考）；上方 680（Put Wall，弱结构）。
• Gamma 区域：切换参考 671（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 678.0C — Vol 18,957 | 最新价 $1.94 | OI 907→15837 (ΔOI +14930张) | ΔOI/Volume 78.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14930张（+1646.1% vs前日OI），连续性待观察（方向未知）
11-20 625.0P — Vol 28,408 | 最新价 $0.90 | OI 26755→40541 (ΔOI +13786张) | ΔOI/Volume 48.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13786张（+51.5% vs前日OI），连续性待观察（方向未知）
12-18 665.0P — Vol 17,674 | 最新价 $23.22 | OI 14339→27145 (ΔOI +12806张) | ΔOI/Volume 72.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12806张（+89.3% vs前日OI），连续性待观察（方向未知）
12-18 710.0C — Vol 46,664 | 最新价 $4.00 | OI 37295→49618 (ΔOI +12323张) | ΔOI/Volume 26.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12323张（+33.0% vs前日OI），连续性待观察（方向未知）
12-18 715.0C — Vol 11,511 | 最新价 $3.18 | OI 44077→54193 (ΔOI +10116张) | ΔOI/Volume 87.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10116张（+22.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 63,961 张（Put 26,592 / Call 37,369），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $30M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 128.0k / P 129.7k，今日成交量: C 483.3k / P 369.3k，平值价格ATM: C $4.02 / P $3.68 ｜ ATM IV 52.9%，预期波动 ±1.1%，Max Pain 661
Top ΔOI: P 585 +8,905 ｜ C 667 +4,531 ｜ C 675 +4,402

📆 Forward Expiration Structure

11-20  C +33.4k / P -15.9k ｜ Activity HIGH ｜ 1D
11-23  C +9.3k / P +5.8k ｜ Activity HIGH ｜ 4D
11-24  C +4.2k / P +16.2k ｜ Activity HIGH ｜ 5D
11-25  C +18.8k / P +8.7k ｜ Activity HIGH ｜ 6D

📆 11-20 Forward Structure
存量OI: C 1248.1k / P 1088.0k，今日变化ΔOI: C +33.4k / P -15.9k，平值价格ATM: C $6.88 / P $6.40 ｜ ATM IV 41.4%，净 delta 敞口 5.8M shares
Top ΔOI: C 678 +14,930 ｜ P 625 +13,786 ｜ P 680 -10,925
仓位参考: Max Pain 680 ｜ Call Wall 680（+1.1%，弱）（OI 43.0k） ｜ Put Wall 680（+1.1%）（OI 76.8k）
量化解读： 存量两侧均衡｜ATM IV 41.4%｜历史 Rank 99%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,802,409 股

📆 11-23 Forward Structure
存量OI: C 52.8k / P 42.6k，今日变化ΔOI: C +9.3k / P +5.8k，平值价格ATM: C $8.89 / P $8.56 ｜ ATM IV 30.1%，净 delta 敞口 361k shares
Top ΔOI: P 630 +1,363 ｜ C 690 +1,280 ｜ C 687 +1,253
仓位参考: Max Pain 665 ｜ Call Wall 690（+2.6%，弱）（OI 2.6k） ｜ Put Wall 665（-1.1%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 30.1%｜历史 Rank 99%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 360,509 股

📆 11-24 Forward Structure
存量OI: C 32.9k / P 44.6k，今日变化ΔOI: C +4.2k / P +16.2k，平值价格ATM: C $9.87 / P $10.00 ｜ ATM IV 31.1%，净 delta 敞口 100k shares
Top ΔOI: P 570 +6,343 ｜ P 555 +5,681 ｜ C 689 +1,125
仓位参考: Max Pain 666 ｜ Call Wall 685（+1.8%，弱）（OI 4.0k） ｜ Put Wall 660（-1.9%，弱）（OI 4.9k）
量化解读： 存量 Put 重｜ATM IV 31.1%｜历史 Rank 99%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 99,750 股

📆 11-25 Forward Structure
存量OI: C 41.7k / P 23.7k，今日变化ΔOI: C +18.8k / P +8.7k，平值价格ATM: C $10.69 / P $11.19 ｜ ATM IV 31.5%，净 delta 敞口 245k shares
Top ΔOI: C 725 +9,953 ｜ P 655 +1,892 ｜ C 690 +1,826
仓位参考: Max Pain 666 ｜ Call Wall 670（-0.4%，弱）（OI 2.5k） ｜ Put Wall 655（-2.6%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 31.5%｜历史 Rank 99%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 244,510 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/QQQ_morning.json