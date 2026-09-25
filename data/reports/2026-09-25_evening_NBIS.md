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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 246.90 → 收盘 237.33（-3.9%） ｜ 今日高 246.90 ｜ 低 235.41 ｜ 昨收 243.48 → 收盘 237.33（-2.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.45 | OI比 0.91 | ATM IV 94.2% | Skew 12.3pp | Term 0.78 | ExpMove ±8.0%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 12.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（7D）±8.0% ｜ 10-09（14D）±11.4% ｜ 10-16（21D）±14.2% ｜ 10-23（28D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,164,305 | GEX Change vs 上次快照 -3,329,004 | Flip: Primary Flip: 214.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 489 / LOW 53 / INVALID 212
结构观察区: Primary Flip 214.93（全链重定价，覆盖 80%）
最近结构参考: Flip 215（现价高于该位 10.4%）
量化视角： 正 Gamma（1416万，无历史分位）｜正 Gamma 减弱（333万）｜现价位于 Flip 上方 10.42%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +6.0k / P +3.5k ｜ Activity HIGH ｜ 7D
10-09  C +2.4k / P +0.1k ｜ Activity HIGH ｜ 14D
10-16  C +7.0k / P +0.9k ｜ Activity HIGH ｜ 21D
10-23  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 40.1k / P 26.5k，今日变化ΔOI: C +6.0k / P +3.5k，平值价格ATM: C $9.50 / P $9.46 ｜ ATM IV 72.5%，净 delta 敞口 -116k shares
Top ΔOI: C 270 +762 ｜ C 210 -638
仓位参考: Max Pain 225 ｜ Call Wall 235（-1.0%，弱）（OI 5.0k） ｜ Put Wall 220（-7.3%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 72.5%｜历史 Rank 32%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 负 115,740 股

📆 10-09 Forward Structure
存量OI: C 15.3k / P 11.8k，今日变化ΔOI: C +2.4k / P +0.1k，平值价格ATM: C $13.70 / P $13.45 ｜ ATM IV 72.6%，净 delta 敞口 70k shares
Top ΔOI: C 212 +830
仓位参考: Max Pain 220 ｜ Call Wall 240（+1.1%，弱）（OI 2.0k） ｜ Put Wall 225（-5.2%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 72.6%｜历史 Rank 32%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 70,194 股

📆 10-16 Forward Structure
存量OI: C 62.7k / P 79.5k，今日变化ΔOI: C +7.0k / P +0.9k，平值价格ATM: C $17.00 / P $16.64 ｜ ATM IV 70.5%，净 delta 敞口 37k shares
Top ΔOI: C 300 +3,791 ｜ C 270 +855 ｜ C 275 +802
仓位参考: Max Pain 220 ｜ Call Wall 240（+1.1%，弱）（OI 4.3k） ｜ Put Wall 220（-7.3%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.5%｜历史 Rank 32%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 37,046 股

📆 10-23 Forward Structure
存量OI: C 4.7k / P 8.2k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $21.12 / P $18.25 ｜ ATM IV 73.8%，净 delta 敞口 -3k shares
Top ΔOI: P 235 +141
仓位参考: Max Pain 230 ｜ Call Wall 225（-5.2%，弱）（OI 0.4k） ｜ Put Wall 235（-1.0%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.8%｜历史 Rank 32%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 3,332 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/NBIS_evening.json