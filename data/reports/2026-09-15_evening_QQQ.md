# 期权晚报 2026-09-15（快照 18:31 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $nan
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 708.76 → 收盘 704.54（-0.6%） ｜ 今日高 709.53 ｜ 低 703.64 ｜ 昨收 709.18 → 收盘 704.54（-0.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-18，窗口结束前不做对错判定）

Options: P/C成交量 0.92 | OI比 2.56 | ATM IV 11.5% | Skew 2.9pp | Term 1.64 | ExpMove ±1.0%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常偏陡（Term 1.64）｜保护溢价中性（Skew 2.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.56×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 6% ｜ P/C OI(近端) 93%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 6%）｜近端 Put 显著偏重（P/C OI 分位 93%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-16（1D）±1.0% ｜ 09-17（2D）±1.4% ｜ 09-18（3D）±1.7% ｜ 09-21（6D）±1.9%
   ⇒ IV–VIX Spread: -5.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,038,215,065 | GEX Change vs 上次快照 12,736,657 | Flip: Primary Flip: 718.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2850 / LOW 542 / INVALID 2388
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 718.09（全链重定价，覆盖 93%）
Put Wall 700（弱结构｜现价高于该位 0.6%） | Call Wall 750（弱结构｜现价低于该位 6.1%）
最近结构参考: Put Wall 700（现价高于该位 0.6%）
量化视角： 负 Gamma（10.38亿，历史分位偏负区，比 94% 的交易日更负）｜负 Gamma 缓解（+1274万）｜现价位于 Flip 下方 1.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 710（MaxPain，仅结算参考） / 750（Call Wall，弱结构）。
• Gamma 区域：切换参考 718（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 615.0P — Vol 46 | 最新价 $0.08 | OI 22413→42415 (ΔOI +20002张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20002张（+89.2% vs前日OI），连续性待观察（方向未知）
10-16 685.0P — Vol 2,536 | 最新价 $8.53 | OI 10883→18823 (ΔOI +7940张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7940张（+73.0% vs前日OI），连续性待观察（方向未知）
量化视角： 2 个事件合计 ΔOI ≈ 27,942 张（Put 27,942 / Call 0），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $7M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-16  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-17  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-16 Forward Structure
存量OI: C 57.3k / P 123.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.93 / P $3.38 ｜ ATM IV 24.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 710 ｜ Call Wall 725（+2.9%，弱）（OI 5.6k） ｜ Put Wall 700（-0.6%，弱）（OI 6.7k）
量化解读： 存量 Put 重｜ATM IV 24.6%｜历史 Rank 14%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-17（Activity LOW）仓位参考: Max Pain 712 ｜ Call Wall 727（+3.2%，弱）（OI 2.2k） ｜ Put Wall 650（-7.7%）（OI 9.5k）

09-18（Activity LOW）仓位参考: Max Pain 700 ｜ Call Wall 750（+6.5%，弱）（OI 50.6k） ｜ Put Wall 700（-0.6%）（OI 117.7k）

09-21（Activity LOW）仓位参考: Max Pain 715 ｜ Call Wall 735（+4.3%，弱）（OI 2.1k） ｜ Put Wall 715（+1.5%）（OI 7.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=22 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=22）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/QQQ_evening.json