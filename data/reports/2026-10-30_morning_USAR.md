# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $759.94 ｜ QQQ $692.72
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 10.52 → 今开 9.88（-6.1%） | 较昨收变动（含盘初走势） ｜ 今日高 10.04 ｜ 低 9.72

Options: P/C成交量 0.33 | OI比 0.32 | ATM IV 152.8% | Skew -20.1pp | Term 0.59 | ExpMove ±10.9%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜Put 保护异常便宜（Skew -20.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±10.9% ｜ 11-13（14D）±12.4% ｜ 11-20（21D）±18.0% ｜ 11-27（28D）±23.5%
   ⇒ IV–VIX Spread: +134.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,240,565 | GEX Change vs 上次快照 -3,210,796 | Flip: Primary Flip: 9.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 200 / LOW 71 / INVALID 149
结构观察区: Primary Flip 9.02（全链重定价，覆盖 91%）
Put Wall 10（弱结构｜现价低于该位 1.3%）
最近结构参考: Put Wall 10（现价低于该位 1.3%）
量化视角： 正 Gamma（324万，无历史分位）｜正 Gamma 减弱（321万）｜现价位于 Flip 上方 9.47%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 8.0P — Vol 922 | 最新价 $0.12 | OI 965→1859 (ΔOI +894张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增894张（+92.6% vs前日OI），连续性待观察（方向未知）
10-30 11.0C — Vol 1,779 | 最新价 $0.06 | OI 4950→5199 (ΔOI +249张) | ΔOI/Volume 14.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增249张（+5.0% vs前日OI），值得跟踪（方向未知）
11-06 12.0C — Vol 509 | 最新价 $0.17 | OI 729→940 (ΔOI +211张) | ΔOI/Volume 41.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增211张（+28.9% vs前日OI），连续性待观察（方向未知）
10-30 11.5C — Vol 718 | 最新价 $0.02 | OI 3542→3701 (ΔOI +159张) | ΔOI/Volume 22.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增159张（+4.5% vs前日OI），值得跟踪（方向未知）
10-30 10.5P — Vol 681 | 最新价 $0.19 | OI 656→806 (ΔOI +150张) | ΔOI/Volume 22.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增150张（+22.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,663 张（Put 1,044 / Call 619），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 29.5k / P 9.5k，今日成交量: C 1.0k / P 0.3k，平值价格ATM: C $0.12 / P $0.23 ｜ ATM IV 152.8%，预期波动 ±3.6%，Max Pain 10
Top ΔOI: P 12 -962 ｜ C 11 +249 ｜ C 10 -176

📆 Forward Expiration Structure

11-06  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 7D
11-13  C +81 / P +25 ｜ Activity MEDIUM △ ｜ 14D
11-20  C -0.3k / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
11-27  C +0.3k / P +41 ｜ Activity MEDIUM △ ｜ 28D

📆 11-06 Forward Structure
存量OI: C 8.8k / P 5.6k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $0.43 / P $0.65 ｜ ATM IV 89.0%，净 delta 敞口 -14k shares
Top ΔOI: C 10 -126
仓位参考: Max Pain 10 ｜ Call Wall 10（+1.3%，弱）（OI 0.8k） ｜ Put Wall 9（-8.8%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 89.0%｜历史 Rank 84%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 14,299 股

11-13（MEDIUM △）Top ΔOI: 10P +26
11-13（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 9（-8.8%，弱）（OI 0.6k） ｜ Put Wall 9（-8.8%，弱）（OI 0.4k）

11-20（MEDIUM △）Top ΔOI: 12P -317
11-20（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 9.5（-3.7%，弱）（OI 1.4k） ｜ Put Wall 10（+1.3%，弱）（OI 6.3k）

11-27（MEDIUM △）Top ΔOI: 9P +21
11-27（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 10（+1.3%）（OI 1.6k） ｜ Put Wall 9.5（-3.7%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/USAR_morning.json