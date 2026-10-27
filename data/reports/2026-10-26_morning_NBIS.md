# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 158.74 → 今开 158.90（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 162.99 ｜ 低 155.86

Options: P/C成交量 0.51 | OI比 0.61 | ATM IV 93.6% | Skew 3.4pp | Term 1.03 | ExpMove ±10.5%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 1.03）｜保护溢价中性（Skew 3.4pp）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±10.5% ｜ 11-06（11D）±14.8% ｜ 11-13（18D）±20.3% ｜ 11-20（25D）±22.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,367,256 | GEX Change vs 上次快照 -1,107,926 | Flip: Primary Flip: 173.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 604 / LOW 23 / INVALID 137
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 173.86（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 5.9%）
最近结构参考: Put Wall 150（现价高于该位 5.9%）
量化视角： 负 Gamma（837万，无历史分位）｜负 Gamma 加深（111万）｜现价位于 Flip 下方 8.61%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 185（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 174（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 225.0P — Vol 2,405 | 最新价 $65.04 | OI 325→2695 (ΔOI +2370张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2370张（+729.2% vs前日OI），连续性待观察（方向未知）
10-30 235.0C — Vol 2,186 | 最新价 $0.14 | OI 1204→3315 (ΔOI +2111张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2111张（+175.3% vs前日OI），连续性待观察（方向未知）
11-20 75.0P — Vol 2,725 | 最新价 $0.32 | OI 3748→5813 (ΔOI +2065张) | ΔOI/Volume 75.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2065张（+55.1% vs前日OI），连续性待观察（方向未知）
10-30 170.0C — Vol 3,140 | 最新价 $4.09 | OI 1716→3423 (ΔOI +1707张) | ΔOI/Volume 54.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1707张（+99.5% vs前日OI），连续性待观察（方向未知）
11-20 80.0P — Vol 1,784 | 最新价 $0.40 | OI 357→1862 (ΔOI +1505张) | ΔOI/Volume 84.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1505张（+421.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,758 张（Put 5,940 / Call 3,818），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +11.5k / P +3.4k ｜ Activity HIGH ｜ 4D
11-06  C +1.7k / P +6.0k ｜ Activity HIGH ｜ 11D
11-13  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 18D
11-20  C +1.0k / P +3.5k ｜ Activity HIGH ｜ 25D

📆 10-30 Forward Structure
存量OI: C 78.1k / P 47.4k，今日变化ΔOI: C +11.5k / P +3.4k，平值价格ATM: C $7.85 / P $8.80 ｜ ATM IV 93.6%，净 delta 敞口 404k shares
Top ΔOI: P 225 -1,869 ｜ C 170 +1,707
仓位参考: Max Pain 185 ｜ Call Wall 170（+7.0%，弱）（OI 3.4k） ｜ Put Wall 150（-5.6%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 93.6%｜历史 Rank 34%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 404,222 股

📆 11-06 Forward Structure
存量OI: C 36.2k / P 23.5k，今日变化ΔOI: C +1.7k / P +6.0k，平值价格ATM: C $11.18 / P $12.25 ｜ ATM IV 94.2%，净 delta 敞口 -452k shares
Top ΔOI: P 225 +2,370 ｜ P 230 +1,313 ｜ P 220 +1,277
仓位参考: Max Pain 215 ｜ Put Wall 170（+7.0%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 94.2%｜历史 Rank 34%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 452,085 股

11-13（MEDIUM △）Top ΔOI: 175C +112 ｜ 150P +107
11-13（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 170（+7.0%，弱）（OI 0.6k） ｜ Put Wall 165（+3.8%，弱）（OI 1.4k）

📆 11-20 Forward Structure
存量OI: C 90.6k / P 104.1k，今日变化ΔOI: C +1.0k / P +3.5k，平值价格ATM: C $17.05 / P $17.86 ｜ ATM IV 99.5%，净 delta 敞口 29k shares
Top ΔOI: P 75 +2,065 ｜ P 80 +1,505 ｜ C 200 +623
仓位参考: Max Pain 195 ｜ Call Wall 170（+7.0%，弱）（OI 3.0k） ｜ Put Wall 150（-5.6%，弱）（OI 8.1k）
量化解读： 存量两侧均衡｜ATM IV 99.5%｜历史 Rank 34%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 29,049 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/NBIS_morning.json