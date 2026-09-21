# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 140C ΔOI +457（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 136.82 → 收盘 137.68（+0.6%） ｜ 今日高 140.16 ｜ 低 135.62 ｜ 昨收 135.47 → 收盘 137.68（+1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.38 | OI比 0.69 | ATM IV 58.2% | Skew -1.5pp | Term 0.98 | ExpMove ±5.0%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±5.0% ｜ 10-02（11D）±7.8% ｜ 10-09（18D）±9.4% ｜ 10-16（25D）±11.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,736,451 | GEX Change vs 上次快照 -1,119,175 | Flip: Primary Flip: 129.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 576 / LOW 27 / INVALID 123
结构观察区: Primary Flip 129.76（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 8.2%）
最近结构参考: Flip 130（现价高于该位 6.1%）
量化视角： 正 Gamma（974万，无历史分位）｜正 Gamma 减弱（112万）｜现价位于 Flip 上方 6.10%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 130（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 150.0C — Vol 2,454 | 最新价 $3.45 | OI 9977→10701 (ΔOI +724张) | ΔOI/Volume 29.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增724张（+7.3% vs前日OI），连续性待观察（方向未知）
10-09 150.0C — Vol 203 | 最新价 $2.46 | OI 333→931 (ΔOI +598张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增598张（+179.6% vs前日OI），连续性待观察（方向未知）
09-25 125.0P — Vol 355 | 最新价 $0.25 | OI 401→955 (ΔOI +554张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增554张（+138.2% vs前日OI），连续性待观察（方向未知）
09-25 140.0C — Vol 3,312 | 最新价 $2.50 | OI 965→1422 (ΔOI +457张) | ΔOI/Volume 13.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增457张（+47.4% vs前日OI），连续性待观察（方向未知）
09-25 135.0P — Vol 598 | 最新价 $2.08 | OI 539→989 (ΔOI +450张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增450张（+83.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,783 张（Put 1,004 / Call 1,779），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +3.2k / P +3.3k ｜ Activity HIGH ｜ 4D
10-02  C +0.9k / P +0.9k ｜ Activity HIGH ｜ 11D
10-09  C +1.2k / P +0.2k ｜ Activity HIGH ｜ 18D
10-16  C +1.5k / P -0.7k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 24.6k / P 16.9k，今日变化ΔOI: C +3.2k / P +3.3k，平值价格ATM: C $3.30 / P $3.55 ｜ ATM IV 58.2%，净 delta 敞口 44k shares
Top ΔOI: P 125 +554 ｜ C 140 +457 ｜ P 135 +450
仓位参考: Max Pain 136 ｜ Call Wall 150（+8.9%，弱）（OI 5.1k） ｜ Put Wall 130（-5.6%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.2%｜历史 Rank 32%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 43,905 股

📆 10-02 Forward Structure
存量OI: C 10.9k / P 10.2k，今日变化ΔOI: C +0.9k / P +0.9k，平值价格ATM: C $5.25 / P $5.45 ｜ ATM IV 54.5%，净 delta 敞口 21k shares
Top ΔOI: P 127 +220
仓位参考: Max Pain 132 ｜ Call Wall 150（+8.9%）（OI 1.9k） ｜ Put Wall 130（-5.6%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜ATM IV 54.5%｜历史 Rank 32%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 20,948 股

📆 10-09 Forward Structure
存量OI: C 4.2k / P 4.6k，今日变化ΔOI: C +1.2k / P +0.2k，平值价格ATM: C $6.25 / P $6.65 ｜ ATM IV 53.6%，净 delta 敞口 49k shares
Top ΔOI: C 150 +598 ｜ C 136 +279
仓位参考: Max Pain 137 ｜ Call Wall 150（+8.9%）（OI 0.9k） ｜ Put Wall 140（+1.7%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.6%｜历史 Rank 32%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,942 股

📆 10-16 Forward Structure
存量OI: C 65.7k / P 52.5k，今日变化ΔOI: C +1.5k / P -0.7k，平值价格ATM: C $7.75 / P $7.65 ｜ ATM IV 53.1%，净 delta 敞口 81k shares
Top ΔOI: C 150 +724 ｜ P 135 -593
仓位参考: Max Pain 125 ｜ Call Wall 150（+8.9%）（OI 10.7k） ｜ Put Wall 130（-5.6%，弱）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 53.1%｜历史 Rank 32%（近端代理）｜净 delta 敞口 正 81,043 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/NOW_evening.json