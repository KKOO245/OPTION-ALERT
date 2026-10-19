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
🔴 **事件差分**: 10-23（4D）ATM IV 131.3% vs 10-30 100.5%（差 +30.8pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 230P ΔOI -2,204（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 233.23 → 收盘 226.22（-3.0%） ｜ 今日高 233.50 ｜ 低 224.20 ｜ 昨收 221.31 → 收盘 226.22（+2.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-22，窗口结束前不做对错判定）

Options: P/C成交量 0.51 | OI比 1.01 | ATM IV 131.3% | Skew 5.4pp | Term 0.64 | ExpMove ±11.0%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价中性（Skew 5.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±11.0% ｜ 10-30（11D）±14.0% ｜ 11-06（18D）±15.7% ｜ 11-13（25D）±18.4%
   ⇒ IV–VIX Spread: +112.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,407,864 | GEX Change vs 上次快照 140,813 | Flip: Primary Flip: 257.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 615 / LOW 28 / INVALID 185
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 257.10（全链重定价，覆盖 100%）
最近结构参考: Flip 257（现价低于该位 12.0%）
量化视角： 负 Gamma（741万，无历史分位）｜负 Gamma 缓解（+14万）｜现价位于 Flip 下方 12.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 248（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 257（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 195.0P — Vol 124 | 最新价 $8.40 | OI 1125→2809 (ΔOI +1684张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1684张（+149.7% vs前日OI），连续性待观察（方向未知）
10-23 145.0P — Vol 6 | 最新价 $0.09 | OI 20→1580 (ΔOI +1560张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1560张（+7800.0% vs前日OI），连续性待观察（方向未知）
10-23 190.0C — Vol 29 | 最新价 $41.00 | OI 78→1566 (ΔOI +1488张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1488张（+1907.7% vs前日OI），连续性待观察（方向未知）
11-20 165.0P — Vol 48 | 最新价 $3.00 | OI 922→1653 (ΔOI +731张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增731张（+79.3% vs前日OI），连续性待观察（方向未知）
10-23 180.0P — Vol 567 | 最新价 $0.76 | OI 361→1028 (ΔOI +667张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增667张（+184.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,130 张（Put 4,642 / Call 1,488），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +4.8k / P +8.0k ｜ Activity HIGH ｜ 4D
10-30  C +1.0k / P -1.7k ｜ Activity HIGH ｜ 11D
11-06  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
11-13  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 37.9k / P 38.1k，今日变化ΔOI: C +4.8k / P +8.0k，平值价格ATM: C $13.00 / P $11.85 ｜ ATM IV 131.3%，净 delta 敞口 136k shares
Top ΔOI: C 190 +1,488 ｜ C 255 -863
仓位参考: Max Pain 248 ｜ Call Wall 230（+1.7%，弱）（OI 1.5k） ｜ Put Wall 230（+1.7%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 131.3%｜历史 Rank 83%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 136,272 股

📆 10-30 Forward Structure
存量OI: C 18.0k / P 22.6k，今日变化ΔOI: C +1.0k / P -1.7k，平值价格ATM: C $16.45 / P $15.20 ｜ ATM IV 100.5%，净 delta 敞口 154k shares
Top ΔOI: P 230 -2,204 ｜ P 205 +329 ｜ P 285 -280
仓位参考: Max Pain 252 ｜ Call Wall 240（+6.1%，弱）（OI 1.4k） ｜ Put Wall 240（+6.1%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 100.5%｜历史 Rank 83%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 153,587 股

11-06（MEDIUM △）Top ΔOI: 250C +133 ｜ 250P +57
11-06（MEDIUM △）仓位参考: Max Pain 260 ｜ Call Wall 240（+6.1%，弱）（OI 0.2k） ｜ Put Wall 235（+3.9%）（OI 2.8k）

📆 11-13 Forward Structure
存量OI: C 4.0k / P 7.8k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $22.30 / P $19.40 ｜ ATM IV 86.4%，净 delta 敞口 5k shares
Top ΔOI: C 270 +267 ｜ C 250 +203
仓位参考: Max Pain 265 ｜ Call Wall 240（+6.1%，弱）（OI 0.3k） ｜ Put Wall 230（+1.7%）（OI 2.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 86.4%｜历史 Rank 83%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 4,887 股

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 131.3% vs 10-30 100.5%（差 +30.8pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=57 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=57）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/BE_evening.json