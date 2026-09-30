# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $763.55 ｜ QQQ $739.77
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 192C ΔOI +2,367（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 186.97 → 今开 187.93（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 190.68 ｜ 低 187.00

Options: P/C成交量 0.33 | OI比 0.62 | ATM IV 49.9% | Skew 2.1pp | Term 0.91 | ExpMove ±3.1%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 2.1pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±3.1% ｜ 10-09（9D）±5.6% ｜ 10-16（16D）±7.3% ｜ 10-23（23D）±9.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 61,312,191 | GEX Change vs 上次快照 26,621,809 | Flip: Primary Flip: 181.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 611 / LOW 84 / INVALID 141
结构观察区: Primary Flip 181.20（全链重定价，覆盖 100%）
Call Wall 200（现价低于该位 5.0%）
最近结构参考: Flip 181（现价高于该位 4.9%）
量化视角： 正 Gamma（6131万，无历史分位）｜正 Gamma 增强（+2662万）｜现价位于 Flip 上方 4.88%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 192.5C — Vol 4,952 | 最新价 $1.30 | OI 3463→5830 (ΔOI +2367张) | ΔOI/Volume 47.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2367张（+68.3% vs前日OI），连续性待观察（方向未知）
10-09 165.0P — Vol 2,599 | 最新价 $0.47 | OI 1240→3151 (ΔOI +1911张) | ΔOI/Volume 73.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1911张（+154.1% vs前日OI），连续性待观察（方向未知）
10-02 185.0P — Vol 8,811 | 最新价 $2.39 | OI 5496→6882 (ΔOI +1386张) | ΔOI/Volume 15.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1386张（+25.2% vs前日OI），连续性待观察（方向未知）
10-30 230.0C — Vol 1,303 | 最新价 $0.80 | OI 399→1585 (ΔOI +1186张) | ΔOI/Volume 91.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1186张（+297.2% vs前日OI），连续性待观察（方向未知）
10-02 190.0C — Vol 8,434 | 最新价 $2.06 | OI 5231→6123 (ΔOI +892张) | ΔOI/Volume 10.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增892张（+17.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,742 张（Put 3,297 / Call 4,445），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +3.7k / P +2.6k ｜ Activity HIGH ｜ 2D
10-09  C +2.1k / P +2.6k ｜ Activity HIGH ｜ 9D
10-16  C -1.4k / P +77 ｜ Activity HIGH ｜ 16D
10-23  C +0.7k / P +1.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 132.3k / P 81.8k，今日变化ΔOI: C +3.7k / P +2.6k，平值价格ATM: C $2.86 / P $3.08 ｜ ATM IV 49.9%，净 delta 敞口 46k shares
Top ΔOI: C 192 +2,367 ｜ P 185 +1,386 ｜ P 177 -1,308
仓位参考: Max Pain 185 ｜ Call Wall 200（+5.2%）（OI 25.9k） ｜ Put Wall 177.5（-6.6%，弱）（OI 7.4k）
量化解读： 存量 Call 重｜ATM IV 49.9%｜历史 Rank 40%（近端代理）｜IV/RV 1.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,240 股

📆 10-09 Forward Structure
存量OI: C 30.8k / P 42.8k，今日变化ΔOI: C +2.1k / P +2.6k，平值价格ATM: C $5.40 / P $5.25 ｜ ATM IV 44.5%，净 delta 敞口 54k shares
Top ΔOI: P 165 +1,911 ｜ C 200 +885
仓位参考: Max Pain 185 ｜ Call Wall 200（+5.2%，弱）（OI 4.6k） ｜ Put Wall 190（-0.0%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 44.5%｜历史 Rank 40%（近端代理）｜IV/RV 1.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,659 股

📆 10-16 Forward Structure
存量OI: C 151.3k / P 169.1k，今日变化ΔOI: C -1.4k / P +77，平值价格ATM: C $7.15 / P $6.80 ｜ ATM IV 44.5%，净 delta 敞口 690 shares
Top ΔOI: C 210 -1,168 ｜ C 200 +595
仓位参考: Max Pain 165 ｜ Call Wall 200（+5.2%，弱）（OI 15.0k） ｜ Put Wall 175（-7.9%，弱）（OI 7.8k）
量化解读： 存量两侧均衡｜ATM IV 44.5%｜历史 Rank 40%（近端代理）｜IV/RV 1.70×（近似）｜净 delta 敞口 正 690 股

10-23（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 180（-5.3%）（OI 4.6k） ｜ Put Wall 175（-7.9%，弱）（OI 1.6k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 49.9% vs 10-09 44.5%（差 +5.4pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/PLTR_morning.json