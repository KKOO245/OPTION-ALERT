# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 14C ΔOI +1,234（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 13.65 → 今开 13.81（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 14.01 ｜ 低 13.77

Options: P/C成交量 0.09 | OI比 0.42 | ATM IV 71.4% | Skew -0.2pp | Term 1.01 | ExpMove ±5.2%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.09×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±5.2% ｜ 10-16（10D）±9.1% ｜ 10-23（17D）±11.6% ｜ 10-30（24D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 192,566 | GEX Change vs 上次快照 2,609,113 | Flip: Primary Flip: 13.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 210 / LOW 65 / INVALID 115
结构观察区: Primary Flip 13.87（全链重定价，覆盖 100%）
Put Wall 15（弱结构｜现价低于该位 7.2%）
最近结构参考: Flip 14（现价高于该位 0.3%）
量化视角： 正 Gamma（19万，无历史分位）｜由负转正（+261万）｜现价位于 Flip 上方 0.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 14.5C — Vol 2,176 | 最新价 $0.11 | OI 1602→2836 (ΔOI +1234张) | ΔOI/Volume 56.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1234张（+77.0% vs前日OI），连续性待观察（方向未知）
10-09 14.0C — Vol 2,192 | 最新价 $0.25 | OI 1092→2020 (ΔOI +928张) | ΔOI/Volume 42.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增928张（+85.0% vs前日OI），连续性待观察（方向未知）
11-06 17.0P — Vol 730 | 最新价 $3.63 | OI 46→774 (ΔOI +728张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增728张（+1582.6% vs前日OI），连续性待观察（方向未知）
10-30 16.5C — Vol 779 | 最新价 $0.18 | OI 167→886 (ΔOI +719张) | ΔOI/Volume 92.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增719张（+430.5% vs前日OI），连续性待观察（方向未知）
10-09 13.0P — Vol 762 | 最新价 $0.14 | OI 635→1335 (ΔOI +700张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增700张（+110.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,309 张（Put 1,428 / Call 2,881），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +3.8k / P +0.2k ｜ Activity HIGH ｜ 3D
10-16  C +1.1k / P -0.6k ｜ Activity MEDIUM △ ｜ 10D
10-23  C +0.6k / P +0.5k ｜ Activity MEDIUM △ ｜ 17D
10-30  C +1.1k / P +0.7k ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 17.8k / P 7.5k，今日变化ΔOI: C +3.8k / P +0.2k，平值价格ATM: C $0.35 / P $0.38 ｜ ATM IV 71.4%，净 delta 敞口 189k shares
Top ΔOI: C 14 +1,234 ｜ C 14 +928 ｜ P 13 +700
仓位参考: Max Pain 14 ｜ Call Wall 14.5（+4.2%，弱）（OI 2.8k） ｜ Put Wall 13（-6.6%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 71.4%｜历史 Rank 5%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 189,077 股

10-16（MEDIUM △）Top ΔOI: 15C +497 ｜ 15P -338
10-16（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15（+7.8%）（OI 5.6k）

10-23（MEDIUM △）Top ΔOI: 15P +567 ｜ 16P -205
10-23（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（+0.6%，弱）（OI 0.5k）

📆 10-30 Forward Structure
存量OI: C 5.6k / P 7.2k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $0.89 / P $0.98 ｜ ATM IV 66.6%，净 delta 敞口 -9k shares
Top ΔOI: P 16 +440 ｜ P 17 -192
仓位参考: Max Pain 16 ｜ Call Wall 15（+7.8%，弱）（OI 0.3k） ｜ Put Wall 14（+0.6%）（OI 2.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.6%｜历史 Rank 5%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 负 9,255 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/USAR_morning.json