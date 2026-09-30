# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $769.13 ｜ QQQ $743.55
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-02 132C ΔOI +1,125（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 129.94 → 今开 129.75（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 133.58 ｜ 低 128.85

Options: P/C成交量 0.34 | OI比 0.81 | ATM IV 58.2% | Skew -1.0pp | Term 1.02 | ExpMove ±3.6%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±3.6% ｜ 10-09（9D）±8.4% ｜ 10-16（16D）±10.6% ｜ 10-23（23D）±12.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,282,982 | GEX Change vs 上次快照 9,185,606 | Flip: Primary Flip: 131.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 549 / LOW 27 / INVALID 120
结构观察区: Primary Flip 131.66（全链重定价，覆盖 100%）
Put Wall 125（弱结构｜现价高于该位 6.2%）
最近结构参考: Flip 132（现价高于该位 0.8%）
量化视角： 正 Gamma（328万，无历史分位）｜由负转正（+919万）｜现价位于 Flip 上方 0.83%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（Put Wall，弱结构） / 132（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 132.0C — Vol 3,030 | 最新价 $1.96 | OI 616→1741 (ΔOI +1125张) | ΔOI/Volume 37.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1125张（+182.6% vs前日OI），连续性待观察（方向未知）
10-23 122.0P — Vol 1,061 | 最新价 $3.62 | OI 2095→3103 (ΔOI +1008张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1008张（+48.1% vs前日OI），连续性待观察（方向未知）
10-16 140.0C — Vol 1,618 | 最新价 $2.40 | OI 4619→5617 (ΔOI +998张) | ΔOI/Volume 61.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增998张（+21.6% vs前日OI），连续性待观察（方向未知）
10-23 117.0P — Vol 1,033 | 最新价 $2.03 | OI 1961→2957 (ΔOI +996张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增996张（+50.8% vs前日OI），连续性待观察（方向未知）
10-02 131.0C — Vol 1,939 | 最新价 $2.41 | OI 355→1102 (ΔOI +747张) | ΔOI/Volume 38.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增747张（+210.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,874 张（Put 2,004 / Call 2,870），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +4.0k / P +1.1k ｜ Activity HIGH ｜ 2D
10-09  C +1.0k / P +1.3k ｜ Activity MEDIUM △ ｜ 9D
10-16  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 16D
10-23  C +0.4k / P +2.5k ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 31.4k / P 25.4k，今日变化ΔOI: C +4.0k / P +1.1k，平值价格ATM: C $2.30 / P $2.54 ｜ ATM IV 58.2%，净 delta 敞口 186k shares
Top ΔOI: C 132 +1,125 ｜ C 131 +747 ｜ P 129 +446
仓位参考: Max Pain 132 ｜ Call Wall 140（+5.5%，弱）（OI 2.8k） ｜ Put Wall 125（-5.8%）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 58.2%｜历史 Rank 36%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 186,081 股

10-09（MEDIUM △）Top ΔOI: 134C +307 ｜ 120P +193
10-09（MEDIUM △）仓位参考: Max Pain 134 ｜ Put Wall 120（-9.6%，弱）（OI 1.1k）

📆 10-16 Forward Structure
存量OI: C 76.0k / P 62.8k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $5.76 / P $8.25 ｜ ATM IV 50.9%，净 delta 敞口 50k shares
Top ΔOI: C 140 +998 ｜ P 125 +445
仓位参考: Max Pain 130 ｜ Call Wall 140（+5.5%，弱）（OI 5.6k） ｜ Put Wall 125（-5.8%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 50.9%｜历史 Rank 36%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 49,910 股

10-23（MEDIUM △）Top ΔOI: 122P +1,008 ｜ 117P +996
10-23（MEDIUM △）仓位参考: Max Pain 133 ｜ Call Wall 140（+5.5%，弱）（OI 0.9k） ｜ Put Wall 122（-8.1%，弱）（OI 3.1k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 58.2% vs 10-09 51.3%（差 +6.9pp）——覆盖 PCE 物价 Price Index MoM、Personal Spending MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/NOW_morning.json