# 期权晚报 2026-10-30（快照 16:40 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 492P ΔOI +4,485（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 500P ΔOI +1,033 占该期限总 OI 11.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 479.36 → 收盘 471.51（-1.6%） ｜ 今日高 483.39 ｜ 低 460.10 ｜ 昨收 513.86 → 收盘 471.51（-8.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 5.15 | OI比 6.15 | ATM IV 163.5% | Skew 143.3pp | Term 0.28 | ExpMove ±6.9%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.28，近月 IV 高于远月）｜保护溢价显著（Skew 143.3pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 5.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 5.15×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 6.15×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±6.9% ｜ 11-13（14D）±8.7% ｜ 11-20（21D）±8.9% ｜ 11-27（28D）±9.6%
   ⇒ IV–VIX Spread: +144.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -26,899,982 | GEX Change vs 上次快照 28,851,704 | Flip: Primary Flip: 512.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 558 / LOW 231 / INVALID 803
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 512.25（全链重定价，覆盖 88%）
最近结构参考: Flip 512（现价低于该位 8.0%）
量化视角： 负 Gamma（2690万，无历史分位）｜负 Gamma 缓解（+2885万）｜现价位于 Flip 下方 7.95%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 502（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 512（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.7k / P +9.2k ｜ Activity HIGH ｜ 7D
11-13  C -0.3k / P +0.4k ｜ Activity HIGH ｜ 14D
11-20  C +2.3k / P +6.3k ｜ Activity HIGH ｜ 21D
11-27  C +42 / P +1.1k ｜ Activity HIGH ｜ 28D

📆 11-06 Forward Structure
存量OI: C 38.6k / P 19.4k，今日变化ΔOI: C +0.7k / P +9.2k，平值价格ATM: C $13.00 / P $19.69 ｜ ATM IV 54.2%，净 delta 敞口 -465k shares
Top ΔOI: P 492 +4,485 ｜ P 460 +4,441 ｜ P 500 +239
仓位参考: Max Pain 505 ｜ Put Wall 460（-2.4%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 464,693 股

📆 11-13 Forward Structure
存量OI: C 24.7k / P 7.9k，今日变化ΔOI: C -0.3k / P +0.4k，平值价格ATM: C $21.70 / P $19.12 ｜ ATM IV 49.5%，净 delta 敞口 -24k shares
Top ΔOI: P 480 +378 ｜ C 500 -90
仓位参考: Max Pain 510 ｜ Put Wall 460（-2.4%）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 49.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 24,000 股

📆 11-20 Forward Structure
存量OI: C 41.7k / P 69.4k，今日变化ΔOI: C +2.3k / P +6.3k，平值价格ATM: C $21.00 / P $21.17 ｜ ATM IV 50.9%，净 delta 敞口 -258k shares
Top ΔOI: P 475 +4,517 ｜ P 465 +898 ｜ C 575 +745
仓位参考: Max Pain 530 ｜ Call Wall 500（+6.0%，弱）（OI 1.4k） ｜ Put Wall 460（-2.4%，弱）（OI 7.0k）
量化解读： 存量 Put 重｜ATM IV 50.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 257,622 股

📆 11-27 Forward Structure
存量OI: C 4.1k / P 5.1k，今日变化ΔOI: C +42 / P +1.1k，平值价格ATM: C $22.10 / P $23.00 ｜ ATM IV 45.7%，净 delta 敞口 -68k shares
Top ΔOI: P 500 +1,033
仓位参考: Max Pain 505 ｜ Put Wall 500（+6.0%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 45.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 67,760 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/SOXX_evening.json