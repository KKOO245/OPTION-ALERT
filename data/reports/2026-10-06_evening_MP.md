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
🟡 **近现价集中开仓**: 10-09 50C ΔOI +765（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 56C ΔOI +822 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 47.40 → 收盘 48.53（+2.4%） ｜ 今日高 48.65 ｜ 低 47.30 ｜ 昨收 46.84 → 收盘 48.53（+3.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.56 | OI比 0.84 | ATM IV 60.3% | Skew -4.2pp | Term 0.99 | ExpMove ±4.6%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构正常（Term 0.99）｜Put 保护异常便宜（Skew -4.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.6% ｜ 10-16（10D）±7.3% ｜ 10-23（17D）±9.8% ｜ 10-30（24D）±11.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 565,728 | GEX Change vs 上次快照 595,981 | Flip: Primary Flip: 48.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 268 / LOW 53 / INVALID 115
结构观察区: Primary Flip 48.26（全链重定价，覆盖 99%）
Put Wall 45（现价高于该位 7.8%） | Call Wall 50（弱结构｜现价低于该位 2.9%）
最近结构参考: Flip 48（现价高于该位 0.6%）
量化视角： 正 Gamma（57万，无历史分位）｜由负转正（+60万）｜现价位于 Flip 上方 0.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall） / 48（MaxPain，仅结算参考）；上方 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +2.5k / P +2.2k ｜ Activity HIGH ｜ 3D
10-16  C +0.3k / P +32 ｜ Activity MEDIUM △ ｜ 10D
10-23  C +0.4k / P +0.1k ｜ Activity HIGH ｜ 17D
10-30  C +1.3k / P +48 ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 10.9k / P 9.2k，今日变化ΔOI: C +2.5k / P +2.2k，平值价格ATM: C $1.07 / P $1.18 ｜ ATM IV 60.3%，净 delta 敞口 65k shares
Top ΔOI: P 45 +809 ｜ C 50 +765 ｜ P 45 +622
仓位参考: Max Pain 48 ｜ Call Wall 50（+3.0%，弱）（OI 1.8k） ｜ Put Wall 47（-3.2%）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 60.3%｜历史 Rank 37%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 65,116 股

10-16（MEDIUM △）Top ΔOI: 52C +90
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+3.0%，弱）（OI 4.0k） ｜ Put Wall 45（-7.3%，弱）（OI 4.4k）

📆 10-23 Forward Structure
存量OI: C 2.6k / P 1.7k，今日变化ΔOI: C +0.4k / P +0.1k，平值价格ATM: C $2.22 / P $2.52 ｜ ATM IV 53.9%，净 delta 敞口 -4k shares
仓位参考: Max Pain 51 ｜ Call Wall 53（+9.2%，弱）（OI 0.2k） ｜ Put Wall 45（-7.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 53.9%｜历史 Rank 37%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 3,558 股

📆 10-30 Forward Structure
存量OI: C 4.3k / P 2.1k，今日变化ΔOI: C +1.3k / P +48，平值价格ATM: C $2.41 / P $3.00 ｜ ATM IV 54.6%，净 delta 敞口 33k shares
Top ΔOI: C 49 +242
仓位参考: Max Pain 49 ｜ Call Wall 49（+1.0%，弱）（OI 0.3k） ｜ Put Wall 45（-7.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 54.6%｜历史 Rank 37%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 正 32,745 股

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 60.3% vs 10-16 53.8%（差 +6.5pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/MP_evening.json