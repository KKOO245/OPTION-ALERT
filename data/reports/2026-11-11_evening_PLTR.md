# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $690.38
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 172C ΔOI +3,317（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 173.31 → 收盘 172.40（-0.5%） ｜ 今日高 175.41 ｜ 低 170.80 ｜ 昨收 168.82 → 收盘 172.40（+2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.57 | OI比 0.62 | ATM IV 54.3% | Skew 3.0pp | Term 0.88 | ExpMove ±3.2%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.0pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±3.2% ｜ 11-20（9D）±6.3% ｜ 11-27（16D）±7.8% ｜ 12-04（23D）±9.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 56,021,017 | GEX Change vs 上次快照 3,586,836 | Flip: Primary Flip: 160.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 544 / LOW 191 / INVALID 199
结构观察区: Primary Flip 160.24（全链重定价，覆盖 99%）
Call Wall 165（弱结构｜现价高于该位 4.5%）
最近结构参考: Call Wall 165（现价高于该位 4.5%）
量化视角： 正 Gamma（5602万，无历史分位）｜正 Gamma 增强（+359万）｜现价位于 Flip 上方 7.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考） / 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +5.1k / P +0.9k ｜ Activity MEDIUM △ ｜ 2D
11-20  C +1.7k / P -0.4k ｜ Activity MEDIUM △ ｜ 9D
11-27  C +0.7k / P +1.1k ｜ Activity HIGH ｜ 16D
12-04  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 138.4k / P 85.8k，今日变化ΔOI: C +5.1k / P +0.9k，平值价格ATM: C $2.73 / P $2.78 ｜ ATM IV 54.3%，净 delta 敞口 170k shares
Top ΔOI: C 172 +3,317 ｜ C 180 +1,159 ｜ C 177 +1,071
仓位参考: Max Pain 162 ｜ Call Wall 165（-4.3%，弱）（OI 13.7k） ｜ Put Wall 165（-4.3%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 54.3%｜历史 Rank 61%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 170,345 股

11-20（MEDIUM △）Top ΔOI: 167C +1,073
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 180（+4.4%，弱）（OI 10.7k） ｜ Put Wall 185（+7.3%，弱）（OI 9.9k）

📆 11-27 Forward Structure
存量OI: C 17.3k / P 22.0k，今日变化ΔOI: C +0.7k / P +1.1k，平值价格ATM: C $6.90 / P $6.54 ｜ ATM IV 47.2%，净 delta 敞口 25k shares
Top ΔOI: C 180 +388
仓位参考: Max Pain 175 ｜ Call Wall 180（+4.4%，弱）（OI 1.3k） ｜ Put Wall 160（-7.2%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 47.2%｜历史 Rank 61%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 24,755 股

12-04（MEDIUM △）Top ΔOI: 150P +395 ｜ 185C +89
12-04（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 185（+7.3%，弱）（OI 1.1k） ｜ Put Wall 160（-7.2%，弱）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/PLTR_evening.json