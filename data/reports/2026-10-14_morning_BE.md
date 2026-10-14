# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $771.45 ｜ QQQ $732.55
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 255C ΔOI +657（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 263.45 → 今开 257.50（-2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 258.52 ｜ 低 250.25

Options: P/C成交量 0.84 | OI比 1.06 | ATM IV 88.0% | Skew 3.1pp | Term 0.91 | ExpMove ±5.6%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 3.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.06×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±5.6% ｜ 10-23（9D）±11.9% ｜ 10-30（16D）±14.8% ｜ 11-06（23D）±16.2%
   ⇒ IV–VIX Spread: +72.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,906,917 | GEX Change vs 上次快照 -7,591,176 | Flip: Primary Flip: 262.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 617 / LOW 84 / INVALID 179
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 262.22（全链重定价，覆盖 100%）
Put Wall 240（弱结构｜现价高于该位 4.7%）
最近结构参考: Flip 262（现价低于该位 4.2%）
量化视角： 负 Gamma（991万，无历史分位）｜负 Gamma 加深（759万）｜现价位于 Flip 下方 4.21%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 240（Put Wall，弱结构）；上方 265（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 262（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 260.0C — Vol 2,876 | 最新价 $17.36 | OI 398→2311 (ΔOI +1913张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1913张（+480.6% vs前日OI），连续性待观察（方向未知）
10-23 255.0P — Vol 1,221 | 最新价 $11.60 | OI 599→1612 (ΔOI +1013张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1013张（+169.1% vs前日OI），连续性待观察（方向未知）
10-23 240.0P — Vol 898 | 最新价 $6.30 | OI 1419→2224 (ΔOI +805张) | ΔOI/Volume 89.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增805张（+56.7% vs前日OI），连续性待观察（方向未知）
10-23 235.0P — Vol 790 | 最新价 $4.90 | OI 920→1638 (ΔOI +718张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增718张（+78.0% vs前日OI），连续性待观察（方向未知）
10-23 300.0C — Vol 1,044 | 最新价 $4.75 | OI 1209→1914 (ΔOI +705张) | ΔOI/Volume 67.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增705张（+58.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,154 张（Put 2,536 / Call 2,618），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.9k / P +0.7k ｜ Activity HIGH ｜ 2D
10-23  C +5.6k / P +3.8k ｜ Activity HIGH ｜ 9D
10-30  C +0.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +0.1k / P +0.3k ｜ Activity LOW ｜ 23D

📆 10-16 Forward Structure
存量OI: C 98.8k / P 104.3k，今日变化ΔOI: C +1.9k / P +0.7k，平值价格ATM: C $7.75 / P $6.30 ｜ ATM IV 88.0%，净 delta 敞口 111k shares
Top ΔOI: C 255 +657 ｜ C 270 -594 ｜ P 237 +339
仓位参考: Max Pain 265 ｜ Call Wall 270（+7.5%，弱）（OI 7.1k） ｜ Put Wall 260（+3.5%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 88.0%｜历史 Rank 51%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 110,507 股

📆 10-23 Forward Structure
存量OI: C 25.4k / P 26.1k，今日变化ΔOI: C +5.6k / P +3.8k，平值价格ATM: C $15.55 / P $14.35 ｜ ATM IV 97.0%，净 delta 敞口 30k shares
Top ΔOI: C 260 +1,913 ｜ P 255 +1,013 ｜ P 240 +805
仓位参考: Max Pain 260 ｜ Call Wall 260（+3.5%，弱）（OI 2.3k） ｜ Put Wall 240（-4.5%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 97.0%｜历史 Rank 51%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 30,212 股

10-30（MEDIUM △）Top ΔOI: 240P +372 ｜ 305C -148
10-30（MEDIUM △）仓位参考: Max Pain 280 ｜ Call Wall 270（+7.5%，弱）（OI 0.6k） ｜ Put Wall 230（-8.4%，弱）（OI 3.0k）

11-06（Activity LOW）仓位参考: Max Pain 270 ｜ Call Wall 260（+3.5%，弱）（OI 0.4k） ｜ Put Wall 235（-6.4%，弱）（OI 2.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/BE_morning.json