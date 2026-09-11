# 期权晨报 2026-09-11（快照 10:40 ET）

📊 市场环境

SPY $764.35 ｜ QQQ $714.09
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
🟡 **近现价集中开仓**: 09-25 155C ΔOI +788（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 148.18 → 今开 150.07（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 150.59 ｜ 低 145.92

Options: P/C成交量 0.31 | OI比 1.27 | ATM IV 76.7% | Skew -0.6pp | Term 0.66 | ExpMove ±6.1%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±6.1% ｜ 09-25（14D）±7.9% ｜ 10-02（21D）±9.7% ｜ 10-09（28D）±11.0%
   ⇒ IV–VIX Spread: +60.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 48,349,735 | GEX Change vs 上次快照 15,983,622 | Flip: Primary Flip: 145.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 606 / LOW 176 / INVALID 322
结构观察区: Primary Flip 145.23（全链重定价，覆盖 98%）
Call Wall 150（弱结构｜现价低于该位 1.2%）
最近结构参考: Call Wall 150（现价低于该位 1.2%）
量化视角： 正 Gamma（4835万，无历史分位）｜正 Gamma 增强（+1598万）｜现价位于 Flip 上方 2.01%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 147（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 145（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 90.0P — Vol 7,896 | 最新价 $0.01 | OI 11434→19078 (ΔOI +7644张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7644张（+66.8% vs前日OI），连续性待观察（方向未知）
09-11 152.5C — Vol 77,798 | 最新价 $0.66 | OI 8898→14799 (ΔOI +5901张) | ΔOI/Volume 7.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5901张（+66.3% vs前日OI），连续性待观察（方向未知）
09-11 155.0C — Vol 90,719 | 最新价 $0.32 | OI 14669→19576 (ΔOI +4907张) | ΔOI/Volume 5.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4907张（+33.5% vs前日OI），连续性待观察（方向未知）
09-11 160.0C — Vol 66,005 | 最新价 $0.09 | OI 26419→30385 (ΔOI +3966张) | ΔOI/Volume 6.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3966张（+15.0% vs前日OI），连续性待观察（方向未知）
09-11 150.0C — Vol 70,976 | 最新价 $1.35 | OI 13765→16711 (ΔOI +2946张) | ΔOI/Volume 4.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2946张（+21.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 25,364 张（Put 7,644 / Call 17,720），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +4.9k / P +12.7k ｜ Activity HIGH ｜ 7D
09-25  C +3.6k / P +1.4k ｜ Activity HIGH ｜ 14D
10-02  C +1.3k / P +1.3k ｜ Activity HIGH ｜ 21D
10-09  C +1.2k / P +0.8k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 595.0k / P 490.9k
今日变化ΔOI: C +4.9k / P +12.7k
平值价格ATM:  C 3.33 / P 5.66
隐含波动率 ATM IV:  52.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -74k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 165 ｜ -2,184 ｜ $0.47 ｜ 名义 $-102.6k* ｜ +11.4%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 145（结算参考） ｜ Call Wall 155（+4.6%，弱）（OI 54.0k） ｜ Put Wall 150（+1.2%）（OI 46.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.3%｜历史 Rank 92%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 73,519 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 51.5k / P 67.1k
今日变化ΔOI: C +3.6k / P +1.4k
平值价格ATM:  C 5.84 / P 5.86
隐含波动率 ATM IV:  50.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 37k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 155 ｜ +788 ｜ $3.25 ｜ 名义 $256.1k* ｜ +4.6%
C 170 ｜ -761 ｜ $0.78 ｜ 名义 $-59.4k* ｜ +14.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：155（+4.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 144（结算参考）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.7%｜历史 Rank 92%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,821 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 24.8k / P 36.6k
今日变化ΔOI: C +1.3k / P +1.3k
平值价格ATM:  C 7.50 / P 6.85
隐含波动率 ATM IV:  50.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -19k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 170 ｜ +520 ｜ $1.45 ｜ 名义 $75.4k* ｜ +14.7%
P 145 ｜ +466 ｜ $5.14 ｜ 名义 $239.5k* ｜ -2.1%
P 140 ｜ +214 ｜ $3.70 ｜ 名义 $79.2k* ｜ -5.5%
结构参考：170（+14.7%） / 145（-2.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 145（结算参考）
量化解读： 存量 Put 重｜ATM IV 50.6%｜历史 Rank 92%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,676 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-09 Forward Structure
存量OI:      C 11.0k / P 12.0k
今日变化ΔOI: C +1.2k / P +0.8k
平值价格ATM:  C 8.45 / P 7.80
隐含波动率 ATM IV:  50.3%
净 delta 敞口变化 ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 160 ｜ +335 ｜ $3.96 ｜ 名义 $132.7k* ｜ +8.0%
P 150 ｜ +205 ｜ $8.90 ｜ 名义 $182.4k* ｜ +1.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：160（+8.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 146（结算参考） ｜ Put Wall 135（-8.9%）（OI 2.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.3%｜历史 Rank 92%（近端代理）｜净 delta 敞口 正 5,804 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/SPCX_morning.json