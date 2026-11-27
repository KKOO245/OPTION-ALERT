# 期权晚报 2026-11-27（快照 16:40 ET）

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

🔍 重点速览
🟡 **近现价集中开仓**: 11-30 78C ΔOI +700（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 67P ΔOI +720 占该期限总 OI 28.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 77.12 → 收盘 79.18（+2.7%） ｜ 今日高 79.23 ｜ 低 76.52 ｜ 昨收 73.89 → 收盘 79.18（+7.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-04，窗口结束前不做对错判定）

Options: P/C成交量 0.10 | OI比 0.24 | ATM IV 86.3% | Skew 29.1pp | Term 0.57 | ExpMove ±4.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价显著（Skew 29.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.10×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±4.4% ｜ 12-02（5D）±2.0% ｜ 12-04（7D）±5.9% ｜ 12-07（10D）±6.9%
   ⇒ IV–VIX Spread: +62.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 20,393,438 | GEX Change vs 上次快照 -9,036,256 | Flip: Primary Flip: 76.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 489 / LOW 175 / INVALID 630
结构观察区: Primary Flip 76.51（全链重定价，覆盖 87%）
Put Wall 75（弱结构｜现价高于该位 5.6%）
最近结构参考: Flip 77（现价高于该位 3.5%）
量化视角： 正 Gamma（2039万，无历史分位）｜正 Gamma 减弱（904万）｜现价位于 Flip 上方 3.49%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall，弱结构） / 71（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 77（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +1.2k / P +0.6k ｜ Activity HIGH ｜ 3D
12-02  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 5D
12-04  C +35.6k / P +3.4k ｜ Activity HIGH ｜ 7D
12-07  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 4.5k / P 2.8k，今日变化ΔOI: C +1.2k / P +0.6k，平值价格ATM: C $1.03 / P $2.48 ｜ ATM IV 41.8%，净 delta 敞口 90k shares
Top ΔOI: C 78 +700
仓位参考: Max Pain 71 ｜ Call Wall 80（+1.0%）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 41.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 90,236 股

📆 12-02 Forward Structure
存量OI: C 1.2k / P 1.4k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $1.55 / P $0.00 ｜ ATM IV 46.6%，净 delta 敞口 13k shares
Top ΔOI: P 73 +50 ｜ C 79 +40
仓位参考: Max Pain 73 ｜ Call Wall 75（-5.3%）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 46.6%｜历史 Rank 100%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 正 12,570 股

📆 12-04 Forward Structure
存量OI: C 48.5k / P 20.9k，今日变化ΔOI: C +35.6k / P +3.4k，平值价格ATM: C $1.68 / P $3.00 ｜ ATM IV 50.0%，净 delta 敞口 2.2M shares
Top ΔOI: C 76 +17,564 ｜ C 79 +17,449
仓位参考: Max Pain 76 ｜ Call Wall 76（-4.0%，弱）（OI 20.6k） ｜ Put Wall 75（-5.3%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 50.0%｜历史 Rank 100%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,226,489 股

📆 12-07 Forward Structure
存量OI: C 1.0k / P 0.6k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $1.91 / P $3.57 ｜ ATM IV 46.6%，净 delta 敞口 48k shares
Top ΔOI: C 77 +610 ｜ C 80 +71
仓位参考: Max Pain 72 ｜ Call Wall 77（-2.8%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 46.6%｜历史 Rank 100%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 正 47,583 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/GDX_evening.json