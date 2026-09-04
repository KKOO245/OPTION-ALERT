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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 98.75 → 收盘 99.26（+0.5%） ｜ 今日高 100.10 ｜ 低 98.02 ｜ 昨收 101.49 → 收盘 99.26（-2.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-11，窗口结束前不做对错判定）

Options: P/C成交量 0.86 | OI比 0.98 | ATM IV 71.0% | Skew -4.0pp | Term 0.61 | ExpMove ±4.5%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（7D）±4.5% ｜ 09-18（14D）±6.9% ｜ 09-25（21D）±8.2% ｜ 10-02（28D）±9.6%
   ⇒ IV–VIX Spread: +56.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 6,784,921 | GEX Change vs 上次快照 -14,988,154 | Flip: Primary Flip: 98.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 519 / LOW 160 / INVALID 299
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 98.57（全链重定价，覆盖 87%）
Call Wall 100（弱结构｜现价低于该位 0.7%）
最近结构参考: Flip 99（现价高于该位 0.7%）
量化视角： 正 Gamma（678万，无历史分位）｜正 Gamma 减弱（1499万）｜现价位于 Flip 上方 0.70%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 99（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 99（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 102.0C — Vol 9,329 | 最新价 $1.16 | OI 213→5513 (ΔOI +5300张) | ΔOI/Volume 56.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5300张（+2488.3% vs前日OI），连续性待观察（方向未知）
09-11 106.0C — Vol 7,885 | 最新价 $0.39 | OI 146→5226 (ΔOI +5080张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5080张（+3479.4% vs前日OI），连续性待观察（方向未知）
09-18 80.0P — Vol 21 | 最新价 $0.09 | OI 66246→71131 (ΔOI +4885张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增4885张（+7.4% vs前日OI），值得跟踪（方向未知）
09-04 98.0P — Vol 14,430 | 最新价 $0.01 | OI 3276→7510 (ΔOI +4234张) | ΔOI/Volume 29.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4234张（+129.2% vs前日OI），连续性待观察（方向未知）
09-18 95.0P — Vol 3,272 | 最新价 $1.55 | OI 11067→14922 (ΔOI +3855张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3855张（+34.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,354 张（Put 12,974 / Call 10,380），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 14D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 21D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 49.0k / P 36.0k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.39 / P 2.10
隐含波动率 ATM IV:  40.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 96（结算参考） ｜ Call Wall 99（-0.3%，弱）（OI 7.1k） ｜ Put Wall 92（-7.3%，弱）（OI 6.2k）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 98%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 90（结算参考） ｜ Call Wall 100（+0.7%，弱）（OI 23.8k）

09-25（Activity LOW）仓位参考: Max Pain 96（结算参考） ｜ Call Wall 105（+5.8%，弱）（OI 0.7k）

10-02（Activity LOW）仓位参考: Max Pain 99（结算参考） ｜ Put Wall 97（-2.3%）（OI 15.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/GDX_evening.json