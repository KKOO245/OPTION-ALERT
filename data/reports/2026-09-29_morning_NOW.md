# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.73 ｜ QQQ $737.93
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-02 125P ΔOI +2,567（距现价 -4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 131.45 → 今开 130.83（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 132.25 ｜ 低 129.30

Options: P/C成交量 0.61 | OI比 0.89 | ATM IV 59.9% | Skew -1.3pp | Term 0.99 | ExpMove ±4.6%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（3D）±4.6% ｜ 10-09（10D）±7.2% ｜ 10-16（17D）±9.2% ｜ 10-23（24D）±11.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,466,367 | GEX Change vs 上次快照 -2,393,287 | Flip: Primary Flip: 132.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 556 / LOW 24 / INVALID 116
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 132.00（全链重定价，覆盖 100%）
Put Wall 125（弱结构｜现价高于该位 4.7%）
最近结构参考: Flip 132（现价低于该位 0.8%）
量化视角： 负 Gamma（247万，无历史分位）｜负 Gamma 加深（239万）｜现价位于 Flip 下方 0.82%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（Put Wall，弱结构）；上方 134（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 125.0P — Vol 3,576 | 最新价 $1.05 | OI 1318→3885 (ΔOI +2567张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2567张（+194.8% vs前日OI），连续性待观察（方向未知）
10-09 150.0C — Vol 2,596 | 最新价 $0.53 | OI 4790→7077 (ΔOI +2287张) | ΔOI/Volume 88.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2287张（+47.8% vs前日OI），连续性待观察（方向未知）
10-16 125.0P — Vol 2,345 | 最新价 $3.20 | OI 3928→5659 (ΔOI +1731张) | ΔOI/Volume 73.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1731张（+44.1% vs前日OI），连续性待观察（方向未知）
10-23 125.0P — Vol 1,543 | 最新价 $4.50 | OI 565→1950 (ΔOI +1385张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1385张（+245.1% vs前日OI），连续性待观察（方向未知）
10-02 135.0C — Vol 2,157 | 最新价 $1.90 | OI 505→1377 (ΔOI +872张) | ΔOI/Volume 40.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增872张（+172.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,842 张（Put 5,683 / Call 3,159），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +2.8k / P +5.0k ｜ Activity HIGH ｜ 3D
10-09  C +3.1k / P +1.9k ｜ Activity HIGH ｜ 10D
10-16  C +0.2k / P +1.9k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +0.3k / P +3.2k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 27.4k / P 24.3k，今日变化ΔOI: C +2.8k / P +5.0k，平值价格ATM: C $3.05 / P $2.95 ｜ ATM IV 59.9%，净 delta 敞口 28k shares
Top ΔOI: P 125 +2,567 ｜ C 135 +872 ｜ P 121 +786
仓位参考: Max Pain 134 ｜ Call Wall 140（+6.9%，弱）（OI 2.7k） ｜ Put Wall 125（-4.5%）（OI 3.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.9%｜历史 Rank 51%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,344 股

📆 10-09 Forward Structure
存量OI: C 14.3k / P 10.3k，今日变化ΔOI: C +3.1k / P +1.9k，平值价格ATM: C $4.40 / P $5.01 ｜ ATM IV 51.7%，净 delta 敞口 9k shares
Top ΔOI: C 150 +2,287
仓位参考: Max Pain 135 ｜ Put Wall 120（-8.3%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 51.7%｜历史 Rank 51%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 正 8,628 股

10-16（MEDIUM △）Top ΔOI: 125P +1,731
10-16（MEDIUM △）仓位参考: Max Pain 130 ｜ Call Wall 140（+6.9%，弱）（OI 4.6k） ｜ Put Wall 120（-8.3%，弱）（OI 5.7k）

📆 10-23 Forward Structure
存量OI: C 7.7k / P 12.7k，今日变化ΔOI: C +0.3k / P +3.2k，平值价格ATM: C $7.10 / P $8.00 ｜ ATM IV 53.2%，净 delta 敞口 -73k shares
Top ΔOI: P 125 +1,385 ｜ P 120 +573 ｜ P 122 +395
仓位参考: Max Pain 134 ｜ Call Wall 140（+6.9%，弱）（OI 1.0k） ｜ Put Wall 122（-6.8%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 53.2%｜历史 Rank 51%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 负 72,823 股

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 59.9% vs 10-09 51.7%（差 +8.2pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/NOW_morning.json