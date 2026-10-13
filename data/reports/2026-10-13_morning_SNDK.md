# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.90 ｜ QQQ $743.57
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
🟡 **事件差分**: 10-16 ATM IV 71.8% vs 10-23 61.8%（差 +10.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 1400P ΔOI +981（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,487.33 → 今开 1,405.75（-5.5%） | 较昨收变动（含盘初走势） ｜ 今日高 1463.29 ｜ 低 1403.16

Options: P/C成交量 0.59 | OI比 0.99 | ATM IV 71.8% | Skew 0.9pp | Term 0.93 | ExpMove ±5.5%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 0.93）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±5.5% ｜ 10-23（10D）±8.3% ｜ 10-30（17D）±12.7% ｜ 11-06（24D）±14.4%
   ⇒ IV–VIX Spread: +56.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,556,989 | GEX Change vs 上次快照 960,602 | Flip: Primary Flip: 1556.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1848 / LOW 472 / INVALID 888
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1556.48（全链重定价，覆盖 100%）
最近结构参考: Flip 1556（现价低于该位 8.0%）
量化视角： 负 Gamma（1056万，无历史分位）｜负 Gamma 缓解（+96万）｜现价位于 Flip 下方 7.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,600（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1556（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 1700.0C — Vol 4,954 | 最新价 $2.20 | OI 1857→3637 (ΔOI +1780张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1780张（+95.8% vs前日OI），连续性待观察（方向未知）
10-16 1600.0C — Vol 5,583 | 最新价 $8.20 | OI 1308→2462 (ΔOI +1154张) | ΔOI/Volume 20.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1154张（+88.2% vs前日OI），连续性待观察（方向未知）
10-23 1500.0C — Vol 1,757 | 最新价 $54.60 | OI 50→1068 (ΔOI +1018张) | ΔOI/Volume 57.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1018张（+2036.0% vs前日OI），连续性待观察（方向未知）
10-16 1400.0P — Vol 3,910 | 最新价 $10.00 | OI 2446→3427 (ΔOI +981张) | ΔOI/Volume 25.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增981张（+40.1% vs前日OI），连续性待观察（方向未知）
10-16 1675.0C — Vol 1,240 | 最新价 $2.95 | OI 293→1230 (ΔOI +937张) | ΔOI/Volume 75.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增937张（+319.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,870 张（Put 981 / Call 4,889），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +13.2k / P +3.4k ｜ Activity HIGH ｜ 3D
10-23  C +4.4k / P +1.6k ｜ Activity HIGH ｜ 10D
10-30  C +2.5k / P +0.6k ｜ Activity HIGH ｜ 17D
11-06  C +0.8k / P +0.6k ｜ Activity HIGH ｜ 24D

📆 10-16 Forward Structure
存量OI: C 69.6k / P 69.2k，今日变化ΔOI: C +13.2k / P +3.4k，平值价格ATM: C $42.71 / P $36.04 ｜ ATM IV 71.8%，净 delta 敞口 247k shares
Top ΔOI: C 1700 +1,780 ｜ C 1600 +1,154 ｜ P 1400 +981
仓位参考: Max Pain 1,600 ｜ Call Wall 1520（+6.1%，弱）（OI 1.6k） ｜ Put Wall 1400（-2.3%，弱）（OI 3.4k）
量化解读： 存量两侧均衡｜ATM IV 71.8%｜历史 Rank 28%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 247,295 股

📆 10-23 Forward Structure
存量OI: C 18.7k / P 16.0k，今日变化ΔOI: C +4.4k / P +1.6k，平值价格ATM: C $63.30 / P $55.20 ｜ ATM IV 61.8%，净 delta 敞口 74k shares
Top ΔOI: C 1500 +1,018 ｜ C 1550 +241
仓位参考: Max Pain 1,600 ｜ Call Wall 1500（+4.7%，弱）（OI 1.1k） ｜ Put Wall 1500（+4.7%）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 61.8%｜历史 Rank 28%（近端代理）｜IV/RV 1.29×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 73,704 股

📆 10-30 Forward Structure
存量OI: C 11.6k / P 12.5k，今日变化ΔOI: C +2.5k / P +0.6k，平值价格ATM: C $93.15 / P $89.19 ｜ ATM IV 72.3%，净 delta 敞口 40k shares
Top ΔOI: C 1500 +409 ｜ C 2040 +267 ｜ C 2000 +265
仓位参考: Max Pain 1,650 ｜ Call Wall 1500（+4.7%，弱）（OI 0.6k） ｜ Put Wall 1500（+4.7%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.3%｜历史 Rank 28%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,804 股

📆 11-06 Forward Structure
存量OI: C 4.3k / P 5.0k，今日变化ΔOI: C +0.8k / P +0.6k，平值价格ATM: C $106.20 / P $100.20 ｜ ATM IV 69.0%，净 delta 敞口 -3k shares
Top ΔOI: C 1650 +244 ｜ P 1500 +92
仓位参考: Max Pain 1,640 ｜ Call Wall 1560（+8.9%，弱）（OI 0.1k） ｜ Put Wall 1400（-2.3%）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.0%｜历史 Rank 28%（近端代理）｜IV/RV 1.45×（近似）｜净 delta 敞口 负 2,988 股

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 71.8% vs 10-23 61.8%（差 +10.0pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/SNDK_morning.json