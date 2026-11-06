# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $740.12 ｜ QQQ $659.92
VIX 24.90 ↓11.6%（5D +28.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
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
🟡 **近现价集中开仓**: 11-09 87C ΔOI +1,119（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-09 87C ΔOI +1,119 占该期限总 OI 21.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 85.75 → 今开 84.39（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 86.14 ｜ 低 84.01

Options: P/C成交量 1.11 | OI比 0.46 | ATM IV 76.3% | Skew 10.0pp | Term 0.60 | ExpMove ±3.3%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价显著（Skew 10.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-09（3D）±3.3% ｜ 11-11（5D）±5.2% ｜ 11-13（7D）±5.9% ｜ 11-16（10D）±6.9%
   ⇒ IV–VIX Spread: +51.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 25,732,567 | GEX Change vs 上次快照 702,704 | Flip: Primary Flip: 81.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 546 / LOW 134 / INVALID 460
结构观察区: Primary Flip 81.44（全链重定价，覆盖 97%）
Call Wall 81（弱结构｜现价高于该位 5.5%）
最近结构参考: Flip 81（现价高于该位 5.0%）
量化视角： 正 Gamma（2573万，无历史分位）｜正 Gamma 增强（+70万）｜现价位于 Flip 上方 4.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 78（MaxPain，仅结算参考） / 81（Call Wall，弱结构）。
• Gamma 区域：切换参考 81（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 92.0C — Vol 5,035 | 最新价 $0.66 | OI 215→5239 (ΔOI +5024张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5024张（+2336.7% vs前日OI），连续性待观察（方向未知）
11-13 89.0C — Vol 5,079 | 最新价 $1.35 | OI 312→5135 (ΔOI +4823张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4823张（+1545.8% vs前日OI），连续性待观察（方向未知）
11-06 25.0P — Vol 4,444 | 最新价 $0.01 | OI 0→4444 (ΔOI +4444张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4444张（前日OI缺失），连续性待观察（方向未知）
11-06 83.0P — Vol 5,146 | 最新价 $0.35 | OI 1032→5379 (ΔOI +4347张) | ΔOI/Volume 84.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4347张（+421.2% vs前日OI），连续性待观察（方向未知）
11-06 84.0P — Vol 6,435 | 最新价 $0.59 | OI 653→3467 (ΔOI +2814张) | ΔOI/Volume 43.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2814张（+430.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,452 张（Put 11,605 / Call 9,847），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 96.9k / P 44.4k，今日成交量: C 1.7k / P 1.9k，平值价格ATM: C $0.92 / P $0.52 ｜ ATM IV 76.3%，预期波动 ±1.7%，Max Pain 78
Top ΔOI: P 25 +4,444 ｜ P 83 +4,347 ｜ P 72 -2,957

📆 Forward Expiration Structure

11-09  C +1.2k / P +0.8k ｜ Activity HIGH ｜ 3D
11-11  C +0.2k / P +52 ｜ Activity LOW ｜ 5D
11-13  C +16.8k / P +1.0k ｜ Activity HIGH ｜ 7D
11-16  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 10D

📆 11-09 Forward Structure
存量OI: C 2.9k / P 2.3k，今日变化ΔOI: C +1.2k / P +0.8k，平值价格ATM: C $1.75 / P $1.09 ｜ ATM IV 42.9%，净 delta 敞口 8k shares
Top ΔOI: C 87 +1,119 ｜ P 84 +270 ｜ P 87 +201
仓位参考: Max Pain 83 ｜ Call Wall 87（+1.8%）（OI 1.2k） ｜ Put Wall 84（-1.7%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 42.9%｜历史 Rank 99%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,664 股

11-11（Activity LOW）仓位参考: Max Pain 78 ｜ Call Wall 85（-0.6%）（OI 2.2k）

📆 11-13 Forward Structure
存量OI: C 29.0k / P 24.2k，今日变化ΔOI: C +16.8k / P +1.0k，平值价格ATM: C $2.35 / P $2.71 ｜ ATM IV 49.0%，净 delta 敞口 437k shares
Top ΔOI: C 92 +5,024 ｜ C 89 +4,823 ｜ C 88 +2,655
仓位参考: Max Pain 82 ｜ Call Wall 89（+4.1%，弱）（OI 5.1k） ｜ Put Wall 82（-4.1%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 49.0%｜历史 Rank 99%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 436,537 股

11-16（MEDIUM △）Top ΔOI: 87C +138 ｜ 80P +61
11-16（MEDIUM △）仓位参考: Max Pain 82 ｜ Call Wall 80（-6.4%，弱）（OI 0.2k） ｜ Put Wall 81（-5.3%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/GDX_morning.json