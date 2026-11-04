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
🔴 **事件差分**: 11-06（2D）ATM IV 101.7% vs 11-13 84.2%（差 +17.5pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-06 1100P ΔOI -436（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,126.52 → 今开 1,079.00（-4.2%） | 较昨收变动（含盘初走势） ｜ 今日高 1120.22 ｜ 低 1059.00

Options: P/C成交量 0.55 | OI比 0.70 | ATM IV 101.7% | Skew 3.7pp | Term 0.75 | ExpMove ±6.4%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±6.4% ｜ 11-13（9D）±10.7% ｜ 11-20（16D）±13.9% ｜ 11-27（23D）±17.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,953,008 | GEX Change vs 上次快照 464,871 | Flip: Primary Flip: 1129.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1700 / LOW 566 / INVALID 974
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1129.02（全链重定价，覆盖 100%）
Put Wall 1,000（弱结构｜现价高于该位 10.0%）
最近结构参考: Flip 1129（现价低于该位 2.5%）
量化视角： 负 Gamma（195万，无历史分位）｜负 Gamma 缓解（+46万）｜现价位于 Flip 下方 2.55%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,000（Put Wall，弱结构）；上方 1,190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1129（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 1400.0C — Vol 4,682 | 最新价 $0.90 | OI 1311→3276 (ΔOI +1965张) | ΔOI/Volume 42.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1965张（+149.9% vs前日OI），连续性待观察（方向未知）
11-06 1300.0C — Vol 3,562 | 最新价 $3.10 | OI 1654→2493 (ΔOI +839张) | ΔOI/Volume 23.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增839张（+50.7% vs前日OI），连续性待观察（方向未知）
11-20 1150.0C — Vol 1,040 | 最新价 $70.88 | OI 352→1184 (ΔOI +832张) | ΔOI/Volume 80.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增832张（+236.4% vs前日OI），连续性待观察（方向未知）
11-20 950.0P — Vol 787 | 最新价 $21.85 | OI 787→1195 (ΔOI +408张) | ΔOI/Volume 51.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增408张（+51.8% vs前日OI），连续性待观察（方向未知）
11-06 1320.0C — Vol 572 | 最新价 $2.25 | OI 310→704 (ΔOI +394张) | ΔOI/Volume 68.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增394张（+127.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,438 张（Put 408 / Call 4,030），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +6.2k / P +1.6k ｜ Activity HIGH ｜ 2D
11-13  C +2.8k / P +0.4k ｜ Activity HIGH ｜ 9D
11-20  C +2.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
11-27  C +0.7k / P +0.2k ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 44.5k / P 30.9k，今日变化ΔOI: C +6.2k / P +1.6k，平值价格ATM: C $34.55 / P $35.65 ｜ ATM IV 101.7%，净 delta 敞口 56k shares
Top ΔOI: C 1400 +1,965 ｜ C 1300 +839 ｜ P 1100 -436
仓位参考: Max Pain 1,190 ｜ Call Wall 1200（+9.1%，弱）（OI 1.4k） ｜ Put Wall 1000（-9.1%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 101.7%｜历史 Rank 57%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 56,144 股

📆 11-13 Forward Structure
存量OI: C 15.6k / P 9.8k，今日变化ΔOI: C +2.8k / P +0.4k，平值价格ATM: C $56.63 / P $61.28 ｜ ATM IV 84.2%，净 delta 敞口 39k shares
Top ΔOI: C 1150 +193
仓位参考: Max Pain 1,250 ｜ Call Wall 1200（+9.1%，弱）（OI 0.4k） ｜ Put Wall 1100（-0.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 84.2%｜历史 Rank 57%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 38,844 股

11-20（MEDIUM △）Top ΔOI: 1150C +832 ｜ 950P +408
11-20（MEDIUM △）仓位参考: Max Pain 1,390 ｜ Call Wall 1150（+4.5%，弱）（OI 1.2k） ｜ Put Wall 1000（-9.1%，弱）（OI 2.3k）

11-27（MEDIUM △）Top ΔOI: 1200C +72
11-27（MEDIUM △）仓位参考: Max Pain 1,270 ｜ Put Wall 1150（+4.5%）（OI 1.1k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 101.7% vs 11-13 84.2%（差 +17.5pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/SNDK_morning.json