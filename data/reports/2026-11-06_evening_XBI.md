# 期权晚报 2026-11-06（快照 21:00 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 25.64 ↓9.0%（5D +32.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 148.82 → 收盘 152.21（+2.3%） ｜ 今日高 152.92 ｜ 低 147.56 ｜ 昨收 148.40 → 收盘 152.21（+2.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 1.83 | OI比 1.54 | ATM IV 41.0% | Skew 3.5pp | Term 0.90 | ExpMove ±4.0%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构正常（Term 0.90）｜保护溢价中性（Skew 3.5pp）｜当日成交偏 Put（P/C量 1.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.83×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.54×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±4.0% ｜ 11-20（14D）±5.9% ｜ 11-27（21D）±10.5% ｜ 12-04（28D）±6.8%
   ⇒ IV–VIX Spread: +15.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,499,589 | GEX Change vs 上次快照 6,612,064 | Flip: Primary Flip: 157.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 298 / LOW 74 / INVALID 282
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 157.91（全链重定价，覆盖 95%）
Put Wall 145（弱结构｜现价高于该位 5.0%）
最近结构参考: Flip 158（现价低于该位 3.6%）
量化视角： 负 Gamma（850万，无历史分位）｜负 Gamma 缓解（+661万）｜现价位于 Flip 下方 3.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（Put Wall，弱结构）；上方 154（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 21D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 11-13 Forward Structure
存量OI: C 3.1k / P 4.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.20 / P $2.81 ｜ ATM IV 41.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 154 ｜ Call Wall 160（+5.1%）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 41.0%｜历史 Rank 86%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 154 ｜ Call Wall 160（+5.1%，弱）（OI 2.2k） ｜ Put Wall 145（-4.7%，弱）（OI 7.2k）

11-27（Activity LOW）仓位参考: Max Pain 158 ｜ Call Wall 152.5（+0.2%，弱）（OI 0.1k） ｜ Put Wall 156（+2.5%）（OI 0.2k）

12-04（Activity LOW）仓位参考: Max Pain 161 ｜ Call Wall 162（+6.4%，弱）（OI 44） ｜ Put Wall 147（-3.4%，弱）（OI 45）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/XBI_evening.json