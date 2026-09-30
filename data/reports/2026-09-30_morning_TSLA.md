# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $763.55 ｜ QQQ $739.77
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 49.4% vs 10-05 38.1%（差 +11.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 365C ΔOI +4,159（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 420C ΔOI +5,866 占该期限总 OI 11.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 352.84 → 今开 351.79（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 352.50 ｜ 低 345.88

Options: P/C成交量 0.88 | OI比 0.55 | ATM IV 48.3% | Skew -0.8pp | Term 0.92 | ExpMove ±3.2%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±3.2% ｜ 10-05（5D）±3.9% ｜ 10-07（7D）±4.6% ｜ 10-09（9D）±5.1%
   ⇒ IV–VIX Spread: +32.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,718,306 | GEX Change vs 上次快照 -2,718,382 | Flip: Primary Flip: 348.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1139 / LOW 119 / INVALID 718
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 348.89（全链重定价，覆盖 99%）
最近结构参考: Flip 349（现价低于该位 0.3%）
量化视角： 负 Gamma（1072万，无历史分位）｜负 Gamma 加深（272万）｜现价位于 Flip 下方 0.33%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 355（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 349（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 360.0C — Vol 74,409 | 最新价 $0.79 | OI 3845→10189 (ΔOI +6344张) | ΔOI/Volume 8.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6344张（+165.0% vs前日OI），连续性待观察（方向未知）
09-30 355.0C — Vol 90,170 | 最新价 $2.10 | OI 758→7098 (ΔOI +6340张) | ΔOI/Volume 7.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6340张（+836.4% vs前日OI），连续性待观察（方向未知）
10-05 420.0C — Vol 6,311 | 最新价 $0.12 | OI 707→6573 (ΔOI +5866张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5866张（+829.7% vs前日OI），连续性待观察（方向未知）
09-30 370.0C — Vol 32,700 | 最新价 $0.13 | OI 6532→12229 (ΔOI +5697张) | ΔOI/Volume 17.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5697张（+87.2% vs前日OI），连续性待观察（方向未知）
10-02 410.0C — Vol 6,828 | 最新价 $0.10 | OI 3929→9049 (ΔOI +5120张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5120张（+130.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,367 张（Put 0 / Call 29,367），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 130.4k / P 71.8k，今日成交量: C 186.0k / P 162.9k，平值价格ATM: C $2.91 / P $1.06 ｜ ATM IV 48.3%，预期波动 ±1.1%，Max Pain 355
Top ΔOI: C 360 +6,344 ｜ C 355 +6,340 ｜ C 370 +5,697

📆 Forward Expiration Structure

10-02  C +31.6k / P +11.9k ｜ Activity HIGH ｜ 2D
10-05  C +6.5k / P +1.4k ｜ Activity HIGH ｜ 5D
10-07  C +2.8k / P +1.2k ｜ Activity HIGH ｜ 7D
10-09  C +6.2k / P +6.1k ｜ Activity HIGH ｜ 9D

📆 10-02 Forward Structure
存量OI: C 246.5k / P 254.1k，今日变化ΔOI: C +31.6k / P +11.9k，平值价格ATM: C $6.50 / P $4.50 ｜ ATM IV 49.4%，净 delta 敞口 91k shares
Top ΔOI: C 365 +4,159 ｜ C 370 +2,946
仓位参考: Max Pain 360 ｜ Call Wall 360（+3.5%，弱）（OI 14.4k） ｜ Put Wall 350（+0.6%，弱）（OI 7.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 49.4%｜历史 Rank 36%（近端代理）｜IV/RV 1.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 91,121 股

📆 10-05 Forward Structure
存量OI: C 35.1k / P 15.9k，今日变化ΔOI: C +6.5k / P +1.4k，平值价格ATM: C $7.45 / P $5.94 ｜ ATM IV 38.1%，净 delta 敞口 55k shares
Top ΔOI: C 390 -3,941 ｜ C 375 +677
仓位参考: Max Pain 360 ｜ Call Wall 370（+6.4%，弱）（OI 2.0k） ｜ Put Wall 325（-6.5%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 38.1%｜历史 Rank 36%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 正 54,814 股

📆 10-07 Forward Structure
存量OI: C 9.1k / P 3.2k，今日变化ΔOI: C +2.8k / P +1.2k，平值价格ATM: C $8.65 / P $7.33 ｜ ATM IV 38.8%，净 delta 敞口 12k shares
Top ΔOI: C 355 +389 ｜ C 365 +288 ｜ C 380 +250
仓位参考: Max Pain 360 ｜ Call Wall 375（+7.8%，弱）（OI 1.1k） ｜ Put Wall 360（+3.5%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 38.8%｜历史 Rank 36%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 正 11,686 股

📆 10-09 Forward Structure
存量OI: C 59.7k / P 46.2k，今日变化ΔOI: C +6.2k / P +6.1k，平值价格ATM: C $10.00 / P $7.70 ｜ ATM IV 39.5%，净 delta 敞口 72k shares
仓位参考: Max Pain 360 ｜ Call Wall 370（+6.4%，弱）（OI 3.7k） ｜ Put Wall 350（+0.6%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 39.5%｜历史 Rank 36%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 正 71,787 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 49.4% vs 10-05 38.1%（差 +11.2pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/TSLA_morning.json