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
🟡 **近现价集中开仓**: 10-16 157C ΔOI +7,561（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 154.37 → 收盘 154.34（-0.0%） ｜ 今日高 158.11 ｜ 低 150.50 ｜ 昨收 151.47 → 收盘 154.34（+1.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.94 | ATM IV 46.1% | Skew 0.4pp | Term 1.37 | ExpMove ±6.4%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常偏陡（Term 1.37）｜保护溢价薄（Skew 0.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（7D）±6.4% ｜ 10-23（14D）±9.0% ｜ 10-30（21D）±11.8% ｜ 11-06（28D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,023,367 | GEX Change vs 上次快照 7,973,213 | Flip: Primary Flip: 142.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 81%（带内） ｜ IV 有效性: VALID 564 / LOW 94 / INVALID 284
结构观察区: Primary Flip 142.46（全链重定价，覆盖 81%）
Call Wall 160（弱结构｜现价低于该位 3.5%）
最近结构参考: Call Wall 160（现价低于该位 3.5%）
量化视角： 正 Gamma（3102万，无历史分位）｜正 Gamma 增强（+797万）｜现价位于 Flip 上方 8.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 142（全链重定价，覆盖 81%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +19.5k / P +13.6k ｜ Activity HIGH ｜ 7D
10-23  C +4.4k / P +5.6k ｜ Activity HIGH ｜ 14D
10-30  C +2.5k / P +3.9k ｜ Activity HIGH ｜ 21D
11-06  C +0.4k / P +2.2k ｜ Activity HIGH ｜ 28D

📆 10-16 Forward Structure
存量OI: C 221.6k / P 201.8k，今日变化ΔOI: C +19.5k / P +13.6k，平值价格ATM: C $4.64 / P $5.27 ｜ ATM IV 57.7%，净 delta 敞口 25k shares
Top ΔOI: C 95 -12,394 ｜ C 157 +7,561 ｜ C 165 +6,201
仓位参考: Max Pain 140 ｜ Call Wall 155（+0.4%，弱）（OI 17.1k） ｜ Put Wall 142（-8.0%，弱）（OI 7.0k）
量化解读： 存量两侧均衡｜ATM IV 57.7%｜历史 Rank 2%（近端代理）｜IV/RV 0.78×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 24,953 股

📆 10-23 Forward Structure
存量OI: C 36.2k / P 52.9k，今日变化ΔOI: C +4.4k / P +5.6k，平值价格ATM: C $6.71 / P $7.15 ｜ ATM IV 57.8%，净 delta 敞口 162k shares
Top ΔOI: C 150 +1,250 ｜ C 149 +1,039
仓位参考: Max Pain 160 ｜ Call Wall 165（+6.9%，弱）（OI 2.4k） ｜ Put Wall 160（+3.7%）（OI 6.1k）
量化解读： 存量 Put 重｜ATM IV 57.8%｜历史 Rank 2%（近端代理）｜IV/RV 0.78×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 162,173 股

📆 10-30 Forward Structure
存量OI: C 29.3k / P 38.9k，今日变化ΔOI: C +2.5k / P +3.9k，平值价格ATM: C $8.90 / P $9.25 ｜ ATM IV 61.8%，净 delta 敞口 -23k shares
Top ΔOI: C 200 +1,252 ｜ C 195 +661 ｜ C 165 -571
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+5.3%，弱）（OI 2.6k） ｜ Put Wall 160（+3.7%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜ATM IV 61.8%｜历史 Rank 2%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 负 23,410 股

📆 11-06 Forward Structure
存量OI: C 8.5k / P 15.3k，今日变化ΔOI: C +0.4k / P +2.2k，平值价格ATM: C $11.45 / P $10.88 ｜ ATM IV 63.1%，净 delta 敞口 -63k shares
Top ΔOI: P 165 +535 ｜ P 120 +512
仓位参考: Max Pain 160 ｜ Call Wall 160（+3.7%）（OI 1.2k） ｜ Put Wall 160（+3.7%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 63.1%｜历史 Rank 2%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 负 62,597 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/MSTR_evening.json