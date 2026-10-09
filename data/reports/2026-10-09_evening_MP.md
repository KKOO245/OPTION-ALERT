# 期权晚报 2026-10-09（快照 16:40 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 14.84 ↓3.7%（5D -3.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 45P ΔOI +562（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 46.74 → 收盘 46.14（-1.3%） ｜ 今日高 46.74 ｜ 低 45.42 ｜ 昨收 46.14 → 收盘 46.14（+0.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-14，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 0.72 | ATM IV 76.5% | Skew 4.4pp | Term 0.76 | ExpMove ±5.6%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 4.4pp）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±5.6% ｜ 10-23（14D）±8.0% ｜ 10-30（21D）±9.6% ｜ 11-06（28D）±12.5%
   ⇒ IV–VIX Spread: +61.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,946,895 | GEX Change vs 上次快照 2,125,249 | Flip: Primary Flip: 47.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 81%（带内） ｜ IV 有效性: VALID 256 / LOW 55 / INVALID 141
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.55（全链重定价，覆盖 81%）
Put Wall 45（现价高于该位 2.5%） | Call Wall 50（弱结构｜现价低于该位 7.7%）
最近结构参考: Put Wall 45（现价高于该位 2.5%）
量化视角： 负 Gamma（195万，无历史分位）｜负 Gamma 缓解（+213万）｜现价位于 Flip 下方 2.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall）；上方 47（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 81%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +33 / P +0.9k ｜ Activity HIGH ｜ 7D
10-23  C +0.2k / P +89 ｜ Activity MEDIUM △ ｜ 14D
10-30  C +82 / P +0.1k ｜ Activity MEDIUM △ ｜ 21D
11-06  C +0.1k / P +48 ｜ Activity MEDIUM △ ｜ 28D

📆 10-16 Forward Structure
存量OI: C 20.9k / P 18.1k，今日变化ΔOI: C +33 / P +0.9k，平值价格ATM: C $1.41 / P $1.19 ｜ ATM IV 50.6%，净 delta 敞口 -12k shares
Top ΔOI: P 45 +562 ｜ C 49 -78
仓位参考: Max Pain 50 ｜ Call Wall 50（+8.4%）（OI 4.5k） ｜ Put Wall 45（-2.5%，弱）（OI 4.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.6%｜历史 Rank 66%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 12,460 股

10-23（MEDIUM △）Top ΔOI: 50C +91 ｜ 45P +43
10-23（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+8.4%，弱）（OI 0.3k） ｜ Put Wall 45（-2.5%，弱）（OI 0.3k）

10-30（MEDIUM △）Top ΔOI: 50C +42
10-30（MEDIUM △）仓位参考: Max Pain 49 ｜ Call Wall 50（+8.4%，弱）（OI 0.4k） ｜ Put Wall 44（-4.6%）（OI 1.6k）

11-06（MEDIUM △）仓位参考: Max Pain 47 ｜ Call Wall 47（+1.9%，弱）（OI 0.1k） ｜ Put Wall 45（-2.5%，弱）（OI 69）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/MP_evening.json