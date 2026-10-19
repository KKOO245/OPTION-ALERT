# 期权晚报 2026-10-19（快照 16:40 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-23 13C ΔOI +44（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 12P ΔOI +231 占该期限总 OI 21.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 13.26 → 收盘 13.01（-1.9%） ｜ 今日高 13.32 ｜ 低 12.77 ｜ 昨收 12.88 → 收盘 13.01（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.08 | OI比 0.29 | ATM IV 87.3% | Skew 13.9pp | Term 0.89 | ExpMove ±7.1%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 13.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.29）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.08×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.29×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±7.1% ｜ 10-30（11D）±11.4% ｜ 11-06（18D）±14.6% ｜ 11-13（25D）±17.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 407,541 | GEX Change vs 上次快照 148,238 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 138 / LOW 78 / INVALID 182
结构观察区: NO_CROSS
Put Wall 14（现价低于该位 7.1%）
最近结构参考: Put Wall 14（现价低于该位 7.1%）
量化视角： 正 Gamma（41万，无历史分位）｜正 Gamma 增强（+15万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 16（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 12.5P — Vol 125（Yahoo补） | 最新价 $0.90 | OI 1→232 (ΔOI +231张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增231张（+23100.0% vs前日OI），值得跟踪（方向未知）
10-23 13.5C — Vol 83 | 最新价 $0.21 | OI 168→212 (ΔOI +44张) | ΔOI/Volume 53.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44张（+26.2% vs前日OI），连续性待观察（方向未知）
11-06 15.0P — Vol 69（Yahoo补） | 最新价 $2.15 | OI 26→59 (ΔOI +33张) | ΔOI/Volume 47.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33张（+126.9% vs前日OI），连续性待观察（方向未知）
10-30 12.0P — Vol 1（Yahoo补） | 最新价 $0.23 | OI 71→99 (ΔOI +28张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增28张（+39.4% vs前日OI），值得跟踪（方向未知）
11-06 14.5P — Vol 80（Yahoo补） | 最新价 $1.95 | OI 16→44 (ΔOI +28张) | ΔOI/Volume 35.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28张（+175.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 364 张（Put 320 / Call 44），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.1k / P -84 ｜ Activity MEDIUM △ ｜ 4D
10-30  C +32 / P +43 ｜ Activity MEDIUM △ ｜ 11D
11-06  C +6 / P +68 ｜ Activity HIGH ｜ 18D
11-13  C +0 / P +0.3k ｜ Activity MEDIUM △ ｜ 25D

📆 10-23 Forward Structure
存量OI: C 5.8k / P 1.7k，今日变化ΔOI: C +0.1k / P -84，平值价格ATM: C $0.45 / P $0.47 ｜ ATM IV 87.3%，净 delta 敞口 15k shares
Top ΔOI: C 13 +44
仓位参考: Max Pain 16 ｜ Put Wall 14（+7.6%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 87.3%｜历史 Rank 21%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,898 股

10-30（MEDIUM △）Top ΔOI: 12P +28
10-30（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 14（+7.6%）（OI 0.4k）

📆 11-06 Forward Structure
存量OI: C 1.5k / P 0.5k，今日变化ΔOI: C +6 / P +68，平值价格ATM: C $1.03 / P $0.87 ｜ ATM IV 76.8%，净 delta 敞口 -5k shares
Top ΔOI: P 12 +5
仓位参考: Max Pain 16 ｜ Put Wall 13（-0.1%，弱）（OI 76）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.8%｜历史 Rank 21%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 负 4,646 股

11-13（MEDIUM △）Top ΔOI: 12P +231 ｜ 14P +9
11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+3.8%，弱）（OI 50） ｜ Put Wall 12.5（-3.9%）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 87.3% vs 10-30 78.4%（差 +8.8pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/NNE_evening.json