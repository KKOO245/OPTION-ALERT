# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $769.11 ｜ QQQ $721.42
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-22 736C ΔOI +16,949（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-27 740C ΔOI +9,796 占该期限总 OI 14.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 717.63 → 今开 722.22（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 723.57 ｜ 低 719.72

Options: P/C成交量 0.80 | OI比 1.71 | ATM IV 29.2% | Skew 3.0pp | Term 0.74 | ExpMove ±1.2%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价中性（Skew 3.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.71×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 25% ｜ P/C OI(近端) 57%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 25%）｜近端持仓结构中性（P/C OI 分位 57%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-22（1D）±1.2% ｜ 10-23（2D）±1.5% ｜ 10-26（5D）±1.9% ｜ 10-27（6D）±2.1%
   ⇒ IV–VIX Spread: +12.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -399,020,091 | GEX Change vs 上次快照 450,287,077 | Flip: Primary Flip: 729.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3321 / LOW 319 / INVALID 1638
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 729.08（全链重定价，覆盖 99%）
最近结构参考: Flip 729（现价低于该位 0.8%）
量化视角： 负 Gamma（3.99亿，历史分位偏负区，比 75% 的交易日更负）｜负 Gamma 缓解（+4.50亿）｜现价位于 Flip 下方 0.80%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 719（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 729（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-22 540.0P — Vol 21,783 | 最新价 $0.01 | OI 105→20437 (ΔOI +20332张) | ΔOI/Volume 93.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20332张（+19363.8% vs前日OI），连续性待观察（方向未知）
10-22 736.0C — Vol 18,050 | 最新价 $0.26 | OI 314→17263 (ΔOI +16949张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16949张（+5397.8% vs前日OI），连续性待观察（方向未知）
10-22 733.0C — Vol 17,094 | 最新价 $0.51 | OI 721→15916 (ΔOI +15195张) | ΔOI/Volume 88.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15195张（+2107.5% vs前日OI），连续性待观察（方向未知）
10-22 722.0C — Vol 16,352 | 最新价 $3.57 | OI 735→12760 (ΔOI +12025张) | ΔOI/Volume 73.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12025张（+1636.0% vs前日OI），连续性待观察（方向未知）
10-27 740.0C — Vol 11,750 | 最新价 $1.08 | OI 562→10358 (ΔOI +9796张) | ΔOI/Volume 83.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9796张（+1743.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 74,297 张（Put 20,332 / Call 53,965），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 119.1k / P 203.9k，今日成交量: C 489.8k / P 389.8k，平值价格ATM: C $2.17 / P $2.41 ｜ ATM IV 29.2%，预期波动 ±0.6%，Max Pain 719
Top ΔOI: C 725 +5,058 ｜ P 653 +4,638 ｜ P 654 +4,352

📆 Forward Expiration Structure

10-22  C +57.8k / P +50.4k ｜ Activity HIGH ｜ 1D
10-23  C +17.6k / P +13.9k ｜ Activity HIGH ｜ 2D
10-26  C +8.0k / P +14.0k ｜ Activity HIGH ｜ 5D
10-27  C +13.3k / P +10.1k ｜ Activity HIGH ｜ 6D

📆 10-22 Forward Structure
存量OI: C 93.3k / P 113.3k，今日变化ΔOI: C +57.8k / P +50.4k，平值价格ATM: C $4.29 / P $4.28 ｜ ATM IV 24.9%，净 delta 敞口 1.3M shares
Top ΔOI: C 736 +16,949 ｜ C 733 +15,195
仓位参考: Max Pain 720 ｜ Call Wall 736（+1.8%，弱）（OI 17.3k） ｜ Put Wall 708（-2.1%，弱）（OI 10.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.9%｜历史 Rank 89%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,279,598 股

📆 10-23 Forward Structure
存量OI: C 276.2k / P 420.7k，今日变化ΔOI: C +17.6k / P +13.9k，平值价格ATM: C $5.63 / P $5.42 ｜ ATM IV 24.2%，净 delta 敞口 620k shares
Top ΔOI: P 710 +5,637 ｜ P 720 -4,104 ｜ C 720 +3,290
仓位参考: Max Pain 725 ｜ Call Wall 735（+1.6%）（OI 25.6k） ｜ Put Wall 710（-1.8%，弱）（OI 45.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.2%｜历史 Rank 89%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 619,652 股

📆 10-26 Forward Structure
存量OI: C 34.0k / P 57.5k，今日变化ΔOI: C +8.0k / P +14.0k，平值价格ATM: C $7.02 / P $6.59 ｜ ATM IV 19.4%，净 delta 敞口 44k shares
Top ΔOI: C 762 +2,126
仓位参考: Max Pain 725 ｜ Call Wall 740（+2.3%，弱）（OI 1.2k） ｜ Put Wall 720（-0.4%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 19.4%｜历史 Rank 89%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 正 44,106 股

📆 10-27 Forward Structure
存量OI: C 27.6k / P 38.3k，今日变化ΔOI: C +13.3k / P +10.1k，平值价格ATM: C $7.96 / P $7.20 ｜ ATM IV 20.0%，净 delta 敞口 -7k shares
Top ΔOI: C 740 +9,796 ｜ P 729 +1,689 ｜ P 722 +1,675
仓位参考: Max Pain 728 ｜ Call Wall 740（+2.3%）（OI 10.4k） ｜ Put Wall 722（-0.2%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 20.0%｜历史 Rank 89%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 负 7,292 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/QQQ_morning.json