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
🟡 **近现价集中开仓**: 09-25 202C ΔOI +5,727（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 115P ΔOI +2,736 占该期限总 OI 21.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 205.50 → 收盘 201.05（-2.2%） ｜ 今日高 208.33 ｜ 低 200.65 ｜ 昨收 194.25 → 收盘 201.05（+3.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.37 | OI比 0.60 | ATM IV 75.5% | Skew -6.5pp | Term 0.89 | ExpMove ±6.3%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（4D）±6.3% ｜ 10-02（11D）±9.6% ｜ 10-09（18D）±11.9% ｜ 10-16（25D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,538,991 | GEX Change vs 上次快照 -811,714 | Flip: Primary Flip: 172.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 558 / LOW 89 / INVALID 233
结构观察区: Primary Flip 172.17（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价高于该位 0.5%）
最近结构参考: Call Wall 200（现价高于该位 0.5%）
量化视角： 正 Gamma（2854万，无历史分位）｜正 Gamma 减弱（81万）｜现价位于 Flip 上方 16.77%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 172（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 212.5C — Vol 3,664 | 最新价 $2.65 | OI 297→9150 (ΔOI +8853张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8853张（+2980.8% vs前日OI），连续性待观察（方向未知）
09-25 110.0P — Vol 14 | 最新价 $0.02 | OI 1578→7977 (ΔOI +6399张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6399张（+405.5% vs前日OI），连续性待观察（方向未知）
10-16 50.0P — Vol 6,401（Yahoo补） | 最新价 $0.05 | OI 105→6477 (ΔOI +6372张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6372张（+6068.6% vs前日OI），连续性待观察（方向未知）
09-25 202.5C — Vol 1,132 | 最新价 $5.70 | OI 240→5967 (ΔOI +5727张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5727张（+2386.2% vs前日OI），连续性待观察（方向未知）
09-25 210.0C — Vol 10,519 | 最新价 $3.24 | OI 643→6234 (ΔOI +5591张) | ΔOI/Volume 53.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5591张（+869.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,942 张（Put 12,771 / Call 20,171），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-25  C +43.3k / P +24.5k ｜ Activity HIGH ｜ 4D
10-02  C +2.4k / P +9.9k ｜ Activity HIGH ｜ 11D
10-09  C +1.1k / P +4.0k ｜ Activity HIGH ｜ 18D
10-16  C +9.1k / P +17.9k ｜ Activity HIGH ｜ 25D

📆 09-25 Forward Structure
存量OI: C 75.1k / P 44.9k，今日变化ΔOI: C +43.3k / P +24.5k，平值价格ATM: C $6.85 / P $5.90 ｜ ATM IV 75.5%，净 delta 敞口 1.5M shares
Top ΔOI: C 212 +8,853 ｜ C 202 +5,727
仓位参考: Max Pain 180 ｜ Call Wall 212.5（+5.7%，弱）（OI 9.2k） ｜ Put Wall 187.5（-6.7%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 75.5%｜历史 Rank 48%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,527,766 股

📆 10-02 Forward Structure
存量OI: C 16.0k / P 27.9k，今日变化ΔOI: C +2.4k / P +9.9k，平值价格ATM: C $10.34 / P $9.00 ｜ ATM IV 68.5%，净 delta 敞口 24k shares
仓位参考: Max Pain 185 ｜ Call Wall 187.5（-6.7%，弱）（OI 1.3k） ｜ Put Wall 187.5（-6.7%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 68.5%｜历史 Rank 48%（近端代理）｜IV/RV 0.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,040 股

📆 10-09 Forward Structure
存量OI: C 4.3k / P 8.2k，今日变化ΔOI: C +1.1k / P +4.0k，平值价格ATM: C $12.70 / P $11.17 ｜ ATM IV 66.9%，净 delta 敞口 12k shares
Top ΔOI: P 190 +218
仓位参考: Max Pain 185 ｜ Call Wall 220（+9.4%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 66.9%｜历史 Rank 48%（近端代理）｜IV/RV 0.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,987 股

📆 10-16 Forward Structure
存量OI: C 71.1k / P 71.3k，今日变化ΔOI: C +9.1k / P +17.9k，平值价格ATM: C $14.72 / P $13.30 ｜ ATM IV 66.5%，净 delta 敞口 150k shares
Top ΔOI: C 240 +3,382
仓位参考: Max Pain 170 ｜ Call Wall 200（-0.5%，弱）（OI 6.2k） ｜ Put Wall 200（-0.5%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜ATM IV 66.5%｜历史 Rank 48%（近端代理）｜IV/RV 0.72×（近似）｜净 delta 敞口 正 149,935 股

📅 事件差分（观察，非因果）: 09-25（4D）ATM IV 75.5% vs 10-02 68.5%（差 +7.0pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/COIN_evening.json