# 期权晚报 2026-10-06（快照 21:00 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 593.54 → 收盘 589.45（-0.7%） ｜ 今日高 596.39 ｜ 低 588.64 ｜ 昨收 589.51 → 收盘 589.45（-0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 4.09 | OI比 1.56 | ATM IV 31.7% | Skew 3.1pp | Term 1.13 | ExpMove ±2.3%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构正常（Term 1.13）｜保护溢价中性（Skew 3.1pp）｜当日成交偏 Put（P/C量 4.09）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.09×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.56×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±2.3% ｜ 10-16（10D）±4.3% ｜ 10-23（17D）±6.3% ｜ 10-30（24D）±7.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,992,055 | GEX Change vs 上次快照 533,726 | Flip: Primary Flip: 574.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 507 / LOW 256 / INVALID 737
结构观察区: Primary Flip 574.76（全链重定价，覆盖 85%）
Call Wall 600（现价低于该位 1.8%）
最近结构参考: Call Wall 600（现价低于该位 1.8%）
量化视角： 正 Gamma（899万，无历史分位）｜正 Gamma 增强（+53万）｜现价位于 Flip 上方 2.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 555（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 575（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-09 Forward Structure
存量OI: C 5.6k / P 8.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.70 / P $7.00 ｜ ATM IV 31.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 555 ｜ Put Wall 555（-5.8%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 31.7%｜历史 Rank 43%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 530 ｜ Call Wall 600（+1.8%）（OI 8.9k）

10-23（Activity LOW）仓位参考: Max Pain 540 ｜ Call Wall 555（-5.8%，弱）（OI 92）

10-30（Activity LOW）仓位参考: Max Pain 555

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SOXX_evening.json