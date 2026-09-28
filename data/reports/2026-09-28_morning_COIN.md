# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $765.39 ｜ QQQ $736.53
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
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
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-02 202C ΔOI +15,201（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 202C ΔOI +15,201 占该期限总 OI 14.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 195.11 → 今开 196.00（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 198.78 ｜ 低 193.00

Options: P/C成交量 0.27 | OI比 0.61 | ATM IV 70.7% | Skew -5.6pp | Term 0.95 | ExpMove ±6.1%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -5.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±6.1% ｜ 10-09（11D）±9.5% ｜ 10-16（18D）±11.6% ｜ 10-23（25D）±13.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,372,473 | GEX Change vs 上次快照 14,774,296 | Flip: Primary Flip: 176.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 497 / LOW 122 / INVALID 253
结构观察区: Primary Flip 176.47（全链重定价，覆盖 100%）
Call Wall 202（弱结构｜现价低于该位 3.4%）
最近结构参考: Call Wall 202（现价低于该位 3.4%）
量化视角： 正 Gamma（2237万，无历史分位）｜正 Gamma 增强（+1477万）｜现价位于 Flip 上方 10.80%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考）；上方 202（Call Wall，弱结构）。
• Gamma 区域：切换参考 176（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 202.5C — Vol 16,294 | 最新价 $3.73 | OI 461→15662 (ΔOI +15201张) | ΔOI/Volume 93.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15201张（+3297.4% vs前日OI），连续性待观察（方向未知）
10-02 212.5C — Vol 11,978 | 最新价 $1.70 | OI 1300→12409 (ΔOI +11109张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11109张（+854.5% vs前日OI），连续性待观察（方向未知）
10-02 210.0C — Vol 8,065 | 最新价 $2.09 | OI 1611→6215 (ΔOI +4604张) | ΔOI/Volume 57.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4604张（+285.8% vs前日OI），连续性待观察（方向未知）
10-09 100.0P — Vol 5,557 | 最新价 $0.04 | OI 361→3423 (ΔOI +3062张) | ΔOI/Volume 55.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3062张（+848.2% vs前日OI），连续性待观察（方向未知）
10-02 205.0C — Vol 3,130 | 最新价 $3.07 | OI 892→2956 (ΔOI +2064张) | ΔOI/Volume 65.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2064张（+231.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,040 张（Put 3,062 / Call 32,978），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +38.2k / P +4.8k ｜ Activity HIGH ｜ 4D
10-09  C +1.1k / P +5.7k ｜ Activity HIGH ｜ 11D
10-16  C +2.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 18D
10-23  C +0.3k / P +0.6k ｜ Activity MEDIUM △ ｜ 25D

📆 10-02 Forward Structure
存量OI: C 65.8k / P 40.4k，今日变化ΔOI: C +38.2k / P +4.8k，平值价格ATM: C $6.50 / P $5.40 ｜ ATM IV 70.7%，净 delta 敞口 986k shares
Top ΔOI: C 202 +15,201 ｜ C 212 +11,109 ｜ C 210 +4,604
仓位参考: Max Pain 190 ｜ Call Wall 202.5（+3.6%，弱）（OI 15.7k） ｜ Put Wall 190（-2.8%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 70.7%｜历史 Rank 34%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 985,916 股

📆 10-09 Forward Structure
存量OI: C 7.6k / P 19.9k，今日变化ΔOI: C +1.1k / P +5.7k，平值价格ATM: C $10.00 / P $8.65 ｜ ATM IV 64.2%，净 delta 敞口 24k shares
仓位参考: Max Pain 188 ｜ Call Wall 200（+2.3%）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 64.2%｜历史 Rank 34%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,099 股

10-16（MEDIUM △）Top ΔOI: 212C +834 ｜ 205C +421
10-16（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+2.3%，弱）（OI 6.1k） ｜ Put Wall 200（+2.3%，弱）（OI 3.9k）

10-23（MEDIUM △）Top ΔOI: 205P +220 ｜ 190C +178
10-23（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 190（-2.8%，弱）（OI 0.3k） ｜ Put Wall 190（-2.8%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 70.7% vs 10-09 64.2%（差 +6.6pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/COIN_morning.json