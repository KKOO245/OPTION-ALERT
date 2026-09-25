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
🟡 **近现价集中开仓**: 09-28 730P ΔOI +6,726（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-01 660P ΔOI +8,750 占该期限总 OI 11.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 742.84 → 收盘 744.50（+0.2%） ｜ 今日高 745.91 ｜ 低 739.64 ｜ 昨收 741.10 → 收盘 744.50（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.90 | OI比 2.08 | ATM IV 18.5% | Skew 1.8pp | Term 0.97 | ExpMove ±0.8%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构正常（Term 0.97）｜保护溢价薄（Skew 1.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.08×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 89% ｜ P/C OI(近端) 81%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 89%）｜近端持仓结构中性（P/C OI 分位 81%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-28（3D）±0.8% ｜ 09-29（4D）±1.1% ｜ 09-30（5D）±1.5% ｜ 10-01（6D）±1.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 484,995,597 | GEX Change vs 上次快照 63,586,985 | Flip: Primary Flip: 736.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 3325 / LOW 338 / INVALID 1665
结构观察区: Primary Flip 736.63（全链重定价，覆盖 91%）
Call Wall 760（弱结构｜现价低于该位 2.0%）
最近结构参考: Flip 737（现价高于该位 1.1%）
量化视角： 正 Gamma（4.85亿，历史分位偏正区，比 89% 的交易日更正）｜正 Gamma 增强（+6359万）｜现价位于 Flip 上方 1.07%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 735（MaxPain，仅结算参考）；上方 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 737（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-28  C +29.0k / P +21.0k ｜ Activity HIGH ｜ 3D
09-29  C +10.0k / P +26.4k ｜ Activity HIGH ｜ 4D
09-30  C +6.9k / P -2.8k ｜ Activity MEDIUM △ ｜ 5D
10-01  C +9.8k / P +17.8k ｜ Activity HIGH ｜ 6D

📆 09-28 Forward Structure
存量OI: C 76.8k / P 169.4k，今日变化ΔOI: C +29.0k / P +21.0k，平值价格ATM: C $3.50 / P $2.86 ｜ ATM IV 11.6%，净 delta 敞口 740k shares
Top ΔOI: P 730 +6,726 ｜ C 755 +4,989 ｜ C 749 +4,217
仓位参考: Max Pain 737 ｜ Call Wall 755（+1.4%）（OI 8.5k） ｜ Put Wall 727（-2.4%）（OI 31.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 11.6%｜历史 Rank 51%（近端代理）｜IV/RV 0.75×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 739,520 股

📆 09-29 Forward Structure
存量OI: C 40.9k / P 102.8k，今日变化ΔOI: C +10.0k / P +26.4k，平值价格ATM: C $4.65 / P $3.91 ｜ ATM IV 13.6%，净 delta 敞口 86k shares
Top ΔOI: P 730 +14,160 ｜ P 712 +2,439 ｜ P 715 +1,795
仓位参考: Max Pain 735 ｜ Call Wall 751（+0.9%，弱）（OI 2.1k） ｜ Put Wall 725（-2.6%，弱）（OI 19.5k）
量化解读： 存量 Put 重｜ATM IV 13.6%｜历史 Rank 51%（近端代理）｜IV/RV 0.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 85,528 股

09-30（MEDIUM △）Top ΔOI: 720C +5,553 ｜ 680P -3,514
09-30（MEDIUM △）仓位参考: Max Pain 721 ｜ Call Wall 726（-2.5%）（OI 45.2k） ｜ Put Wall 730（-1.9%，弱）（OI 49.2k）

📆 10-01 Forward Structure
存量OI: C 30.3k / P 44.1k，今日变化ΔOI: C +9.8k / P +17.8k，平值价格ATM: C $6.61 / P $5.84 ｜ ATM IV 16.4%，净 delta 敞口 285k shares
Top ΔOI: P 660 +8,750 ｜ C 740 +2,210 ｜ P 725 +1,098
仓位参考: Max Pain 738 ｜ Call Wall 740（-0.6%）（OI 6.0k） ｜ Put Wall 740（-0.6%，弱）（OI 4.2k）
量化解读： 存量 Put 重｜ATM IV 16.4%｜历史 Rank 51%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 285,113 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/QQQ_evening.json