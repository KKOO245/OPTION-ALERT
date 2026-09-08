# 期权晨报 2026-09-08（快照 10:49 ET）

📊 市场环境

SPY $765.76 ｜ QQQ $718.36
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


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 174.33 → 今开 173.10（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 175.82 ｜ 低 170.70

Options: P/C成交量 1.17 | OI比 0.89 | ATM IV 53.6% | Skew 1.2pp | Term 0.89 | ExpMove ±4.0%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜当日成交偏 Put（P/C量 1.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.17×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（3D）±4.0% ｜ 09-18（10D）±6.6% ｜ 09-25（17D）±8.3% ｜ 10-02（24D）±10.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,597,956 | GEX Change vs 上次快照 -10,785,191 | Flip: Primary Flip: 166.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 593 / LOW 78 / INVALID 181
结构观察区: Primary Flip 166.25（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 1.3%）
最近结构参考: Put Wall 170（现价高于该位 1.3%）
量化视角： 正 Gamma（2860万，无历史分位）｜正 Gamma 减弱（1079万）｜现价位于 Flip 上方 3.61%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构）；上方 172（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 100%）。
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
存量OI:      C 106.0k / P 94.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.62 / P 3.36
隐含波动率 ATM IV:  53.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 172（结算参考） ｜ Call Wall 177.5（+3.1%，弱）（OI 10.7k）
量化解读： 存量两侧均衡｜ATM IV 53.6%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 150（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 175（结算参考） ｜ Put Wall 170（-1.3%）（OI 7.4k）

10-02（Activity LOW）仓位参考: Max Pain 175（结算参考） ｜ Call Wall 180（+4.5%，弱）（OI 2.4k） ｜ Put Wall 160（-7.1%，弱）（OI 2.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/PLTR_morning.json