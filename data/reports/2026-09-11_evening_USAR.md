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
🟡 **单日价格波动**: -2.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 16.03 → 收盘 15.56（-3.0%） ｜ 今日高 16.12 ｜ 低 15.51 ｜ 昨收 16.04 → 收盘 15.56（-3.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-16，窗口结束前不做对错判定）

Options: P/C成交量 1.19 | OI比 0.44 | ATM IV 172.2% | Skew -76.9pp | Term 0.43 | ExpMove ±7.4%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.43，近月 IV 高于远月）｜Put 保护异常便宜（Skew -76.9pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.44）+ 当日成交偏 Put（P/C量 1.19）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.19×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±7.4% ｜ 09-25（14D）±11.9% ｜ 10-02（21D）±14.2% ｜ 10-09（28D）±18.3%
   ⇒ IV–VIX Spread: +156.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,201,050 | GEX Change vs 上次快照 -1,240,443 | Flip: Primary Flip: 16.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 215 / LOW 73 / INVALID 196
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.35（全链重定价，覆盖 95%）
Put Wall 15（弱结构｜现价高于该位 3.7%）
最近结构参考: Put Wall 15（现价高于该位 3.7%）
量化视角： 负 Gamma（420万，无历史分位）｜负 Gamma 加深（124万）｜现价位于 Flip 下方 4.80%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 18.0C — Vol 2,053 | 最新价 $0.08 | OI 3161→6340 (ΔOI +3179张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3179张（+100.6% vs前日OI），连续性待观察（方向未知）
10-16 18.0C — Vol 310 | 最新价 $0.67 | OI 1196→3851 (ΔOI +2655张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2655张（+222.0% vs前日OI），连续性待观察（方向未知）
10-16 15.0P — Vol 2,807 | 最新价 $1.10 | OI 929→3560 (ΔOI +2631张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2631张（+283.2% vs前日OI），连续性待观察（方向未知）
09-18 17.0P — Vol 1,647 | 最新价 $1.59 | OI 2157→3260 (ΔOI +1103张) | ΔOI/Volume 67.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1103张（+51.1% vs前日OI），连续性待观察（方向未知）
09-11 17.0C — Vol 312 | 最新价 $0.01 | OI 335→994 (ΔOI +659张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增659张（+196.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,227 张（Put 3,734 / Call 6,493），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 14D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-18 Forward Structure
存量OI: C 120.7k / P 64.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.57 / P $0.58 ｜ ATM IV 67.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 19 ｜ Put Wall 15（-3.6%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 67.5%｜历史 Rank 91%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 15（-3.6%）（OI 0.8k）

10-02（Activity LOW）仓位参考: Max Pain 18

10-09（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 16（+2.8%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/USAR_evening.json