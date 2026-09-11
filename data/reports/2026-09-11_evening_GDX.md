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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 98.21 → 收盘 97.10（-1.1%） ｜ 今日高 99.08 ｜ 低 96.23 ｜ 昨收 96.03 → 收盘 97.10（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.76 | OI比 0.96 | ATM IV 40.5% | Skew 7.8pp | Term 1.06 | ExpMove ±4.6%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常（Term 1.06）｜保护溢价显著（Skew 7.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（7D）±4.6% ｜ 09-25（14D）±6.6% ｜ 10-02（21D）±9.6% ｜ 10-09（28D）±9.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,060,970 | GEX Change vs 上次快照 -29,131,013 | Flip: Primary Flip: 98.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 455 / LOW 140 / INVALID 355
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 98.57（全链重定价，覆盖 85%）
Call Wall 100（弱结构｜现价低于该位 2.9%）
最近结构参考: Flip 99（现价低于该位 1.5%）
量化视角： 负 Gamma（2006万，无历史分位）｜由正转负（2913万）｜现价位于 Flip 下方 1.50%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 97（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 99（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 99.0C — Vol 1,110 | 最新价 $1.47 | OI 716→11114 (ΔOI +10398张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10398张（+1452.2% vs前日OI），连续性待观察（方向未知）
09-18 103.0C — Vol 296 | 最新价 $0.53 | OI 2741→12955 (ΔOI +10214张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10214张（+372.6% vs前日OI），连续性待观察（方向未知）
09-11 96.0P — Vol 5,927 | 最新价 $0.01 | OI 7880→13667 (ΔOI +5787张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5787张（+73.4% vs前日OI），连续性待观察（方向未知）
09-18 91.0P — Vol 645 | 最新价 $0.50 | OI 2810→8007 (ΔOI +5197张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5197张（+184.9% vs前日OI），连续性待观察（方向未知）
09-18 93.0P — Vol 8,742 | 最新价 $0.79 | OI 7563→9785 (ΔOI +2222张) | ΔOI/Volume 25.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2222张（+29.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 33,818 张（Put 13,206 / Call 20,612），跨 2 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI: C 276.8k / P 428.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.15 / P $2.35 ｜ ATM IV 43.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 91 ｜ Call Wall 100（+3.0%，弱）（OI 23.5k）
量化解读： 存量 Put 重｜ATM IV 43.4%｜历史 Rank 60%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 96 ｜ Put Wall 90（-7.3%，弱）（OI 1.2k）

10-02（Activity LOW）仓位参考: Max Pain 99 ｜ Put Wall 97（-0.1%）（OI 15.1k）

10-09（Activity LOW）仓位参考: Max Pain 98

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/GDX_evening.json