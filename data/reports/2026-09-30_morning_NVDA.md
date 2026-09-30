# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $763.55 ｜ QQQ $739.77
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 230P ΔOI +7,101（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 227.21 → 今开 229.00（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 232.37 ｜ 低 228.80

Options: P/C成交量 0.45 | OI比 0.61 | ATM IV 37.1% | Skew 2.6pp | Term 0.85 | ExpMove ±2.2%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.2% ｜ 10-05（5D）±2.6% ｜ 10-07（7D）±3.4% ｜ 10-09（9D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 718,528,732 | GEX Change vs 上次快照 268,644,672 | Flip: Primary Flip: 218.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 714 / LOW 209 / INVALID 505
结构观察区: Primary Flip 218.76（全链重定价，覆盖 98%）
Call Wall 235（弱结构｜现价低于该位 1.5%）
最近结构参考: Call Wall 235（现价低于该位 1.5%）
量化视角： 正 Gamma（7.19亿，无历史分位）｜正 Gamma 增强（+2.69亿）｜现价位于 Flip 上方 5.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 228（MaxPain，仅结算参考）；上方 235（Call Wall，弱结构）。
• Gamma 区域：切换参考 219（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-30 235.0C — Vol 160,056 | 最新价 $0.08 | OI 18109→40171 (ΔOI +22062张) | ΔOI/Volume 13.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22062张（+121.8% vs前日OI），连续性待观察（方向未知）
09-30 232.5C — Vol 216,948 | 最新价 $0.18 | OI 9737→29661 (ΔOI +19924张) | ΔOI/Volume 9.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19924张（+204.6% vs前日OI），连续性待观察（方向未知）
09-30 230.0C — Vol 174,868 | 最新价 $0.55 | OI 12848→31638 (ΔOI +18790张) | ΔOI/Volume 10.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18790张（+146.2% vs前日OI），连续性待观察（方向未知）
10-02 250.0C — Vol 75,290 | 最新价 $0.02 | OI 48006→63280 (ΔOI +15274张) | ΔOI/Volume 20.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15274张（+31.8% vs前日OI），连续性待观察（方向未知）
09-30 227.5P — Vol 94,669 | 最新价 $1.63 | OI 3324→11377 (ΔOI +8053张) | ΔOI/Volume 8.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8053张（+242.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 84,103 张（Put 8,053 / Call 76,050），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 185.2k / P 113.7k，今日成交量: C 283.4k / P 126.3k，平值价格ATM: C $0.39 / P $1.77 ｜ ATM IV 37.1%，预期波动 ±0.9%，Max Pain 228
Top ΔOI: C 235 +22,062 ｜ C 232 +19,924 ｜ C 230 +18,790

📆 Forward Expiration Structure

10-02  C +46.4k / P +30.6k ｜ Activity HIGH ｜ 2D
10-05  C +8.9k / P +9.2k ｜ Activity HIGH ｜ 5D
10-07  C +2.4k / P +2.9k ｜ Activity HIGH ｜ 7D
10-09  C +6.5k / P +7.2k ｜ Activity HIGH ｜ 9D

📆 10-02 Forward Structure
存量OI: C 491.0k / P 388.6k，今日变化ΔOI: C +46.4k / P +30.6k，平值价格ATM: C $1.95 / P $3.22 ｜ ATM IV 34.8%，净 delta 敞口 227k shares
Top ΔOI: C 250 +15,274 ｜ P 230 +7,101 ｜ C 237 +6,850
仓位参考: Max Pain 225 ｜ Call Wall 227.5（-1.7%，弱）（OI 77.4k） ｜ Put Wall 215（-7.1%，弱）（OI 25.4k）
量化解读： 存量 Call 重｜ATM IV 34.8%｜历史 Rank 26%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 226,753 股

📆 10-05 Forward Structure
存量OI: C 42.3k / P 25.7k，今日变化ΔOI: C +8.9k / P +9.2k，平值价格ATM: C $2.50 / P $3.55 ｜ ATM IV 27.7%，净 delta 敞口 232k shares
Top ΔOI: C 235 +3,667 ｜ P 212 +1,977 ｜ P 220 +1,910
仓位参考: Max Pain 225 ｜ Call Wall 235（+1.5%，弱）（OI 7.2k） ｜ Put Wall 220（-5.0%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.7%｜历史 Rank 26%（近端代理）｜IV/RV 1.16×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 231,510 股

📆 10-07 Forward Structure
存量OI: C 10.7k / P 6.8k，今日变化ΔOI: C +2.4k / P +2.9k，平值价格ATM: C $3.40 / P $4.35 ｜ ATM IV 29.0%，净 delta 敞口 62k shares
Top ΔOI: P 210 +1,039 ｜ P 227 +358 ｜ C 237 +321
仓位参考: Max Pain 228 ｜ Call Wall 247.5（+6.9%）（OI 4.3k） ｜ Put Wall 210（-9.3%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.0%｜历史 Rank 26%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 62,439 股

📆 10-09 Forward Structure
存量OI: C 121.4k / P 144.3k，今日变化ΔOI: C +6.5k / P +7.2k，平值价格ATM: C $4.00 / P $4.80 ｜ ATM IV 30.6%，净 delta 敞口 -147k shares
Top ΔOI: P 230 +5,013 ｜ P 210 -2,635 ｜ C 240 +1,845
仓位参考: Max Pain 225 ｜ Call Wall 250（+8.0%，弱）（OI 17.5k） ｜ Put Wall 215（-7.1%，弱）（OI 9.9k）
量化解读： 存量 Put 重｜ATM IV 30.6%｜历史 Rank 26%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 负 146,901 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 34.8% vs 10-05 27.7%（差 +7.1pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/NVDA_morning.json