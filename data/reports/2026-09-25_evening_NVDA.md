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
🟡 **近现价集中开仓**: 09-28 230C ΔOI +4,352（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 225.15 → 收盘 225.07（-0.0%） ｜ 今日高 226.94 ｜ 低 223.13 ｜ 昨收 224.58 → 收盘 225.07（+0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.37 | OI比 0.64 | ATM IV 21.0% | Skew -49.0pp | Term 1.43 | ExpMove ±1.5%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常偏陡（Term 1.43）｜Put 保护异常便宜（Skew -49.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-28（3D）±1.5% ｜ 09-30（5D）±2.5% ｜ 10-02（7D）±3.1% ｜ 10-05（10D）±3.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 668,504,067 | GEX Change vs 上次快照 -63,475,485 | Flip: Primary Flip: 213.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 633 / LOW 206 / INVALID 513
结构观察区: Primary Flip 213.51（全链重定价，覆盖 84%）
Call Wall 230（弱结构｜现价低于该位 2.1%）
最近结构参考: Call Wall 230（现价低于该位 2.1%）
量化视角： 正 Gamma（6.69亿，无历史分位）｜正 Gamma 减弱（6348万）｜现价位于 Flip 上方 5.42%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 214（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-28  C +15.2k / P +13.7k ｜ Activity HIGH ｜ 3D
09-30  C +7.1k / P +5.0k ｜ Activity HIGH ｜ 5D
10-02  C +11.2k / P +18.7k ｜ Activity HIGH ｜ 7D
10-05  C +4.6k / P +1.4k ｜ Activity HIGH ｜ 10D

📆 09-28 Forward Structure
存量OI: C 68.0k / P 52.5k，今日变化ΔOI: C +15.2k / P +13.7k，平值价格ATM: C $1.72 / P $1.60 ｜ ATM IV 20.3%，净 delta 敞口 248k shares
Top ΔOI: C 230 +4,352 ｜ C 237 +3,750 ｜ C 225 +3,717
仓位参考: Max Pain 222 ｜ Call Wall 230（+2.2%，弱）（OI 12.7k） ｜ Put Wall 220（-2.3%，弱）（OI 6.0k）
量化解读： 存量 Call 重｜ATM IV 20.3%｜历史 Rank 50%（近端代理）｜IV/RV 0.75×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 247,920 股

📆 09-30 Forward Structure
存量OI: C 37.3k / P 25.2k，今日变化ΔOI: C +7.1k / P +5.0k，平值价格ATM: C $2.91 / P $2.78 ｜ ATM IV 26.6%，净 delta 敞口 156k shares
Top ΔOI: P 212 +1,905 ｜ C 225 +1,852 ｜ C 230 +1,180
仓位参考: Max Pain 222 ｜ Call Wall 230（+2.2%）（OI 9.6k） ｜ Put Wall 212.5（-5.6%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 26.6%｜历史 Rank 50%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 156,117 股

📆 10-02 Forward Structure
存量OI: C 219.7k / P 249.0k，今日变化ΔOI: C +11.2k / P +18.7k，平值价格ATM: C $3.70 / P $3.40 ｜ ATM IV 28.4%，净 delta 敞口 -120k shares
Top ΔOI: P 215 +4,420 ｜ P 225 +3,267
仓位参考: Max Pain 220 ｜ Call Wall 235（+4.4%，弱）（OI 26.9k） ｜ Put Wall 220（-2.3%，弱）（OI 13.6k）
量化解读： 存量两侧均衡｜ATM IV 28.4%｜历史 Rank 50%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 120,321 股

📆 10-05 Forward Structure
存量OI: C 15.1k / P 5.8k，今日变化ΔOI: C +4.6k / P +1.4k，平值价格ATM: C $4.28 / P $3.70 ｜ ATM IV 26.3%，净 delta 敞口 153k shares
Top ΔOI: C 225 +970 ｜ C 230 +790 ｜ C 235 +687
仓位参考: Max Pain 222 ｜ Call Wall 230（+2.2%）（OI 3.9k） ｜ Put Wall 222.5（-1.1%）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 26.3%｜历史 Rank 50%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 正 152,627 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/NVDA_evening.json