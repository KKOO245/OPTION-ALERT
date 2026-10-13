# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.81 ｜ QQQ $743.57
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 56C ΔOI +3,095（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 54.35 → 今开 54.28（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 54.33 ｜ 低 53.71

Options: P/C成交量 0.50 | OI比 0.55 | ATM IV 38.7% | Skew -0.8pp | Term 0.86 | ExpMove ±1.8%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（1D）±1.8% ｜ 10-16（3D）±2.7% ｜ 10-19（6D）±3.4% ｜ 10-21（8D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 52,490,308 | GEX Change vs 上次快照 6,423,484 | Flip: Primary Flip: 52.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 715 / LOW 171 / INVALID 448
结构观察区: Primary Flip 52.21（全链重定价，覆盖 99%）
Put Wall 50（弱结构｜现价高于该位 7.9%）
最近结构参考: Flip 52（现价高于该位 3.3%）
量化视角： 正 Gamma（5249万，无历史分位）｜正 Gamma 增强（+642万）｜现价位于 Flip 上方 3.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 52（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 60.0C — Vol 5,785 | 最新价 $0.26 | OI 2736→7875 (ΔOI +5139张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5139张（+187.8% vs前日OI），连续性待观察（方向未知）
10-14 56.0C — Vol 3,835 | 最新价 $0.12 | OI 701→3796 (ΔOI +3095张) | ΔOI/Volume 80.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3095张（+441.5% vs前日OI），连续性待观察（方向未知）
10-14 55.0C — Vol 2,416 | 最新价 $0.31 | OI 685→2173 (ΔOI +1488张) | ΔOI/Volume 61.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1488张（+217.2% vs前日OI），连续性待观察（方向未知）
10-23 54.0P — Vol 2,879 | 最新价 $0.97 | OI 1592→3043 (ΔOI +1451张) | ΔOI/Volume 50.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1451张（+91.1% vs前日OI），连续性待观察（方向未知）
10-14 55.5C — Vol 1,218 | 最新价 $0.17 | OI 459→1517 (ΔOI +1058张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1058张（+230.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,231 张（Put 1,451 / Call 10,780），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-14  C +8.9k / P +2.9k ｜ Activity HIGH ｜ 1D
10-16  C -2.8k / P +0.9k ｜ Activity HIGH ｜ 3D
10-19  C +1.1k / P +0.8k ｜ Activity HIGH ｜ 6D
10-21  C +1.5k / P +0.5k ｜ Activity HIGH ｜ 8D

📆 10-14 Forward Structure
存量OI: C 20.8k / P 11.4k，今日变化ΔOI: C +8.9k / P +2.9k，平值价格ATM: C $0.45 / P $0.52 ｜ ATM IV 38.7%，净 delta 敞口 14k shares
Top ΔOI: C 56 +3,095 ｜ C 55 +1,488 ｜ C 55 +1,058
仓位参考: Max Pain 54 ｜ Call Wall 56（+3.8%）（OI 3.8k） ｜ Put Wall 54（+0.1%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 38.7%｜历史 Rank 64%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,512 股

📆 10-16 Forward Structure
存量OI: C 471.4k / P 195.9k，今日变化ΔOI: C -2.8k / P +0.9k，平值价格ATM: C $0.69 / P $0.75 ｜ ATM IV 35.7%，净 delta 敞口 53k shares
Top ΔOI: C 55 +950 ｜ C 55 +627
仓位参考: Max Pain 56 ｜ Call Wall 50（-7.3%，弱）（OI 26.9k） ｜ Put Wall 50（-7.3%，弱）（OI 23.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.7%｜历史 Rank 64%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,474 股

📆 10-19 Forward Structure
存量OI: C 3.6k / P 2.4k，今日变化ΔOI: C +1.1k / P +0.8k，平值价格ATM: C $0.93 / P $0.88 ｜ ATM IV 29.8%，净 delta 敞口 -10k shares
Top ΔOI: C 55 +357 ｜ C 55 +354 ｜ P 52 +147
仓位参考: Max Pain 54 ｜ Call Wall 55（+2.0%，弱）（OI 0.5k） ｜ Put Wall 55（+2.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 29.8%｜历史 Rank 64%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 负 10,104 股

📆 10-21 Forward Structure
存量OI: C 3.7k / P 1.4k，今日变化ΔOI: C +1.5k / P +0.5k，平值价格ATM: C $1.25 / P $1.01 ｜ ATM IV 30.8%，净 delta 敞口 2k shares
Top ΔOI: C 57 +307
仓位参考: Max Pain 54 ｜ Call Wall 53.5（-0.8%，弱）（OI 0.5k） ｜ Put Wall 53（-1.7%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 30.8%｜历史 Rank 64%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 2,436 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/SLV_morning.json