# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.42 ｜ QQQ $714.88
VIX 15.78 ↓11.6%（5D +8.6%） ｜ Vol Regime: NORMAL
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

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 16.04 → 今开 16.03（-0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 16.12 ｜ 低 15.69

Options: P/C成交量 0.44 | OI比 0.44 | ATM IV 105.4% | Skew -5.0pp | Term 0.74 | ExpMove ±8.4%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±8.4% ｜ 09-25（14D）±11.8% ｜ 10-02（21D）±15.0% ｜ 10-09（28D）±17.6%
   ⇒ IV–VIX Spread: +89.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,960,607 | GEX Change vs 上次快照 738,070 | Flip: Primary Flip: 16.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 240 / LOW 87 / INVALID 157
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.45（全链重定价，覆盖 97%）
Put Wall 15（弱结构｜现价高于该位 6.0%）
最近结构参考: Flip 16（现价低于该位 3.4%）
量化视角： 负 Gamma（296万，无历史分位）｜负 Gamma 缓解（+74万）｜现价位于 Flip 下方 3.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 18.0C — Vol 4,139 | 最新价 $0.18 | OI 3161→6340 (ΔOI +3179张) | ΔOI/Volume 76.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3179张（+100.6% vs前日OI），连续性待观察（方向未知）
10-16 18.0C — Vol 3,132 | 最新价 $0.89 | OI 1196→3851 (ΔOI +2655张) | ΔOI/Volume 84.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2655张（+222.0% vs前日OI），连续性待观察（方向未知）
10-16 15.0P — Vol 2,805 | 最新价 $1.00 | OI 929→3560 (ΔOI +2631张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2631张（+283.2% vs前日OI），连续性待观察（方向未知）
09-18 17.0P — Vol 1,477 | 最新价 $1.33 | OI 2157→3260 (ΔOI +1103张) | ΔOI/Volume 74.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1103张（+51.1% vs前日OI），连续性待观察（方向未知）
09-11 17.0C — Vol 1,267 | 最新价 $0.05 | OI 335→994 (ΔOI +659张) | ΔOI/Volume 52.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增659张（+196.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,227 张（Put 3,734 / Call 6,493），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +3.6k / P -1.0k ｜ Activity MEDIUM △ ｜ 7D
09-25  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 14D
10-02  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +50 / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 120.7k / P 64.1k
今日变化ΔOI: C +3.6k / P -1.0k
平值价格ATM:  C 0.63 / P 0.71
隐含波动率 ATM IV:  75.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 252k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 25 ｜ -2,820 ｜ $8.85 ｜ 名义 $-2.50M* ｜ +57.2%
P 17 ｜ +1,103 ｜ $1.38 ｜ 名义 $152.2k* ｜ +6.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：17（+6.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Put Wall 15（-5.7%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 75.6%｜历史 Rank 26%（近端代理）｜净 delta 敞口 正 252,189 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 15P +159 ｜ 16C +112
09-25（MEDIUM △）仓位参考: Max Pain 18（结算参考） ｜ Put Wall 15（-5.7%）（OI 0.8k）

10-02（MEDIUM △）Top ΔOI: 17P +48
10-02（MEDIUM △）仓位参考: Max Pain 18（结算参考）

10-09（MEDIUM △）Top ΔOI: 15P +111 ｜ 14P +73
10-09（MEDIUM △）仓位参考: Max Pain 18（结算参考） ｜ Put Wall 16（+0.6%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/USAR_morning.json