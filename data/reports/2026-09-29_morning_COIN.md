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
🟡 **事件差分**: 10-02 ATM IV 73.7% vs 10-09 63.7%（差 +10.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 191.79 → 今开 197.41（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 197.63 ｜ 低 191.92

Options: P/C成交量 0.37 | OI比 0.60 | ATM IV 73.7% | Skew -3.8pp | Term 0.91 | ExpMove ±5.5%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -3.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±5.5% ｜ 10-09（10D）±8.7% ｜ 10-16（17D）±11.2% ｜ 10-23（24D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 20,726,851 | GEX Change vs 上次快照 2,400,214 | Flip: Primary Flip: 177.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 524 / LOW 119 / INVALID 241
结构观察区: Primary Flip 177.92（全链重定价，覆盖 100%）
Call Wall 202（弱结构｜现价低于该位 4.9%）
最近结构参考: Call Wall 202（现价低于该位 4.9%）
量化视角： 正 Gamma（2073万，无历史分位）｜正 Gamma 增强（+240万）｜现价位于 Flip 上方 8.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考）；上方 202（Call Wall，弱结构）。
• Gamma 区域：切换参考 178（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 205.0C — Vol 1,960 | 最新价 $1.72 | OI 2956→3665 (ΔOI +709张) | ΔOI/Volume 36.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增709张（+24.0% vs前日OI），连续性待观察（方向未知）
10-02 210.0C — Vol 3,537 | 最新价 $1.08 | OI 6215→6873 (ΔOI +658张) | ΔOI/Volume 18.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增658张（+10.6% vs前日OI），连续性待观察（方向未知）
10-02 230.0C — Vol 936 | 最新价 $0.18 | OI 794→1366 (ΔOI +572张) | ΔOI/Volume 61.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增572张（+72.0% vs前日OI），连续性待观察（方向未知）
10-02 200.0C — Vol 2,876 | 最新价 $2.83 | OI 2269→2832 (ΔOI +563张) | ΔOI/Volume 19.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增563张（+24.8% vs前日OI），连续性待观察（方向未知）
10-16 110.0P — Vol 500 | 最新价 $0.07 | OI 10431→10931 (ΔOI +500张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增500张（+4.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,002 张（Put 500 / Call 2,502），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +5.5k / P +2.5k ｜ Activity MEDIUM △ ｜ 3D
10-09  C +1.1k / P +1.1k ｜ Activity MEDIUM △ ｜ 10D
10-16  C +0.5k / P +0.9k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +0.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 71.3k / P 42.9k，今日变化ΔOI: C +5.5k / P +2.5k，平值价格ATM: C $5.25 / P $5.24 ｜ ATM IV 73.7%，净 delta 敞口 71k shares
Top ΔOI: C 205 +709 ｜ C 210 +658
仓位参考: Max Pain 190 ｜ Call Wall 202.5（+5.1%，弱）（OI 16.1k） ｜ Put Wall 190（-1.4%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 73.7%｜历史 Rank 42%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 70,780 股

10-09（MEDIUM △）Top ΔOI: 200C +364
10-09（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 200（+3.8%）（OI 1.8k）

10-16（MEDIUM △）Top ΔOI: 180P +265
10-16（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+3.8%，弱）（OI 6.3k） ｜ Put Wall 200（+3.8%，弱）（OI 3.9k）

10-23（MEDIUM △）Top ΔOI: 187C +355 ｜ 192P +349
10-23（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 187.5（-2.7%，弱）（OI 0.4k） ｜ Put Wall 192.5（-0.1%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 73.7% vs 10-09 63.7%（差 +10.0pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/COIN_morning.json