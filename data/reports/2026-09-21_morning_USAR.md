# 期权晨报 2026-09-21（快照 10:20 ET）

📊 市场环境

SPY $773.06 ｜ QQQ $741.47
VIX 14.85 ↑0.3%（5D -13.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-25 16C ΔOI +635（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 15.37 → 今开 16.68（+8.5%） | 较昨收变动（含盘初走势） ｜ 今日高 16.90 ｜ 低 16.28

Options: P/C成交量 0.21 | OI比 0.49 | ATM IV 91.1% | Skew -8.3pp | Term 0.80 | ExpMove ±7.8%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±7.8% ｜ 10-02（11D）±10.4% ｜ 10-09（18D）±14.3% ｜ 10-16（25D）±15.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,785,262 | GEX Change vs 上次快照 3,668,623 | Flip: Primary Flip: 15.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 234 / LOW 53 / INVALID 149
结构观察区: Primary Flip 15.29（全链重定价，覆盖 100%）
Put Wall 15（现价高于该位 9.8%）
最近结构参考: Flip 15（现价高于该位 7.8%）
量化视角： 正 Gamma（379万，无历史分位）｜正 Gamma 增强（+367万）｜现价位于 Flip 上方 7.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 21.0C — Vol 5,528 | 最新价 $0.19 | OI 32→5019 (ΔOI +4987张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4987张（+15584.4% vs前日OI），连续性待观察（方向未知）
09-25 16.5C — Vol 1,111 | 最新价 $0.23 | OI 1393→2028 (ΔOI +635张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增635张（+45.6% vs前日OI），连续性待观察（方向未知）
10-16 15.0P — Vol 701 | 最新价 $0.99 | OI 4655→5290 (ΔOI +635张) | ΔOI/Volume 90.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增635张（+13.6% vs前日OI），连续性待观察（方向未知）
09-25 14.5P — Vol 485 | 最新价 $0.23 | OI 975→1419 (ΔOI +444张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增444张（+45.5% vs前日OI），连续性待观察（方向未知）
09-25 15.0P — Vol 593 | 最新价 $0.40 | OI 1179→1608 (ΔOI +429张) | ΔOI/Volume 72.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增429张（+36.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,130 张（Put 1,508 / Call 5,622），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +2.0k / P +1.9k ｜ Activity HIGH ｜ 4D
10-02  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 11D
10-09  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
10-16  C -1.7k / P +0.9k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 20.2k / P 9.8k，今日变化ΔOI: C +2.0k / P +1.9k，平值价格ATM: C $0.61 / P $0.67 ｜ ATM IV 91.1%，净 delta 敞口 65k shares
Top ΔOI: C 16 +635 ｜ P 15 +429
仓位参考: Max Pain 16 ｜ Call Wall 18（+9.2%，弱）（OI 2.3k） ｜ Put Wall 16.5（+0.1%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 91.1%｜历史 Rank 14%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 64,966 股

10-02（MEDIUM △）Top ΔOI: 17P +192 ｜ 15C +145
10-02（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 17（+3.2%）（OI 1.4k）

10-09（MEDIUM △）Top ΔOI: 15C +107 ｜ 15P +34
10-09（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 16（-2.9%）（OI 1.2k）

📆 10-16 Forward Structure
存量OI: C 29.1k / P 12.7k，今日变化ΔOI: C -1.7k / P +0.9k，平值价格ATM: C $1.27 / P $1.26 ｜ ATM IV 75.7%，净 delta 敞口 -17k shares
Top ΔOI: P 15 +635 ｜ C 18 +194
仓位参考: Max Pain 17 ｜ Call Wall 18（+9.2%，弱）（OI 4.5k） ｜ Put Wall 15（-9.0%）（OI 5.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 75.7%｜历史 Rank 14%（近端代理）｜IV/RV 1.55×（近似）｜净 delta 敞口 负 17,438 股

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 91.1% vs 10-02 81.2%（差 +9.9pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/USAR_morning.json