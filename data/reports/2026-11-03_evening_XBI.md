# 期权晚报 2026-11-03（快照 16:41 ET）

📊 市场环境

SPY $754.35 ｜ QQQ $685.28
VIX 20.83 ↓1.5%（5D +18.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 149P ΔOI +167（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 152.96 → 收盘 154.97（+1.3%） ｜ 今日高 156.92 ｜ 低 152.83 ｜ 昨收 152.05 → 收盘 154.97（+1.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.57 | OI比 1.73 | ATM IV 43.8% | Skew 6.0pp | Term 0.85 | ExpMove ±3.2%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 6.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.73×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±3.2% ｜ 11-13（10D）±5.3% ｜ 11-20（17D）±6.7% ｜ 11-27（24D）±8.1%
   ⇒ IV–VIX Spread: +22.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,832,167 | GEX Change vs 上次快照 -405,972 | Flip: Primary Flip: 159.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 348 / LOW 79 / INVALID 345
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.22（全链重定价，覆盖 95%）
Put Wall 145（现价高于该位 6.9%） | Call Wall 165（现价低于该位 6.1%）
最近结构参考: Flip 159（现价低于该位 2.7%）
量化视角： 负 Gamma（683万，无历史分位）｜负 Gamma 加深（41万）｜现价位于 Flip 下方 2.67%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（Put Wall） / 153（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.2k / P +0.8k ｜ Activity MEDIUM △ ｜ 3D
11-13  C +0.3k / P +96 ｜ Activity HIGH ｜ 10D
11-20  C +0.2k / P -0.6k ｜ Activity HIGH ｜ 17D
11-27  C +0.1k / P +39 ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 5.6k / P 9.7k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $2.67 / P $2.30 ｜ ATM IV 43.8%，净 delta 敞口 -12k shares
Top ΔOI: P 152 +202 ｜ P 149 +167 ｜ P 150 +90
仓位参考: Max Pain 153 ｜ Call Wall 159（+2.6%，弱）（OI 0.4k） ｜ Put Wall 153（-1.3%）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 43.8%｜历史 Rank 92%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 12,047 股

📆 11-13 Forward Structure
存量OI: C 2.2k / P 2.0k，今日变化ΔOI: C +0.3k / P +96，平值价格ATM: C $4.35 / P $3.85 ｜ ATM IV 40.4%，净 delta 敞口 6k shares
Top ΔOI: C 157 +79 ｜ C 160 +41 ｜ C 158 +36
仓位参考: Max Pain 153 ｜ Call Wall 160（+3.2%）（OI 0.5k） ｜ Put Wall 148（-4.5%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 40.4%｜历史 Rank 92%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,865 股

📆 11-20 Forward Structure
存量OI: C 23.4k / P 46.0k，今日变化ΔOI: C +0.2k / P -0.6k，平值价格ATM: C $5.37 / P $5.00 ｜ ATM IV 40.0%，净 delta 敞口 11k shares
Top ΔOI: P 145 -1,299 ｜ P 144 +781
仓位参考: Max Pain 155 ｜ Call Wall 165（+6.5%）（OI 7.1k） ｜ Put Wall 145（-6.4%，弱）（OI 9.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.0%｜历史 Rank 92%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,806 股

📆 11-27 Forward Structure
存量OI: C 1.0k / P 1.3k，今日变化ΔOI: C +0.1k / P +39，平值价格ATM: C $6.60 / P $5.88 ｜ ATM IV 37.9%，净 delta 敞口 6k shares
Top ΔOI: C 152 +127 ｜ C 160 +18 ｜ P 153 +14
仓位参考: Max Pain 157 ｜ Call Wall 152.5（-1.6%，弱）（OI 0.1k） ｜ Put Wall 156（+0.7%）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.9%｜历史 Rank 92%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 正 6,386 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/XBI_evening.json