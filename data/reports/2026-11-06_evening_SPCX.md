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
🟡 **近现价集中开仓**: 11-09 130P ΔOI -2,092（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-09 115P ΔOI +8,326 占该期限总 OI 13.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 131.14 → 收盘 134.27（+2.4%） ｜ 今日高 135.32 ｜ 低 128.57 ｜ 昨收 123.62 → 收盘 134.27（+8.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 0.58 | ATM IV 62.3% | Skew 8.8pp | Term 0.98 | ExpMove ±4.1%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.98）｜保护溢价显著（Skew 8.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-09（3D）±4.1% ｜ 11-11（5D）±6.3% ｜ 11-13（7D）±7.8% ｜ 11-16（10D）±8.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,381,502 | GEX Change vs 上次快照 3,037,312 | Flip: Primary Flip: 135.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 736 / LOW 180 / INVALID 664
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 135.54（全链重定价，覆盖 83%）
最近结构参考: Flip 136（现价低于该位 0.9%）
量化视角： 负 Gamma（638万，无历史分位）｜负 Gamma 缓解（+304万）｜现价位于 Flip 下方 0.94%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 134（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 136（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +9.1k / P +14.4k ｜ Activity HIGH ｜ 3D
11-11  C +7.4k / P +5.5k ｜ Activity HIGH ｜ 5D
11-13  C +10.7k / P +6.3k ｜ Activity HIGH ｜ 7D
11-16  C +1.7k / P -89 ｜ Activity HIGH ｜ 10D

📆 11-09 Forward Structure
存量OI: C 22.4k / P 41.6k，今日变化ΔOI: C +9.1k / P +14.4k，平值价格ATM: C $2.89 / P $2.65 ｜ ATM IV 57.1%，净 delta 敞口 829k shares
Top ΔOI: P 115 +8,326 ｜ P 130 -2,092
仓位参考: Max Pain 130 ｜ Call Wall 130（-3.2%，弱）（OI 1.8k） ｜ Put Wall 122（-9.1%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 57.1%｜历史 Rank 70%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 828,861 股

📆 11-11 Forward Structure
存量OI: C 14.1k / P 10.9k，今日变化ΔOI: C +7.4k / P +5.5k，平值价格ATM: C $4.38 / P $4.05 ｜ ATM IV 67.7%，净 delta 敞口 364k shares
Top ΔOI: C 127 +1,047 ｜ C 130 +980
仓位参考: Max Pain 130 ｜ Call Wall 140（+4.3%，弱）（OI 1.3k） ｜ Put Wall 130（-3.2%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 67.7%｜历史 Rank 70%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 363,646 股

📆 11-13 Forward Structure
存量OI: C 93.3k / P 77.9k，今日变化ΔOI: C +10.7k / P +6.3k，平值价格ATM: C $5.40 / P $5.05 ｜ ATM IV 69.8%，净 delta 敞口 664k shares
Top ΔOI: P 100 +2,947 ｜ C 140 +1,882
仓位参考: Max Pain 141 ｜ Call Wall 140（+4.3%，弱）（OI 4.4k） ｜ Put Wall 125（-6.9%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜ATM IV 69.8%｜历史 Rank 70%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 664,124 股

📆 11-16 Forward Structure
存量OI: C 3.2k / P 1.5k，今日变化ΔOI: C +1.7k / P -89，平值价格ATM: C $5.89 / P $5.40 ｜ ATM IV 63.6%，净 delta 敞口 135k shares
Top ΔOI: P 180 -980 ｜ C 150 +589 ｜ C 130 +357
仓位参考: Max Pain 130 ｜ Call Wall 130（-3.2%，弱）（OI 0.4k） ｜ Put Wall 130（-3.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 63.6%｜历史 Rank 70%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 135,042 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SPCX_evening.json