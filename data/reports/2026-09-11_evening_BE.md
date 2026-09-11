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
🟡 **单日价格波动**: +7.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 268.52 → 收盘 275.75（+2.7%） ｜ 今日高 277.26 ｜ 低 266.12 ｜ 昨收 258.49 → 收盘 275.75（+6.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.66 | OI比 1.23 | ATM IV 55.4% | Skew 7.4pp | Term 1.39 | ExpMove ±7.9%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常偏陡（Term 1.39）｜保护溢价显著（Skew 7.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±7.9% ｜ 09-25（14D）±11.8% ｜ 10-02（21D）±14.6% ｜ 10-09（28D）±17.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,965,562 | GEX Change vs 上次快照 1,299,284 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 540 / LOW 111 / INVALID 381
结构观察区: NO_CROSS
Call Wall 250（弱结构｜现价高于该位 10.3%）
最近结构参考: Call Wall 250（现价高于该位 10.3%）
量化视角： 正 Gamma（2397万，无历史分位）｜正 Gamma 增强（+130万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（MaxPain，仅结算参考） / 250（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 237.5P — Vol 187 | 最新价 $0.03 | OI 285→1365 (ΔOI +1080张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1080张（+378.9% vs前日OI），连续性待观察（方向未知）
09-11 230.0P — Vol 189 | 最新价 $0.03 | OI 2510→3453 (ΔOI +943张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增943张（+37.6% vs前日OI），连续性待观察（方向未知）
09-18 290.0C — Vol 1,088 | 最新价 $5.68 | OI 4655→5597 (ΔOI +942张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增942张（+20.2% vs前日OI），连续性待观察（方向未知）
09-18 295.0C — Vol 280 | 最新价 $4.35 | OI 72→945 (ΔOI +873张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增873张（+1212.5% vs前日OI），连续性待观察（方向未知）
09-11 300.0C — Vol 1,333 | 最新价 $0.01 | OI 3078→3910 (ΔOI +832张) | ΔOI/Volume 62.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增832张（+27.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,670 张（Put 2,023 / Call 2,647），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI: C 131.7k / P 112.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $11.24 / P $10.65 ｜ ATM IV 72.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 232 ｜ Call Wall 250（-9.3%，弱）（OI 20.7k）
量化解读： 存量两侧均衡｜ATM IV 72.5%｜历史 Rank 7%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 245 ｜ Call Wall 300（+8.8%，弱）（OI 1.0k） ｜ Put Wall 250（-9.3%，弱）（OI 2.2k）

10-02（Activity LOW）仓位参考: Max Pain 245 ｜ Call Wall 300（+8.8%，弱）（OI 1.9k）

10-09（Activity LOW）仓位参考: Max Pain 250 ｜ Call Wall 295（+7.0%）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/BE_evening.json