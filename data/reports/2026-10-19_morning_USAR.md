# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.80 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 10.54 → 今开 10.77（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 10.79 ｜ 低 10.08

Options: P/C成交量 0.37 | OI比 0.35 | ATM IV 90.1% | Skew 9.5pp | Term 0.96 | ExpMove ±8.2%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构正常（Term 0.96）｜保护溢价显著（Skew 9.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±8.2% ｜ 10-30（11D）±14.0% ｜ 11-06（18D）±16.6% ｜ 11-13（25D）±20.7%
   ⇒ IV–VIX Spread: +71.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 86,238 | GEX Change vs 上次快照 1,832,038 | Flip: Primary Flip: 10.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 145 / LOW 76 / INVALID 211
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 10.12（全链重定价，覆盖 99%）
Put Wall 10（弱结构｜现价高于该位 1.5%）
最近结构参考: Flip 10（现价高于该位 0.3%）
量化视角： 正 Gamma（9万，无历史分位）｜由负转正（+183万）｜现价位于 Flip 上方 0.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构）；上方 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 12.0C — Vol 1,466 | 最新价 $0.59 | OI 750→1616 (ΔOI +866张) | ΔOI/Volume 59.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增866张（+115.5% vs前日OI），连续性待观察（方向未知）
10-23 12.0C — Vol 963 | 最新价 $0.08 | OI 972→1684 (ΔOI +712张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增712张（+73.2% vs前日OI），连续性待观察（方向未知）
10-23 12.5C — Vol 641 | 最新价 $0.05 | OI 823→1383 (ΔOI +560张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增560张（+68.0% vs前日OI），连续性待观察（方向未知）
10-30 13.5C — Vol 640 | 最新价 $0.07 | OI 275→733 (ΔOI +458张) | ΔOI/Volume 71.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增458张（+166.6% vs前日OI），连续性待观察（方向未知）
10-30 12.5C — Vol 457 | 最新价 $0.12 | OI 535→933 (ΔOI +398张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增398张（+74.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,994 张（Put 0 / Call 2,994），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.1k / P +0.4k ｜ Activity MEDIUM △ ｜ 4D
10-30  C +1.3k / P +46 ｜ Activity HIGH ｜ 11D
11-06  C +0.3k / P -0.2k ｜ Activity MEDIUM △ ｜ 18D
11-13  C +25 / P +60 ｜ Activity MEDIUM △ ｜ 25D

📆 10-23 Forward Structure
存量OI: C 18.5k / P 6.5k，今日变化ΔOI: C +2.1k / P +0.4k，平值价格ATM: C $0.56 / P $0.27 ｜ ATM IV 90.1%，净 delta 敞口 27k shares
Top ΔOI: C 10 +395
仓位参考: Max Pain 12 ｜ Call Wall 11（+8.4%，弱）（OI 1.1k） ｜ Put Wall 9.5（-6.4%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 90.1%｜历史 Rank 21%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,566 股

📆 10-30 Forward Structure
存量OI: C 10.3k / P 9.3k，今日变化ΔOI: C +1.3k / P +46，平值价格ATM: C $0.95 / P $0.47 ｜ ATM IV 84.3%，净 delta 敞口 26k shares
Top ΔOI: C 10 +180
仓位参考: Max Pain 14 ｜ Call Wall 11（+8.4%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 84.3%｜历史 Rank 21%（近端代理）｜IV/RV 1.50×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 26,500 股

11-06（MEDIUM △）Top ΔOI: 17P -227 ｜ 10P +58
11-06（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 11（+8.4%，弱）（OI 0.2k） ｜ Put Wall 10（-1.5%，弱）（OI 0.8k）

11-13（MEDIUM △）Top ΔOI: 15P -97 ｜ 10P +50
11-13（MEDIUM △）仓位参考: Max Pain 15 ｜ Call Wall 10.5（+3.4%，弱）（OI 0.2k） ｜ Put Wall 11（+8.4%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 90.1% vs 10-30 84.3%（差 +5.8pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=57 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=57）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/USAR_morning.json