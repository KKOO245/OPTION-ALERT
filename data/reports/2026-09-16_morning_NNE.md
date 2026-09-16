# 期权晨报 2026-09-16（快照 11:22 ET）

📊 市场环境

SPY $760.53 ｜ QQQ $710.92
VIX 16.68 ↓3.0%（5D +1.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75　⏰ 今日
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　⏰ 今日
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.78 → 今开 16.09（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 16.15 ｜ 低 15.31

Options: P/C成交量 0.67 | OI比 0.45 | ATM IV 90.0% | Skew -2.4pp | Term 0.88 | ExpMove ±6.1%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.45）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.45×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±6.1% ｜ 09-25（9D）±10.3% ｜ 10-02（16D）±12.8% ｜ 10-09（23D）±27.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 717,141 | GEX Change vs 上次快照 257,666 | Flip: Primary Flip: 14.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 156 / LOW 98 / INVALID 196
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 14.25（全链重定价，覆盖 98%）
Put Wall 15（弱结构｜现价高于该位 4.0%）
最近结构参考: Put Wall 15（现价高于该位 4.0%）
量化视角： 正 Gamma（72万，无历史分位）｜正 Gamma 增强（+26万）｜现价位于 Flip 上方 9.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 14.0P — Vol 373 | 最新价 $0.60 | OI 139→502 (ΔOI +363张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增363张（+261.1% vs前日OI），连续性待观察（方向未知）
09-18 17.0C — Vol 270 | 最新价 $0.13 | OI 369→496 (ΔOI +127张) | ΔOI/Volume 47.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+34.4% vs前日OI），连续性待观察（方向未知）
09-18 18.0C — Vol 106 | 最新价 $0.05 | OI 364→450 (ΔOI +86张) | ΔOI/Volume 81.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增86张（+23.6% vs前日OI），连续性待观察（方向未知）
09-18 17.5C — Vol 102 | 最新价 $0.05 | OI 184→260 (ΔOI +76张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增76张（+41.3% vs前日OI），连续性待观察（方向未知）
09-18 15.0P — Vol 69 | 最新价 $0.25 | OI 491→556 (ΔOI +65张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增65张（+13.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 717 张（Put 428 / Call 289），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.3k / P +44 ｜ Activity MEDIUM △ ｜ 2D
09-25  C +0.1k / P -0.1k ｜ Activity HIGH ｜ 9D
10-02  C -1 / P -41 ｜ Activity LOW ｜ 16D
10-09  C -2 / P +23 ｜ Activity LOW ｜ 23D

📆 09-18 Forward Structure
存量OI: C 9.0k / P 4.1k，今日变化ΔOI: C +0.3k / P +44，平值价格ATM: C $0.45 / P $0.50 ｜ ATM IV 90.0%，净 delta 敞口 8k shares
Top ΔOI: C 17 +127
仓位参考: Max Pain 18 ｜ Call Wall 17（+9.0%，弱）（OI 0.5k） ｜ Put Wall 16（+2.6%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 90.0%｜历史 Rank 17%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,823 股

📆 09-25 Forward Structure
存量OI: C 5.2k / P 1.7k，今日变化ΔOI: C +0.1k / P -0.1k，平值价格ATM: C $0.95 / P $0.65 ｜ ATM IV 84.0%，净 delta 敞口 10k shares
Top ΔOI: P 16 -62 ｜ P 15 -36
仓位参考: Max Pain 18 ｜ Put Wall 15（-3.8%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 84.0%｜历史 Rank 17%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,612 股

10-02（Activity LOW）仓位参考: Max Pain 19 ｜ Put Wall 15（-3.8%）（OI 0.2k）

10-09（Activity LOW）仓位参考: Max Pain 19 ｜ Put Wall 16（+2.6%）（OI 0.1k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 90.0% vs 09-25 84.0%（差 +6.0pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/NNE_morning.json