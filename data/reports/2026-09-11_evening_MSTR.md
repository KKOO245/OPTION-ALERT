# 期权晚报 2026-09-11（快照 17:15 ET）

📊 市场环境

SPY $764.29 ｜ QQQ $714.88
VIX 15.84 ↓11.2%（5D +9.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.2　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 3.4 ｜ 前值 3.4　✅ 今日已公布
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 0.4 ｜ 前值 0.1　✅ 今日已公布
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 2.4 ｜ 前值 2.5　✅ 今日已公布
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 47.8 ｜ 前值 51.7　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: +2.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 130.53 → 收盘 130.97（+0.3%） ｜ 今日高 137.89 ｜ 低 129.28 ｜ 昨收 128.56 → 收盘 130.97（+1.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.31 | OI比 0.74 | ATM IV 54.2% | Skew -7.2pp | Term 1.25 | ExpMove ±7.5%（近端） | Rank 6%
量化视角： IV 历史低位（Rank 6%，期权偏便宜）｜期限结构正常偏陡（Term 1.25）｜Put 保护异常便宜（Skew -7.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±7.5% ｜ 09-25（14D）±10.4% ｜ 10-02（21D）±12.8% ｜ 10-09（28D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,522,377 | GEX Change vs 上次快照 -39,559,829 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 762 / LOW 131 / INVALID 359
结构观察区: NO_CROSS
量化视角： 正 Gamma（2952万，无历史分位）｜正 Gamma 减弱（3956万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 80.0P — Vol 6,253 | 最新价 $0.03 | OI 11722→24744 (ΔOI +13022张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13022张（+111.1% vs前日OI），连续性待观察（方向未知）
09-18 125.0P — Vol 11,729 | 最新价 $2.26 | OI 3756→7386 (ΔOI +3630张) | ΔOI/Volume 30.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3630张（+96.7% vs前日OI），连续性待观察（方向未知）
09-18 132.0C — Vol 5,870 | 最新价 $4.43 | OI 546→3294 (ΔOI +2748张) | ΔOI/Volume 46.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2748张（+503.3% vs前日OI），连续性待观察（方向未知）
09-18 135.0C — Vol 22,738 | 最新价 $3.30 | OI 4170→6882 (ΔOI +2712张) | ΔOI/Volume 11.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2712张（+65.0% vs前日OI），连续性待观察（方向未知）
09-18 138.0C — Vol 14,729 | 最新价 $2.43 | OI 0→2597 (ΔOI +2597张) | ΔOI/Volume 17.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2597张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 24,709 张（Put 16,652 / Call 8,057），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI: C 296.0k / P 236.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.95 / P $4.83 ｜ ATM IV 67.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 120
量化解读： 存量 Call 重｜ATM IV 67.0%｜历史 Rank 6%（近端代理）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 125 ｜ Call Wall 140（+6.9%，弱）（OI 1.6k）

10-02（Activity LOW）仓位参考: Max Pain 130

10-09（Activity LOW）仓位参考: Max Pain 135 ｜ Put Wall 130（-0.7%，弱）（OI 1.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/MSTR_evening.json