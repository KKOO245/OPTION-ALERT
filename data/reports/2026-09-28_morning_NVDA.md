# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $767.62 ｜ QQQ $737.28
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-30 232C ΔOI +6,682（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 225.07 → 今开 229.70（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 233.21 ｜ 低 229.50

Options: P/C成交量 0.28 | OI比 0.75 | ATM IV 48.9% | Skew -1.3pp | Term 0.65 | ExpMove ±2.3%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（2D）±2.3% ｜ 10-02（4D）±3.0% ｜ 10-05（7D）±3.1% ｜ 10-07（9D）±3.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 583,530,080 | GEX Change vs 上次快照 314,375,904 | Flip: Primary Flip: 215.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 674 / LOW 194 / INVALID 514
结构观察区: Primary Flip 215.61（全链重定价，覆盖 99%）
Call Wall 230（弱结构｜现价高于该位 0.7%）
最近结构参考: Call Wall 230（现价高于该位 0.7%）
量化视角： 正 Gamma（5.84亿，无历史分位）｜正 Gamma 增强（+3.14亿）｜现价位于 Flip 上方 7.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 222（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 227.5C — Vol 89,530 | 最新价 $2.47 | OI 6052→75663 (ΔOI +69611张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69611张（+1150.2% vs前日OI），连续性待观察（方向未知）
10-02 232.5C — Vol 49,711 | 最新价 $0.99 | OI 6132→45334 (ΔOI +39202张) | ΔOI/Volume 78.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39202张（+639.3% vs前日OI），连续性待观察（方向未知）
10-02 235.0C — Vol 46,568 | 最新价 $0.59 | OI 26904→51138 (ΔOI +24234张) | ΔOI/Volume 52.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24234张（+90.1% vs前日OI），连续性待观察（方向未知）
10-02 215.0P — Vol 19,288 | 最新价 $0.72 | OI 11328→25950 (ΔOI +14622张) | ΔOI/Volume 75.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14622张（+129.1% vs前日OI），连续性待观察（方向未知）
10-02 115.0P — Vol 14,809 | 最新价 $0.01 | OI 954→14626 (ΔOI +13672张) | ΔOI/Volume 92.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13672张（+1433.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 161,341 张（Put 28,294 / Call 133,047），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 105.8k / P 79.8k，今日成交量: C 489.2k / P 138.3k，平值价格ATM: C $0.69 / P $1.97 ｜ ATM IV 48.9%，预期波动 ±1.2%，Max Pain 222
Top ΔOI: C 230 +13,099 ｜ C 227 +12,853 ｜ P 202 +4,863

📆 Forward Expiration Structure

09-30  C +18.1k / P +16.2k ｜ Activity HIGH ｜ 2D
10-02  C +158.1k / P +88.0k ｜ Activity HIGH ｜ 4D
10-05  C +4.1k / P +2.5k ｜ Activity HIGH ｜ 7D
10-07  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 09-30 Forward Structure
存量OI: C 55.3k / P 41.4k，今日变化ΔOI: C +18.1k / P +16.2k，平值价格ATM: C $2.05 / P $3.24 ｜ ATM IV 35.9%，净 delta 敞口 814k shares
Top ΔOI: C 232 +6,682 ｜ C 235 +3,346
仓位参考: Max Pain 222 ｜ Call Wall 230（-0.7%，弱）（OI 11.2k） ｜ Put Wall 212.5（-8.3%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 35.9%｜历史 Rank 68%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 813,821 股

📆 10-02 Forward Structure
存量OI: C 377.8k / P 337.0k，今日变化ΔOI: C +158.1k / P +88.0k，平值价格ATM: C $2.97 / P $4.02 ｜ ATM IV 34.6%，净 delta 敞口 8.0M shares
Top ΔOI: C 227 +69,611 ｜ C 232 +39,202 ｜ C 235 +24,234
仓位参考: Max Pain 222 ｜ Call Wall 227.5（-1.8%，弱）（OI 75.7k） ｜ Put Wall 215（-7.2%，弱）（OI 25.9k）
量化解读： 存量两侧均衡｜ATM IV 34.6%｜历史 Rank 68%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,996,341 股

📆 10-05 Forward Structure
存量OI: C 19.2k / P 8.3k，今日变化ΔOI: C +4.1k / P +2.5k，平值价格ATM: C $3.40 / P $3.90 ｜ ATM IV 29.6%，净 delta 敞口 181k shares
Top ΔOI: C 225 +762 ｜ P 220 +736 ｜ P 215 +734
仓位参考: Max Pain 222 ｜ Call Wall 230（-0.7%）（OI 4.3k） ｜ Put Wall 222.5（-3.9%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 29.6%｜历史 Rank 68%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 181,301 股

📆 10-07 Forward Structure
存量OI: C 1.4k / P 0.8k，今日变化ΔOI: C +0.8k / P +0.5k，平值价格ATM: C $4.10 / P $5.00 ｜ ATM IV 30.9%，净 delta 敞口 34k shares
Top ΔOI: P 215 +160 ｜ C 225 +146 ｜ C 230 +107
仓位参考: Max Pain 220 ｜ Call Wall 225（-2.9%，弱）（OI 0.3k） ｜ Put Wall 215（-7.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 30.9%｜历史 Rank 68%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 33,550 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/NVDA_morning.json