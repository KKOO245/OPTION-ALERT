# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 12-04 105C ΔOI +7,279（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-04 105C ΔOI +7,279 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 103.72 → 今开 108.44（+4.6%） | 较昨收变动（含盘初走势） ｜ 今日高 108.70 ｜ 低 104.44

Options: P/C成交量 0.63 | OI比 0.64 | ATM IV 126.1% | Skew 10.5pp | Term 0.62 | ExpMove ±9.4%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价显著（Skew 10.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±9.4% ｜ 12-11（14D）±13.5% ｜ 12-18（21D）±15.1% ｜ 12-24（27D）±17.1%
   ⇒ IV–VIX Spread: +98.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,308,575 | GEX Change vs 上次快照 22,498,299 | Flip: Primary Flip: 97.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 381 / LOW 224 / INVALID 477
结构观察区: Primary Flip 97.03（全链重定价，覆盖 90%）
Put Wall 100（弱结构｜现价高于该位 5.4%）
最近结构参考: Put Wall 100（现价高于该位 5.4%）
量化视角： 正 Gamma（1131万，无历史分位）｜由负转正（+2250万）｜现价位于 Flip 上方 8.68%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 108（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 97（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 105.0C — Vol 7,555 | 最新价 $4.77 | OI 139→7418 (ΔOI +7279张) | ΔOI/Volume 96.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7279张（+5236.7% vs前日OI），连续性待观察（方向未知）
12-04 101.0C — Vol 7,323 | 最新价 $6.85 | OI 7→7268 (ΔOI +7261张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7261张（+103728.6% vs前日OI），连续性待观察（方向未知）
12-04 107.0C — Vol 3,649 | 最新价 $3.80 | OI 249→3506 (ΔOI +3257张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3257张（+1308.0% vs前日OI），连续性待观察（方向未知）
12-04 96.0P — Vol 3,014 | 最新价 $2.48 | OI 127→3080 (ΔOI +2953张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2953张（+2325.2% vs前日OI），连续性待观察（方向未知）
12-04 100.0P — Vol 3,677 | 最新价 $3.70 | OI 1324→3745 (ΔOI +2421张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2421张（+182.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,171 张（Put 5,374 / Call 17,797），跨 1 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 57.1k / P 36.5k，今日成交量: C 5.7k / P 3.6k，平值价格ATM: C $1.04 / P $1.06 ｜ ATM IV 126.1%，预期波动 ±2.0%，Max Pain 108
Top ΔOI: C 114 -3,179 ｜ C 116 -2,190 ｜ C 118 -1,820

📆 Forward Expiration Structure

12-04  C +29.1k / P +7.5k ｜ Activity HIGH ｜ 7D
12-11  C +0.5k / P -0.2k ｜ Activity MEDIUM △ ｜ 14D
12-18  C +1.6k / P +0.9k ｜ Activity MEDIUM △ ｜ 21D
12-24  C +0.1k / P +0.5k ｜ Activity HIGH ｜ 27D

📆 12-04 Forward Structure
存量OI: C 44.2k / P 26.4k，今日变化ΔOI: C +29.1k / P +7.5k，平值价格ATM: C $5.10 / P $4.82 ｜ ATM IV 82.2%，净 delta 敞口 1.4M shares
Top ΔOI: C 105 +7,279 ｜ C 101 +7,261 ｜ C 107 +3,257
仓位参考: Max Pain 101 ｜ Call Wall 105（-0.4%，弱）（OI 7.4k） ｜ Put Wall 100（-5.2%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 82.2%｜历史 Rank 95%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,366,708 股

12-11（MEDIUM △）Top ΔOI: 94P +202
12-11（MEDIUM △）仓位参考: Max Pain 120 ｜ Call Wall 110（+4.3%，弱）（OI 0.3k） ｜ Put Wall 100（-5.2%，弱）（OI 0.7k）

12-18（MEDIUM △）Top ΔOI: 80P +1,099
12-18（MEDIUM △）仓位参考: Max Pain 130 ｜ Put Wall 110（+4.3%）（OI 7.9k）

📆 12-24 Forward Structure
存量OI: C 4.3k / P 2.5k，今日变化ΔOI: C +0.1k / P +0.5k，平值价格ATM: C $10.07 / P $8.00 ｜ ATM IV 78.4%，净 delta 敞口 -1k shares
仓位参考: Max Pain 105 ｜ Call Wall 105（-0.4%，弱）（OI 0.5k） ｜ Put Wall 105（-0.4%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.4%｜历史 Rank 95%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 负 1,130 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/COIN_morning.json