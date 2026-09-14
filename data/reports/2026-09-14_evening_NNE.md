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
🟡 **单日价格波动**: -4.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 15.85 → 收盘 15.89（+0.3%） ｜ 今日高 16.24 ｜ 低 15.70 ｜ 昨收 16.41 → 收盘 15.89（-3.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.20 | OI比 0.49 | ATM IV 85.1% | Skew -2.4pp | Term 0.93 | ExpMove ±7.2%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.20×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±7.2% ｜ 09-25（11D）±12.1% ｜ 10-02（18D）±24.6% ｜ 10-09（25D）±16.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 357,075 | GEX Change vs 上次快照 379,962 | Flip: Primary Flip: 15.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 217 / LOW 90 / INVALID 143
结构观察区: Primary Flip 15.29（全链重定价，覆盖 99%）
Put Wall 15（弱结构｜现价高于该位 5.9%）
最近结构参考: Flip 15（现价高于该位 3.9%）
量化视角： 正 Gamma（36万，无历史分位）｜由负转正（+38万）｜现价位于 Flip 上方 3.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 21.0C — Vol 16（Yahoo补） | 最新价 $0.40 | OI 153→2611 (ΔOI +2458张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2458张（+1606.5% vs前日OI），连续性待观察（方向未知）
10-02 15.0P — Vol 7（Yahoo补） | 最新价 $0.47 | OI 43→325 (ΔOI +282张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增282张（+655.8% vs前日OI），值得跟踪（方向未知）
09-25 15.5P — Vol 189（Yahoo补） | 最新价 $0.40 | OI 37→226 (ΔOI +189张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增189张（+510.8% vs前日OI），连续性待观察（方向未知）
09-25 17.0P — Vol 5（Yahoo补） | 最新价 $0.98 | OI 95→268 (ΔOI +173张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增173张（+182.1% vs前日OI），值得跟踪（方向未知）
10-02 20.0C — Vol 31 | 最新价 $0.15 | OI 77→216 (ΔOI +139张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增139张（+180.5% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,241 张（Put 644 / Call 2,597），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 7.9k / P 3.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.60 / P $0.55 ｜ ATM IV 85.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 19 ｜ Put Wall 16（+0.7%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 85.2%｜历史 Rank 12%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 17（+7.0%，弱）（OI 0.3k）

10-02（Activity LOW）仓位参考: Max Pain 19 ｜ Put Wall 15（-5.6%）（OI 0.3k）

10-09（Activity LOW）仓位参考: Max Pain 19 ｜ Put Wall 16（+0.7%）（OI 66）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 85.2% vs 09-25 77.9%（差 +7.2pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/NNE_evening.json