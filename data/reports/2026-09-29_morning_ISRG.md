# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 417C ΔOI +183（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 414.79 → 今开 411.90（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 414.20 ｜ 低 407.07

Options: P/C成交量 0.12 | OI比 1.58 | ATM IV 41.4% | Skew 2.6pp | Term 1.05 | ExpMove ±2.8%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常（Term 1.05）｜保护溢价中性（Skew 2.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.12×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.58×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±2.8% ｜ 10-09（10D）±3.3% ｜ 10-16（17D）±5.5% ｜ 10-23（24D）±9.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,488,294 | GEX Change vs 上次快照 -525,669 | Flip: Primary Flip: 386.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 292 / LOW 149 / INVALID 421
结构观察区: Primary Flip 386.85（全链重定价，覆盖 97%）
Call Wall 420（弱结构｜现价低于该位 2.9%）
最近结构参考: Call Wall 420（现价低于该位 2.9%）
量化视角： 正 Gamma（249万，无历史分位）｜正 Gamma 减弱（53万）｜现价位于 Flip 上方 5.39%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 387（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 417.5C — Vol 201 | 最新价 $6.40 | OI 13→196 (ΔOI +183张) | ΔOI/Volume 91.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增183张（+1407.7% vs前日OI），连续性待观察（方向未知）
10-02 420.0C — Vol 202 | 最新价 $4.25 | OI 194→259 (ΔOI +65张) | ΔOI/Volume 32.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增65张（+33.5% vs前日OI），连续性待观察（方向未知）
10-02 425.0C — Vol 176 | 最新价 $2.80 | OI 41→98 (ΔOI +57张) | ΔOI/Volume 32.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增57张（+139.0% vs前日OI），连续性待观察（方向未知）
10-16 417.5P — Vol 52 | 最新价 $14.00 | OI 0→52 (ΔOI +52张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增52张（前日OI缺失），值得跟踪（方向未知）
10-02 430.0C — Vol 99 | 最新价 $1.60 | OI 31→82 (ΔOI +51张) | ΔOI/Volume 51.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增51张（+164.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 408 张（Put 52 / Call 356），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.5k / P +94 ｜ Activity HIGH ｜ 3D
10-09  C +77 / P +21 ｜ Activity MEDIUM △ ｜ 10D
10-16  C +8 / P -20 ｜ Activity MEDIUM △ ｜ 17D
10-23  C +54 / P +86 ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 2.1k / P 3.4k，今日变化ΔOI: C +0.5k / P +94，平值价格ATM: C $6.91 / P $4.30 ｜ ATM IV 41.4%，净 delta 敞口 6k shares
Top ΔOI: C 417 +183 ｜ C 420 +65 ｜ C 425 +57
仓位参考: Max Pain 390 ｜ Call Wall 410（+0.6%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.4%｜历史 Rank 55%（近端代理）｜IV/RV 1.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 5,551 股

10-09（MEDIUM △）Top ΔOI: 430C +38 ｜ 435C +32
10-09（MEDIUM △）仓位参考: Max Pain 370 ｜ Call Wall 420（+3.0%，弱）（OI 0.1k） ｜ Put Wall 370（-9.2%，弱）（OI 17）

10-16（MEDIUM △）Top ΔOI: 400C -59 ｜ 417P +52
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-1.9%，弱）（OI 0.9k） ｜ Put Wall 380（-6.8%，弱）（OI 0.6k）

10-23（MEDIUM △）Top ΔOI: 415P +19 ｜ 415C +13
10-23（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 415（+1.8%，弱）（OI 75） ｜ Put Wall 420（+3.0%，弱）（OI 92）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 41.4% vs 10-09 34.2%（差 +7.2pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/ISRG_morning.json