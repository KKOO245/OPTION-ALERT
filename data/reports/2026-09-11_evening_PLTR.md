# 期权晚报 2026-09-11（快照 16:40 ET）

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
🟡 **近现价集中开仓**: 09-18 170C ΔOI +8,394（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 168.00 → 收盘 167.23（-0.5%） ｜ 今日高 168.61 ｜ 低 165.40 ｜ 昨收 165.86 → 收盘 167.23（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.83 | OI比 0.78 | ATM IV 27.9% | Skew 27.5pp | Term 1.62 | ExpMove ±4.8%（近端） | Rank — (历史不足)
量化视角： 期限结构正常偏陡（Term 1.62）｜保护溢价显著（Skew 27.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（7D）±4.8% ｜ 09-25（14D）±6.8% ｜ 10-02（21D）±8.6% ｜ 10-09（28D）±10.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,986,691 | GEX Change vs 上次快照 1,309,497 | Flip: Primary Flip: 161.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 508 / LOW 87 / INVALID 283
结构观察区: Primary Flip 161.09（全链重定价，覆盖 86%）
Put Wall 170（弱结构｜现价低于该位 1.6%） | Call Wall 180（弱结构｜现价低于该位 7.1%）
最近结构参考: Put Wall 170（现价低于该位 1.6%）
量化视角： 正 Gamma（2899万，无历史分位）｜正 Gamma 增强（+131万）｜现价位于 Flip 上方 3.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（Put Wall，弱结构） / 170（MaxPain，仅结算参考） / 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 157.5P — Vol 3,200 | 最新价 $0.94 | OI 2406→11473 (ΔOI +9067张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9067张（+376.9% vs前日OI），连续性待观察（方向未知）
09-18 170.0C — Vol 9,796 | 最新价 $2.76 | OI 11911→20305 (ΔOI +8394张) | ΔOI/Volume 85.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8394张（+70.5% vs前日OI），连续性待观察（方向未知）
09-18 177.5C — Vol 3,015 | 最新价 $0.89 | OI 3306→11143 (ΔOI +7837张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7837张（+237.1% vs前日OI），连续性待观察（方向未知）
09-18 175.0C — Vol 9,378 | 最新价 $1.33 | OI 11826→16367 (ΔOI +4541张) | ΔOI/Volume 48.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4541张（+38.4% vs前日OI），连续性待观察（方向未知）
09-18 172.5C — Vol 8,472 | 最新价 $1.94 | OI 3128→7563 (ΔOI +4435张) | ΔOI/Volume 52.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4435张（+141.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 34,274 张（Put 9,067 / Call 25,207），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +30.2k / P +20.7k ｜ Activity HIGH ｜ 7D
09-25  C +1.4k / P -1.2k ｜ Activity HIGH ｜ 14D
10-02  C +0.5k / P +3.6k ｜ Activity MEDIUM △ ｜ 21D
10-09  C +0.3k / P +1.8k ｜ Activity HIGH ｜ 28D

📆 09-18 Forward Structure
存量OI:      C 305.8k / P 261.9k
今日变化ΔOI: C +30.2k / P +20.7k
平值价格ATM:  C 3.89 / P 4.05
隐含波动率 ATM IV:  42.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 395k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 157 ｜ +9,067 ｜ $0.94 ｜ 名义 $852.3k* ｜ -5.8%
C 170 ｜ +8,394 ｜ $2.76 ｜ 名义 $2.32M* ｜ +1.7%
C 177 ｜ +7,837 ｜ $0.89 ｜ 名义 $697.5k* ｜ +6.1%
结构参考：170（+1.7%） / 157（-5.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 155（结算参考） ｜ Call Wall 170（+1.7%，弱）（OI 20.3k）
量化解读： 存量两侧均衡｜ATM IV 42.8%｜期限正常（远月高于近端）｜净 delta 敞口 正 394,625 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 24.0k / P 32.2k
今日变化ΔOI: C +1.4k / P -1.2k
平值价格ATM:  C 5.65 / P 5.72
隐含波动率 ATM IV:  43.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 298k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 170 ｜ -4,266 ｜ $7.11 ｜ 名义 $-3.03M* ｜ +1.7%
C 170 ｜ +538 ｜ $4.62 ｜ 名义 $248.6k* ｜ +1.7%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：170（+1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 172（结算参考）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.7%｜净 delta 敞口 正 298,488 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 170P +3,590 ｜ 182C +221
10-02（MEDIUM △）仓位参考: Max Pain 172（结算参考） ｜ Call Wall 180（+7.6%，弱）（OI 2.5k） ｜ Put Wall 170（+1.7%）（OI 4.3k）

📆 10-09 Forward Structure
存量OI:      C 6.9k / P 10.1k
今日变化ΔOI: C +0.3k / P +1.8k
平值价格ATM:  C 8.61 / P 8.10
隐含波动率 ATM IV:  45.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -53k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 170 ｜ +1,258 ｜ $9.32 ｜ 名义 $1.17M* ｜ +1.7%
C 167 ｜ +91 ｜ $8.61 ｜ 名义 $78.4k* ｜ +0.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：170（+1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 170（结算参考） ｜ Put Wall 170（+1.7%）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 45.1%｜净 delta 敞口 负 52,795 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-11/PLTR_evening.json