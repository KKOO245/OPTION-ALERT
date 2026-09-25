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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-02 51C ΔOI +534（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 47.5）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 49.30 → 收盘 48.83（-1.0%） ｜ 今日高 49.76 ｜ 低 48.13 ｜ 昨收 49.30 → 收盘 48.83（-1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.61 | OI比 0.67 | ATM IV 69.1% | Skew 21.5pp | Term 0.76 | ExpMove ±5.8%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 21.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±5.8% ｜ 10-09（14D）±8.1% ｜ 10-16（21D）±10.0% ｜ 10-23（28D）±11.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,844,129 | GEX Change vs 上次快照 964,471 | Flip: Candidates 47.54 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 283 / LOW 62 / INVALID 139
结构观察区: ≈48（全链重定价，覆盖 79%，CONDITIONAL）
Put Wall 50（弱结构｜现价低于该位 2.3%）
最近结构参考: Put Wall 50（现价低于该位 2.3%）
量化视角： 正 Gamma（184万，无历史分位）｜正 Gamma 增强（+96万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 49（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +1.5k / P +0.5k ｜ Activity HIGH ｜ 7D
10-09  C +0.2k / P +39 ｜ Activity MEDIUM △ ｜ 14D
10-16  C +0.2k / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +68 / P +30 ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 9.5k / P 5.7k，今日变化ΔOI: C +1.5k / P +0.5k，平值价格ATM: C $1.30 / P $1.51 ｜ ATM IV 51.7%，净 delta 敞口 24k shares
Top ΔOI: C 51 +534 ｜ C 50 +332
仓位参考: Max Pain 50 ｜ Call Wall 49（+0.3%，弱）（OI 1.2k） ｜ Put Wall 50（+2.4%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 51.7%｜历史 Rank 53%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 正 24,405 股

10-09（MEDIUM △）Top ΔOI: 50C -16
10-09（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 47（-3.7%）（OI 1.1k）

10-16（MEDIUM △）Top ΔOI: 48P +504 ｜ 45C +196
10-16（MEDIUM △）仓位参考: Max Pain 52 ｜ Call Wall 50（+2.4%，弱）（OI 3.0k） ｜ Put Wall 50（+2.4%，弱）（OI 3.3k）

10-23（MEDIUM △）Top ΔOI: 51P -17 ｜ 46P +16
10-23（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 50（+2.4%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/MP_evening.json