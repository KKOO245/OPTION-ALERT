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
🟡 **事件差分**: 11-06 ATM IV 48.3% vs 11-13 37.1%（差 +11.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 440.75 → 今开 458.99（+4.1%） | 较昨收变动（含盘初走势） ｜ 今日高 478.07 ｜ 低 453.69

Options: P/C成交量 0.35 | OI比 0.62 | ATM IV 48.3% | Skew 4.1pp | Term 0.70 | ExpMove ±2.7%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价中性（Skew 4.1pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±2.7% ｜ 11-13（9D）±2.3% ｜ 11-20（16D）±6.2% ｜ 11-27（23D）±3.5%
   ⇒ IV–VIX Spread: +31.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,172,165 | GEX Change vs 上次快照 534,485 | Flip: Primary Flip: 415.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 281 / LOW 141 / INVALID 490
结构观察区: Primary Flip 415.91（全链重定价，覆盖 92%）
最近结构参考: Flip 416（现价高于该位 14.2%）
量化视角： 正 Gamma（317万，无历史分位）｜正 Gamma 增强（+53万）｜现价位于 Flip 上方 14.18%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 430（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 416（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 387.5P — Vol 110 | 最新价 $0.40 | OI 0→55 (ΔOI +55张) | ΔOI/Volume 50.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增55张（前日OI缺失），值得跟踪（方向未知）
11-20 455.0C — Vol 77 | 最新价 $8.73 | OI 325→352 (ΔOI +27张) | ΔOI/Volume 35.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增27张（+8.3% vs前日OI），值得跟踪（方向未知）
11-20 440.0P — Vol 34 | 最新价 $12.50 | OI 146→170 (ΔOI +24张) | ΔOI/Volume 70.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增24张（+16.4% vs前日OI），值得跟踪（方向未知）
11-06 480.0C — Vol 24 | 最新价 $0.20 | OI 74→98 (ΔOI +24张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24张（+32.4% vs前日OI），连续性待观察（方向未知）
11-06 465.0C — Vol 23 | 最新价 $0.71 | OI 99→122 (ΔOI +23张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23张（+23.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 153 张（Put 79 / Call 74），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.1k / P +19 ｜ Activity HIGH ｜ 2D
11-13  C +7 / P +76 ｜ Activity MEDIUM △ ｜ 9D
11-20  C +22 / P +60 ｜ Activity MEDIUM △ ｜ 16D
11-27  C +2 / P +3 ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 2.6k / P 1.6k，今日变化ΔOI: C +0.1k / P +19，平值价格ATM: C $6.73 / P $6.30 ｜ ATM IV 48.3%，净 delta 敞口 8k shares
Top ΔOI: C 480 +24 ｜ C 465 +23 ｜ C 460 +16
仓位参考: Max Pain 430 ｜ Call Wall 445（-6.3%）（OI 0.5k） ｜ Put Wall 450（-5.2%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 48.3%｜历史 Rank 82%（近端代理）｜IV/RV 1.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,276 股

11-13（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 440（-7.3%，弱）（OI 0.1k） ｜ Put Wall 435（-8.4%，弱）（OI 55）

11-20（MEDIUM △）Top ΔOI: 455C +27 ｜ 440P +24
11-20（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 435（-8.4%，弱）（OI 0.6k） ｜ Put Wall 427.5（-10.0%，弱）（OI 0.4k）

11-27（MEDIUM △）Top ΔOI: 435P +1 ｜ 450C +1
11-27（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 430（-9.5%，弱）（OI 64）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 48.3% vs 11-13 37.1%（差 +11.2pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/ISRG_morning.json