# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $761.06 ｜ QQQ $709.18
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
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

🔍 重点速览
🟡 **单日价格波动**: +3.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-18 ATM IV 87.2% vs 09-25 75.4%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-18 139C ΔOI +21,101（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 130.97 → 今开 130.88（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 136.54 ｜ 低 130.73

Options: P/C成交量 0.37 | OI比 0.59 | ATM IV 87.2% | Skew -9.2pp | Term 0.84 | ExpMove ±7.6%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±7.6% ｜ 09-25（11D）±10.6% ｜ 10-02（18D）±12.9% ｜ 10-09（25D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,587,095 | GEX Change vs 上次快照 45,064,718 | Flip: Primary Flip: 115.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 871 / LOW 92 / INVALID 235
结构观察区: Primary Flip 115.49（全链重定价，覆盖 100%）
最近结构参考: Flip 115（现价高于该位 16.8%）
量化视角： 正 Gamma（7459万，无历史分位）｜正 Gamma 增强（+4506万）｜现价位于 Flip 上方 16.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 115（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 145.0C — Vol 28,387 | 最新价 $1.18 | OI 4231→26290 (ΔOI +22059张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22059张（+521.4% vs前日OI），连续性待观察（方向未知）
09-18 139.0C — Vol 21,845 | 最新价 $2.25 | OI 93→21194 (ΔOI +21101张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21101张（+22689.2% vs前日OI），连续性待观察（方向未知）
09-18 141.0C — Vol 17,061 | 最新价 $1.78 | OI 789→17459 (ΔOI +16670张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16670张（+2112.8% vs前日OI），连续性待观察（方向未知）
09-18 135.0C — Vol 22,738 | 最新价 $3.30 | OI 6882→22476 (ΔOI +15594张) | ΔOI/Volume 68.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15594张（+226.6% vs前日OI），连续性待观察（方向未知）
09-18 140.0C — Vol 24,566 | 最新价 $1.95 | OI 10342→25054 (ΔOI +14712张) | ΔOI/Volume 59.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14712张（+142.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 90,136 张（Put 0 / Call 90,136），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +164.6k / P +37.0k ｜ Activity HIGH ｜ 4D
09-25  C +2.9k / P +7.9k ｜ Activity HIGH ｜ 11D
10-02  C +2.1k / P +3.5k ｜ Activity MEDIUM △ ｜ 18D
10-09  C +0.3k / P +2.6k ｜ Activity MEDIUM △ ｜ 25D

📆 09-18 Forward Structure
存量OI: C 460.5k / P 273.9k，今日变化ΔOI: C +164.6k / P +37.0k，平值价格ATM: C $5.25 / P $4.95 ｜ ATM IV 87.2%，净 delta 敞口 6.1M shares
Top ΔOI: C 145 +22,059 ｜ C 139 +21,101 ｜ C 141 +16,670
仓位参考: Max Pain 120
量化解读： 存量 Call 重｜ATM IV 87.2%｜历史 Rank 61%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,067,182 股

📆 09-25 Forward Structure
存量OI: C 25.5k / P 50.0k，今日变化ΔOI: C +2.9k / P +7.9k，平值价格ATM: C $7.35 / P $7.00 ｜ ATM IV 75.4%，净 delta 敞口 39k shares
Top ΔOI: C 160 +741
仓位参考: Max Pain 126
量化解读： 存量 Put 重｜ATM IV 75.4%｜历史 Rank 61%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,068 股

10-02（MEDIUM △）Top ΔOI: 142C +534
10-02（MEDIUM △）仓位参考: Max Pain 130 ｜ Call Wall 145（+7.5%，弱）（OI 2.7k）

10-09（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 130（-3.6%，弱）（OI 2.0k）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 87.2% vs 09-25 75.4%（差 +11.8pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/MSTR_morning.json