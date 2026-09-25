# 期权晚报 2026-09-25（快照 16:40 ET）

📊 市场环境

SPY $771.35 ｜ QQQ $744.50
VIX 14.87 ↓5.1%（5D +0.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 550P ΔOI +99（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 569.95 → 收盘 572.68（+0.5%） ｜ 今日高 575.69 ｜ 低 567.35 ｜ 昨收 566.07 → 收盘 572.68（+1.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-02，窗口结束前不做对错判定）

Options: P/C成交量 1.68 | OI比 1.61 | ATM IV 62.2% | Skew -43.3pp | Term 0.61 | ExpMove ±3.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -43.3pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.68×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.61×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±3.8% ｜ 10-09（14D）±5.8% ｜ 10-16（21D）±7.0% ｜ 10-23（28D）±0.0%
   ⇒ IV–VIX Spread: +47.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,985,996 | GEX Change vs 上次快照 -1,811,015 | Flip: Primary Flip: 553.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 522 / LOW 264 / INVALID 798
结构观察区: Primary Flip 553.34（全链重定价，覆盖 92%）
Call Wall 600（现价低于该位 4.6%）
最近结构参考: Flip 553（现价高于该位 3.5%）
量化视角： 正 Gamma（899万，无历史分位）｜正 Gamma 减弱（181万）｜现价位于 Flip 上方 3.50%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 545（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 553（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0.3k / P -0.8k ｜ Activity HIGH ｜ 7D
10-09  C +91 / P +0.1k ｜ Activity HIGH ｜ 14D
10-16  C -1.9k / P +0.4k ｜ Activity HIGH ｜ 21D
10-23  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 15.0k / P 13.8k，今日变化ΔOI: C +0.3k / P -0.8k，平值价格ATM: C $11.92 / P $10.00 ｜ ATM IV 35.1%，净 delta 敞口 23k shares
Top ΔOI: P 540 -598 ｜ P 560 -424 ｜ P 550 +99
仓位参考: Max Pain 542 ｜ Call Wall 542.5（-5.3%，弱）（OI 2.8k） ｜ Put Wall 550（-4.0%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 35.1%｜历史 Rank 94%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 23,051 股

📆 10-09 Forward Structure
存量OI: C 4.1k / P 2.4k，今日变化ΔOI: C +91 / P +0.1k，平值价格ATM: C $16.05 / P $17.08 ｜ ATM IV 35.0%，净 delta 敞口 2k shares
Top ΔOI: C 560 +57 ｜ P 520 +35
仓位参考: Max Pain 525 ｜ Call Wall 537.5（-6.1%，弱）（OI 0.4k） ｜ Put Wall 547.5（-4.4%，弱）（OI 87）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.0%｜历史 Rank 94%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,243 股

📆 10-16 Forward Structure
存量OI: C 39.6k / P 84.8k，今日变化ΔOI: C -1.9k / P +0.4k，平值价格ATM: C $20.90 / P $19.10 ｜ ATM IV 36.2%，净 delta 敞口 -80k shares
Top ΔOI: C 600 -1,429 ｜ P 535 +514
仓位参考: Max Pain 530 ｜ Call Wall 600（+4.8%）（OI 9.9k）
量化解读： 存量 Put 重｜ATM IV 36.2%｜历史 Rank 94%（近端代理）｜IV/RV 0.96×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 80,469 股

📆 10-23 Forward Structure
存量OI: C 0.9k / P 4.8k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 38.2%，净 delta 敞口 6k shares
Top ΔOI: C 410 +60 ｜ P 520 +31
仓位参考: Max Pain 525 ｜ Call Wall 570（-0.5%，弱）（OI 65）
量化解读： 存量 Put 重｜ATM IV 38.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 6,276 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/SOXX_evening.json