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


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 18.65 → 收盘 17.61（-5.6%） ｜ 今日高 19.30 ｜ 低 17.25 ｜ 昨收 17.69 → 收盘 17.61（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.28 | OI比 0.31 | ATM IV 143.7% | Skew 13.7pp | Term 0.56 | ExpMove ±7.8%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价显著（Skew 13.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±7.8% ｜ 09-18（14D）±12.1% ｜ 09-25（21D）±14.6% ｜ 10-02（28D）±18.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,703,906 | GEX Change vs 上次快照 -1,910,772 | Flip: Primary Flip: 16.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 235 / LOW 84 / INVALID 209
结构观察区: Primary Flip 16.42（全链重定价，覆盖 88%）
最近结构参考: Flip 16（现价高于该位 7.3%）
量化视角： 正 Gamma（570万，无历史分位）｜正 Gamma 减弱（191万）｜现价位于 Flip 上方 7.26%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 23.0C — Vol 4 | 最新价 $0.25 | OI 50→4079 (ΔOI +4029张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4029张（+8058.0% vs前日OI），连续性待观察（方向未知）
10-09 22.0C — Vol 40 | 最新价 $0.51 | OI 14→3013 (ΔOI +2999张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2999张（+21421.4% vs前日OI），连续性待观察（方向未知）
09-18 20.5C — Vol 6 | 最新价 $0.22 | OI 156→698 (ΔOI +542张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增542张（+347.4% vs前日OI），连续性待观察（方向未知）
09-11 17.0P — Vol 1,030 | 最新价 $0.39 | OI 519→966 (ΔOI +447张) | ΔOI/Volume 43.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增447张（+86.1% vs前日OI），连续性待观察（方向未知）
09-18 21.0C — Vol 46 | 最新价 $0.16 | OI 1406→1792 (ΔOI +386张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增386张（+27.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,403 张（Put 447 / Call 7,956），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 16.5k / P 4.6k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 0.78 / P 0.60
隐含波动率 ATM IV:  67.2%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 18（结算参考） ｜ Put Wall 17（-3.5%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 67.2%｜历史 Rank 73%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 20（结算参考）

09-25（Activity LOW）仓位参考: Max Pain 18（结算参考）

10-02（Activity LOW）仓位参考: Max Pain 18（结算参考）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/USAR_evening.json