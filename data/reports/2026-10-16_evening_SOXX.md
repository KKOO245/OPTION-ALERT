# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 500C ΔOI +975（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 580C ΔOI +700 占该期限总 OI 13.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 505.01 → 收盘 493.39（-2.3%） ｜ 今日高 509.60 ｜ 低 492.88 ｜ 昨收 514.71 → 收盘 493.39（-4.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 4.26 | OI比 2.24 | ATM IV 219.9% | Skew -6.1pp | Term 0.19 | ExpMove ±5.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.19，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.1pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 4.26）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.26×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±5.2% ｜ 10-30（14D）±3.0% ｜ 11-06（21D）±7.9% ｜ 11-13（28D）±4.5%
   ⇒ IV–VIX Spread: +199.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -35,120,647 | GEX Change vs 上次快照 16,553,873 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 67%（带内） ｜ IV 有效性: VALID 550 / LOW 247 / INVALID 855
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 500（弱结构｜现价低于该位 1.3%）
最近结构参考: Put Wall 500（现价低于该位 1.3%）
量化视角： 负 Gamma（3512万，无历史分位）｜负 Gamma 缓解（+1655万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 500（Put Wall，弱结构） / 530（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +2.8k / P +1.0k ｜ Activity HIGH ｜ 7D
10-30  C +7.1k / P -3.5k ｜ Activity HIGH ｜ 14D
11-06  C +1.5k / P +0.3k ｜ Activity HIGH ｜ 21D
11-13  C +76 / P -37 ｜ Activity HIGH ｜ 28D

📆 10-23 Forward Structure
存量OI: C 6.9k / P 15.5k，今日变化ΔOI: C +2.8k / P +1.0k，平值价格ATM: C $14.11 / P $11.64 ｜ ATM IV 46.5%，净 delta 敞口 47k shares
Top ΔOI: C 500 +975 ｜ P 490 +807 ｜ C 510 +298
仓位参考: Max Pain 548 ｜ Call Wall 500（+1.3%，弱）（OI 1.1k） ｜ Put Wall 510（+3.4%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 47,481 股

📆 10-30 Forward Structure
存量OI: C 14.8k / P 45.0k，今日变化ΔOI: C +7.1k / P -3.5k，平值价格ATM: C $0.00 / P $15.00 ｜ ATM IV 45.6%，净 delta 敞口 264k shares
Top ΔOI: P 500 -5,051 ｜ P 480 +3,482 ｜ C 600 +2,813
仓位参考: Max Pain 550 ｜ Put Wall 500（+1.3%）（OI 12.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 263,961 股

📆 11-06 Forward Structure
存量OI: C 2.9k / P 2.4k，今日变化ΔOI: C +1.5k / P +0.3k，平值价格ATM: C $20.98 / P $18.05 ｜ ATM IV 43.8%，净 delta 敞口 9k shares
Top ΔOI: C 580 +700 ｜ C 550 +411
仓位参考: Max Pain 550 ｜ Put Wall 500（+1.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 43.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,055 股

📆 11-13 Forward Structure
存量OI: C 1.0k / P 1.7k，今日变化ΔOI: C +76 / P -37，平值价格ATM: C $0.00 / P $22.32 ｜ ATM IV 42.8%，净 delta 敞口 5k shares
Top ΔOI: P 515 -43 ｜ C 520 +26
仓位参考: Max Pain 560 ｜ Put Wall 520（+5.4%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.63×（近似）｜净 delta 敞口 正 4,520 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SOXX_evening.json