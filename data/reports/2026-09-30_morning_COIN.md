# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
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
🟡 **事件差分**: 10-02 ATM IV 73.9% vs 10-09 62.9%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 180P ΔOI +2,479（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 190.02 → 今开 195.48（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 198.66 ｜ 低 186.38

Options: P/C成交量 0.17 | OI比 0.64 | ATM IV 73.9% | Skew -3.9pp | Term 0.87 | ExpMove ±4.9%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±4.9% ｜ 10-09（9D）±7.9% ｜ 10-16（16D）±10.4% ｜ 10-23（23D）±15.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,820,520 | GEX Change vs 上次快照 -2,931,185 | Flip: Primary Flip: 181.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 535 / LOW 127 / INVALID 222
结构观察区: Primary Flip 181.19（全链重定价，覆盖 100%）
Call Wall 202（弱结构｜现价低于该位 7.0%）
最近结构参考: Flip 181（现价高于该位 3.9%）
量化视角： 正 Gamma（1182万，无历史分位）｜正 Gamma 减弱（293万）｜现价位于 Flip 上方 3.89%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（MaxPain，仅结算参考） / 202（Call Wall，弱结构）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 180.0P — Vol 3,458 | 最新价 $1.36 | OI 1688→4167 (ΔOI +2479张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2479张（+146.9% vs前日OI），连续性待观察（方向未知）
10-02 200.0C — Vol 4,797 | 最新价 $1.83 | OI 2832→3665 (ΔOI +833张) | ΔOI/Volume 17.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增833张（+29.4% vs前日OI），连续性待观察（方向未知）
10-09 170.0P — Vol 428 | 最新价 $1.40 | OI 437→790 (ΔOI +353张) | ΔOI/Volume 82.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增353张（+80.8% vs前日OI），连续性待观察（方向未知）
10-02 190.0C — Vol 1,148 | 最新价 $5.10 | OI 943→1260 (ΔOI +317张) | ΔOI/Volume 27.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增317张（+33.6% vs前日OI），连续性待观察（方向未知）
10-02 205.0C — Vol 1,275 | 最新价 $1.06 | OI 3665→3980 (ΔOI +315张) | ΔOI/Volume 24.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增315张（+8.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,297 张（Put 2,832 / Call 1,465），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.6k / P +3.9k ｜ Activity MEDIUM △ ｜ 2D
10-09  C +1.4k / P +0.8k ｜ Activity HIGH ｜ 9D
10-16  C +1.3k / P -0.1k ｜ Activity HIGH ｜ 16D
10-23  C +0.7k / P +0.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 72.9k / P 46.8k，今日变化ΔOI: C +1.6k / P +3.9k，平值价格ATM: C $4.95 / P $4.26 ｜ ATM IV 73.9%，净 delta 敞口 22k shares
Top ΔOI: P 180 +2,479 ｜ C 200 +833
仓位参考: Max Pain 190 ｜ Call Wall 202.5（+7.6%，弱）（OI 15.9k） ｜ Put Wall 180（-4.4%，弱）（OI 4.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.9%｜历史 Rank 43%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 21,925 股

📆 10-09 Forward Structure
存量OI: C 10.1k / P 21.8k，今日变化ΔOI: C +1.4k / P +0.8k，平值价格ATM: C $8.00 / P $6.95 ｜ ATM IV 62.9%，净 delta 敞口 7k shares
Top ΔOI: P 170 +353
仓位参考: Max Pain 190 ｜ Call Wall 200（+6.3%）（OI 1.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.9%｜历史 Rank 43%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,788 股

📆 10-16 Forward Structure
存量OI: C 84.4k / P 74.4k，今日变化ΔOI: C +1.3k / P -0.1k，平值价格ATM: C $10.05 / P $9.49 ｜ ATM IV 62.2%，净 delta 敞口 28k shares
Top ΔOI: C 220 +306
仓位参考: Max Pain 175 ｜ Call Wall 200（+6.3%，弱）（OI 6.4k） ｜ Put Wall 200（+6.3%，弱）（OI 3.9k）
量化解读： 存量两侧均衡｜ATM IV 62.2%｜历史 Rank 43%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 27,621 股

10-23（MEDIUM △）Top ΔOI: 202C +228 ｜ 202P +219
10-23（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 190（+0.9%，弱）（OI 0.5k） ｜ Put Wall 192.5（+2.3%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 73.9% vs 10-09 62.9%（差 +11.0pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/COIN_morning.json