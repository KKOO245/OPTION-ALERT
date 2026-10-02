# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 195C ΔOI +5,200（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 189.29 → 今开 194.40（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 200.35 ｜ 低 189.29

Options: P/C成交量 0.32 | OI比 0.77 | ATM IV 100.0% | Skew -1.1pp | Term 0.67 | ExpMove ±6.9%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±6.9% ｜ 10-16（14D）±9.8% ｜ 10-23（21D）±9.9% ｜ 10-30（28D）±13.5%
   ⇒ IV–VIX Spread: +84.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,881,086 | GEX Change vs 上次快照 13,553,826 | Flip: Primary Flip: 176.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 494 / LOW 137 / INVALID 261
结构观察区: Primary Flip 176.77（全链重定价，覆盖 96%）
Call Wall 200（现价低于该位 3.7%）
最近结构参考: Call Wall 200（现价低于该位 3.7%）
量化视角： 正 Gamma（2788万，无历史分位）｜正 Gamma 增强（+1355万）｜现价位于 Flip 上方 8.95%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 177（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 195.0C — Vol 5,796 | 最新价 $4.41 | OI 425→5625 (ΔOI +5200张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5200张（+1223.5% vs前日OI），连续性待观察（方向未知）
10-09 202.5C — Vol 5,375 | 最新价 $2.42 | OI 308→5348 (ΔOI +5040张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5040张（+1636.4% vs前日OI），连续性待观察（方向未知）
10-09 192.5C — Vol 5,114 | 最新价 $5.40 | OI 241→5086 (ΔOI +4845张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4845张（+2010.4% vs前日OI），连续性待观察（方向未知）
10-09 200.0C — Vol 6,383 | 最新价 $2.98 | OI 2938→7729 (ΔOI +4791张) | ΔOI/Volume 75.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4791张（+163.1% vs前日OI），连续性待观察（方向未知）
10-02 195.0C — Vol 5,156 | 最新价 $1.00 | OI 1930→2563 (ΔOI +633张) | ΔOI/Volume 12.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增633张（+32.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,509 张（Put 0 / Call 20,509），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 58.3k / P 44.9k，今日成交量: C 30.5k / P 9.8k，平值价格ATM: C $1.88 / P $2.30 ｜ ATM IV 100.0%，预期波动 ±2.2%，Max Pain 190
Top ΔOI: C 212 -8,836 ｜ C 202 -8,494 ｜ C 205 -2,391

📆 Forward Expiration Structure

10-09  C +21.6k / P +0.7k ｜ Activity HIGH ｜ 7D
10-16  C +0.6k / P -0.2k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.2k / P +61 ｜ Activity MEDIUM △ ｜ 21D
10-30  C +0.4k / P +0.9k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 34.3k / P 24.4k，今日变化ΔOI: C +21.6k / P +0.7k，平值价格ATM: C $6.43 / P $6.87 ｜ ATM IV 59.9%，净 delta 敞口 784k shares
Top ΔOI: C 195 +5,200 ｜ C 202 +5,040 ｜ C 192 +4,845
仓位参考: Max Pain 190 ｜ Call Wall 200（+3.9%，弱）（OI 7.7k）
量化解读： 存量 Call 重｜ATM IV 59.9%｜历史 Rank 87%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 784,280 股

10-16（MEDIUM △）Top ΔOI: 207C +160
10-16（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+3.9%，弱）（OI 6.3k） ｜ Put Wall 200（+3.9%，弱）（OI 3.9k）

10-23（MEDIUM △）Top ΔOI: 200C +35
10-23（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 190（-1.3%，弱）（OI 0.5k） ｜ Put Wall 192.5（-0.0%，弱）（OI 0.4k）

10-30（MEDIUM △）Top ΔOI: 135P +354 ｜ 200C +228
10-30（MEDIUM △）仓位参考: Max Pain 192 ｜ Call Wall 210（+9.0%，弱）（OI 0.7k） ｜ Put Wall 200（+3.9%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/COIN_morning.json