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


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 764.72 → 收盘 764.29（-0.1%） ｜ 今日高 766.37 ｜ 低 763.60 ｜ 昨收 757.83 → 收盘 764.29（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.22 | OI比 1.70 | ATM IV 8.9% | Skew 19.0pp | Term 1.40 | ExpMove ±0.5%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常偏陡（Term 1.40）｜保护溢价显著（Skew 19.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.22×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.70×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 43% ｜ P/C OI(近端) 38%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 43%）｜近端持仓结构中性（P/C OI 分位 38%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-14（3D）±0.5% ｜ 09-15（4D）±0.7% ｜ 09-16（5D）±1.0% ｜ 09-17（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -592,218,180 | GEX Change vs 上次快照 -166,536,521 | Flip: Primary Flip: 769.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 3228 / LOW 344 / INVALID 2046
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 769.21（全链重定价，覆盖 93%）
Call Wall 800（弱结构｜现价低于该位 4.5%）
最近结构参考: Flip 769（现价低于该位 0.6%）
量化视角： 负 Gamma（5.92亿，历史分位 43%，中性区）｜负 Gamma 加深（1.67亿）｜现价位于 Flip 下方 0.64%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 761（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 750.0P — Vol 100,820 | 最新价 $1.80 | OI 64944→186670 (ΔOI +121726张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增121726张（+187.4% vs前日OI），连续性待观察（方向未知）
09-18 730.0P — Vol 76,244 | 最新价 $0.52 | OI 50899→115705 (ΔOI +64806张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增64806张（+127.3% vs前日OI），连续性待观察（方向未知）
09-18 740.0P — Vol 8,446 | 最新价 $0.90 | OI 68727→109347 (ΔOI +40620张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40620张（+59.1% vs前日OI），连续性待观察（方向未知）
09-11 732.0P — Vol 10,011 | 最新价 $0.01 | OI 12660→35851 (ΔOI +23191张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23191张（+183.2% vs前日OI），连续性待观察（方向未知）
09-11 755.0P — Vol 62,191 | 最新价 $0.01 | OI 35224→54327 (ΔOI +19103张) | ΔOI/Volume 30.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19103张（+54.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 269,446 张（Put 269,446 / Call 0），跨 2 个期限｜近端保护（5 档，距现价 ≤5%，权利金合计约 $22M，买/卖方向不可观测）｜彩票/名义 2 档（价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-14  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-15  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-16  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-17  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-14 Forward Structure
存量OI: C 71.7k / P 98.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.19 / P $1.78 ｜ ATM IV 7.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 759 ｜ Call Wall 765（+0.1%，弱）（OI 6.9k） ｜ Put Wall 700（-8.4%）（OI 20.1k）
量化解读： 存量 Put 重｜ATM IV 7.1%｜历史 Rank 16%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

09-15（Activity LOW）仓位参考: Max Pain 760 ｜ Call Wall 770（+0.7%，弱）（OI 4.8k） ｜ Put Wall 760（-0.6%，弱）（OI 22.0k）

09-16（Activity LOW）仓位参考: Max Pain 760 ｜ Call Wall 770（+0.7%）（OI 2.8k） ｜ Put Wall 735（-3.8%，弱）（OI 2.7k）

09-17（Activity LOW）仓位参考: Max Pain 760 ｜ Call Wall 775（+1.4%，弱）（OI 2.6k） ｜ Put Wall 745（-2.5%）（OI 4.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SPY_evening.json