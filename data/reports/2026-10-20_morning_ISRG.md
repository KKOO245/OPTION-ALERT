# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.58 ｜ QQQ $717.63
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-23（3D）ATM IV 107.3% vs 10-30 66.2%（差 +41.0pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-23 435C ΔOI +539（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 475C ΔOI +1,028 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 433.18 → 今开 433.50（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 437.00 ｜ 低 432.00

Options: P/C成交量 0.58 | OI比 0.89 | ATM IV 107.3% | Skew -0.5pp | Term 0.44 | ExpMove ±8.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.44，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±8.2% ｜ 10-30（10D）±8.4% ｜ 11-06（17D）±4.7% ｜ 11-13（24D）±10.2%
   ⇒ IV–VIX Spread: +89.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,883,367 | GEX Change vs 上次快照 283,898 | Flip: Primary Flip: 402.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 408 / LOW 75 / INVALID 483
结构观察区: Primary Flip 402.66（全链重定价，覆盖 100%）
Call Wall 475（弱结构｜现价低于该位 8.4%）
最近结构参考: Flip 403（现价高于该位 8.0%）
量化视角： 正 Gamma（188万，无历史分位）｜正 Gamma 增强（+28万）｜现价位于 Flip 上方 8.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 420（MaxPain，仅结算参考）；上方 475（Call Wall，弱结构）。
• Gamma 区域：切换参考 403（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 475.0C — Vol 1,079 | 最新价 $4.40 | OI 49→1077 (ΔOI +1028张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1028张（+2098.0% vs前日OI），连续性待观察（方向未知）
10-23 435.0C — Vol 637 | 最新价 $16.05 | OI 51→590 (ΔOI +539张) | ΔOI/Volume 84.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增539张（+1056.9% vs前日OI），连续性待观察（方向未知）
11-20 435.0C — Vol 517 | 最新价 $22.94 | OI 131→575 (ΔOI +444张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增444张（+338.9% vs前日OI），连续性待观察（方向未知）
10-23 365.0P — Vol 452 | 最新价 $0.90 | OI 51→458 (ΔOI +407张) | ΔOI/Volume 90.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增407张（+798.0% vs前日OI），连续性待观察（方向未知）
10-23 405.0P — Vol 424 | 最新价 $6.29 | OI 27→430 (ΔOI +403张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增403张（+1492.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,821 张（Put 810 / Call 2,011），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +2.4k / P +2.7k ｜ Activity HIGH ｜ 3D
10-30  C +78 / P +80 ｜ Activity MEDIUM △ ｜ 10D
11-06  C +57 / P +36 ｜ Activity MEDIUM △ ｜ 17D
11-13  C +40 / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 5.4k / P 4.8k，今日变化ΔOI: C +2.4k / P +2.7k，平值价格ATM: C $17.00 / P $18.45 ｜ ATM IV 107.3%，净 delta 敞口 20k shares
Top ΔOI: C 475 +1,028 ｜ C 435 +539
仓位参考: Max Pain 420 ｜ Call Wall 475（+9.2%）（OI 1.1k） ｜ Put Wall 415（-4.6%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 107.3%｜历史 Rank 100%（近端代理）｜IV/RV 4.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 20,484 股

10-30（MEDIUM △）Top ΔOI: 440C +17 ｜ 450C +13
10-30（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 460（+5.7%，弱）（OI 0.1k） ｜ Put Wall 410（-5.7%，弱）（OI 66）

11-06（MEDIUM △）Top ΔOI: 407P +20
11-06（MEDIUM △）仓位参考: Max Pain 420 ｜ Call Wall 455（+4.6%，弱）（OI 54） ｜ Put Wall 450（+3.4%，弱）（OI 64）

11-13（MEDIUM △）Top ΔOI: 420P +68 ｜ 475C +15
11-13（MEDIUM △）仓位参考: Max Pain 420 ｜ Call Wall 475（+9.2%，弱）（OI 47） ｜ Put Wall 420（-3.5%，弱）（OI 68）

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 107.3% vs 10-30 66.2%（差 +41.0pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/ISRG_morning.json