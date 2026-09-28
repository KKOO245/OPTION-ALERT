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
🟡 **近现价集中开仓**: 10-05 53P ΔOI +146（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 64C ΔOI +539 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 55.32 → 收盘 54.95（-0.7%） ｜ 今日高 55.83 ｜ 低 54.87 ｜ 昨收 58.14 → 收盘 54.95（-5.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-01，窗口结束前不做对错判定）

Options: P/C成交量 0.55 | OI比 0.65 | ATM IV 45.2% | Skew 22.5pp | Term 0.81 | ExpMove ±2.4%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 22.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（2D）±2.4% ｜ 10-02（4D）±3.5% ｜ 10-05（7D）±3.9% ｜ 10-07（9D）±4.4%
   ⇒ IV–VIX Spread: +29.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,840,160 | GEX Change vs 上次快照 -14,773,011 | Flip: Primary Flip: 55.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 675 / LOW 193 / INVALID 432
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 55.09（全链重定价，覆盖 93%）
Put Wall 50（弱结构｜现价高于该位 9.9%） | Call Wall 60（弱结构｜现价低于该位 8.4%）
最近结构参考: Flip 55（现价低于该位 0.3%）
量化视角： 负 Gamma（384万，无历史分位）｜由正转负（1477万）｜现价位于 Flip 下方 0.26%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 58（MaxPain，仅结算参考） / 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-07 57.0P — Vol 3,243 | 最新价 $2.53 | OI 248→4494 (ΔOI +4246张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4246张（+1712.1% vs前日OI），连续性待观察（方向未知）
09-30 61.0C — Vol 2,012 | 最新价 $0.01 | OI 1510→3042 (ΔOI +1532张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1532张（+101.5% vs前日OI），连续性待观察（方向未知）
量化视角： 2 个事件合计 ΔOI ≈ 5,778 张（Put 4,246 / Call 1,532），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-30  C +5.6k / P -0.9k ｜ Activity MEDIUM △ ｜ 2D
10-02  C +4.4k / P +4.3k ｜ Activity HIGH ｜ 4D
10-05  C +1.1k / P +0.4k ｜ Activity HIGH ｜ 7D
10-07  C +0.9k / P +4.7k ｜ Activity HIGH ｜ 9D

📆 09-30 Forward Structure
存量OI: C 300.0k / P 127.0k，今日变化ΔOI: C +5.6k / P -0.9k，平值价格ATM: C $0.63 / P $0.66 ｜ ATM IV 39.4%，净 delta 敞口 87k shares
Top ΔOI: C 58 +1,363
仓位参考: Max Pain 56 ｜ Call Wall 60（+9.2%，弱）（OI 6.6k） ｜ Put Wall 53（-3.5%）（OI 13.2k）
量化解读： 存量 Call 重｜ATM IV 39.4%｜历史 Rank 76%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 87,412 股

📆 10-02 Forward Structure
存量OI: C 80.3k / P 39.2k，今日变化ΔOI: C +4.4k / P +4.3k，平值价格ATM: C $0.96 / P $0.96 ｜ ATM IV 41.4%，净 delta 敞口 -228k shares
Top ΔOI: P 59 +586
仓位参考: Max Pain 58 ｜ Call Wall 60（+9.2%，弱）（OI 12.3k） ｜ Put Wall 50（-9.0%）（OI 7.2k）
量化解读： 存量 Call 重｜ATM IV 41.4%｜历史 Rank 76%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 228,474 股

📆 10-05 Forward Structure
存量OI: C 2.7k / P 2.5k，今日变化ΔOI: C +1.1k / P +0.4k，平值价格ATM: C $1.08 / P $1.07 ｜ ATM IV 35.5%，净 delta 敞口 -14k shares
Top ΔOI: P 53 +146 ｜ C 59 +141
仓位参考: Max Pain 60 ｜ Call Wall 59（+7.4%，弱）（OI 0.2k） ｜ Put Wall 59.5（+8.3%）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 35.5%｜历史 Rank 76%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 负 13,732 股

📆 10-07 Forward Structure
存量OI: C 2.2k / P 5.7k，今日变化ΔOI: C +0.9k / P +4.7k，平值价格ATM: C $1.23 / P $1.20 ｜ ATM IV 36.4%，净 delta 敞口 -325k shares
Top ΔOI: P 57 +4,246 ｜ C 57 +176
仓位参考: Max Pain 58 ｜ Call Wall 60（+9.2%）（OI 0.6k） ｜ Put Wall 57（+3.7%）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 36.4%｜历史 Rank 76%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 负 324,874 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=29 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=29）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/SLV_evening.json