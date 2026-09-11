# 期权晨报 2026-09-11（快照 10:20 ET）

📊 市场环境

SPY $765.58 ｜ QQQ $716.43
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
🟡 **近现价集中开仓**: 09-25 16C ΔOI +112（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 16.04 → 今开 16.03（-0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 16.12 ｜ 低 15.78

Options: P/C成交量 0.99 | OI比 0.44 | ATM IV 90.8% | Skew -24.1pp | Term 0.87 | ExpMove ±8.9%（近端） | Rank 11%
量化视角： IV 历史低位（Rank 11%，期权偏便宜）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -24.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±8.9% ｜ 09-25（14D）±12.8% ｜ 10-02（21D）±16.0% ｜ 10-09（28D）±17.4%
   ⇒ IV–VIX Spread: +74.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,901,341 | GEX Change vs 上次快照 -202,663 | Flip: Primary Flip: 16.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 226 / LOW 95 / INVALID 163
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.55（全链重定价，覆盖 97%）
Put Wall 15（弱结构｜现价高于该位 5.9%）
最近结构参考: Flip 17（现价低于该位 4.0%）
量化视角： 负 Gamma（390万，无历史分位）｜负 Gamma 加深（20万）｜现价位于 Flip 下方 4.03%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 97%）。
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

09-18  C +3.6k / P -1.0k ｜ Activity HIGH ｜ 7D
09-25  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 14D
10-02  C +0.2k / P +0.2k ｜ Activity HIGH ｜ 21D
10-09  C +50 / P +0.3k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 120.7k / P 64.1k
今日变化ΔOI: C +3.6k / P -1.0k
平值价格ATM:  C 0.75 / P 0.67
隐含波动率 ATM IV:  77.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 275k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 18 ｜ +3,179 ｜ $0.18 ｜ 名义 $57.2k* ｜ +13.4%
P 25 ｜ -2,820 ｜ $8.85 ｜ 名义 $-2.50M* ｜ +57.4%
P 17 ｜ +1,103 ｜ $1.33 ｜ 名义 $146.7k* ｜ +7.1%
结构参考：18（+13.4%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 19（结算参考） ｜ Put Wall 15（-5.5%，弱）（OI 8.8k）
量化解读： 存量 Call 重｜ATM IV 77.4%｜历史 Rank 11%（近端代理）｜净 delta 敞口 正 275,046 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 9.4k / P 3.8k
今日变化ΔOI: C +0.2k / P +0.3k
平值价格ATM:  C 1.08 / P 0.95
隐含波动率 ATM IV:  77.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 15 ｜ +159 ｜ $0.49 ｜ 名义 $7.8k* ｜ -5.5%
C 16 ｜ +112 ｜ $1.08 ｜ 名义 $12.1k* ｜ +0.8%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：16（+0.8%） / 15（-5.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 15（-5.5%）（OI 0.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.0%｜历史 Rank 11%（近端代理）｜净 delta 敞口 负 4,085 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 7.6k / P 2.8k
今日变化ΔOI: C +0.2k / P +0.2k
平值价格ATM:  C 1.36 / P 1.18
隐含波动率 ATM IV:  81.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 1k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 17 ｜ +48 ｜ $1.80 ｜ 名义 $8.6k* ｜ +7.1%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：17（+7.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考）
量化解读： 存量 Call 重｜ATM IV 81.0%｜历史 Rank 11%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,360 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-09 Forward Structure
存量OI:      C 4.0k / P 2.2k
今日变化ΔOI: C +50 / P +0.3k
平值价格ATM:  C 1.45 / P 1.32
隐含波动率 ATM IV:  79.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 15 ｜ +111 ｜ $0.85 ｜ 名义 $9.4k* ｜ -5.5%
P 14 ｜ +73 ｜ $0.65 ｜ 名义 $4.7k* ｜ -8.7%
P 16 ｜ +43 ｜ $1.32 ｜ 名义 $5.7k* ｜ +0.8%
结构参考：16（+0.8%） / 15（-5.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 16（+0.8%）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.0%｜历史 Rank 11%（近端代理）｜净 delta 敞口 负 9,843 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=14 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=14）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/USAR_morning.json