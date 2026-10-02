# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $753.63
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 140C ΔOI +1,374（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 137.76 → 今开 139.41（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 139.57 ｜ 低 135.18

Options: P/C成交量 0.36 | OI比 0.75 | ATM IV 65.4% | Skew -0.7pp | Term 0.88 | ExpMove ±5.2%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±5.2% ｜ 10-16（14D）±7.5% ｜ 10-23（21D）±9.1% ｜ 10-30（28D）±12.9%
   ⇒ IV–VIX Spread: +49.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 17,499,364 | GEX Change vs 上次快照 -3,798,622 | Flip: Primary Flip: 131.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 538 / LOW 55 / INVALID 111
结构观察区: Primary Flip 131.71（全链重定价，覆盖 96%）
Put Wall 125（弱结构｜现价高于该位 9.1%） | Call Wall 150（现价低于该位 9.1%）
最近结构参考: Flip 132（现价高于该位 3.6%）
量化视角： 正 Gamma（1750万，无历史分位）｜正 Gamma 减弱（380万）｜现价位于 Flip 上方 3.56%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（Put Wall，弱结构） / 132（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 140.0C — Vol 2,504 | 最新价 $3.10 | OI 607→1981 (ΔOI +1374张) | ΔOI/Volume 54.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1374张（+226.4% vs前日OI），连续性待观察（方向未知）
10-16 142.0C — Vol 1,018 | 最新价 $3.95 | OI 152→804 (ΔOI +652张) | ΔOI/Volume 64.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增652张（+428.9% vs前日OI），连续性待观察（方向未知）
10-09 145.0C — Vol 1,263 | 最新价 $1.45 | OI 844→1277 (ΔOI +433张) | ΔOI/Volume 34.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增433张（+51.3% vs前日OI），连续性待观察（方向未知）
10-02 141.0C — Vol 2,381 | 最新价 $0.54 | OI 1161→1562 (ΔOI +401张) | ΔOI/Volume 16.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增401张（+34.5% vs前日OI），连续性待观察（方向未知）
10-09 143.0C — Vol 546 | 最新价 $2.07 | OI 152→545 (ΔOI +393张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增393张（+258.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,253 张（Put 0 / Call 3,253），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 33.9k / P 25.5k，今日成交量: C 3.8k / P 1.4k，平值价格ATM: C $1.04 / P $0.89 ｜ ATM IV 65.4%，预期波动 ±1.4%，Max Pain 132
Top ΔOI: C 145 -644 ｜ C 140 -470 ｜ C 141 +401

📆 Forward Expiration Structure

10-09  C +2.6k / P -25 ｜ Activity MEDIUM △ ｜ 7D
10-16  C +0.6k / P -0.3k ｜ Activity HIGH ｜ 14D
10-23  C +0.4k / P -0.5k ｜ Activity LOW ｜ 21D
10-30  C +0.3k / P -46 ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 16.0k / P 11.8k，今日变化ΔOI: C +2.6k / P -25，平值价格ATM: C $3.80 / P $3.28 ｜ ATM IV 45.9%，净 delta 敞口 58k shares
Top ΔOI: C 140 +1,374 ｜ C 145 +433 ｜ C 143 +393
仓位参考: Max Pain 135 ｜ Call Wall 150（+10.0%）（OI 4.3k） ｜ Put Wall 131（-4.0%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 45.9%｜历史 Rank 90%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 58,109 股

📆 10-16 Forward Structure
存量OI: C 76.6k / P 62.1k，今日变化ΔOI: C +0.6k / P -0.3k，平值价格ATM: C $5.30 / P $4.87 ｜ ATM IV 46.9%，净 delta 敞口 19k shares
Top ΔOI: C 142 +652 ｜ P 130 -610 ｜ P 131 +156
仓位参考: Max Pain 130 ｜ Call Wall 150（+10.0%）（OI 13.8k） ｜ Put Wall 125（-8.4%，弱）（OI 5.4k）
量化解读： 存量 Call 重｜ATM IV 46.9%｜历史 Rank 90%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 18,655 股

10-23（Activity LOW）仓位参考: Max Pain 134 ｜ Call Wall 134（-1.8%，弱）（OI 1.0k） ｜ Put Wall 125（-8.4%，弱）（OI 1.9k）

10-30（MEDIUM △）Top ΔOI: 140P +56 ｜ 150C +56
10-30（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 140（+2.6%，弱）（OI 0.6k） ｜ Put Wall 123（-9.8%，弱）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/NOW_morning.json