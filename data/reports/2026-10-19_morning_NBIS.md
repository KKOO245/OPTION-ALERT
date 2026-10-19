# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.65 ｜ QQQ $721.19
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **事件差分**: 10-23 ATM IV 104.9% vs 10-30 93.4%（差 +11.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 170P ΔOI +707（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 165.47 → 今开 176.60（+6.7%） | 较昨收变动（含盘初走势） ｜ 今日高 176.69 ｜ 低 166.59

Options: P/C成交量 0.54 | OI比 0.72 | ATM IV 104.9% | Skew 9.1pp | Term 0.88 | ExpMove ±8.9%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 9.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±8.9% ｜ 10-30（11D）±13.9% ｜ 11-06（18D）±7.8% ｜ 11-13（25D）±19.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,308,458 | GEX Change vs 上次快照 906,976 | Flip: Primary Flip: 180.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 503 / LOW 48 / INVALID 189
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 180.53（全链重定价，覆盖 100%）
最近结构参考: Flip 181（现价低于该位 7.6%）
量化视角： 负 Gamma（831万，无历史分位）｜负 Gamma 缓解（+91万）｜现价位于 Flip 下方 7.55%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 240.0C — Vol 10,409 | 最新价 $1.08 | OI 4372→7776 (ΔOI +3404张) | ΔOI/Volume 32.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3404张（+77.9% vs前日OI），连续性待观察（方向未知）
11-20 150.0P — Vol 4,602 | 最新价 $11.99 | OI 5688→8794 (ΔOI +3106张) | ΔOI/Volume 67.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3106张（+54.6% vs前日OI），连续性待观察（方向未知）
10-23 180.0C — Vol 8,685 | 最新价 $3.28 | OI 932→3901 (ΔOI +2969张) | ΔOI/Volume 34.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2969张（+318.6% vs前日OI），连续性待观察（方向未知）
10-23 110.0P — Vol 2,744 | 最新价 $0.33 | OI 6→2647 (ΔOI +2641张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2641张（+44016.7% vs前日OI），连续性待观察（方向未知）
11-20 145.0P — Vol 2,941 | 最新价 $10.10 | OI 2501→4793 (ΔOI +2292张) | ΔOI/Volume 77.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2292张（+91.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,412 张（Put 8,039 / Call 6,373），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +23.1k / P +19.3k ｜ Activity HIGH ｜ 4D
10-30  C +6.4k / P +5.2k ｜ Activity HIGH ｜ 11D
11-06  C +6.1k / P +1.7k ｜ Activity HIGH ｜ 18D
11-13  C +1.3k / P +0.5k ｜ Activity MEDIUM △ ｜ 25D

📆 10-23 Forward Structure
存量OI: C 85.6k / P 61.5k，今日变化ΔOI: C +23.1k / P +19.3k，平值价格ATM: C $7.33 / P $7.60 ｜ ATM IV 104.9%，净 delta 敞口 47k shares
Top ΔOI: C 180 +2,969
仓位参考: Max Pain 190 ｜ Call Wall 180（+7.9%，弱）（OI 3.9k） ｜ Put Wall 165（-1.1%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 104.9%｜历史 Rank 54%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,736 股

📆 10-30 Forward Structure
存量OI: C 39.5k / P 27.8k，今日变化ΔOI: C +6.4k / P +5.2k，平值价格ATM: C $12.25 / P $10.89 ｜ ATM IV 93.4%，净 delta 敞口 9k shares
Top ΔOI: P 120 +955
仓位参考: Max Pain 205 ｜ Put Wall 180（+7.9%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 93.4%｜历史 Rank 54%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 正 9,473 股

📆 11-06 Forward Structure
存量OI: C 28.1k / P 16.1k，今日变化ΔOI: C +6.1k / P +1.7k，平值价格ATM: C $0.00 / P $13.00 ｜ ATM IV 91.7%，净 delta 敞口 -5k shares
Top ΔOI: C 240 +3,404 ｜ C 230 +1,000 ｜ P 170 +707
仓位参考: Max Pain 210 ｜ Put Wall 170（+1.9%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 91.7%｜历史 Rank 54%（近端代理）｜IV/RV 1.12×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 4,720 股

11-13（MEDIUM △）Top ΔOI: 200C +251 ｜ 210C +211
11-13（MEDIUM △）仓位参考: Max Pain 210 ｜ Call Wall 180（+7.9%，弱）（OI 0.4k） ｜ Put Wall 165（-1.1%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 104.9% vs 10-30 93.4%（差 +11.6pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/NBIS_morning.json