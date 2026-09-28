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
🟡 **近现价集中开仓**: 10-02 152P ΔOI +2,470（距现价 -2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 153P ΔOI +436 占该期限总 OI 22.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 154.66 → 收盘 156.61（+1.3%） ｜ 今日高 157.63 ｜ 低 153.74 ｜ 昨收 155.03 → 收盘 156.61（+1.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-05，窗口结束前不做对错判定）

Options: P/C成交量 1.75 | OI比 4.88 | ATM IV 39.8% | Skew 2.0pp | Term 0.80 | ExpMove ±3.3%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价中性（Skew 2.0pp）｜当日成交偏 Put（P/C量 1.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.75×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 4.88×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±3.3% ｜ 10-09（11D）±4.8% ｜ 10-16（18D）±6.0% ｜ 10-23（25D）±7.3%
   ⇒ IV–VIX Spread: +23.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,686,421 | GEX Change vs 上次快照 7,563,502 | Flip: Primary Flip: 166.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 338 / LOW 77 / INVALID 343
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.62（全链重定价，覆盖 99%）
Put Wall 150（现价高于该位 4.4%）
最近结构参考: Put Wall 150（现价高于该位 4.4%）
量化视角： 负 Gamma（3369万，无历史分位）｜负 Gamma 缓解（+756万）｜现价位于 Flip 下方 6.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 156（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 145.0P — Vol 1,006 | 最新价 $0.09 | OI 3621→7240 (ΔOI +3619张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3619张（+99.9% vs前日OI），连续性待观察（方向未知）
10-02 152.5P — Vol 6 | 最新价 $1.05 | OI 121→2591 (ΔOI +2470张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2470张（+2041.3% vs前日OI），连续性待观察（方向未知）
10-02 148.0P — Vol 6,209 | 最新价 $0.23 | OI 10099→12000 (ΔOI +1901张) | ΔOI/Volume 30.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1901张（+18.8% vs前日OI），连续性待观察（方向未知）
10-16 150.0P — Vol 326 | 最新价 $1.89 | OI 20901→22351 (ΔOI +1450张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1450张（+6.9% vs前日OI），值得跟踪（方向未知）
10-16 135.0P — Vol 3 | 最新价 $0.20 | OI 4257→5375 (ΔOI +1118张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1118张（+26.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,558 张（Put 10,558 / Call 0），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.8k / P +9.1k ｜ Activity HIGH ｜ 4D
10-09  C +71 / P +85 ｜ Activity HIGH ｜ 11D
10-16  C +0.2k / P +3.2k ｜ Activity MEDIUM △ ｜ 18D
10-23  C +97 / P +0.7k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 6.6k / P 32.2k，今日变化ΔOI: C +1.8k / P +9.1k，平值价格ATM: C $2.60 / P $2.55 ｜ ATM IV 39.8%，净 delta 敞口 -39k shares
Top ΔOI: P 145 +3,619 ｜ P 152 +2,470 ｜ P 148 +1,901
仓位参考: Max Pain 156 ｜ Call Wall 162（+3.4%）（OI 1.6k） ｜ Put Wall 148（-5.5%）（OI 12.0k）
量化解读： 存量 Put 重｜ATM IV 39.8%｜历史 Rank 83%（近端代理）｜IV/RV 1.66×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 38,940 股

📆 10-09 Forward Structure
存量OI: C 0.7k / P 3.1k，今日变化ΔOI: C +71 / P +85，平值价格ATM: C $3.80 / P $3.68 ｜ ATM IV 33.6%，净 delta 敞口 3k shares
Top ΔOI: C 158 +64 ｜ P 145 +47
仓位参考: Max Pain 157 ｜ Call Wall 158（+0.9%）（OI 0.2k） ｜ Put Wall 150（-4.2%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 33.6%｜历史 Rank 83%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,806 股

10-16（MEDIUM △）Top ΔOI: 150P +1,450 ｜ 145P +476
10-16（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 165（+5.4%，弱）（OI 2.9k） ｜ Put Wall 150（-4.2%）（OI 22.4k）

📆 10-23 Forward Structure
存量OI: C 0.5k / P 1.5k，今日变化ΔOI: C +97 / P +0.7k，平值价格ATM: C $4.66 / P $6.83 ｜ ATM IV 32.7%，净 delta 敞口 -13k shares
Top ΔOI: P 153 +436 ｜ P 145 +97
仓位参考: Max Pain 159 ｜ Call Wall 154（-1.7%，弱）（OI 74） ｜ Put Wall 153（-2.3%）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 32.7%｜历史 Rank 83%（近端代理）｜IV/RV 1.36×（近似）｜净 delta 敞口 负 13,328 股

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 39.8% vs 10-09 33.6%（差 +6.1pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/XBI_evening.json