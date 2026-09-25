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
🟡 **近现价集中开仓**: 09-30 360P ΔOI +682（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 384.90 → 收盘 372.11（-3.3%） ｜ 今日高 386.83 ｜ 低 367.67 ｜ 昨收 377.94 → 收盘 372.11（-1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 1.03 | ATM IV 25.9% | Skew 3.2pp | Term 1.69 | ExpMove ±1.9%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常偏陡（Term 1.69）｜保护溢价中性（Skew 3.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.03×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-28（3D）±1.9% ｜ 09-30（5D）±3.2% ｜ 10-02（7D）±4.6% ｜ 10-05（10D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,778,119 | GEX Change vs 上次快照 -10,488,602 | Flip: Primary Flip: 348.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 1123 / LOW 124 / INVALID 625
结构观察区: Primary Flip 348.15（全链重定价，覆盖 83%）
Call Wall 400（弱结构｜现价低于该位 7.0%）
最近结构参考: Flip 348（现价高于该位 6.9%）
量化视角： 正 Gamma（7478万，无历史分位）｜正 Gamma 减弱（1049万）｜现价位于 Flip 上方 6.88%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 348（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-28  C +10.3k / P +10.5k ｜ Activity HIGH ｜ 3D
09-30  C +5.1k / P +3.3k ｜ Activity HIGH ｜ 5D
10-02  C +11.1k / P +21.5k ｜ Activity HIGH ｜ 7D
10-05  C +2.1k / P +1.3k ｜ Activity HIGH ｜ 10D

📆 09-28 Forward Structure
存量OI: C 38.8k / P 29.4k，今日变化ΔOI: C +10.3k / P +10.5k，平值价格ATM: C $3.30 / P $3.65 ｜ ATM IV 25.9%，净 delta 敞口 -155k shares
仓位参考: Max Pain 378 ｜ Call Wall 400（+7.5%，弱）（OI 4.8k） ｜ Put Wall 365（-1.9%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 25.9%｜历史 Rank 70%（近端代理）｜IV/RV 0.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 154,579 股

📆 09-30 Forward Structure
存量OI: C 21.4k / P 15.2k，今日变化ΔOI: C +5.1k / P +3.3k，平值价格ATM: C $5.72 / P $6.05 ｜ ATM IV 33.8%，净 delta 敞口 2k shares
Top ΔOI: C 405 +1,200 ｜ C 400 +1,013 ｜ P 360 +682
仓位参考: Max Pain 375 ｜ Call Wall 400（+7.5%）（OI 3.3k） ｜ Put Wall 375（+0.8%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 33.8%｜历史 Rank 70%（近端代理）｜IV/RV 0.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,827 股

📆 10-02 Forward Structure
存量OI: C 123.8k / P 125.8k，今日变化ΔOI: C +11.1k / P +21.5k，平值价格ATM: C $8.55 / P $8.69 ｜ ATM IV 41.7%，净 delta 敞口 -138k shares
Top ΔOI: C 397 +3,129
仓位参考: Max Pain 360 ｜ Call Wall 360（-3.3%）（OI 16.7k）
量化解读： 存量两侧均衡｜ATM IV 41.7%｜历史 Rank 70%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 138,435 股

📆 10-05 Forward Structure
存量OI: C 6.6k / P 5.7k，今日变化ΔOI: C +2.1k / P +1.3k，平值价格ATM: C $9.49 / P $9.20 ｜ ATM IV 38.2%，净 delta 敞口 6k shares
Top ΔOI: C 385 +303 ｜ C 405 +240 ｜ C 390 +202
仓位参考: Max Pain 378 ｜ Call Wall 380（+2.1%，弱）（OI 0.8k） ｜ Put Wall 375（+0.8%）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 38.2%｜历史 Rank 70%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 6,467 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/TSLA_evening.json