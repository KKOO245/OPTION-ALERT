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


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 658.35 → 收盘 656.10（-0.3%） ｜ 今日高 664.52 ｜ 低 653.99 ｜ 昨收 647.05 → 收盘 656.10（+1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 1.43 | OI比 1.04 | ATM IV 26.7% | Skew 7.3pp | Term 1.13 | ExpMove ±1.9%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构正常（Term 1.13）｜保护溢价显著（Skew 7.3pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.43×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 23% ｜ P/C OI(近端) 6%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 23%）｜近端持仓极端 Call 重（P/C OI 分位 6%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-09（3D）±1.9% ｜ 11-10（4D）±2.7% ｜ 11-11（5D）±3.2% ｜ 11-12（6D）±3.5%
   ⇒ IV–VIX Spread: +1.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -423,055,609 | GEX Change vs 上次快照 -35,767,773 | Flip: Primary Flip: 690.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2851 / LOW 169 / INVALID 1920
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 690.42（全链重定价，覆盖 98%）
Put Wall 650（弱结构｜现价高于该位 0.9%）
最近结构参考: Put Wall 650（现价高于该位 0.9%）
量化视角： 负 Gamma（4.23亿，历史分位偏负区，比 77% 的交易日更负）｜负 Gamma 加深（3577万）｜现价位于 Flip 下方 4.97%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 650（Put Wall，弱结构）；上方 663（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 690（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-10  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-11  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-12  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 11-09 Forward Structure
存量OI: C 98.6k / P 102.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.66 / P $6.02 ｜ ATM IV 26.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 663 ｜ Call Wall 660（+0.6%，弱）（OI 6.1k） ｜ Put Wall 640（-2.5%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜ATM IV 26.7%｜历史 Rank 83%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-10（Activity LOW）仓位参考: Max Pain 670 ｜ Call Wall 672（+2.4%，弱）（OI 3.6k） ｜ Put Wall 650（-0.9%，弱）（OI 1.5k）

11-11（Activity LOW）仓位参考: Max Pain 676 ｜ Call Wall 670（+2.1%，弱）（OI 0.9k） ｜ Put Wall 645（-1.7%，弱）（OI 1.6k）

11-12（Activity LOW）仓位参考: Max Pain 667 ｜ Call Wall 656（-0.0%，弱）（OI 1.7k） ｜ Put Wall 656（-0.0%，弱）（OI 1.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/QQQ_evening.json