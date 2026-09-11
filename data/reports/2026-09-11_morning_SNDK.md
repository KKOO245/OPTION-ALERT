# 期权晨报 2026-09-11（快照 10:20 ET）

📊 市场环境

SPY $765.58 ｜ QQQ $716.40
VIX 15.94 ↓10.7%（5D +9.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -3.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 1700C ΔOI +384（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,692.59 → 今开 1,713.00（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 1720.33 ｜ 低 1616.80

Options: P/C成交量 0.63 | OI比 0.91 | ATM IV 105.8% | Skew -9.2pp | Term 0.67 | ExpMove ±7.6%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（7D）±7.6% ｜ 09-25（14D）±10.9% ｜ 10-02（21D）±13.4% ｜ 10-09（28D）±17.3%
   ⇒ IV–VIX Spread: +89.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,197,702 | GEX Change vs 上次快照 -5,049,942 | Flip: Primary Flip: 1653.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1777 / LOW 589 / INVALID 1096
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1653.78（全链重定价，覆盖 97%）
Put Wall 1,500（弱结构｜现价高于该位 8.8%）
最近结构参考: Flip 1654（现价低于该位 1.3%）
量化视角： 负 Gamma（320万，无历史分位）｜由正转负（505万）｜现价位于 Flip 下方 1.34%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构）；上方 1,680（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1654（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 1600.0P — Vol 6,636 | 最新价 $2.80 | OI 2251→3626 (ΔOI +1375张) | ΔOI/Volume 20.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1375张（+61.1% vs前日OI），连续性待观察（方向未知）
09-11 1800.0C — Vol 10,998 | 最新价 $2.95 | OI 2970→3835 (ΔOI +865张) | ΔOI/Volume 7.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增865张（+29.1% vs前日OI），连续性待观察（方向未知）
09-11 2250.0C — Vol 732 | 最新价 $0.05 | OI 207→830 (ΔOI +623张) | ΔOI/Volume 85.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+301.0% vs前日OI），连续性待观察（方向未知）
09-11 1700.0C — Vol 7,395 | 最新价 $24.52 | OI 1064→1676 (ΔOI +612张) | ΔOI/Volume 8.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增612张（+57.5% vs前日OI），连续性待观察（方向未知）
09-11 1835.0C — Vol 817 | 最新价 $1.40 | OI 101→692 (ΔOI +591张) | ΔOI/Volume 72.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+585.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,066 张（Put 1,375 / Call 2,691），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +2.9k / P +3.4k ｜ Activity HIGH ｜ 7D
09-25  C +0.4k / P +0.5k ｜ Activity HIGH ｜ 14D
10-02  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 69.8k / P 83.9k
今日变化ΔOI: C +2.9k / P +3.4k
平值价格ATM:  C 58.00 / P 66.12
隐含波动率 ATM IV:  67.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -47k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1700 ｜ +384 ｜ $32.34 ｜ 名义 $1.24M* ｜ +4.2%
P 1600 ｜ +322 ｜ $51.20 ｜ 名义 $1.65M* ｜ -1.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：1700（+4.2%） / 1600（-1.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,500（结算参考）
量化解读： 存量 Put 重｜ATM IV 67.6%｜历史 Rank 60%（近端代理）｜净 delta 敞口 负 47,372 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 8.5k / P 15.9k
今日变化ΔOI: C +0.4k / P +0.5k
平值价格ATM:  C 94.70 / P 84.00
隐含波动率 ATM IV:  67.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1700 ｜ +134 ｜ $57.60 ｜ 名义 $771.8k* ｜ +4.2%
P 1700 ｜ +77 ｜ $131.46 ｜ 名义 $1.01M* ｜ +4.2%
P 1535 ｜ +59 ｜ $46.00 ｜ 名义 $271.4k* ｜ -5.9%
结构参考：1700（+4.2%） / 1535（-5.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,600（结算参考）
量化解读： 存量 Put 重｜ATM IV 67.9%｜历史 Rank 60%（近端代理）｜净 delta 敞口 负 6,043 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 1690P +108 ｜ 1700C +86
10-02（MEDIUM △）仓位参考: Max Pain 1,590（结算参考） ｜ Call Wall 1600（-1.9%，弱）（OI 0.3k） ｜ Put Wall 1500（-8.1%，弱）（OI 0.4k）

📆 10-09 Forward Structure
存量OI:      C 2.2k / P 2.8k
今日变化ΔOI: C +0.6k / P +0.2k
平值价格ATM:  C 180.58 / P 102.00
隐含波动率 ATM IV:  70.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1750 ｜ +77 ｜ $84.00 ｜ 名义 $646.8k* ｜ +7.3%
C 1700 ｜ +69 ｜ $99.62 ｜ 名义 $687.4k* ｜ +4.2%
C 1600 ｜ +48 ｜ $190.00 ｜ 名义 $912.0k* ｜ -1.9%
结构参考：1750（+7.3%） / 1600（-1.9%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 1,650（结算参考） ｜ Call Wall 1750（+7.3%，弱）（OI 0.1k） ｜ Put Wall 1500（-8.1%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.6%｜历史 Rank 60%（近端代理）｜净 delta 敞口 正 14,704 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SNDK_morning.json