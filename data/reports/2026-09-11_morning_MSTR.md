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

🔍 重点速览
🟡 **单日价格波动**: +6.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 132C ΔOI +2,748（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 128.56 → 今开 130.53（+1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 137.89 ｜ 低 129.28

Options: P/C成交量 0.14 | OI比 0.74 | ATM IV 109.6% | Skew -6.2pp | Term 0.65 | ExpMove ±8.3%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±8.3% ｜ 09-25（14D）±11.5% ｜ 10-02（21D）±13.8% ｜ 10-09（28D）±15.8%
   ⇒ IV–VIX Spread: +93.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 69,082,206 | GEX Change vs 上次快照 50,556,836 | Flip: Primary Flip: 123.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 808 / LOW 154 / INVALID 290
结构观察区: Primary Flip 123.43（全链重定价，覆盖 99%）
最近结构参考: Flip 123（现价高于该位 10.4%）
量化视角： 正 Gamma（6908万，无历史分位）｜正 Gamma 增强（+5056万）｜现价位于 Flip 上方 10.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 123（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 80.0P — Vol 13,238 | 最新价 $0.06 | OI 11722→24744 (ΔOI +13022张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13022张（+111.1% vs前日OI），连续性待观察（方向未知）
09-18 125.0P — Vol 5,881 | 最新价 $3.65 | OI 3756→7386 (ΔOI +3630张) | ΔOI/Volume 61.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3630张（+96.7% vs前日OI），连续性待观察（方向未知）
09-18 132.0C — Vol 3,362 | 最新价 $4.35 | OI 546→3294 (ΔOI +2748张) | ΔOI/Volume 81.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2748张（+503.3% vs前日OI），连续性待观察（方向未知）
09-18 135.0C — Vol 4,078 | 最新价 $3.25 | OI 4170→6882 (ΔOI +2712张) | ΔOI/Volume 66.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2712张（+65.0% vs前日OI），连续性待观察（方向未知）
09-18 138.0C — Vol 2,664 | 最新价 $2.50 | OI 0→2597 (ΔOI +2597张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2597张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 24,709 张（Put 16,652 / Call 8,057），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +24.9k / P +25.9k ｜ Activity HIGH ｜ 7D
09-25  C +1.2k / P +4.7k ｜ Activity HIGH ｜ 14D
10-02  C +0.2k / P +3.0k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +0.3k / P +3.0k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 296.0k / P 236.8k
今日变化ΔOI: C +24.9k / P +25.9k
平值价格ATM:  C 5.57 / P 5.72
隐含波动率 ATM IV:  73.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 892k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 125 ｜ +3,630 ｜ $1.46 ｜ 名义 $530.0k* ｜ -8.3%
C 132 ｜ +2,748 ｜ $7.40 ｜ 名义 $2.03M* ｜ -3.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：125（-8.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 120（结算参考）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.7%｜历史 Rank 86%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 892,466 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 22.7k / P 42.0k
今日变化ΔOI: C +1.2k / P +4.7k
平值价格ATM:  C 7.66 / P 8.00
隐含波动率 ATM IV:  71.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 13k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 125（结算参考） ｜ Call Wall 140（+2.8%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 71.3%｜历史 Rank 86%（近端代理）｜净 delta 敞口 正 13,131 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）仓位参考: Max Pain 130（结算参考） ｜ Call Wall 145（+6.4%，弱）（OI 2.6k）

📆 10-09 Forward Structure
存量OI:      C 5.6k / P 14.1k
今日变化ΔOI: C +0.3k / P +3.0k
平值价格ATM:  C 11.00 / P 10.57
隐含波动率 ATM IV:  71.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -27k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 100 ｜ +541 ｜ $0.93 ｜ 名义 $50.3k* ｜ -26.6%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：100（-26.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 135（结算参考） ｜ Put Wall 130（-4.6%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 71.7%｜历史 Rank 86%（近端代理）｜净 delta 敞口 负 26,813 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/MSTR_morning.json