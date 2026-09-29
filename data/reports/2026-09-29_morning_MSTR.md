# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.86 ｜ QQQ $738.95
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
🟡 **事件差分**: 10-02 ATM IV 78.6% vs 10-09 67.1%（差 +11.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 160C ΔOI +1,928（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 157.14 → 今开 161.45（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 161.62 ｜ 低 155.50

Options: P/C成交量 0.66 | OI比 0.82 | ATM IV 78.6% | Skew -6.8pp | Term 0.86 | ExpMove ±6.0%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（3D）±6.0% ｜ 10-09（10D）±9.2% ｜ 10-16（17D）±11.5% ｜ 10-23（24D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 49,876,935 | GEX Change vs 上次快照 -2,595,802 | Flip: Primary Flip: 145.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 806 / LOW 52 / INVALID 184
结构观察区: Primary Flip 145.14（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 145（现价高于该位 7.8%）
量化视角： 正 Gamma（4988万，无历史分位）｜正 Gamma 减弱（260万）｜现价位于 Flip 上方 7.82%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 145（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 160.0C — Vol 10,952 | 最新价 $3.73 | OI 3221→5149 (ΔOI +1928张) | ΔOI/Volume 17.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1928张（+59.9% vs前日OI），连续性待观察（方向未知）
10-02 165.0C — Vol 7,025 | 最新价 $2.29 | OI 30103→31933 (ΔOI +1830张) | ΔOI/Volume 26.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1830张（+6.1% vs前日OI），连续性待观察（方向未知）
10-02 90.0P — Vol 1,864 | 最新价 $0.01 | OI 16609→18107 (ΔOI +1498张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1498张（+9.0% vs前日OI），连续性待观察（方向未知）
10-02 157.5P — Vol 5,242 | 最新价 $5.00 | OI 1318→2413 (ΔOI +1095张) | ΔOI/Volume 20.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1095张（+83.1% vs前日OI），连续性待观察（方向未知）
10-02 155.0P — Vol 5,106 | 最新价 $3.80 | OI 6285→7228 (ΔOI +943张) | ΔOI/Volume 18.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增943张（+15.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,294 张（Put 3,536 / Call 3,758），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +9.5k / P +7.9k ｜ Activity HIGH ｜ 3D
10-09  C +0.4k / P +4.1k ｜ Activity MEDIUM △ ｜ 10D
10-16  C +1.0k / P +1.1k ｜ Activity HIGH ｜ 17D
10-23  C +1.6k / P +2.5k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 239.5k / P 195.5k，今日变化ΔOI: C +9.5k / P +7.9k，平值价格ATM: C $4.21 / P $5.10 ｜ ATM IV 78.6%，净 delta 敞口 30k shares
Top ΔOI: C 160 +1,928 ｜ C 165 +1,830
仓位参考: Max Pain 155 ｜ Call Wall 170（+8.6%，弱）（OI 44.9k） ｜ Put Wall 150（-4.2%，弱）（OI 12.4k）
量化解读： 存量 Call 重｜ATM IV 78.6%｜历史 Rank 46%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 30,045 股

10-09（MEDIUM △）Top ΔOI: 144C -2,619 ｜ 165C +852
10-09（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 165（+5.4%，弱）（OI 5.0k） ｜ Put Wall 155（-1.0%，弱）（OI 1.9k）

📆 10-16 Forward Structure
存量OI: C 172.9k / P 142.6k，今日变化ΔOI: C +1.0k / P +1.1k，平值价格ATM: C $9.20 / P $8.85 ｜ ATM IV 66.2%，净 delta 敞口 14k shares
Top ΔOI: C 200 -501 ｜ C 175 +454 ｜ C 160 +392
仓位参考: Max Pain 120 ｜ Call Wall 155（-1.0%，弱）（OI 10.4k） ｜ Put Wall 160（+2.2%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.2%｜历史 Rank 46%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,036 股

📆 10-23 Forward Structure
存量OI: C 15.9k / P 23.3k，今日变化ΔOI: C +1.6k / P +2.5k，平值价格ATM: C $11.10 / P $10.70 ｜ ATM IV 65.9%，净 delta 敞口 -12k shares
Top ΔOI: C 180 +482 ｜ C 170 +469
仓位参考: Max Pain 158 ｜ Call Wall 170（+8.6%，弱）（OI 1.5k） ｜ Put Wall 155（-1.0%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 65.9%｜历史 Rank 46%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 负 11,996 股

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 78.6% vs 10-09 67.1%（差 +11.5pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/MSTR_morning.json