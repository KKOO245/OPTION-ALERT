# 期权晨报 2026-11-27（快照 10:20 ET）

📊 市场环境

SPY $722.09 ｜ QQQ $642.10
VIX 27.52 ↑2.7%（5D -23.3%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 84.99 → 今开 89.67（+5.5%） | 较昨收变动（含盘初走势） ｜ 今日高 89.88 ｜ 低 83.88

Options: P/C成交量 0.77 | OI比 0.31 | ATM IV 235.1% | Skew 11.4pp | Term 0.55 | ExpMove ±16.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜保护溢价显著（Skew 11.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±16.0% ｜ 12-11（14D）±22.6% ｜ 12-18（21D）±26.0% ｜ 12-24（27D）±28.0%
   ⇒ IV–VIX Spread: +207.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 3,922,599 | GEX Change vs 上次快照 9,970,655 | Flip: Primary Flip: 79.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 524 / LOW 130 / INVALID 386
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 79.19（全链重定价，覆盖 95%）
Put Wall 80（弱结构｜现价高于该位 5.7%）
最近结构参考: Put Wall 80（现价高于该位 5.7%）
量化视角： 正 Gamma（392万，无历史分位）｜由负转正（+997万）｜现价位于 Flip 上方 6.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 90（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 50.0P — Vol 4,201 | 最新价 $0.19 | OI 206→4152 (ΔOI +3946张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3946张（+1915.5% vs前日OI），连续性待观察（方向未知）
11-27 80.0C — Vol 6,672 | 最新价 $6.35 | OI 412→2517 (ΔOI +2105张) | ΔOI/Volume 31.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2105张（+510.9% vs前日OI），连续性待观察（方向未知）
12-18 100.0C — Vol 3,134 | 最新价 $5.70 | OI 2441→4205 (ΔOI +1764张) | ΔOI/Volume 56.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1764张（+72.3% vs前日OI），连续性待观察（方向未知）
11-27 90.0C — Vol 10,383 | 最新价 $1.13 | OI 1890→3467 (ΔOI +1577张) | ΔOI/Volume 15.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1577张（+83.4% vs前日OI），连续性待观察（方向未知）
12-18 40.0P — Vol 1,557 | 最新价 $0.53 | OI 544→1849 (ΔOI +1305张) | ΔOI/Volume 83.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1305张（+239.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,697 张（Put 5,251 / Call 5,446），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 113.8k / P 34.8k，今日成交量: C 14.9k / P 11.5k，平值价格ATM: C $1.19 / P $2.02 ｜ ATM IV 235.1%，预期波动 ±3.8%，Max Pain 90
Top ΔOI: C 80 +2,105 ｜ C 90 +1,577 ｜ P 65 +1,012

📆 Forward Expiration Structure

12-04  C +6.7k / P +6.7k ｜ Activity HIGH ｜ 7D
12-11  C +1.9k / P +0.4k ｜ Activity MEDIUM △ ｜ 14D
12-18  C +6.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
12-24  C +0.7k / P +0.2k ｜ Activity MEDIUM △ ｜ 27D

📆 12-04 Forward Structure
存量OI: C 36.7k / P 23.4k，今日变化ΔOI: C +6.7k / P +6.7k，平值价格ATM: C $6.55 / P $7.00 ｜ ATM IV 141.1%，净 delta 敞口 175k shares
Top ΔOI: C 100 +846
仓位参考: Max Pain 93 ｜ Call Wall 90（+6.4%，弱）（OI 1.2k） ｜ Put Wall 90（+6.4%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 141.1%｜历史 Rank 100%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 175,405 股

12-11（MEDIUM △）Top ΔOI: 80C +358 ｜ 100C +220
12-11（MEDIUM △）仓位参考: Max Pain 100 ｜ Call Wall 90（+6.4%，弱）（OI 0.5k） ｜ Put Wall 85（+0.5%，弱）（OI 1.1k）

12-18（MEDIUM △）Top ΔOI: 180P -1,895 ｜ 100C +1,764
12-18（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 80（-5.4%，弱）（OI 8.0k）

12-24（MEDIUM △）Top ΔOI: 95C +99
12-24（MEDIUM △）仓位参考: Max Pain 115 ｜ Put Wall 80（-5.4%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/NBIS_morning.json