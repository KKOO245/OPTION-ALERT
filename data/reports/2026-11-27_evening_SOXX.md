# 期权晚报 2026-11-27（快照 21:00 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 132.18 → 收盘 134.07（+1.4%） ｜ 今日高 134.86 ｜ 低 128.01 ｜ 昨收 127.98 → 收盘 134.07（+4.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-04，窗口结束前不做对错判定）

Options: P/C成交量 0.42 | OI比 2.87 | ATM IV 81.5% | Skew 12.8pp | Term 0.75 | ExpMove ±9.4%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价显著（Skew 12.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.87×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±9.4% ｜ 12-11（14D）±8.2% ｜ 12-18（21D）±12.2% ｜ 12-24（27D）±19.2%
   ⇒ IV–VIX Spread: +57.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,740,786 | GEX Change vs 上次快照 -2,585,830 | Flip: Primary Flip: 138.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 539 / LOW 222 / INVALID 555
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 138.67（全链重定价，覆盖 100%）
最近结构参考: Flip 139（现价低于该位 3.3%）
量化视角： 负 Gamma（1074万，无历史分位）｜负 Gamma 加深（259万）｜现价位于 Flip 下方 3.32%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 145（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 139（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +0 / P +0 ｜ Activity LOW ｜ 7D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 14D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 21D
12-24  C +0 / P +0 ｜ Activity LOW ｜ 27D

📆 12-04 Forward Structure
存量OI: C 18.6k / P 53.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.50 / P $7.14 ｜ ATM IV 81.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 145 ｜ Call Wall 140（+4.4%，弱）（OI 0.8k） ｜ Put Wall 130（-3.0%，弱）（OI 11.5k）
量化解读： 存量 Put 重｜ATM IV 81.5%｜历史 Rank 98%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 135（+0.7%）（OI 2.7k） ｜ Put Wall 140（+4.4%，弱）（OI 0.9k）

12-18（Activity LOW）仓位参考: Max Pain 150 ｜ Put Wall 130（-3.0%，弱）（OI 11.3k）

12-24（Activity LOW）仓位参考: Max Pain 131 ｜ Call Wall 131（-2.3%）（OI 10.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SOXX_evening.json