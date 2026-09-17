# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $760.90 ｜ QQQ $715.87
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-18 1650C ΔOI +493（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,519.97 → 今开 1,564.50（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 1625.35 ｜ 低 1564.50

Options: P/C成交量 0.46 | OI比 1.09 | ATM IV 76.0% | Skew -2.6pp | Term 0.90 | ExpMove ±3.7%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±3.7% ｜ 09-25（8D）±7.8% ｜ 10-02（15D）±11.4% ｜ 10-09（22D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,631,005 | GEX Change vs 上次快照 16,372,451 | Flip: Primary Flip: 1573.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1961 / LOW 523 / INVALID 892
结构观察区: Primary Flip 1573.88（全链重定价，覆盖 98%）
最近结构参考: Flip 1574（现价高于该位 2.5%）
量化视角： 正 Gamma（663万，无历史分位）｜由负转正（+1637万）｜现价位于 Flip 上方 2.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1574（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 900.0P — Vol 752 | 最新价 $0.03 | OI 1593→2380 (ΔOI +787张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增787张（+49.4% vs前日OI），连续性待观察（方向未知）
09-18 1800.0C — Vol 2,169 | 最新价 $0.45 | OI 4017→4722 (ΔOI +705张) | ΔOI/Volume 32.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增705张（+17.6% vs前日OI），连续性待观察（方向未知）
09-18 1650.0C — Vol 3,924 | 最新价 $4.20 | OI 1527→2020 (ΔOI +493张) | ΔOI/Volume 12.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增493张（+32.3% vs前日OI），连续性待观察（方向未知）
09-18 1400.0P — Vol 2,356 | 最新价 $3.40 | OI 4635→5048 (ΔOI +413张) | ΔOI/Volume 17.5% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增413张（+8.9% vs前日OI），值得跟踪（方向未知）
09-18 2510.0C — Vol 400 | 最新价 $0.05 | OI 280→680 (ΔOI +400张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增400张（+142.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,798 张（Put 1,200 / Call 1,598），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +3.4k / P +2.8k ｜ Activity MEDIUM △ ｜ 1D
09-25  C +1.4k / P +1.0k ｜ Activity HIGH ｜ 8D
10-02  C +0.3k / P +0.4k ｜ Activity MEDIUM △ ｜ 15D
10-09  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 09-18 Forward Structure
存量OI: C 94.4k / P 103.2k，今日变化ΔOI: C +3.4k / P +2.8k，平值价格ATM: C $27.00 / P $33.00 ｜ ATM IV 76.0%，净 delta 敞口 187k shares
Top ΔOI: C 1650 +493
仓位参考: Max Pain 1,500 ｜ Call Wall 1750（+8.5%，弱）（OI 3.7k） ｜ Put Wall 1500（-7.0%，弱）（OI 3.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.0%｜历史 Rank 30%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 186,750 股

📆 09-25 Forward Structure
存量OI: C 15.6k / P 20.5k，今日变化ΔOI: C +1.4k / P +1.0k，平值价格ATM: C $61.00 / P $65.46 ｜ ATM IV 66.6%，净 delta 敞口 33k shares
Top ΔOI: C 1705 +143 ｜ C 1625 +137 ｜ C 1700 +119
仓位参考: Max Pain 1,575 ｜ Call Wall 1700（+5.4%，弱）（OI 0.7k） ｜ Put Wall 1500（-7.0%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.6%｜历史 Rank 30%（近端代理）｜净 delta 敞口 正 33,341 股

10-02（MEDIUM △）Top ΔOI: 1280P +87 ｜ 1700C +62
10-02（MEDIUM △）仓位参考: Max Pain 1,580 ｜ Call Wall 1600（-0.8%，弱）（OI 0.5k） ｜ Put Wall 1500（-7.0%，弱）（OI 0.4k）

10-09（MEDIUM △）Top ΔOI: 1320P +37 ｜ 1310P +24
10-09（MEDIUM △）仓位参考: Max Pain 1,610 ｜ Call Wall 1750（+8.5%，弱）（OI 0.1k） ｜ Put Wall 1500（-7.0%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 76.0% vs 09-25 66.6%（差 +9.4pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/SNDK_morning.json