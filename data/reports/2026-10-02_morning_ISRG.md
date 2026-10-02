# 期权晨报 2026-10-02（快照 10:20 ET）

📊 市场环境

SPY $769.72 ｜ QQQ $749.58
VIX 15.56 ↓5.1%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 401.24 → 今开 406.47（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 406.47 ｜ 低 394.69

Options: P/C成交量 0.19 | OI比 1.67 | ATM IV 63.7% | Skew -15.8pp | Term 0.68 | ExpMove ±4.0%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜Put 保护异常便宜（Skew -15.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.67×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±4.0% ｜ 10-16（14D）±5.3% ｜ 10-23（21D）±9.4% ｜ 10-30（28D）±10.8%
   ⇒ IV–VIX Spread: +48.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 511,640 | GEX Change vs 上次快照 -1,670,987 | Flip: Primary Flip: 390.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 282 / LOW 169 / INVALID 411
结构观察区: Primary Flip 390.88（全链重定价，覆盖 90%）
Call Wall 400（弱结构｜现价低于该位 1.2%）
最近结构参考: Flip 391（现价高于该位 1.1%）
量化视角： 正 Gamma（51万，无历史分位）｜正 Gamma 减弱（167万）｜现价位于 Flip 上方 1.07%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 391（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 440.0C — Vol 34 | 最新价 $2.09 | OI 7→41 (ΔOI +34张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增34张（+485.7% vs前日OI），连续性待观察（方向未知）
10-09 442.5C — Vol 34 | 最新价 $1.34 | OI 0→34 (ΔOI +34张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增34张（前日OI缺失），值得跟踪（方向未知）
10-02 390.0P — Vol 55 | 最新价 $0.40 | OI 52→85 (ΔOI +33张) | ΔOI/Volume 60.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33张（+63.5% vs前日OI），连续性待观察（方向未知）
10-09 367.5P — Vol 32 | 最新价 $2.03 | OI 0→32 (ΔOI +32张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增32张（前日OI缺失），值得跟踪（方向未知）
10-23 400.0C — Vol 34 | 最新价 $19.96 | OI 51→83 (ΔOI +32张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32张（+62.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 165 张（Put 65 / Call 100），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 2.1k / P 3.6k，今日成交量: C 63 / P 67，平值价格ATM: C $4.30 / P $1.35 ｜ ATM IV 63.7%，预期波动 ±1.4%，Max Pain 395
Top ΔOI: C 405 -62 ｜ C 410 -36 ｜ P 390 +33

📆 Forward Expiration Structure

10-09  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 7D
10-16  C -14 / P +29 ｜ Activity LOW ｜ 14D
10-23  C +58 / P +14 ｜ Activity LOW ｜ 21D
10-30  C +7 / P +18 ｜ Activity LOW ｜ 28D

📆 10-09 Forward Structure
存量OI: C 1.3k / P 0.5k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $11.55 / P $4.30 ｜ ATM IV 32.2%，净 delta 敞口 -2k shares
Top ΔOI: P 367 +32
仓位参考: Max Pain 380 ｜ Call Wall 420（+6.3%，弱）（OI 0.1k） ｜ Put Wall 375（-5.1%，弱）（OI 34）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,615 股

10-16（Activity LOW）仓位参考: Max Pain 390 ｜ Call Wall 400（+1.2%，弱）（OI 0.9k） ｜ Put Wall 360（-8.9%，弱）（OI 1.4k）

10-23（Activity LOW）仓位参考: Max Pain 415 ｜ Call Wall 425（+7.6%）（OI 0.5k） ｜ Put Wall 415（+5.0%）（OI 0.4k）

10-30（Activity LOW）仓位参考: Max Pain 380 ｜ Call Wall 375（-5.1%，弱）（OI 59） ｜ Put Wall 375（-5.1%，弱）（OI 49）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/ISRG_morning.json