# 期权晚报 2026-09-02（快照 18:14 ET）

📊 市场环境

SPY $765.16 ｜ QQQ $709.24
VIX 15.20 ↓7.0%（5D -1.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 09-04 ATM IV 76.8% vs 09-11 64.7%（差 +12.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 123.35 → 收盘 123.19（-0.1%） ｜ 今日高 124.66 ｜ 低 121.38
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.27 | OI比 0.68 | ATM IV 76.8% | Skew -5.2pp | Term 0.88 | ExpMove ±4.6%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.27×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±4.6% ｜ 09-11（9D）±8.1% ｜ 09-18（16D）±11.1% ｜ 09-25（23D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,422,628 | GEX Change vs 上次快照 3,315,013 | Flip: Primary Flip: 117.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 891 / LOW 145 / INVALID 294
结构观察区: Primary Flip 117.77（全链重定价，覆盖 99%）
最近结构参考: Flip 118（现价高于该位 4.6%）
量化视角： 正 Gamma（2942万，无历史分位）｜正 Gamma 增强（+332万）｜现价位于 Flip 上方 4.60%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 118（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 131.0C — Vol 948 | 最新价 $0.70 | OI 10146→12725 (ΔOI +2579张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2579张（+25.4% vs前日OI），连续性待观察（方向未知）
09-04 128.0C — Vol 2,152 | 最新价 $1.22 | OI 1242→2655 (ΔOI +1413张) | ΔOI/Volume 65.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1413张（+113.8% vs前日OI），连续性待观察（方向未知）
09-04 129.0C — Vol 1,604 | 最新价 $1.00 | OI 976→2290 (ΔOI +1314张) | ΔOI/Volume 81.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1314张（+134.6% vs前日OI），连续性待观察（方向未知）
09-04 134.0C — Vol 990 | 最新价 $0.36 | OI 4491→5691 (ΔOI +1200张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1200张（+26.7% vs前日OI），连续性待观察（方向未知）
09-11 155.0C — Vol 174 | 最新价 $0.26 | OI 464→1339 (ΔOI +875张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增875张（+188.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,381 张（Put 0 / Call 7,381），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 9D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 16D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 260.3k / P 178.0k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.00 / P 2.71
隐含波动率 ATM IV:  76.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 76.8%｜历史 Rank 43%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 76.8% vs 09-11 64.7%（差 +12.2pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/MSTR_evening.json