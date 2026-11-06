# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.16 ｜ QQQ $656.10
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
🟡 **近现价集中开仓**: 11-20 870P ΔOI +1,931（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 806.43 → 今开 898.27（+11.4%） | 较昨收变动（含盘初走势） ｜ 今日高 912.09 ｜ 低 830.22

Options: P/C成交量 0.65 | OI比 0.49 | ATM IV 202.0% | Skew 15.8pp | Term 0.47 | ExpMove ±13.1%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.47，近月 IV 高于远月）｜保护溢价显著（Skew 15.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±13.1% ｜ 11-20（14D）±17.8% ｜ 11-27（21D）±24.1% ｜ 12-04（28D）±21.6%
   ⇒ IV–VIX Spread: +177.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 380,780 | GEX Change vs 上次快照 6,242,162 | Flip: Primary Flip: 866.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1671 / LOW 545 / INVALID 1532
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 866.68（全链重定价，覆盖 100%）
Put Wall 800（弱结构｜现价高于该位 9.0%）
最近结构参考: Flip 867（现价高于该位 0.6%）
量化视角： 正 Gamma（38万，无历史分位）｜由负转正（+624万）｜现价位于 Flip 上方 0.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 800（Put Wall，弱结构）；上方 925（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 867（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 1000.0C — Vol 10,158 | 最新价 $0.80 | OI 245→3094 (ΔOI +2849张) | ΔOI/Volume 28.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2849张（+1162.9% vs前日OI），连续性待观察（方向未知）
11-06 900.0C — Vol 9,352 | 最新价 $5.49 | OI 26→2517 (ΔOI +2491张) | ΔOI/Volume 26.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2491张（+9580.8% vs前日OI），连续性待观察（方向未知）
11-20 870.0P — Vol 2,442 | 最新价 $99.90 | OI 210→2141 (ΔOI +1931张) | ΔOI/Volume 79.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1931张（+919.5% vs前日OI），连续性待观察（方向未知）
11-06 950.0C — Vol 6,086 | 最新价 $1.90 | OI 24→1442 (ΔOI +1418张) | ΔOI/Volume 23.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1418张（+5908.3% vs前日OI），连续性待观察（方向未知）
11-13 700.0P — Vol 2,956 | 最新价 $26.10 | OI 289→1577 (ΔOI +1288张) | ΔOI/Volume 43.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1288张（+445.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,977 张（Put 3,219 / Call 6,758），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $23M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 70.5k / P 34.4k，今日成交量: C 34.6k / P 22.6k，平值价格ATM: C $19.95 / P $18.00 ｜ ATM IV 202.0%，预期波动 ±4.4%，Max Pain 925
Top ΔOI: C 1000 +2,849 ｜ C 900 +2,491 ｜ C 950 +1,418

📆 Forward Expiration Structure

11-13  C +9.2k / P +4.8k ｜ Activity HIGH ｜ 7D
11-20  C +9.5k / P -1.8k ｜ Activity HIGH ｜ 14D
11-27  C +1.3k / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
12-04  C +1.5k / P +0.4k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 28.5k / P 16.7k，今日变化ΔOI: C +9.2k / P +4.8k，平值价格ATM: C $58.70 / P $55.50 ｜ ATM IV 116.1%，净 delta 敞口 276k shares
Top ΔOI: P 700 +1,288 ｜ C 950 +1,044 ｜ C 1300 +559
仓位参考: Max Pain 995 ｜ Call Wall 950（+9.0%，弱）（OI 1.0k） ｜ Put Wall 820（-5.9%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 116.1%｜历史 Rank 98%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 275,926 股

📆 11-20 Forward Structure
存量OI: C 66.9k / P 51.4k，今日变化ΔOI: C +9.5k / P -1.8k，平值价格ATM: C $83.39 / P $72.00 ｜ ATM IV 107.5%，净 delta 敞口 733k shares
Top ΔOI: P 870 +1,931 ｜ P 1680 -1,102 ｜ C 1600 +1,085
仓位参考: Max Pain 1,160 ｜ Call Wall 800（-8.2%，弱）（OI 2.3k） ｜ Put Wall 870（-0.2%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 107.5%｜历史 Rank 98%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 732,760 股

11-27（MEDIUM △）Top ΔOI: 1000C +154 ｜ 860P +112
11-27（MEDIUM △）仓位参考: Max Pain 1,200 ｜ Put Wall 930（+6.7%，弱）（OI 0.2k）

📆 12-04 Forward Structure
存量OI: C 6.2k / P 4.3k，今日变化ΔOI: C +1.5k / P +0.4k，平值价格ATM: C $104.35 / P $83.80 ｜ ATM IV 95.4%，净 delta 敞口 34k shares
Top ΔOI: C 1500 -187 ｜ C 1120 +168 ｜ C 1095 +150
仓位参考: Max Pain 1,095 ｜ Call Wall 950（+9.0%，弱）（OI 0.1k） ｜ Put Wall 820（-5.9%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 95.4%｜历史 Rank 98%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 34,173 股

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 116.1% vs 11-20 107.5%（差 +8.5pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SNDK_morning.json