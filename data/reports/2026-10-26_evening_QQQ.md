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


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 702.20 → 收盘 712.20（+1.4%） ｜ 今日高 715.25 ｜ 低 705.58 ｜ 昨收 704.40 → 收盘 712.20（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.17 | OI比 1.21 | ATM IV 20.8% | Skew 2.4pp | Term 1.09 | ExpMove ±0.9%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构正常（Term 1.09）｜保护溢价中性（Skew 2.4pp）｜当日成交偏 Put（P/C量 1.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.17×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 14% ｜ P/C OI(近端) 15%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 14%）｜近端持仓结构中性（P/C OI 分位 15%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-27（1D）±0.9% ｜ 10-28（2D）±1.5% ｜ 10-29（3D）±2.0% ｜ 10-30（4D）±2.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -674,238,175 | GEX Change vs 上次快照 -14,321,324 | Flip: Primary Flip: 726.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2853 / LOW 270 / INVALID 1245
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 726.90（全链重定价，覆盖 98%）
最近结构参考: Flip 727（现价低于该位 2.0%）
量化视角： 负 Gamma（6.74亿，历史分位偏负区，比 86% 的交易日更负）｜负 Gamma 加深（1432万）｜现价位于 Flip 下方 2.02%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 715（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 727（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-02 740.0C — Vol 1,961 | 最新价 $0.76 | OI 736→15988 (ΔOI +15252张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15252张（+2072.3% vs前日OI），连续性待观察（方向未知）
11-20 680.0P — Vol 9,208 | 最新价 $7.48 | OI 65697→76958 (ΔOI +11261张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增11261张（+17.1% vs前日OI），值得跟踪（方向未知）
11-06 713.0P — Vol 3,383 | 最新价 $12.42 | OI 39314→49355 (ΔOI +10041张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10041张（+25.5% vs前日OI），连续性待观察（方向未知）
11-02 720.0C — Vol 1,459 | 最新价 $5.74 | OI 871→9366 (ΔOI +8495张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8495张（+975.3% vs前日OI），连续性待观察（方向未知）
11-02 725.0C — Vol 400 | 最新价 $3.67 | OI 696→8355 (ΔOI +7659张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7659张（+1100.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 52,708 张（Put 21,302 / Call 31,406），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $21M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-28  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-29  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 10-27 Forward Structure
存量OI: C 94.3k / P 114.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.41 / P $2.82 ｜ ATM IV 20.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 715 ｜ Call Wall 710（-0.3%，弱）（OI 4.4k） ｜ Put Wall 700（-1.7%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 20.8%｜历史 Rank 64%（近端代理）｜IV/RV 1.16×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-28（Activity LOW）仓位参考: Max Pain 716 ｜ Call Wall 730（+2.5%，弱）（OI 2.7k） ｜ Put Wall 720（+1.1%，弱）（OI 2.6k）

10-29（Activity LOW）仓位参考: Max Pain 718 ｜ Call Wall 725（+1.8%，弱）（OI 2.3k） ｜ Put Wall 705（-1.0%，弱）（OI 1.8k）

10-30（Activity LOW）仓位参考: Max Pain 725 ｜ Call Wall 730（+2.5%，弱）（OI 16.6k） ｜ Put Wall 700（-1.7%，弱）（OI 72.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/QQQ_evening.json