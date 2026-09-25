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
🟡 **近现价集中开仓**: 10-02 285C ΔOI +726（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 269.91 → 收盘 288.70（+7.0%） ｜ 今日高 292.72 ｜ 低 264.01 ｜ 昨收 266.65 → 收盘 288.70（+8.3%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-09-30，窗口结束前不做对错判定）

Options: P/C成交量 0.57 | OI比 1.21 | ATM IV 96.2% | Skew -11.3pp | Term 0.79 | ExpMove ±8.3%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -11.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±8.3% ｜ 10-09（14D）±11.8% ｜ 10-16（21D）±14.2% ｜ 10-23（28D）±17.4%
   ⇒ IV–VIX Spread: +81.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,999,512 | GEX Change vs 上次快照 222,317 | Flip: Primary Flip: 254.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 554 / LOW 97 / INVALID 283
结构观察区: Primary Flip 254.81（全链重定价，覆盖 86%）
Call Wall 300（弱结构｜现价低于该位 3.8%）
最近结构参考: Call Wall 300（现价低于该位 3.8%）
量化视角： 正 Gamma（1500万，无历史分位）｜正 Gamma 增强（+22万）｜现价位于 Flip 上方 13.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 265（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 255（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +3.6k / P +6.1k ｜ Activity HIGH ｜ 7D
10-09  C +0.7k / P +1.4k ｜ Activity HIGH ｜ 14D
10-16  C -83 / P +1.4k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +1.0k / P +1.7k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 25.3k / P 27.4k，今日变化ΔOI: C +3.6k / P +6.1k，平值价格ATM: C $12.60 / P $11.35 ｜ ATM IV 74.9%，净 delta 敞口 130k shares
Top ΔOI: P 260 +1,228 ｜ C 285 +726 ｜ P 250 +569
仓位参考: Max Pain 260 ｜ Call Wall 300（+3.9%，弱）（OI 3.9k） ｜ Put Wall 260（-9.9%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜ATM IV 74.9%｜历史 Rank 58%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 130,339 股

📆 10-09 Forward Structure
存量OI: C 5.6k / P 10.5k，今日变化ΔOI: C +0.7k / P +1.4k，平值价格ATM: C $18.51 / P $15.51 ｜ ATM IV 74.4%，净 delta 敞口 27k shares
仓位参考: Max Pain 260 ｜ Call Wall 295（+2.2%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 74.4%｜历史 Rank 58%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 27,081 股

10-16（MEDIUM △）Top ΔOI: 320C -344 ｜ 350C -291
10-16（MEDIUM △）仓位参考: Max Pain 255 ｜ Call Wall 280（-3.0%，弱）（OI 8.5k） ｜ Put Wall 260（-9.9%，弱）（OI 3.7k）

📆 10-23 Forward Structure
存量OI: C 6.8k / P 12.7k，今日变化ΔOI: C +1.0k / P +1.7k，平值价格ATM: C $26.38 / P $24.00 ｜ ATM IV 75.8%，净 delta 敞口 36k shares
Top ΔOI: C 300 +451
仓位参考: Max Pain 250 ｜ Call Wall 300（+3.9%）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 75.8%｜历史 Rank 58%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 36,182 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/BE_evening.json