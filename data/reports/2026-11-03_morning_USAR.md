# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $753.95 ｜ QQQ $685.78
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 8.85 → 今开 8.94（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 9.03 ｜ 低 8.83

Options: P/C成交量 0.19 | OI比 0.59 | ATM IV 116.4% | Skew -6.7pp | Term 0.81 | ExpMove ±9.3%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±9.3% ｜ 11-13（10D）±14.6% ｜ 11-20（17D）±18.4% ｜ 11-27（24D）±19.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -679,933 | GEX Change vs 上次快照 -136,638 | Flip: Primary Flip: 9.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 228 / LOW 61 / INVALID 107
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.19（全链重定价，覆盖 100%）
最近结构参考: Flip 9（现价低于该位 3.2%）
量化视角： 负 Gamma（68万，无历史分位）｜负 Gamma 加深（14万）｜现价位于 Flip 下方 3.18%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 8.0P — Vol 1,694 | 最新价 $0.14 | OI 202→1756 (ΔOI +1554张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1554张（+769.3% vs前日OI），连续性待观察（方向未知）
11-06 10.5C — Vol 1,759 | 最新价 $0.04 | OI 1596→2507 (ΔOI +911张) | ΔOI/Volume 51.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增911张（+57.1% vs前日OI），连续性待观察（方向未知）
11-06 10.0C — Vol 1,715 | 最新价 $0.10 | OI 1151→1947 (ΔOI +796张) | ΔOI/Volume 46.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增796张（+69.2% vs前日OI），连续性待观察（方向未知）
11-06 9.5C — Vol 933 | 最新价 $0.22 | OI 197→902 (ΔOI +705张) | ΔOI/Volume 75.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增705张（+357.9% vs前日OI），连续性待观察（方向未知）
11-20 9.0P — Vol 869 | 最新价 $0.85 | OI 3097→3606 (ΔOI +509张) | ΔOI/Volume 58.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增509张（+16.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,475 张（Put 2,063 / Call 2,412），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +3.3k / P +2.1k ｜ Activity HIGH ｜ 3D
11-13  C +0.5k / P -28 ｜ Activity MEDIUM △ ｜ 10D
11-20  C +1.1k / P +1.1k ｜ Activity MEDIUM △ ｜ 17D
11-27  C +25 / P +0.1k ｜ Activity MEDIUM △ ｜ 24D

📆 11-06 Forward Structure
存量OI: C 14.0k / P 8.2k，今日变化ΔOI: C +3.3k / P +2.1k，平值价格ATM: C $0.38 / P $0.45 ｜ ATM IV 116.4%，净 delta 敞口 18k shares
仓位参考: Max Pain 10 ｜ Call Wall 9.5（+6.8%，弱）（OI 0.9k） ｜ Put Wall 9（+1.2%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 116.4%｜历史 Rank 53%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,509 股

11-13（MEDIUM △）Top ΔOI: 15P -103
11-13（MEDIUM △）仓位参考: Max Pain 10 ｜ Put Wall 9.5（+6.8%，弱）（OI 0.4k）

11-20（MEDIUM △）Top ΔOI: 9P +509 ｜ 9P +501
11-20（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 9.5（+6.8%，弱）（OI 1.7k） ｜ Put Wall 9（+1.2%，弱）（OI 3.6k）

11-27（MEDIUM △）Top ΔOI: 9P +47 ｜ 9P +24
11-27（MEDIUM △）仓位参考: Max Pain 10 ｜ Put Wall 9.5（+6.8%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 116.4% vs 11-13 110.2%（差 +6.2pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/USAR_morning.json