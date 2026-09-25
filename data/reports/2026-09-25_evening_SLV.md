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
🟡 **近现价集中开仓**: 09-28 56P ΔOI +1,143（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 57.80 → 收盘 58.14（+0.6%） ｜ 今日高 58.50 ｜ 低 57.25 ｜ 昨收 57.62 → 收盘 58.14（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.68 | OI比 0.33 | ATM IV 25.4% | Skew -28.8pp | Term 1.25 | ExpMove ±1.6%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构正常偏陡（Term 1.25）｜Put 保护异常便宜（Skew -28.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-28（3D）±1.6% ｜ 09-30（5D）±2.6% ｜ 10-02（7D）±3.4% ｜ 10-05（10D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 77,627,524 | GEX Change vs 上次快照 6,928,410 | Flip: Primary Flip: 56.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 686 / LOW 208 / INVALID 368
结构观察区: Primary Flip 56.01（全链重定价，覆盖 92%）
Put Wall 60（弱结构｜现价低于该位 3.1%）
最近结构参考: Put Wall 60（现价低于该位 3.1%）
量化视角： 正 Gamma（7763万，无历史分位）｜正 Gamma 增强（+693万）｜现价位于 Flip 上方 3.80%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 58（MaxPain，仅结算参考）；上方 60（Put Wall，弱结构）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-28  C +3.4k / P +2.2k ｜ Activity HIGH ｜ 3D
09-30  C +15.8k / P -6.6k ｜ Activity HIGH ｜ 5D
10-02  C +8.2k / P +1.6k ｜ Activity HIGH ｜ 7D
10-05  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 10D

📆 09-28 Forward Structure
存量OI: C 15.6k / P 11.1k，今日变化ΔOI: C +3.4k / P +2.2k，平值价格ATM: C $0.52 / P $0.40 ｜ ATM IV 21.2%，净 delta 敞口 123k shares
Top ΔOI: P 56 +1,143 ｜ C 58 +1,054 ｜ P 55 +711
仓位参考: Max Pain 58 ｜ Call Wall 62.5（+7.5%，弱）（OI 2.3k） ｜ Put Wall 56（-3.7%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 21.2%｜历史 Rank 21%（近端代理）｜IV/RV 0.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 123,042 股

📆 09-30 Forward Structure
存量OI: C 294.4k / P 127.8k，今日变化ΔOI: C +15.8k / P -6.6k，平值价格ATM: C $0.83 / P $0.66 ｜ ATM IV 27.0%，净 delta 敞口 1.1M shares
Top ΔOI: P 70 -2,737 ｜ P 70 -2,220
仓位参考: Max Pain 57 ｜ Call Wall 60（+3.2%，弱）（OI 5.9k） ｜ Put Wall 53（-8.8%）（OI 13.4k）
量化解读： 存量 Call 重｜ATM IV 27.0%｜历史 Rank 21%（近端代理）｜IV/RV 0.72×（近似）｜净 delta 敞口 正 1,065,437 股

📆 10-02 Forward Structure
存量OI: C 75.9k / P 34.9k，今日变化ΔOI: C +8.2k / P +1.6k，平值价格ATM: C $1.07 / P $0.89 ｜ ATM IV 30.3%，净 delta 敞口 314k shares
Top ΔOI: C 59 +4,190 ｜ C 58 +2,424 ｜ P 57 +957
仓位参考: Max Pain 58 ｜ Call Wall 60（+3.2%，弱）（OI 11.9k） ｜ Put Wall 56（-3.7%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 30.3%｜历史 Rank 21%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 313,846 股

📆 10-05 Forward Structure
存量OI: C 1.5k / P 2.0k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $1.21 / P $0.98 ｜ ATM IV 28.1%，净 delta 敞口 -1k shares
Top ΔOI: P 53 +68 ｜ P 57 +65 ｜ P 56 +54
仓位参考: Max Pain 60 ｜ Call Wall 60（+3.2%，弱）（OI 0.2k） ｜ Put Wall 59.5（+2.3%）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 28.1%｜历史 Rank 21%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 负 1,231 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/SLV_evening.json