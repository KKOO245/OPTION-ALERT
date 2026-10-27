# 期权晚报 2026-10-26（快照 21:54 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 18.39 ↓5.5%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 48.60 → 收盘 48.66（+0.1%） ｜ 今日高 49.03 ｜ 低 47.86 ｜ 昨收 48.72 → 收盘 48.66（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.82 | ATM IV 45.4% | Skew 4.5pp | Term 0.82 | ExpMove ±2.6%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 4.5pp）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-28（2D）±2.6% ｜ 10-30（4D）±3.7% ｜ 11-02（7D）±4.2% ｜ 11-04（9D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,899,941 | GEX Change vs 上次快照 -4,203,434 | Flip: Primary Flip: 49.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 640 / LOW 90 / INVALID 384
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 49.08（全链重定价，覆盖 99%）
Put Wall 50（弱结构｜现价低于该位 2.7%）
最近结构参考: Flip 49（现价低于该位 0.9%）
量化视角： 负 Gamma（990万，无历史分位）｜负 Gamma 加深（420万）｜现价位于 Flip 下方 0.86%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 48.0P — Vol 1,554 | 最新价 $1.56 | OI 16222→19623 (ΔOI +3401张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3401张（+21.0% vs前日OI），连续性待观察（方向未知）
11-04 51.5C — Vol 52 | 最新价 $0.32 | OI 0→2920 (ΔOI +2920张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2920张（前日OI缺失），值得跟踪（方向未知）
11-20 47.0P — Vol 142 | 最新价 $1.20 | OI 2402→5175 (ΔOI +2773张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2773张（+115.5% vs前日OI），连续性待观察（方向未知）
11-20 58.0C — Vol 60 | 最新价 $0.18 | OI 4289→7059 (ΔOI +2770张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2770张（+64.6% vs前日OI），连续性待观察（方向未知）
11-13 55.0C — Vol 198 | 最新价 $0.22 | OI 1401→4116 (ΔOI +2715张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2715张（+193.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,579 张（Put 6,174 / Call 8,405），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-28 Forward Structure
存量OI: C 16.2k / P 13.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.72 / P $0.57 ｜ ATM IV 45.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 50 ｜ Call Wall 50（+2.8%）（OI 3.9k） ｜ Put Wall 45.5（-6.5%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 45.4%｜历史 Rank 76%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 52 ｜ Call Wall 50（+2.8%，弱）（OI 1.9k） ｜ Put Wall 45（-7.5%，弱）（OI 4.1k）

11-02（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50.5（+3.8%）（OI 0.4k） ｜ Put Wall 53（+8.9%）（OI 0.2k）

11-04（Activity LOW）仓位参考: Max Pain 48 ｜ Call Wall 51.5（+5.8%）（OI 2.9k） ｜ Put Wall 53（+8.9%，弱）（OI 78）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/SLV_evening.json