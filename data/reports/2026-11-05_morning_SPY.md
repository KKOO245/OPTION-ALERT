# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $752.25 ｜ QQQ $657.58
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 760P ΔOI +11,457（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 766.81 → 今开 765.47（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 765.97 ｜ 低 748.78

Options: P/C成交量 1.83 | OI比 1.74 | ATM IV 33.3% | Skew 1.9pp | Term 0.50 | ExpMove ±1.2%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜当日成交偏 Put（P/C量 1.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.83×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.74×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 21% ｜ P/C OI(近端) 42%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 21%）｜近端持仓结构中性（P/C OI 分位 42%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-06（1D）±1.2% ｜ 11-09（4D）±1.5% ｜ 11-10（5D）±1.8% ｜ 11-11（6D）±2.0%
   ⇒ IV–VIX Spread: +12.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,689,504,255 | GEX Change vs 上次快照 -1,434,740,314 | Flip: Primary Flip: 770.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3017 / LOW 322 / INVALID 1797
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.10（全链重定价，覆盖 98%）
最近结构参考: Flip 770（现价低于该位 2.2%）
量化视角： 负 Gamma（16.90亿，历史分位偏负区，比 79% 的交易日更负）｜负 Gamma 加深（14.35亿）｜现价位于 Flip 下方 2.21%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 766（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 728.0P — Vol 31,537 | 最新价 $1.35 | OI 29586→51015 (ΔOI +21429张) | ΔOI/Volume 68.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21429张（+72.4% vs前日OI），连续性待观察（方向未知）
11-05 764.0P — Vol 45,230 | 最新价 $0.89 | OI 9→13145 (ΔOI +13136张) | ΔOI/Volume 29.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13136张（+145955.6% vs前日OI），连续性待观察（方向未知）
11-05 770.0C — Vol 86,190 | 最新价 $1.16 | OI 4653→17572 (ΔOI +12919张) | ΔOI/Volume 15.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12919张（+277.6% vs前日OI），连续性待观察（方向未知）
11-06 760.0P — Vol 33,634 | 最新价 $1.08 | OI 11725→23182 (ΔOI +11457张) | ΔOI/Volume 34.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11457张（+97.7% vs前日OI），连续性待观察（方向未知）
11-09 680.0P — Vol 11,385 | 最新价 $0.02 | OI 294→11507 (ΔOI +11213张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11213张（+3813.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 70,154 张（Put 57,235 / Call 12,919），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 163.6k / P 284.6k，今日成交量: C 662.2k / P 1211.2k，平值价格ATM: C $2.46 / P $3.00 ｜ ATM IV 33.3%，预期波动 ±0.7%，Max Pain 766
Top ΔOI: P 764 +13,136 ｜ C 770 +12,919 ｜ P 760 +9,730

📆 Forward Expiration Structure

11-06  C +22.3k / P +44.9k ｜ Activity HIGH ｜ 1D
11-09  C +15.5k / P +40.4k ｜ Activity HIGH ｜ 4D
11-10  C +25.2k / P +38.3k ｜ Activity HIGH ｜ 5D
11-11  C +10.1k / P +29.1k ｜ Activity HIGH ｜ 6D

📆 11-06 Forward Structure
存量OI: C 260.5k / P 495.7k，今日变化ΔOI: C +22.3k / P +44.9k，平值价格ATM: C $4.52 / P $4.66 ｜ ATM IV 25.9%，净 delta 敞口 -3.8M shares
Top ΔOI: P 760 +11,457 ｜ P 767 +8,310 ｜ P 765 +6,220
仓位参考: Max Pain 765 ｜ Call Wall 770（+2.2%，弱）（OI 11.8k） ｜ Put Wall 750（-0.4%）（OI 38.6k）
量化解读： 存量 Put 重｜ATM IV 25.9%｜历史 Rank 98%（近端代理）｜IV/RV 2.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,777,006 股

📆 11-09 Forward Structure
存量OI: C 50.1k / P 97.2k，今日变化ΔOI: C +15.5k / P +40.4k，平值价格ATM: C $5.83 / P $5.76 ｜ ATM IV 17.8%，净 delta 敞口 -1.1M shares
Top ΔOI: P 680 +11,213 ｜ P 755 +6,070
仓位参考: Max Pain 764 ｜ Call Wall 775（+2.9%，弱）（OI 4.3k） ｜ Put Wall 755（+0.3%，弱）（OI 9.9k）
量化解读： 存量 Put 重｜ATM IV 17.8%｜历史 Rank 98%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 负 1,138,972 股

📆 11-10 Forward Structure
存量OI: C 54.0k / P 65.4k，今日变化ΔOI: C +25.2k / P +38.3k，平值价格ATM: C $6.75 / P $6.74 ｜ ATM IV 18.6%，净 delta 敞口 -2.4M shares
Top ΔOI: P 764 +5,797 ｜ P 772 +5,637 ｜ P 758 +5,085
仓位参考: Max Pain 770 ｜ Call Wall 770（+2.2%，弱）（OI 8.7k） ｜ Put Wall 764（+1.5%，弱）（OI 5.8k）
量化解读： 存量 Put 重｜ATM IV 18.6%｜历史 Rank 98%（近端代理）｜IV/RV 1.49×（近似）｜净 delta 敞口 负 2,384,737 股

📆 11-11 Forward Structure
存量OI: C 25.4k / P 53.2k，今日变化ΔOI: C +10.1k / P +29.1k，平值价格ATM: C $7.51 / P $7.31 ｜ ATM IV 18.7%，净 delta 敞口 -813k shares
Top ΔOI: P 750 +3,093 ｜ P 720 +2,820 ｜ P 763 +2,214
仓位参考: Max Pain 767 ｜ Call Wall 775（+2.9%，弱）（OI 2.9k） ｜ Put Wall 750（-0.4%，弱）（OI 6.4k）
量化解读： 存量 Put 重｜ATM IV 18.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.50×（近似）｜净 delta 敞口 负 812,834 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 25.9% vs 11-09 17.8%（差 +8.1pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/SPY_morning.json