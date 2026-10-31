# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 40C ΔOI +711（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 40C ΔOI +711 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 41.64 → 今开 39.26（-5.7%） | 较昨收变动（含盘初走势） ｜ 今日高 40.34 ｜ 低 39.00

Options: P/C成交量 0.48 | OI比 0.58 | ATM IV 96.4% | Skew -17.5pp | Term 0.66 | ExpMove ±8.9%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -17.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±8.9% ｜ 11-13（14D）±12.3% ｜ 11-20（21D）±12.0% ｜ 11-27（28D）±12.6%
   ⇒ IV–VIX Spread: +77.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,361,601 | GEX Change vs 上次快照 -2,347,286 | Flip: Primary Flip: 37.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 330 / LOW 59 / INVALID 137
结构观察区: Primary Flip 37.55（全链重定价，覆盖 93%）
最近结构参考: Flip 38（现价高于该位 6.8%）
量化视角： 正 Gamma（336万，无历史分位）｜正 Gamma 减弱（235万）｜现价位于 Flip 上方 6.80%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 41（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 38（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 44.0P — Vol 1,046 | 最新价 $4.10 | OI 9→1055 (ΔOI +1046张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1046张（+11622.2% vs前日OI），连续性待观察（方向未知）
11-13 40.0C — Vol 2,287 | 最新价 $3.30 | OI 62→773 (ΔOI +711张) | ΔOI/Volume 31.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增711张（+1146.8% vs前日OI），连续性待观察（方向未知）
11-06 44.0C — Vol 258 | 最新价 $1.11 | OI 526→741 (ΔOI +215张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增215张（+40.9% vs前日OI），连续性待观察（方向未知）
11-20 55.0C — Vol 320 | 最新价 $0.28 | OI 1781→1938 (ΔOI +157张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增157张（+8.8% vs前日OI），连续性待观察（方向未知）
11-06 45.0C — Vol 506 | 最新价 $0.85 | OI 1643→1765 (ΔOI +122张) | ΔOI/Volume 24.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增122张（+7.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,251 张（Put 1,046 / Call 1,205），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 13.2k / P 7.6k，今日成交量: C 0.4k / P 0.2k，平值价格ATM: C $0.46 / P $0.38 ｜ ATM IV 96.4%，预期波动 ±2.1%，Max Pain 41
Top ΔOI: P 45 -133 ｜ C 42 -119 ｜ C 45 +110

📆 Forward Expiration Structure

11-06  C +0.9k / P +0.2k ｜ Activity MEDIUM △ ｜ 7D
11-13  C +0.9k / P -0.3k ｜ Activity HIGH ｜ 14D
11-20  C +0.7k / P +0.9k ｜ Activity HIGH ｜ 21D
11-27  C +26 / P +12 ｜ Activity MEDIUM △ ｜ 28D

📆 11-06 Forward Structure
存量OI: C 9.9k / P 4.7k，今日变化ΔOI: C +0.9k / P +0.2k，平值价格ATM: C $1.94 / P $1.64 ｜ ATM IV 79.5%，净 delta 敞口 11k shares
Top ΔOI: C 44 +215
仓位参考: Max Pain 42 ｜ Call Wall 43（+7.2%，弱）（OI 1.0k） ｜ Put Wall 38（-5.2%）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 79.5%｜历史 Rank 91%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,757 股

📆 11-13 Forward Structure
存量OI: C 4.0k / P 2.0k，今日变化ΔOI: C +0.9k / P -0.3k，平值价格ATM: C $2.35 / P $2.58 ｜ ATM IV 73.4%，净 delta 敞口 58k shares
Top ΔOI: C 40 +711 ｜ P 39 -308 ｜ C 42 +75
仓位参考: Max Pain 40 ｜ Call Wall 40（-0.2%，弱）（OI 0.8k） ｜ Put Wall 39（-2.7%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 73.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 57,669 股

📆 11-20 Forward Structure
存量OI: C 16.9k / P 9.8k，今日变化ΔOI: C +0.7k / P +0.9k，平值价格ATM: C $2.32 / P $2.50 ｜ ATM IV 65.9%，净 delta 敞口 -54k shares
Top ΔOI: P 44 +1,046
仓位参考: Max Pain 45 ｜ Call Wall 40（-0.2%，弱）（OI 0.9k） ｜ Put Wall 40（-0.2%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 65.9%｜历史 Rank 91%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 53,611 股

11-27（MEDIUM △）Top ΔOI: 43P -10 ｜ 44C -10
11-27（MEDIUM △）仓位参考: Max Pain 44 ｜ Call Wall 44（+9.7%，弱）（OI 1.0k） ｜ Put Wall 38（-5.2%，弱）（OI 68）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/MP_morning.json