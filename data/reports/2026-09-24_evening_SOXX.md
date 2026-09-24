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
🟡 **近现价集中开仓**: 09-25 550P ΔOI +265（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 554.97 → 收盘 566.07（+2.0%） ｜ 今日高 566.81 ｜ 低 553.24 ｜ 昨收 565.72 → 收盘 566.07（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.63 | OI比 1.63 | ATM IV 30.3% | Skew 0.7pp | Term 1.24 | ExpMove ±1.7%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常偏陡（Term 1.24）｜保护溢价薄（Skew 0.7pp）｜当日成交偏 Put（P/C量 1.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.63×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.63×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±1.7% ｜ 10-02（8D）±4.1% ｜ 10-09（15D）±6.0% ｜ 10-16（22D）±7.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,788,886 | GEX Change vs 上次快照 -8,068,230 | Flip: Primary Flip: 556.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 595 / LOW 321 / INVALID 668
结构观察区: Primary Flip 556.31（全链重定价，覆盖 96%）
Call Wall 600（现价低于该位 5.7%）
最近结构参考: Flip 556（现价高于该位 1.8%）
量化视角： 正 Gamma（779万，无历史分位）｜正 Gamma 减弱（807万）｜现价位于 Flip 上方 1.75%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 545（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 556（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +96 / P +1.8k ｜ Activity HIGH ｜ 1D
10-02  C +2.5k / P +2.7k ｜ Activity HIGH ｜ 8D（新行权价 C 19）
10-09  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 15D
10-16  C -3.2k / P +3.1k ｜ Activity MEDIUM △ ｜ 22D

📆 09-25 Forward Structure
存量OI: C 11.6k / P 19.0k，今日变化ΔOI: C +96 / P +1.8k，平值价格ATM: C $4.58 / P $4.97 ｜ ATM IV 30.3%，净 delta 敞口 -51k shares
Top ΔOI: P 555 +432 ｜ P 545 +427 ｜ P 550 +265
仓位参考: Max Pain 545 ｜ Call Wall 580（+2.5%，弱）（OI 2.1k） ｜ Put Wall 550（-2.8%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 30.3%｜历史 Rank 38%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 50,691 股

📆 10-02 Forward Structure
存量OI: C 14.7k / P 14.6k，今日变化ΔOI: C +2.5k / P +2.7k（新行权价 C 19），平值价格ATM: C $12.00 / P $11.40 ｜ ATM IV 36.8%，净 delta 敞口 -34k shares
Top ΔOI: C 582 +2,205 ｜ P 540 +835 ｜ P 560 +816
仓位参考: Max Pain 542 ｜ Call Wall 542.5（-4.2%，弱）（OI 2.8k） ｜ Put Wall 540（-4.6%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.8%｜历史 Rank 38%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 负 33,872 股

10-09（MEDIUM △）Top ΔOI: 550C +134 ｜ 570C +102
10-09（MEDIUM △）仓位参考: Max Pain 522 ｜ Call Wall 537.5（-5.0%，弱）（OI 0.4k） ｜ Put Wall 547.5（-3.3%，弱）（OI 87）

10-16（MEDIUM △）Top ΔOI: 400P +3,147 ｜ 530P +2,400
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 600（+6.0%）（OI 11.3k） ｜ Put Wall 530（-6.4%，弱）（OI 4.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/SOXX_evening.json