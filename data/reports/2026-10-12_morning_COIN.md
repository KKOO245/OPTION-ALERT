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
🟡 **近现价集中开仓**: 10-16 185C ΔOI +7,115（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 100P ΔOI +5,858 占该期限总 OI 20.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 179.39 → 今开 179.00（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 184.23 ｜ 低 177.41

Options: P/C成交量 0.41 | OI比 0.82 | ATM IV 63.7% | Skew -3.9pp | Term 1.08 | ExpMove ±5.4%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±5.4% ｜ 10-23（11D）±8.1% ｜ 10-30（18D）±11.4% ｜ 11-06（25D）±14.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,924,556 | GEX Change vs 上次快照 12,270,378 | Flip: Primary Flip: 169.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 486 / LOW 111 / INVALID 225
结构观察区: Primary Flip 169.85（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 8.9%）
最近结构参考: Flip 170（现价高于该位 7.3%）
量化视角： 正 Gamma（2392万，无历史分位）｜正 Gamma 增强（+1227万）｜现价位于 Flip 上方 7.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 170（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 100.0P — Vol 8,946 | 最新价 $0.04 | OI 2698→11415 (ΔOI +8717张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8717张（+323.1% vs前日OI），连续性待观察（方向未知）
10-16 185.0C — Vol 12,041 | 最新价 $3.55 | OI 3683→10798 (ΔOI +7115张) | ΔOI/Volume 59.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7115张（+193.2% vs前日OI），连续性待观察（方向未知）
10-16 192.5C — Vol 6,984 | 最新价 $1.70 | OI 625→6500 (ΔOI +5875张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5875张（+940.0% vs前日OI），连续性待观察（方向未知）
10-23 100.0P — Vol 6,388 | 最新价 $0.06 | OI 66→5924 (ΔOI +5858张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5858张（+8875.8% vs前日OI），连续性待观察（方向未知）
10-16 165.0P — Vol 5,823 | 最新价 $0.89 | OI 3723→8819 (ΔOI +5096张) | ΔOI/Volume 87.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5096张（+136.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,661 张（Put 19,671 / Call 12,990），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +23.9k / P +23.4k ｜ Activity HIGH ｜ 4D
10-23  C +1.0k / P +8.3k ｜ Activity HIGH ｜ 11D
10-30  C +1.2k / P +1.9k ｜ Activity HIGH ｜ 18D
11-06  C +25 / P +0.4k ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 134.4k / P 110.2k，今日变化ΔOI: C +23.9k / P +23.4k，平值价格ATM: C $4.85 / P $4.92 ｜ ATM IV 63.6%，净 delta 敞口 660k shares
Top ΔOI: C 185 +7,115 ｜ C 192 +5,875
仓位参考: Max Pain 180 ｜ Call Wall 185（+1.5%，弱）（OI 10.8k） ｜ Put Wall 165（-9.5%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 63.6%｜历史 Rank 18%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 659,588 股

📆 10-23 Forward Structure
存量OI: C 11.2k / P 17.0k，今日变化ΔOI: C +1.0k / P +8.3k，平值价格ATM: C $7.55 / P $7.24 ｜ ATM IV 58.4%，净 delta 敞口 -5k shares
仓位参考: Max Pain 188 ｜ Call Wall 190（+4.2%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 58.4%｜历史 Rank 18%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 5,325 股

📆 10-30 Forward Structure
存量OI: C 11.3k / P 10.6k，今日变化ΔOI: C +1.2k / P +1.9k，平值价格ATM: C $10.25 / P $10.45 ｜ ATM IV 64.9%，净 delta 敞口 38k shares
Top ΔOI: C 190 +283 ｜ C 192 +166
仓位参考: Max Pain 185 ｜ Call Wall 200（+9.7%，弱）（OI 1.6k） ｜ Put Wall 180（-1.2%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.9%｜历史 Rank 18%（近端代理）｜IV/RV 1.21×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 37,710 股

11-06（MEDIUM △）Top ΔOI: 177P +129
11-06（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 200（+9.7%）（OI 0.6k） ｜ Put Wall 170（-6.7%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 63.6% vs 10-23 58.4%（差 +5.3pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/COIN_morning.json