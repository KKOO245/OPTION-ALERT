# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $757.88 ｜ QQQ $688.17
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 48.5% vs 11-20 37.2%（差 +11.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 430P ΔOI +52（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 449.53 → 今开 448.61（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 451.26 ｜ 低 439.20

Options: P/C成交量 0.06 | OI比 0.95 | ATM IV 48.5% | Skew 10.0pp | Term 0.69 | ExpMove ±3.4%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 10.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.06×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（1D）±3.4% ｜ 11-20（8D）±4.9% ｜ 11-27（15D）±2.3% ｜ 12-04（22D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,644,200 | GEX Change vs 上次快照 -668,244 | Flip: Primary Flip: 417.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 354 / LOW 196 / INVALID 460
结构观察区: Primary Flip 417.85（全链重定价，覆盖 95%）
Call Wall 480（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 418（现价高于该位 5.8%）
量化视角： 正 Gamma（264万，无历史分位）｜正 Gamma 减弱（67万）｜现价位于 Flip 上方 5.84%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 440（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 418（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 430.0P — Vol 55 | 最新价 $0.93 | OI 74→126 (ΔOI +52张) | ΔOI/Volume 94.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52张（+70.3% vs前日OI），连续性待观察（方向未知）
11-13 440.0P — Vol 16 | 最新价 $2.00 | OI 22→37 (ΔOI +15张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15张（+68.2% vs前日OI），连续性待观察（方向未知）
11-13 417.5P — Vol 12 | 最新价 $0.05 | OI 15→27 (ΔOI +12张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12张（+80.0% vs前日OI），连续性待观察（方向未知）
11-13 445.0P — Vol 14 | 最新价 $3.25 | OI 15→26 (ΔOI +11张) | ΔOI/Volume 78.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11张（+73.3% vs前日OI），连续性待观察（方向未知）
11-27 445.0P — Vol 24 | 最新价 $11.20 | OI 4→15 (ΔOI +11张) | ΔOI/Volume 45.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11张（+275.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 101 张（Put 101 / Call 0），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +28 / P +69 ｜ Activity MEDIUM △ ｜ 1D
11-20  C -15 / P -52 ｜ Activity LOW ｜ 8D
11-27  C +19 / P +15 ｜ Activity MEDIUM △ ｜ 15D
12-04  C -16 / P +4 ｜ Activity LOW ｜ 22D

📆 11-13 Forward Structure
存量OI: C 1.7k / P 1.6k，今日变化ΔOI: C +28 / P +69，平值价格ATM: C $10.77 / P $4.34 ｜ ATM IV 48.5%，净 delta 敞口 4k shares
Top ΔOI: P 430 +52 ｜ P 482 -21 ｜ P 440 +15
仓位参考: Max Pain 440 ｜ Call Wall 480（+8.5%，弱）（OI 0.2k） ｜ Put Wall 462.5（+4.6%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.5%｜历史 Rank 83%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,380 股

11-20（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 420（-5.0%，弱）（OI 0.8k） ｜ Put Wall 410（-7.3%，弱）（OI 0.5k）

11-27（MEDIUM △）Top ΔOI: 445P +11 ｜ 435C +6
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-2.8%，弱）（OI 64） ｜ Put Wall 410（-7.3%，弱）（OI 42）

12-04（Activity LOW）仓位参考: Max Pain 450 ｜ Call Wall 475（+7.4%，弱）（OI 82） ｜ Put Wall 405（-8.4%，弱）（OI 25）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 48.5% vs 11-20 37.2%（差 +11.3pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/ISRG_morning.json