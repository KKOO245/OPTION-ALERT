# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $751.25 ｜ QQQ $656.30
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 93.1% vs 11-13 68.2%（差 +24.9pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-13 165P ΔOI +902（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 171.70 → 今开 166.72（-2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 167.25 ｜ 低 155.89

Options: P/C成交量 1.50 | OI比 1.04 | ATM IV 93.1% | Skew 5.0pp | Term 0.61 | ExpMove ±4.5%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价中性（Skew 5.0pp）｜当日成交偏 Put（P/C量 1.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.50×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（1D）±4.5% ｜ 11-13（8D）±8.2% ｜ 11-20（15D）±10.3% ｜ 11-27（22D）±11.4%
   ⇒ IV–VIX Spread: +72.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -41,158,642 | GEX Change vs 上次快照 -24,811,484 | Flip: Primary Flip: 172.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 535 / LOW 142 / INVALID 229
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 172.59（全链重定价，覆盖 100%）
最近结构参考: Flip 173（现价低于该位 8.4%）
量化视角： 负 Gamma（4116万，无历史分位）｜负 Gamma 加深（2481万）｜现价位于 Flip 下方 8.44%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 180（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 173（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 192.5C — Vol 23,208 | 最新价 $0.07 | OI 2298→6261 (ΔOI +3963张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3963张（+172.4% vs前日OI），连续性待观察（方向未知）
11-06 172.5P — Vol 10,798 | 最新价 $3.80 | OI 1930→4827 (ΔOI +2897张) | ΔOI/Volume 26.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2897张（+150.1% vs前日OI），连续性待观察（方向未知）
11-06 177.5C — Vol 12,678 | 最新价 $1.28 | OI 1678→3769 (ΔOI +2091张) | ΔOI/Volume 16.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2091张（+124.6% vs前日OI），连续性待观察（方向未知）
11-20 165.0P — Vol 5,087 | 最新价 $5.20 | OI 5032→7114 (ΔOI +2082张) | ΔOI/Volume 40.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2082张（+41.4% vs前日OI），连续性待观察（方向未知）
11-06 170.0P — Vol 22,918 | 最新价 $2.57 | OI 7234→9032 (ΔOI +1798张) | ΔOI/Volume 7.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1798张（+24.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,831 张（Put 6,777 / Call 6,054），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C -2.9k / P -2.8k ｜ Activity MEDIUM △ ｜ 1D
11-13  C +5.1k / P +3.5k ｜ Activity HIGH ｜ 8D
11-20  C +1.9k / P +3.4k ｜ Activity HIGH ｜ 15D
11-27  C +1.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 22D

📆 11-06 Forward Structure
存量OI: C 190.5k / P 198.4k，今日变化ΔOI: C -2.9k / P -2.8k，平值价格ATM: C $3.90 / P $3.15 ｜ ATM IV 93.1%，净 delta 敞口 -10k shares
仓位参考: Max Pain 180 ｜ Call Wall 170（+7.6%，弱）（OI 2.9k） ｜ Put Wall 150（-5.1%，弱）（OI 9.6k）
量化解读： 存量两侧均衡｜ATM IV 93.1%｜历史 Rank 94%（近端代理）｜IV/RV 2.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,410 股

📆 11-13 Forward Structure
存量OI: C 42.9k / P 37.2k，今日变化ΔOI: C +5.1k / P +3.5k，平值价格ATM: C $6.85 / P $6.10 ｜ ATM IV 68.2%，净 delta 敞口 -74k shares
Top ΔOI: P 165 +902 ｜ C 180 +832
仓位参考: Max Pain 180 ｜ Call Wall 170（+7.6%，弱）（OI 1.1k） ｜ Put Wall 155（-1.9%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 68.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 74,294 股

📆 11-20 Forward Structure
存量OI: C 179.4k / P 181.3k，今日变化ΔOI: C +1.9k / P +3.4k，平值价格ATM: C $7.36 / P $8.90 ｜ ATM IV 62.6%，净 delta 敞口 -118k shares
Top ΔOI: P 165 +2,082 ｜ P 170 +1,218 ｜ P 145 +521
仓位参考: Max Pain 175 ｜ Call Wall 165（+4.4%，弱）（OI 11.8k） ｜ Put Wall 150（-5.1%，弱）（OI 9.3k）
量化解读： 存量两侧均衡｜ATM IV 62.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 118,031 股

11-27（MEDIUM △）Top ΔOI: 180C +389 ｜ 145P +268
11-27（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 160（+1.2%，弱）（OI 0.5k） ｜ Put Wall 145（-8.2%，弱）（OI 1.4k）

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 93.1% vs 11-13 68.2%（差 +24.9pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/PLTR_morning.json