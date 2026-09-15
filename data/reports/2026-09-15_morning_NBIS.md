# 期权晨报 2026-09-15（快照 10:20 ET）

📊 市场环境

SPY $759.03 ｜ QQQ $706.39
VIX 17.08 ↓0.1%（5D +8.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.6（fear）
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 212.19 → 今开 211.17（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 216.56 ｜ 低 210.61

Options: P/C成交量 0.66 | OI比 1.29 | ATM IV 86.6% | Skew -0.9pp | Term 0.92 | ExpMove ±6.7%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±6.7% ｜ 09-25（10D）±10.4% ｜ 10-02（17D）±14.1% ｜ 10-09（24D）±16.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,531,704 | GEX Change vs 上次快照 303,885 | Flip: Primary Flip: 227.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 551 / LOW 76 / INVALID 139
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 227.94（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 7.4%）
最近结构参考: Flip 228（现价低于该位 5.8%）
量化视角： 负 Gamma（853万，无历史分位）｜负 Gamma 缓解（+30万）｜现价位于 Flip 下方 5.76%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 228（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 227.5C — Vol 2,860 | 最新价 $6.13 | OI 67→2882 (ΔOI +2815张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2815张（+4201.5% vs前日OI），连续性待观察（方向未知）
09-25 130.0P — Vol 1,968 | 最新价 $0.04 | OI 603→2553 (ΔOI +1950张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1950张（+323.4% vs前日OI），连续性待观察（方向未知）
09-18 270.0C — Vol 2,250 | 最新价 $0.17 | OI 4533→5961 (ΔOI +1428张) | ΔOI/Volume 63.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1428张（+31.5% vs前日OI），连续性待观察（方向未知）
09-18 250.0C — Vol 4,495 | 最新价 $0.56 | OI 9210→10447 (ΔOI +1237张) | ΔOI/Volume 27.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1237张（+13.4% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 1,561 | 最新价 $0.08 | OI 3881→4877 (ΔOI +996张) | ΔOI/Volume 63.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增996张（+25.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,426 张（Put 2,946 / Call 5,480），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +3.0k / P +5.6k ｜ Activity HIGH ｜ 3D
09-25  C +5.1k / P +3.9k ｜ Activity HIGH ｜ 10D
10-02  C +0.4k / P +0.6k ｜ Activity MEDIUM △ ｜ 17D
10-09  C +0.3k / P +1.0k ｜ Activity MEDIUM △ ｜ 24D

📆 09-18 Forward Structure
存量OI: C 140.5k / P 181.0k，今日变化ΔOI: C +3.0k / P +5.6k，平值价格ATM: C $6.86 / P $7.45 ｜ ATM IV 86.6%，净 delta 敞口 49k shares
Top ΔOI: C 227 -1,939 ｜ C 250 +1,237
仓位参考: Max Pain 220 ｜ Call Wall 200（-6.9%，弱）（OI 7.2k） ｜ Put Wall 210（-2.2%，弱）（OI 10.4k）
量化解读： 存量 Put 重｜ATM IV 86.6%｜历史 Rank 18%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 49,308 股

📆 09-25 Forward Structure
存量OI: C 18.9k / P 21.2k，今日变化ΔOI: C +5.1k / P +3.9k，平值价格ATM: C $10.75 / P $11.50 ｜ ATM IV 78.9%，净 delta 敞口 104k shares
Top ΔOI: C 227 +2,815 ｜ P 200 +798
仓位参考: Max Pain 220 ｜ Call Wall 227.5（+5.9%）（OI 2.9k） ｜ Put Wall 200（-6.9%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 78.9%｜历史 Rank 18%（近端代理）｜净 delta 敞口 正 104,313 股

10-02（MEDIUM △）Top ΔOI: 230C +85
10-02（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 210（-2.2%，弱）（OI 0.3k） ｜ Put Wall 200（-6.9%，弱）（OI 0.6k）

10-09（MEDIUM △）Top ΔOI: 215P +295 ｜ 210P +284
10-09（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 235（+9.4%，弱）（OI 0.3k） ｜ Put Wall 200（-6.9%，弱）（OI 0.7k）

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 86.6% vs 09-25 78.9%（差 +7.7pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/NBIS_morning.json