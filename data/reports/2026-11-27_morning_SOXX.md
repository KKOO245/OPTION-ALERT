# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $730.70 ｜ QQQ $650.99
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-11 135C ΔOI +1,597（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-24 100P ΔOI +10,726 占该期限总 OI 31.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 127.98 → 今开 132.18（+3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 132.30 ｜ 低 128.02

Options: P/C成交量 1.60 | OI比 0.32 | ATM IV 113.3% | Skew -28.4pp | Term 0.60 | ExpMove ±6.8%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜Put 保护异常便宜（Skew -28.4pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.32）+ 当日成交偏 Put（P/C量 1.60）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.60×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±6.8% ｜ 12-11（14D）±13.0% ｜ 12-18（21D）±11.6% ｜ 12-24（27D）±19.5%
   ⇒ IV–VIX Spread: +85.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,154,956 | GEX Change vs 上次快照 18,937,105 | Flip: Primary Flip: 132.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 560 / LOW 271 / INVALID 789
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 132.23（全链重定价，覆盖 93%）
最近结构参考: Flip 132（现价低于该位 2.6%）
量化视角： 负 Gamma（815万，无历史分位）｜负 Gamma 缓解（+1894万）｜现价位于 Flip 下方 2.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 133（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-24 100.0P — Vol 11,231 | 最新价 $2.45 | OI 145→10871 (ΔOI +10726张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10726张（+7397.2% vs前日OI），连续性待观察（方向未知）
12-24 131.0C — Vol 10,379 | 最新价 $7.00 | OI 4→10002 (ΔOI +9998张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9998张（+249950.0% vs前日OI），连续性待观察（方向未知）
12-18 110.0P — Vol 8,907 | 最新价 $3.50 | OI 8557→16266 (ΔOI +7709张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7709张（+90.1% vs前日OI），连续性待观察（方向未知）
12-18 145.0C — Vol 9,273 | 最新价 $2.90 | OI 5103→11094 (ΔOI +5991张) | ΔOI/Volume 64.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5991张（+117.4% vs前日OI），连续性待观察（方向未知）
12-18 105.0P — Vol 6,852 | 最新价 $2.60 | OI 3603→6818 (ΔOI +3215张) | ΔOI/Volume 46.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3215张（+89.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 37,639 张（Put 21,650 / Call 15,989），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 77.6k / P 24.8k，今日成交量: C 2.5k / P 4.0k，平值价格ATM: C $1.10 / P $1.38 ｜ ATM IV 113.3%，预期波动 ±1.9%，Max Pain 133
Top ΔOI: P 146 -3,072 ｜ P 150 -2,082 ｜ P 145 -1,544

📆 Forward Expiration Structure

12-04  C +1.9k / P -4.4k ｜ Activity HIGH ｜ 7D
12-11  C +2.1k / P +2.5k ｜ Activity HIGH ｜ 14D
12-18  C +11.2k / P +1.6k ｜ Activity HIGH ｜ 21D
12-24  C +10.3k / P +10.4k ｜ Activity HIGH ｜ 27D

📆 12-04 Forward Structure
存量OI: C 18.6k / P 53.4k，今日变化ΔOI: C +1.9k / P -4.4k，平值价格ATM: C $3.05 / P $5.66 ｜ ATM IV 88.6%，净 delta 敞口 468k shares
Top ΔOI: P 140 -1,606 ｜ P 122 -1,576 ｜ P 166 -1,212
仓位参考: Max Pain 145 ｜ Call Wall 133.33（+3.5%，弱）（OI 0.7k） ｜ Put Wall 130（+0.9%，弱）（OI 11.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 88.6%｜历史 Rank 100%（近端代理）｜IV/RV 0.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 468,125 股

📆 12-11 Forward Structure
存量OI: C 9.0k / P 14.8k，今日变化ΔOI: C +2.1k / P +2.5k，平值价格ATM: C $5.00 / P $11.80 ｜ ATM IV 79.7%，净 delta 敞口 46k shares
Top ΔOI: P 115 +1,611 ｜ C 135 +1,597 ｜ P 105 +1,079
仓位参考: Max Pain 135 ｜ Call Wall 135（+4.8%）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 79.7%｜历史 Rank 100%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,320 股

📆 12-18 Forward Structure
存量OI: C 287.1k / P 212.0k，今日变化ΔOI: C +11.2k / P +1.6k，平值价格ATM: C $5.98 / P $9.01 ｜ ATM IV 76.4%，净 delta 敞口 669k shares
Top ΔOI: P 125 -7,742 ｜ P 110 +7,709 ｜ C 145 +5,991
仓位参考: Max Pain 150 ｜ Put Wall 125（-3.0%，弱）（OI 26.5k）
量化解读： 存量 Call 重｜ATM IV 76.4%｜历史 Rank 100%（近端代理）｜IV/RV 0.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 668,537 股

📆 12-24 Forward Structure
存量OI: C 15.9k / P 18.7k，今日变化ΔOI: C +10.3k / P +10.4k，平值价格ATM: C $10.80 / P $14.34 ｜ ATM IV 68.5%，净 delta 敞口 405k shares
Top ΔOI: P 100 +10,726 ｜ C 131 +9,998 ｜ P 120 -548
仓位参考: Max Pain 131 ｜ Call Wall 131（+1.7%）（OI 10.0k）
量化解读： 存量两侧均衡｜ATM IV 68.5%｜历史 Rank 100%（近端代理）｜IV/RV 0.15×（近似）｜净 delta 敞口 正 404,643 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/SOXX_morning.json