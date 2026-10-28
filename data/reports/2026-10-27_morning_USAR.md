# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $nan
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-30 10C ΔOI +1,864（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 8.91 → 今开 9.12（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 9.69 ｜ 低 9.02

Options: P/C成交量 0.47 | OI比 0.40 | ATM IV 95.6% | Skew 10.4pp | Term 0.91 | ExpMove ±7.2%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 10.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±7.2% ｜ 11-06（10D）±12.8% ｜ 11-13（17D）±14.1% ｜ 11-20（24D）±21.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,321 | GEX Change vs 上次快照 2,895,011 | Flip: Primary Flip: 9.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 219 / LOW 76 / INVALID 125
结构观察区: Primary Flip 9.62（全链重定价，覆盖 100%）
Put Wall 9（弱结构｜现价高于该位 6.9%） | Call Wall 10（弱结构｜现价低于该位 3.7%）
最近结构参考: Flip 10（现价高于该位 0.0%）
量化视角： 正 Gamma（0万，无历史分位）｜由负转正（+290万）｜现价位于 Flip 上方 0.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 9（Put Wall，弱结构）；上方 10（MaxPain，仅结算参考） / 10（Call Wall，弱结构）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 10.0C — Vol 2,779 | 最新价 $0.04 | OI 1162→3026 (ΔOI +1864张) | ΔOI/Volume 67.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1864张（+160.4% vs前日OI），连续性待观察（方向未知）
11-20 9.0P — Vol 1,562 | 最新价 $0.89 | OI 1747→3057 (ΔOI +1310张) | ΔOI/Volume 83.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1310张（+75.0% vs前日OI），连续性待观察（方向未知）
11-20 9.0C — Vol 854 | 最新价 $0.89 | OI 501→1236 (ΔOI +735张) | ΔOI/Volume 86.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增735张（+146.7% vs前日OI），连续性待观察（方向未知）
10-30 9.5C — Vol 1,235 | 最新价 $0.13 | OI 370→1088 (ΔOI +718张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增718张（+194.1% vs前日OI），连续性待观察（方向未知）
11-20 9.5C — Vol 871 | 最新价 $0.66 | OI 703→1404 (ΔOI +701张) | ΔOI/Volume 80.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增701张（+99.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,328 张（Put 1,310 / Call 4,018），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +3.6k / P +96 ｜ Activity MEDIUM △ ｜ 3D
11-06  C +0.8k / P -45 ｜ Activity MEDIUM △ ｜ 10D
11-13  C +0.8k / P -27 ｜ Activity HIGH ｜ 17D
11-20  C +2.2k / P -0.4k ｜ Activity MEDIUM △ ｜ 24D

📆 10-30 Forward Structure
存量OI: C 23.6k / P 9.4k，今日变化ΔOI: C +3.6k / P +96，平值价格ATM: C $0.41 / P $0.28 ｜ ATM IV 95.6%，净 delta 敞口 176k shares
Top ΔOI: C 10 +1,864 ｜ C 9 +718 ｜ C 10 +514
仓位参考: Max Pain 10 ｜ Call Wall 10（+3.9%，弱）（OI 3.0k） ｜ Put Wall 9（-6.5%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 95.6%｜历史 Rank 27%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 175,795 股

11-06（MEDIUM △）Top ΔOI: 10C +310 ｜ 10C +188
11-06（MEDIUM △）仓位参考: Max Pain 11 ｜ Call Wall 10（+3.9%，弱）（OI 0.6k） ｜ Put Wall 9（-6.5%）（OI 1.6k）

📆 11-13 Forward Structure
存量OI: C 3.9k / P 2.7k，今日变化ΔOI: C +0.8k / P -27，平值价格ATM: C $0.60 / P $0.76 ｜ ATM IV 94.1%，净 delta 敞口 72k shares
Top ΔOI: C 9 +585 ｜ P 9 +251 ｜ P 15 -209
仓位参考: Max Pain 10 ｜ Call Wall 9（-6.5%，弱）（OI 0.6k） ｜ Put Wall 9（-6.5%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 94.1%｜历史 Rank 27%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 71,934 股

11-20（MEDIUM △）Top ΔOI: 10P -1,553 ｜ 9P +1,310
11-20（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 9.5（-1.3%，弱）（OI 1.4k） ｜ Put Wall 10（+3.9%，弱）（OI 6.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/USAR_morning.json