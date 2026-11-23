# 期权晚报 2026-11-23（快照 16:40 ET）

📊 市场环境

SPY $722.29 ｜ QQQ $651.03
VIX 26.62 ↓25.8%（5D +16.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 12-11 165C ΔOI +100（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 176.04 → 收盘 168.15（-4.5%） ｜ 今日高 177.00 ｜ 低 165.30 ｜ 昨收 142.39 → 收盘 168.15（+18.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.79 | OI比 0.56 | ATM IV 118.0% | Skew 14.4pp | Term 0.87 | ExpMove ±9.7%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价显著（Skew 14.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±9.7% ｜ 12-04（11D）±15.4% ｜ 12-11（18D）±21.6% ｜ 12-18（25D）±22.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,715,648 | GEX Change vs 上次快照 -619,388 | Flip: Primary Flip: 181.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 544 / LOW 86 / INVALID 330
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 181.00（全链重定价，覆盖 100%）
最近结构参考: Flip 181（现价低于该位 7.1%）
量化视角： 负 Gamma（272万，无历史分位）｜负 Gamma 加深（62万）｜现价位于 Flip 下方 7.10%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 165（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 150.0C — Vol 2,485 | 最新价 $22.00 | OI 16→1744 (ΔOI +1728张) | ΔOI/Volume 69.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1728张（+10800.0% vs前日OI），连续性待观察（方向未知）
11-27 195.0C — Vol 3,868 | 最新价 $0.98 | OI 856→2416 (ΔOI +1560张) | ΔOI/Volume 40.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1560张（+182.2% vs前日OI），连续性待观察（方向未知）
12-24 135.0P — Vol 21 | 最新价 $6.50 | OI 73→1616 (ΔOI +1543张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1543张（+2113.7% vs前日OI），连续性待观察（方向未知）
11-27 145.0P — Vol 1,494 | 最新价 $1.59 | OI 369→1834 (ΔOI +1465张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1465张（+397.0% vs前日OI），连续性待观察（方向未知）
11-27 120.0C — Vol 2 | 最新价 $53.47 | OI 9→1259 (ΔOI +1250张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1250张（+13888.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,546 张（Put 3,008 / Call 4,538），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +13.7k / P +6.7k ｜ Activity HIGH ｜ 4D
12-04  C +1.2k / P +2.6k ｜ Activity HIGH ｜ 11D
12-11  C +0.8k / P +0.3k ｜ Activity HIGH ｜ 18D
12-18  C +2.5k / P -1.2k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 40.5k / P 22.8k，今日变化ΔOI: C +13.7k / P +6.7k，平值价格ATM: C $8.60 / P $7.65 ｜ ATM IV 118.0%，净 delta 敞口 871k shares
Top ΔOI: C 150 +1,728 ｜ C 195 +1,560 ｜ P 145 +1,465
仓位参考: Max Pain 165 ｜ Call Wall 170（+1.1%，弱）（OI 1.7k） ｜ Put Wall 160（-4.8%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 118.0%｜历史 Rank 74%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 870,556 股

📆 12-04 Forward Structure
存量OI: C 11.2k / P 10.9k，今日变化ΔOI: C +1.2k / P +2.6k，平值价格ATM: C $13.45 / P $12.40 ｜ ATM IV 112.9%，净 delta 敞口 34k shares
Top ΔOI: P 150 +998 ｜ C 150 +306 ｜ C 165 +298
仓位参考: Max Pain 195 ｜ Call Wall 180（+7.0%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 112.9%｜历史 Rank 74%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,444 股

📆 12-11 Forward Structure
存量OI: C 4.7k / P 5.1k，今日变化ΔOI: C +0.8k / P +0.3k，平值价格ATM: C $20.95 / P $15.30 ｜ ATM IV 106.4%，净 delta 敞口 29k shares
Top ΔOI: P 140 +147 ｜ C 165 +100
仓位参考: Max Pain 195 ｜ Call Wall 170（+1.1%，弱）（OI 0.1k） ｜ Put Wall 175（+4.1%）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 106.4%｜历史 Rank 74%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 29,008 股

📆 12-18 Forward Structure
存量OI: C 62.3k / P 75.4k，今日变化ΔOI: C +2.5k / P -1.2k，平值价格ATM: C $19.63 / P $17.75 ｜ ATM IV 105.1%，净 delta 敞口 316k shares
Top ΔOI: P 135 -1,255 ｜ C 170 +845 ｜ P 140 +797
仓位参考: Max Pain 210 ｜ Call Wall 170（+1.1%，弱）（OI 1.8k） ｜ Put Wall 175（+4.1%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 105.1%｜历史 Rank 74%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 315,559 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 118.0% vs 12-04 112.9%（差 +5.0pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/BE_evening.json