# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（4D）ATM IV 153.1% vs 11-27 120.8%（差 +32.3pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-20 110C ΔOI +2,142（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 115.88 → 今开 106.74（-7.9%） | 较昨收变动（含盘初走势） ｜ 今日高 111.55 ｜ 低 104.75

Options: P/C成交量 0.37 | OI比 0.68 | ATM IV 153.0% | Skew 15.1pp | Term 0.72 | ExpMove ±13.2%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价显著（Skew 15.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±13.2% ｜ 11-27（11D）±17.1% ｜ 12-04（18D）±9.1% ｜ 12-11（25D）±22.4%
   ⇒ IV–VIX Spread: +131.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,937,939 | GEX Change vs 上次快照 1,765,201 | Flip: Primary Flip: 119.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 493 / LOW 56 / INVALID 257
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 119.41（全链重定价，覆盖 100%）
Put Wall 100（弱结构｜现价高于该位 7.4%）
最近结构参考: Put Wall 100（现价高于该位 7.4%）
量化视角： 负 Gamma（594万，无历史分位）｜负 Gamma 缓解（+177万）｜现价位于 Flip 下方 10.02%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 119（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 120.0C — Vol 6,667 | 最新价 $5.40 | OI 1745→4343 (ΔOI +2598张) | ΔOI/Volume 39.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2598张（+148.9% vs前日OI），连续性待观察（方向未知）
11-20 130.0C — Vol 6,790 | 最新价 $2.38 | OI 1952→4156 (ΔOI +2204张) | ΔOI/Volume 32.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2204张（+112.9% vs前日OI），连续性待观察（方向未知）
11-20 110.0C — Vol 5,168 | 最新价 $10.60 | OI 119→2261 (ΔOI +2142张) | ΔOI/Volume 41.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2142张（+1800.0% vs前日OI），连续性待观察（方向未知）
11-20 80.0P — Vol 2,445 | 最新价 $0.22 | OI 2176→3804 (ΔOI +1628张) | ΔOI/Volume 66.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1628张（+74.8% vs前日OI），连续性待观察（方向未知）
11-20 170.0C — Vol 2,339 | 最新价 $0.12 | OI 2822→4179 (ΔOI +1357张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1357张（+48.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,929 张（Put 1,628 / Call 8,301），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +23.1k / P +0.6k ｜ Activity MEDIUM △ ｜ 4D
11-27  C +5.7k / P +0.4k ｜ Activity HIGH ｜ 11D
12-04  C +1.7k / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
12-11  C +1.0k / P +2.2k ｜ Activity HIGH ｜ 25D

📆 11-20 Forward Structure
存量OI: C 168.4k / P 114.0k，今日变化ΔOI: C +23.1k / P +0.6k，平值价格ATM: C $7.10 / P $7.05 ｜ ATM IV 153.1%，净 delta 敞口 919k shares
Top ΔOI: C 120 +2,598 ｜ C 130 +2,204 ｜ C 110 +2,142
仓位参考: Max Pain 145 ｜ Call Wall 110（+2.4%，弱）（OI 2.3k） ｜ Put Wall 115（+7.0%，弱）（OI 9.9k）
量化解读： 存量 Call 重｜ATM IV 153.1%｜历史 Rank 92%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 918,652 股

📆 11-27 Forward Structure
存量OI: C 28.8k / P 19.0k，今日变化ΔOI: C +5.7k / P +0.4k，平值价格ATM: C $9.50 / P $8.90 ｜ ATM IV 120.8%，净 delta 敞口 359k shares
Top ΔOI: P 225 -1,937 ｜ C 150 +1,250 ｜ C 116 +1,152
仓位参考: Max Pain 145 ｜ Call Wall 116（+8.0%，弱）（OI 1.2k） ｜ Put Wall 110（+2.4%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 120.8%｜历史 Rank 92%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 359,414 股

12-04（MEDIUM △）Top ΔOI: 70P -701 ｜ 80P -342
12-04（MEDIUM △）仓位参考: Max Pain 130 ｜ Put Wall 100（-6.9%，弱）（OI 0.9k）

📆 12-11 Forward Structure
存量OI: C 4.8k / P 7.6k，今日变化ΔOI: C +1.0k / P +2.2k，平值价格ATM: C $13.55 / P $10.50 ｜ ATM IV 111.7%，净 delta 敞口 -44k shares
Top ΔOI: P 100 +1,064 ｜ P 80 +462
仓位参考: Max Pain 140 ｜ Call Wall 115（+7.0%，弱）（OI 0.1k） ｜ Put Wall 100（-6.9%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 111.7%｜历史 Rank 92%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 负 43,545 股

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 153.1% vs 11-27 120.8%（差 +32.3pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/NBIS_morning.json