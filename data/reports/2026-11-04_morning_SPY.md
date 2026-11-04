# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.05 ｜ QQQ $696.62
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-05 730P ΔOI +3,887（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 754.35 → 今开 762.99（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 768.63 ｜ 低 762.64

Options: P/C成交量 0.66 | OI比 1.83 | ATM IV 22.5% | Skew 4.1pp | Term 0.61 | ExpMove ±0.8%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价中性（Skew 4.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.83×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 53% ｜ P/C OI(近端) 50%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 53%）｜近端持仓结构中性（P/C OI 分位 50%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-05（1D）±0.8% ｜ 11-06（2D）±1.0% ｜ 11-09（5D）±1.2% ｜ 11-10（6D）±1.4%
   ⇒ IV–VIX Spread: +5.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -129,982,500 | GEX Change vs 上次快照 1,379,590,684 | Flip: Primary Flip: 768.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2988 / LOW 293 / INVALID 1977
结构观察区: Primary Flip 768.74（全链重定价，覆盖 99%）
最近结构参考: Flip 769（现价低于该位 0.1%）
量化视角： 负 Gamma（1.30亿，历史分位 53%，中性区）｜负 Gamma 缓解（+13.80亿）｜现价位于 Flip 下方 0.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 757（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 718.0P — Vol 25,098 | 最新价 $3.14 | OI 26258→44244 (ΔOI +17986张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17986张（+68.5% vs前日OI），连续性待观察（方向未知）
11-04 770.0C — Vol 25,052 | 最新价 $0.17 | OI 4753→13444 (ΔOI +8691张) | ΔOI/Volume 34.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8691张（+182.8% vs前日OI），连续性待观察（方向未知）
11-04 755.0C — Vol 48,959 | 最新价 $4.09 | OI 1450→9605 (ΔOI +8155张) | ΔOI/Volume 16.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8155张（+562.4% vs前日OI），连续性待观察（方向未知）
11-04 760.0C — Vol 33,222 | 最新价 $1.96 | OI 3836→10095 (ΔOI +6259张) | ΔOI/Volume 18.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6259张（+163.2% vs前日OI），连续性待观察（方向未知）
11-06 615.0P — Vol 6,514 | 最新价 $0.03 | OI 1046→7038 (ΔOI +5992张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5992张（+572.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 47,083 张（Put 23,978 / Call 23,105），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 181.7k / P 333.3k，今日成交量: C 870.8k / P 578.6k，平值价格ATM: C $1.90 / P $1.83 ｜ ATM IV 22.5%，预期波动 ±0.5%，Max Pain 757
Top ΔOI: C 770 +8,691 ｜ C 755 +8,155 ｜ C 760 +6,259

📆 Forward Expiration Structure

11-05  C +30.5k / P +39.8k ｜ Activity HIGH ｜ 1D
11-06  C +20.9k / P +31.7k ｜ Activity HIGH ｜ 2D
11-09  C +9.6k / P +9.9k ｜ Activity HIGH ｜ 5D
11-10  C +8.8k / P +7.6k ｜ Activity HIGH ｜ 6D

📆 11-05 Forward Structure
存量OI: C 85.0k / P 130.8k，今日变化ΔOI: C +30.5k / P +39.8k，平值价格ATM: C $2.97 / P $2.84 ｜ ATM IV 16.2%，净 delta 敞口 1.5M shares
Top ΔOI: P 730 +3,887 ｜ C 745 +3,614
仓位参考: Max Pain 755 ｜ Call Wall 780（+1.6%）（OI 16.3k） ｜ Put Wall 750（-2.3%，弱）（OI 6.0k）
量化解读： 存量 Put 重｜ATM IV 16.2%｜历史 Rank 90%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,514,643 股

📆 11-06 Forward Structure
存量OI: C 238.3k / P 450.8k，今日变化ΔOI: C +20.9k / P +31.7k，平值价格ATM: C $4.19 / P $3.76 ｜ ATM IV 16.4%，净 delta 敞口 985k shares
Top ΔOI: P 730 +4,405
仓位参考: Max Pain 762 ｜ Call Wall 770（+0.3%，弱）（OI 17.7k） ｜ Put Wall 750（-2.3%）（OI 42.4k）
量化解读： 存量 Put 重｜ATM IV 16.4%｜历史 Rank 90%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 985,000 股

📆 11-09 Forward Structure
存量OI: C 34.6k / P 56.7k，今日变化ΔOI: C +9.6k / P +9.9k，平值价格ATM: C $4.89 / P $4.45 ｜ ATM IV 12.8%，净 delta 敞口 424k shares
Top ΔOI: C 757 +1,237 ｜ C 790 -1,177 ｜ C 786 +1,025
仓位参考: Max Pain 760 ｜ Call Wall 775（+1.0%，弱）（OI 4.1k） ｜ Put Wall 745（-2.9%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜ATM IV 12.8%｜历史 Rank 90%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 423,921 股

📆 11-10 Forward Structure
存量OI: C 28.8k / P 27.1k，今日变化ΔOI: C +8.8k / P +7.6k，平值价格ATM: C $5.82 / P $5.24 ｜ ATM IV 13.5%，净 delta 敞口 268k shares
Top ΔOI: C 780 +865 ｜ C 782 +854
仓位参考: Max Pain 760 ｜ Call Wall 775（+1.0%，弱）（OI 4.4k） ｜ Put Wall 755（-1.6%）（OI 3.3k）
量化解读： 存量两侧均衡｜ATM IV 13.5%｜历史 Rank 90%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 正 268,414 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/SPY_morning.json