# 期权晨报 2026-11-18（快照 10:20 ET）

📊 市场环境

SPY $735.61 ｜ QQQ $nan
VIX 24.58 ↓3.5%（5D +40.5%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-19 632P ΔOI +2,511（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 656.95 → 今开 661.07（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 662.80 ｜ 低 653.80

Options: P/C成交量 1.15 | OI比 1.29 | ATM IV 51.7% | Skew 5.1pp | Term 0.57 | ExpMove ±2.1%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 26% ｜ P/C OI(近端) 21%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 26%）｜近端持仓结构中性（P/C OI 分位 21%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-19（1D）±2.1% ｜ 11-20（2D）±2.8% ｜ 11-23（5D）±3.3% ｜ 11-24（6D）±3.6%
   ⇒ IV–VIX Spread: +27.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -374,522,754 | GEX Change vs 上次快照 227,977,025 | Flip: Primary Flip: 672.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3576 / LOW 136 / INVALID 1442
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 672.26（全链重定价，覆盖 96%）
最近结构参考: Flip 672（现价低于该位 1.8%）
量化视角： 负 Gamma（3.75亿，历史分位 26%，中性区）｜负 Gamma 缓解（+2.28亿）｜现价位于 Flip 下方 1.80%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 660（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 672（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 592.0P — Vol 24,468 | 最新价 $0.52 | OI 566→22177 (ΔOI +21611张) | ΔOI/Volume 88.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21611张（+3818.2% vs前日OI），连续性待观察（方向未知）
11-20 679.0C — Vol 23,268 | 最新价 $2.83 | OI 1144→20701 (ΔOI +19557张) | ΔOI/Volume 84.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19557张（+1709.5% vs前日OI），连续性待观察（方向未知）
12-04 610.0P — Vol 19,592 | 最新价 $5.50 | OI 377→18937 (ΔOI +18560张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18560张（+4923.1% vs前日OI），连续性待观察（方向未知）
12-04 635.0P — Vol 19,101 | 最新价 $10.35 | OI 1164→19383 (ΔOI +18219张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18219张（+1565.2% vs前日OI），连续性待观察（方向未知）
11-30 675.0C — Vol 14,470 | 最新价 $7.95 | OI 2919→14483 (ΔOI +11564张) | ΔOI/Volume 79.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11564张（+396.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 89,511 张（Put 58,390 / Call 31,121），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $29M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 134.8k / P 173.9k，今日成交量: C 466.3k / P 534.2k，平值价格ATM: C $3.56 / P $3.81 ｜ ATM IV 51.7%，预期波动 ±1.1%，Max Pain 660
Top ΔOI: P 580 +8,440 ｜ C 670 +5,673 ｜ P 575 +5,524

📆 Forward Expiration Structure

11-19  C +19.6k / P +13.5k ｜ Activity HIGH ｜ 1D
11-20  C +101.6k / P +58.3k ｜ Activity MEDIUM △ ｜ 2D
11-23  C +6.9k / P +10.6k ｜ Activity HIGH ｜ 5D
11-24  C +13.3k / P +1.3k ｜ Activity HIGH ｜ 6D

📆 11-19 Forward Structure
存量OI: C 59.3k / P 73.5k，今日变化ΔOI: C +19.6k / P +13.5k，平值价格ATM: C $6.95 / P $7.12 ｜ ATM IV 45.8%，净 delta 敞口 302k shares
Top ΔOI: P 632 +2,511 ｜ C 680 +2,137 ｜ P 607 +1,042
仓位参考: Max Pain 666 ｜ Put Wall 664（+0.6%，弱）（OI 5.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 301,955 股

11-20（MEDIUM △）Top ΔOI: 592P +21,611 ｜ 679C +19,557
11-20（MEDIUM △）仓位参考: Max Pain 685 ｜ Call Wall 670（+1.5%，弱）（OI 22.6k） ｜ Put Wall 650（-1.5%，弱）（OI 39.0k）

📆 11-23 Forward Structure
存量OI: C 43.5k / P 36.9k，今日变化ΔOI: C +6.9k / P +10.6k，平值价格ATM: C $11.07 / P $10.90 ｜ ATM IV 34.7%，净 delta 敞口 -33k shares
Top ΔOI: P 645 +4,279
仓位参考: Max Pain 670 ｜ Put Wall 645（-2.3%）（OI 5.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.7%｜历史 Rank 99%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 负 32,731 股

📆 11-24 Forward Structure
存量OI: C 28.7k / P 28.4k，今日变化ΔOI: C +13.3k / P +1.3k，平值价格ATM: C $12.16 / P $11.95 ｜ ATM IV 34.9%，净 delta 敞口 276k shares
Top ΔOI: C 685 +3,705 ｜ C 695 +3,035 ｜ P 660 -1,760
仓位参考: Max Pain 670 ｜ Put Wall 660（-0.0%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜ATM IV 34.9%｜历史 Rank 99%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 275,855 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/QQQ_morning.json