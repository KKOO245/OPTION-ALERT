# 期权晚报 2026-10-06（快照 16:40 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 305P ΔOI +566（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 295.25 → 收盘 295.78（+0.2%） ｜ 今日高 300.80 ｜ 低 285.64 ｜ 昨收 286.65 → 收盘 295.78（+3.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.71 | OI比 1.17 | ATM IV 72.0% | Skew -0.3pp | Term 1.13 | ExpMove ±5.4%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 1.13）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±5.4% ｜ 10-16（10D）±8.8% ｜ 10-23（17D）±11.5% ｜ 10-30（24D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,373,615 | GEX Change vs 上次快照 136,557 | Flip: Primary Flip: 276.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 588 / LOW 91 / INVALID 153
结构观察区: Primary Flip 276.51（全链重定价，覆盖 100%）
Call Wall 300（弱结构｜现价低于该位 1.4%）
最近结构参考: Call Wall 300（现价低于该位 1.4%）
量化视角： 正 Gamma（1137万，无历史分位）｜正 Gamma 增强（+14万）｜现价位于 Flip 上方 6.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 280（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 277（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +7.6k / P +9.8k ｜ Activity HIGH ｜ 3D
10-16  C +1.0k / P +4.2k ｜ Activity HIGH ｜ 10D
10-23  C +0.3k / P -0.3k ｜ Activity MEDIUM △ ｜ 17D
10-30  C +0.2k / P +1.9k ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 31.6k / P 36.9k，今日变化ΔOI: C +7.6k / P +9.8k，平值价格ATM: C $8.77 / P $7.29 ｜ ATM IV 72.0%，净 delta 敞口 198k shares
Top ΔOI: C 267 +874
仓位参考: Max Pain 280 ｜ Call Wall 300（+1.4%）（OI 2.8k） ｜ Put Wall 280（-5.3%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜ATM IV 72.0%｜历史 Rank 29%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 197,530 股

📆 10-16 Forward Structure
存量OI: C 77.8k / P 89.0k，今日变化ΔOI: C +1.0k / P +4.2k，平值价格ATM: C $14.08 / P $12.08 ｜ ATM IV 67.3%，净 delta 敞口 -23k shares
Top ΔOI: P 230 +1,593 ｜ P 305 +566
仓位参考: Max Pain 270 ｜ Call Wall 270（-8.7%，弱）（OI 7.6k） ｜ Put Wall 275（-7.0%，弱）（OI 3.3k）
量化解读： 存量两侧均衡｜ATM IV 67.3%｜历史 Rank 29%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 22,696 股

10-23（MEDIUM △）Top ΔOI: 230P -644
10-23（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 300（+1.4%，弱）（OI 1.1k） ｜ Put Wall 280（-5.3%，弱）（OI 0.7k）

📆 10-30 Forward Structure
存量OI: C 9.1k / P 19.1k，今日变化ΔOI: C +0.2k / P +1.9k，平值价格ATM: C $26.00 / P $21.40 ｜ ATM IV 76.4%，净 delta 敞口 -6k shares
仓位参考: Max Pain 285 ｜ Call Wall 300（+1.4%，弱）（OI 1.3k） ｜ Put Wall 285（-3.6%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 76.4%｜历史 Rank 29%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 负 5,922 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/BE_evening.json