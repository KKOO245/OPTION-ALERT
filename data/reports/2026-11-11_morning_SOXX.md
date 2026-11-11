# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.90 ｜ QQQ $690.38
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 155C ΔOI +15,158（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 146.59 → 今开 153.69（+4.8%） | 较昨收变动（含盘初走势） ｜ 今日高 154.04 ｜ 低 150.88

Options: P/C成交量 2.42 | OI比 2.18 | ATM IV 59.1% | Skew 12.1pp | Term 0.84 | ExpMove ±3.5%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价显著（Skew 12.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.42×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.18×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±3.5% ｜ 11-20（9D）±7.4% ｜ 11-27（16D）±12.0% ｜ 12-04（23D）±13.0%
   ⇒ IV–VIX Spread: +40.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,560,980 | GEX Change vs 上次快照 43,879,523 | Flip: Primary Flip: 154.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 587 / LOW 428 / INVALID 789
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 154.57（全链重定价，覆盖 98%）
Call Wall 155（弱结构｜现价低于该位 1.2%）
最近结构参考: Flip 155（现价低于该位 0.9%）
量化视角： 负 Gamma（1256万，无历史分位）｜负 Gamma 缓解（+4388万）｜现价位于 Flip 下方 0.94%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 153（MaxPain，仅结算参考） / 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 155.0C — Vol 15,378 | 最新价 $2.60 | OI 1367→16525 (ΔOI +15158张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15158张（+1108.8% vs前日OI），连续性待观察（方向未知）
11-13 140.0P — Vol 2,897 | 最新价 $1.35 | OI 3300→5056 (ΔOI +1756张) | ΔOI/Volume 60.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1756张（+53.2% vs前日OI），连续性待观察（方向未知）
11-20 135.0P — Vol 1,752 | 最新价 $2.15 | OI 7685→8561 (ΔOI +876张) | ΔOI/Volume 50.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增876张（+11.4% vs前日OI），连续性待观察（方向未知）
11-20 160.0C — Vol 2,090 | 最新价 $1.45 | OI 6617→7371 (ΔOI +754张) | ΔOI/Volume 36.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增754张（+11.4% vs前日OI），连续性待观察（方向未知）
11-13 130.0P — Vol 1,753 | 最新价 $0.33 | OI 4263→5007 (ΔOI +744张) | ΔOI/Volume 42.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增744张（+17.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,288 张（Put 3,376 / Call 15,912），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.7k / P +3.6k ｜ Activity HIGH ｜ 2D
11-20  C +15.4k / P +1.3k ｜ Activity HIGH ｜ 9D
11-27  C +0.2k / P +0.4k ｜ Activity LOW ｜ 16D
12-04  C +0.4k / P +0.3k ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 110.8k / P 241.6k，今日变化ΔOI: C +0.7k / P +3.6k，平值价格ATM: C $2.52 / P $2.92 ｜ ATM IV 59.1%，净 delta 敞口 31k shares
Top ΔOI: P 140 +1,756
仓位参考: Max Pain 153
量化解读： 存量 Put 重｜ATM IV 59.1%｜历史 Rank 92%（近端代理）｜IV/RV 0.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 30,774 股

📆 11-20 Forward Structure
存量OI: C 214.9k / P 314.9k，今日变化ΔOI: C +15.4k / P +1.3k，平值价格ATM: C $5.60 / P $5.70 ｜ ATM IV 58.0%，净 delta 敞口 765k shares
Top ΔOI: C 155 +15,158 ｜ P 135 +876
仓位参考: Max Pain 158 ｜ Call Wall 155（+1.2%，弱）（OI 16.5k） ｜ Put Wall 150（-2.0%，弱）（OI 21.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.0%｜历史 Rank 92%（近端代理）｜IV/RV 0.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 764,902 股

11-27（Activity LOW）仓位参考: Max Pain 162 ｜ Call Wall 161.67（+5.6%）（OI 10.0k） ｜ Put Wall 146.67（-4.2%，弱）（OI 3.2k）

📆 12-04 Forward Structure
存量OI: C 6.3k / P 8.3k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $7.03 / P $12.85 ｜ ATM IV 50.8%，净 delta 敞口 6k shares
Top ΔOI: C 160 +103
仓位参考: Max Pain 160 ｜ Call Wall 160（+4.5%）（OI 1.0k） ｜ Put Wall 148.33（-3.1%，弱）（OI 0.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.8%｜历史 Rank 92%（近端代理）｜IV/RV 0.12×（近似）｜净 delta 敞口 正 6,045 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SOXX_morning.json