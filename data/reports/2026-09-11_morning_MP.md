# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.35 ｜ QQQ $714.04
VIX 15.78 ↓11.6%（5D +8.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
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
🟡 **近现价集中开仓**: 09-18 54C ΔOI +1,928（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 51.32 → 今开 51.10（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 51.74 ｜ 低 50.34

Options: P/C成交量 0.24 | OI比 0.73 | ATM IV 92.8% | Skew 7.7pp | Term 0.69 | ExpMove ±7.2%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 7.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±7.2% ｜ 09-25（14D）±11.1% ｜ 10-02（21D）±16.3% ｜ 10-09（28D）±13.7%
   ⇒ IV–VIX Spread: +77.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,907,880 | GEX Change vs 上次快照 2,505,537 | Flip: Primary Flip: 53.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 240 / LOW 68 / INVALID 124
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 53.27（全链重定价，覆盖 97%）
Put Wall 55（弱结构｜现价低于该位 6.2%）
最近结构参考: Flip 53（现价低于该位 3.1%）
量化视角： 负 Gamma（291万，无历史分位）｜负 Gamma 缓解（+251万）｜现价位于 Flip 下方 3.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 55（Put Wall，弱结构） / 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 53（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 54.0C — Vol 2,160 | 最新价 $1.08 | OI 258→2186 (ΔOI +1928张) | ΔOI/Volume 89.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1928张（+747.3% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 1,004 | 最新价 $0.86 | OI 3962→4579 (ΔOI +617张) | ΔOI/Volume 61.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增617张（+15.6% vs前日OI），连续性待观察（方向未知）
09-25 55.0P — Vol 566 | 最新价 $4.75 | OI 179→721 (ΔOI +542张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增542张（+302.8% vs前日OI），连续性待观察（方向未知）
09-11 55.0C — Vol 703 | 最新价 $0.07 | OI 825→1344 (ΔOI +519张) | ΔOI/Volume 73.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增519张（+62.9% vs前日OI），连续性待观察（方向未知）
09-25 59.0C — Vol 231 | 最新价 $0.74 | OI 59→282 (ΔOI +223张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增223张（+378.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,829 张（Put 542 / Call 3,287），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.3k / P -1.7k ｜ Activity MEDIUM △ ｜ 7D
09-25  C +0.4k / P +0.7k ｜ Activity MEDIUM △ ｜ 14D
10-02  C +17 / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +62 / P +84 ｜ Activity MEDIUM △ ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 52.8k / P 42.9k
今日变化ΔOI: C +2.3k / P -1.7k
平值价格ATM:  C 1.31 / P 2.38
隐含波动率 ATM IV:  62.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 131k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 54 ｜ +1,928 ｜ $0.70 ｜ 名义 $135.0k* ｜ +4.7%
C 55 ｜ +617 ｜ $0.53 ｜ 名义 $32.7k* ｜ +6.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：54（+4.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 55（结算参考） ｜ Put Wall 55（+6.6%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 62.6%｜历史 Rank 88%（近端代理）｜净 delta 敞口 正 130,883 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 55P +542 ｜ 53P +47
09-25（MEDIUM △）仓位参考: Max Pain 55（结算参考）

10-02（MEDIUM △）Top ΔOI: 48P +62 ｜ 50P +21
10-02（MEDIUM △）仓位参考: Max Pain 59（结算参考） ｜ Put Wall 50（-3.1%）（OI 1.2k）

10-09（MEDIUM △）Top ΔOI: 55C -52 ｜ 50P +29
10-09（MEDIUM △）仓位参考: Max Pain 55（结算参考） ｜ Call Wall 55（+6.6%）（OI 1.0k） ｜ Put Wall 47（-8.9%）（OI 1.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/MP_morning.json