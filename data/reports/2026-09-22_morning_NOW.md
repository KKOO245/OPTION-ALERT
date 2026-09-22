# 期权晨报 2026-09-22（快照 10:20 ET）

📊 市场环境

SPY $773.25 ｜ QQQ $747.46
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 140C ΔOI +1,098（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 137.68 → 今开 141.83（+3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 142.10 ｜ 低 135.74

Options: P/C成交量 0.17 | OI比 0.63 | ATM IV 61.2% | Skew -1.8pp | Term 0.92 | ExpMove ±4.8%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±4.8% ｜ 10-02（10D）±7.2% ｜ 10-09（17D）±9.9% ｜ 10-16（24D）±10.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,313,688 | GEX Change vs 上次快照 -344,067 | Flip: Primary Flip: 130.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 601 / LOW 29 / INVALID 96
结构观察区: Primary Flip 130.72（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 9.1%）
最近结构参考: Flip 131（现价高于该位 4.3%）
量化视角： 正 Gamma（931万，无历史分位）｜正 Gamma 减弱（34万）｜现价位于 Flip 上方 4.33%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 122.0P — Vol 1,406 | 最新价 $2.91 | OI 49→1450 (ΔOI +1401张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1401张（+2859.2% vs前日OI），连续性待观察（方向未知）
10-23 117.0P — Vol 1,401 | 最新价 $1.88 | OI 218→1501 (ΔOI +1283张) | ΔOI/Volume 91.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1283张（+588.5% vs前日OI），连续性待观察（方向未知）
09-25 140.0C — Vol 3,312 | 最新价 $2.50 | OI 1422→2520 (ΔOI +1098张) | ΔOI/Volume 33.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1098张（+77.2% vs前日OI），连续性待观察（方向未知）
09-25 150.0C — Vol 2,253 | 最新价 $0.44 | OI 5091→6073 (ΔOI +982张) | ΔOI/Volume 43.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增982张（+19.3% vs前日OI），连续性待观察（方向未知）
09-25 145.0C — Vol 2,318 | 最新价 $1.05 | OI 3451→4316 (ΔOI +865张) | ΔOI/Volume 37.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增865张（+25.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,629 张（Put 2,684 / Call 2,945），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +5.4k / P +2.1k ｜ Activity HIGH ｜ 3D
10-02  C +2.1k / P +1.0k ｜ Activity MEDIUM △ ｜ 10D
10-09  C +0.8k / P +0.9k ｜ Activity MEDIUM △ ｜ 17D
10-16  C +2.4k / P +2.3k ｜ Activity MEDIUM △ ｜ 24D

📆 09-25 Forward Structure
存量OI: C 30.0k / P 18.9k，今日变化ΔOI: C +5.4k / P +2.1k，平值价格ATM: C $3.80 / P $2.78 ｜ ATM IV 61.2%，净 delta 敞口 100k shares
Top ΔOI: C 140 +1,098 ｜ C 150 +982 ｜ C 145 +865
仓位参考: Max Pain 136 ｜ Call Wall 150（+10.0%，弱）（OI 6.1k） ｜ Put Wall 130（-4.7%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 61.2%｜历史 Rank 56%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 99,568 股

10-02（MEDIUM △）Top ΔOI: 150C +451 ｜ 145C +372
10-02（MEDIUM △）仓位参考: Max Pain 132 ｜ Call Wall 150（+10.0%）（OI 2.3k） ｜ Put Wall 130（-4.7%）（OI 1.1k）

10-09（MEDIUM △）Top ΔOI: 128P +263 ｜ 126P +262
10-09（MEDIUM △）仓位参考: Max Pain 136 ｜ Call Wall 150（+10.0%）（OI 1.0k） ｜ Put Wall 140（+2.7%，弱）（OI 0.5k）

10-16（MEDIUM △）Top ΔOI: 140C +773 ｜ 130P +754
10-16（MEDIUM △）仓位参考: Max Pain 125 ｜ Call Wall 150（+10.0%）（OI 11.2k） ｜ Put Wall 130（-4.7%，弱）（OI 4.7k）

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 61.2% vs 10-02 55.5%（差 +5.7pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/NOW_morning.json