# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 180C ΔOI +1,210（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 174.80 → 收盘 172.00（-1.6%） ｜ 今日高 179.05 ｜ 低 171.81 ｜ 昨收 178.45 → 收盘 172.00（-3.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-13，窗口结束前不做对错判定）

Options: P/C成交量 0.32 | OI比 0.55 | ATM IV 65.1% | Skew -4.6pp | Term 1.00 | ExpMove ±2.9%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -4.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.9% ｜ 10-16（8D）±6.3% ｜ 10-23（15D）±8.2% ｜ 10-30（22D）±12.7%
   ⇒ IV–VIX Spread: +49.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,527,457 | GEX Change vs 上次快照 362,770 | Flip: Primary Flip: 173.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 425 / LOW 124 / INVALID 295
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 173.54（全链重定价，覆盖 90%）
最近结构参考: Flip 174（现价低于该位 0.9%）
量化视角： 负 Gamma（353万，无历史分位）｜负 Gamma 缓解（+36万）｜现价位于 Flip 下方 0.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 185（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 174（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +2.8k / P +2.3k ｜ Activity HIGH ｜ 1D
10-16  C +5.3k / P +1.0k ｜ Activity HIGH ｜ 8D
10-23  C +1.0k / P +1.0k ｜ Activity HIGH ｜ 15D
10-30  C +0.7k / P +0.4k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 71.4k / P 39.5k，今日变化ΔOI: C +2.8k / P +2.3k，平值价格ATM: C $2.40 / P $2.60 ｜ ATM IV 65.1%，净 delta 敞口 -25k shares
Top ΔOI: C 185 +1,322 ｜ C 180 +1,210
仓位参考: Max Pain 185 ｜ Call Wall 187.5（+9.0%，弱）（OI 8.7k） ｜ Put Wall 177.5（+3.2%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 65.1%｜历史 Rank 21%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 负 24,563 股

📆 10-16 Forward Structure
存量OI: C 91.3k / P 81.1k，今日变化ΔOI: C +5.3k / P +1.0k，平值价格ATM: C $5.70 / P $5.20 ｜ ATM IV 55.4%，净 delta 敞口 43k shares
Top ΔOI: C 185 +427
仓位参考: Max Pain 180 ｜ Call Wall 185（+7.6%，弱）（OI 2.4k） ｜ Put Wall 165（-4.1%，弱）（OI 3.4k）
量化解读： 存量两侧均衡｜ATM IV 55.4%｜历史 Rank 21%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 42,893 股

📆 10-23 Forward Structure
存量OI: C 9.3k / P 8.3k，今日变化ΔOI: C +1.0k / P +1.0k，平值价格ATM: C $7.78 / P $6.28 ｜ ATM IV 55.4%，净 delta 敞口 -16k shares
Top ΔOI: P 157 +239 ｜ P 170 +187
仓位参考: Max Pain 188 ｜ Call Wall 187.5（+9.0%，弱）（OI 0.5k） ｜ Put Wall 170（-1.2%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.4%｜历史 Rank 21%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 16,474 股

📆 10-30 Forward Structure
存量OI: C 9.4k / P 8.1k，今日变化ΔOI: C +0.7k / P +0.4k，平值价格ATM: C $12.25 / P $9.50 ｜ ATM IV 65.1%，净 delta 敞口 4k shares
Top ΔOI: C 200 +314 ｜ C 180 +146 ｜ P 180 +124
仓位参考: Max Pain 185 ｜ Call Wall 185（+7.6%，弱）（OI 1.2k） ｜ Put Wall 170（-1.2%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 65.1%｜历史 Rank 21%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 正 4,128 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 65.1% vs 10-16 55.4%（差 +9.7pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/COIN_evening.json