# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 141C ΔOI +8,272（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 131.36 → 收盘 136.10（+3.6%） ｜ 今日高 139.75 ｜ 低 131.12 ｜ 昨收 134.76 → 收盘 136.10（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.54 | OI比 0.56 | ATM IV 79.4% | Skew 3.1pp | Term 0.91 | ExpMove ±6.6%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 3.1pp）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±6.6% ｜ 11-20（11D）±9.4% ｜ 11-27（18D）±6.0% ｜ 12-04（25D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,149,275 | GEX Change vs 上次快照 2,530,033 | Flip: Primary Flip: 129.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 352 / LOW 206 / INVALID 430
结构观察区: Primary Flip 129.87（全链重定价，覆盖 99%）
最近结构参考: Flip 130（现价高于该位 4.8%）
量化视角： 正 Gamma（1015万，无历史分位）｜正 Gamma 增强（+253万）｜现价位于 Flip 上方 4.80%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 130（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 147.0C — Vol 632 | 最新价 $1.26 | OI 142→8496 (ΔOI +8354张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8354张（+5883.1% vs前日OI），连续性待观察（方向未知）
11-13 141.0C — Vol 591 | 最新价 $2.54 | OI 135→8407 (ΔOI +8272张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8272张（+6127.4% vs前日OI），连续性待观察（方向未知）
11-13 143.0C — Vol 481 | 最新价 $2.10 | OI 75→7060 (ΔOI +6985张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6985张（+9313.3% vs前日OI），连续性待观察（方向未知）
11-13 137.0C — Vol 824 | 最新价 $4.15 | OI 128→7098 (ΔOI +6970张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6970张（+5445.3% vs前日OI），连续性待观察（方向未知）
11-13 140.0C — Vol 4,611 | 最新价 $2.95 | OI 473→3330 (ΔOI +2857张) | ΔOI/Volume 62.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2857张（+604.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 33,438 张（Put 0 / Call 33,438），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +45.6k / P +8.2k ｜ Activity HIGH ｜ 4D
11-20  C +1.4k / P +3.1k ｜ Activity HIGH ｜ 11D
11-27  C +0.5k / P +0.5k ｜ Activity HIGH ｜ 18D
12-04  C +0.1k / P +1.1k ｜ Activity HIGH ｜ 25D

📆 11-13 Forward Structure
存量OI: C 63.5k / P 35.3k，今日变化ΔOI: C +45.6k / P +8.2k，平值价格ATM: C $4.75 / P $4.28 ｜ ATM IV 79.4%，净 delta 敞口 1.3M shares
Top ΔOI: C 147 +8,354 ｜ C 141 +8,272 ｜ C 143 +6,985
仓位参考: Max Pain 137 ｜ Call Wall 147（+8.0%，弱）（OI 8.5k） ｜ Put Wall 135（-0.8%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 79.4%｜历史 Rank 60%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,345,854 股

📆 11-20 Forward Structure
存量OI: C 78.1k / P 62.4k，今日变化ΔOI: C +1.4k / P +3.1k，平值价格ATM: C $7.00 / P $5.82 ｜ ATM IV 71.3%，净 delta 敞口 64k shares
Top ΔOI: P 120 +645 ｜ C 140 +466
仓位参考: Max Pain 165 ｜ Put Wall 140（+2.9%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 71.3%｜历史 Rank 60%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 63,826 股

📆 11-27 Forward Structure
存量OI: C 4.5k / P 7.4k，今日变化ΔOI: C +0.5k / P +0.5k，平值价格ATM: C $8.20 / P $0.00 ｜ ATM IV 67.7%，净 delta 敞口 13k shares
仓位参考: Max Pain 150 ｜ Call Wall 140（+2.9%，弱）（OI 0.1k） ｜ Put Wall 130（-4.5%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 67.7%｜历史 Rank 60%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 12,900 股

📆 12-04 Forward Structure
存量OI: C 4.3k / P 6.7k，今日变化ΔOI: C +0.1k / P +1.1k，平值价格ATM: C $10.50 / P $8.30 ｜ ATM IV 69.0%，净 delta 敞口 -6k shares
Top ΔOI: P 135 +208
仓位参考: Max Pain 140 ｜ Call Wall 140（+2.9%）（OI 1.3k） ｜ Put Wall 135（-0.8%）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 69.0%｜历史 Rank 60%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 6,053 股

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 79.4% vs 11-20 71.3%（差 +8.1pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/COIN_evening.json