# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $743.51
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 427.64 → 今开 428.98（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 430.00 ｜ 低 416.37

Options: P/C成交量 2.21 | OI比 0.92 | ATM IV 45.4% | Skew -7.6pp | Term 1.02 | ExpMove ±3.8%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -7.6pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±3.8% ｜ 10-23（10D）±8.3% ｜ 10-30（17D）±8.4% ｜ 11-06（24D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,564,121 | GEX Change vs 上次快照 -882,143 | Flip: Primary Flip: 398.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 389 / LOW 130 / INVALID 385
结构观察区: Primary Flip 398.63（全链重定价，覆盖 94%）
Call Wall 420（弱结构｜现价低于该位 0.0%）
最近结构参考: Call Wall 420（现价低于该位 0.0%）
量化视角： 正 Gamma（256万，无历史分位）｜正 Gamma 减弱（88万）｜现价位于 Flip 上方 5.36%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 399（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 310.0P — Vol 250 | 最新价 $0.86 | OI 0→250 (ΔOI +250张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增250张（前日OI缺失），值得跟踪（方向未知）
10-23 500.0C — Vol 223 | 最新价 $1.45 | OI 0→220 (ΔOI +220张) | ΔOI/Volume 98.7% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增220张（前日OI缺失），值得跟踪（方向未知）
10-23 460.0C — Vol 244 | 最新价 $6.50 | OI 236→430 (ΔOI +194张) | ΔOI/Volume 79.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增194张（+82.2% vs前日OI），连续性待观察（方向未知）
10-16 445.0C — Vol 89 | 最新价 $1.42 | OI 133→214 (ΔOI +81张) | ΔOI/Volume 91.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81张（+60.9% vs前日OI），连续性待观察（方向未知）
10-16 442.5C — Vol 52 | 最新价 $1.65 | OI 50→95 (ΔOI +45张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增45张（+90.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 790 张（Put 250 / Call 540），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.2k / P +98 ｜ Activity MEDIUM △ ｜ 3D
10-23  C +0.5k / P +86 ｜ Activity MEDIUM △ ｜ 10D
10-30  C +26 / P +2 ｜ Activity MEDIUM △ ｜ 17D
11-06  C +7 / P +28 ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 11.7k / P 10.7k，今日变化ΔOI: C +0.2k / P +98，平值价格ATM: C $9.00 / P $6.79 ｜ ATM IV 45.4%，净 delta 敞口 143 shares
Top ΔOI: C 445 +81 ｜ C 442 +45 ｜ P 425 +44
仓位参考: Max Pain 395 ｜ Call Wall 400（-4.8%，弱）（OI 0.9k） ｜ Put Wall 380（-9.5%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 45.4%｜历史 Rank 81%（近端代理）｜IV/RV 1.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 143 股

10-23（MEDIUM △）Top ΔOI: 460C +194 ｜ 400P +39
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（+1.2%，弱）（OI 0.5k） ｜ Put Wall 415（-1.2%）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 455C +11 ｜ 430C +5
10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 460（+9.5%，弱）（OI 94） ｜ Put Wall 380（-9.5%，弱）（OI 50）

11-06（MEDIUM △）Top ΔOI: 390P +27 ｜ 425P +5
11-06（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 455（+8.3%，弱）（OI 50） ｜ Put Wall 390（-7.1%）（OI 52）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/ISRG_morning.json