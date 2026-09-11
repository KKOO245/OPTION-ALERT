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
🟡 **单日价格波动**: -2.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,713.00 → 收盘 1,633.35（-4.6%） ｜ 今日高 1720.33 ｜ 低 1616.80 ｜ 昨收 1,692.59 → 收盘 1,633.35（-3.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-16，窗口结束前不做对错判定）

Options: P/C成交量 0.62 | OI比 0.91 | ATM IV 69.2% | Skew -20.9pp | Term 0.96 | ExpMove ±6.6%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -20.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（7D）±6.6% ｜ 09-25（14D）±9.5% ｜ 10-02（21D）±12.9% ｜ 10-09（28D）±15.9%
   ⇒ IV–VIX Spread: +53.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,051,773 | GEX Change vs 上次快照 -4,232,272 | Flip: Primary Flip: 1665.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 1720 / LOW 537 / INVALID 1205
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1665.77（全链重定价，覆盖 82%）
Put Wall 1,500（弱结构｜现价高于该位 8.9%）
最近结构参考: Flip 1666（现价低于该位 1.9%）
量化视角： 负 Gamma（305万，无历史分位）｜由正转负（423万）｜现价位于 Flip 下方 1.95%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构）；上方 1,680（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1666（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 1600.0P — Vol 11,173 | 最新价 $0.01 | OI 2251→3626 (ΔOI +1375张) | ΔOI/Volume 12.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1375张（+61.1% vs前日OI），连续性待观察（方向未知）
09-11 1800.0C — Vol 5,378 | 最新价 $0.05 | OI 2970→3835 (ΔOI +865张) | ΔOI/Volume 16.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增865张（+29.1% vs前日OI），连续性待观察（方向未知）
09-11 2250.0C — Vol 41 | 最新价 $0.05 | OI 207→830 (ΔOI +623张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+301.0% vs前日OI），连续性待观察（方向未知）
09-11 1700.0C — Vol 14,366 | 最新价 $0.05 | OI 1064→1676 (ΔOI +612张) | ΔOI/Volume 4.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增612张（+57.5% vs前日OI），连续性待观察（方向未知）
09-11 1835.0C — Vol 651 | 最新价 $0.05 | OI 101→692 (ΔOI +591张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+585.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,066 张（Put 1,375 / Call 2,691），跨 1 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI: C 69.8k / P 83.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $53.45 / P $53.99 ｜ ATM IV 59.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,500
量化解读： 存量 Put 重｜ATM IV 59.2%｜历史 Rank 24%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 1,600

10-02（Activity LOW）仓位参考: Max Pain 1,590 ｜ Call Wall 1600（-2.0%，弱）（OI 0.3k） ｜ Put Wall 1500（-8.2%，弱）（OI 0.4k）

10-09（Activity LOW）仓位参考: Max Pain 1,650 ｜ Call Wall 1750（+7.1%，弱）（OI 0.1k） ｜ Put Wall 1500（-8.2%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SNDK_evening.json