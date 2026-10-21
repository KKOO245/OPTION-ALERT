# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $773.28 ｜ QQQ $725.20
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 438.00 → 今开 402.49（-8.1%） | 较昨收变动（含盘初走势） ｜ 今日高 432.49 ｜ 低 398.99

Options: P/C成交量 1.15 | OI比 1.01 | ATM IV 59.7% | Skew -9.2pp | Term 0.56 | ExpMove ±3.1%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜Put 保护异常便宜（Skew -9.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±3.1% ｜ 10-30（9D）±7.6% ｜ 11-06（16D）±0.0% ｜ 11-13（23D）±11.2%
   ⇒ IV–VIX Spread: +42.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -858,345 | GEX Change vs 上次快照 -3,153,129 | Flip: Primary Flip: 423.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 347 / LOW 170 / INVALID 449
结构观察区: Primary Flip 423.06（全链重定价，覆盖 97%）
最近结构参考: Flip 423（现价低于该位 1.0%）
量化视角： 负 Gamma（86万，无历史分位）｜由正转负（315万）｜现价位于 Flip 下方 1.05%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 425（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 423（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 520.0C — Vol 854 | 最新价 $0.79 | OI 31→760 (ΔOI +729张) | ΔOI/Volume 85.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增729张（+2351.6% vs前日OI），连续性待观察（方向未知）
10-23 390.0P — Vol 706 | 最新价 $2.00 | OI 145→671 (ΔOI +526张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增526张（+362.8% vs前日OI），连续性待观察（方向未知）
11-20 410.0P — Vol 391 | 最新价 $10.29 | OI 97→450 (ΔOI +353张) | ΔOI/Volume 90.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增353张（+363.9% vs前日OI），连续性待观察（方向未知）
10-23 400.0P — Vol 721 | 最新价 $3.45 | OI 469→816 (ΔOI +347张) | ΔOI/Volume 48.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增347张（+74.0% vs前日OI），连续性待观察（方向未知）
10-23 435.0P — Vol 328 | 最新价 $14.92 | OI 21→305 (ΔOI +284张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增284张（+1352.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,239 张（Put 1,510 / Call 729），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +3.2k / P +3.8k ｜ Activity HIGH ｜ 2D
10-30  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 9D
11-06  C +20 / P +85 ｜ Activity MEDIUM △ ｜ 16D
11-13  C +35 / P +47 ｜ Activity LOW ｜ 23D

📆 10-23 Forward Structure
存量OI: C 8.6k / P 8.7k，今日变化ΔOI: C +3.2k / P +3.8k，平值价格ATM: C $8.64 / P $4.46 ｜ ATM IV 59.7%，净 delta 敞口 -65k shares
Top ΔOI: P 390 +526 ｜ P 400 +347
仓位参考: Max Pain 425 ｜ Call Wall 450（+7.5%，弱）（OI 0.7k） ｜ Put Wall 400（-4.4%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 59.7%｜历史 Rank 91%（近端代理）｜IV/RV 2.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 64,867 股

📆 10-30 Forward Structure
存量OI: C 1.8k / P 1.2k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $22.00 / P $9.80 ｜ ATM IV 41.6%，净 delta 敞口 -4k shares
Top ΔOI: P 397 +101
仓位参考: Max Pain 410 ｜ Call Wall 450（+7.5%，弱）（OI 0.1k） ｜ Put Wall 397.5（-5.0%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,442 股

11-06（MEDIUM △）Top ΔOI: 400P +33 ｜ 405P +31
11-06（MEDIUM △）仓位参考: Max Pain 420 ｜ Call Wall 455（+8.7%，弱）（OI 54） ｜ Put Wall 400（-4.4%，弱）（OI 65）

11-13（Activity LOW）仓位参考: Max Pain 420 ｜ Call Wall 410（-2.1%，弱）（OI 26） ｜ Put Wall 420（+0.3%，弱）（OI 68）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/ISRG_morning.json