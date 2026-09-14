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

🔍 重点速览
🟡 **单日价格波动**: +4.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-18 ATM IV 86.7% vs 09-25 74.6%（差 +12.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 130.88 → 收盘 136.94（+4.6%） ｜ 今日高 137.51 ｜ 低 130.73 ｜ 昨收 130.97 → 收盘 136.94（+4.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 0.59 | ATM IV 86.7% | Skew -6.7pp | Term 0.83 | ExpMove ±7.4%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±7.4% ｜ 09-25（11D）±10.3% ｜ 10-02（18D）±12.4% ｜ 10-09（25D）±15.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 80,974,140 | GEX Change vs 上次快照 6,387,045 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 849 / LOW 105 / INVALID 244
结构观察区: NO_CROSS
量化视角： 正 Gamma（8097万，无历史分位）｜正 Gamma 增强（+639万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 145.0C — Vol 6,306 | 最新价 $2.29 | OI 4231→26290 (ΔOI +22059张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22059张（+521.4% vs前日OI），连续性待观察（方向未知）
09-18 139.0C — Vol 3,934 | 最新价 $4.15 | OI 93→21194 (ΔOI +21101张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21101张（+22689.2% vs前日OI），连续性待观察（方向未知）
09-18 141.0C — Vol 1,090 | 最新价 $3.40 | OI 789→17459 (ΔOI +16670张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16670张（+2112.8% vs前日OI），连续性待观察（方向未知）
09-18 135.0C — Vol 6,162 | 最新价 $5.99 | OI 6882→22476 (ΔOI +15594张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15594张（+226.6% vs前日OI），连续性待观察（方向未知）
09-18 140.0C — Vol 14,118 | 最新价 $3.76 | OI 10342→25054 (ΔOI +14712张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14712张（+142.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 90,136 张（Put 0 / Call 90,136），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 460.5k / P 273.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.00 / P $5.13 ｜ ATM IV 86.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 120 ｜ Call Wall 145（+5.9%，弱）（OI 26.3k） ｜ Put Wall 125（-8.7%，弱）（OI 8.5k）
量化解读： 存量 Call 重｜ATM IV 86.7%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 126 ｜ Call Wall 140（+2.2%，弱）（OI 1.9k） ｜ Put Wall 125（-8.7%，弱）（OI 2.3k）

10-02（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 145（+5.9%，弱）（OI 2.7k） ｜ Put Wall 130（-5.1%，弱）（OI 2.4k）

10-09（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 130（-5.1%，弱）（OI 0.3k） ｜ Put Wall 130（-5.1%，弱）（OI 2.0k）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 86.7% vs 09-25 74.6%（差 +12.1pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/MSTR_evening.json