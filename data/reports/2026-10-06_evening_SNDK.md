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
🟡 **近现价集中开仓**: 10-09 1600P ΔOI +620（距现价 -3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,700.00 → 收盘 1,660.46（-2.3%） ｜ 今日高 1716.50 ｜ 低 1650.00 ｜ 昨收 1,704.16 → 收盘 1,660.46（-2.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-09，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 1.06 | ATM IV 58.1% | Skew -0.1pp | Term 1.08 | ExpMove ±4.2%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.06×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.2% ｜ 10-16（10D）±7.5% ｜ 10-23（17D）±10.5% ｜ 10-30（24D）±12.9%
   ⇒ IV–VIX Spread: +43.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,136,645 | GEX Change vs 上次快照 -1,947,137 | Flip: Primary Flip: 1702.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1540 / LOW 420 / INVALID 1140
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1702.66（全链重定价，覆盖 100%）
最近结构参考: Flip 1703（现价低于该位 2.5%）
量化视角： 负 Gamma（514万，无历史分位）｜负 Gamma 加深（195万）｜现价位于 Flip 下方 2.48%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1703（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +6.6k / P +6.3k ｜ Activity HIGH ｜ 3D
10-16  C +1.6k / P +0.8k ｜ Activity MEDIUM △ ｜ 10D
10-23  C +0.9k / P +1.2k ｜ Activity HIGH ｜ 17D
10-30  C +0.8k / P +0.9k ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 32.8k / P 34.9k，今日变化ΔOI: C +6.6k / P +6.3k，平值价格ATM: C $35.74 / P $33.64 ｜ ATM IV 58.1%，净 delta 敞口 -60k shares
Top ΔOI: P 1550 +712 ｜ C 1900 +709 ｜ P 1600 +620
仓位参考: Max Pain 1,700 ｜ Call Wall 1800（+8.4%，弱）（OI 1.9k） ｜ Put Wall 1600（-3.6%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.1%｜历史 Rank 16%（近端代理）｜IV/RV 0.94×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 60,352 股

10-16（MEDIUM △）Top ΔOI: 2000C +297 ｜ 1800C +249
10-16（MEDIUM △）仓位参考: Max Pain 1,670 ｜ Call Wall 1800（+8.4%，弱）（OI 1.5k） ｜ Put Wall 1500（-9.7%，弱）（OI 1.7k）

📆 10-23 Forward Structure
存量OI: C 8.7k / P 10.0k，今日变化ΔOI: C +0.9k / P +1.2k，平值价格ATM: C $93.60 / P $81.10 ｜ ATM IV 57.4%，净 delta 敞口 4k shares
Top ΔOI: C 1700 +167 ｜ P 1500 +127
仓位参考: Max Pain 1,710 ｜ Call Wall 1800（+8.4%，弱）（OI 0.4k） ｜ Put Wall 1500（-9.7%）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 57.4%｜历史 Rank 16%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,923 股

📆 10-30 Forward Structure
存量OI: C 5.5k / P 9.0k，今日变化ΔOI: C +0.8k / P +0.9k，平值价格ATM: C $110.12 / P $104.20 ｜ ATM IV 63.1%，净 delta 敞口 6k shares
Top ΔOI: C 1700 +140 ｜ P 1700 +118
仓位参考: Max Pain 1,710 ｜ Call Wall 1700（+2.4%，弱）（OI 0.3k） ｜ Put Wall 1500（-9.7%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 63.1%｜历史 Rank 16%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 5,719 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=42 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=42）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SNDK_evening.json