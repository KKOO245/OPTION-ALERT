# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 10C ΔOI +1,063（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 10.33 → 收盘 10.23（-1.0%） ｜ 今日高 10.35 ｜ 低 10.08 ｜ 昨收 10.06 → 收盘 10.23（+1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.26 | OI比 0.24 | ATM IV 84.6% | Skew 14.3pp | Term 1.01 | ExpMove ±5.3%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 1.01）｜保护溢价显著（Skew 14.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±5.3% ｜ 10-30（9D）±9.7% ｜ 11-06（16D）±14.1% ｜ 11-13（23D）±17.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,952,047 | GEX Change vs 上次快照 159,308 | Flip: Primary Flip: 9.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 228 / LOW 90 / INVALID 118
结构观察区: Primary Flip 9.87（全链重定价，覆盖 99%）
Put Wall 10（弱结构｜现价高于该位 2.3%）
最近结构参考: Put Wall 10（现价高于该位 2.3%）
量化视角： 正 Gamma（195万，无历史分位）｜正 Gamma 增强（+16万）｜现价位于 Flip 上方 3.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构）；上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +2.6k / P -0.7k ｜ Activity HIGH ｜ 2D
10-30  C +1.1k / P -39 ｜ Activity HIGH ｜ 9D
11-06  C +0.2k / P -0.1k ｜ Activity MEDIUM △ ｜ 16D
11-13  C +0.1k / P -33 ｜ Activity MEDIUM △ ｜ 23D

📆 10-23 Forward Structure
存量OI: C 23.7k / P 5.6k，今日变化ΔOI: C +2.6k / P -0.7k，平值价格ATM: C $0.36 / P $0.18 ｜ ATM IV 84.6%，净 delta 敞口 136k shares
Top ΔOI: C 10 +1,063 ｜ P 12 -361
仓位参考: Max Pain 10 ｜ Call Wall 10.5（+2.6%，弱）（OI 2.6k） ｜ Put Wall 9.5（-7.1%）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 84.6%｜历史 Rank 16%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 135,706 股

📆 10-30 Forward Structure
存量OI: C 18.5k / P 8.9k，今日变化ΔOI: C +1.1k / P -39，平值价格ATM: C $0.62 / P $0.37 ｜ ATM IV 78.7%，净 delta 敞口 64k shares
Top ΔOI: C 10 +646 ｜ C 11 +160
仓位参考: Max Pain 12 ｜ Call Wall 11（+7.5%，弱）（OI 2.7k） ｜ Put Wall 10（-2.2%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 78.7%｜历史 Rank 16%（近端代理）｜IV/RV 1.46×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 64,473 股

11-06（MEDIUM △）Top ΔOI: 10C +33
11-06（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 11（+7.5%，弱）（OI 0.4k） ｜ Put Wall 10（-2.2%，弱）（OI 0.8k）

11-13（MEDIUM △）仓位参考: Max Pain 15 ｜ Call Wall 10.5（+2.6%，弱）（OI 0.2k） ｜ Put Wall 11（+7.5%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/USAR_evening.json