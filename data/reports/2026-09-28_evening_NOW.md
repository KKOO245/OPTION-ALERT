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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 131P ΔOI +507（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 150C ΔOI +2,190 占该期限总 OI 11.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 129.80 → 收盘 131.45（+1.3%） ｜ 今日高 131.89 ｜ 低 126.76 ｜ 昨收 135.62 → 收盘 131.45（-3.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.95 | OI比 0.79 | ATM IV 59.4% | Skew 1.0pp | Term 1.00 | ExpMove ±5.1%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 1.00）｜保护溢价薄（Skew 1.0pp）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±5.1% ｜ 10-09（11D）±7.3% ｜ 10-16（18D）±9.3% ｜ 10-23（25D）±11.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 819,863 | GEX Change vs 上次快照 1,175,035 | Flip: Primary Flip: 130.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 547 / LOW 26 / INVALID 117
结构观察区: Primary Flip 130.94（全链重定价，覆盖 100%）
Put Wall 120（弱结构｜现价高于该位 9.5%）
最近结构参考: Flip 131（现价高于该位 0.4%）
量化视角： 正 Gamma（82万，无历史分位）｜由负转正（+118万）｜现价位于 Flip 上方 0.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（Put Wall，弱结构）；上方 135（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 150.0C — Vol 2,596 | 最新价 $0.53 | OI 2600→4790 (ΔOI +2190张) | ΔOI/Volume 84.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2190张（+84.2% vs前日OI），连续性待观察（方向未知）
10-02 140.0C — Vol 2,451 | 最新价 $0.70 | OI 1174→2723 (ΔOI +1549张) | ΔOI/Volume 63.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1549张（+131.9% vs前日OI），连续性待观察（方向未知）
10-16 150.0C — Vol 2,351 | 最新价 $1.10 | OI 12526→13962 (ΔOI +1436张) | ΔOI/Volume 61.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1436张（+11.5% vs前日OI），连续性待观察（方向未知）
10-16 132.0P — Vol 10 | 最新价 $6.45 | OI 72→853 (ΔOI +781张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增781张（+1084.7% vs前日OI），连续性待观察（方向未知）
10-09 131.0P — Vol 26 | 最新价 $4.55 | OI 76→583 (ΔOI +507张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增507张（+667.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,463 张（Put 1,288 / Call 5,175），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +5.4k / P +2.3k ｜ Activity HIGH ｜ 4D
10-09  C +2.6k / P +1.2k ｜ Activity HIGH ｜ 11D
10-16  C +2.2k / P +2.6k ｜ Activity HIGH ｜ 18D
10-23  C +0.6k / P +0.7k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 24.7k / P 19.4k，今日变化ΔOI: C +5.4k / P +2.3k，平值价格ATM: C $3.56 / P $3.15 ｜ ATM IV 59.5%，净 delta 敞口 -56k shares
Top ΔOI: C 140 +1,549
仓位参考: Max Pain 135 ｜ Call Wall 140（+6.5%，弱）（OI 2.7k） ｜ Put Wall 120（-8.7%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 59.5%｜历史 Rank 48%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 56,261 股

📆 10-09 Forward Structure
存量OI: C 11.3k / P 8.4k，今日变化ΔOI: C +2.6k / P +1.2k，平值价格ATM: C $5.05 / P $4.55 ｜ ATM IV 52.9%，净 delta 敞口 -15k shares
Top ΔOI: C 150 +2,190 ｜ P 131 +507
仓位参考: Max Pain 136 ｜ Put Wall 120（-8.7%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 52.9%｜历史 Rank 48%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 15,118 股

📆 10-16 Forward Structure
存量OI: C 74.4k / P 60.3k，今日变化ΔOI: C +2.2k / P +2.6k，平值价格ATM: C $6.44 / P $5.83 ｜ ATM IV 51.7%，净 delta 敞口 -72k shares
Top ΔOI: C 150 +1,436 ｜ P 132 +781 ｜ P 130 +504
仓位参考: Max Pain 130 ｜ Call Wall 140（+6.5%，弱）（OI 4.6k） ｜ Put Wall 120（-8.7%，弱）（OI 5.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.7%｜历史 Rank 48%（近端代理）｜IV/RV 1.10×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 71,824 股

📆 10-23 Forward Structure
存量OI: C 7.4k / P 9.5k，今日变化ΔOI: C +0.6k / P +0.7k，平值价格ATM: C $7.64 / P $7.20 ｜ ATM IV 54.9%，净 delta 敞口 -4k shares
Top ΔOI: C 136 +162 ｜ P 125 +125 ｜ P 145 +117
仓位参考: Max Pain 135 ｜ Call Wall 140（+6.5%，弱）（OI 1.0k） ｜ Put Wall 122（-7.2%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 54.9%｜历史 Rank 48%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 3,849 股

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 59.5% vs 10-09 52.9%（差 +6.6pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/NOW_evening.json