# 期权晨报 2026-11-06（快照 10:20 ET）

📊 市场环境

SPY $735.23 ｜ QQQ $656.10
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
🟡 **事件差分**: 11-13 ATM IV 85.0% vs 11-20 72.6%（差 +12.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 11-27 48C ΔOI -769 占该期限总 OI 12.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 33.74 → 今开 34.93（+3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 35.29 ｜ 低 33.82

Options: P/C成交量 0.35 | OI比 0.52 | ATM IV 185.4% | Skew 26.1pp | Term 0.38 | ExpMove ±11.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.38，近月 IV 高于远月）｜保护溢价显著（Skew 26.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±11.4% ｜ 11-20（14D）±11.2% ｜ 11-27（21D）±13.5% ｜ 12-04（28D）±16.9%
   ⇒ IV–VIX Spread: +160.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,346,263 | GEX Change vs 上次快照 2,298,656 | Flip: Primary Flip: 33.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 317 / LOW 72 / INVALID 129
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 33.88（全链重定价，覆盖 95%）
Put Wall 35（现价高于该位 0.3%）
最近结构参考: Put Wall 35（现价高于该位 0.3%）
量化视角： 正 Gamma（135万，无历史分位）｜由负转正（+230万）｜现价位于 Flip 上方 3.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 34（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 30.0P — Vol 2,122 | 最新价 $0.15 | OI 132→2160 (ΔOI +2028张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2028张（+1536.4% vs前日OI），连续性待观察（方向未知）
11-06 40.0C — Vol 2,179 | 最新价 $0.10 | OI 768→2222 (ΔOI +1454张) | ΔOI/Volume 66.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1454张（+189.3% vs前日OI），连续性待观察（方向未知）
11-06 37.5C — Vol 1,297 | 最新价 $0.25 | OI 117→1360 (ΔOI +1243张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1243张（+1062.4% vs前日OI），连续性待观察（方向未知）
11-06 34.0P — Vol 1,407 | 最新价 $1.35 | OI 191→1427 (ΔOI +1236张) | ΔOI/Volume 87.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1236张（+647.1% vs前日OI），连续性待观察（方向未知）
11-06 38.0C — Vol 816 | 最新价 $0.20 | OI 420→1187 (ΔOI +767张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增767张（+182.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,728 张（Put 3,264 / Call 3,464），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 22.9k / P 11.9k，今日成交量: C 1.1k / P 0.4k，平值价格ATM: C $0.74 / P $0.67 ｜ ATM IV 185.4%，预期波动 ±4.0%，Max Pain 37
Top ΔOI: P 30 +2,028 ｜ C 40 +1,454 ｜ C 37 +1,243

📆 Forward Expiration Structure

11-13  C +0.6k / P +0.3k ｜ Activity HIGH ｜ 7D
11-20  C +0.8k / P -41 ｜ Activity HIGH ｜ 14D
11-27  C -0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 21D
12-04  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 28D

📆 11-13 Forward Structure
存量OI: C 7.7k / P 3.3k，今日变化ΔOI: C +0.6k / P +0.3k，平值价格ATM: C $1.75 / P $2.25 ｜ ATM IV 85.0%，净 delta 敞口 30k shares
Top ΔOI: C 38 +140
仓位参考: Max Pain 39 ｜ Call Wall 35（-0.3%，弱）（OI 0.6k） ｜ Put Wall 35（-0.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 85.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 29,692 股

📆 11-20 Forward Structure
存量OI: C 20.4k / P 13.2k，今日变化ΔOI: C +0.8k / P -41，平值价格ATM: C $1.93 / P $2.00 ｜ ATM IV 72.6%，净 delta 敞口 40k shares
Top ΔOI: C 35 +401 ｜ P 42 -187
仓位参考: Max Pain 44 ｜ Put Wall 35（-0.3%）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 72.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,732 股

11-27（MEDIUM △）Top ΔOI: 42P +160
11-27（MEDIUM △）仓位参考: Max Pain 43 ｜ Put Wall 38（+8.2%，弱）（OI 89）

12-04（MEDIUM △）Top ΔOI: 34P +205 ｜ 34C +59
12-04（MEDIUM △）仓位参考: Max Pain 35 ｜ Call Wall 35（-0.3%）（OI 0.5k） ｜ Put Wall 34（-3.2%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 85.0% vs 11-20 72.6%（差 +12.4pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/MP_morning.json