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
🟡 **近现价集中开仓**: 12-04 82C ΔOI +12,892（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 79.96 → 今开 84.57（+5.8%） | 较昨收变动（含盘初走势） ｜ 今日高 84.67 ｜ 低 78.84

Options: P/C成交量 0.76 | OI比 0.62 | ATM IV 214.7% | Skew 10.3pp | Term 0.48 | ExpMove ±13.3%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜保护溢价显著（Skew 10.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±13.3% ｜ 12-11（14D）±17.6% ｜ 12-18（21D）±21.1% ｜ 12-24（27D）±22.6%
   ⇒ IV–VIX Spread: +187.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,035,068 | GEX Change vs 上次快照 28,882,637 | Flip: Primary Flip: 74.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 505 / LOW 167 / INVALID 456
结构观察区: Primary Flip 74.38（全链重定价，覆盖 98%）
Call Wall 85（弱结构｜现价低于该位 6.0%）
最近结构参考: Call Wall 85（现价低于该位 6.0%）
量化视角： 正 Gamma（1904万，无历史分位）｜由负转正（+2888万）｜现价位于 Flip 上方 7.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 84（MaxPain，仅结算参考） / 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 74（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 40.0P — Vol 20,285 | 最新价 $0.12 | OI 2063→19574 (ΔOI +17511张) | ΔOI/Volume 86.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17511张（+848.8% vs前日OI），连续性待观察（方向未知）
12-04 82.0C — Vol 13,374 | 最新价 $4.89 | OI 273→13165 (ΔOI +12892张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12892张（+4722.3% vs前日OI），连续性待观察（方向未知）
12-04 87.0C — Vol 13,276 | 最新价 $2.97 | OI 701→13191 (ΔOI +12490张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12490张（+1781.7% vs前日OI），连续性待观察（方向未知）
12-04 90.0C — Vol 13,769 | 最新价 $2.19 | OI 1101→12296 (ΔOI +11195张) | ΔOI/Volume 81.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11195张（+1016.8% vs前日OI），连续性待观察（方向未知）
12-04 85.0C — Vol 11,711 | 最新价 $3.70 | OI 1853→12120 (ΔOI +10267张) | ΔOI/Volume 87.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10267张（+554.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 64,355 张（Put 17,511 / Call 46,844），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 222.2k / P 138.0k，今日成交量: C 49.6k / P 37.6k，平值价格ATM: C $1.21 / P $1.52 ｜ ATM IV 214.7%，预期波动 ±3.4%，Max Pain 84
Top ΔOI: C 86 -13,303 ｜ C 90 -13,172 ｜ C 91 -6,320

📆 Forward Expiration Structure

12-04  C +79.6k / P +45.6k ｜ Activity HIGH ｜ 7D
12-11  C +4.5k / P +8.3k ｜ Activity HIGH ｜ 14D
12-18  C +12.3k / P +8.7k ｜ Activity HIGH ｜ 21D
12-24  C +0.5k / P +2.1k ｜ Activity MEDIUM △ ｜ 27D

📆 12-04 Forward Structure
存量OI: C 140.0k / P 124.4k，今日变化ΔOI: C +79.6k / P +45.6k，平值价格ATM: C $5.25 / P $5.35 ｜ ATM IV 119.9%，净 delta 敞口 2.5M shares
Top ΔOI: P 40 +17,511 ｜ C 82 +12,892 ｜ C 87 +12,490
仓位参考: Max Pain 82 ｜ Call Wall 87（+8.8%，弱）（OI 13.2k） ｜ Put Wall 80（+0.1%，弱）（OI 8.4k）
量化解读： 存量两侧均衡｜ATM IV 119.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,521,170 股

📆 12-11 Forward Structure
存量OI: C 17.9k / P 47.9k，今日变化ΔOI: C +4.5k / P +8.3k，平值价格ATM: C $7.04 / P $7.00 ｜ ATM IV 114.1%，净 delta 敞口 113k shares
Top ΔOI: P 65 +2,414 ｜ P 60 +1,771 ｜ P 70 +1,343
仓位参考: Max Pain 90 ｜ Call Wall 80（+0.1%，弱）（OI 0.6k） ｜ Put Wall 80（+0.1%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 114.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 113,471 股

📆 12-18 Forward Structure
存量OI: C 259.4k / P 179.5k，今日变化ΔOI: C +12.3k / P +8.7k，平值价格ATM: C $8.45 / P $8.44 ｜ ATM IV 108.9%，净 delta 敞口 465k shares
Top ΔOI: P 30 +5,296 ｜ C 100 +4,077 ｜ C 90 +2,713
仓位参考: Max Pain 105 ｜ Call Wall 85（+6.3%，弱）（OI 9.6k） ｜ Put Wall 80（+0.1%，弱）（OI 9.1k）
量化解读： 存量 Call 重｜ATM IV 108.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 465,424 股

12-24（MEDIUM △）Top ΔOI: 55P +689
12-24（MEDIUM △）仓位参考: Max Pain 110 ｜ Call Wall 85（+6.3%，弱）（OI 0.4k） ｜ Put Wall 80（+0.1%，弱）（OI 1.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/MSTR_morning.json