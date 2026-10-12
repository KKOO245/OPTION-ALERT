# 期权晚报 2026-10-12（快照 16:40 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-23 1500P ΔOI +233（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,537.15 → 收盘 1,487.33（-3.2%） ｜ 今日高 1538.09 ｜ 低 1464.43 ｜ 昨收 1,581.82 → 收盘 1,487.33（-6.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-15，窗口结束前不做对错判定）

Options: P/C成交量 0.67 | OI比 1.17 | ATM IV 63.6% | Skew 0.0pp | Term 1.02 | ExpMove ±5.4%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 1.02）｜保护溢价薄（Skew 0.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±5.4% ｜ 10-23（11D）±7.9% ｜ 10-30（18D）±12.2% ｜ 11-06（25D）±14.1%
   ⇒ IV–VIX Spread: +48.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,525,599 | GEX Change vs 上次快照 215,560 | Flip: Primary Flip: 1632.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1856 / LOW 429 / INVALID 923
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1632.38（全链重定价，覆盖 99%）
最近结构参考: Flip 1632（现价低于该位 8.9%）
量化视角： 负 Gamma（1053万，无历史分位）｜负 Gamma 缓解（+22万）｜现价位于 Flip 下方 8.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,650（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1632（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 1000.0P — Vol 112 | 最新价 $0.15 | OI 2162→3352 (ΔOI +1190张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1190张（+55.0% vs前日OI），连续性待观察（方向未知）
10-16 750.0P — Vol 1 | 最新价 $0.02 | OI 111→565 (ΔOI +454张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增454张（+409.0% vs前日OI），值得跟踪（方向未知）
10-16 520.0P — Vol 1 | 最新价 $0.03 | OI 431→825 (ΔOI +394张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增394张（+91.4% vs前日OI），值得跟踪（方向未知）
10-16 1700.0C — Vol 4,954 | 最新价 $2.20 | OI 1464→1857 (ΔOI +393张) | ΔOI/Volume 7.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增393张（+26.8% vs前日OI），连续性待观察（方向未知）
10-23 1850.0C — Vol 244 | 最新价 $2.87 | OI 264→629 (ΔOI +365张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增365张（+138.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,796 张（Put 2,038 / Call 758），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +3.8k / P +6.9k ｜ Activity HIGH ｜ 4D
10-23  C +1.9k / P +2.1k ｜ Activity HIGH ｜ 11D
10-30  C +0.8k / P +0.6k ｜ Activity HIGH ｜ 18D
11-06  C +0.5k / P +0.6k ｜ Activity HIGH ｜ 25D

📆 10-16 Forward Structure
存量OI: C 56.4k / P 65.8k，今日变化ΔOI: C +3.8k / P +6.9k，平值价格ATM: C $41.30 / P $38.39 ｜ ATM IV 63.6%，净 delta 敞口 -194k shares
仓位参考: Max Pain 1,650 ｜ Call Wall 1600（+7.6%，弱）（OI 1.3k） ｜ Put Wall 1400（-5.9%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 63.6%｜历史 Rank 20%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 194,210 股

📆 10-23 Forward Structure
存量OI: C 14.3k / P 14.4k，今日变化ΔOI: C +1.9k / P +2.1k，平值价格ATM: C $62.25 / P $55.91 ｜ ATM IV 57.4%，净 delta 敞口 -30k shares
Top ΔOI: C 1850 +365 ｜ P 1500 +233
仓位参考: Max Pain 1,670 ｜ Call Wall 1600（+7.6%，弱）（OI 0.3k） ｜ Put Wall 1500（+0.9%）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 57.4%｜历史 Rank 20%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 30,085 股

📆 10-30 Forward Structure
存量OI: C 9.1k / P 11.9k，今日变化ΔOI: C +0.8k / P +0.6k，平值价格ATM: C $96.30 / P $85.51 ｜ ATM IV 67.6%，净 delta 敞口 4k shares
Top ΔOI: C 1600 +224 ｜ C 1500 +154
仓位参考: Max Pain 1,690 ｜ Call Wall 1600（+7.6%，弱）（OI 0.5k） ｜ Put Wall 1500（+0.9%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 67.6%｜历史 Rank 20%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,475 股

📆 11-06 Forward Structure
存量OI: C 3.6k / P 4.4k，今日变化ΔOI: C +0.5k / P +0.6k，平值价格ATM: C $105.50 / P $104.12 ｜ ATM IV 66.0%，净 delta 敞口 1k shares
Top ΔOI: P 1040 +122 ｜ C 1865 +56
仓位参考: Max Pain 1,670 ｜ Call Wall 1560（+4.9%，弱）（OI 0.1k） ｜ Put Wall 1400（-5.9%）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 66.0%｜历史 Rank 20%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 1,135 股

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 63.6% vs 10-23 57.4%（差 +6.2pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=45 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=45）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SNDK_evening.json