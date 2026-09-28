# 期权晚报 2026-09-28（快照 16:40 ET）

📊 市场环境

SPY $765.61 ｜ QQQ $736.53
VIX 16.07 ↑8.1%（5D +8.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 235C ΔOI +2,171（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 235.00 → 收盘 231.88（-1.3%） ｜ 今日高 245.35 ｜ 低 228.38 ｜ 昨收 237.33 → 收盘 231.88（-2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.72 | ATM IV 87.1% | Skew -1.6pp | Term 0.88 | ExpMove ±7.3%（近端） | Rank 19%
量化视角： IV 历史低位（Rank 19%，期权偏便宜）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±7.3% ｜ 10-09（11D）±11.1% ｜ 10-16（18D）±13.5% ｜ 10-23（25D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,662,985 | GEX Change vs 上次快照 -4,784,335 | Flip: Primary Flip: 222.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 515 / LOW 26 / INVALID 127
结构观察区: Primary Flip 222.28（全链重定价，覆盖 100%）
最近结构参考: Flip 222（现价高于该位 4.3%）
量化视角： 正 Gamma（566万，无历史分位）｜正 Gamma 减弱（478万）｜现价位于 Flip 上方 4.32%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 222（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 235.0C — Vol 1,948 | 最新价 $7.20 | OI 4953→7124 (ΔOI +2171张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2171张（+43.8% vs前日OI），连续性待观察（方向未知）
10-02 220.0P — Vol 1,471 | 最新价 $3.59 | OI 2762→4078 (ΔOI +1316张) | ΔOI/Volume 89.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1316张（+47.6% vs前日OI），连续性待观察（方向未知）
10-02 250.0C — Vol 5,810 | 最新价 $2.69 | OI 2694→3628 (ΔOI +934张) | ΔOI/Volume 16.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增934张（+34.7% vs前日OI），连续性待观察（方向未知）
10-16 250.0C — Vol 3,284 | 最新价 $9.70 | OI 2894→3779 (ΔOI +885张) | ΔOI/Volume 26.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增885张（+30.6% vs前日OI），连续性待观察（方向未知）
10-16 110.0P — Vol 1,521（Yahoo补） | 最新价 $0.06 | OI 1654→2487 (ΔOI +833张) | ΔOI/Volume 54.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增833张（+50.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,139 张（Put 2,149 / Call 3,990），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +8.2k / P +8.4k ｜ Activity HIGH ｜ 4D
10-09  C +1.6k / P +2.1k ｜ Activity HIGH ｜ 11D
10-16  C +2.6k / P +2.5k ｜ Activity HIGH ｜ 18D
10-23  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 48.3k / P 34.9k，今日变化ΔOI: C +8.2k / P +8.4k，平值价格ATM: C $8.20 / P $8.74 ｜ ATM IV 87.1%，净 delta 敞口 17k shares
Top ΔOI: C 235 +2,171 ｜ P 220 +1,316 ｜ C 250 +934
仓位参考: Max Pain 230 ｜ Call Wall 235（+1.3%）（OI 7.1k） ｜ Put Wall 220（-5.1%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 87.1%｜历史 Rank 19%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,957 股

📆 10-09 Forward Structure
存量OI: C 16.9k / P 13.9k，今日变化ΔOI: C +1.6k / P +2.1k，平值价格ATM: C $13.00 / P $12.75 ｜ ATM IV 78.9%，净 delta 敞口 -11k shares
Top ΔOI: C 275 +552 ｜ P 200 +512 ｜ P 205 +386
仓位参考: Max Pain 220 ｜ Call Wall 240（+3.5%，弱）（OI 2.1k） ｜ Put Wall 210（-9.4%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.9%｜历史 Rank 19%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,836 股

📆 10-16 Forward Structure
存量OI: C 65.3k / P 82.0k，今日变化ΔOI: C +2.6k / P +2.5k，平值价格ATM: C $16.12 / P $15.08 ｜ ATM IV 79.0%，净 delta 敞口 33k shares
Top ΔOI: C 250 +885 ｜ C 240 +414
仓位参考: Max Pain 220 ｜ Call Wall 240（+3.5%，弱）（OI 4.7k） ｜ Put Wall 210（-9.4%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.0%｜历史 Rank 19%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,107 股

📆 10-23 Forward Structure
存量OI: C 4.9k / P 9.0k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $21.50 / P $17.35 ｜ ATM IV 78.2%，净 delta 敞口 -11k shares
Top ΔOI: P 210 +130 ｜ P 200 +88
仓位参考: Max Pain 230 ｜ Call Wall 240（+3.5%，弱）（OI 0.4k） ｜ Put Wall 210（-9.4%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 78.2%｜历史 Rank 19%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 负 11,393 股

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 87.1% vs 10-09 78.9%（差 +8.3pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/NBIS_evening.json