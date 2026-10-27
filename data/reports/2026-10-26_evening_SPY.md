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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 759.90 → 收盘 765.37（+0.7%） ｜ 今日高 767.73 ｜ 低 761.63 ｜ 昨收 759.97 → 收盘 765.37（+0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.07 | OI比 1.75 | ATM IV 12.0% | Skew 1.5pp | Term 1.20 | ExpMove ±0.5%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常偏陡（Term 1.20）｜保护溢价薄（Skew 1.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.75×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 29% ｜ P/C OI(近端) 43%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 29%）｜近端持仓结构中性（P/C OI 分位 43%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-27（1D）±0.5% ｜ 10-28（2D）±0.9% ｜ 10-29（3D）±1.2% ｜ 10-30（4D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,221,327,469 | GEX Change vs 上次快照 547,769,388 | Flip: Primary Flip: 773.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3077 / LOW 258 / INVALID 1393
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.61（全链重定价，覆盖 99%）
最近结构参考: Flip 774（现价低于该位 1.1%）
量化视角： 负 Gamma（12.21亿，历史分位 29%，中性区）｜负 Gamma 缓解（+5.48亿）｜现价位于 Flip 下方 1.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 767（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 774（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 755.0P — Vol 66,604 | 最新价 $2.06 | OI 23470→150938 (ΔOI +127468张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127468张（+543.1% vs前日OI），连续性待观察（方向未知）
10-30 745.0P — Vol 63,266 | 最新价 $0.83 | OI 81237→157799 (ΔOI +76562张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增76562张（+94.2% vs前日OI），连续性待观察（方向未知）
10-27 753.0P — Vol 11,337 | 最新价 $0.06 | OI 572→24620 (ΔOI +24048张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24048张（+4204.2% vs前日OI），连续性待观察（方向未知）
11-20 722.0P — Vol 17,231 | 最新价 $2.88 | OI 6260→24947 (ΔOI +18687张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18687张（+298.5% vs前日OI），连续性待观察（方向未知）
11-20 700.0P — Vol 970 | 最新价 $1.71 | OI 75322→87048 (ΔOI +11726张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增11726张（+15.6% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 258,491 张（Put 258,491 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $34M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-28  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-29  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 10-27 Forward Structure
存量OI: C 83.2k / P 145.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.05 / P $1.81 ｜ ATM IV 12.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 767 ｜ Call Wall 777（+1.5%）（OI 6.9k） ｜ Put Wall 753（-1.6%，弱）（OI 24.6k）
量化解读： 存量 Put 重｜ATM IV 12.0%｜历史 Rank 44%（近端代理）｜IV/RV 1.31×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-28（Activity LOW）仓位参考: Max Pain 767 ｜ Call Wall 785（+2.6%，弱）（OI 3.5k）

10-29（Activity LOW）仓位参考: Max Pain 766 ｜ Call Wall 786（+2.7%，弱）（OI 2.8k） ｜ Put Wall 744（-2.8%，弱）（OI 3.0k）

10-30（Activity LOW）仓位参考: Max Pain 765 ｜ Call Wall 780（+1.9%，弱）（OI 26.3k） ｜ Put Wall 745（-2.7%，弱）（OI 157.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/SPY_evening.json