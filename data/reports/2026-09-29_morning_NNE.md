# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.86 ｜ QQQ $738.93
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
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
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 15P ΔOI +202（距现价 -4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 16.16 → 今开 16.55（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 16.60 ｜ 低 16.20

Options: P/C成交量 1.07 | OI比 0.46 | ATM IV 70.5% | Skew -8.0pp | Term 1.08 | ExpMove ±6.9%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -8.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±6.9% ｜ 10-09（10D）±9.8% ｜ 10-16（17D）±13.2% ｜ 10-23（24D）±16.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,024,306 | GEX Change vs 上次快照 8,128 | Flip: Primary Flip: 15.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 200 / LOW 82 / INVALID 154
结构观察区: Primary Flip 15.42（全链重定价，覆盖 96%）
Put Wall 15（弱结构｜现价高于该位 8.4%）
最近结构参考: Flip 15（现价高于该位 5.4%）
量化视角： 正 Gamma（102万，无历史分位）｜正 Gamma 增强（+1万）｜现价位于 Flip 上方 5.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 15.0P — Vol 286 | 最新价 $0.35 | OI 51→326 (ΔOI +275张) | ΔOI/Volume 96.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增275张（+539.2% vs前日OI），连续性待观察（方向未知）
10-02 15.5P — Vol 206 | 最新价 $0.27 | OI 162→364 (ΔOI +202张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增202张（+124.7% vs前日OI），连续性待观察（方向未知）
10-02 17.5C — Vol 221 | 最新价 $0.12 | OI 74→275 (ΔOI +201张) | ΔOI/Volume 91.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增201张（+271.6% vs前日OI），连续性待观察（方向未知）
10-30 14.0P — Vol 180 | 最新价 $0.50 | OI 90→270 (ΔOI +180张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增180张（+200.0% vs前日OI），连续性待观察（方向未知）
10-02 18.0C — Vol 180 | 最新价 $0.10 | OI 493→640 (ΔOI +147张) | ΔOI/Volume 81.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增147张（+29.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,005 张（Put 657 / Call 348），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 3D
10-09  C +55 / P +0.2k ｜ Activity HIGH ｜ 10D
10-16  C +64 / P +36 ｜ Activity MEDIUM △ ｜ 17D
10-23  C +5 / P +0.1k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 5.1k / P 2.3k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $0.42 / P $0.70 ｜ ATM IV 70.5%，净 delta 敞口 -2k shares
Top ΔOI: P 15 +202 ｜ C 17 +201
仓位参考: Max Pain 17 ｜ Put Wall 15.5（-4.7%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 70.5%｜历史 Rank 2%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,529 股

📆 10-09 Forward Structure
存量OI: C 5.0k / P 1.3k，今日变化ΔOI: C +55 / P +0.2k，平值价格ATM: C $0.65 / P $0.95 ｜ ATM IV 73.1%，净 delta 敞口 -11k shares
Top ΔOI: P 15 +275
仓位参考: Max Pain 18 ｜ Put Wall 15（-7.7%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.1%｜历史 Rank 2%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 10,810 股

10-16（MEDIUM △）Top ΔOI: 16P +31
10-16（MEDIUM △）仓位参考: Max Pain 20 ｜ Put Wall 15（-7.7%，弱）（OI 0.8k）

📆 10-23 Forward Structure
存量OI: C 4.7k / P 0.7k，今日变化ΔOI: C +5 / P +0.1k，平值价格ATM: C $1.40 / P $1.25 ｜ ATM IV 79.0%，净 delta 敞口 -6k shares
Top ΔOI: P 17 +40 ｜ P 17 +31 ｜ P 16 +19
仓位参考: Max Pain 18 ｜ Put Wall 16（-1.6%）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.0%｜历史 Rank 2%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 5,629 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/NNE_morning.json