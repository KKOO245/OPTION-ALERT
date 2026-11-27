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
🟡 **近现价集中开仓**: 11-30 40C ΔOI +1,498（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 38C ΔOI +3,504 占该期限总 OI 14.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 39.56 → 收盘 39.40（-0.4%） ｜ 今日高 39.65 ｜ 低 38.92 ｜ 昨收 37.10 → 收盘 39.40（+6.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-04，窗口结束前不做对错判定）

Options: P/C成交量 1.00 | OI比 0.30 | ATM IV 94.0% | Skew 18.8pp | Term 0.57 | ExpMove ±3.1%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价显著（Skew 18.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-30（3D）±3.1% ｜ 12-02（5D）±5.0% ｜ 12-04（7D）±6.5% ｜ 12-07（10D）±6.8%
   ⇒ IV–VIX Spread: +70.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,818,680 | GEX Change vs 上次快照 -14,646,452 | Flip: Primary Flip: 36.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 814 / LOW 185 / INVALID 757
结构观察区: Primary Flip 36.18（全链重定价，覆盖 85%）
Put Wall 40（弱结构｜现价低于该位 1.5%）
最近结构参考: Put Wall 40（现价低于该位 1.5%）
量化视角： 正 Gamma（3982万，无历史分位）｜正 Gamma 减弱（1465万）｜现价位于 Flip 上方 8.90%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 38（MaxPain，仅结算参考）；上方 40（Put Wall，弱结构）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-30  C +7.6k / P +0.9k ｜ Activity HIGH ｜ 3D
12-02  C +8.3k / P +1.7k ｜ Activity HIGH ｜ 5D
12-04  C +6.0k / P +0.9k ｜ Activity HIGH ｜ 7D
12-07  C +3.3k / P +0.4k ｜ Activity HIGH ｜ 10D

📆 11-30 Forward Structure
存量OI: C 37.1k / P 14.4k，今日变化ΔOI: C +7.6k / P +0.9k，平值价格ATM: C $0.59 / P $0.62 ｜ ATM IV 42.6%，净 delta 敞口 505k shares
Top ΔOI: C 40 +1,498 ｜ C 38 +1,213 ｜ C 36 +1,078
仓位参考: Max Pain 38 ｜ Call Wall 40（+1.5%，弱）（OI 3.8k） ｜ Put Wall 39（-1.0%）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 42.6%｜历史 Rank 98%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 505,020 股

📆 12-02 Forward Structure
存量OI: C 18.3k / P 6.2k，今日变化ΔOI: C +8.3k / P +1.7k，平值价格ATM: C $0.96 / P $1.02 ｜ ATM IV 52.8%，净 delta 敞口 494k shares
Top ΔOI: C 38 +3,504 ｜ C 40 +1,353 ｜ C 38 +778
仓位参考: Max Pain 38 ｜ Call Wall 42（+6.6%，弱）（OI 5.1k） ｜ Put Wall 39（-1.0%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 52.8%｜历史 Rank 98%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 493,947 股

📆 12-04 Forward Structure
存量OI: C 121.5k / P 22.4k，今日变化ΔOI: C +6.0k / P +0.9k，平值价格ATM: C $1.19 / P $1.36 ｜ ATM IV 57.2%，净 delta 敞口 303k shares
Top ΔOI: C 42 +1,417 ｜ C 42 +1,109 ｜ C 36 +583
仓位参考: Max Pain 40 ｜ Put Wall 40（+1.5%）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 57.2%｜历史 Rank 98%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 302,894 股

📆 12-07 Forward Structure
存量OI: C 4.3k / P 1.7k，今日变化ΔOI: C +3.3k / P +0.4k，平值价格ATM: C $1.16 / P $1.52 ｜ ATM IV 52.7%，净 delta 敞口 276k shares
Top ΔOI: C 34 +2,521 ｜ C 34 +168 ｜ C 40 +117
仓位参考: Max Pain 34 ｜ Call Wall 38（-3.6%，弱）（OI 0.6k） ｜ Put Wall 36（-8.6%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 52.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 276,036 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SLV_evening.json