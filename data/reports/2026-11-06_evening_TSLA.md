# 期权晚报 2026-11-06（快照 16:40 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 25.64 ↓9.0%（5D +32.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-09 350C ΔOI +1,582（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 348.92 → 收盘 358.22（+2.7%） ｜ 今日高 363.84 ｜ 低 347.60 ｜ 昨收 343.69 → 收盘 358.22（+4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.84 | OI比 1.20 | ATM IV 29.3% | Skew 0.8pp | Term 1.76 | ExpMove ±3.6%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.76）｜保护溢价薄（Skew 0.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-09（3D）±3.6% ｜ 11-11（5D）±5.3% ｜ 11-13（7D）±6.5% ｜ 11-16（10D）±7.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,096,737 | GEX Change vs 上次快照 4,010,567 | Flip: Primary Flip: 348.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 1248 / LOW 200 / INVALID 1102
结构观察区: Primary Flip 348.67（全链重定价，覆盖 85%）
最近结构参考: Flip 349（现价高于该位 2.7%）
量化视角： 正 Gamma（2310万，无历史分位）｜正 Gamma 增强（+401万）｜现价位于 Flip 上方 2.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 349（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +18.3k / P +11.7k ｜ Activity HIGH ｜ 3D
11-11  C +12.0k / P +8.0k ｜ Activity HIGH ｜ 5D
11-13  C +32.1k / P +16.4k ｜ Activity HIGH ｜ 7D
11-16  C +5.2k / P +2.8k ｜ Activity HIGH ｜ 10D

📆 11-09 Forward Structure
存量OI: C 46.5k / P 35.2k，今日变化ΔOI: C +18.3k / P +11.7k，平值价格ATM: C $6.80 / P $6.04 ｜ ATM IV 48.9%，净 delta 敞口 770k shares
Top ΔOI: C 380 +2,772 ｜ C 350 +1,582
仓位参考: Max Pain 368 ｜ Call Wall 380（+6.1%，弱）（OI 3.0k） ｜ Put Wall 380（+6.1%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 48.9%｜历史 Rank 3%（近端代理）｜IV/RV 0.91×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 770,096 股

📆 11-11 Forward Structure
存量OI: C 26.6k / P 18.7k，今日变化ΔOI: C +12.0k / P +8.0k，平值价格ATM: C $9.80 / P $9.20 ｜ ATM IV 57.6%，净 delta 敞口 256k shares
Top ΔOI: C 400 +1,287 ｜ C 372 +1,140 ｜ P 300 +911
仓位参考: Max Pain 370 ｜ Call Wall 390（+8.9%，弱）（OI 1.7k） ｜ Put Wall 355（-0.9%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 57.6%｜历史 Rank 3%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 255,973 股

📆 11-13 Forward Structure
存量OI: C 88.7k / P 59.7k，今日变化ΔOI: C +32.1k / P +16.4k，平值价格ATM: C $12.17 / P $11.24 ｜ ATM IV 59.1%，净 delta 敞口 1.2M shares
Top ΔOI: C 377 +7,147 ｜ C 350 +4,887 ｜ C 362 +4,321
仓位参考: Max Pain 360 ｜ Call Wall 377.5（+5.4%，弱）（OI 7.4k） ｜ Put Wall 325（-9.3%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 59.1%｜历史 Rank 3%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,235,884 股

📆 11-16 Forward Structure
存量OI: C 9.2k / P 4.9k，今日变化ΔOI: C +5.2k / P +2.8k，平值价格ATM: C $14.10 / P $12.18 ｜ ATM IV 53.5%，净 delta 敞口 61k shares
Top ΔOI: P 300 +573 ｜ C 380 +448
仓位参考: Max Pain 370 ｜ Call Wall 380（+6.1%，弱）（OI 0.5k） ｜ Put Wall 380（+6.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 53.5%｜历史 Rank 3%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 61,038 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/TSLA_evening.json