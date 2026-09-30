# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 93.7% vs 10-09 80.9%（差 +12.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 280C ΔOI +1,044（距现价 -3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 262.87 → 今开 272.82（+3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 297.60 ｜ 低 271.23

Options: P/C成交量 0.58 | OI比 1.26 | ATM IV 93.6% | Skew -4.5pp | Term 0.93 | ExpMove ±7.1%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -4.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.26×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±7.1% ｜ 10-09（10D）±11.2% ｜ 10-16（17D）±13.8% ｜ 10-23（24D）±15.9%
   ⇒ IV–VIX Spread: +77.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,949,864 | GEX Change vs 上次快照 8,647,829 | Flip: Primary Flip: 265.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 552 / LOW 79 / INVALID 259
结构观察区: Primary Flip 265.84（全链重定价，覆盖 100%）
Call Wall 270（弱结构｜现价高于该位 7.3%）
最近结构参考: Call Wall 270（现价高于该位 7.3%）
量化视角： 正 Gamma（1095万，无历史分位）｜正 Gamma 增强（+865万）｜现价位于 Flip 上方 8.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（MaxPain，仅结算参考） / 270（Call Wall，弱结构）。
• Gamma 区域：切换参考 266（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 250.0P — Vol 2,675 | 最新价 $3.85 | OI 2131→3839 (ΔOI +1708张) | ΔOI/Volume 63.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1708张（+80.2% vs前日OI），连续性待观察（方向未知）
10-16 270.0C — Vol 1,546 | 最新价 $14.85 | OI 8019→9162 (ΔOI +1143张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1143张（+14.2% vs前日OI），连续性待观察（方向未知）
10-02 280.0C — Vol 2,928 | 最新价 $3.50 | OI 1510→2554 (ΔOI +1044张) | ΔOI/Volume 35.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1044张（+69.1% vs前日OI），连续性待观察（方向未知）
10-02 290.0P — Vol 1,732 | 最新价 $29.23 | OI 630→1622 (ΔOI +992张) | ΔOI/Volume 57.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增992张（+157.5% vs前日OI），连续性待观察（方向未知）
10-02 260.0P — Vol 2,132 | 最新价 $7.38 | OI 2182→3107 (ΔOI +925张) | ΔOI/Volume 43.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增925张（+42.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,812 张（Put 3,625 / Call 2,187），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +2.5k / P +12.9k ｜ Activity HIGH ｜ 3D
10-09  C +2.3k / P +3.9k ｜ Activity HIGH ｜ 10D
10-16  C +1.6k / P +1.7k ｜ Activity HIGH ｜ 17D
10-23  C +2.1k / P +0.8k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 36.9k / P 46.6k，今日变化ΔOI: C +2.5k / P +12.9k，平值价格ATM: C $10.64 / P $10.00 ｜ ATM IV 93.7%，净 delta 敞口 37k shares
Top ΔOI: P 250 +1,708 ｜ C 280 +1,044 ｜ P 290 +992
仓位参考: Max Pain 270 ｜ Call Wall 300（+3.5%）（OI 4.0k） ｜ Put Wall 290（+0.1%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 93.7%｜历史 Rank 56%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,559 股

📆 10-09 Forward Structure
存量OI: C 9.9k / P 14.9k，今日变化ΔOI: C +2.3k / P +3.9k，平值价格ATM: C $17.00 / P $15.40 ｜ ATM IV 80.9%，净 delta 敞口 94k shares
Top ΔOI: P 250 +447 ｜ C 300 +415
仓位参考: Max Pain 260 ｜ Call Wall 300（+3.5%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 80.9%｜历史 Rank 56%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 93,642 股

📆 10-16 Forward Structure
存量OI: C 69.6k / P 76.2k，今日变化ΔOI: C +1.6k / P +1.7k，平值价格ATM: C $20.50 / P $19.41 ｜ ATM IV 79.3%，净 delta 敞口 91k shares
Top ΔOI: C 270 +1,143 ｜ C 280 -796 ｜ C 265 +534
仓位参考: Max Pain 260 ｜ Call Wall 270（-6.8%，弱）（OI 9.2k） ｜ Put Wall 270（-6.8%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜ATM IV 79.3%｜历史 Rank 56%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 91,497 股

📆 10-23 Forward Structure
存量OI: C 8.9k / P 13.3k，今日变化ΔOI: C +2.1k / P +0.8k，平值价格ATM: C $23.40 / P $22.73 ｜ ATM IV 77.7%，净 delta 敞口 76k shares
Top ΔOI: C 400 +520 ｜ C 280 +516 ｜ C 350 +319
仓位参考: Max Pain 250 ｜ Call Wall 280（-3.4%，弱）（OI 0.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.7%｜历史 Rank 56%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 76,302 股

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 93.7% vs 10-09 80.9%（差 +12.8pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/BE_morning.json