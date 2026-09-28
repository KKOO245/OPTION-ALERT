# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $767.62 ｜ QQQ $737.20
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.8（fear）
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-02 150C ΔOI +5,688（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 148.68 → 今开 148.50（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 150.80 ｜ 低 145.66

Options: P/C成交量 0.43 | OI比 1.18 | ATM IV 54.0% | Skew -1.0pp | Term 0.86 | ExpMove ±4.6%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.18×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（4D）±4.6% ｜ 10-09（11D）±6.7% ｜ 10-16（18D）±8.3% ｜ 10-23（25D）±10.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 7,077,727 | GEX Change vs 上次快照 -5,705,359 | Flip: Primary Flip: 147.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 528 / LOW 81 / INVALID 309
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.61（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 7.2%）
最近结构参考: Flip 148（现价高于该位 0.5%）
量化视角： 正 Gamma（708万，无历史分位）｜正 Gamma 减弱（571万）｜现价位于 Flip 上方 0.55%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 149（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 140.0P — Vol 11,169 | 最新价 $0.85 | OI 6910→13443 (ΔOI +6533张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6533张（+94.5% vs前日OI），连续性待观察（方向未知）
10-02 150.0C — Vol 18,671 | 最新价 $3.06 | OI 9165→14853 (ΔOI +5688张) | ΔOI/Volume 30.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5688张（+62.1% vs前日OI），连续性待观察（方向未知）
10-02 120.0P — Vol 7,068 | 最新价 $0.04 | OI 2353→7243 (ΔOI +4890张) | ΔOI/Volume 69.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4890张（+207.8% vs前日OI），连续性待观察（方向未知）
10-02 90.0P — Vol 4,818 | 最新价 $0.01 | OI 10491→14878 (ΔOI +4387张) | ΔOI/Volume 91.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4387张（+41.8% vs前日OI），连续性待观察（方向未知）
10-02 144.0P — Vol 5,739 | 最新价 $1.78 | OI 1651→5474 (ΔOI +3823张) | ΔOI/Volume 66.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3823张（+231.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 25,321 张（Put 19,633 / Call 5,688），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +27.4k / P +50.0k ｜ Activity HIGH ｜ 4D
10-09  C +6.4k / P +4.1k ｜ Activity HIGH ｜ 11D
10-16  C +1.5k / P +4.9k ｜ Activity MEDIUM △ ｜ 18D
10-23  C +1.9k / P +2.0k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 136.8k / P 161.5k，今日变化ΔOI: C +27.4k / P +50.0k，平值价格ATM: C $3.30 / P $3.59 ｜ ATM IV 54.0%，净 delta 敞口 -186k shares
Top ΔOI: P 140 +6,533 ｜ C 150 +5,688
仓位参考: Max Pain 149 ｜ Call Wall 150（+1.1%，弱）（OI 14.9k） ｜ Put Wall 140（-5.7%，弱）（OI 13.4k）
量化解读： 存量 Put 重｜ATM IV 54.0%｜历史 Rank 35%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 186,132 股

📆 10-09 Forward Structure
存量OI: C 49.9k / P 39.5k，今日变化ΔOI: C +6.4k / P +4.1k，平值价格ATM: C $4.90 / P $5.10 ｜ ATM IV 48.2%，净 delta 敞口 54k shares
Top ΔOI: P 143 +984 ｜ C 160 +803 ｜ C 145 +756
仓位参考: Max Pain 149 ｜ Call Wall 155（+4.4%，弱）（OI 4.7k） ｜ Put Wall 135（-9.0%）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 48.2%｜历史 Rank 35%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,990 股

10-16（MEDIUM △）Top ΔOI: 150P +2,521 ｜ 135P +1,262
10-16（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 160（+7.8%，弱）（OI 35.4k） ｜ Put Wall 135（-9.0%，弱）（OI 30.2k）

📆 10-23 Forward Structure
存量OI: C 23.6k / P 19.7k，今日变化ΔOI: C +1.9k / P +2.0k，平值价格ATM: C $8.65 / P $7.20 ｜ ATM IV 46.3%，净 delta 敞口 -8k shares
Top ΔOI: P 140 +377
仓位参考: Max Pain 149 ｜ Call Wall 150（+1.1%，弱）（OI 3.0k） ｜ Put Wall 135（-9.0%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.3%｜历史 Rank 35%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 7,816 股

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 54.0% vs 10-09 48.2%（差 +5.8pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/SPCX_morning.json