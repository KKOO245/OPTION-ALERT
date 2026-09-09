# 期权晚报 2026-09-09（快照 18:23 ET）

📊 市场环境

SPY $762.40 ｜ QQQ $716.31
VIX 16.46 ↑4.7%（5D +8.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.98 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 160.50 → 收盘 159.38（-0.7%） ｜ 今日高 162.97 ｜ 低 159.35 ｜ 昨收 161.93 → 收盘 159.38（-1.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-14，窗口结束前不做对错判定）

Options: P/C成交量 7.83 | OI比 2.41 | ATM IV 37.9% | Skew -0.8pp | Term 0.82 | ExpMove ±2.6%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 7.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 7.83×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.41×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（2D）±2.6% ｜ 09-18（9D）±4.2% ｜ 09-25（16D）±5.9% ｜ 10-02（23D）±10.7%
   ⇒ IV–VIX Spread: +21.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -37,258,378 | GEX Change vs 上次快照 -1,226,789 | Flip: Primary Flip: 165.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 422 / LOW 109 / INVALID 321
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 165.70（全链重定价，覆盖 97%）
Put Wall 158（弱结构｜现价高于该位 0.9%） | Call Wall 170（弱结构｜现价低于该位 6.2%）
最近结构参考: Put Wall 158（现价高于该位 0.9%）
量化视角： 负 Gamma（3726万，无历史分位）｜负 Gamma 加深（123万）｜现价位于 Flip 下方 3.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 158（Put Wall，弱结构）；上方 163（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 143.0P — Vol 1 | 最新价 $0.10 | OI 3620→6021 (ΔOI +2401张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2401张（+66.3% vs前日OI），连续性待观察（方向未知）
09-11 161.0P — Vol 2,006 | 最新价 $2.20 | OI 59→2013 (ΔOI +1954张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1954张（+3311.9% vs前日OI），连续性待观察（方向未知）
09-11 160.0P — Vol 24 | 最新价 $1.64 | OI 624→2110 (ΔOI +1486张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1486张（+238.1% vs前日OI），连续性待观察（方向未知）
09-11 146.5P — Vol 18（Yahoo补） | 最新价 $0.03 | OI 10→230 (ΔOI +220张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增220张（+2200.0% vs前日OI），值得跟踪（方向未知）
09-11 147.5P — Vol 2 | 最新价 $0.03 | OI 8→115 (ΔOI +107张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增107张（+1337.5% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,168 张（Put 6,168 / Call 0），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-11 Forward Structure
存量OI:      C 7.2k / P 17.4k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.00 / P 1.19
隐含波动率 ATM IV:  37.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 163（结算参考） ｜ Call Wall 164（+2.9%，弱）（OI 1.7k） ｜ Put Wall 155（-2.7%）（OI 3.5k）
量化解读： 存量 Put 重｜ATM IV 37.9%｜历史 Rank 77%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 158（结算参考） ｜ Call Wall 155（-2.7%，弱）（OI 10.8k） ｜ Put Wall 158（-0.9%，弱）（OI 16.8k）

09-25（Activity LOW）仓位参考: Max Pain 160（结算参考） ｜ Call Wall 167（+4.8%）（OI 1.4k）

10-02（Activity LOW）仓位参考: Max Pain 164（结算参考） ｜ Call Wall 165（+3.5%）（OI 0.2k） ｜ Put Wall 150（-5.9%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-09/XBI_evening.json