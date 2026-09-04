# 期权晚报 2026-09-04（快照 17:18 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 367.81 → 收盘 366.70（-0.3%） ｜ 今日高 369.55 ｜ 低 363.31 ｜ 昨收 369.83 → 收盘 366.70（-0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.02 | OI比 0.44 | ATM IV 78.0% | Skew -11.3pp | Term 0.39 | ExpMove ±3.3%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.39，近月 IV 高于远月）｜Put 保护异常便宜（Skew -11.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±3.3% ｜ 09-18（14D）±6.6% ｜ 09-25（21D）±5.8% ｜ 10-02（28D）±8.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,845,205 | GEX Change vs 上次快照 -380,376 | Flip: Primary Flip: 376.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 230 / LOW 142 / INVALID 522
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 376.56（全链重定价，覆盖 90%）
Call Wall 400（现价低于该位 8.3%）
最近结构参考: Flip 377（现价低于该位 2.6%）
量化视角： 负 Gamma（185万，无历史分位）｜负 Gamma 加深（38万）｜现价位于 Flip 下方 2.62%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 365（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 377（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 375.0C — Vol 8 | 最新价 $0.40 | OI 67→279 (ΔOI +212张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增212张（+316.4% vs前日OI），值得跟踪（方向未知）
09-04 365.0C — Vol 41 | 最新价 $1.60 | OI 10→209 (ΔOI +199张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增199张（+1990.0% vs前日OI），值得跟踪（方向未知）
09-04 370.0C — Vol 9 | 最新价 $0.40 | OI 35→231 (ΔOI +196张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增196张（+560.0% vs前日OI），值得跟踪（方向未知）
09-04 380.0C — Vol 20 | 最新价 $0.04 | OI 235→379 (ΔOI +144张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增144张（+61.3% vs前日OI），值得跟踪（方向未知）
09-18 372.5P — Vol 64（Yahoo补） | 最新价 $10.30 | OI 30→94 (ΔOI +64张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增64张（+213.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 815 张（Put 64 / Call 751），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 0.8k / P 0.8k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 5.90 / P 6.30
隐含波动率 ATM IV:  28.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 375（结算参考） ｜ Call Wall 400（+9.1%，弱）（OI 0.1k） ｜ Put Wall 350（-4.6%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 28.5%｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 378（结算参考） ｜ Call Wall 400（+9.1%，弱）（OI 1.1k）

09-25（Activity LOW）仓位参考: Max Pain 380（结算参考） ｜ Put Wall 370（+0.9%，弱）（OI 0.1k）

10-02（Activity LOW）仓位参考: Max Pain 370（结算参考） ｜ Put Wall 335（-8.6%）（OI 2.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/ISRG_evening.json