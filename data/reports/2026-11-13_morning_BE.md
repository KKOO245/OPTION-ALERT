# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.63
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 99.9% vs 11-27 89.3%（差 +10.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 195P ΔOI +560（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 201.93 → 今开 200.45（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 205.92 ｜ 低 185.01

Options: P/C成交量 0.81 | OI比 1.08 | ATM IV 143.4% | Skew 2.7pp | Term 0.62 | ExpMove ±11.2%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（7D）±11.2% ｜ 11-27（14D）±14.7% ｜ 12-04（21D）±17.1% ｜ 12-11（28D）±19.7%
   ⇒ IV–VIX Spread: +123.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,655,890 | GEX Change vs 上次快照 -7,801,860 | Flip: Primary Flip: 206.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 512 / LOW 155 / INVALID 277
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 206.52（全链重定价，覆盖 98%）
Put Wall 200（弱结构｜现价低于该位 5.3%）
最近结构参考: Put Wall 200（现价低于该位 5.3%）
量化视角： 负 Gamma（1366万，无历史分位）｜负 Gamma 加深（780万）｜现价位于 Flip 下方 8.32%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 195（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 207（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 175.0P — Vol 5,256 | 最新价 $10.40 | OI 994→5578 (ΔOI +4584张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4584张（+461.2% vs前日OI），连续性待观察（方向未知）
11-20 215.0C — Vol 2,050 | 最新价 $6.70 | OI 845→1584 (ΔOI +739张) | ΔOI/Volume 36.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增739张（+87.5% vs前日OI），连续性待观察（方向未知）
11-20 125.0P — Vol 823 | 最新价 $0.05 | OI 1103→1798 (ΔOI +695张) | ΔOI/Volume 84.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增695张（+63.0% vs前日OI），连续性待观察（方向未知）
11-20 195.0P — Vol 1,262 | 最新价 $8.55 | OI 2424→2984 (ΔOI +560张) | ΔOI/Volume 44.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增560张（+23.1% vs前日OI），连续性待观察（方向未知）
11-13 212.5C — Vol 1,211 | 最新价 $1.27 | OI 1044→1573 (ΔOI +529张) | ΔOI/Volume 43.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增529张（+50.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,107 张（Put 5,839 / Call 1,268），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $5M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 47.2k / P 51.0k，今日成交量: C 8.7k / P 7.1k，平值价格ATM: C $3.17 / P $2.75 ｜ ATM IV 143.4%，预期波动 ±3.1%，Max Pain 195
Top ΔOI: C 212 +529 ｜ C 187 +468 ｜ P 190 -434

📆 Forward Expiration Structure

11-20  C +2.0k / P +3.8k ｜ Activity HIGH ｜ 7D
11-27  C +1.0k / P +93 ｜ Activity MEDIUM △ ｜ 14D
12-04  C +0.3k / P +0.3k ｜ Activity LOW ｜ 21D
12-11  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 83.8k / P 89.0k，今日变化ΔOI: C +2.0k / P +3.8k，平值价格ATM: C $10.45 / P $10.80 ｜ ATM IV 99.9%，净 delta 敞口 -27k shares
Top ΔOI: C 215 +739 ｜ P 195 +560
仓位参考: Max Pain 215 ｜ Call Wall 200（+5.6%，弱）（OI 3.1k） ｜ Put Wall 200（+5.6%，弱）（OI 5.2k）
量化解读： 存量两侧均衡｜ATM IV 99.9%｜历史 Rank 89%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,428 股

11-27（MEDIUM △）Top ΔOI: 210C +168 ｜ 215C +157
11-27（MEDIUM △）仓位参考: Max Pain 215 ｜ Call Wall 200（+5.6%，弱）（OI 0.7k） ｜ Put Wall 200（+5.6%，弱）（OI 1.4k）

12-04（Activity LOW）仓位参考: Max Pain 200 ｜ Call Wall 200（+5.6%，弱）（OI 0.6k） ｜ Put Wall 200（+5.6%）（OI 1.8k）

12-11（MEDIUM △）Top ΔOI: 230C +205 ｜ 190P +67
12-11（MEDIUM △）仓位参考: Max Pain 210 ｜ Call Wall 195（+3.0%，弱）（OI 0.2k） ｜ Put Wall 175（-7.6%）（OI 2.0k）

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 99.9% vs 11-27 89.3%（差 +10.6pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/BE_morning.json