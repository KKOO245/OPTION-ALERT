# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $743.53
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 46.0（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-19 90C ΔOI +530（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 90C ΔOI +530 占该期限总 OI 24.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 88.53 → 今开 89.13（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 89.38 ｜ 低 87.31

Options: P/C成交量 1.21 | OI比 0.68 | ATM IV 43.6% | Skew -0.1pp | Term 0.90 | ExpMove ±3.9%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.68）+ 当日成交偏 Put（P/C量 1.21）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±3.9% ｜ 10-19（6D）±4.3% ｜ 10-21（8D）±4.8% ｜ 10-23（10D）±6.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,715,844 | GEX Change vs 上次快照 -14,893,991 | Flip: Primary Flip: 87.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 565 / LOW 142 / INVALID 437
结构观察区: Primary Flip 87.18（全链重定价，覆盖 95%）
Call Wall 90（弱结构｜现价低于该位 3.1%）
最近结构参考: Flip 87（现价高于该位 0.6%）
量化视角： 正 Gamma（1172万，无历史分位）｜正 Gamma 减弱（1489万）｜现价位于 Flip 上方 0.63%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 89（MaxPain，仅结算参考） / 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 87（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 85.0P — Vol 3,059 | 最新价 $0.32 | OI 9582→10778 (ΔOI +1196张) | ΔOI/Volume 39.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1196张（+12.5% vs前日OI），连续性待观察（方向未知）
10-21 98.0C — Vol 1,013 | 最新价 $0.10 | OI 716→1729 (ΔOI +1013张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1013张（+141.5% vs前日OI），连续性待观察（方向未知）
10-16 84.0P — Vol 1,556 | 最新价 $0.18 | OI 6484→7410 (ΔOI +926张) | ΔOI/Volume 59.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增926张（+14.3% vs前日OI），连续性待观察（方向未知）
10-30 95.0C — Vol 815 | 最新价 $1.00 | OI 415→1125 (ΔOI +710张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增710张（+171.1% vs前日OI），连续性待观察（方向未知）
10-16 92.0C — Vol 837 | 最新价 $0.40 | OI 2418→2999 (ΔOI +581张) | ΔOI/Volume 69.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增581张（+24.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,426 张（Put 2,122 / Call 2,304），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -1.4k / P +3.4k ｜ Activity MEDIUM △ ｜ 3D
10-19  C +0.7k / P +99 ｜ Activity HIGH ｜ 6D
10-21  C +1.2k / P +13 ｜ Activity HIGH ｜ 8D
10-23  C +0.9k / P +0.7k ｜ Activity MEDIUM △ ｜ 10D

📆 10-16 Forward Structure
存量OI: C 191.7k / P 129.5k，今日变化ΔOI: C -1.4k / P +3.4k，平值价格ATM: C $2.12 / P $1.30 ｜ ATM IV 43.6%，净 delta 敞口 -27k shares
Top ΔOI: C 95 -1,929 ｜ P 85 +1,196 ｜ P 84 +926
仓位参考: Max Pain 89 ｜ Call Wall 90.5（+3.2%，弱）（OI 21.6k） ｜ Put Wall 85（-3.1%，弱）（OI 10.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.6%｜历史 Rank 68%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,216 股

📆 10-19 Forward Structure
存量OI: C 1.7k / P 0.5k，今日变化ΔOI: C +0.7k / P +99，平值价格ATM: C $2.15 / P $1.59 ｜ ATM IV 36.6%，净 delta 敞口 17k shares
Top ΔOI: C 90 +530 ｜ C 92 +61 ｜ C 94 +38
仓位参考: Max Pain 88 ｜ Call Wall 90（+2.6%）（OI 0.8k） ｜ Put Wall 88（+0.3%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 36.6%｜历史 Rank 68%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 17,419 股

📆 10-21 Forward Structure
存量OI: C 2.5k / P 2.5k，今日变化ΔOI: C +1.2k / P +13，平值价格ATM: C $2.46 / P $1.79 ｜ ATM IV 38.4%，净 delta 敞口 10k shares
Top ΔOI: C 92 +69 ｜ C 91 +67
仓位参考: Max Pain 85
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.4%｜历史 Rank 68%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,969 股

10-23（MEDIUM △）Top ΔOI: 83P +548 ｜ 94C +431
10-23（MEDIUM △）仓位参考: Max Pain 90 ｜ Call Wall 90（+2.6%，弱）（OI 0.6k） ｜ Put Wall 85（-3.1%，弱）（OI 1.3k）

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 43.6% vs 10-19 36.6%（差 +7.1pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/GDX_morning.json