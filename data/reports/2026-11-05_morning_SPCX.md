# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $732.06 ｜ QQQ $647.05
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
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
🔴 **事件差分**: 11-06（1D）ATM IV 94.6% vs 11-09 70.0%（差 +24.7pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-09 120P ΔOI +7,880（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 135.92 → 今开 131.34（-3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 131.87 ｜ 低 123.06

Options: P/C成交量 1.16 | OI比 0.71 | ATM IV 94.6% | Skew 10.9pp | Term 0.63 | ExpMove ±4.4%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价显著（Skew 10.9pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.71）+ 当日成交偏 Put（P/C量 1.16）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±4.4% ｜ 11-09（4D）±6.0% ｜ 11-11（6D）±7.5% ｜ 11-13（8D）±8.4%
   ⇒ IV–VIX Spread: +73.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -83,386,073 | GEX Change vs 上次快照 -2,250,086 | Flip: Primary Flip: 136.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 696 / LOW 149 / INVALID 609
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 136.74（全链重定价，覆盖 94%）
Put Wall 135（弱结构｜现价低于该位 6.8%）
最近结构参考: Put Wall 135（现价低于该位 6.8%）
量化视角： 负 Gamma（8339万，无历史分位）｜负 Gamma 加深（225万）｜现价位于 Flip 下方 8.03%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（Put Wall，弱结构） / 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-09 120.0P — Vol 8,792 | 最新价 $0.35 | OI 149→8029 (ΔOI +7880张) | ΔOI/Volume 89.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7880张（+5288.6% vs前日OI），连续性待观察（方向未知）
11-20 115.0P — Vol 7,259 | 最新价 $1.01 | OI 19724→23537 (ΔOI +3813张) | ΔOI/Volume 52.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3813张（+19.3% vs前日OI），连续性待观察（方向未知）
11-09 130.0P — Vol 5,166 | 最新价 $1.42 | OI 784→4431 (ΔOI +3647张) | ΔOI/Volume 70.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3647张（+465.2% vs前日OI），连续性待观察（方向未知）
11-20 120.0P — Vol 11,446 | 最新价 $1.61 | OI 18580→22026 (ΔOI +3446张) | ΔOI/Volume 30.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3446张（+18.6% vs前日OI），连续性待观察（方向未知）
11-06 147.0C — Vol 6,783 | 最新价 $0.24 | OI 3016→6349 (ΔOI +3333张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3333张（+110.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,119 张（Put 18,786 / Call 3,333），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +7.9k / P -1.6k ｜ Activity MEDIUM △ ｜ 1D
11-09  C +3.8k / P +19.6k ｜ Activity HIGH ｜ 4D
11-11  C +3.2k / P +2.1k ｜ Activity HIGH ｜ 6D
11-13  C +10.3k / P +11.8k ｜ Activity MEDIUM △ ｜ 8D

📆 11-06 Forward Structure
存量OI: C 257.3k / P 181.6k，今日变化ΔOI: C +7.9k / P -1.6k，平值价格ATM: C $2.61 / P $2.98 ｜ ATM IV 94.6%，净 delta 敞口 777k shares
Top ΔOI: P 135 -6,650
仓位参考: Max Pain 142 ｜ Put Wall 135（+7.3%，弱）（OI 15.7k）
量化解读： 存量 Call 重｜ATM IV 94.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 777,075 股

📆 11-09 Forward Structure
存量OI: C 13.4k / P 27.2k，今日变化ΔOI: C +3.8k / P +19.6k，平值价格ATM: C $3.60 / P $3.93 ｜ ATM IV 70.0%，净 delta 敞口 -748k shares
Top ΔOI: P 120 +7,880 ｜ P 130 +3,647 ｜ P 115 +2,625
仓位参考: Max Pain 140 ｜ Call Wall 138（+9.7%，弱）（OI 0.4k） ｜ Put Wall 120（-4.6%）（OI 8.0k）
量化解读： 存量 Put 重｜ATM IV 70.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 负 747,807 股

📆 11-11 Forward Structure
存量OI: C 6.7k / P 5.3k，今日变化ΔOI: C +3.2k / P +2.1k，平值价格ATM: C $4.70 / P $4.70 ｜ ATM IV 71.6%，净 delta 敞口 -64k shares
Top ΔOI: C 140 +896 ｜ P 125 +512 ｜ C 137 +336
仓位参考: Max Pain 139 ｜ Call Wall 137（+8.9%，弱）（OI 0.4k） ｜ Put Wall 125（-0.6%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 71.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 64,212 股

11-13（MEDIUM △）Top ΔOI: 118P +2,831 ｜ 117P +2,029
11-13（MEDIUM △）仓位参考: Max Pain 145 ｜ Put Wall 135（+7.3%，弱）（OI 5.3k）

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 94.6% vs 11-09 70.0%（差 +24.7pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/SPCX_morning.json