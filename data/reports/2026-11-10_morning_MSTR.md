# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.55
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 95.1% vs 11-20 82.8%（差 +12.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 130C ΔOI +1,615（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 125.59 → 今开 121.95（-2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 126.40 ｜ 低 119.70

Options: P/C成交量 1.11 | OI比 0.63 | ATM IV 95.1% | Skew 5.7pp | Term 0.79 | ExpMove ±7.2%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 5.7pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±7.2% ｜ 11-20（10D）±11.1% ｜ 11-27（17D）±13.1% ｜ 12-04（24D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,726,215 | GEX Change vs 上次快照 1,847,489 | Flip: Primary Flip: 119.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 561 / LOW 166 / INVALID 255
结构观察区: Primary Flip 119.27（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价低于该位 7.2%）
最近结构参考: Flip 119（现价高于该位 5.1%）
量化视角： 正 Gamma（3673万，无历史分位）｜正 Gamma 增强（+185万）｜现价位于 Flip 上方 5.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 130（MaxPain，仅结算参考） / 135（Call Wall，弱结构）。
• Gamma 区域：切换参考 119（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 135.0C — Vol 9,353 | 最新价 $1.57 | OI 7443→10821 (ΔOI +3378张) | ΔOI/Volume 36.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3378张（+45.4% vs前日OI），连续性待观察（方向未知）
11-13 160.0C — Vol 2,599 | 最新价 $0.08 | OI 3116→4732 (ΔOI +1616张) | ΔOI/Volume 62.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1616张（+51.9% vs前日OI），连续性待观察（方向未知）
11-13 130.0C — Vol 5,702 | 最新价 $3.03 | OI 1106→2721 (ΔOI +1615张) | ΔOI/Volume 28.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1615张（+146.0% vs前日OI），连续性待观察（方向未知）
11-13 133.0C — Vol 2,950 | 最新价 $2.05 | OI 43164→44621 (ΔOI +1457张) | ΔOI/Volume 49.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1457张（+3.4% vs前日OI），连续性待观察（方向未知）
11-13 106.0P — Vol 1,121 | 最新价 $0.43 | OI 992→2053 (ΔOI +1061张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1061张（+107.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,127 张（Put 1,061 / Call 8,066），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +16.5k / P -0.4k ｜ Activity MEDIUM △ ｜ 3D
11-20  C +3.3k / P +2.7k ｜ Activity HIGH ｜ 10D
11-27  C +1.2k / P +2.3k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +1.0k / P +3.6k ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 230.3k / P 145.1k，今日变化ΔOI: C +16.5k / P -0.4k，平值价格ATM: C $4.55 / P $4.49 ｜ ATM IV 95.1%，净 delta 敞口 777k shares
Top ΔOI: C 135 +3,378 ｜ C 130 +1,615
仓位参考: Max Pain 130 ｜ Call Wall 133（+6.1%，弱）（OI 44.6k）
量化解读： 存量 Call 重｜ATM IV 95.1%｜历史 Rank 74%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 776,591 股

📆 11-20 Forward Structure
存量OI: C 164.4k / P 149.7k，今日变化ΔOI: C +3.3k / P +2.7k，平值价格ATM: C $7.25 / P $6.70 ｜ ATM IV 82.8%，净 delta 敞口 191k shares
Top ΔOI: C 137 +576
仓位参考: Max Pain 135 ｜ Call Wall 135（+7.7%）（OI 43.4k） ｜ Put Wall 120（-4.2%，弱）（OI 10.9k）
量化解读： 存量两侧均衡｜ATM IV 82.8%｜历史 Rank 74%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 191,259 股

11-27（MEDIUM △）Top ΔOI: 120P -858 ｜ 95P +649
11-27（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 130（+3.8%，弱）（OI 0.8k） ｜ Put Wall 135（+7.7%，弱）（OI 2.6k）

12-04（MEDIUM △）Top ΔOI: 85P +847 ｜ 135C +462
12-04（MEDIUM △）仓位参考: Max Pain 150 ｜ Put Wall 135（+7.7%，弱）（OI 1.9k）

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 95.1% vs 11-20 82.8%（差 +12.3pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/MSTR_morning.json