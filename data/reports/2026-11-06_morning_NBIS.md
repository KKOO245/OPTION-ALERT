# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-13（7D）ATM IV 175.5% vs 11-20 146.7%（差 +28.8pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 120.37 → 今开 130.64（+8.5%） | 较昨收变动（含盘初走势） ｜ 今日高 136.87 ｜ 低 128.38

Options: P/C成交量 0.68 | OI比 0.40 | ATM IV 188.6% | Skew 6.3pp | Term 0.67 | ExpMove ±20.0%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价显著（Skew 6.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±20.0% ｜ 11-20（14D）±23.1% ｜ 11-27（21D）±24.8% ｜ 12-04（28D）±26.3%
   ⇒ IV–VIX Spread: +163.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,246,940 | GEX Change vs 上次快照 12,090,369 | Flip: Primary Flip: 129.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 573 / LOW 64 / INVALID 215
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 129.27（全链重定价，覆盖 93%）
最近结构参考: Flip 129（现价高于该位 1.7%）
量化视角： 正 Gamma（125万，无历史分位）｜由负转正（+1209万）｜现价位于 Flip 上方 1.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 129（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 110.0P — Vol 6,112 | 最新价 $10.60 | OI 1641→5659 (ΔOI +4018张) | ΔOI/Volume 65.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4018张（+244.8% vs前日OI），连续性待观察（方向未知）
11-06 125.0C — Vol 9,442 | 最新价 $3.10 | OI 18→3540 (ΔOI +3522张) | ΔOI/Volume 37.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3522张（+19566.7% vs前日OI），连续性待观察（方向未知）
11-06 110.0P — Vol 16,720 | 最新价 $1.52 | OI 541→3634 (ΔOI +3093张) | ΔOI/Volume 18.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3093张（+571.7% vs前日OI），连续性待观察（方向未知）
11-27 225.0P — Vol 2,346 | 最新价 $106.62 | OI 77→2404 (ΔOI +2327张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2327张（+3022.1% vs前日OI），连续性待观察（方向未知）
11-13 160.0C — Vol 2,789 | 最新价 $2.50 | OI 1300→3297 (ΔOI +1997张) | ΔOI/Volume 71.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1997张（+153.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,957 张（Put 9,438 / Call 5,519），跨 4 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 103.5k / P 41.2k，今日成交量: C 16.7k / P 11.4k，平值价格ATM: C $2.38 / P $2.96 ｜ ATM IV 188.6%，预期波动 ±4.1%，Max Pain 137
Top ΔOI: C 125 +3,522 ｜ P 110 +3,093 ｜ C 130 +1,928

📆 Forward Expiration Structure

11-13  C +8.5k / P -0.7k ｜ Activity HIGH ｜ 7D
11-20  C +4.5k / P +0.5k ｜ Activity MEDIUM △ ｜ 14D
11-27  C +0.8k / P +5.1k ｜ Activity HIGH ｜ 21D
12-04  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 51.4k / P 29.3k，今日变化ΔOI: C +8.5k / P -0.7k，平值价格ATM: C $12.81 / P $13.50 ｜ ATM IV 175.5%，净 delta 敞口 785k shares
Top ΔOI: C 160 +1,997 ｜ P 225 -1,899 ｜ C 150 +1,554
仓位参考: Max Pain 160 ｜ Put Wall 130（-1.2%）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 175.5%｜历史 Rank 99%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 785,319 股

11-20（MEDIUM △）Top ΔOI: 110P +4,018 ｜ 115P -1,552
11-20（MEDIUM △）仓位参考: Max Pain 178 ｜ Put Wall 140（+6.4%，弱）（OI 5.2k）

📆 11-27 Forward Structure
存量OI: C 11.9k / P 15.4k，今日变化ΔOI: C +0.8k / P +5.1k，平值价格ATM: C $17.63 / P $15.00 ｜ ATM IV 130.5%，净 delta 敞口 -404k shares
Top ΔOI: P 225 +2,327 ｜ P 230 +1,286 ｜ P 220 +1,239
仓位参考: Max Pain 195 ｜ Put Wall 140（+6.4%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 130.5%｜历史 Rank 99%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 404,493 股

📆 12-04 Forward Structure
存量OI: C 3.1k / P 4.0k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $18.25 / P $16.40 ｜ ATM IV 126.4%，净 delta 敞口 17k shares
Top ΔOI: C 140 +217 ｜ P 100 +115 ｜ C 150 +102
仓位参考: Max Pain 160 ｜ Call Wall 140（+6.4%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 126.4%｜历史 Rank 99%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 17,372 股

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 175.5% vs 11-20 146.7%（差 +28.8pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/NBIS_morning.json