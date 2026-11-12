# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 465C ΔOI +82（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 450.04 → 今开 446.00（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 450.99 ｜ 低 443.24

Options: P/C成交量 2.27 | OI比 0.92 | ATM IV 42.1% | Skew -12.8pp | Term 0.81 | ExpMove ±3.4%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -12.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.27×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（2D）±3.4% ｜ 11-20（9D）±5.0% ｜ 11-27（16D）±12.0% ｜ 12-04（23D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,777,969 | GEX Change vs 上次快照 -595,738 | Flip: Primary Flip: 418.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 344 / LOW 188 / INVALID 472
结构观察区: Primary Flip 418.53（全链重定价，覆盖 93%）
Call Wall 480（弱结构｜现价低于该位 7.5%）
最近结构参考: Flip 419（现价高于该位 6.1%）
量化视角： 正 Gamma（278万，无历史分位）｜正 Gamma 减弱（60万）｜现价位于 Flip 上方 6.14%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 440（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 419（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 465.0C — Vol 98 | 最新价 $1.35 | OI 42→124 (ΔOI +82张) | ΔOI/Volume 83.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增82张（+195.2% vs前日OI），连续性待观察（方向未知）
11-13 460.0C — Vol 71 | 最新价 $2.50 | OI 39→86 (ΔOI +47张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47张（+120.5% vs前日OI），连续性待观察（方向未知）
11-13 430.0P — Vol 53 | 最新价 $1.60 | OI 36→74 (ΔOI +38张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38张（+105.6% vs前日OI），连续性待观察（方向未知）
11-20 460.0P — Vol 35 | 最新价 $16.30 | OI 114→146 (ΔOI +32张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32张（+28.1% vs前日OI），连续性待观察（方向未知）
11-27 485.0C — Vol 27 | 最新价 $2.00 | OI 9→30 (ΔOI +21张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21张（+233.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 220 张（Put 70 / Call 150），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.1k / P +57 ｜ Activity HIGH ｜ 2D
11-20  C -98 / P +75 ｜ Activity LOW ｜ 9D
11-27  C +54 / P +2 ｜ Activity MEDIUM △ ｜ 16D
12-04  C +2 / P +13 ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 1.7k / P 1.5k，今日变化ΔOI: C +0.1k / P +57，平值价格ATM: C $10.51 / P $4.50 ｜ ATM IV 42.1%，净 delta 敞口 276 shares
Top ΔOI: C 465 +82 ｜ C 460 +47 ｜ P 430 +38
仓位参考: Max Pain 440 ｜ Call Wall 480（+8.0%，弱）（OI 0.2k） ｜ Put Wall 462.5（+4.1%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 42.1%｜历史 Rank 63%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 276 股

11-20（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 420（-5.5%，弱）（OI 0.8k） ｜ Put Wall 410（-7.7%，弱）（OI 0.5k）

11-27（MEDIUM △）Top ΔOI: 485C +21 ｜ 450C +15
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-3.2%，弱）（OI 64） ｜ Put Wall 410（-7.7%，弱）（OI 42）

12-04（MEDIUM △）Top ΔOI: 400P +11 ｜ 420C +2
12-04（MEDIUM △）仓位参考: Max Pain 450 ｜ Call Wall 475（+6.9%，弱）（OI 82） ｜ Put Wall 405（-8.8%，弱）（OI 25）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 42.1% vs 11-20 34.1%（差 +8.1pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/ISRG_morning.json