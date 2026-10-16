# 期权晨报 2026-10-16（快照 10:20 ET）

📊 市场环境

SPY $771.01 ｜ QQQ $716.51
VIX 15.93 ↓3.2%（5D +7.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 91C ΔOI +8,029（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 91C ΔOI +8,029 占该期限总 OI 13.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 87.02 → 今开 86.61（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 88.56 ｜ 低 86.36

Options: P/C成交量 1.53 | OI比 0.67 | ATM IV 51.6% | Skew -14.0pp | Term 0.78 | ExpMove ±3.8%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -14.0pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.67）+ 当日成交偏 Put（P/C量 1.53）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.53×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±3.8% ｜ 10-21（5D）±3.0% ｜ 10-23（7D）±4.1% ｜ 10-26（10D）±5.5%
   ⇒ IV–VIX Spread: +35.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,920,690 | GEX Change vs 上次快照 42,022,799 | Flip: Primary Flip: 86.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 541 / LOW 197 / INVALID 438
结构观察区: Primary Flip 86.63（全链重定价，覆盖 82%）
最近结构参考: Flip 87（现价高于该位 1.4%）
量化视角： 正 Gamma（2892万，无历史分位）｜由负转正（+4202万）｜现价位于 Flip 上方 1.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 88（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 87（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 91.0C — Vol 8,097 | 最新价 $0.73 | OI 384→8413 (ΔOI +8029张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8029张（+2090.9% vs前日OI），连续性待观察（方向未知）
10-23 88.0C — Vol 8,091 | 最新价 $1.52 | OI 256→8178 (ΔOI +7922张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7922张（+3094.5% vs前日OI），连续性待观察（方向未知）
11-20 90.0C — Vol 4,643 | 最新价 $3.20 | OI 3757→6751 (ΔOI +2994张) | ΔOI/Volume 64.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2994张（+79.7% vs前日OI），连续性待观察（方向未知）
11-20 105.0C — Vol 2,514 | 最新价 $0.40 | OI 3618→5695 (ΔOI +2077张) | ΔOI/Volume 82.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2077张（+57.4% vs前日OI），连续性待观察（方向未知）
11-20 100.0C — Vol 2,969 | 最新价 $0.87 | OI 4699→6739 (ΔOI +2040张) | ΔOI/Volume 68.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2040张（+43.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,062 张（Put 0 / Call 23,062），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 165.1k / P 110.7k，今日成交量: C 6.2k / P 9.5k，平值价格ATM: C $0.39 / P $0.62 ｜ ATM IV 51.6%，预期波动 ±1.1%，Max Pain 88
Top ΔOI: C 93 -3,341 ｜ C 90 -3,261 ｜ P 85 -1,733

📆 Forward Expiration Structure

10-19  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 3D
10-21  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 5D
10-23  C +18.2k / P +6.4k ｜ Activity HIGH ｜ 7D
10-26  C +0.7k / P +4 ｜ Activity HIGH ｜ 10D

📆 10-19 Forward Structure
存量OI: C 3.1k / P 1.0k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $1.19 / P $2.15 ｜ ATM IV 28.7%，净 delta 敞口 21k shares
Top ΔOI: C 87 +323 ｜ C 86 +101 ｜ C 89 +97
仓位参考: Max Pain 87 ｜ Call Wall 87（-0.9%，弱）（OI 0.9k） ｜ Put Wall 89（+1.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 28.7%｜历史 Rank 85%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 21,195 股

10-21（MEDIUM △）Top ΔOI: 91C +130 ｜ 88C +67
10-21（MEDIUM △）仓位参考: Max Pain 85

📆 10-23 Forward Structure
存量OI: C 33.6k / P 24.4k，今日变化ΔOI: C +18.2k / P +6.4k，平值价格ATM: C $1.72 / P $1.88 ｜ ATM IV 37.7%，净 delta 敞口 619k shares
Top ΔOI: C 91 +8,029 ｜ C 88 +7,922 ｜ P 80 +2,023
仓位参考: Max Pain 86 ｜ Call Wall 91（+3.6%，弱）（OI 8.4k） ｜ Put Wall 85（-3.2%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 37.7%｜历史 Rank 85%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 618,973 股

📆 10-26 Forward Structure
存量OI: C 1.1k / P 0.9k，今日变化ΔOI: C +0.7k / P +4，平值价格ATM: C $1.54 / P $3.30 ｜ ATM IV 34.2%，净 delta 敞口 23k shares
Top ΔOI: C 92 +410 ｜ C 90 +121 ｜ C 86 +81
仓位参考: Max Pain 83 ｜ Call Wall 92（+4.8%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 34.2%｜历史 Rank 85%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 正 22,690 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/GDX_morning.json