# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $743.41
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.0（neutral）
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
🟡 **事件差分**: 10-16 ATM IV 79.5% vs 10-23 69.3%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 200P ΔOI +1,103（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 210.06 → 今开 200.91（-4.4%） | 较昨收变动（含盘初走势） ｜ 今日高 203.60 ｜ 低 197.60

Options: P/C成交量 0.61 | OI比 0.96 | ATM IV 79.6% | Skew -2.3pp | Term 0.95 | ExpMove ±6.0%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±6.0% ｜ 10-23（10D）±9.1% ｜ 10-30（17D）±11.8% ｜ 11-06（24D）±14.3%
   ⇒ IV–VIX Spread: +64.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,180,701 | GEX Change vs 上次快照 -3,648,166 | Flip: Primary Flip: 218.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 502 / LOW 49 / INVALID 123
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 218.11（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价低于该位 0.7%）
最近结构参考: Put Wall 200（现价低于该位 0.7%）
量化视角： 负 Gamma（2018万，无历史分位）｜负 Gamma 加深（365万）｜现价位于 Flip 下方 8.91%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 218（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 230.0C — Vol 8,473 | 最新价 $1.23 | OI 6421→8964 (ΔOI +2543张) | ΔOI/Volume 30.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2543张（+39.6% vs前日OI），连续性待观察（方向未知）
10-16 220.0C — Vol 4,470 | 最新价 $3.00 | OI 2751→4441 (ΔOI +1690张) | ΔOI/Volume 37.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1690张（+61.4% vs前日OI），连续性待观察（方向未知）
10-23 215.0C — Vol 1,594 | 最新价 $7.60 | OI 102→1372 (ΔOI +1270张) | ΔOI/Volume 79.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1270张（+1245.1% vs前日OI），连续性待观察（方向未知）
10-23 310.0C — Vol 1,629 | 最新价 $0.19 | OI 378→1619 (ΔOI +1241张) | ΔOI/Volume 76.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1241张（+328.3% vs前日OI），连续性待观察（方向未知）
10-16 200.0P — Vol 9,901 | 最新价 $2.51 | OI 5075→6178 (ΔOI +1103张) | ΔOI/Volume 11.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1103张（+21.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,847 张（Put 1,103 / Call 6,744），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +12.6k / P +5.4k ｜ Activity HIGH ｜ 3D
10-23  C +5.2k / P +3.7k ｜ Activity HIGH ｜ 10D
10-30  C +1.7k / P +1.0k ｜ Activity HIGH ｜ 17D
11-06  C +0.6k / P +1.7k ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 126.5k / P 121.6k，今日变化ΔOI: C +12.6k / P +5.4k，平值价格ATM: C $6.84 / P $5.00 ｜ ATM IV 79.5%，净 delta 敞口 80k shares
Top ΔOI: C 230 +2,543 ｜ C 220 +1,690 ｜ P 200 +1,103
仓位参考: Max Pain 220 ｜ Call Wall 210（+5.7%，弱）（OI 3.4k） ｜ Put Wall 190（-4.4%，弱）（OI 7.2k）
量化解读： 存量两侧均衡｜ATM IV 79.5%｜历史 Rank 12%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 80,346 股

📆 10-23 Forward Structure
存量OI: C 24.4k / P 18.9k，今日变化ΔOI: C +5.2k / P +3.7k，平值价格ATM: C $9.82 / P $8.23 ｜ ATM IV 69.3%，净 delta 敞口 -33k shares
Top ΔOI: C 215 +1,270 ｜ P 190 +867
仓位参考: Max Pain 215 ｜ Call Wall 212.5（+7.0%，弱）（OI 2.1k） ｜ Put Wall 200（+0.7%）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 69.3%｜历史 Rank 12%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 32,963 股

📆 10-30 Forward Structure
存量OI: C 22.6k / P 17.6k，今日变化ΔOI: C +1.7k / P +1.0k，平值价格ATM: C $12.80 / P $10.75 ｜ ATM IV 69.4%，净 delta 敞口 5k shares
Top ΔOI: C 220 +430
仓位参考: Max Pain 225 ｜ Put Wall 200（+0.7%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 69.4%｜历史 Rank 12%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 4,690 股

11-06（MEDIUM △）Top ΔOI: 200P +493 ｜ 220P +230
11-06（MEDIUM △）仓位参考: Max Pain 230 ｜ Put Wall 200（+0.7%）（OI 3.0k）

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 79.5% vs 10-23 69.3%（差 +10.3pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/NBIS_morning.json