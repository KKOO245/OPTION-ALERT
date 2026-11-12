# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $757.88 ｜ QQQ $688.17
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 119.3% vs 11-20 97.8%（差 +21.6pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 205P ΔOI +4,515（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 209.47 → 今开 195.89（-6.5%） | 较昨收变动（含盘初走势） ｜ 今日高 203.19 ｜ 低 193.44

Options: P/C成交量 1.15 | OI比 1.16 | ATM IV 119.3% | Skew -2.6pp | Term 0.73 | ExpMove ±5.5%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（1D）±5.5% ｜ 11-20（8D）±11.8% ｜ 11-27（15D）±12.2% ｜ 12-04（22D）±15.9%
   ⇒ IV–VIX Spread: +100.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,315,709 | GEX Change vs 上次快照 -13,853,572 | Flip: Primary Flip: 207.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 579 / LOW 171 / INVALID 194
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 207.24（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价低于该位 1.6%）
最近结构参考: Put Wall 200（现价低于该位 1.6%）
量化视角： 负 Gamma（932万，无历史分位）｜由正转负（1385万）｜现价位于 Flip 下方 5.00%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 198（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 207（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 185.0P — Vol 9,874 | 最新价 $0.64 | OI 877→9515 (ΔOI +8638张) | ΔOI/Volume 87.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8638张（+985.0% vs前日OI），连续性待观察（方向未知）
11-13 205.0P — Vol 6,129 | 最新价 $4.55 | OI 429→4944 (ΔOI +4515张) | ΔOI/Volume 73.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4515张（+1052.5% vs前日OI），连续性待观察（方向未知）
11-20 110.0P — Vol 2,033 | 最新价 $0.02 | OI 640→2343 (ΔOI +1703张) | ΔOI/Volume 83.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1703张（+266.1% vs前日OI），连续性待观察（方向未知）
11-13 175.0P — Vol 3,040 | 最新价 $0.23 | OI 2092→3616 (ΔOI +1524张) | ΔOI/Volume 50.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1524张（+72.8% vs前日OI），连续性待观察（方向未知）
11-13 200.0P — Vol 2,471 | 最新价 $3.00 | OI 898→1711 (ΔOI +813张) | ΔOI/Volume 32.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增813张（+90.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,193 张（Put 17,193 / Call 0），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +2.8k / P +17.8k ｜ Activity HIGH ｜ 1D
11-20  C +1.6k / P +4.1k ｜ Activity HIGH ｜ 8D
11-27  C +0.7k / P +0.4k ｜ Activity HIGH ｜ 15D
12-04  C +0.3k / P +77 ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 46.2k / P 53.5k，今日变化ΔOI: C +2.8k / P +17.8k，平值价格ATM: C $5.16 / P $5.65 ｜ ATM IV 119.3%，净 delta 敞口 -682k shares
Top ΔOI: P 185 +8,638 ｜ P 205 +4,515 ｜ P 175 +1,524
仓位参考: Max Pain 198 ｜ Call Wall 180（-8.6%，弱）（OI 1.8k） ｜ Put Wall 185（-6.0%）（OI 9.5k）
量化解读： 存量两侧均衡｜ATM IV 119.3%｜历史 Rank 76%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 682,013 股

📆 11-20 Forward Structure
存量OI: C 81.8k / P 85.2k，今日变化ΔOI: C +1.6k / P +4.1k，平值价格ATM: C $11.50 / P $11.75 ｜ ATM IV 97.8%，净 delta 敞口 -76k shares
Top ΔOI: C 230 +774 ｜ C 222 -433
仓位参考: Max Pain 215 ｜ Call Wall 200（+1.6%，弱）（OI 2.9k） ｜ Put Wall 200（+1.6%，弱）（OI 5.5k）
量化解读： 存量两侧均衡｜ATM IV 97.8%｜历史 Rank 76%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 76,217 股

📆 11-27 Forward Structure
存量OI: C 9.8k / P 11.3k，今日变化ΔOI: C +0.7k / P +0.4k，平值价格ATM: C $16.00 / P $8.00 ｜ ATM IV 87.4%，净 delta 敞口 -22k shares
Top ΔOI: P 200 +531 ｜ C 230 +184
仓位参考: Max Pain 215 ｜ Call Wall 200（+1.6%，弱）（OI 0.6k） ｜ Put Wall 200（+1.6%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 87.4%｜历史 Rank 76%（近端代理）｜IV/RV 0.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 21,788 股

12-04（MEDIUM △）Top ΔOI: 175P +87 ｜ 235C +71
12-04（MEDIUM △）仓位参考: Max Pain 205 ｜ Call Wall 200（+1.6%，弱）（OI 0.6k） ｜ Put Wall 200（+1.6%）（OI 1.8k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 119.3% vs 11-20 97.8%（差 +21.6pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/BE_morning.json