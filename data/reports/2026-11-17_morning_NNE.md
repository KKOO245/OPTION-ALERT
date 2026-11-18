# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $737.42 ｜ QQQ $nan
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（3D）ATM IV 104.2% vs 11-27 87.5%（差 +16.7pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 11C ΔOI +53（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 10.74 → 今开 10.69（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 10.77 ｜ 低 10.30

Options: P/C成交量 0.19 | OI比 0.31 | ATM IV 104.2% | Skew 21.4pp | Term 0.87 | ExpMove ±8.7%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价显著（Skew 21.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±8.7% ｜ 11-27（10D）±4.7% ｜ 12-04（17D）±18.5% ｜ 12-11（24D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 824,204 | GEX Change vs 上次快照 -4,406 | Flip: Primary Flip: 9.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 162 / LOW 61 / INVALID 141
结构观察区: Primary Flip 9.02（全链重定价，覆盖 99%）
Put Wall 10（弱结构｜现价高于该位 5.7%）
最近结构参考: Put Wall 10（现价高于该位 5.7%）
量化视角： 正 Gamma（82万，无历史分位）｜正 Gamma 减弱（0万）｜现价位于 Flip 上方 17.22%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构）；上方 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 12.0C — Vol 236 | 最新价 $0.10 | OI 739→896 (ΔOI +157张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增157张（+21.2% vs前日OI），连续性待观察（方向未知）
11-20 11.5C — Vol 248 | 最新价 $0.15 | OI 220→365 (ΔOI +145张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增145张（+65.9% vs前日OI），连续性待观察（方向未知）
11-27 11.5C — Vol 127 | 最新价 $0.35 | OI 28→140 (ΔOI +112张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增112张（+400.0% vs前日OI），连续性待观察（方向未知）
11-20 11.0C — Vol 71 | 最新价 $0.30 | OI 104→157 (ΔOI +53张) | ΔOI/Volume 74.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增53张（+51.0% vs前日OI），连续性待观察（方向未知）
11-20 10.5C — Vol 44 | 最新价 $0.52 | OI 6→48 (ΔOI +42张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增42张（+700.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 509 张（Put 0 / Call 509），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +0.4k / P -13 ｜ Activity HIGH ｜ 3D
11-27  C +0.1k / P +5 ｜ Activity MEDIUM △ ｜ 10D
12-04  C +9 / P +14 ｜ Activity MEDIUM △ ｜ 17D
12-11  C +58 / P +4 ｜ Activity HIGH ｜ 24D

📆 11-20 Forward Structure
存量OI: C 6.8k / P 2.1k，今日变化ΔOI: C +0.4k / P -13，平值价格ATM: C $0.52 / P $0.40 ｜ ATM IV 104.2%，净 delta 敞口 14k shares
Top ΔOI: C 11 +145 ｜ C 11 +53
仓位参考: Max Pain 12 ｜ Call Wall 11.5（+8.8%，弱）（OI 0.4k） ｜ Put Wall 11（+4.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 104.2%｜历史 Rank 50%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,189 股

11-27（MEDIUM △）Top ΔOI: 11C +112 ｜ 11P +10
11-27（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 10（-5.4%，弱）（OI 0.1k）

12-04（MEDIUM △）Top ΔOI: 11P +12
12-04（MEDIUM △）仓位参考: Max Pain 13

📆 12-11 Forward Structure
存量OI: C 0.3k / P 88，今日变化ΔOI: C +58 / P +4，平值价格ATM: C $1.10 / P $0.65 ｜ ATM IV 90.0%，净 delta 敞口 2k shares
Top ΔOI: C 11 +41
仓位参考: Max Pain 11 ｜ Call Wall 11（+4.1%，弱）（OI 41） ｜ Put Wall 11（+4.1%，弱）（OI 14）
量化解读： 存量 Call 重｜ATM IV 90.0%｜历史 Rank 50%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 正 2,337 股

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 104.2% vs 11-27 87.5%（差 +16.7pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/NNE_morning.json