# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.96 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 11P ΔOI +83（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 11.43 → 今开 11.40（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 11.85 ｜ 低 11.21

Options: P/C成交量 0.86 | OI比 0.55 | ATM IV 95.9% | Skew 17.4pp | Term 0.86 | ExpMove ±7.2%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 17.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±7.2% ｜ 11-13（9D）±18.3% ｜ 11-20（16D）±15.0% ｜ 11-27（23D）±13.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -98,583 | GEX Change vs 上次快照 5,965 | Flip: Primary Flip: 11.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 129 / LOW 80 / INVALID 191
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.47（全链重定价，覆盖 92%）
Put Wall 12（弱结构｜现价低于该位 5.8%）
最近结构参考: Flip 11（现价低于该位 1.4%）
量化视角： 负 Gamma（10万，无历史分位）｜负 Gamma 缓解（+1万）｜现价位于 Flip 下方 1.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 12.0C — Vol 130 | 最新价 $0.15 | OI 235→321 (ΔOI +86张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增86张（+36.6% vs前日OI），连续性待观察（方向未知）
11-06 11.0P — Vol 108 | 最新价 $0.20 | OI 307→390 (ΔOI +83张) | ΔOI/Volume 76.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增83张（+27.0% vs前日OI），连续性待观察（方向未知）
11-06 11.5C — Vol 84 | 最新价 $0.35 | OI 213→286 (ΔOI +73张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增73张（+34.3% vs前日OI），连续性待观察（方向未知）
11-06 12.5C — Vol 66 | 最新价 $0.07 | OI 255→316 (ΔOI +61张) | ΔOI/Volume 92.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增61张（+23.9% vs前日OI），连续性待观察（方向未知）
11-20 11.5C — Vol 73 | 最新价 $0.85 | OI 4→58 (ΔOI +54张) | ΔOI/Volume 74.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54张（+1350.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 357 张（Put 83 / Call 274），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.2k / P +74 ｜ Activity HIGH ｜ 2D
11-13  C +84 / P +54 ｜ Activity HIGH ｜ 9D
11-20  C +0.1k / P +19 ｜ Activity MEDIUM △ ｜ 16D
11-27  C +34 / P +4 ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 3.4k / P 1.9k，今日变化ΔOI: C +0.2k / P +74，平值价格ATM: C $0.35 / P $0.47 ｜ ATM IV 95.9%，净 delta 敞口 11k shares
Top ΔOI: C 12 +86 ｜ P 11 +83 ｜ C 11 +73
仓位参考: Max Pain 12 ｜ Call Wall 12（+6.1%，弱）（OI 0.3k） ｜ Put Wall 11.5（+1.7%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 95.9%｜历史 Rank 37%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,721 股

📆 11-13 Forward Structure
存量OI: C 1.1k / P 0.7k，今日变化ΔOI: C +84 / P +54，平值价格ATM: C $1.10 / P $0.97 ｜ ATM IV 89.0%，净 delta 敞口 -2k shares
Top ΔOI: C 12 +37
仓位参考: Max Pain 13 ｜ Call Wall 12（+6.1%，弱）（OI 65） ｜ Put Wall 10.5（-7.2%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 89.0%｜历史 Rank 37%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,606 股

11-20（MEDIUM △）Top ΔOI: 11C +54 ｜ 11P +52
11-20（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 12（+6.1%，弱）（OI 0.3k）

11-27（MEDIUM △）Top ΔOI: 11C +23
11-27（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 11.5（+1.7%，弱）（OI 23）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 95.9% vs 11-13 89.0%（差 +6.9pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/NNE_morning.json