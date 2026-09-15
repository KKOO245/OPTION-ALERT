# 期权晚报 2026-09-15（快照 16:40 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $704.54
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-18 140C ΔOI -747（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 139.15 → 收盘 141.90（+2.0%） ｜ 今日高 147.56 ｜ 低 139.00 ｜ 昨收 142.35 → 收盘 141.90（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.50 | OI比 0.96 | ATM IV 62.1% | Skew -0.4pp | Term 0.87 | ExpMove ±4.5%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（3D）±4.5% ｜ 09-25（10D）±7.5% ｜ 10-02（17D）±9.9% ｜ 10-09（24D）±11.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,445,944 | GEX Change vs 上次快照 -639,727 | Flip: Primary Flip: 125.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 613 / LOW 85 / INVALID 104
结构观察区: Primary Flip 125.22（全链重定价，覆盖 100%）
Call Wall 150（弱结构｜现价低于该位 5.4%）
最近结构参考: Call Wall 150（现价低于该位 5.4%）
量化视角： 正 Gamma（2345万，无历史分位）｜正 Gamma 减弱（64万）｜现价位于 Flip 上方 13.32%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 125（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 165.0C — Vol 380 | 最新价 $2.37 | OI 863→2072 (ΔOI +1209张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1209张（+140.1% vs前日OI），连续性待观察（方向未知）
09-18 155.0C — Vol 2,021 | 最新价 $0.32 | OI 1930→2471 (ΔOI +541张) | ΔOI/Volume 26.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增541张（+28.0% vs前日OI），连续性待观察（方向未知）
10-16 125.0C — Vol 641 | 最新价 $20.05 | OI 2589→3092 (ΔOI +503张) | ΔOI/Volume 78.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增503张（+19.4% vs前日OI），连续性待观察（方向未知）
10-16 145.0C — Vol 593 | 最新价 $7.80 | OI 2500→3002 (ΔOI +502张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增502张（+20.1% vs前日OI），连续性待观察（方向未知）
10-16 200.0C — Vol 2,126 | 最新价 $0.32 | OI 3128→3627 (ΔOI +499张) | ΔOI/Volume 23.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增499张（+15.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,254 张（Put 0 / Call 3,254），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +1.9k / P +1.3k ｜ Activity MEDIUM △ ｜ 3D
09-25  C +2.7k / P +0.7k ｜ Activity HIGH ｜ 10D
10-02  C +0.7k / P +0.4k ｜ Activity HIGH ｜ 17D
10-09  C +0.7k / P -0.2k ｜ Activity HIGH ｜ 24D

📆 09-18 Forward Structure
存量OI: C 114.6k / P 110.1k，今日变化ΔOI: C +1.9k / P +1.3k，平值价格ATM: C $3.16 / P $3.30 ｜ ATM IV 62.1%，净 delta 敞口 -130k shares
Top ΔOI: C 140 -747 ｜ C 141 -708 ｜ C 155 +541
仓位参考: Max Pain 120 ｜ Call Wall 140（-1.3%，弱）（OI 7.4k）
量化解读： 存量两侧均衡｜ATM IV 62.1%｜历史 Rank 57%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 130,324 股

📆 09-25 Forward Structure
存量OI: C 12.1k / P 9.4k，今日变化ΔOI: C +2.7k / P +0.7k，平值价格ATM: C $5.53 / P $5.09 ｜ ATM IV 55.1%，净 delta 敞口 60k shares
Top ΔOI: C 141 +494 ｜ C 150 +366
仓位参考: Max Pain 133 ｜ Call Wall 145（+2.2%，弱）（OI 1.9k） ｜ Put Wall 130（-8.4%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 55.1%｜历史 Rank 57%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,624 股

📆 10-02 Forward Structure
存量OI: C 8.3k / P 8.1k，今日变化ΔOI: C +0.7k / P +0.4k，平值价格ATM: C $7.30 / P $6.75 ｜ ATM IV 54.5%，净 delta 敞口 6k shares
Top ΔOI: C 155 +157
仓位参考: Max Pain 132 ｜ Call Wall 150（+5.7%，弱）（OI 1.5k） ｜ Put Wall 130（-8.4%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 54.5%｜历史 Rank 57%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,020 股

📆 10-09 Forward Structure
存量OI: C 2.3k / P 3.9k，今日变化ΔOI: C +0.7k / P -0.2k，平值价格ATM: C $9.99 / P $5.95 ｜ ATM IV 53.8%，净 delta 敞口 31k shares
仓位参考: Max Pain 138 ｜ Call Wall 155（+9.2%，弱）（OI 0.2k） ｜ Put Wall 140（-1.3%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 53.8%｜历史 Rank 57%（近端代理）｜净 delta 敞口 正 31,031 股

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 62.1% vs 09-25 55.1%（差 +7.0pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/NOW_evening.json