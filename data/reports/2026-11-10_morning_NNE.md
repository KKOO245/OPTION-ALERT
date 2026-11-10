# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.55
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 12C ΔOI +239（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 14C ΔOI +199 占该期限总 OI 21.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 12.48 → 今开 11.96（-4.2%） | 较昨收变动（含盘初走势） ｜ 今日高 12.35 ｜ 低 11.75

Options: P/C成交量 0.35 | OI比 0.40 | ATM IV 91.5% | Skew 14.9pp | Term 0.91 | ExpMove ±10.4%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 14.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±10.4% ｜ 11-20（10D）±14.1% ｜ 11-27（17D）±14.4% ｜ 12-04（24D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,860,002 | GEX Change vs 上次快照 415,618 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 180 / LOW 66 / INVALID 140
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 10.0%） | Call Wall 12（现价低于该位 3.2%）
最近结构参考: Call Wall 12（现价低于该位 3.2%）
量化视角： 正 Gamma（186万，无历史分位）｜正 Gamma 增强（+42万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall） / 12（MaxPain，仅结算参考）；上方 12（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 13.5C — Vol 602 | 最新价 $0.35 | OI 37→571 (ΔOI +534张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增534张（+1443.2% vs前日OI），连续性待观察（方向未知）
11-13 13.0C — Vol 634 | 最新价 $0.29 | OI 71→470 (ΔOI +399张) | ΔOI/Volume 62.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增399张（+562.0% vs前日OI），连续性待观察（方向未知）
11-13 14.0C — Vol 293 | 最新价 $0.10 | OI 150→422 (ΔOI +272张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增272张（+181.3% vs前日OI），连续性待观察（方向未知）
11-13 12.5C — Vol 611 | 最新价 $0.60 | OI 110→349 (ΔOI +239张) | ΔOI/Volume 39.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增239张（+217.3% vs前日OI），连续性待观察（方向未知）
12-04 14.0C — Vol 202 | 最新价 $0.42 | OI 14→213 (ΔOI +199张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增199张（+1421.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,643 张（Put 0 / Call 1,643），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +1.2k / P -0.2k ｜ Activity HIGH ｜ 3D
11-20  C +0.9k / P +0.4k ｜ Activity HIGH ｜ 10D
11-27  C +0.3k / P +7 ｜ Activity HIGH ｜ 17D
12-04  C +0.3k / P +22 ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 2.9k / P 1.2k，今日变化ΔOI: C +1.2k / P -0.2k，平值价格ATM: C $1.00 / P $0.26 ｜ ATM IV 91.5%，净 delta 敞口 32k shares
Top ΔOI: C 13 +399 ｜ C 12 +239
仓位参考: Max Pain 12 ｜ Call Wall 13（+7.4%，弱）（OI 0.5k） ｜ Put Wall 11（-9.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 91.5%｜历史 Rank 29%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 31,797 股

📆 11-20 Forward Structure
存量OI: C 6.1k / P 2.3k，今日变化ΔOI: C +0.9k / P +0.4k，平值价格ATM: C $1.25 / P $0.45 ｜ ATM IV 85.8%，净 delta 敞口 19k shares
Top ΔOI: P 11 +179
仓位参考: Max Pain 12 ｜ Call Wall 12（-0.8%，弱）（OI 0.7k） ｜ Put Wall 11（-9.1%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 85.8%｜历史 Rank 29%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,602 股

📆 11-27 Forward Structure
存量OI: C 4.8k / P 0.7k，今日变化ΔOI: C +0.3k / P +7，平值价格ATM: C $1.00 / P $0.74 ｜ ATM IV 85.2%，净 delta 敞口 9k shares
Top ΔOI: C 13 +26
仓位参考: Max Pain 12 ｜ Call Wall 12.5（+3.3%）（OI 4.0k） ｜ Put Wall 12.5（+3.3%）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 85.2%｜历史 Rank 29%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,871 股

📆 12-04 Forward Structure
存量OI: C 0.5k / P 0.4k，今日变化ΔOI: C +0.3k / P +22，平值价格ATM: C $0.83 / P $0.77 ｜ ATM IV 78.9%，净 delta 敞口 9k shares
Top ΔOI: C 12 +33 ｜ P 12 +18
仓位参考: Max Pain 13 ｜ Call Wall 12.5（+3.3%，弱）（OI 48）
量化解读： 存量 Call 重｜ATM IV 78.9%｜历史 Rank 29%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 正 9,021 股

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 91.5% vs 11-20 85.8%（差 +5.7pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/NNE_morning.json