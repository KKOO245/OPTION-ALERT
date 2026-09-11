# 期权晨报 2026-09-11（快照 10:20 ET）

📊 市场环境

SPY $765.58 ｜ QQQ $716.39
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
🟡 **单日价格波动**: +6.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-25 280C ΔOI +205（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 258.49 → 今开 268.52（+3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 277.26 ｜ 低 266.12

Options: P/C成交量 0.80 | OI比 1.23 | ATM IV 121.6% | Skew -4.2pp | Term 0.66 | ExpMove ±9.0%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±9.0% ｜ 09-25（14D）±12.5% ｜ 10-02（21D）±15.3% ｜ 10-09（28D）±17.7%
   ⇒ IV–VIX Spread: +105.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,552,189 | GEX Change vs 上次快照 7,252,352 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 680 / LOW 117 / INVALID 235
结构观察区: NO_CROSS
Call Wall 250（弱结构｜现价高于该位 10.1%）
最近结构参考: Call Wall 250（现价高于该位 10.1%）
量化视角： 正 Gamma（2455万，无历史分位）｜正 Gamma 增强（+725万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（MaxPain，仅结算参考） / 250（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 237.5P — Vol 1,339 | 最新价 $0.33 | OI 285→1365 (ΔOI +1080张) | ΔOI/Volume 80.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1080张（+378.9% vs前日OI），连续性待观察（方向未知）
09-11 230.0P — Vol 1,309 | 最新价 $0.10 | OI 2510→3453 (ΔOI +943张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增943张（+37.6% vs前日OI），连续性待观察（方向未知）
09-18 290.0C — Vol 2,213 | 最新价 $3.15 | OI 4655→5597 (ΔOI +942张) | ΔOI/Volume 42.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增942张（+20.2% vs前日OI），连续性待观察（方向未知）
09-18 295.0C — Vol 919 | 最新价 $2.47 | OI 72→945 (ΔOI +873张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增873张（+1212.5% vs前日OI），连续性待观察（方向未知）
09-11 300.0C — Vol 2,601 | 最新价 $0.05 | OI 3078→3910 (ΔOI +832张) | ΔOI/Volume 32.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增832张（+27.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,670 张（Put 2,023 / Call 2,647），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +3.9k / P +5.1k ｜ Activity HIGH ｜ 7D
09-25  C +1.0k / P +1.5k ｜ Activity HIGH ｜ 14D
10-02  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +0.3k / P +0.5k ｜ Activity MEDIUM △ ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 131.7k / P 112.9k
今日变化ΔOI: C +3.9k / P +5.1k
平值价格ATM:  C 12.60 / P 12.15
隐含波动率 ATM IV:  80.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 46k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 290 ｜ +942 ｜ $6.80 ｜ 名义 $640.6k* ｜ +5.3%
C 295 ｜ +873 ｜ $5.40 ｜ 名义 $471.4k* ｜ +7.1%
P 255 ｜ +825 ｜ $4.55 ｜ 名义 $375.4k* ｜ -7.4%
结构参考：290（+5.3%） / 255（-7.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 232（结算参考） ｜ Call Wall 250（-9.2%，弱）（OI 20.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 80.0%｜历史 Rank 78%（近端代理）｜净 delta 敞口 正 45,921 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 11.4k / P 17.0k
今日变化ΔOI: C +1.0k / P +1.5k
平值价格ATM:  C 17.90 / P 16.40
隐含波动率 ATM IV:  80.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 235 ｜ +323 ｜ $3.37 ｜ 名义 $108.9k* ｜ -14.7%
C 280 ｜ +205 ｜ $16.12 ｜ 名义 $330.5k* ｜ +1.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：280（+1.7%） / 235（-14.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 245（结算参考） ｜ Call Wall 300（+9.0%，弱）（OI 1.0k） ｜ Put Wall 250（-9.2%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 80.0%｜历史 Rank 78%（近端代理）｜净 delta 敞口 正 13,965 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 275C +131 ｜ 245C +100
10-02（MEDIUM △）仓位参考: Max Pain 245（结算参考） ｜ Call Wall 300（+9.0%，弱）（OI 1.9k）

10-09（MEDIUM △）仓位参考: Max Pain 250（结算参考） ｜ Call Wall 295（+7.1%）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/BE_morning.json