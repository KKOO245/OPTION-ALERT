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


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 89.67 → 收盘 89.46（-0.2%） ｜ 今日高 89.88 ｜ 低 83.88 ｜ 昨收 84.99 → 收盘 89.46（+5.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 0.50 | OI比 0.64 | ATM IV 128.1% | Skew 10.1pp | Term 0.90 | ExpMove ±14.5%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构正常（Term 0.90）｜保护溢价显著（Skew 10.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±14.5% ｜ 12-11（14D）±22.2% ｜ 12-18（21D）±25.4% ｜ 12-24（27D）±26.9%
   ⇒ IV–VIX Spread: +104.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,693,973 | GEX Change vs 上次快照 -6,616,572 | Flip: Primary Flip: 97.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 514 / LOW 65 / INVALID 181
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 97.08（全链重定价，覆盖 100%）
最近结构参考: Flip 97（现价低于该位 7.9%）
量化视角： 负 Gamma（269万，无历史分位）｜由正转负（662万）｜现价位于 Flip 下方 7.85%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 93（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 97（全链重定价，覆盖 100%）。
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
存量OI: C 36.7k / P 23.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.60 / P $6.35 ｜ ATM IV 128.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 93 ｜ Call Wall 90（+0.6%，弱）（OI 1.2k） ｜ Put Wall 90（+0.6%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 128.1%｜历史 Rank 76%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 100 ｜ Call Wall 90（+0.6%，弱）（OI 0.5k） ｜ Put Wall 85（-5.0%，弱）（OI 1.1k）

12-18（Activity LOW）仓位参考: Max Pain 135 ｜ Put Wall 90（+0.6%，弱）（OI 4.1k）

12-24（Activity LOW）仓位参考: Max Pain 115 ｜ Put Wall 90（+0.6%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=108 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=108）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/NBIS_evening.json