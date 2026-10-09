# 期权晨报 2026-10-09（快照 10:20 ET）

📊 市场环境

SPY $778.69 ｜ QQQ $751.27
VIX 15.10 ↓2.0%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 150P ΔOI +1,438（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 149.29 → 今开 149.32（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 153.83 ｜ 低 149.03

Options: P/C成交量 0.08 | OI比 1.22 | ATM IV 58.7% | Skew 60.0pp | Term 0.65 | ExpMove ±5.2%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价显著（Skew 60.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.08×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.22×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±5.2% ｜ 10-23（14D）±7.8% ｜ 10-30（21D）±6.0% ｜ 11-06（28D）±3.6%
   ⇒ IV–VIX Spread: +43.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -32,073,673 | GEX Change vs 上次快照 25,010,795 | Flip: Primary Flip: 166.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 328 / LOW 118 / INVALID 326
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 166.57（全链重定价，覆盖 91%）
Put Wall 150（现价高于该位 2.2%）
最近结构参考: Put Wall 150（现价高于该位 2.2%）
量化视角： 负 Gamma（3207万，无历史分位）｜负 Gamma 缓解（+2501万）｜现价位于 Flip 下方 7.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 155.0C — Vol 1,702 | 最新价 $2.74 | OI 16→1526 (ΔOI +1510张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1510张（+9437.5% vs前日OI），连续性待观察（方向未知）
10-16 150.0P — Vol 1,884 | 最新价 $3.51 | OI 22593→24031 (ΔOI +1438张) | ΔOI/Volume 76.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1438张（+6.4% vs前日OI），连续性待观察（方向未知）
10-16 140.0P — Vol 2,336 | 最新价 $0.57 | OI 5875→7213 (ΔOI +1338张) | ΔOI/Volume 57.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1338张（+22.8% vs前日OI），连续性待观察（方向未知）
10-16 155.0C — Vol 1,096 | 最新价 $1.11 | OI 1769→2458 (ΔOI +689张) | ΔOI/Volume 62.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增689张（+39.0% vs前日OI），连续性待观察（方向未知）
10-16 144.0P — Vol 927 | 最新价 $1.10 | OI 3859→4212 (ΔOI +353张) | ΔOI/Volume 38.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增353张（+9.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,328 张（Put 3,129 / Call 2,199），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 7.1k / P 8.6k，今日成交量: C 1.6k / P 0.1k，平值价格ATM: C $1.08 / P $0.85 ｜ ATM IV 58.7%，预期波动 ±1.3%，Max Pain 152
Top ΔOI: P 148 -2,364 ｜ P 155 -2,249 ｜ C 156 +334

📆 Forward Expiration Structure

10-16  C +1.9k / P +2.2k ｜ Activity HIGH ｜ 7D
10-23  C +50 / P +35 ｜ Activity MEDIUM △ ｜ 14D
10-30  C +1.6k / P -0.8k ｜ Activity HIGH ｜ 21D
11-06  C +34 / P +25 ｜ Activity LOW ｜ 28D

📆 10-16 Forward Structure
存量OI: C 42.6k / P 77.0k，今日变化ΔOI: C +1.9k / P +2.2k，平值价格ATM: C $2.90 / P $5.00 ｜ ATM IV 41.6%，净 delta 敞口 106k shares
Top ΔOI: P 150 +1,438 ｜ P 140 +1,338 ｜ C 155 +689
仓位参考: Max Pain 158 ｜ Call Wall 155（+1.1%，弱）（OI 2.5k） ｜ Put Wall 150（-2.2%）（OI 24.0k）
量化解读： 存量 Put 重｜ATM IV 41.6%｜历史 Rank 98%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 106,303 股

10-23（MEDIUM △）Top ΔOI: 140P +27 ｜ 158P -17
10-23（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 162（+5.7%，弱）（OI 90） ｜ Put Wall 153（-0.2%，弱）（OI 0.4k）

📆 10-30 Forward Structure
存量OI: C 4.3k / P 17.4k，今日变化ΔOI: C +1.6k / P -0.8k，平值价格ATM: C $3.40 / P $5.72 ｜ ATM IV 37.3%，净 delta 敞口 96k shares
Top ΔOI: C 155 +1,510 ｜ P 150 -511 ｜ P 140 -449
仓位参考: Max Pain 153 ｜ Call Wall 155（+1.1%）（OI 1.5k） ｜ Put Wall 150（-2.2%，弱）（OI 7.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.3%｜历史 Rank 98%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 96,025 股

11-06（Activity LOW）仓位参考: Max Pain 154 ｜ Call Wall 150（-2.2%，弱）（OI 39） ｜ Put Wall 150（-2.2%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/XBI_morning.json