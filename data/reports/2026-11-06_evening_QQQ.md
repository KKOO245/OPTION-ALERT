# 期权晚报 2026-11-06（快照 16:40 ET）

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
🟡 **近现价集中开仓**: 11-09 660C ΔOI +6,094（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 658.35 → 收盘 656.10（-0.3%） ｜ 今日高 664.52 ｜ 低 654.00 ｜ 昨收 647.05 → 收盘 656.10（+1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 1.24 | OI比 0.89 | ATM IV 32.4% | Skew 1.3pp | Term 0.93 | ExpMove ±1.9%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构正常（Term 0.93）｜保护溢价薄（Skew 1.3pp）｜当日成交偏 Put（P/C量 1.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 23% ｜ P/C OI(近端) 3%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 23%）｜近端持仓极端 Call 重（P/C OI 分位 3%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-09（3D）±1.9% ｜ 11-10（4D）±2.7% ｜ 11-11（5D）±3.2% ｜ 11-12（6D）±3.5%
   ⇒ IV–VIX Spread: +6.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -429,133,382 | GEX Change vs 上次快照 -41,845,545 | Flip: Primary Flip: 688.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 2806 / LOW 288 / INVALID 2298
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 688.72（全链重定价，覆盖 85%）
Put Wall 650（弱结构｜现价高于该位 0.9%）
最近结构参考: Put Wall 650（现价高于该位 0.9%）
量化视角： 负 Gamma（4.29亿，历史分位偏负区，比 77% 的交易日更负）｜负 Gamma 加深（4185万）｜现价位于 Flip 下方 4.74%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 650（Put Wall，弱结构）；上方 680（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 689（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +57.3k / P +14.8k ｜ Activity HIGH ｜ 3D
11-10  C +18.9k / P +7.8k ｜ Activity HIGH ｜ 4D
11-11  C +11.5k / P +12.4k ｜ Activity HIGH ｜ 5D
11-12  C +18.4k / P +12.9k ｜ Activity HIGH ｜ 6D

📆 11-09 Forward Structure
存量OI: C 98.6k / P 102.2k，今日变化ΔOI: C +57.3k / P +14.8k，平值价格ATM: C $6.66 / P $6.02 ｜ ATM IV 26.7%，净 delta 敞口 1.6M shares
Top ΔOI: C 660 +6,094 ｜ C 680 +5,293 ｜ C 670 +4,105
仓位参考: Max Pain 663 ｜ Call Wall 660（+0.6%，弱）（OI 6.1k） ｜ Put Wall 640（-2.5%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 26.7%｜历史 Rank 91%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,600,309 股

📆 11-10 Forward Structure
存量OI: C 59.1k / P 28.1k，今日变化ΔOI: C +18.9k / P +7.8k，平值价格ATM: C $9.22 / P $8.44 ｜ ATM IV 32.1%，净 delta 敞口 355k shares
Top ΔOI: C 672 +3,599 ｜ C 660 +2,026 ｜ C 670 +1,434
仓位参考: Max Pain 670 ｜ Call Wall 672（+2.4%，弱）（OI 3.6k） ｜ Put Wall 650（-0.9%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 32.1%｜历史 Rank 91%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 355,247 股

📆 11-11 Forward Structure
存量OI: C 33.5k / P 29.9k，今日变化ΔOI: C +11.5k / P +12.4k，平值价格ATM: C $10.77 / P $10.03 ｜ ATM IV 33.7%，净 delta 敞口 95k shares
Top ΔOI: C 690 +1,454 ｜ P 605 +1,338 ｜ P 635 +1,177
仓位参考: Max Pain 676 ｜ Call Wall 670（+2.1%，弱）（OI 0.9k） ｜ Put Wall 645（-1.7%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.7%｜历史 Rank 91%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 95,446 股

📆 11-12 Forward Structure
存量OI: C 37.7k / P 26.1k，今日变化ΔOI: C +18.4k / P +12.9k，平值价格ATM: C $11.85 / P $11.15 ｜ ATM IV 34.4%，净 delta 敞口 137k shares
Top ΔOI: C 685 +2,543 ｜ C 695 +2,434 ｜ C 656 +1,709
仓位参考: Max Pain 667 ｜ Call Wall 656（-0.0%，弱）（OI 1.7k） ｜ Put Wall 656（-0.0%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 34.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 136,723 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/QQQ_evening.json