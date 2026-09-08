# 期权晨报 2026-09-08（快照 10:20 ET）

📊 市场环境

SPY $766.61 ｜ QQQ $717.65
VIX 15.64 ↑2.2%（5D -4.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.2（fear）
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

Options: P/C成交量 1.33 | OI比 0.89 | ATM IV 55.0% | Skew 1.6pp | Term 0.87 | ExpMove ±4.2%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜当日成交偏 Put（P/C量 1.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.33×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（3D）±4.2% ｜ 09-18（10D）±6.7% ｜ 09-25（17D）±8.3% ｜ 10-02（24D）±9.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 26,692,964 | GEX Change vs 上次快照 -12,690,183 | Flip: Primary Flip: 165.95（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 621 / LOW 76 / INVALID 155
结构观察区: Primary Flip 165.95（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 1.0%）
最近结构参考: Put Wall 170（现价高于该位 1.0%）
量化视角： 正 Gamma（2669万，无历史分位）｜正 Gamma 减弱（1269万）｜现价位于 Flip 上方 3.47%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
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
平值价格ATM:  C 3.35 / P 3.85
隐含波动率 ATM IV:  55.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 172（结算参考） ｜ Call Wall 177.5（+3.4%，弱）（OI 10.7k）
量化解读： 存量两侧均衡｜ATM IV 55.0%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 150（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 175（结算参考） ｜ Put Wall 170（-1.0%）（OI 7.4k）

10-02（Activity LOW）仓位参考: Max Pain 175（结算参考） ｜ Call Wall 180（+4.8%，弱）（OI 2.4k） ｜ Put Wall 160（-6.8%，弱）（OI 2.8k）

📅 事件差分（观察，非因果）: 09-11（3D）ATM IV 55.0% vs 09-18 49.6%（差 +5.4pp）——覆盖 PPI 生产者物价 MoM、成屋销售、Core Inflation Rate MoM、Inflation Rate MoM、Inflation Rate YoY、Core Inflation Rate YoY、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/PLTR_morning.json