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


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 130.50 → 收盘 132.53（+1.6%） ｜ 今日高 134.45 ｜ 低 130.39 ｜ 昨收 131.17 → 收盘 132.53（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 0.81 | ATM IV 45.5% | Skew 9.7pp | Term 1.13 | ExpMove ±5.5%（近端） | Rank — (历史不足)
量化视角： 期限结构正常（Term 1.13）｜保护溢价显著（Skew 9.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（7D）±5.5% ｜ 09-25（14D）±8.0% ｜ 10-02（21D）±9.7% ｜ 10-09（28D）±11.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,347,165 | GEX Change vs 上次快照 1,356,571 | Flip: Primary Flip: 123.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 525 / LOW 111 / INVALID 204
结构观察区: Primary Flip 123.37（全链重定价，覆盖 90%）
最近结构参考: Flip 123（现价高于该位 7.4%）
量化视角： 正 Gamma（1335万，无历史分位）｜正 Gamma 增强（+136万）｜现价位于 Flip 上方 7.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 134（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 123（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 170.0C — Vol 331 | 最新价 $0.83 | OI 2625→4673 (ΔOI +2048张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2048张（+78.0% vs前日OI），连续性待观察（方向未知）
09-11 144.0C — Vol 101 | 最新价 $0.04 | OI 623→1839 (ΔOI +1216张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1216张（+195.2% vs前日OI），连续性待观察（方向未知）
09-11 124.0P — Vol 45 | 最新价 $0.01 | OI 1399→2524 (ΔOI +1125张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1125张（+80.4% vs前日OI），连续性待观察（方向未知）
09-11 140.0C — Vol 818 | 最新价 $0.01 | OI 3720→4559 (ΔOI +839张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增839张（+22.6% vs前日OI），连续性待观察（方向未知）
09-11 134.0C — Vol 2,909 | 最新价 $0.01 | OI 739→1559 (ΔOI +820张) | ΔOI/Volume 28.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增820张（+111.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,048 张（Put 1,125 / Call 4,923），跨 2 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI: C 110.3k / P 106.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.40 / P $3.90 ｜ ATM IV 49.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 120 ｜ Call Wall 120（-9.5%，弱）（OI 9.9k）
量化解读： 存量两侧均衡｜ATM IV 49.6%｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 132 ｜ Call Wall 145（+9.4%）（OI 1.8k）

10-02（Activity LOW）仓位参考: Max Pain 131

10-09（Activity LOW）仓位参考: Max Pain 140 ｜ Put Wall 140（+5.6%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/NOW_evening.json