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


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 423.96 → 今开 423.02（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 427.45 ｜ 低 421.03

Options: P/C成交量 0.53 | OI比 0.93 | ATM IV 35.2% | Skew 3.4pp | Term 1.33 | ExpMove ±3.9%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构正常偏陡（Term 1.33）｜保护溢价中性（Skew 3.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±3.9% ｜ 10-23（11D）±3.9% ｜ 10-30（18D）±0.0% ｜ 11-06（25D）±10.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,632,140 | GEX Change vs 上次快照 1,239,264 | Flip: Primary Flip: 404.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 326 / LOW 142 / INVALID 436
结构观察区: Primary Flip 404.32（全链重定价，覆盖 87%）
Call Wall 420（弱结构｜现价高于该位 1.6%）
最近结构参考: Call Wall 420（现价高于该位 1.6%）
量化视角： 正 Gamma（363万，无历史分位）｜正 Gamma 增强（+124万）｜现价位于 Flip 上方 5.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 404（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 457.5C — Vol 958 | 最新价 $0.30 | OI 0→219 (ΔOI +219张) | ΔOI/Volume 22.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增219张（前日OI缺失），值得跟踪（方向未知）
10-30 510.0C — Vol 342 | 最新价 $1.68 | OI 0→146 (ΔOI +146张) | ΔOI/Volume 42.7% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增146张（前日OI缺失），值得跟踪（方向未知）
10-23 340.0P — Vol 287 | 最新价 $0.74 | OI 8→147 (ΔOI +139张) | ΔOI/Volume 48.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增139张（+1737.5% vs前日OI），连续性待观察（方向未知）
10-16 450.0C — Vol 173 | 最新价 $0.90 | OI 563→702 (ΔOI +139张) | ΔOI/Volume 80.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增139张（+24.7% vs前日OI），连续性待观察（方向未知）
10-16 440.0C — Vol 176 | 最新价 $2.25 | OI 523→623 (ΔOI +100张) | ΔOI/Volume 56.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增100张（+19.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 743 张（Put 139 / Call 604），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.6k / P +53 ｜ Activity MEDIUM △ ｜ 4D
10-23  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 11D
10-30  C +0.3k / P +81 ｜ Activity MEDIUM △ ｜ 18D
11-06  C +11 / P +10 ｜ Activity LOW ｜ 25D

📆 10-16 Forward Structure
存量OI: C 11.5k / P 10.6k，今日变化ΔOI: C +0.6k / P +53，平值价格ATM: C $6.55 / P $10.00 ｜ ATM IV 35.2%，净 delta 敞口 -252 shares
Top ΔOI: C 457 +219 ｜ C 450 +139 ｜ C 440 +100
仓位参考: Max Pain 395 ｜ Call Wall 400（-6.2%，弱）（OI 0.9k） ｜ Put Wall 400（-6.2%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 35.2%｜历史 Rank 23%（近端代理）｜IV/RV 1.41×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 252 股

📆 10-23 Forward Structure
存量OI: C 1.9k / P 1.6k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $16.70 / P $0.00 ｜ ATM IV 61.1%，净 delta 敞口 4k shares
Top ΔOI: C 465 +18
仓位参考: Max Pain 415 ｜ Call Wall 425（-0.4%）（OI 0.5k） ｜ Put Wall 415（-2.7%）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.1%｜历史 Rank 23%（近端代理）｜IV/RV 2.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,813 股

10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 460（+7.8%，弱）（OI 94） ｜ Put Wall 400（-6.2%，弱）（OI 43）

11-06（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 455（+6.7%，弱）（OI 49） ｜ Put Wall 400（-6.2%，弱）（OI 37）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/ISRG_morning.json