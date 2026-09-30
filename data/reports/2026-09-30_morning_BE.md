# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $769.13 ｜ QQQ $743.57
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 89.6% vs 10-09 76.6%（差 +13.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 290P ΔOI +1,375（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 291.25 → 今开 296.06（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 300.35 ｜ 低 286.62

Options: P/C成交量 1.08 | OI比 1.08 | ATM IV 89.6% | Skew -7.6pp | Term 0.95 | ExpMove ±5.6%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -7.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±5.6% ｜ 10-09（9D）±9.7% ｜ 10-16（16D）±13.3% ｜ 10-23（23D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,116,807 | GEX Change vs 上次快照 -4,111,074 | Flip: Primary Flip: 273.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 669 / LOW 86 / INVALID 135
结构观察区: Primary Flip 273.35（全链重定价，覆盖 100%）
Call Wall 300（弱结构｜现价低于该位 4.2%）
最近结构参考: Call Wall 300（现价低于该位 4.2%）
量化视角： 正 Gamma（912万，无历史分位）｜正 Gamma 减弱（411万）｜现价位于 Flip 上方 5.19%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 280（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 273（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 285.0P — Vol 1,866 | 最新价 $25.10 | OI 13→1728 (ΔOI +1715张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1715张（+13192.3% vs前日OI），连续性待观察（方向未知）
10-02 340.0C — Vol 3,682 | 最新价 $0.53 | OI 530→2004 (ΔOI +1474张) | ΔOI/Volume 40.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1474张（+278.1% vs前日OI），连续性待观察（方向未知）
10-02 290.0P — Vol 6,464 | 最新价 $8.98 | OI 1622→2997 (ΔOI +1375张) | ΔOI/Volume 21.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1375张（+84.8% vs前日OI），连续性待观察（方向未知）
10-02 350.0C — Vol 3,133 | 最新价 $0.23 | OI 907→2125 (ΔOI +1218张) | ΔOI/Volume 38.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1218张（+134.3% vs前日OI），连续性待观察（方向未知）
10-02 300.0C — Vol 11,795 | 最新价 $6.26 | OI 3991→5209 (ΔOI +1218张) | ΔOI/Volume 10.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1218张（+30.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,000 张（Put 3,090 / Call 3,910），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +12.6k / P +6.9k ｜ Activity HIGH ｜ 2D
10-09  C +2.7k / P +1.3k ｜ Activity HIGH ｜ 9D
10-16  C +1.6k / P +2.4k ｜ Activity MEDIUM △ ｜ 16D
10-23  C +1.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 49.5k / P 53.5k，今日变化ΔOI: C +12.6k / P +6.9k，平值价格ATM: C $8.00 / P $8.00 ｜ ATM IV 89.6%，净 delta 敞口 -274k shares
Top ΔOI: P 290 +1,375 ｜ C 300 +1,218
仓位参考: Max Pain 280 ｜ Call Wall 300（+4.3%）（OI 5.2k） ｜ Put Wall 290（+0.9%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 89.6%｜历史 Rank 52%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 274,010 股

📆 10-09 Forward Structure
存量OI: C 12.6k / P 16.3k，今日变化ΔOI: C +2.7k / P +1.3k，平值价格ATM: C $14.26 / P $13.65 ｜ ATM IV 76.6%，净 delta 敞口 -25k shares
Top ΔOI: P 240 -780 ｜ P 290 +690
仓位参考: Max Pain 270 ｜ Call Wall 300（+4.3%，弱）（OI 0.9k） ｜ Put Wall 290（+0.9%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.6%｜历史 Rank 52%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 24,596 股

10-16（MEDIUM △）Top ΔOI: 270C -934 ｜ 230P -915
10-16（MEDIUM △）仓位参考: Max Pain 260 ｜ Call Wall 270（-6.1%，弱）（OI 8.2k） ｜ Put Wall 260（-9.6%，弱）（OI 3.7k）

10-23（MEDIUM △）Top ΔOI: 220P +540 ｜ 275P +481
10-23（MEDIUM △）仓位参考: Max Pain 265 ｜ Call Wall 300（+4.3%，弱）（OI 0.8k） ｜ Put Wall 280（-2.6%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 89.6% vs 10-09 76.6%（差 +13.0pp）——覆盖 PCE 物价 Price Index MoM、Personal Spending MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/BE_morning.json