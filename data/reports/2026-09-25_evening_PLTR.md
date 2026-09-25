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
🟡 **近现价集中开仓**: 10-02 197C ΔOI +4,417（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 192.86 → 收盘 189.67（-1.7%） ｜ 今日高 194.21 ｜ 低 189.35 ｜ 昨收 192.59 → 收盘 189.67（-1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.45 | OI比 0.82 | ATM IV 29.5% | Skew 17.0pp | Term 1.54 | ExpMove ±4.9%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.54）｜保护溢价显著（Skew 17.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（7D）±4.9% ｜ 10-09（14D）±7.0% ｜ 10-16（21D）±8.7% ｜ 10-23（28D）±10.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 64,434,995 | GEX Change vs 上次快照 -23,788,693 | Flip: Primary Flip: 169.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 510 / LOW 105 / INVALID 245
结构观察区: Primary Flip 169.45（全链重定价，覆盖 83%）
Call Wall 200（弱结构｜现价低于该位 5.2%）
最近结构参考: Call Wall 200（现价低于该位 5.2%）
量化视角： 正 Gamma（6443万，无历史分位）｜正 Gamma 减弱（2379万）｜现价位于 Flip 上方 11.94%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 169（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +24.3k / P +10.5k ｜ Activity HIGH ｜ 7D
10-09  C +1.6k / P +4.1k ｜ Activity HIGH ｜ 14D
10-16  C +2.6k / P +2.8k ｜ Activity HIGH ｜ 21D
10-23  C +1.2k / P +0.8k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 73.3k / P 59.2k，今日变化ΔOI: C +24.3k / P +10.5k，平值价格ATM: C $4.55 / P $4.75 ｜ ATM IV 44.5%，净 delta 敞口 207k shares
Top ΔOI: C 200 +6,043 ｜ C 207 +5,111 ｜ C 197 +4,417
仓位参考: Max Pain 182 ｜ Call Wall 200（+5.4%）（OI 14.9k） ｜ Put Wall 177.5（-6.4%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 44.5%｜历史 Rank 3%（近端代理）｜净 delta 敞口 正 207,357 股

📆 10-09 Forward Structure
存量OI: C 22.3k / P 31.9k，今日变化ΔOI: C +1.6k / P +4.1k，平值价格ATM: C $6.60 / P $6.70 ｜ ATM IV 45.0%，净 delta 敞口 -3k shares
仓位参考: Max Pain 178 ｜ Call Wall 200（+5.4%，弱）（OI 3.2k） ｜ Put Wall 190（+0.2%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 45.0%｜历史 Rank 3%（近端代理）｜净 delta 敞口 负 3,387 股

📆 10-16 Forward Structure
存量OI: C 149.5k / P 162.3k，今日变化ΔOI: C +2.6k / P +2.8k，平值价格ATM: C $8.25 / P $8.15 ｜ ATM IV 45.1%，净 delta 敞口 -15k shares
Top ΔOI: P 157 +1,340 ｜ C 205 +1,006 ｜ P 182 +826
仓位参考: Max Pain 165 ｜ Call Wall 200（+5.4%，弱）（OI 13.3k） ｜ Put Wall 175（-7.7%，弱）（OI 7.4k）
量化解读： 存量两侧均衡｜ATM IV 45.1%｜历史 Rank 3%（近端代理）｜净 delta 敞口 负 14,662 股

📆 10-23 Forward Structure
存量OI: C 17.6k / P 9.9k，今日变化ΔOI: C +1.2k / P +0.8k，平值价格ATM: C $9.65 / P $9.50 ｜ ATM IV 45.5%，净 delta 敞口 8k shares
仓位参考: Max Pain 175 ｜ Call Wall 180（-5.1%）（OI 4.6k） ｜ Put Wall 175（-7.7%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 45.5%｜历史 Rank 3%（近端代理）｜净 delta 敞口 正 8,286 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/PLTR_evening.json