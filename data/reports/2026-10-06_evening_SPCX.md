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
🟡 **近现价集中开仓**: 10-09 177C ΔOI +14,137（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-12 180C ΔOI +2,778 占该期限总 OI 11.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 172.10 → 收盘 171.92（-0.1%） ｜ 今日高 176.42 ｜ 低 171.39 ｜ 昨收 171.09 → 收盘 171.92（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.69 | OI比 1.15 | ATM IV 50.3% | Skew -1.6pp | Term 0.98 | ExpMove ±3.7%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±3.7% ｜ 10-12（6D）±4.4% ｜ 10-14（8D）±5.2% ｜ 10-16（10D）±6.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 125,579,192 | GEX Change vs 上次快照 -6,785,300 | Flip: Primary Flip: 158.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 585 / LOW 79 / INVALID 560
结构观察区: Primary Flip 158.30（全链重定价，覆盖 98%）
Call Wall 160（弱结构｜现价高于该位 7.4%）
最近结构参考: Call Wall 160（现价高于该位 7.4%）
量化视角： 正 Gamma（1.26亿，无历史分位）｜正 Gamma 减弱（679万）｜现价位于 Flip 上方 8.61%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +39.5k / P +63.0k ｜ Activity HIGH ｜ 3D
10-12  C +15.5k / P +8.2k ｜ Activity HIGH ｜ 6D
10-14  C N/A / P N/A ｜ Activity LOW ｜ 8D（新上架）
10-16  C +3.5k / P -8.9k ｜ Activity MEDIUM △ ｜ 10D

📆 10-09 Forward Structure
存量OI: C 168.8k / P 193.4k，今日变化ΔOI: C +39.5k / P +63.0k，平值价格ATM: C $2.94 / P $3.40 ｜ ATM IV 50.3%，净 delta 敞口 -313k shares
Top ΔOI: P 160 +16,467 ｜ C 177 +14,137 ｜ P 165 +10,977
仓位参考: Max Pain 160 ｜ Call Wall 180（+4.7%）（OI 24.1k） ｜ Put Wall 160（-6.9%，弱）（OI 19.6k）
量化解读： 存量两侧均衡｜ATM IV 50.3%｜历史 Rank 33%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 313,015 股

📆 10-12 Forward Structure
存量OI: C 15.5k / P 8.2k，今日变化ΔOI: C +15.5k / P +8.2k，平值价格ATM: C $3.50 / P $4.00 ｜ ATM IV 42.2%，净 delta 敞口 422k shares
Top ΔOI: C 180 +2,778 ｜ C 170 +2,269 ｜ C 190 +2,001
仓位参考: Max Pain 165 ｜ Call Wall 180（+4.7%，弱）（OI 2.8k） ｜ Put Wall 165（-4.0%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 42.2%｜历史 Rank 33%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 421,517 股

10-16（MEDIUM △）Top ΔOI: 185C +14,782
10-16（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 160（-6.9%，弱）（OI 36.0k） ｜ Put Wall 155（-9.8%，弱）（OI 12.9k）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 50.3% vs 10-12 42.2%（差 +8.2pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SPCX_evening.json