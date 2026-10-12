# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.00 ｜ QQQ $745.78
VIX 15.29 ↑3.0%（5D -1.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.0（neutral）
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
🟡 **近现价集中开仓**: 10-16 152P ΔOI +1,255（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 153.77 → 今开 153.43（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 154.12 ｜ 低 152.45

Options: P/C成交量 0.28 | OI比 1.74 | ATM IV 34.5% | Skew -1.3pp | Term 0.93 | ExpMove ±3.4%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.74×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（4D）±3.4% ｜ 10-23（11D）±4.9% ｜ 10-30（18D）±7.1% ｜ 11-06（25D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -52,876,916 | GEX Change vs 上次快照 -10,525,729 | Flip: Primary Flip: 160.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 402 / LOW 75 / INVALID 295
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 160.91（全链重定价，覆盖 90%）
Put Wall 150（现价高于该位 2.1%）
最近结构参考: Put Wall 150（现价高于该位 2.1%）
量化视角： 负 Gamma（5288万，无历史分位）｜负 Gamma 加深（1053万）｜现价位于 Flip 下方 4.80%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 158（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 152.0P — Vol 1,267 | 最新价 $1.56 | OI 563→1818 (ΔOI +1255张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1255张（+222.9% vs前日OI），连续性待观察（方向未知）
10-16 162.5C — Vol 1,258 | 最新价 $0.25 | OI 38→1284 (ΔOI +1246张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1246张（+3278.9% vs前日OI），连续性待观察（方向未知）
10-16 146.0P — Vol 1,354 | 最新价 $0.37 | OI 608→1762 (ΔOI +1154张) | ΔOI/Volume 85.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1154张（+189.8% vs前日OI），连续性待观察（方向未知）
10-30 142.0P — Vol 768 | 最新价 $1.20 | OI 91→451 (ΔOI +360张) | ΔOI/Volume 46.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增360张（+395.6% vs前日OI），连续性待观察（方向未知）
11-13 153.0P — Vol 350 | 最新价 $6.71 | OI 0→350 (ΔOI +350张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增350张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,365 张（Put 3,119 / Call 1,246），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.8k / P +0.2k ｜ Activity MEDIUM △ ｜ 4D
10-23  C +0.5k / P +0.3k ｜ Activity MEDIUM △ ｜ 11D
10-30  C -0.2k / P +0.5k ｜ Activity HIGH ｜ 18D
11-06  C +14 / P +0.1k ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 44.5k / P 77.2k，今日变化ΔOI: C +1.8k / P +0.2k，平值价格ATM: C $3.40 / P $1.80 ｜ ATM IV 34.5%，净 delta 敞口 13k shares
Top ΔOI: P 152 +1,255 ｜ C 162 +1,246 ｜ P 146 +1,154
仓位参考: Max Pain 158 ｜ Call Wall 155（+1.2%，弱）（OI 2.5k） ｜ Put Wall 150（-2.1%）（OI 23.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.5%｜历史 Rank 58%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,514 股

10-23（MEDIUM △）Top ΔOI: 155C +172 ｜ 153P +111
10-23（MEDIUM △）仓位参考: Max Pain 154 ｜ Call Wall 155（+1.2%，弱）（OI 0.2k） ｜ Put Wall 153（-0.1%，弱）（OI 0.6k）

📆 10-30 Forward Structure
存量OI: C 4.1k / P 18.0k，今日变化ΔOI: C -0.2k / P +0.5k，平值价格ATM: C $5.10 / P $5.72 ｜ ATM IV 32.1%，净 delta 敞口 -23k shares
Top ΔOI: P 142 +360 ｜ P 150 +216 ｜ C 155 -159
仓位参考: Max Pain 153 ｜ Call Wall 155（+1.2%）（OI 1.4k） ｜ Put Wall 150（-2.1%，弱）（OI 7.3k）
量化解读： 存量 Put 重｜ATM IV 32.1%｜历史 Rank 58%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 负 22,739 股

11-06（MEDIUM △）Top ΔOI: 155P +88 ｜ 162P +12
11-06（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 150（-2.1%，弱）（OI 35） ｜ Put Wall 150（-2.1%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/XBI_morning.json