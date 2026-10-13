# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.29 ↑3.0%（5D -1.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-14 235C ΔOI +3,277（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 195P ΔOI +9,450 占该期限总 OI 11.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 229.28 → 今开 228.73（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 228.86 ｜ 低 224.92

Options: P/C成交量 0.89 | OI比 1.04 | ATM IV 31.9% | Skew 0.2pp | Term 0.95 | ExpMove ±2.0%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 0.95）｜保护溢价薄（Skew 0.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-14（2D）±2.0% ｜ 10-16（4D）±2.8% ｜ 10-19（7D）±3.2% ｜ 10-21（9D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 325,916,655 | GEX Change vs 上次快照 89,647,209 | Flip: Primary Flip: 217.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 753 / LOW 198 / INVALID 587
结构观察区: Primary Flip 217.13（全链重定价，覆盖 97%）
Call Wall 240（弱结构｜现价低于该位 5.4%）
最近结构参考: Flip 217（现价高于该位 4.5%）
量化视角： 正 Gamma（3.26亿，无历史分位）｜正 Gamma 增强（+8965万）｜现价位于 Flip 上方 4.54%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 230（MaxPain，仅结算参考） / 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 217（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 110.0P — Vol 46,231 | 最新价 $0.01 | OI 9601→53629 (ΔOI +44028张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44028张（+458.6% vs前日OI），连续性待观察（方向未知）
10-16 237.5C — Vol 43,049 | 最新价 $0.93 | OI 12685→42425 (ΔOI +29740张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29740张（+234.4% vs前日OI），连续性待观察（方向未知）
10-16 232.5C — Vol 48,531 | 最新价 $2.33 | OI 17359→39819 (ΔOI +22460张) | ΔOI/Volume 46.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22460张（+129.4% vs前日OI），连续性待观察（方向未知）
10-16 235.0C — Vol 45,745 | 最新价 $1.53 | OI 53070→72867 (ΔOI +19797张) | ΔOI/Volume 43.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19797张（+37.3% vs前日OI），连续性待观察（方向未知）
10-16 242.5C — Vol 28,487 | 最新价 $0.34 | OI 22250→39928 (ΔOI +17678张) | ΔOI/Volume 62.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17678张（+79.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 133,703 张（Put 44,028 / Call 89,675），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 93.8k / P 97.4k，今日成交量: C 98.4k / P 87.1k，平值价格ATM: C $0.46 / P $1.20 ｜ ATM IV 31.9%，预期波动 ±0.7%，Max Pain 230
Top ΔOI: C 232 +12,508 ｜ C 235 +10,278 ｜ C 230 +7,715

📆 Forward Expiration Structure

10-14  C +15.4k / P +21.6k ｜ Activity HIGH ｜ 2D
10-16  C +73.0k / P +94.4k ｜ Activity MEDIUM △ ｜ 4D
10-19  C +6.0k / P +1.8k ｜ Activity HIGH ｜ 7D
10-21  C +3.5k / P +0.4k ｜ Activity HIGH ｜ 9D

📆 10-14 Forward Structure
存量OI: C 48.0k / P 37.6k，今日变化ΔOI: C +15.4k / P +21.6k，平值价格ATM: C $1.97 / P $2.65 ｜ ATM IV 32.0%，净 delta 敞口 -168k shares
Top ΔOI: C 235 +3,277 ｜ C 230 +2,887
仓位参考: Max Pain 230 ｜ Call Wall 237.5（+4.6%，弱）（OI 6.1k） ｜ Put Wall 215（-5.3%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.0%｜历史 Rank 12%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 168,478 股

10-16（MEDIUM △）Top ΔOI: 180C -29,978 ｜ 237C +29,740
10-16（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 220（-3.1%，弱）（OI 99.3k） ｜ Put Wall 220（-3.1%，弱）（OI 60.0k）

📆 10-19 Forward Structure
存量OI: C 30.4k / P 6.1k，今日变化ΔOI: C +6.0k / P +1.8k，平值价格ATM: C $3.45 / P $3.80 ｜ ATM IV 27.8%，净 delta 敞口 53k shares
Top ΔOI: C 235 +1,830 ｜ C 240 +675 ｜ C 245 +550
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+9.0%，弱）（OI 9.3k） ｜ Put Wall 220（-3.1%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 27.8%｜历史 Rank 12%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 52,878 股

📆 10-21 Forward Structure
存量OI: C 6.7k / P 2.4k，今日变化ΔOI: C +3.5k / P +0.4k，平值价格ATM: C $3.95 / P $4.32 ｜ ATM IV 28.3%，净 delta 敞口 43k shares
Top ΔOI: C 240 +2,176 ｜ C 230 +308 ｜ C 242 +286
仓位参考: Max Pain 230 ｜ Call Wall 240（+5.7%）（OI 3.1k） ｜ Put Wall 227.5（+0.2%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 28.3%｜历史 Rank 12%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 42,810 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/NVDA_morning.json