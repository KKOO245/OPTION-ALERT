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
🟡 **近现价集中开仓**: 10-02 139C ΔOI +224（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 137.25 → 收盘 135.62（-1.2%） ｜ 今日高 139.83 ｜ 低 135.60 ｜ 昨收 137.78 → 收盘 135.62（-1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.32 | OI比 0.62 | ATM IV 38.2% | Skew 2.9pp | Term 1.41 | ExpMove ±5.5%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.41）｜保护溢价中性（Skew 2.9pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±5.5% ｜ 10-09（14D）±8.0% ｜ 10-16（21D）±9.7% ｜ 10-23（28D）±12.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,520,344 | GEX Change vs 上次快照 -4,972,937 | Flip: Primary Flip: 128.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 533 / LOW 50 / INVALID 143
结构观察区: Primary Flip 128.47（全链重定价，覆盖 86%）
最近结构参考: Flip 128（现价高于该位 5.6%）
量化视角： 正 Gamma（852万，无历史分位）｜正 Gamma 减弱（497万）｜现价位于 Flip 上方 5.56%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 136（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 128（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +1.6k / P +1.6k ｜ Activity HIGH ｜ 7D
10-09  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 14D
10-16  C +2.4k / P +1.0k ｜ Activity HIGH ｜ 21D
10-23  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 19.3k / P 17.0k，今日变化ΔOI: C +1.6k / P +1.6k，平值价格ATM: C $3.71 / P $3.81 ｜ ATM IV 50.3%，净 delta 敞口 -15k shares
Top ΔOI: P 131 +312 ｜ C 145 +261 ｜ C 139 +224
仓位参考: Max Pain 135 ｜ Call Wall 145（+6.9%，弱）（OI 1.5k） ｜ Put Wall 130（-4.1%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.3%｜历史 Rank 0%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 14,539 股

📆 10-09 Forward Structure
存量OI: C 8.7k / P 7.2k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $5.42 / P $5.36 ｜ ATM IV 50.3%，净 delta 敞口 7k shares
仓位参考: Max Pain 136 ｜ Put Wall 140（+3.2%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 50.3%｜历史 Rank 0%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,169 股

📆 10-16 Forward Structure
存量OI: C 72.2k / P 57.7k，今日变化ΔOI: C +2.4k / P +1.0k，平值价格ATM: C $6.70 / P $6.45 ｜ ATM IV 50.2%，净 delta 敞口 2k shares
Top ΔOI: C 150 +987 ｜ P 140 +361
仓位参考: Max Pain 127 ｜ Call Wall 140（+3.2%，弱）（OI 4.5k） ｜ Put Wall 130（-4.1%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜ATM IV 50.2%｜历史 Rank 0%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,902 股

📆 10-23 Forward Structure
存量OI: C 6.8k / P 8.8k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $8.25 / P $8.05 ｜ ATM IV 53.9%，净 delta 敞口 6k shares
Top ΔOI: P 120 +285
仓位参考: Max Pain 135 ｜ Call Wall 140（+3.2%，弱）（OI 1.0k） ｜ Put Wall 125（-7.8%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.9%｜历史 Rank 0%（近端代理）｜净 delta 敞口 正 5,620 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/NOW_evening.json