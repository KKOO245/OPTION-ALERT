# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.43 ｜ QQQ $745.68
VIX 15.29 ↑3.0%（5D -1.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-16 90C ΔOI +21,135（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 98C ΔOI +614 占该期限总 OI 16.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 89.28 → 今开 88.23（-1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 88.79 ｜ 低 87.93

Options: P/C成交量 0.26 | OI比 0.65 | ATM IV 42.4% | Skew -0.0pp | Term 0.96 | ExpMove ±3.7%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（4D）±3.7% ｜ 10-19（7D）±4.8% ｜ 10-21（9D）±4.9% ｜ 10-23（11D）±5.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,438,957 | GEX Change vs 上次快照 9,087,001 | Flip: Primary Flip: 87.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 557 / LOW 131 / INVALID 390
结构观察区: Primary Flip 87.07（全链重定价，覆盖 98%）
Call Wall 90（弱结构｜现价低于该位 2.2%）
最近结构参考: Flip 87（现价高于该位 1.7%）
量化视角： 正 Gamma（2344万，无历史分位）｜正 Gamma 增强（+909万）｜现价位于 Flip 上方 1.69%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 89（MaxPain，仅结算参考） / 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 87（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 93.5C — Vol 21,175 | 最新价 $0.55 | OI 139→21291 (ΔOI +21152张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21152张（+15217.3% vs前日OI），连续性待观察（方向未知）
10-16 90.5C — Vol 21,532 | 最新价 $1.36 | OI 369→21504 (ΔOI +21135张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21135张（+5727.6% vs前日OI），连续性待观察（方向未知）
10-16 86.0P — Vol 5,862 | 最新价 $0.65 | OI 5076→10064 (ΔOI +4988张) | ΔOI/Volume 85.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4988张（+98.3% vs前日OI），连续性待观察（方向未知）
10-23 75.0P — Vol 5,034 | 最新价 $0.05 | OI 515→5374 (ΔOI +4859张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4859张（+943.5% vs前日OI），连续性待观察（方向未知）
10-16 95.0C — Vol 6,766 | 最新价 $0.30 | OI 6869→11543 (ΔOI +4674张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4674张（+68.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 56,808 张（Put 9,847 / Call 46,961），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +54.2k / P +11.6k ｜ Activity HIGH ｜ 4D
10-19  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 7D
10-21  C +0.7k / P -44 ｜ Activity HIGH ｜ 9D
10-23  C +0.9k / P +5.5k ｜ Activity HIGH ｜ 11D

📆 10-16 Forward Structure
存量OI: C 193.1k / P 126.1k，今日变化ΔOI: C +54.2k / P +11.6k，平值价格ATM: C $1.70 / P $1.55 ｜ ATM IV 42.4%，净 delta 敞口 993k shares
Top ΔOI: C 93 +21,152 ｜ C 90 +21,135 ｜ P 86 +4,988
仓位参考: Max Pain 89 ｜ Call Wall 90.5（+2.2%，弱）（OI 21.5k） ｜ Put Wall 90（+1.6%，弱）（OI 10.4k）
量化解读： 存量 Call 重｜ATM IV 42.4%｜历史 Rank 65%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 993,332 股

10-19（MEDIUM △）Top ΔOI: 88P +79 ｜ 86P +55
10-19（MEDIUM △）仓位参考: Max Pain 89 ｜ Call Wall 92（+3.9%）（OI 0.4k） ｜ Put Wall 88（-0.6%，弱）（OI 82）

📆 10-21 Forward Structure
存量OI: C 1.3k / P 2.5k，今日变化ΔOI: C +0.7k / P -44，平值价格ATM: C $1.91 / P $2.41 ｜ ATM IV 37.8%，净 delta 敞口 5k shares
Top ΔOI: C 93 +36
仓位参考: Max Pain 85
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.8%｜历史 Rank 65%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 4,557 股

📆 10-23 Forward Structure
存量OI: C 8.6k / P 12.6k，今日变化ΔOI: C +0.9k / P +5.5k，平值价格ATM: C $2.60 / P $2.52 ｜ ATM IV 39.7%，净 delta 敞口 -149 shares
Top ΔOI: P 84 +410 ｜ C 95 +358
仓位参考: Max Pain 91 ｜ Call Wall 90（+1.6%，弱）（OI 0.6k） ｜ Put Wall 85（-4.0%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 39.7%｜历史 Rank 65%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 149 股

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 42.4% vs 10-19 37.4%（差 +5.0pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/GDX_morning.json