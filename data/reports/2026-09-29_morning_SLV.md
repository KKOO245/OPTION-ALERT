# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.73 ｜ QQQ $737.93
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-30 56C ΔOI +2,010（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-07 57P ΔOI -2,676 占该期限总 OI 34.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 54.95 → 今开 55.03（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 55.33 ｜ 低 54.90

Options: P/C成交量 0.28 | OI比 0.40 | ATM IV 35.8% | Skew 0.4pp | Term 0.97 | ExpMove ±1.7%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 0.97）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（1D）±1.7% ｜ 10-02（3D）±2.9% ｜ 10-05（6D）±3.4% ｜ 10-07（8D）±4.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,828,227 | GEX Change vs 上次快照 8,325,257 | Flip: Primary Flip: 55.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 753 / LOW 192 / INVALID 399
结构观察区: Primary Flip 55.03（全链重定价，覆盖 95%）
Put Wall 50（弱结构｜现价高于该位 10.2%） | Call Wall 60（弱结构｜现价低于该位 8.2%）
最近结构参考: Flip 55（现价高于该位 0.1%）
量化视角： 正 Gamma（283万，无历史分位）｜由负转正（+833万）｜现价位于 Flip 上方 0.12%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构） / 55（MaxPain，仅结算参考）；上方 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 57.0C — Vol 6,397 | 最新价 $1.02 | OI 3788→6681 (ΔOI +2893张) | ΔOI/Volume 45.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2893张（+76.4% vs前日OI），连续性待观察（方向未知）
09-30 58.5C — Vol 4,786 | 最新价 $0.04 | OI 2625→5493 (ΔOI +2868张) | ΔOI/Volume 59.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2868张（+109.3% vs前日OI），连续性待观察（方向未知）
09-30 56.0C — Vol 3,831 | 最新价 $0.29 | OI 1016→3026 (ΔOI +2010张) | ΔOI/Volume 52.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2010张（+197.8% vs前日OI），连续性待观察（方向未知）
09-30 54.5P — Vol 2,812 | 最新价 $0.43 | OI 522→2101 (ΔOI +1579张) | ΔOI/Volume 56.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1579张（+302.5% vs前日OI），连续性待观察（方向未知）
09-30 57.0C — Vol 2,251 | 最新价 $0.12 | OI 1041→2547 (ΔOI +1506张) | ΔOI/Volume 66.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1506张（+144.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,856 张（Put 1,579 / Call 9,277），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-30  C +12.2k / P -3.3k ｜ Activity HIGH ｜ 1D
10-02  C +5.6k / P +4.3k ｜ Activity MEDIUM △ ｜ 3D
10-05  C +2.0k / P +1.8k ｜ Activity HIGH ｜ 6D
10-07  C +1.9k / P -1.9k ｜ Activity HIGH ｜ 8D

📆 09-30 Forward Structure
存量OI: C 312.3k / P 123.6k，今日变化ΔOI: C +12.2k / P -3.3k，平值价格ATM: C $0.53 / P $0.42 ｜ ATM IV 35.8%，净 delta 敞口 1.1M shares
Top ΔOI: C 58 +2,868 ｜ C 56 +2,010 ｜ P 65 -1,980
仓位参考: Max Pain 55 ｜ Call Wall 60（+8.9%，弱）（OI 6.5k） ｜ Put Wall 53（-3.8%）（OI 13.8k）
量化解读： 存量 Call 重｜ATM IV 35.8%｜历史 Rank 58%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,127,568 股

10-02（MEDIUM △）Top ΔOI: 54P +1,245 ｜ 55C +1,201
10-02（MEDIUM △）仓位参考: Max Pain 58 ｜ Call Wall 60（+8.9%，弱）（OI 11.2k） ｜ Put Wall 50（-9.2%）（OI 7.5k）

📆 10-05 Forward Structure
存量OI: C 4.7k / P 4.3k，今日变化ΔOI: C +2.0k / P +1.8k，平值价格ATM: C $1.00 / P $0.86 ｜ ATM IV 31.4%，净 delta 敞口 -13k shares
Top ΔOI: C 58 +370 ｜ C 57 +306 ｜ P 55 +275
仓位参考: Max Pain 58 ｜ Call Wall 58（+5.3%，弱）（OI 0.4k） ｜ Put Wall 59.5（+8.0%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 31.4%｜历史 Rank 58%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 负 12,605 股

📆 10-07 Forward Structure
存量OI: C 4.1k / P 3.8k，今日变化ΔOI: C +1.9k / P -1.9k，平值价格ATM: C $1.18 / P $1.01 ｜ ATM IV 32.6%，净 delta 敞口 214k shares
Top ΔOI: P 57 -2,676 ｜ C 59 +665 ｜ C 59 +619
仓位参考: Max Pain 57 ｜ Call Wall 59（+7.1%，弱）（OI 0.7k） ｜ Put Wall 57（+3.5%）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 32.6%｜历史 Rank 58%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 213,503 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SLV_morning.json