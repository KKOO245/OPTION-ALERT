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
🟡 **近现价集中开仓**: 10-02 400C ΔOI +11（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 397.64 → 收盘 405.18（+1.9%） ｜ 今日高 406.39 ｜ 低 391.95 ｜ 昨收 399.52 → 收盘 405.18（+1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-02，窗口结束前不做对错判定）

Options: P/C成交量 0.60 | OI比 0.68 | ATM IV 173.9% | Skew 138.6pp | Term 0.25 | ExpMove ±3.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.25，近月 IV 高于远月）｜保护溢价显著（Skew 138.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±3.2% ｜ 10-09（14D）±5.8% ｜ 10-16（21D）±6.4% ｜ 10-23（28D）±9.8%
   ⇒ IV–VIX Spread: +159.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,855,405 | GEX Change vs 上次快照 1,735,973 | Flip: Primary Flip: 380.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 286 / LOW 144 / INVALID 466
结构观察区: Primary Flip 380.72（全链重定价，覆盖 87%）
Call Wall 400（弱结构｜现价高于该位 1.3%）
最近结构参考: Call Wall 400（现价高于该位 1.3%）
量化视角： 正 Gamma（286万，无历史分位）｜正 Gamma 增强（+174万）｜现价位于 Flip 上方 6.42%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 381（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +31 / P +55 ｜ Activity MEDIUM △ ｜ 7D
10-09  C +16 / P +4 ｜ Activity MEDIUM △ ｜ 14D
10-16  C +33 / P -14 ｜ Activity LOW ｜ 21D
10-23  C +19 / P +0.1k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 1.2k / P 3.1k，今日变化ΔOI: C +31 / P +55，平值价格ATM: C $7.25 / P $5.75 ｜ ATM IV 30.6%，净 delta 敞口 -79 shares
Top ΔOI: P 400 +37 ｜ C 395 +14 ｜ C 400 +11
仓位参考: Max Pain 378 ｜ Call Wall 410（+1.2%）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 30.6%｜历史 Rank 100%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 79 股

10-09（MEDIUM △）Top ΔOI: 430C +4 ｜ 440C +4
10-09（MEDIUM △）仓位参考: Max Pain 370 ｜ Call Wall 420（+3.7%，弱）（OI 0.1k） ｜ Put Wall 385（-5.0%，弱）（OI 16）

10-16（Activity LOW）仓位参考: Max Pain 380 ｜ Call Wall 400（-1.3%，弱）（OI 1.0k） ｜ Put Wall 380（-6.2%，弱）（OI 0.6k）

📆 10-23 Forward Structure
存量OI: C 0.8k / P 0.6k，今日变化ΔOI: C +19 / P +0.1k，平值价格ATM: C $19.60 / P $20.20 ｜ ATM IV 42.9%，净 delta 敞口 -96 shares
Top ΔOI: P 400 +16
仓位参考: Max Pain 395 ｜ Call Wall 415（+2.4%，弱）（OI 62） ｜ Put Wall 420（+3.7%，弱）（OI 92）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.9%｜历史 Rank 100%（近端代理）｜净 delta 敞口 负 96 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/ISRG_evening.json