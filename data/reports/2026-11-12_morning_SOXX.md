# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.38
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 160C ΔOI +4,665（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 155.40 → 今开 150.26（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 154.57 ｜ 低 150.04

Options: P/C成交量 4.87 | OI比 2.11 | ATM IV 67.0% | Skew 2.1pp | Term 0.77 | ExpMove ±3.1%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜当日成交偏 Put（P/C量 4.87）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.87×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.11×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±3.1% ｜ 11-20（8D）±7.8% ｜ 11-27（15D）±8.3% ｜ 12-04（22D）±13.4%
   ⇒ IV–VIX Spread: +48.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -18,132,286 | GEX Change vs 上次快照 -12,601,369 | Flip: Primary Flip: 154.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 642 / LOW 457 / INVALID 705
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 154.54（全链重定价，覆盖 97%）
Call Wall 155（弱结构｜现价低于该位 1.6%）
最近结构参考: Flip 155（现价低于该位 1.3%）
量化视角： 负 Gamma（1813万，无历史分位）｜负 Gamma 加深（1260万）｜现价位于 Flip 下方 1.26%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 153（MaxPain，仅结算参考） / 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 160.0C — Vol 6,290 | 最新价 $0.85 | OI 2734→7399 (ΔOI +4665张) | ΔOI/Volume 74.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4665张（+170.6% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 20,915 | 最新价 $1.25 | OI 15722→17928 (ΔOI +2206张) | ΔOI/Volume 10.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2206张（+14.0% vs前日OI），连续性待观察（方向未知）
11-13 163.33C — Vol 2,243 | 最新价 $0.40 | OI 29017→30719 (ΔOI +1702张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1702张（+5.9% vs前日OI），连续性待观察（方向未知）
11-13 150.0P — Vol 3,030 | 最新价 $0.89 | OI 1285→2783 (ΔOI +1498张) | ΔOI/Volume 49.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1498张（+116.6% vs前日OI），连续性待观察（方向未知）
12-04 172.5C — Vol 1,450 | 最新价 $1.91 | OI 13→1463 (ΔOI +1450张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1450张（+11153.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,521 张（Put 3,704 / Call 7,817），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +6.0k / P +5.0k ｜ Activity HIGH ｜ 1D
11-20  C -7.7k / P -63.1k ｜ Activity HIGH ｜ 8D
11-27  C +3.0k / P +0.8k ｜ Activity MEDIUM △ ｜ 15D
12-04  C +3.6k / P +1.1k ｜ Activity HIGH ｜ 22D

📆 11-13 Forward Structure
存量OI: C 116.8k / P 246.6k，今日变化ΔOI: C +6.0k / P +5.0k，平值价格ATM: C $2.62 / P $2.15 ｜ ATM IV 67.0%，净 delta 敞口 -307k shares
Top ΔOI: C 160 +4,665 ｜ C 163 +1,702 ｜ P 150 +1,498
仓位参考: Max Pain 153 ｜ Call Wall 160（+4.9%，弱）（OI 7.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 67.0%｜历史 Rank 95%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 306,842 股

📆 11-20 Forward Structure
存量OI: C 207.2k / P 251.8k，今日变化ΔOI: C -7.7k / P -63.1k，平值价格ATM: C $6.05 / P $5.80 ｜ ATM IV 61.7%，净 delta 敞口 529k shares
Top ΔOI: P 120 -17,615 ｜ P 105 -17,139 ｜ P 130 -8,867
仓位参考: Max Pain 158 ｜ Call Wall 155（+1.6%，弱）（OI 17.8k） ｜ Put Wall 150（-1.7%，弱）（OI 18.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 61.7%｜历史 Rank 95%（近端代理）｜IV/RV 0.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 529,033 股

11-27（MEDIUM △）Top ΔOI: 161C +1,009 ｜ 162C +537
11-27（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 161.67（+6.0%）（OI 11.1k） ｜ Put Wall 150（-1.7%，弱）（OI 3.3k）

📆 12-04 Forward Structure
存量OI: C 9.9k / P 9.3k，今日变化ΔOI: C +3.6k / P +1.1k，平值价格ATM: C $7.63 / P $12.85 ｜ ATM IV 51.7%，净 delta 敞口 28k shares
Top ΔOI: C 172 +1,450 ｜ C 165 +1,409 ｜ C 173 +513
仓位参考: Max Pain 160 ｜ Call Wall 160（+4.9%，弱）（OI 1.1k） ｜ Put Wall 150（-1.7%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 51.7%｜历史 Rank 95%（近端代理）｜IV/RV 0.12×（近似）｜净 delta 敞口 正 27,825 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 67.0% vs 11-20 61.7%（差 +5.3pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/SOXX_morning.json