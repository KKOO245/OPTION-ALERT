# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $767.62 ｜ QQQ $737.25
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
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-02 16P ΔOI +212（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 20C ΔOI +3,500 占该期限总 OI 66.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 16.99 → 今开 16.70（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 16.85 ｜ 低 16.48

Options: P/C成交量 0.88 | OI比 0.42 | ATM IV 73.6% | Skew -0.1pp | Term 1.06 | ExpMove ±8.2%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 1.06）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±8.2% ｜ 10-09（11D）±10.9% ｜ 10-16（18D）±14.2% ｜ 10-23（25D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,103,816 | GEX Change vs 上次快照 -573,642 | Flip: Primary Flip: 15.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 207 / LOW 74 / INVALID 155
结构观察区: Primary Flip 15.50（全链重定价，覆盖 98%）
Put Wall 15（弱结构｜现价高于该位 10.3%）
最近结构参考: Flip 16（现价高于该位 6.8%）
量化视角： 正 Gamma（110万，无历史分位）｜正 Gamma 减弱（57万）｜现价位于 Flip 上方 6.77%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 20.5C — Vol 3,540 | 最新价 $0.30 | OI 50→3550 (ΔOI +3500张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3500张（+7000.0% vs前日OI），连续性待观察（方向未知）
10-02 16.5P — Vol 254 | 最新价 $0.45 | OI 78→290 (ΔOI +212张) | ΔOI/Volume 83.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增212张（+271.8% vs前日OI），连续性待观察（方向未知）
10-09 17.5P — Vol 182 | 最新价 $1.10 | OI 57→239 (ΔOI +182张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增182张（+319.3% vs前日OI），连续性待观察（方向未知）
10-02 17.0P — Vol 176 | 最新价 $0.71 | OI 87→240 (ΔOI +153张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增153张（+175.9% vs前日OI），连续性待观察（方向未知）
10-23 16.0P — Vol 122 | 最新价 $0.77 | OI 29→151 (ΔOI +122张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增122张（+420.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,169 张（Put 669 / Call 3,500），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 4D
10-09  C +0.1k / P +0.3k ｜ Activity HIGH ｜ 11D
10-16  C +0.2k / P -0.3k ｜ Activity MEDIUM △ ｜ 18D
10-23  C +3.5k / P +0.2k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 4.6k / P 1.9k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $0.90 / P $0.45 ｜ ATM IV 73.6%，净 delta 敞口 -4k shares
Top ΔOI: P 16 +212 ｜ P 17 +153
仓位参考: Max Pain 18 ｜ Call Wall 18（+8.8%，弱）（OI 0.5k） ｜ Put Wall 16.5（-0.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.6%｜历史 Rank 3%（近端代理）｜IV/RV 1.03×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 3,686 股

📆 10-09 Forward Structure
存量OI: C 5.0k / P 1.1k，今日变化ΔOI: C +0.1k / P +0.3k，平值价格ATM: C $1.00 / P $0.81 ｜ ATM IV 69.0%，净 delta 敞口 -11k shares
Top ΔOI: P 17 +182 ｜ P 16 +111
仓位参考: Max Pain 18 ｜ Put Wall 17.5（+5.7%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.0%｜历史 Rank 3%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 11,423 股

10-16（MEDIUM △）Top ΔOI: 29P -203
10-16（MEDIUM △）仓位参考: Max Pain 20 ｜ Put Wall 15（-9.4%，弱）（OI 0.8k）

📆 10-23 Forward Structure
存量OI: C 4.7k / P 0.6k，今日变化ΔOI: C +3.5k / P +0.2k，平值价格ATM: C $1.40 / P $1.25 ｜ ATM IV 87.2%，净 delta 敞口 75k shares
Top ΔOI: C 20 +3,500 ｜ P 16 +122
仓位参考: Max Pain 18 ｜ Put Wall 16（-3.3%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 87.2%｜历史 Rank 3%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 正 75,095 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/NNE_morning.json