# 期权晨报 2026-09-25（快照 10:20 ET）

📊 市场环境

SPY $769.28 ｜ QQQ $741.55
VIX 15.83 ↑1.0%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 137.78 → 今开 137.25（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 139.83 ｜ 低 136.02

Options: P/C成交量 0.17 | OI比 0.62 | ATM IV 75.4% | Skew 0.6pp | Term 0.74 | ExpMove ±5.4%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价薄（Skew 0.6pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±5.4% ｜ 10-09（14D）±8.7% ｜ 10-16（21D）±9.7% ｜ 10-23（28D）±13.6%
   ⇒ IV–VIX Spread: +59.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,493,281 | GEX Change vs 上次快照 -999,044 | Flip: Primary Flip: 132.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 540 / LOW 59 / INVALID 127
结构观察区: Primary Flip 132.73（全链重定价，覆盖 94%）
Call Wall 150（现价低于该位 8.4%）
最近结构参考: Flip 133（现价高于该位 3.6%）
量化视角： 正 Gamma（1349万，无历史分位）｜正 Gamma 减弱（100万）｜现价位于 Flip 上方 3.57%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 150.0C — Vol 4,557 | 最新价 $2.93 | OI 11539→12526 (ΔOI +987张) | ΔOI/Volume 21.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增987张（+8.6% vs前日OI），连续性待观察（方向未知）
10-16 140.0P — Vol 662 | 最新价 $7.77 | OI 1676→2037 (ΔOI +361张) | ΔOI/Volume 54.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增361张（+21.5% vs前日OI），连续性待观察（方向未知）
10-30 185.0C — Vol 373 | 最新价 $0.99 | OI 63→419 (ΔOI +356张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增356张（+565.1% vs前日OI），连续性待观察（方向未知）
10-16 200.0C — Vol 658 | 最新价 $0.06 | OI 3943→4266 (ΔOI +323张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增323张（+8.2% vs前日OI），连续性待观察（方向未知）
10-02 131.0P — Vol 378 | 最新价 $1.51 | OI 352→664 (ΔOI +312张) | ΔOI/Volume 82.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增312张（+88.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,339 张（Put 673 / Call 1,666），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 34.8k / P 21.6k，今日成交量: C 3.8k / P 0.7k，平值价格ATM: C $2.52 / P $0.38 ｜ ATM IV 75.4%，预期波动 ±2.1%，Max Pain 136
Top ΔOI: P 130 -284 ｜ P 138 +245 ｜ C 146 +226

📆 Forward Expiration Structure

10-02  C +1.6k / P +1.6k ｜ Activity MEDIUM △ ｜ 7D
10-09  C +0.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 14D
10-16  C +2.4k / P +1.0k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +0.6k / P +0.5k ｜ Activity MEDIUM △ ｜ 28D

📆 10-02 Forward Structure
存量OI: C 19.3k / P 17.0k，今日变化ΔOI: C +1.6k / P +1.6k，平值价格ATM: C $4.23 / P $3.25 ｜ ATM IV 52.8%，净 delta 敞口 17k shares
Top ΔOI: P 131 +312 ｜ C 145 +261 ｜ C 139 +224
仓位参考: Max Pain 135 ｜ Call Wall 150（+9.1%）（OI 3.1k） ｜ Put Wall 130（-5.4%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.8%｜历史 Rank 95%（近端代理）｜净 delta 敞口 正 17,151 股

10-09（MEDIUM △）Top ΔOI: 150C +205
10-09（MEDIUM △）仓位参考: Max Pain 136 ｜ Call Wall 150（+9.1%）（OI 2.6k） ｜ Put Wall 140（+1.8%，弱）（OI 0.5k）

10-16（MEDIUM △）Top ΔOI: 150C +987 ｜ 140P +361
10-16（MEDIUM △）仓位参考: Max Pain 127 ｜ Call Wall 150（+9.1%）（OI 12.5k） ｜ Put Wall 130（-5.4%，弱）（OI 4.9k）

10-23（MEDIUM △）Top ΔOI: 120P +285
10-23（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 140（+1.8%，弱）（OI 1.0k） ｜ Put Wall 125（-9.1%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/NOW_morning.json