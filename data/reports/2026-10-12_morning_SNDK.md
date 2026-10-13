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
🟡 **近现价集中开仓**: 10-23 1500P ΔOI +233（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,581.82 → 今开 1,537.15（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 1538.09 ｜ 低 1472.56

Options: P/C成交量 0.78 | OI比 1.17 | ATM IV 65.9% | Skew 0.2pp | Term 1.01 | ExpMove ±5.7%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 1.01）｜保护溢价薄（Skew 0.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±5.7% ｜ 10-23（11D）±8.4% ｜ 10-30（18D）±12.7% ｜ 11-06（25D）±14.0%
   ⇒ IV–VIX Spread: +50.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,741,159 | GEX Change vs 上次快照 -5,619,184 | Flip: Primary Flip: 1631.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1812 / LOW 425 / INVALID 971
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1631.02（全链重定价，覆盖 99%）
最近结构参考: Flip 1631（现价低于该位 9.6%）
量化视角： 负 Gamma（1074万，无历史分位）｜负 Gamma 加深（562万）｜现价位于 Flip 下方 9.64%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,650（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1631（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 1000.0P — Vol 1,479 | 最新价 $0.15 | OI 2162→3352 (ΔOI +1190张) | ΔOI/Volume 80.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1190张（+55.0% vs前日OI），连续性待观察（方向未知）
10-16 750.0P — Vol 518 | 最新价 $0.10 | OI 111→565 (ΔOI +454张) | ΔOI/Volume 87.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增454张（+409.0% vs前日OI），连续性待观察（方向未知）
10-16 520.0P — Vol 399 | 最新价 $0.05 | OI 431→825 (ΔOI +394张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增394张（+91.4% vs前日OI），连续性待观察（方向未知）
10-16 1700.0C — Vol 1,710 | 最新价 $11.20 | OI 1464→1857 (ΔOI +393张) | ΔOI/Volume 23.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增393张（+26.8% vs前日OI），连续性待观察（方向未知）
10-23 1850.0C — Vol 710 | 最新价 $8.00 | OI 264→629 (ΔOI +365张) | ΔOI/Volume 51.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增365张（+138.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,796 张（Put 2,038 / Call 758），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +3.8k / P +6.9k ｜ Activity HIGH ｜ 4D
10-23  C +1.9k / P +2.1k ｜ Activity HIGH ｜ 11D
10-30  C +0.8k / P +0.6k ｜ Activity HIGH ｜ 18D
11-06  C +0.5k / P +0.6k ｜ Activity HIGH ｜ 25D

📆 10-16 Forward Structure
存量OI: C 56.4k / P 65.8k，今日变化ΔOI: C +3.8k / P +6.9k，平值价格ATM: C $41.70 / P $41.75 ｜ ATM IV 65.9%，净 delta 敞口 -209k shares
仓位参考: Max Pain 1,650 ｜ Call Wall 1600（+8.6%，弱）（OI 1.3k） ｜ Put Wall 1400（-5.0%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 65.9%｜历史 Rank 24%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 208,829 股

📆 10-23 Forward Structure
存量OI: C 14.3k / P 14.4k，今日变化ΔOI: C +1.9k / P +2.1k，平值价格ATM: C $62.00 / P $61.80 ｜ ATM IV 59.7%，净 delta 敞口 -34k shares
Top ΔOI: C 1850 +365 ｜ P 1500 +233
仓位参考: Max Pain 1,670 ｜ Call Wall 1600（+8.6%，弱）（OI 0.3k） ｜ Put Wall 1500（+1.8%）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 59.7%｜历史 Rank 24%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 33,971 股

📆 10-30 Forward Structure
存量OI: C 9.1k / P 11.9k，今日变化ΔOI: C +0.8k / P +0.6k，平值价格ATM: C $96.00 / P $91.35 ｜ ATM IV 69.9%，净 delta 敞口 3k shares
Top ΔOI: C 1600 +224 ｜ C 1500 +154
仓位参考: Max Pain 1,690 ｜ Call Wall 1600（+8.6%，弱）（OI 0.5k） ｜ Put Wall 1500（+1.8%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.9%｜历史 Rank 24%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,165 股

📆 11-06 Forward Structure
存量OI: C 3.6k / P 4.4k，今日变化ΔOI: C +0.5k / P +0.6k，平值价格ATM: C $107.53 / P $98.82 ｜ ATM IV 68.8%，净 delta 敞口 500 shares
Top ΔOI: P 1040 +122 ｜ C 1865 +56
仓位参考: Max Pain 1,670 ｜ Call Wall 1560（+5.8%，弱）（OI 0.1k） ｜ Put Wall 1400（-5.0%）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 68.8%｜历史 Rank 24%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 500 股

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 65.9% vs 10-23 59.7%（差 +6.3pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SNDK_morning.json