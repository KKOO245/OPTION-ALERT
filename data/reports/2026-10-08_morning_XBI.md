# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.92
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **事件差分**: 10-09 ATM IV 48.4% vs 10-16 34.7%（差 +13.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 154P ΔOI -2,245（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 150.23 → 今开 149.00（-0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 149.40 ｜ 低 146.50

Options: P/C成交量 0.28 | OI比 2.26 | ATM IV 48.4% | Skew -10.1pp | Term 0.67 | ExpMove ±1.4%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜Put 保护异常便宜（Skew -10.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.26×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±1.4% ｜ 10-16（8D）±8.9% ｜ 10-23（15D）±1.2% ｜ 10-30（22D）±9.1%
   ⇒ IV–VIX Spread: +32.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -61,831,804 | GEX Change vs 上次快照 -2,382,063 | Flip: Primary Flip: 160.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 280 / LOW 110 / INVALID 382
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 160.38（全链重定价，覆盖 85%）
Put Wall 150（现价低于该位 1.8%）
最近结构参考: Put Wall 150（现价低于该位 1.8%）
量化视角： 负 Gamma（6183万，无历史分位）｜负 Gamma 加深（238万）｜现价位于 Flip 下方 8.13%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall） / 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 153.0C — Vol 297 | 最新价 $0.52 | OI 295→542 (ΔOI +247张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增247张（+83.7% vs前日OI），连续性待观察（方向未知）
11-06 143.0P — Vol 252 | 最新价 $2.36 | OI 13→253 (ΔOI +240张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增240张（+1846.2% vs前日OI），连续性待观察（方向未知）
10-09 145.0P — Vol 208 | 最新价 $0.14 | OI 1247→1453 (ΔOI +206张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增206张（+16.5% vs前日OI），连续性待观察（方向未知）
10-30 145.0P — Vol 200 | 最新价 $2.78 | OI 73→273 (ΔOI +200张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增200张（+274.0% vs前日OI），连续性待观察（方向未知）
10-16 141.0P — Vol 183 | 最新价 $0.37 | OI 49→223 (ΔOI +174张) | ΔOI/Volume 95.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增174张（+355.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,067 张（Put 820 / Call 247），跨 4 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 1D
10-16  C -1.5k / P -4.0k ｜ Activity MEDIUM △ ｜ 8D
10-23  C +0.3k / P +95 ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 6.0k / P 13.5k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $1.60 / P $0.48 ｜ ATM IV 48.4%，净 delta 敞口 -8k shares
Top ΔOI: C 153 +247 ｜ P 145 +206 ｜ C 155 +117
仓位参考: Max Pain 155 ｜ Call Wall 145（-1.6%）（OI 1.0k） ｜ Put Wall 148（+0.4%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.4%｜历史 Rank 96%（近端代理）｜IV/RV 1.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,895 股

10-16（MEDIUM △）Top ΔOI: 154P -2,245 ｜ 144P -973
10-16（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 155（+5.2%，弱）（OI 1.8k） ｜ Put Wall 150（+1.8%）（OI 22.6k）

10-23（MEDIUM △）Top ΔOI: 145P +89
10-23（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 154（+4.5%，弱）（OI 89） ｜ Put Wall 140（-5.0%，弱）（OI 0.7k）

📆 10-30 Forward Structure
存量OI: C 2.7k / P 18.2k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $10.10 / P $3.37 ｜ ATM IV 33.1%，净 delta 敞口 -1k shares
Top ΔOI: P 145 +200
仓位参考: Max Pain 153 ｜ Call Wall 150（+1.8%，弱）（OI 0.1k） ｜ Put Wall 150（+1.8%，弱）（OI 7.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 负 1,073 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 48.4% vs 10-16 34.7%（差 +13.7pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/XBI_morning.json