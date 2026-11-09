# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.91 ｜ QQQ $679.35
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
🟡 **近现价集中开仓**: 11-10 753C ΔOI +4,464（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 735.29 → 今开 741.95（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 749.41 ｜ 低 741.09

Options: P/C成交量 0.49 | OI比 1.80 | ATM IV 25.2% | Skew 3.9pp | Term 0.69 | ExpMove ±1.1%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.80×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 35% ｜ P/C OI(近端) 47%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 35%）｜近端持仓结构中性（P/C OI 分位 47%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-10（1D）±1.1% ｜ 11-11（2D）±1.4% ｜ 11-12（3D）±1.6% ｜ 11-13（4D）±1.8%
   ⇒ IV–VIX Spread: +3.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -916,574,563 | GEX Change vs 上次快照 538,727,134 | Flip: Primary Flip: 758.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3336 / LOW 224 / INVALID 1656
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 758.44（全链重定价，覆盖 99%）
最近结构参考: Flip 758（现价低于该位 1.3%）
量化视角： 负 Gamma（9.17亿，历史分位 35%，中性区）｜负 Gamma 缓解（+5.39亿）｜现价位于 Flip 下方 1.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 741（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 758（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 710.0P — Vol 121,240 | 最新价 $5.39 | OI 23684→131906 (ΔOI +108222张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增108222张（+456.9% vs前日OI），连续性待观察（方向未知）
11-13 715.0P — Vol 63,406 | 最新价 $3.47 | OI 10487→64985 (ΔOI +54498张) | ΔOI/Volume 86.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54498张（+519.7% vs前日OI），连续性待观察（方向未知）
11-13 730.0P — Vol 62,713 | 最新价 $6.95 | OI 25107→70316 (ΔOI +45209张) | ΔOI/Volume 72.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增45209张（+180.1% vs前日OI），连续性待观察（方向未知）
11-20 725.0P — Vol 198,871 | 最新价 $8.55 | OI 110852→153423 (ΔOI +42571张) | ΔOI/Volume 21.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增42571张（+38.4% vs前日OI），连续性待观察（方向未知）
11-27 720.0P — Vol 45,476 | 最新价 $8.88 | OI 3280→45727 (ΔOI +42447张) | ΔOI/Volume 93.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增42447张（+1294.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 292,947 张（Put 292,947 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $183M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 193.3k / P 347.7k，今日成交量: C 804.8k / P 390.9k，平值价格ATM: C $2.24 / P $1.87 ｜ ATM IV 25.2%，预期波动 ±0.5%，Max Pain 741
Top ΔOI: P 730 +16,017 ｜ P 650 +13,649 ｜ P 610 +8,858

📆 Forward Expiration Structure

11-10  C +30.5k / P +19.3k ｜ Activity HIGH ｜ 1D
11-11  C +17.9k / P +7.4k ｜ Activity HIGH ｜ 2D
11-12  C +6.8k / P +8.1k ｜ Activity HIGH ｜ 3D
11-13  C +30.4k / P +147.0k ｜ Activity HIGH ｜ 4D

📆 11-10 Forward Structure
存量OI: C 139.6k / P 96.3k，今日变化ΔOI: C +30.5k / P +19.3k，平值价格ATM: C $4.28 / P $3.74 ｜ ATM IV 22.8%，净 delta 敞口 1.2M shares
Top ΔOI: C 753 +4,464 ｜ C 748 +4,215
仓位参考: Max Pain 740 ｜ Call Wall 740（-1.1%，弱）（OI 12.4k） ｜ Put Wall 734（-1.9%）（OI 10.0k）
量化解读： 存量 Call 重｜ATM IV 22.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,213,857 股

📆 11-11 Forward Structure
存量OI: C 76.3k / P 80.4k，今日变化ΔOI: C +17.9k / P +7.4k，平值价格ATM: C $5.44 / P $4.84 ｜ ATM IV 21.8%，净 delta 敞口 497k shares
Top ΔOI: P 716 +5,039 ｜ C 770 +3,760 ｜ P 725 -1,641
仓位参考: Max Pain 746 ｜ Call Wall 770（+2.9%）（OI 6.7k） ｜ Put Wall 750（+0.2%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 496,987 股

📆 11-12 Forward Structure
存量OI: C 55.4k / P 58.4k，今日变化ΔOI: C +6.8k / P +8.1k，平值价格ATM: C $6.40 / P $5.86 ｜ ATM IV 21.4%，净 delta 敞口 122k shares
Top ΔOI: P 725 +2,686 ｜ C 760 +1,275 ｜ P 735 +949
仓位参考: Max Pain 748 ｜ Call Wall 760（+1.6%，弱）（OI 2.4k） ｜ Put Wall 735（-1.8%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜ATM IV 21.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 122,216 股

📆 11-13 Forward Structure
存量OI: C 284.7k / P 488.3k，今日变化ΔOI: C +30.4k / P +147.0k，平值价格ATM: C $7.27 / P $6.47 ｜ ATM IV 21.3%，净 delta 敞口 29k shares
Top ΔOI: P 715 +54,498 ｜ P 730 +45,209 ｜ P 655 +9,014
仓位参考: Max Pain 750 ｜ Call Wall 750（+0.2%，弱）（OI 11.2k） ｜ Put Wall 730（-2.5%，弱）（OI 70.3k）
量化解读： 存量 Put 重｜ATM IV 21.3%｜历史 Rank 93%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 28,618 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SPY_morning.json