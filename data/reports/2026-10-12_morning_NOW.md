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
🟡 **近现价集中开仓**: 10-30 150C ΔOI +69（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 140.86 → 今开 145.54（+3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 148.14 ｜ 低 142.24

Options: P/C成交量 0.24 | OI比 0.75 | ATM IV 54.5% | Skew 0.9pp | Term 1.07 | ExpMove ±4.5%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 1.07）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（4D）±4.5% ｜ 10-23（11D）±7.2% ｜ 10-30（18D）±12.2% ｜ 11-06（25D）±13.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,244,864 | GEX Change vs 上次快照 11,648,247 | Flip: Primary Flip: 132.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 530 / LOW 29 / INVALID 77
结构观察区: Primary Flip 132.55（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 4.0%）
最近结构参考: Call Wall 150（现价低于该位 4.0%）
量化视角： 正 Gamma（2824万，无历史分位）｜正 Gamma 增强（+1165万）｜现价位于 Flip 上方 8.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 110.0P — Vol 907 | 最新价 $0.50 | OI 984→1495 (ΔOI +511张) | ΔOI/Volume 56.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增511张（+51.9% vs前日OI），连续性待观察（方向未知）
10-16 150.0C — Vol 3,311 | 最新价 $0.79 | OI 15862→16235 (ΔOI +373张) | ΔOI/Volume 11.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增373张（+2.4% vs前日OI），值得跟踪（方向未知）
10-16 152.5C — Vol 466 | 最新价 $0.50 | OI 400→765 (ΔOI +365张) | ΔOI/Volume 78.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增365张（+91.2% vs前日OI），连续性待观察（方向未知）
10-16 144.0C — Vol 559 | 最新价 $2.15 | OI 582→931 (ΔOI +349张) | ΔOI/Volume 62.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增349张（+60.0% vs前日OI），连续性待观察（方向未知）
10-16 141.0C — Vol 1,036 | 最新价 $3.49 | OI 270→619 (ΔOI +349张) | ΔOI/Volume 33.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增349张（+129.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,947 张（Put 511 / Call 1,436），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +2.5k / P +1.0k ｜ Activity HIGH ｜ 4D
10-23  C +0.5k / P +0.5k ｜ Activity MEDIUM △ ｜ 11D
10-30  C +0.2k / P +0.5k ｜ Activity HIGH ｜ 18D
11-06  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 87.8k / P 66.3k，今日变化ΔOI: C +2.5k / P +1.0k，平值价格ATM: C $3.25 / P $3.15 ｜ ATM IV 54.5%，净 delta 敞口 34k shares
Top ΔOI: C 120 -504 ｜ C 150 +373 ｜ C 152 +365
仓位参考: Max Pain 130 ｜ Call Wall 150（+4.2%）（OI 16.2k） ｜ Put Wall 130（-9.7%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 54.5%｜历史 Rank 40%（近端代理）｜IV/RV 1.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 33,895 股

10-23（MEDIUM △）Top ΔOI: 157C +276
10-23（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 142（-1.4%，弱）（OI 1.2k）

📆 10-30 Forward Structure
存量OI: C 8.4k / P 10.8k，今日变化ΔOI: C +0.2k / P +0.5k，平值价格ATM: C $8.97 / P $8.55 ｜ ATM IV 66.3%，净 delta 敞口 1k shares
Top ΔOI: C 150 +69
仓位参考: Max Pain 135 ｜ Call Wall 150（+4.2%，弱）（OI 0.9k） ｜ Put Wall 130（-9.7%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 66.3%｜历史 Rank 40%（近端代理）｜IV/RV 2.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,126 股

11-06（MEDIUM △）Top ΔOI: 135P +19
11-06（MEDIUM △）仓位参考: Max Pain 137 ｜ Call Wall 155（+7.7%）（OI 0.9k） ｜ Put Wall 130（-9.7%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 54.5% vs 10-23 49.1%（差 +5.4pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/NOW_morning.json