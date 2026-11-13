# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.56
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 108.9% vs 11-27 95.8%（差 +13.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-27 8C ΔOI +1,411（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 8.07 → 今开 8.09（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 8.36 ｜ 低 7.93

Options: P/C成交量 0.14 | OI比 0.29 | ATM IV 189.4% | Skew -7.7pp | Term 0.54 | ExpMove ±12.5%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.29）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.29×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±12.5% ｜ 11-27（14D）±16.0% ｜ 12-04（21D）±20.2% ｜ 12-11（28D）±21.7%
   ⇒ IV–VIX Spread: +169.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,338,776 | GEX Change vs 上次快照 1,683,338 | Flip: Primary Flip: 7.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 189 / LOW 94 / INVALID 141
结构观察区: Primary Flip 7.31（全链重定价，覆盖 97%）
Put Wall 8（弱结构｜现价高于该位 0.9%）
最近结构参考: Put Wall 8（现价高于该位 0.9%）
量化视角： 正 Gamma（434万，无历史分位）｜正 Gamma 增强（+168万）｜现价位于 Flip 上方 10.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 8（Put Wall，弱结构）；上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 7（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 8.5C — Vol 6,008 | 最新价 $0.09 | OI 1277→4963 (ΔOI +3686张) | ΔOI/Volume 61.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3686张（+288.6% vs前日OI），连续性待观察（方向未知）
11-13 8.0P — Vol 5,175 | 最新价 $0.18 | OI 1332→3465 (ΔOI +2133张) | ΔOI/Volume 41.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2133张（+160.1% vs前日OI），连续性待观察（方向未知）
11-20 8.5C — Vol 2,701 | 最新价 $0.31 | OI 937→2528 (ΔOI +1591张) | ΔOI/Volume 58.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1591张（+169.8% vs前日OI），连续性待观察（方向未知）
11-27 8.0C — Vol 2,158 | 最新价 $0.70 | OI 1277→2688 (ΔOI +1411张) | ΔOI/Volume 65.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1411张（+110.5% vs前日OI），连续性待观察（方向未知）
11-20 10.0C — Vol 4,096 | 最新价 $0.07 | OI 5946→6803 (ΔOI +857张) | ΔOI/Volume 20.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增857张（+14.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,678 张（Put 2,133 / Call 7,545），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 32.0k / P 9.3k，今日成交量: C 0.5k / P 76，平值价格ATM: C $0.22 / P $0.12 ｜ ATM IV 189.4%，预期波动 ±4.1%，Max Pain 8
Top ΔOI: C 8 +3,686 ｜ P 8 +2,133 ｜ P 7 +612

📆 Forward Expiration Structure

11-20  C +2.9k / P +0.3k ｜ Activity MEDIUM △ ｜ 7D
11-27  C +1.5k / P +38 ｜ Activity MEDIUM △ ｜ 14D
12-04  C +30 / P +41 ｜ Activity LOW ｜ 21D
12-11  C +95 / P +84 ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 50.9k / P 32.9k，今日变化ΔOI: C +2.9k / P +0.3k，平值价格ATM: C $0.59 / P $0.42 ｜ ATM IV 108.9%，净 delta 敞口 60k shares
Top ΔOI: C 8 +1,591 ｜ P 7 +510
仓位参考: Max Pain 10 ｜ Call Wall 8.5（+5.3%，弱）（OI 2.5k） ｜ Put Wall 8（-0.9%，弱）（OI 6.9k）
量化解读： 存量 Call 重｜ATM IV 108.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,718 股

11-27（MEDIUM △）Top ΔOI: 8C +1,411
11-27（MEDIUM △）仓位参考: Max Pain 8 ｜ Call Wall 8（-0.9%，弱）（OI 2.7k） ｜ Put Wall 8（-0.9%，弱）（OI 0.5k）

12-04（Activity LOW）仓位参考: Max Pain 10 ｜ Call Wall 8（-0.9%，弱）（OI 0.1k） ｜ Put Wall 8.5（+5.3%）（OI 0.3k）

12-11（MEDIUM △）Top ΔOI: 8C +55 ｜ 8P +44
12-11（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 7.5（-7.1%，弱）（OI 97） ｜ Put Wall 8（-0.9%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 108.9% vs 11-27 95.8%（差 +13.1pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/USAR_morning.json