# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.49
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 390P ΔOI +1,948（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 460C ΔOI +8,934 占该期限总 OI 10.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 397.45 → 今开 401.94（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 404.40 ｜ 低 386.57

Options: P/C成交量 0.58 | OI比 1.29 | ATM IV 77.0% | Skew 1.6pp | Term 0.44 | ExpMove ±3.1%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.44，近月 IV 高于远月）｜保护溢价薄（Skew 1.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±3.1% ｜ 11-18（5D）±4.5% ｜ 11-20（7D）±5.5% ｜ 11-23（10D）±7.2%
   ⇒ IV–VIX Spread: +57.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 85,173,990 | GEX Change vs 上次快照 -43,116,665 | Flip: Primary Flip: 373.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1413 / LOW 303 / INVALID 958
结构观察区: Primary Flip 373.14（全链重定价，覆盖 98%）
Call Wall 400（现价低于该位 2.9%）
最近结构参考: Call Wall 400（现价低于该位 2.9%）
量化视角： 正 Gamma（8517万，无历史分位）｜正 Gamma 减弱（4312万）｜现价位于 Flip 上方 4.07%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 375（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 373（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-16 460.0C — Vol 9,296 | 最新价 $0.14 | OI 1213→10147 (ΔOI +8934张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8934张（+736.5% vs前日OI），连续性待观察（方向未知）
11-13 410.0C — Vol 46,877 | 最新价 $1.08 | OI 7303→14067 (ΔOI +6764张) | ΔOI/Volume 14.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6764张（+92.6% vs前日OI），连续性待观察（方向未知）
11-13 390.0P — Vol 47,498 | 最新价 $1.94 | OI 3276→8053 (ΔOI +4777张) | ΔOI/Volume 10.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4777张（+145.8% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 6,287 | 最新价 $0.01 | OI 9001→13695 (ΔOI +4694张) | ΔOI/Volume 74.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4694张（+52.1% vs前日OI），连续性待观察（方向未知）
11-13 420.0C — Vol 24,343 | 最新价 $0.32 | OI 4782→8680 (ΔOI +3898张) | ΔOI/Volume 16.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3898张（+81.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,067 张（Put 9,471 / Call 19,596），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 217.3k / P 279.6k，今日成交量: C 302.5k / P 175.2k，平值价格ATM: C $4.00 / P $2.58 ｜ ATM IV 77.0%，预期波动 ±1.7%，Max Pain 375
Top ΔOI: C 410 +6,764 ｜ P 390 +4,777 ｜ C 420 +3,898

📆 Forward Expiration Structure

11-16  C +25.3k / P +10.9k ｜ Activity HIGH ｜ 3D
11-18  C +4.7k / P +3.6k ｜ Activity HIGH ｜ 5D
11-20  C +12.3k / P +21.5k ｜ Activity HIGH ｜ 7D
11-23  C +1.2k / P +0.6k ｜ Activity HIGH ｜ 10D

📆 11-16 Forward Structure
存量OI: C 56.7k / P 31.5k，今日变化ΔOI: C +25.3k / P +10.9k，平值价格ATM: C $6.80 / P $5.10 ｜ ATM IV 40.2%，净 delta 敞口 -104k shares
Top ΔOI: P 390 +1,948
仓位参考: Max Pain 388 ｜ Call Wall 400（+3.0%，弱）（OI 3.0k） ｜ Put Wall 370（-4.7%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 40.2%｜历史 Rank 88%（近端代理）｜IV/RV 0.70×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 103,911 股

📆 11-18 Forward Structure
存量OI: C 14.8k / P 15.6k，今日变化ΔOI: C +4.7k / P +3.6k，平值价格ATM: C $9.05 / P $8.25 ｜ ATM IV 46.2%，净 delta 敞口 3k shares
Top ΔOI: C 430 +1,810 ｜ C 420 +436
仓位参考: Max Pain 390 ｜ Call Wall 410（+5.6%，弱）（OI 1.2k） ｜ Put Wall 392.5（+1.1%）（OI 2.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.2%｜历史 Rank 88%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,068 股

📆 11-20 Forward Structure
存量OI: C 297.9k / P 349.8k，今日变化ΔOI: C +12.3k / P +21.5k，平值价格ATM: C $11.40 / P $9.80 ｜ ATM IV 48.7%，净 delta 敞口 341k shares
Top ΔOI: C 380 +1,934
仓位参考: Max Pain 375 ｜ Call Wall 400（+3.0%，弱）（OI 22.0k）
量化解读： 存量两侧均衡｜ATM IV 48.7%｜历史 Rank 88%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 341,236 股

📆 11-23 Forward Structure
存量OI: C 3.6k / P 4.2k，今日变化ΔOI: C +1.2k / P +0.6k，平值价格ATM: C $16.81 / P $11.03 ｜ ATM IV 44.9%，净 delta 敞口 -1k shares
Top ΔOI: P 392 +184 ｜ C 420 +157
仓位参考: Max Pain 390 ｜ Call Wall 420（+8.2%，弱）（OI 0.4k） ｜ Put Wall 392.5（+1.1%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.9%｜历史 Rank 88%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 负 1,199 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/TSLA_morning.json