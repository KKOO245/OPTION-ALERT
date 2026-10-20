# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 12P ΔOI +5（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 12P ΔOI +231 占该期限总 OI 21.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 12.88 → 今开 13.26（+3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 13.32 ｜ 低 12.77

Options: P/C成交量 1.00 | OI比 0.29 | ATM IV 73.0% | Skew -3.3pp | Term 1.01 | ExpMove ±8.2%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -3.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.29）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.29×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±8.2% ｜ 10-30（11D）±11.5% ｜ 11-06（18D）±14.9% ｜ 11-13（25D）±18.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 259,304 | GEX Change vs 上次快照 -43,474 | Flip: Primary Flip: 11.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 137 / LOW 76 / INVALID 185
结构观察区: Primary Flip 11.50（全链重定价，覆盖 97%）
Put Wall 14（现价低于该位 8.6%）
最近结构参考: Put Wall 14（现价低于该位 8.6%）
量化视角： 正 Gamma（26万，无历史分位）｜正 Gamma 减弱（4万）｜现价位于 Flip 上方 11.22%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 12.5P — Vol 240 | 最新价 $0.90 | OI 1→232 (ΔOI +231张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增231张（+23100.0% vs前日OI），连续性待观察（方向未知）
10-23 13.5C — Vol 62 | 最新价 $0.26 | OI 168→212 (ΔOI +44张) | ΔOI/Volume 71.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44张（+26.2% vs前日OI），连续性待观察（方向未知）
11-06 15.0P — Vol 69 | 最新价 $2.15 | OI 26→59 (ΔOI +33张) | ΔOI/Volume 47.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33张（+126.9% vs前日OI），连续性待观察（方向未知）
10-30 12.0P — Vol 28 | 最新价 $0.23 | OI 71→99 (ΔOI +28张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28张（+39.4% vs前日OI），连续性待观察（方向未知）
11-06 14.5P — Vol 80 | 最新价 $1.95 | OI 16→44 (ΔOI +28张) | ΔOI/Volume 35.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28张（+175.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 364 张（Put 320 / Call 44），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.1k / P -84 ｜ Activity MEDIUM △ ｜ 4D
10-30  C +32 / P +43 ｜ Activity MEDIUM △ ｜ 11D
11-06  C +6 / P +68 ｜ Activity HIGH ｜ 18D
11-13  C +0 / P +0.3k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 5.8k / P 1.7k，今日变化ΔOI: C +0.1k / P -84，平值价格ATM: C $0.45 / P $0.60 ｜ ATM IV 73.0%，净 delta 敞口 15k shares
Top ΔOI: C 13 +44
仓位参考: Max Pain 16 ｜ Put Wall 14（+9.5%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 73.0%｜历史 Rank 4%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 14,966 股

10-30（MEDIUM △）Top ΔOI: 12P +28
10-30（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 14（+9.5%）（OI 0.4k）

📆 11-06 Forward Structure
存量OI: C 1.5k / P 0.5k，今日变化ΔOI: C +6 / P +68，平值价格ATM: C $1.03 / P $0.87 ｜ ATM IV 73.5%，净 delta 敞口 -5k shares
Top ΔOI: P 12 +5
仓位参考: Max Pain 16 ｜ Put Wall 13（+1.6%，弱）（OI 76）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.5%｜历史 Rank 4%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 负 4,578 股

📆 11-13 Forward Structure
存量OI: C 0.6k / P 0.5k，今日变化ΔOI: C +0 / P +0.3k，平值价格ATM: C $1.28 / P $1.05 ｜ ATM IV 75.2%，净 delta 敞口 -11k shares
Top ΔOI: P 12 +231 ｜ P 14 +9 ｜ P 13 +8
仓位参考: Max Pain 14 ｜ Call Wall 13.5（+5.6%，弱）（OI 50） ｜ Put Wall 12.5（-2.3%）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 75.2%｜历史 Rank 4%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 负 10,975 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/NNE_morning.json