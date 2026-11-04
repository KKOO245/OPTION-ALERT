# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.05 ｜ QQQ $697.28
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 8.71 → 今开 8.77（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 9.02 ｜ 低 8.48

Options: P/C成交量 0.28 | OI比 0.54 | ATM IV 117.6% | Skew 0.2pp | Term 0.81 | ExpMove ±7.8%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±7.8% ｜ 11-13（9D）±15.0% ｜ 11-20（16D）±18.7% ｜ 11-27（23D）±20.7%
   ⇒ IV–VIX Spread: +100.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -401,199 | GEX Change vs 上次快照 1,176,790 | Flip: Primary Flip: 8.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 175 / LOW 67 / INVALID 154
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 8.66（全链重定价，覆盖 100%）
最近结构参考: Flip 9（现价低于该位 1.8%）
量化视角： 负 Gamma（40万，无历史分位）｜负 Gamma 缓解（+118万）｜现价位于 Flip 下方 1.76%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 9.5C — Vol 1,670 | 最新价 $0.10 | OI 902→2176 (ΔOI +1274张) | ΔOI/Volume 76.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1274张（+141.2% vs前日OI），连续性待观察（方向未知）
11-06 7.5P — Vol 766 | 最新价 $0.04 | OI 6→766 (ΔOI +760张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增760张（+12666.7% vs前日OI），连续性待观察（方向未知）
11-20 9.0C — Vol 619 | 最新价 $0.70 | OI 1359→1933 (ΔOI +574张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增574张（+42.2% vs前日OI），连续性待观察（方向未知）
11-20 9.0P — Vol 740 | 最新价 $0.96 | OI 3606→4051 (ΔOI +445张) | ΔOI/Volume 60.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增445张（+12.3% vs前日OI），连续性待观察（方向未知）
11-20 8.0P — Vol 527 | 最新价 $0.46 | OI 1788→2119 (ΔOI +331张) | ΔOI/Volume 62.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增331张（+18.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,384 张（Put 1,536 / Call 1,848），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +2.3k / P +0.7k ｜ Activity HIGH ｜ 2D
11-13  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 9D
11-20  C +0.8k / P +0.7k ｜ Activity HIGH ｜ 16D
11-27  C -0.2k / P +82 ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 16.3k / P 8.9k，今日变化ΔOI: C +2.3k / P +0.7k，平值价格ATM: C $0.36 / P $0.30 ｜ ATM IV 117.6%，净 delta 敞口 54k shares
Top ΔOI: C 9 +322
仓位参考: Max Pain 10 ｜ Call Wall 9（+5.8%，弱）（OI 0.8k） ｜ Put Wall 9（+5.8%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 117.6%｜历史 Rank 55%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 54,283 股

11-13（MEDIUM △）仓位参考: Max Pain 10 ｜ Put Wall 9（+5.8%，弱）（OI 0.4k）

📆 11-20 Forward Structure
存量OI: C 34.1k / P 29.0k，今日变化ΔOI: C +0.8k / P +0.7k，平值价格ATM: C $0.58 / P $1.01 ｜ ATM IV 106.3%，净 delta 敞口 10k shares
Top ΔOI: C 9 +574 ｜ P 9 +445 ｜ P 8 +331
仓位参考: Max Pain 12 ｜ Call Wall 9（+5.8%，弱）（OI 1.9k） ｜ Put Wall 9（+5.8%，弱）（OI 4.1k）
量化解读： 存量两侧均衡｜ATM IV 106.3%｜历史 Rank 55%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,622 股

11-27（MEDIUM △）Top ΔOI: 16P -123 ｜ 8P +120
11-27（MEDIUM △）仓位参考: Max Pain 10 ｜ Put Wall 8（-6.0%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 117.6% vs 11-13 112.3%（差 +5.3pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=83 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=83）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/USAR_morning.json