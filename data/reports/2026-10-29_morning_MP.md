# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.48 ｜ QQQ $715.76
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 41.06 → 今开 40.10（-2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 41.91 ｜ 低 40.10

Options: P/C成交量 1.34 | OI比 0.57 | ATM IV 84.8% | Skew 10.0pp | Term 0.79 | ExpMove ±3.6%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 10.0pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.57）+ 当日成交偏 Put（P/C量 1.34）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.34×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±3.6% ｜ 11-06（8D）±15.0% ｜ 11-13（15D）±6.5% ｜ 11-20（22D）±17.9%
   ⇒ IV–VIX Spread: +68.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,672,988 | GEX Change vs 上次快照 1,003,391 | Flip: Primary Flip: 38.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 319 / LOW 71 / INVALID 136
结构观察区: Primary Flip 38.90（全链重定价，覆盖 95%）
最近结构参考: Flip 39（现价高于该位 6.8%）
量化视角： 正 Gamma（467万，无历史分位）｜正 Gamma 增强（+100万）｜现价位于 Flip 上方 6.83%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 41（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 39（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 48.0C — Vol 5,164 | 最新价 $0.94 | OI 1001→3042 (ΔOI +2041张) | ΔOI/Volume 39.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2041张（+203.9% vs前日OI），连续性待观察（方向未知）
10-30 45.0C — Vol 348 | 最新价 $0.05 | OI 486→728 (ΔOI +242张) | ΔOI/Volume 69.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增242张（+49.8% vs前日OI），连续性待观察（方向未知）
11-20 45.0C — Vol 284 | 最新价 $1.41 | OI 1913→2130 (ΔOI +217张) | ΔOI/Volume 76.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增217张（+11.3% vs前日OI），连续性待观察（方向未知）
11-06 44.0C — Vol 223 | 最新价 $0.85 | OI 403→526 (ΔOI +123张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增123张（+30.5% vs前日OI），连续性待观察（方向未知）
10-30 42.0C — Vol 322 | 最新价 $0.50 | OI 959→1082 (ΔOI +123张) | ΔOI/Volume 38.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增123张（+12.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,746 张（Put 0 / Call 2,746），跨 4 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.5k / P -0.3k ｜ Activity MEDIUM △ ｜ 1D
11-06  C +0.3k / P -0.1k ｜ Activity LOW ｜ 8D
11-13  C +26 / P +37 ｜ Activity MEDIUM △ ｜ 15D
11-20  C +0.3k / P +69 ｜ Activity LOW ｜ 22D

📆 10-30 Forward Structure
存量OI: C 13.6k / P 7.7k，今日变化ΔOI: C +0.5k / P -0.3k，平值价格ATM: C $0.76 / P $0.75 ｜ ATM IV 84.8%，净 delta 敞口 32k shares
Top ΔOI: C 45 +242 ｜ C 42 +123
仓位参考: Max Pain 41 ｜ Call Wall 40（-3.8%，弱）（OI 1.2k） ｜ Put Wall 44（+5.9%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 84.8%｜历史 Rank 80%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 31,821 股

11-06（Activity LOW）仓位参考: Max Pain 42 ｜ Call Wall 45（+8.3%，弱）（OI 1.6k） ｜ Put Wall 38（-8.6%）（OI 0.9k）

11-13（MEDIUM △）Top ΔOI: 37P +17 ｜ 38C -13
11-13（MEDIUM △）仓位参考: Max Pain 42 ｜ Put Wall 39（-6.2%）（OI 0.8k）

11-20（Activity LOW）仓位参考: Max Pain 45 ｜ Call Wall 45（+8.3%，弱）（OI 2.1k） ｜ Put Wall 45（+8.3%，弱）（OI 1.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/MP_morning.json