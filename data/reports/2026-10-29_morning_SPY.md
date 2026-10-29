# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $765.72 ｜ QQQ $715.34
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 765P ΔOI +13,462（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-03 660P ΔOI +11,337 占该期限总 OI 15.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 772.31 → 今开 768.79（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 769.92 ｜ 低 767.27

Options: P/C成交量 1.06 | OI比 1.64 | ATM IV 22.6% | Skew 2.0pp | Term 0.60 | ExpMove ±0.8%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价中性（Skew 2.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.64×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 38% ｜ P/C OI(近端) 34%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 38%）｜近端持仓结构中性（P/C OI 分位 34%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-30（1D）±0.8% ｜ 11-02（4D）±1.0% ｜ 11-03（5D）±1.1% ｜ 11-04（6D）±1.4%
   ⇒ IV–VIX Spread: +5.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -788,492,065 | GEX Change vs 上次快照 -639,323,829 | Flip: Primary Flip: 773.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 2504 / LOW 383 / INVALID 1429
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.88（全链重定价，覆盖 92%）
最近结构参考: Flip 774（现价低于该位 0.6%）
量化视角： 负 Gamma（7.88亿，历史分位 38%，中性区）｜负 Gamma 加深（6.39亿）｜现价位于 Flip 下方 0.57%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 734.0P — Vol 28,812 | 最新价 $2.60 | OI 13583→35390 (ΔOI +21807张) | ΔOI/Volume 75.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21807张（+160.6% vs前日OI），连续性待观察（方向未知）
11-04 767.0P — Vol 24,684 | 最新价 $3.66 | OI 11544→29783 (ΔOI +18239张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18239张（+158.0% vs前日OI），连续性待观察（方向未知）
10-30 765.0P — Vol 31,374 | 最新价 $1.28 | OI 45690→59152 (ΔOI +13462张) | ΔOI/Volume 42.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13462张（+29.5% vs前日OI），连续性待观察（方向未知）
11-03 660.0P — Vol 11,339 | 最新价 $0.02 | OI 2→11339 (ΔOI +11337张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11337张（+566850.0% vs前日OI），连续性待观察（方向未知）
11-06 749.0P — Vol 11,245 | 最新价 $1.39 | OI 571→10592 (ΔOI +10021张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10021张（+1755.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 74,866 张（Put 74,866 / Call 0），跨 5 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $15M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 124.7k / P 204.8k，今日成交量: C 504.5k / P 534.2k，平值价格ATM: C $2.34 / P $1.48 ｜ ATM IV 22.6%，预期波动 ±0.5%，Max Pain 770
Top ΔOI: P 770 +6,337 ｜ C 780 +5,823 ｜ C 775 +5,231

📆 Forward Expiration Structure

10-30  C +6.3k / P +29.6k ｜ Activity HIGH ｜ 1D
11-02  C +8.2k / P +25.0k ｜ Activity HIGH ｜ 4D
11-03  C +9.3k / P +18.5k ｜ Activity HIGH ｜ 5D
11-04  C +5.6k / P +29.6k ｜ Activity HIGH ｜ 6D

📆 10-30 Forward Structure
存量OI: C 674.7k / P 1666.2k，今日变化ΔOI: C +6.3k / P +29.6k，平值价格ATM: C $3.57 / P $2.42 ｜ ATM IV 16.3%，净 delta 敞口 -789k shares
Top ΔOI: P 765 +13,462 ｜ P 748 -5,984 ｜ C 764 +4,036
仓位参考: Max Pain 765 ｜ Call Wall 780（+1.4%，弱）（OI 27.9k） ｜ Put Wall 750（-2.5%，弱）（OI 67.1k）
量化解读： 存量 Put 重｜ATM IV 16.3%｜历史 Rank 91%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 789,312 股

📆 11-02 Forward Structure
存量OI: C 38.5k / P 76.6k，今日变化ΔOI: C +8.2k / P +25.0k，平值价格ATM: C $4.45 / P $3.21 ｜ ATM IV 11.4%，净 delta 敞口 -479k shares
Top ΔOI: P 775 +5,790 ｜ P 760 +3,071 ｜ P 705 +1,702
仓位参考: Max Pain 770 ｜ Call Wall 770（+0.1%，弱）（OI 2.1k） ｜ Put Wall 750（-2.5%，弱）（OI 8.9k）
量化解读： 存量 Put 重｜ATM IV 11.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.24×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 478,611 股

📆 11-03 Forward Structure
存量OI: C 26.4k / P 49.0k，今日变化ΔOI: C +9.3k / P +18.5k，平值价格ATM: C $4.90 / P $3.76 ｜ ATM IV 11.8%，净 delta 敞口 -45k shares
Top ΔOI: C 780 +2,524 ｜ P 759 +2,441
仓位参考: Max Pain 770 ｜ Call Wall 780（+1.4%，弱）（OI 3.3k） ｜ Put Wall 755（-1.9%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜ATM IV 11.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.29×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 44,519 股

📆 11-04 Forward Structure
存量OI: C 16.7k / P 66.7k，今日变化ΔOI: C +5.6k / P +29.6k，平值价格ATM: C $6.00 / P $4.72 ｜ ATM IV 13.0%，净 delta 敞口 -838k shares
Top ΔOI: P 767 +18,239 ｜ P 758 +3,548 ｜ P 760 +822
仓位参考: Max Pain 769 ｜ Call Wall 771（+0.2%，弱）（OI 1.3k） ｜ Put Wall 767（-0.3%）（OI 29.8k）
量化解读： 存量 Put 重｜ATM IV 13.0%｜历史 Rank 91%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 负 838,163 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SPY_morning.json