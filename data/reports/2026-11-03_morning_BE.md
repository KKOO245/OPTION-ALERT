# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $753.95 ｜ QQQ $685.76
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（3D）ATM IV 124.8% vs 11-13 102.3%（差 +22.6pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-06 225C ΔOI +1,212（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 196.25 → 今开 210.33（+7.2%） | 较昨收变动（含盘初走势） ｜ 今日高 220.50 ｜ 低 208.20

Options: P/C成交量 0.26 | OI比 0.71 | ATM IV 124.8% | Skew 7.8pp | Term 0.72 | ExpMove ±9.4%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价显著（Skew 7.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±9.4% ｜ 11-13（10D）±14.0% ｜ 11-20（17D）±16.2% ｜ 11-27（24D）±18.4%
   ⇒ IV–VIX Spread: +103.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 796,457 | GEX Change vs 上次快照 6,851,416 | Flip: Primary Flip: 214.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 559 / LOW 91 / INVALID 196
结构观察区: Primary Flip 214.54（全链重定价，覆盖 100%）
Put Wall 200（现价高于该位 8.5%）
最近结构参考: Flip 215（现价高于该位 1.2%）
量化视角： 正 Gamma（80万，无历史分位）｜由负转正（+685万）｜现价位于 Flip 上方 1.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall） / 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 240.0C — Vol 3,415 | 最新价 $0.57 | OI 1479→2988 (ΔOI +1509张) | ΔOI/Volume 44.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1509张（+102.0% vs前日OI），连续性待观察（方向未知）
11-06 235.0C — Vol 2,113 | 最新价 $0.81 | OI 722→2020 (ΔOI +1298张) | ΔOI/Volume 61.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1298张（+179.8% vs前日OI），连续性待观察（方向未知）
11-06 225.0C — Vol 2,900 | 最新价 $1.68 | OI 1619→2831 (ΔOI +1212张) | ΔOI/Volume 41.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1212张（+74.9% vs前日OI），连续性待观察（方向未知）
11-06 250.0C — Vol 1,821 | 最新价 $0.27 | OI 1294→2498 (ΔOI +1204张) | ΔOI/Volume 66.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1204张（+93.0% vs前日OI），连续性待观察（方向未知）
11-06 230.0C — Vol 4,893 | 最新价 $1.17 | OI 1133→2168 (ΔOI +1035张) | ΔOI/Volume 21.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1035张（+91.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,258 张（Put 0 / Call 6,258），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +12.8k / P +3.3k ｜ Activity HIGH ｜ 3D
11-13  C +0.7k / P +0.9k ｜ Activity HIGH ｜ 10D
11-20  C +0.7k / P +41 ｜ Activity HIGH ｜ 17D
11-27  C +0.7k / P +0.5k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 43.2k / P 30.8k，今日变化ΔOI: C +12.8k / P +3.3k，平值价格ATM: C $9.64 / P $10.85 ｜ ATM IV 124.8%，净 delta 敞口 397k shares
Top ΔOI: C 240 +1,509 ｜ C 235 +1,298 ｜ C 225 +1,212
仓位参考: Max Pain 215 ｜ Call Wall 225（+3.6%，弱）（OI 2.8k） ｜ Put Wall 200（-7.9%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 124.8%｜历史 Rank 80%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 397,096 股

📆 11-13 Forward Structure
存量OI: C 12.1k / P 11.2k，今日变化ΔOI: C +0.7k / P +0.9k，平值价格ATM: C $14.50 / P $15.80 ｜ ATM IV 102.3%，净 delta 敞口 2k shares
Top ΔOI: P 192 +316 ｜ P 305 -143 ｜ C 222 -120
仓位参考: Max Pain 235 ｜ Call Wall 222.5（+2.5%，弱）（OI 0.6k） ｜ Put Wall 200（-7.9%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 102.3%｜历史 Rank 80%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,270 股

📆 11-20 Forward Structure
存量OI: C 62.1k / P 72.3k，今日变化ΔOI: C +0.7k / P +41，平值价格ATM: C $17.10 / P $18.15 ｜ ATM IV 95.6%，净 delta 敞口 37k shares
Top ΔOI: P 175 -164 ｜ C 200 +144
仓位参考: Max Pain 230 ｜ Call Wall 200（-7.9%，弱）（OI 2.2k） ｜ Put Wall 200（-7.9%，弱）（OI 5.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 95.6%｜历史 Rank 80%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,348 股

📆 11-27 Forward Structure
存量OI: C 6.1k / P 9.0k，今日变化ΔOI: C +0.7k / P +0.5k，平值价格ATM: C $20.40 / P $19.65 ｜ ATM IV 91.1%，净 delta 敞口 7k shares
Top ΔOI: C 265 +325 ｜ P 210 +267 ｜ C 215 +183
仓位参考: Max Pain 225 ｜ Call Wall 225（+3.6%，弱）（OI 0.5k） ｜ Put Wall 200（-7.9%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 91.1%｜历史 Rank 80%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 6,939 股

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 124.8% vs 11-13 102.3%（差 +22.6pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/BE_morning.json