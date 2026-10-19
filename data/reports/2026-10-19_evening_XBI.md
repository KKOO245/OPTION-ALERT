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
🟡 **近现价集中开仓**: 10-23 146C ΔOI +3,006（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 130P ΔOI +15,383 占该期限总 OI 29.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 145.88 → 收盘 147.86（+1.4%） ｜ 今日高 148.63 ｜ 低 145.30 ｜ 昨收 144.32 → 收盘 147.86（+2.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-26，窗口结束前不做对错判定）

Options: P/C成交量 1.81 | OI比 1.05 | ATM IV 40.8% | Skew 4.4pp | Term 0.79 | ExpMove ±3.1%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 4.4pp）｜当日成交偏 Put（P/C量 1.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.81×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.05×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±3.1% ｜ 10-30（11D）±5.0% ｜ 11-06（18D）±6.0% ｜ 11-13（25D）±7.2%
   ⇒ IV–VIX Spread: +22.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -22,784,927 | GEX Change vs 上次快照 5,842,190 | Flip: Primary Flip: 164.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 347 / LOW 92 / INVALID 327
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.31（全链重定价，覆盖 92%）
Put Wall 140（弱结构｜现价高于该位 5.6%） | Call Wall 155（弱结构｜现价低于该位 4.6%）
最近结构参考: Call Wall 155（现价低于该位 4.6%）
量化视角： 负 Gamma（2278万，无历史分位）｜负 Gamma 缓解（+584万）｜现价位于 Flip 下方 10.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构） / 146（MaxPain，仅结算参考）；上方 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 130.0P — Vol 2 | 最新价 $0.29 | OI 55→15438 (ΔOI +15383张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15383张（+27969.1% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 3,080 | 最新价 $1.00 | OI 6580→18780 (ΔOI +12200张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12200张（+185.4% vs前日OI），连续性待观察（方向未知）
10-23 135.0P — Vol 23 | 最新价 $0.05 | OI 131→3157 (ΔOI +3026张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3026张（+2309.9% vs前日OI），连续性待观察（方向未知）
10-23 146.0C — Vol 2 | 最新价 $3.25 | OI 4→3010 (ΔOI +3006张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3006张（+75150.0% vs前日OI），连续性待观察（方向未知）
10-23 148.0C — Vol 196 | 最新价 $2.24 | OI 50→3046 (ΔOI +2996张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2996张（+5992.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,611 张（Put 30,609 / Call 6,002），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +13.0k / P +10.0k ｜ Activity HIGH ｜ 4D
10-30  C +0.9k / P +27.9k ｜ Activity HIGH ｜ 11D
11-06  C +0.3k / P -6 ｜ Activity MEDIUM △ ｜ 18D
11-13  C +4 / P +0.6k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 17.4k / P 18.3k，今日变化ΔOI: C +13.0k / P +10.0k，平值价格ATM: C $2.24 / P $2.35 ｜ ATM IV 40.8%，净 delta 敞口 556k shares
Top ΔOI: P 135 +3,026 ｜ C 146 +3,006 ｜ C 148 +2,996
仓位参考: Max Pain 146 ｜ Call Wall 150（+1.4%，弱）（OI 3.2k） ｜ Put Wall 144（-2.6%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.8%｜历史 Rank 87%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 556,339 股

📆 10-30 Forward Structure
存量OI: C 5.4k / P 46.1k，今日变化ΔOI: C +0.9k / P +27.9k，平值价格ATM: C $3.95 / P $3.50 ｜ ATM IV 34.6%，净 delta 敞口 -269k shares
Top ΔOI: P 130 +15,383 ｜ P 140 +12,200 ｜ C 155 +828
仓位参考: Max Pain 152 ｜ Call Wall 155（+4.8%）（OI 1.6k） ｜ Put Wall 140（-5.3%，弱）（OI 18.8k）
量化解读： 存量 Put 重｜ATM IV 34.6%｜历史 Rank 87%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 268,628 股

11-06（MEDIUM △）Top ΔOI: 154C +215 ｜ 150C +36
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+4.8%，弱）（OI 0.3k） ｜ Put Wall 145（-1.9%，弱）（OI 0.4k）

📆 11-13 Forward Structure
存量OI: C 0.3k / P 1.7k，今日变化ΔOI: C +4 / P +0.6k，平值价格ATM: C $5.31 / P $5.32 ｜ ATM IV 33.5%，净 delta 敞口 -16k shares
Top ΔOI: P 140 +501 ｜ P 144 +33 ｜ P 151 +33
仓位参考: Max Pain 155 ｜ Call Wall 148（+0.1%，弱）（OI 15） ｜ Put Wall 140（-5.3%）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 33.5%｜历史 Rank 87%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 负 15,903 股

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 40.8% vs 10-30 34.6%（差 +6.2pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/XBI_evening.json