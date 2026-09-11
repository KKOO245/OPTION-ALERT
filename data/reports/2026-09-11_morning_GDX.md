# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.35 ｜ QQQ $714.11
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
🟡 **单日价格波动**: +2.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 99C ΔOI +10,398（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 96.03 → 今开 98.21（+2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 99.08 ｜ 低 97.02

Options: P/C成交量 1.42 | OI比 0.96 | ATM IV 63.9% | Skew -9.5pp | Term 0.70 | ExpMove ±5.2%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.5pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.42×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（7D）±5.2% ｜ 09-25（14D）±8.1% ｜ 10-02（21D）±9.8% ｜ 10-09（28D）±9.2%
   ⇒ IV–VIX Spread: +48.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 9,070,043 | GEX Change vs 上次快照 36,670,202 | Flip: Primary Flip: 97.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 583 / LOW 180 / INVALID 187
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 97.87（全链重定价，覆盖 93%）
Call Wall 100（弱结构｜现价低于该位 1.8%）
最近结构参考: Flip 98（现价高于该位 0.4%）
量化视角： 正 Gamma（907万，无历史分位）｜由负转正（+3667万）｜现价位于 Flip 上方 0.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 97（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 98（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 99.0C — Vol 11,134 | 最新价 $1.69 | OI 716→11114 (ΔOI +10398张) | ΔOI/Volume 93.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10398张（+1452.2% vs前日OI），连续性待观察（方向未知）
09-18 103.0C — Vol 11,324 | 最新价 $0.75 | OI 2741→12955 (ΔOI +10214张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10214张（+372.6% vs前日OI），连续性待观察（方向未知）
09-11 96.0P — Vol 8,991 | 最新价 $1.37 | OI 7880→13667 (ΔOI +5787张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5787张（+73.4% vs前日OI），连续性待观察（方向未知）
09-18 91.0P — Vol 6,193 | 最新价 $1.00 | OI 2810→8007 (ΔOI +5197张) | ΔOI/Volume 83.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5197张（+184.9% vs前日OI），连续性待观察（方向未知）
09-18 93.0P — Vol 4,295 | 最新价 $1.52 | OI 7563→9785 (ΔOI +2222张) | ΔOI/Volume 51.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2222张（+29.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 33,818 张（Put 13,206 / Call 20,612），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +21.7k / P +11.6k ｜ Activity HIGH ｜ 7D
09-25  C +87 / P +1.7k ｜ Activity HIGH ｜ 14D
10-02  C +85 / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 276.8k / P 428.3k
今日变化ΔOI: C +21.7k / P +11.6k
平值价格ATM:  C 2.60 / P 2.50
隐含波动率 ATM IV:  46.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 484k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 99 ｜ +10,398 ｜ $2.04 ｜ 名义 $2.12M* ｜ +0.8%
C 103 ｜ +10,214 ｜ $0.91 ｜ 名义 $929.5k* ｜ +4.9%
P 91 ｜ +5,197 ｜ $0.43 ｜ 名义 $223.5k* ｜ -7.4%
结构参考：99（+0.8%） / 91（-7.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 91（结算参考） ｜ Call Wall 100（+1.8%，弱）（OI 23.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.4%｜历史 Rank 95%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 483,948 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 7.1k / P 9.6k
今日变化ΔOI: C +87 / P +1.7k
平值价格ATM:  C 3.46 / P 4.46
隐含波动率 ATM IV:  44.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -30k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 95 ｜ +352 ｜ $2.15 ｜ 名义 $75.7k* ｜ -3.3%
C 105 ｜ -317 ｜ $1.21 ｜ 名义 $-38.4k* ｜ +6.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：95（-3.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 96（结算参考） ｜ Put Wall 90（-8.4%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 44.9%｜历史 Rank 95%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 29,690 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 96P +130 ｜ 104C +58
10-02（MEDIUM △）仓位参考: Max Pain 99（结算参考） ｜ Put Wall 97（-1.3%）（OI 15.1k）

10-09（MEDIUM △）Top ΔOI: 103P +91 ｜ 108C +85
10-09（MEDIUM △）仓位参考: Max Pain 98（结算参考）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/GDX_morning.json