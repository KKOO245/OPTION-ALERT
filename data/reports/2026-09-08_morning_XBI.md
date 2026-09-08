# 期权晨报 2026-09-08（快照 10:49 ET）

📊 市场环境

SPY $765.75 ｜ QQQ $718.36
VIX 15.51 ↑1.4%（5D -5.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 40.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.99 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 163.81 → 今开 160.76（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 162.71 ｜ 低 158.79

Options: P/C成交量 1.11 | OI比 1.80 | ATM IV 26.9% | Skew 2.6pp | Term 1.10 | ExpMove ±3.0%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常（Term 1.10）｜保护溢价中性（Skew 2.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.80×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（3D）±3.0% ｜ 09-18（10D）±6.3% ｜ 09-25（17D）±5.8% ｜ 10-02（24D）±6.2%
   ⇒ IV–VIX Spread: +11.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -19,996,281 | GEX Change vs 上次快照 -10,170,742 | Flip: Primary Flip: 165.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 380 / LOW 110 / INVALID 362
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 165.32（全链重定价，覆盖 94%）
Put Wall 158（弱结构｜现价高于该位 2.7%） | Call Wall 170（弱结构｜现价低于该位 4.5%）
最近结构参考: Flip 165（现价低于该位 1.8%）
量化视角： 负 Gamma（2000万，无历史分位）｜负 Gamma 加深（1017万）｜现价位于 Flip 下方 1.83%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 158（Put Wall，弱结构）；上方 163（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 10D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-11 Forward Structure
存量OI:      C 8.5k / P 15.4k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.10 / P 1.70
隐含波动率 ATM IV:  26.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 163（结算参考） ｜ Call Wall 164（+1.1%，弱）（OI 2.0k） ｜ Put Wall 162（-0.2%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜ATM IV 26.9%｜历史 Rank 14%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 158（结算参考） ｜ Call Wall 155（-4.5%，弱）（OI 10.8k） ｜ Put Wall 158（-2.6%，弱）（OI 16.9k）

09-25（Activity LOW）仓位参考: Max Pain 160（结算参考） ｜ Call Wall 167（+2.9%）（OI 1.4k）

10-02（Activity LOW）仓位参考: Max Pain 164（结算参考） ｜ Call Wall 165（+1.7%）（OI 0.2k） ｜ Put Wall 150（-7.6%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=13 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=13）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/XBI_morning.json