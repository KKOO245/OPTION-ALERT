# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $721.45
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 16.96 → 收盘 15.73（-7.3%） ｜ 今日高 17.17 ｜ 低 15.40 ｜ 昨收 16.97 → 收盘 15.73（-7.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-25，窗口结束前不做对错判定）

Options: P/C成交量 3.26 | OI比 0.39 | ATM IV 164.0% | Skew -29.8pp | Term 0.48 | ExpMove ±7.9%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜Put 保护异常便宜（Skew -29.8pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.39）+ 当日成交偏 Put（P/C量 3.26）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 3.26×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±7.9% ｜ 10-02（14D）±12.4% ｜ 10-09（21D）±14.5% ｜ 10-16（28D）±17.9%
   ⇒ IV–VIX Spread: +149.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,089,369 | GEX Change vs 上次快照 1,196,680 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 74%（带内） ｜ IV 有效性: VALID 141 / LOW 86 / INVALID 223
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 15（现价高于该位 4.9%）
最近结构参考: Put Wall 15（现价高于该位 4.9%）
量化视角： 正 Gamma（109万，无历史分位）｜由负转正（+120万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 18（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0.3k / P +0.1k ｜ Activity HIGH ｜ 7D
10-02  C +98 / P +44 ｜ Activity MEDIUM △ ｜ 14D
10-09  C +35 / P +15 ｜ Activity MEDIUM △ ｜ 21D
10-16  C +1.4k / P -0.2k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 5.5k / P 2.4k，今日变化ΔOI: C +0.3k / P +0.1k，平值价格ATM: C $0.65 / P $0.59 ｜ ATM IV 73.9%，净 delta 敞口 -6k shares
仓位参考: Max Pain 18 ｜ Put Wall 15（-4.6%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 73.9%｜历史 Rank 92%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 5,749 股

10-02（MEDIUM △）Top ΔOI: 16P +31
10-02（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（-4.6%）（OI 0.2k）

10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（+1.7%）（OI 0.1k）

📆 10-16 Forward Structure
存量OI: C 19.7k / P 6.0k，今日变化ΔOI: C +1.4k / P -0.2k，平值价格ATM: C $1.30 / P $1.52 ｜ ATM IV 79.0%，净 delta 敞口 52k shares
Top ΔOI: C 18 +1,134 ｜ P 34 -100
仓位参考: Max Pain 20 ｜ Put Wall 15（-4.6%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 79.0%｜历史 Rank 92%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 52,132 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/NNE_evening.json