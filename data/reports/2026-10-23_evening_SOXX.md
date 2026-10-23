# 期权晚报 2026-10-23（快照 16:40 ET）

📊 市场环境

SPY $759.97 ｜ QQQ $704.40
VIX 19.45 ↑2.2%（5D -2.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 500C ΔOI +2,667（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 474.55 → 收盘 478.20（+0.8%） ｜ 今日高 485.04 ｜ 低 473.10 ｜ 昨收 475.69 → 收盘 478.20（+0.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 2.97 | OI比 1.51 | ATM IV 119.2% | Skew 83.0pp | Term 0.37 | ExpMove ±5.7%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.37，近月 IV 高于远月）｜保护溢价显著（Skew 83.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.97）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.97×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.51×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±5.7% ｜ 11-06（14D）±4.4% ｜ 11-13（21D）±9.2% ｜ 11-20（28D）±10.1%
   ⇒ IV–VIX Spread: +99.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -36,283,200 | GEX Change vs 上次快照 3,555,324 | Flip: Primary Flip: 535.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 563 / LOW 264 / INVALID 757
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 535.27（全链重定价，覆盖 92%）
最近结构参考: Flip 535（现价低于该位 10.7%）
量化视角： 负 Gamma（3628万，无历史分位）｜负 Gamma 缓解（+356万）｜现价位于 Flip 下方 10.66%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 535（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +8.0k / P +1.6k ｜ Activity HIGH ｜ 7D
11-06  C -0.4k / P +0.7k ｜ Activity HIGH ｜ 14D
11-13  C +0.2k / P +0.5k ｜ Activity HIGH ｜ 21D
11-20  C +0.9k / P +3.7k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 29.0k / P 147.3k，今日变化ΔOI: C +8.0k / P +1.6k，平值价格ATM: C $14.67 / P $12.70 ｜ ATM IV 47.5%，净 delta 敞口 194k shares
Top ΔOI: C 525 +3,869 ｜ C 500 +2,667 ｜ P 470 +1,352
仓位参考: Max Pain 520 ｜ Call Wall 500（+4.6%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 193,560 股

📆 11-06 Forward Structure
存量OI: C 5.7k / P 6.8k，今日变化ΔOI: C -0.4k / P +0.7k，平值价格ATM: C $20.99 / P $0.00 ｜ ATM IV 48.1%，净 delta 敞口 13k shares
Top ΔOI: P 465 +408 ｜ P 440 +406
仓位参考: Max Pain 520 ｜ Put Wall 455（-4.9%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 48.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,702 股

📆 11-13 Forward Structure
存量OI: C 14.4k / P 6.0k，今日变化ΔOI: C +0.2k / P +0.5k，平值价格ATM: C $21.82 / P $21.95 ｜ ATM IV 45.6%，净 delta 敞口 -12k shares
Top ΔOI: P 485 +122
仓位参考: Max Pain 520 ｜ Put Wall 460（-3.8%）（OI 3.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,834 股

📆 11-20 Forward Structure
存量OI: C 29.2k / P 57.5k，今日变化ΔOI: C +0.9k / P +3.7k，平值价格ATM: C $23.90 / P $24.18 ｜ ATM IV 44.5%，净 delta 敞口 -60k shares
Top ΔOI: P 440 +1,281 ｜ P 430 +881 ｜ P 470 +662
仓位参考: Max Pain 560 ｜ Put Wall 460（-3.8%，弱）（OI 7.3k）
量化解读： 存量 Put 重｜ATM IV 44.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 59,859 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SOXX_evening.json