# 期权晚报 2026-10-16（快照 21:00 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 428.43 → 收盘 426.70（-0.4%） ｜ 今日高 434.89 ｜ 低 425.52 ｜ 昨收 427.86 → 收盘 426.70（-0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-23，窗口结束前不做对错判定）

Options: P/C成交量 0.49 | OI比 0.75 | ATM IV 71.0% | Skew -1.2pp | Term 0.66 | ExpMove ±7.8%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±7.8% ｜ 10-30（14D）±5.2% ｜ 11-06（21D）±10.8% ｜ 11-13（28D）±10.7%
   ⇒ IV–VIX Spread: +51.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,270,032 | GEX Change vs 上次快照 -2,876,830 | Flip: Primary Flip: 393.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 286 / LOW 85 / INVALID 373
结构观察区: Primary Flip 393.15（全链重定价，覆盖 100%）
Call Wall 420（弱结构｜现价高于该位 1.6%）
最近结构参考: Call Wall 420（现价高于该位 1.6%）
量化视角： 正 Gamma（127万，无历史分位）｜正 Gamma 减弱（288万）｜现价位于 Flip 上方 8.53%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 415（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 393（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 10-23 Forward Structure
存量OI: C 2.7k / P 2.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $16.57 / P $16.70 ｜ ATM IV 71.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 415 ｜ Call Wall 425（-0.4%，弱）（OI 0.5k） ｜ Put Wall 415（-2.7%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 71.0%｜历史 Rank 97%（近端代理）｜IV/RV 2.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 395 ｜ Call Wall 460（+7.8%，弱）（OI 96） ｜ Put Wall 390（-8.6%，弱）（OI 50）

11-06（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 455（+6.6%，弱）（OI 52） ｜ Put Wall 390（-8.6%）（OI 51）

11-13（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 410（-3.9%，弱）（OI 26）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/ISRG_evening.json