# 期权晨报 2026-10-30（快照 10:20 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 18.77 ↑9.1%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 455P ΔOI +70（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 448.76 → 今开 453.60（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 453.60 ｜ 低 442.53

Options: P/C成交量 0.56 | OI比 0.92 | ATM IV 75.9% | Skew -0.0pp | Term 0.41 | ExpMove ±4.3%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.41，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（7D）±4.3% ｜ 11-13（14D）±6.6% ｜ 11-20（21D）±5.9% ｜ 11-27（28D）±7.1%
   ⇒ IV–VIX Spread: +57.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,037,130 | GEX Change vs 上次快照 -234,564 | Flip: Primary Flip: 416.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 294 / LOW 180 / INVALID 522
结构观察区: Primary Flip 416.18（全链重定价，覆盖 90%）
Call Wall 420（弱结构｜现价高于该位 5.8%）
最近结构参考: Call Wall 420（现价高于该位 5.8%）
量化视角： 正 Gamma（204万，无历史分位）｜正 Gamma 减弱（23万）｜现价位于 Flip 上方 6.74%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 416（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 455.0P — Vol 74 | 最新价 $17.50 | OI 6→76 (ΔOI +70张) | ΔOI/Volume 94.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增70张（+1166.7% vs前日OI），连续性待观察（方向未知）
11-06 482.5C — Vol 88 | 最新价 $0.80 | OI 5→49 (ΔOI +44张) | ΔOI/Volume 50.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44张（+880.0% vs前日OI），连续性待观察（方向未知）
10-30 450.0C — Vol 74 | 最新价 $3.45 | OI 145→188 (ΔOI +43张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43张（+29.7% vs前日OI），连续性待观察（方向未知）
11-06 422.5P — Vol 44 | 最新价 $1.85 | OI 3→44 (ΔOI +41张) | ΔOI/Volume 93.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增41张（+1366.7% vs前日OI），连续性待观察（方向未知）
11-20 440.0P — Vol 49 | 最新价 $9.76 | OI 107→147 (ΔOI +40张) | ΔOI/Volume 81.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增40张（+37.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 238 张（Put 151 / Call 87），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 2.5k / P 2.3k，今日成交量: C 68 / P 38，平值价格ATM: C $4.72 / P $2.60 ｜ ATM IV 75.9%，预期波动 ±1.6%，Max Pain 435
Top ΔOI: C 450 +43 ｜ P 430 +33 ｜ P 432 +29

📆 Forward Expiration Structure

11-06  C +79 / P +0.1k ｜ Activity HIGH ｜ 7D
11-13  C +25 / P -2 ｜ Activity MEDIUM △ ｜ 14D
11-20  C -10 / P +0.1k ｜ Activity MEDIUM △ ｜ 21D
11-27  C +5 / P -2 ｜ Activity LOW ｜ 28D

📆 11-06 Forward Structure
存量OI: C 1.4k / P 1.0k，今日变化ΔOI: C +79 / P +0.1k，平值价格ATM: C $10.93 / P $8.17 ｜ ATM IV 38.7%，净 delta 敞口 -766 shares
Top ΔOI: C 482 +44 ｜ P 422 +41 ｜ P 417 +31
仓位参考: Max Pain 428 ｜ Call Wall 430（-3.2%，弱）（OI 0.1k） ｜ Put Wall 420（-5.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.7%｜历史 Rank 92%（近端代理）｜IV/RV 1.71×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 766 股

11-13（MEDIUM △）Top ΔOI: 460C +7 ｜ 470C +7
11-13（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 440（-1.0%，弱）（OI 0.1k） ｜ Put Wall 420（-5.5%，弱）（OI 81）

11-20（MEDIUM △）Top ΔOI: 455P +70 ｜ 440P +40
11-20（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 420（-5.5%，弱）（OI 0.8k） ｜ Put Wall 410（-7.7%，弱）（OI 0.4k）

11-27（Activity LOW）仓位参考: Max Pain 420 ｜ Call Wall 460（+3.5%，弱）（OI 39） ｜ Put Wall 410（-7.7%，弱）（OI 42）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/ISRG_morning.json