# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-25 775C ΔOI +8,796（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 764.07 → 收盘 767.18（+0.4%） ｜ 今日高 768.95 ｜ 低 763.24 ｜ 昨收 767.81 → 收盘 767.18（-0.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-29，窗口结束前不做对错判定）

Options: P/C成交量 1.04 | OI比 1.42 | ATM IV 15.1% | Skew 1.8pp | Term 0.84 | ExpMove ±0.6%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.42×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 52% ｜ P/C OI(近端) 18%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 52%）｜近端持仓结构中性（P/C OI 分位 18%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-25（1D）±0.6% ｜ 09-28（4D）±0.8% ｜ 09-29（5D）±1.0% ｜ 09-30（6D）±1.1%
   ⇒ IV–VIX Spread: -0.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -156,355,320 | GEX Change vs 上次快照 -882,002,915 | Flip: Primary Flip: 767.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2867 / LOW 402 / INVALID 1943
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 767.90（全链重定价，覆盖 96%）
Call Wall 785（现价低于该位 2.3%）
最近结构参考: Flip 768（现价低于该位 0.1%）
量化视角： 负 Gamma（1.56亿，历史分位 52%，中性区）｜由正转负（8.82亿）｜现价位于 Flip 下方 0.09%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 768（MaxPain，仅结算参考） / 785（Call Wall）。
• Gamma 区域：切换参考 768（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +58.3k / P +52.7k ｜ Activity HIGH ｜ 1D
09-28  C +17.6k / P +14.4k ｜ Activity HIGH ｜ 4D
09-29  C +17.8k / P +38.9k ｜ Activity HIGH ｜ 5D
09-30  C +46.1k / P +170.7k ｜ Activity HIGH ｜ 6D

📆 09-25 Forward Structure
存量OI: C 343.2k / P 677.0k，今日变化ΔOI: C +58.3k / P +52.7k，平值价格ATM: C $1.99 / P $2.23 ｜ ATM IV 13.1%，净 delta 敞口 -289k shares
Top ΔOI: C 775 +8,796 ｜ C 780 +7,933 ｜ P 725 +7,742
仓位参考: Max Pain 767 ｜ Call Wall 785（+2.3%，弱）（OI 30.7k） ｜ Put Wall 745（-2.9%，弱）（OI 145.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.1%｜历史 Rank 64%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 288,695 股

📆 09-28 Forward Structure
存量OI: C 65.5k / P 82.9k，今日变化ΔOI: C +17.6k / P +14.4k，平值价格ATM: C $3.11 / P $3.16 ｜ ATM IV 9.8%，净 delta 敞口 -7k shares
Top ΔOI: P 760 +2,576 ｜ P 725 -2,469 ｜ P 740 +2,447
仓位参考: Max Pain 769 ｜ Call Wall 780（+1.7%）（OI 12.1k） ｜ Put Wall 760（-0.9%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 9.8%｜历史 Rank 64%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 7,180 股

📆 09-29 Forward Structure
存量OI: C 36.2k / P 75.3k，今日变化ΔOI: C +17.8k / P +38.9k，平值价格ATM: C $3.83 / P $3.68 ｜ ATM IV 10.5%，净 delta 敞口 73k shares
Top ΔOI: P 741 +9,535 ｜ P 740 +2,074
仓位参考: Max Pain 765 ｜ Call Wall 780（+1.7%，弱）（OI 1.9k） ｜ Put Wall 748（-2.5%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 10.5%｜历史 Rank 64%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 72,587 股

📆 09-30 Forward Structure
存量OI: C 499.1k / P 1657.6k，今日变化ΔOI: C +46.1k / P +170.7k，平值价格ATM: C $4.46 / P $4.31 ｜ ATM IV 11.3%，净 delta 敞口 -147k shares
Top ΔOI: P 648 +29,654 ｜ P 649 +29,013 ｜ P 676 +18,840
仓位参考: Max Pain 761 ｜ Call Wall 786（+2.5%，弱）（OI 22.0k）
量化解读： 存量 Put 重｜ATM IV 11.3%｜历史 Rank 64%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 146,912 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=28 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=28）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/SPY_evening.json