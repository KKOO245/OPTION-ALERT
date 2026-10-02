# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $771.73 ｜ QQQ $753.70
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 576.33 → 今开 590.59（+2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 596.44 ｜ 低 587.84

Options: P/C成交量 0.12 | OI比 1.79 | ATM IV 51.2% | Skew 11.0pp | Term 0.74 | ExpMove ±5.5%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 11.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.12×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.79×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±5.5% ｜ 10-16（14D）±5.6% ｜ 10-23（21D）±9.3% ｜ 10-30（28D）±9.1%
   ⇒ IV–VIX Spread: +35.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,370,492 | GEX Change vs 上次快照 442,365 | Flip: Primary Flip: 569.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 571 / LOW 294 / INVALID 693
结构观察区: Primary Flip 569.47（全链重定价，覆盖 89%）
Call Wall 600（现价低于该位 0.9%）
最近结构参考: Call Wall 600（现价低于该位 0.9%）
量化视角： 正 Gamma（1437万，无历史分位）｜正 Gamma 增强（+44万）｜现价位于 Flip 上方 4.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 550（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 569（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 610.0C — Vol 557 | 最新价 $0.10 | OI 87→644 (ΔOI +557张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增557张（+640.2% vs前日OI），连续性待观察（方向未知）
10-02 555.0P — Vol 2,073 | 最新价 $0.21 | OI 141→644 (ΔOI +503张) | ΔOI/Volume 24.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增503张（+356.7% vs前日OI），连续性待观察（方向未知）
10-09 550.0P — Vol 424 | 最新价 $3.30 | OI 289→565 (ΔOI +276张) | ΔOI/Volume 65.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增276张（+95.5% vs前日OI），连续性待观察（方向未知）
10-16 570.0P — Vol 184 | 最新价 $13.05 | OI 152→310 (ΔOI +158张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增158张（+104.0% vs前日OI），连续性待观察（方向未知）
10-02 570.0P — Vol 203 | 最新价 $2.14 | OI 107→254 (ΔOI +147张) | ΔOI/Volume 72.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增147张（+137.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,641 张（Put 1,084 / Call 557），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 17.5k / P 31.4k，今日成交量: C 1.1k / P 2.2k，平值价格ATM: C $2.23 / P $4.50 ｜ ATM IV 51.2%，预期波动 ±1.1%，Max Pain 550
Top ΔOI: C 610 +557 ｜ P 555 +503 ｜ P 550 -250

📆 Forward Expiration Structure

10-09  C +67 / P +0.8k ｜ Activity MEDIUM △ ｜ 7D
10-16  C +0.2k / P -26 ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.2k / P +87 ｜ Activity MEDIUM △ ｜ 21D
10-30  C +0.2k / P +0.1k ｜ Activity LOW ｜ 28D

📆 10-09 Forward Structure
存量OI: C 4.8k / P 4.8k，今日变化ΔOI: C +67 / P +0.8k，平值价格ATM: C $9.70 / P $22.80 ｜ ATM IV 33.5%，净 delta 敞口 -6k shares
Top ΔOI: P 550 +276 ｜ P 560 +130 ｜ P 562 +106
仓位参考: Max Pain 532 ｜ Put Wall 560（-5.9%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 33.5%｜历史 Rank 87%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 5,698 股

10-16（MEDIUM △）Top ΔOI: 570P +158
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 600（+0.9%）（OI 9.1k）

10-23（MEDIUM △）Top ΔOI: 580C +31 ｜ 555C +26
10-23（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 610（+2.5%，弱）（OI 0.1k）

10-30（Activity LOW）仓位参考: Max Pain 555 ｜ Call Wall 630（+5.9%）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SOXX_morning.json