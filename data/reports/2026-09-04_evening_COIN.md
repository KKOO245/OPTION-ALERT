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


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 185.30 → 收盘 184.64（-0.4%） ｜ 今日高 189.00 ｜ 低 182.89 ｜ 昨收 192.70 → 收盘 184.64（-4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 0.59 | ATM IV 69.7% | Skew -2.3pp | Term 0.92 | ExpMove ±6.7%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±6.7% ｜ 09-18（14D）±9.9% ｜ 09-25（21D）±12.1% ｜ 10-02（28D）±13.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,952,416 | GEX Change vs 上次快照 -3,795,892 | Flip: Primary Flip: 157.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 478 / LOW 169 / INVALID 413
结构观察区: Primary Flip 157.35（全链重定价，覆盖 82%）
Call Wall 200（弱结构｜现价低于该位 7.7%）
最近结构参考: Call Wall 200（现价低于该位 7.7%）
量化视角： 正 Gamma（2995万，无历史分位）｜正 Gamma 减弱（380万）｜现价位于 Flip 上方 17.35%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 157（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 205.0C — Vol 986 | 最新价 $1.20 | OI 1006→5300 (ΔOI +4294张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4294张（+426.8% vs前日OI），连续性待观察（方向未知）
09-11 197.5C — Vol 466 | 最新价 $2.22 | OI 158→3628 (ΔOI +3470张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3470张（+2196.2% vs前日OI），连续性待观察（方向未知）
09-04 197.5C — Vol 4,864 | 最新价 $0.01 | OI 817→3299 (ΔOI +2482张) | ΔOI/Volume 51.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2482张（+303.8% vs前日OI），连续性待观察（方向未知）
09-18 320.0C — Vol 8 | 最新价 $0.06 | OI 972→2707 (ΔOI +1735张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1735张（+178.5% vs前日OI），连续性待观察（方向未知）
09-04 190.0P — Vol 1,845 | 最新价 $5.38 | OI 1171→2711 (ΔOI +1540张) | ΔOI/Volume 83.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1540张（+131.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,521 张（Put 1,540 / Call 11,981），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 42.9k / P 20.1k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 5.95 / P 6.40
隐含波动率 ATM IV:  59.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 180（结算参考） ｜ Call Wall 180（-2.5%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 59.6%｜历史 Rank 31%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 170（结算参考） ｜ Call Wall 170（-7.9%）（OI 16.0k）

09-25（Activity LOW）仓位参考: Max Pain 170（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 190（结算参考） ｜ Put Wall 172.5（-6.6%，弱）（OI 1.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/COIN_evening.json