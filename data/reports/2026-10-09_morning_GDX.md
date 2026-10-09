# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $776.00 ｜ QQQ $749.68
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 42.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 88C ΔOI +11,111（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 92C ΔOI +399 占该期限总 OI 39.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 86.72 → 今开 88.64（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 89.51 ｜ 低 88.25

Options: P/C成交量 0.11 | OI比 0.31 | ATM IV 48.4% | Skew -4.4pp | Term 0.84 | ExpMove ±4.3%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±4.3% ｜ 10-19（10D）±3.4% ｜ 10-21（12D）±4.6% ｜ 10-23（14D）±6.3%
   ⇒ IV–VIX Spread: +33.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 102,681,618 | GEX Change vs 上次快照 65,516,225 | Flip: Primary Flip: 84.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 462 / LOW 151 / INVALID 361
结构观察区: Primary Flip 84.92（全链重定价，覆盖 90%）
Put Wall 85（弱结构｜现价高于该位 4.6%） | Call Wall 90（弱结构｜现价低于该位 1.2%）
最近结构参考: Call Wall 90（现价低于该位 1.2%）
量化视角： 正 Gamma（1.03亿，无历史分位）｜正 Gamma 增强（+6552万）｜现价位于 Flip 上方 4.70%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构） / 87（MaxPain，仅结算参考）；上方 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 88.5C — Vol 11,160 | 最新价 $1.30 | OI 41→11152 (ΔOI +11111张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11111张（+27100.0% vs前日OI），连续性待观察（方向未知）
10-16 91.5C — Vol 11,236 | 最新价 $0.56 | OI 63→11147 (ΔOI +11084张) | ΔOI/Volume 98.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11084张（+17593.7% vs前日OI），连续性待观察（方向未知）
10-16 81.0P — Vol 3,117 | 最新价 $0.31 | OI 2235→5302 (ΔOI +3067张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3067张（+137.2% vs前日OI），连续性待观察（方向未知）
10-16 89.0C — Vol 3,562 | 最新价 $1.10 | OI 3544→6597 (ΔOI +3053张) | ΔOI/Volume 85.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3053张（+86.2% vs前日OI），连续性待观察（方向未知）
10-21 79.0P — Vol 2,413 | 最新价 $0.39 | OI 0→2413 (ΔOI +2413张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2413张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 30,728 张（Put 5,480 / Call 25,248），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 100.9k / P 31.3k，今日成交量: C 4.3k / P 0.5k，平值价格ATM: C $0.41 / P $0.53 ｜ ATM IV 48.4%，预期波动 ±1.1%，Max Pain 87
Top ΔOI: C 89 +1,858 ｜ P 81 +711 ｜ C 88 +625

📆 Forward Expiration Structure

10-16  C +26.3k / P +5.3k ｜ Activity HIGH ｜ 7D
10-19  C +0.7k / P +12 ｜ Activity HIGH ｜ 10D
10-21  C +25 / P +2.4k ｜ Activity HIGH ｜ 12D
10-23  C +0.8k / P +59 ｜ Activity MEDIUM △ ｜ 14D

📆 10-16 Forward Structure
存量OI: C 139.0k / P 114.5k，今日变化ΔOI: C +26.3k / P +5.3k，平值价格ATM: C $2.01 / P $1.80 ｜ ATM IV 38.3%，净 delta 敞口 1.2M shares
Top ΔOI: C 88 +11,111 ｜ C 91 +11,084 ｜ P 81 +3,067
仓位参考: Max Pain 89 ｜ Call Wall 88.5（-0.5%，弱）（OI 11.2k） ｜ Put Wall 90（+1.2%，弱）（OI 10.4k）
量化解读： 存量 Call 重｜ATM IV 38.3%｜历史 Rank 79%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,159,454 股

📆 10-19 Forward Structure
存量OI: C 0.9k / P 0.1k，今日变化ΔOI: C +0.7k / P +12，平值价格ATM: C $1.02 / P $2.01 ｜ ATM IV 34.7%，净 delta 敞口 24k shares
Top ΔOI: C 92 +399 ｜ C 90 +230 ｜ C 86 +10
仓位参考: Max Pain 86 ｜ Call Wall 92（+3.5%）（OI 0.4k） ｜ Put Wall 90（+1.2%，弱）（OI 23）
量化解读： 存量 Call 重｜ATM IV 34.7%｜历史 Rank 79%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 23,784 股

📆 10-21 Forward Structure
存量OI: C 0.6k / P 2.5k，今日变化ΔOI: C +25 / P +2.4k，平值价格ATM: C $1.67 / P $2.41 ｜ ATM IV 36.4%，净 delta 敞口 -14k shares
Top ΔOI: P 79 +2,413 ｜ P 86 +5
仓位参考: Max Pain 84
量化解读： 存量 Put 重｜ATM IV 36.4%｜历史 Rank 79%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 13,557 股

10-23（MEDIUM △）Top ΔOI: 92C +368 ｜ 90C +190
10-23（MEDIUM △）仓位参考: Max Pain 92 ｜ Call Wall 90（+1.2%，弱）（OI 0.6k） ｜ Put Wall 90（+1.2%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/GDX_morning.json