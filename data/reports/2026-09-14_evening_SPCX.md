# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 147.24 → 收盘 148.15（+0.6%） ｜ 今日高 152.56 ｜ 低 146.61 ｜ 昨收 151.21 → 收盘 148.15（-2.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.49 | OI比 0.83 | ATM IV 58.4% | Skew 1.1pp | Term 0.86 | ExpMove ±4.9%（近端） | Rank 41%
量化视角： IV 中性（Rank 41%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±4.9% ｜ 09-25（11D）±7.2% ｜ 10-02（18D）±9.2% ｜ 10-09（25D）±10.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 59,729,937 | GEX Change vs 上次快照 -3,667,713 | Flip: Primary Flip: 142.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 631 / LOW 122 / INVALID 303
结构观察区: Primary Flip 142.56（全链重定价，覆盖 99%）
Call Wall 150（弱结构｜现价低于该位 1.2%）
最近结构参考: Call Wall 150（现价低于该位 1.2%）
量化视角： 正 Gamma（5973万，无历史分位）｜正 Gamma 减弱（367万）｜现价位于 Flip 上方 3.92%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 157.5C — Vol 10,530 | 最新价 $0.82 | OI 3742→14173 (ΔOI +10431张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10431张（+278.8% vs前日OI），连续性待观察（方向未知）
09-18 90.0P — Vol 1,118 | 最新价 $0.01 | OI 19078→28060 (ΔOI +8982张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8982张（+47.1% vs前日OI），连续性待观察（方向未知）
09-18 160.0C — Vol 31,648 | 最新价 $0.53 | OI 32127→40244 (ΔOI +8117张) | ΔOI/Volume 25.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8117张（+25.3% vs前日OI），连续性待观察（方向未知）
10-16 145.0C — Vol 4,340 | 最新价 $10.70 | OI 6790→11452 (ΔOI +4662张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4662张（+68.7% vs前日OI），连续性待观察（方向未知）
09-18 139.0P — Vol 1,745 | 最新价 $0.80 | OI 1625→5850 (ΔOI +4225张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4225张（+260.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,417 张（Put 13,207 / Call 23,210），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 630.1k / P 526.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.73 / P $3.55 ｜ ATM IV 58.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 145 ｜ Call Wall 155（+4.6%，弱）（OI 56.9k） ｜ Put Wall 150（+1.2%，弱）（OI 46.1k）
量化解读： 存量 Call 重｜ATM IV 58.4%｜历史 Rank 41%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 145 ｜ Call Wall 160（+8.0%，弱）（OI 5.9k） ｜ Put Wall 135（-8.9%，弱）（OI 3.2k）

10-02（Activity LOW）仓位参考: Max Pain 145 ｜ Call Wall 150（+1.2%，弱）（OI 2.9k）

10-09（Activity LOW）仓位参考: Max Pain 147 ｜ Call Wall 160（+8.0%，弱）（OI 1.0k） ｜ Put Wall 135（-8.9%）（OI 2.8k）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 58.4% vs 09-25 52.5%（差 +6.0pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/SPCX_evening.json