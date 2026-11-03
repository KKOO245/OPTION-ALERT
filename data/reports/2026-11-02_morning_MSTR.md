# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　✅ 今日已公布
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-06 ATM IV 93.4% vs 11-13 81.8%（差 +11.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 136C ΔOI +23,773（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 130.51 → 今开 132.12（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 137.30 ｜ 低 130.77

Options: P/C成交量 0.77 | OI比 0.64 | ATM IV 93.4% | Skew 4.9pp | Term 0.79 | ExpMove ±8.1%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 4.9pp）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±8.1% ｜ 11-13（11D）±11.2% ｜ 11-20（18D）±13.8% ｜ 11-27（25D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 53,366,477 | GEX Change vs 上次快照 59,541,049 | Flip: Primary Flip: 119.74（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 514 / LOW 91 / INVALID 235
结构观察区: Primary Flip 119.74（全链重定价，覆盖 100%）
Call Wall 135（现价低于该位 0.8%）
最近结构参考: Call Wall 135（现价低于该位 0.8%）
量化视角： 正 Gamma（5337万，无历史分位）｜由负转正（+5954万）｜现价位于 Flip 上方 11.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（MaxPain，仅结算参考） / 135（Call Wall）。
• Gamma 区域：切换参考 120（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 136.0C — Vol 24,408 | 最新价 $3.85 | OI 81→23854 (ΔOI +23773张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23773张（+29349.4% vs前日OI），连续性待观察（方向未知）
11-06 135.0C — Vol 24,311 | 最新价 $4.10 | OI 220→22086 (ΔOI +21866张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21866张（+9939.1% vs前日OI），连续性待观察（方向未知）
11-06 139.0C — Vol 19,512 | 最新价 $3.00 | OI 86→19218 (ΔOI +19132张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19132张（+22246.5% vs前日OI），连续性待观察（方向未知）
11-06 141.0C — Vol 20,851 | 最新价 $2.22 | OI 552→19333 (ΔOI +18781张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18781张（+3402.4% vs前日OI），连续性待观察（方向未知）
11-06 75.0P — Vol 21,132 | 最新价 $0.11 | OI 2486→20793 (ΔOI +18307张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18307张（+736.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 101,859 张（Put 18,307 / Call 83,552），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +176.6k / P +60.6k ｜ Activity HIGH ｜ 4D
11-13  C -0.2k / P +8.2k ｜ Activity MEDIUM △ ｜ 11D
11-20  C +2.2k / P +3.2k ｜ Activity HIGH ｜ 18D
11-27  C +1.7k / P +3.9k ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 219.6k / P 141.0k，今日变化ΔOI: C +176.6k / P +60.6k，平值价格ATM: C $5.47 / P $5.34 ｜ ATM IV 93.4%，净 delta 敞口 6.9M shares
Top ΔOI: C 136 +23,773 ｜ C 135 +21,866 ｜ C 139 +19,132
仓位参考: Max Pain 135 ｜ Call Wall 136（+1.5%，弱）（OI 23.9k） ｜ Put Wall 125（-6.7%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜ATM IV 93.4%｜历史 Rank 72%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,880,276 股

11-13（MEDIUM △）Top ΔOI: 100P +3,633
11-13（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 144（+7.5%，弱）（OI 0.8k）

📆 11-20 Forward Structure
存量OI: C 150.5k / P 120.4k，今日变化ΔOI: C +2.2k / P +3.2k，平值价格ATM: C $9.15 / P $9.35 ｜ ATM IV 78.4%，净 delta 敞口 -21k shares
Top ΔOI: P 120 +1,378 ｜ C 150 -883
仓位参考: Max Pain 135 ｜ Call Wall 135（+0.8%）（OI 42.8k） ｜ Put Wall 130（-2.9%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.4%｜历史 Rank 72%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 21,345 股

📆 11-27 Forward Structure
存量OI: C 10.7k / P 21.1k，今日变化ΔOI: C +1.7k / P +3.9k，平值价格ATM: C $9.75 / P $11.35 ｜ ATM IV 74.7%，净 delta 敞口 -72k shares
Top ΔOI: P 115 +1,696 ｜ C 170 +589 ｜ P 120 +498
仓位参考: Max Pain 155 ｜ Call Wall 145（+8.2%，弱）（OI 0.8k） ｜ Put Wall 140（+4.5%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 74.7%｜历史 Rank 72%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 72,393 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 93.4% vs 11-13 81.8%（差 +11.5pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/MSTR_morning.json