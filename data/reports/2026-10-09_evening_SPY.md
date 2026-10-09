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
🟡 **近现价集中开仓**: 10-12 780C ΔOI +5,720（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 790C ΔOI -51,342 占该期限总 OI 29.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 776.24 → 收盘 778.57（+0.3%） ｜ 今日高 779.42 ｜ 低 775.14 ｜ 昨收 773.93 → 收盘 778.57（+0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.92 | OI比 1.32 | ATM IV 10.7% | Skew 1.1pp | Term 1.12 | ExpMove ±0.4%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构正常（Term 1.12）｜保护溢价薄（Skew 1.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 77% ｜ P/C OI(近端) 12%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 77%）｜近端持仓结构中性（P/C OI 分位 12%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-12（3D）±0.4% ｜ 10-13（4D）±0.6% ｜ 10-14（5D）±0.8% ｜ 10-15（6D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,049,822,894 | GEX Change vs 上次快照 477,931,353 | Flip: Primary Flip: 773.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 2620 / LOW 364 / INVALID 1760
结构观察区: Primary Flip 773.24（全链重定价，覆盖 88%）
Call Wall 785（现价低于该位 0.8%）
最近结构参考: Flip 773（现价高于该位 0.7%）
量化视角： 正 Gamma（10.50亿，历史分位偏正区，比 77% 的交易日更正）｜正 Gamma 增强（+4.78亿）｜现价位于 Flip 上方 0.69%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 772（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-12  C +33.4k / P +38.9k ｜ Activity HIGH ｜ 3D
10-13  C +18.6k / P +20.6k ｜ Activity HIGH ｜ 4D
10-14  C -13.4k / P +11.9k ｜ Activity HIGH ｜ 5D
10-15  C +7.4k / P +20.2k ｜ Activity HIGH ｜ 6D

📆 10-12 Forward Structure
存量OI: C 98.5k / P 148.3k，今日变化ΔOI: C +33.4k / P +38.9k，平值价格ATM: C $1.36 / P $1.75 ｜ ATM IV 5.5%，净 delta 敞口 1.4M shares
Top ΔOI: P 728 +7,980 ｜ P 729 +6,288 ｜ C 780 +5,720
仓位参考: Max Pain 774 ｜ Call Wall 780（+0.2%，弱）（OI 9.0k） ｜ Put Wall 770（-1.1%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜ATM IV 5.5%｜历史 Rank 30%（近端代理）｜IV/RV 0.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,432,850 股

📆 10-13 Forward Structure
存量OI: C 64.3k / P 95.1k，今日变化ΔOI: C +18.6k / P +20.6k，平值价格ATM: C $2.05 / P $2.37 ｜ ATM IV 6.7%，净 delta 敞口 462k shares
Top ΔOI: P 730 +4,851 ｜ P 731 +4,205 ｜ C 775 +2,388
仓位参考: Max Pain 775 ｜ Call Wall 790（+1.5%，弱）（OI 4.8k） ｜ Put Wall 774（-0.6%，弱）（OI 4.4k）
量化解读： 存量 Put 重｜ATM IV 6.7%｜历史 Rank 30%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 462,191 股

📆 10-14 Forward Structure
存量OI: C 93.2k / P 82.2k，今日变化ΔOI: C -13.4k / P +11.9k，平值价格ATM: C $2.94 / P $3.18 ｜ ATM IV 8.4%，净 delta 敞口 31k shares
Top ΔOI: C 790 -51,342 ｜ C 803 +9,033 ｜ C 805 +7,119
仓位参考: Max Pain 775 ｜ Call Wall 790（+1.5%）（OI 28.5k） ｜ Put Wall 770（-1.1%，弱）（OI 3.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 8.4%｜历史 Rank 30%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 31,012 股

📆 10-15 Forward Structure
存量OI: C 24.6k / P 58.5k，今日变化ΔOI: C +7.4k / P +20.2k，平值价格ATM: C $3.51 / P $3.66 ｜ ATM IV 9.0%，净 delta 敞口 217k shares
Top ΔOI: P 690 +10,167 ｜ P 772 -2,457
仓位参考: Max Pain 775 ｜ Call Wall 781（+0.3%，弱）（OI 1.6k） ｜ Put Wall 772（-0.8%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 9.0%｜历史 Rank 30%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 216,964 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SPY_evening.json