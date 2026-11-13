# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 390P ΔOI +1,948（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 460C ΔOI +8,934 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 401.94 → 收盘 390.22（-2.9%） ｜ 今日高 404.40 ｜ 低 385.83 ｜ 昨收 397.45 → 收盘 390.22（-1.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 1.29 | ATM IV 48.5% | Skew 16.3pp | Term 0.66 | ExpMove ±2.6%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 16.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±2.6% ｜ 11-18（5D）±4.2% ｜ 11-20（7D）±0.1% ｜ 11-23（10D）±5.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 85,603,272 | GEX Change vs 上次快照 429,282 | Flip: Primary Flip: 372.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 1350 / LOW 271 / INVALID 1053
结构观察区: Primary Flip 372.61（全链重定价，覆盖 85%）
Call Wall 400（现价低于该位 2.4%）
最近结构参考: Call Wall 400（现价低于该位 2.4%）
量化视角： 正 Gamma（8560万，无历史分位）｜正 Gamma 增强（+43万）｜现价位于 Flip 上方 4.73%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 375（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 373（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-16  C +25.3k / P +10.9k ｜ Activity HIGH ｜ 3D
11-18  C +4.7k / P +3.6k ｜ Activity HIGH ｜ 5D
11-20  C +12.3k / P +21.5k ｜ Activity HIGH ｜ 7D
11-23  C +1.2k / P +0.6k ｜ Activity HIGH ｜ 10D

📆 11-16 Forward Structure
存量OI: C 56.7k / P 31.5k，今日变化ΔOI: C +25.3k / P +10.9k，平值价格ATM: C $5.25 / P $5.05 ｜ ATM IV 36.4%，净 delta 敞口 -78k shares
Top ΔOI: P 390 +1,948
仓位参考: Max Pain 388 ｜ Call Wall 400（+2.5%，弱）（OI 3.0k） ｜ Put Wall 370（-5.2%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 36.4%｜历史 Rank 38%（近端代理）｜IV/RV 0.63×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 78,479 股

📆 11-18 Forward Structure
存量OI: C 14.8k / P 15.6k，今日变化ΔOI: C +4.7k / P +3.6k，平值价格ATM: C $8.25 / P $8.13 ｜ ATM IV 45.0%，净 delta 敞口 6k shares
Top ΔOI: C 430 +1,810 ｜ C 420 +436
仓位参考: Max Pain 390 ｜ Call Wall 410（+5.1%，弱）（OI 1.2k） ｜ Put Wall 392.5（+0.6%）（OI 2.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.0%｜历史 Rank 38%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,898 股

📆 11-20 Forward Structure
存量OI: C 297.9k / P 349.8k，今日变化ΔOI: C +12.3k / P +21.5k，平值价格ATM: C $0.29 / P $0.00 ｜ ATM IV 21.4%，净 delta 敞口 353k shares
Top ΔOI: C 380 +1,934
仓位参考: Max Pain 375 ｜ Call Wall 400（+2.5%，弱）（OI 22.0k）
量化解读： 存量两侧均衡｜ATM IV 21.4%｜历史 Rank 38%（近端代理）｜IV/RV 0.37×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 352,867 股

📆 11-23 Forward Structure
存量OI: C 3.6k / P 4.2k，今日变化ΔOI: C +1.2k / P +0.6k，平值价格ATM: C $11.45 / P $11.05 ｜ ATM IV 43.5%，净 delta 敞口 -632 shares
Top ΔOI: P 392 +184 ｜ C 420 +157
仓位参考: Max Pain 390 ｜ Call Wall 420（+7.6%，弱）（OI 0.4k） ｜ Put Wall 392.5（+0.6%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.5%｜历史 Rank 38%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 负 632 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/TSLA_evening.json