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


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 51.10 → 收盘 50.51（-1.2%） ｜ 今日高 51.74 ｜ 低 50.34 ｜ 昨收 51.32 → 收盘 50.51（-1.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-16，窗口结束前不做对错判定）

Options: P/C成交量 0.68 | OI比 0.73 | ATM IV 76.9% | Skew -10.7pp | Term 0.80 | ExpMove ±6.6%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -10.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±6.6% ｜ 09-25（14D）±9.4% ｜ 10-02（21D）±11.9% ｜ 10-09（28D）±13.2%
   ⇒ IV–VIX Spread: +61.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,588,755 | GEX Change vs 上次快照 -680,876 | Flip: Primary Flip: 53.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 217 / LOW 55 / INVALID 160
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 53.04（全链重定价，覆盖 90%）
Put Wall 55（弱结构｜现价低于该位 8.2%）
最近结构参考: Flip 53（现价低于该位 4.8%）
量化视角： 负 Gamma（359万，无历史分位）｜负 Gamma 加深（68万）｜现价位于 Flip 下方 4.78%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（Put Wall，弱结构） / 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 53（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 54.0C — Vol 2,116 | 最新价 $0.61 | OI 258→2186 (ΔOI +1928张) | ΔOI/Volume 91.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1928张（+747.3% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 957 | 最新价 $0.44 | OI 3962→4579 (ΔOI +617张) | ΔOI/Volume 64.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增617张（+15.6% vs前日OI），连续性待观察（方向未知）
09-25 55.0P — Vol 25 | 最新价 $5.08 | OI 179→721 (ΔOI +542张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增542张（+302.8% vs前日OI），连续性待观察（方向未知）
09-11 55.0C — Vol 194 | 最新价 $0.04 | OI 825→1344 (ΔOI +519张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增519张（+62.9% vs前日OI），连续性待观察（方向未知）
09-25 59.0C — Vol 47 | 最新价 $0.48 | OI 59→282 (ΔOI +223张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增223张（+378.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,829 张（Put 542 / Call 3,287），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI: C 52.8k / P 42.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.49 / P $1.86 ｜ ATM IV 58.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 55 ｜ Put Wall 55（+8.9%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 58.4%｜历史 Rank 65%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 55

10-02（Activity LOW）仓位参考: Max Pain 59 ｜ Put Wall 50（-1.0%）（OI 1.2k）

10-09（Activity LOW）仓位参考: Max Pain 55 ｜ Call Wall 55（+8.9%）（OI 1.0k） ｜ Put Wall 47（-6.9%）（OI 1.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/MP_evening.json