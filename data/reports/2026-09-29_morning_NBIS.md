# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.73 ｜ QQQ $737.93
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
🟡 **事件差分**: 10-02 ATM IV 91.7% vs 10-09 81.0%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 237C ΔOI +1,314（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 231.88 → 今开 235.01（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 242.98 ｜ 低 233.61

Options: P/C成交量 0.43 | OI比 0.73 | ATM IV 91.7% | Skew -1.4pp | Term 0.86 | ExpMove ±7.1%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±7.1% ｜ 10-09（10D）±10.9% ｜ 10-16（17D）±13.9% ｜ 10-23（24D）±16.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,744,330 | GEX Change vs 上次快照 5,997,166 | Flip: Primary Flip: 223.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 533 / LOW 34 / INVALID 131
结构观察区: Primary Flip 223.54（全链重定价，覆盖 100%）
最近结构参考: Flip 224（现价高于该位 7.1%）
量化视角： 正 Gamma（1174万，无历史分位）｜正 Gamma 增强（+600万）｜现价位于 Flip 上方 7.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 224（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 130.0P — Vol 2,058 | 最新价 $0.01 | OI 647→2460 (ΔOI +1813张) | ΔOI/Volume 88.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1813张（+280.2% vs前日OI），连续性待观察（方向未知）
10-02 237.5C — Vol 2,298 | 最新价 $6.12 | OI 335→1649 (ΔOI +1314张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1314张（+392.2% vs前日OI），连续性待观察（方向未知）
10-02 210.0P — Vol 2,030 | 最新价 $1.46 | OI 3271→4558 (ΔOI +1287张) | ΔOI/Volume 63.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1287张（+39.4% vs前日OI），连续性待观察（方向未知）
10-16 250.0C — Vol 3,284 | 最新价 $9.70 | OI 3779→5015 (ΔOI +1236张) | ΔOI/Volume 37.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1236张（+32.7% vs前日OI），连续性待观察（方向未知）
10-02 250.0C — Vol 5,810 | 最新价 $2.69 | OI 3628→4696 (ΔOI +1068张) | ΔOI/Volume 18.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1068张（+29.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,718 张（Put 3,100 / Call 3,618），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +9.5k / P +7.4k ｜ Activity HIGH ｜ 3D
10-09  C +0.7k / P +2.5k ｜ Activity HIGH ｜ 10D
10-16  C +0.4k / P +2.4k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 57.8k / P 42.2k，今日变化ΔOI: C +9.5k / P +7.4k，平值价格ATM: C $8.10 / P $8.92 ｜ ATM IV 91.7%，净 delta 敞口 230k shares
Top ΔOI: C 237 +1,314 ｜ P 210 +1,287 ｜ C 250 +1,068
仓位参考: Max Pain 230 ｜ Call Wall 235（-1.8%）（OI 7.3k） ｜ Put Wall 220（-8.1%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 91.7%｜历史 Rank 29%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 230,019 股

📆 10-09 Forward Structure
存量OI: C 17.6k / P 16.4k，今日变化ΔOI: C +0.7k / P +2.5k，平值价格ATM: C $12.75 / P $13.30 ｜ ATM IV 81.0%，净 delta 敞口 13k shares
Top ΔOI: C 275 -427 ｜ C 245 +322
仓位参考: Max Pain 222 ｜ Call Wall 240（+0.3%，弱）（OI 2.1k） ｜ Put Wall 225（-6.0%，弱）（OI 1.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.0%｜历史 Rank 29%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,402 股

10-16（MEDIUM △）Top ΔOI: 300C -2,270 ｜ 250C +1,236
10-16（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 240（+0.3%，弱）（OI 5.2k） ｜ Put Wall 220（-8.1%，弱）（OI 3.1k）

10-23（MEDIUM △）Top ΔOI: 330C +250 ｜ 215P +108
10-23（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 240（+0.3%，弱）（OI 0.4k） ｜ Put Wall 220（-8.1%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 91.7% vs 10-09 81.0%（差 +10.7pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/NBIS_morning.json