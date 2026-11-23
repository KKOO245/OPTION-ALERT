# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.39 ｜ QQQ $651.03
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **事件差分**: 11-25 ATM IV 77.3% vs 11-27 63.2%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-25 140C ΔOI +1,947（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 138.43 → 今开 140.01（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 141.86 ｜ 低 138.82
⚠️ 标的停更 1 个交易日：以下对比基于 2026-11-19 晚报，趋势与 OI 增仓指标需 1 个交易日数据恢复

Options: P/C成交量 0.54 | OI比 0.88 | ATM IV 103.4% | Skew 8.2pp | Term 0.55 | ExpMove ±4.9%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜保护溢价显著（Skew 8.2pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-25（2D）±4.9% ｜ 11-27（4D）±5.4% ｜ 11-30（7D）±6.4% ｜ 12-02（9D）±7.8%
   ⇒ IV–VIX Spread: +76.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,263,893 | GEX Change vs 上次快照 78,885,310 | Flip: Primary Flip: 135.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 761 / LOW 187 / INVALID 580
结构观察区: Primary Flip 135.50（全链重定价，覆盖 99%）
最近结构参考: Flip 135（现价高于该位 3.3%）
量化视角： 正 Gamma（2826万，无历史分位）｜由负转正（+7889万）｜现价位于 Flip 上方 3.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 132（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- ⚠️ OI 增仓/异动基于 2026-11-19 快照对比（标的停更 1 个交易日），前几日数据可能失真，请谨慎解读
12-04 80.0P — Vol 9,450 | 最新价 $0.22 | OI 97→9356 (ΔOI +9259张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9259张（+9545.4% vs前日OI），连续性待观察（方向未知）
12-18 135.0C — Vol 10,983 | 最新价 $6.61 | OI 3232→9574 (ΔOI +6342张) | ΔOI/Volume 57.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6342张（+196.2% vs前日OI），连续性待观察（方向未知）
11-30 140.0C — Vol 1,450 | 最新价 $1.40 | OI 0→5369 (ΔOI +5369张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增5369张（前日OI缺失），值得跟踪（方向未知）
11-30 115.0P — Vol 87 | 最新价 $1.54 | OI 0→5034 (ΔOI +5034张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增5034张（前日OI缺失），值得跟踪（方向未知）
11-23 140.0C — Vol 10,120 | 最新价 $0.22 | OI 481→5370 (ΔOI +4889张) | ΔOI/Volume 48.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4889张（+1016.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 30,893 张（Put 14,293 / Call 16,600），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 40.3k / P 35.4k，今日成交量: C 37.3k / P 20.0k，平值价格ATM: C $1.43 / P $1.71 ｜ ATM IV 103.4%，预期波动 ±2.2%，Max Pain 132
Top ΔOI: C 140 +4,889 ｜ P 120 +4,873 ｜ C 131 +3,583

📆 Forward Expiration Structure

11-25  C +9.2k / P +7.9k ｜ Activity HIGH ｜ 2D（新行权价 C 1.0k / P 0.6k）
11-27  C +21.2k / P +32.9k ｜ Activity HIGH ｜ 4D（新行权价 C 24 / P 1.2k）
11-30  C N/A / P N/A ｜ Activity LOW ｜ 7D（新上架）
12-02  C N/A / P N/A ｜ Activity LOW ｜ 9D（新上架）

📆 11-25 Forward Structure
存量OI: C 15.8k / P 12.5k，今日变化ΔOI: C +9.2k / P +7.9k（新行权价 C 1.0k / P 0.6k），平值价格ATM: C $3.35 / P $3.48 ｜ ATM IV 77.3%，净 delta 敞口 284k shares
Top ΔOI: C 140 +1,947 ｜ C 135 +980 ｜ C 146 +847
仓位参考: Max Pain 135 ｜ Call Wall 140（+0.1%，弱）（OI 2.1k） ｜ Put Wall 130（-7.1%）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 77.3%｜历史 Rank 95%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 283,655 股

📆 11-27 Forward Structure
存量OI: C 151.7k / P 96.7k，今日变化ΔOI: C +21.2k / P +32.9k（新行权价 C 24 / P 1.2k），平值价格ATM: C $3.65 / P $3.85 ｜ ATM IV 63.2%，净 delta 敞口 1.0M shares
Top ΔOI: C 135 +4,416 ｜ P 129 +4,208 ｜ P 125 +4,046
仓位参考: Max Pain 137 ｜ Call Wall 150（+7.2%，弱）（OI 9.6k） ｜ Put Wall 140（+0.1%，弱）（OI 7.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 63.2%｜历史 Rank 95%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,027,707 股

11-30（Activity LOW）仓位参考: Max Pain 131 ｜ Call Wall 140（+0.1%）（OI 5.4k）

12-02（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 150（+7.2%）（OI 1.5k） ｜ Put Wall 130（-7.1%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 77.3% vs 11-27 63.2%（差 +14.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/SPCX_morning.json