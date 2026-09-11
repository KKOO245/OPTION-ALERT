# 期权晨报 2026-09-11（快照 10:20 ET）

📊 市场环境

SPY $765.58 ｜ QQQ $716.48
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-18 170C ΔOI +8,394（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 165.86 → 今开 168.00（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 168.61 ｜ 低 165.59

Options: P/C成交量 0.64 | OI比 0.78 | ATM IV 61.0% | Skew -0.8pp | Term 0.77 | ExpMove ±5.3%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±5.3% ｜ 09-25（14D）±7.2% ｜ 10-02（21D）±9.6% ｜ 10-09（28D）±11.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 33,397,878 | GEX Change vs 上次快照 37,027,983 | Flip: Primary Flip: 164.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 526 / LOW 122 / INVALID 230
结构观察区: Primary Flip 164.59（全链重定价，覆盖 98%）
Put Wall 170（弱结构｜现价低于该位 1.1%） | Call Wall 180（弱结构｜现价低于该位 6.6%）
最近结构参考: Put Wall 170（现价低于该位 1.1%）
量化视角： 正 Gamma（3340万，无历史分位）｜由负转正（+3703万）｜现价位于 Flip 上方 2.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（Put Wall，弱结构） / 170（MaxPain，仅结算参考） / 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 157.5P — Vol 9,775 | 最新价 $1.69 | OI 2406→11473 (ΔOI +9067张) | ΔOI/Volume 92.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9067张（+376.9% vs前日OI），连续性待观察（方向未知）
09-18 170.0C — Vol 15,634 | 最新价 $2.98 | OI 11911→20305 (ΔOI +8394张) | ΔOI/Volume 53.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8394张（+70.5% vs前日OI），连续性待观察（方向未知）
09-18 177.5C — Vol 11,627 | 最新价 $1.14 | OI 3306→11143 (ΔOI +7837张) | ΔOI/Volume 67.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7837张（+237.1% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 15,414 | 最新价 $1.64 | OI 11826→16367 (ΔOI +4541张) | ΔOI/Volume 29.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4541张（+38.4% vs前日OI），连续性待观察（方向未知）
09-18 172.5C — Vol 5,765 | 最新价 $2.25 | OI 3128→7563 (ΔOI +4435张) | ΔOI/Volume 76.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4435张（+141.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 34,274 张（Put 9,067 / Call 25,207），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +30.2k / P +20.7k ｜ Activity MEDIUM △ ｜ 7D
09-25  C +1.4k / P -1.2k ｜ Activity MEDIUM △ ｜ 14D
10-02  C +0.5k / P +3.6k ｜ Activity HIGH ｜ 21D
10-09  C +0.3k / P +1.8k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 305.8k / P 261.9k
今日变化ΔOI: C +30.2k / P +20.7k
平值价格ATM:  C 5.10 / P 3.85
隐含波动率 ATM IV:  46.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 598k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 157 ｜ +9,067 ｜ $1.00 ｜ 名义 $906.7k* ｜ -6.3%
C 170 ｜ +8,394 ｜ $3.70 ｜ 名义 $3.11M* ｜ +1.2%
C 177 ｜ +7,837 ｜ $1.39 ｜ 名义 $1.09M* ｜ +5.6%
结构参考：170（+1.2%） / 157（-6.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 155（结算参考） ｜ Call Wall 170（+1.2%，弱）（OI 20.3k）
量化解读： 存量两侧均衡｜ATM IV 46.2%｜净 delta 敞口 正 597,781 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 170P -4,266 ｜ 170C +538
09-25（MEDIUM △）仓位参考: Max Pain 172（结算参考）

📆 10-02 Forward Structure
存量OI:      C 16.3k / P 22.0k
今日变化ΔOI: C +0.5k / P +3.6k
平值价格ATM:  C 8.20 / P 7.90
隐含波动率 ATM IV:  46.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -139k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 170 ｜ +3,590 ｜ $9.55 ｜ 名义 $3.43M* ｜ +1.2%
C 182 ｜ +221 ｜ $2.84 ｜ 名义 $62.8k* ｜ +8.6%
C 150 ｜ +113 ｜ $20.25 ｜ 名义 $228.8k* ｜ -10.7%
结构参考：170（+1.2%） / 150（-10.7%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 172（结算参考） ｜ Call Wall 180（+7.1%，弱）（OI 2.5k） ｜ Put Wall 170（+1.2%）（OI 4.3k）
量化解读： 存量 Put 重｜ATM IV 46.2%｜净 delta 敞口 负 139,040 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-09 Forward Structure
存量OI:      C 6.9k / P 10.1k
今日变化ΔOI: C +0.3k / P +1.8k
平值价格ATM:  C 9.40 / P 9.29
隐含波动率 ATM IV:  46.8%
净 delta 敞口变化 ΔOI Δ Exposure*: -48k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 170 ｜ +1,258 ｜ $9.30 ｜ 名义 $1.17M* ｜ +1.2%
C 167 ｜ +91 ｜ $9.40 ｜ 名义 $85.5k* ｜ -0.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：170（+1.2%） / 167（-0.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Put Wall 170（+1.2%）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 46.8%｜净 delta 敞口 负 48,425 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/PLTR_morning.json