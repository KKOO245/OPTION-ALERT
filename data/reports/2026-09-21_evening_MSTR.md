# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 160C ΔOI +2,329（距现价 -5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 164.58 → 收盘 168.50（+2.4%） ｜ 今日高 169.50 ｜ 低 164.55 ｜ 昨收 153.92 → 收盘 168.50（+9.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.74 | ATM IV 86.8% | Skew -12.6pp | Term 0.86 | ExpMove ±7.3%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -12.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±7.3% ｜ 10-02（11D）±10.8% ｜ 10-09（18D）±13.6% ｜ 10-16（25D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 51,340,997 | GEX Change vs 上次快照 -6,821,899 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 759 / LOW 35 / INVALID 278
结构观察区: NO_CROSS
量化视角： 正 Gamma（5134万，无历史分位）｜正 Gamma 减弱（682万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 155.0C — Vol 3,785 | 最新价 $14.75 | OI 1080→20594 (ΔOI +19514张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19514张（+1806.8% vs前日OI），连续性待观察（方向未知）
09-25 150.0C — Vol 5,202 | 最新价 $18.92 | OI 2669→20707 (ΔOI +18038张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18038张（+675.8% vs前日OI），连续性待观察（方向未知）
09-25 152.5C — Vol 1,461 | 最新价 $16.90 | OI 234→17305 (ΔOI +17071张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17071张（+7295.3% vs前日OI），连续性待观察（方向未知）
09-25 101.0P — Vol 6,662 | 最新价 $0.02 | OI 109→16623 (ΔOI +16514张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16514张（+15150.5% vs前日OI），连续性待观察（方向未知）
09-25 157.5C — Vol 1,383 | 最新价 $12.70 | OI 346→15367 (ΔOI +15021张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15021张（+4341.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 86,158 张（Put 16,514 / Call 69,644），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +156.8k / P +82.7k ｜ Activity HIGH ｜ 4D
10-02  C +9.2k / P +11.6k ｜ Activity HIGH ｜ 11D
10-09  C +7.3k / P +5.6k ｜ Activity HIGH ｜ 18D
10-16  C +8.7k / P +4.7k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 225.6k / P 166.3k，今日变化ΔOI: C +156.8k / P +82.7k，平值价格ATM: C $6.60 / P $5.65 ｜ ATM IV 86.8%，净 delta 敞口 12.1M shares
Top ΔOI: C 155 +19,514 ｜ C 150 +18,038 ｜ C 152 +17,071
仓位参考: Max Pain 135 ｜ Call Wall 155（-8.0%，弱）（OI 20.6k）
量化解读： 存量 Call 重｜ATM IV 86.8%｜历史 Rank 60%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,051,872 股

📆 10-02 Forward Structure
存量OI: C 36.5k / P 60.6k，今日变化ΔOI: C +9.2k / P +11.6k，平值价格ATM: C $9.56 / P $8.59 ｜ ATM IV 77.4%，净 delta 敞口 474k shares
Top ΔOI: C 150 +1,569 ｜ P 150 +1,157
仓位参考: Max Pain 135 ｜ Call Wall 180（+6.8%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 77.4%｜历史 Rank 60%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 473,674 股

📆 10-09 Forward Structure
存量OI: C 17.0k / P 34.7k，今日变化ΔOI: C +7.3k / P +5.6k，平值价格ATM: C $12.00 / P $10.85 ｜ ATM IV 75.7%，净 delta 敞口 481k shares
Top ΔOI: C 144 +3,455 ｜ C 160 +2,329
仓位参考: Max Pain 138 ｜ Call Wall 160（-5.0%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 75.7%｜历史 Rank 60%（近端代理）｜IV/RV 0.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 481,483 股

📆 10-16 Forward Structure
存量OI: C 157.1k / P 127.5k，今日变化ΔOI: C +8.7k / P +4.7k，平值价格ATM: C $13.95 / P $12.75 ｜ ATM IV 75.0%，净 delta 敞口 390k shares
Top ΔOI: C 155 +8,375 ｜ C 95 -2,022
仓位参考: Max Pain 110 ｜ Call Wall 180（+6.8%，弱）（OI 10.8k） ｜ Put Wall 160（-5.0%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 75.0%｜历史 Rank 60%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 正 390,481 股

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 86.8% vs 10-02 77.4%（差 +9.4pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/MSTR_evening.json