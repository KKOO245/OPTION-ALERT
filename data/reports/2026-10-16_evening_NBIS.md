# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 165P ΔOI +1,912（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 184.3）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 181.17 → 收盘 165.47（-8.7%） ｜ 今日高 182.70 ｜ 低 163.27 ｜ 昨收 188.41 → 收盘 165.47（-12.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 0.56 | OI比 0.64 | ATM IV 94.0% | Skew -52.0pp | Term 1.09 | ExpMove ±10.5%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常（Term 1.09）｜Put 保护异常便宜（Skew -52.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±10.5% ｜ 10-30（14D）±14.6% ｜ 11-06（21D）±17.7% ｜ 11-13（28D）±21.3%
   ⇒ IV–VIX Spread: +74.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,910,625 | GEX Change vs 上次快照 -11,172,552 | Flip: Candidates 184.32 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 468 / LOW 41 / INVALID 273
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈184（全链重定价，覆盖 78%，CONDITIONAL）
最近结构参考: Flip 184（现价低于该位 10.2%）
量化视角： 负 Gamma（1091万，无历史分位）｜由正转负（1117万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 184（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +15.2k / P +7.4k ｜ Activity HIGH ｜ 7D
10-30  C +2.9k / P +1.8k ｜ Activity HIGH ｜ 14D
11-06  C +2.8k / P +0.9k ｜ Activity HIGH ｜ 21D
11-13  C +1.6k / P +1.3k ｜ Activity HIGH ｜ 28D

📆 10-23 Forward Structure
存量OI: C 62.6k / P 42.3k，今日变化ΔOI: C +15.2k / P +7.4k，平值价格ATM: C $9.13 / P $8.20 ｜ ATM IV 93.6%，净 delta 敞口 -62k shares
Top ΔOI: P 165 +1,912 ｜ C 200 +1,193
仓位参考: Max Pain 200 ｜ Call Wall 175（+5.8%，弱）（OI 1.2k） ｜ Put Wall 165（-0.3%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 93.6%｜历史 Rank 35%（近端代理）｜IV/RV 1.31×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 62,360 股

📆 10-30 Forward Structure
存量OI: C 33.1k / P 22.6k，今日变化ΔOI: C +2.9k / P +1.8k，平值价格ATM: C $12.50 / P $11.62 ｜ ATM IV 92.9%，净 delta 敞口 11k shares
Top ΔOI: P 155 +386 ｜ C 200 +297
仓位参考: Max Pain 210 ｜ Put Wall 180（+8.8%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 92.9%｜历史 Rank 35%（近端代理）｜IV/RV 1.30×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 11,429 股

📆 11-06 Forward Structure
存量OI: C 22.0k / P 14.4k，今日变化ΔOI: C +2.8k / P +0.9k，平值价格ATM: C $14.75 / P $14.49 ｜ ATM IV 92.7%，净 delta 敞口 38k shares
Top ΔOI: C 230 +1,004 ｜ P 150 +469 ｜ C 200 +325
仓位参考: Max Pain 215 ｜ Put Wall 180（+8.8%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 92.7%｜历史 Rank 35%（近端代理）｜IV/RV 1.30×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 38,442 股

📆 11-13 Forward Structure
存量OI: C 9.3k / P 14.5k，今日变化ΔOI: C +1.6k / P +1.3k，平值价格ATM: C $17.70 / P $17.60 ｜ ATM IV 102.8%，净 delta 敞口 -12k shares
Top ΔOI: P 165 +402 ｜ C 210 +287 ｜ C 180 +198
仓位参考: Max Pain 210 ｜ Call Wall 180（+8.8%，弱）（OI 0.3k） ｜ Put Wall 165（-0.3%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 102.8%｜历史 Rank 35%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 负 11,668 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/NBIS_evening.json