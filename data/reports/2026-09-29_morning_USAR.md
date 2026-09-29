# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.86 ｜ QQQ $738.91
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
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
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 73.2% vs 10-09 63.1%（差 +10.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 14.41 → 今开 14.58（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 14.58 ｜ 低 14.10

Options: P/C成交量 0.48 | OI比 0.50 | ATM IV 73.2% | Skew -5.1pp | Term 0.94 | ExpMove ±5.5%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -5.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±5.5% ｜ 10-09（10D）±8.7% ｜ 10-16（17D）±11.5% ｜ 10-23（24D）±13.7%
   ⇒ IV–VIX Spread: +57.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,930,272 | GEX Change vs 上次快照 1,021,666 | Flip: Primary Flip: 15.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 188 / LOW 62 / INVALID 154
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 15.20（全链重定价，覆盖 100%）
Put Wall 15（弱结构｜现价低于该位 5.7%）
最近结构参考: Put Wall 15（现价低于该位 5.7%）
量化视角： 负 Gamma（293万，无历史分位）｜负 Gamma 缓解（+102万）｜现价位于 Flip 下方 6.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 15.5C — Vol 1,476 | 最新价 $0.11 | OI 464→1468 (ΔOI +1004张) | ΔOI/Volume 68.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1004张（+216.4% vs前日OI），连续性待观察（方向未知）
10-09 15.5P — Vol 900 | 最新价 $1.38 | OI 385→1238 (ΔOI +853张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增853张（+221.6% vs前日OI），连续性待观察（方向未知）
10-02 14.0P — Vol 925 | 最新价 $0.23 | OI 272→1093 (ΔOI +821张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增821张（+301.8% vs前日OI），连续性待观察（方向未知）
10-16 17.5C — Vol 828 | 最新价 $0.14 | OI 152→963 (ΔOI +811张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增811张（+533.5% vs前日OI），连续性待观察（方向未知）
10-16 18.5C — Vol 821 | 最新价 $0.10 | OI 443→1181 (ΔOI +738张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增738张（+166.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,227 张（Put 1,674 / Call 2,553），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +2.8k / P -1.5k ｜ Activity MEDIUM △ ｜ 3D
10-09  C +1.2k / P +1.8k ｜ Activity HIGH ｜ 10D
10-16  C +2.0k / P +1.4k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +0.9k / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 24.1k / P 12.0k，今日变化ΔOI: C +2.8k / P -1.5k，平值价格ATM: C $0.49 / P $0.28 ｜ ATM IV 73.2%，净 delta 敞口 267k shares
Top ΔOI: C 15 +1,004 ｜ P 17 -879 ｜ P 15 -827
仓位参考: Max Pain 16 ｜ Call Wall 15.5（+9.6%，弱）（OI 1.5k） ｜ Put Wall 15.5（+9.6%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 73.2%｜历史 Rank 4%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 267,293 股

📆 10-09 Forward Structure
存量OI: C 7.8k / P 6.3k，今日变化ΔOI: C +1.2k / P +1.8k，平值价格ATM: C $0.72 / P $0.51 ｜ ATM IV 63.1%，净 delta 敞口 -120k shares
Top ΔOI: P 15 +853 ｜ P 16 +563
仓位参考: Max Pain 16 ｜ Put Wall 15.5（+9.6%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 63.1%｜历史 Rank 4%（近端代理）｜IV/RV 1.15×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 120,006 股

10-16（MEDIUM △）Top ΔOI: 17P +642
10-16（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 15（+6.1%）（OI 5.7k）

10-23（MEDIUM △）Top ΔOI: 17P +212
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（+6.1%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 73.2% vs 10-09 63.1%（差 +10.1pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/USAR_morning.json