# 期权晨报 2026-10-22（快照 10:20 ET）

📊 市场环境

SPY $766.63 ｜ QQQ $711.11
VIX 17.91 ↑7.4%（5D +8.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 150P ΔOI +2,200（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 152.78 → 今开 152.25（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 154.44 ｜ 低 151.46

Options: P/C成交量 2.06 | OI比 1.32 | ATM IV 51.4% | Skew 9.9pp | Term 0.66 | ExpMove ±1.3%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 9.9pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.06）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.06×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（1D）±1.3% ｜ 10-30（8D）±4.3% ｜ 11-06（15D）±5.9% ｜ 11-13（22D）±8.9%
   ⇒ IV–VIX Spread: +33.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,513,090 | GEX Change vs 上次快照 -707,540 | Flip: Primary Flip: 160.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 349 / LOW 93 / INVALID 334
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 160.00（全链重定价，覆盖 87%）
最近结构参考: Flip 160（现价低于该位 3.9%）
量化视角： 负 Gamma（1451万，无历史分位）｜负 Gamma 加深（71万）｜现价位于 Flip 下方 3.90%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 165.0C — Vol 5,765 | 最新价 $1.75 | OI 649→5386 (ΔOI +4737张) | ΔOI/Volume 82.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4737张（+729.9% vs前日OI），连续性待观察（方向未知）
10-30 142.0P — Vol 3,485 | 最新价 $0.37 | OI 593→3874 (ΔOI +3281张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3281张（+553.3% vs前日OI），连续性待观察（方向未知）
10-30 150.0P — Vol 4,740 | 最新价 $1.86 | OI 7279→9479 (ΔOI +2200张) | ΔOI/Volume 46.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2200张（+30.2% vs前日OI），连续性待观察（方向未知）
10-23 150.0P — Vol 823 | 最新价 $0.50 | OI 269→628 (ΔOI +359张) | ΔOI/Volume 43.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增359张（+133.5% vs前日OI），连续性待观察（方向未知）
10-30 152.0P — Vol 501 | 最新价 $2.51 | OI 1271→1527 (ΔOI +256张) | ΔOI/Volume 51.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增256张（+20.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,833 张（Put 6,096 / Call 4,737），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.2k / P -0.5k ｜ Activity LOW ｜ 1D
10-30  C +0.4k / P +2.5k ｜ Activity MEDIUM △ ｜ 8D
11-06  C -72 / P -0.4k ｜ Activity MEDIUM △ ｜ 15D
11-13  C +0.1k / P -0.1k ｜ Activity MEDIUM △ ｜ 22D

📆 10-23 Forward Structure
存量OI: C 17.5k / P 23.2k，今日变化ΔOI: C +0.2k / P -0.5k，平值价格ATM: C $0.40 / P $1.60 ｜ ATM IV 51.4%，净 delta 敞口 12k shares
Top ΔOI: P 150 +359 ｜ P 152 -330 ｜ P 148 -243
仓位参考: Max Pain 148 ｜ Call Wall 148（-3.7%，弱）（OI 3.0k） ｜ Put Wall 144（-6.3%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.4%｜历史 Rank 97%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,757 股

10-30（MEDIUM △）Top ΔOI: 142P +3,281 ｜ 140P -3,259
10-30（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+0.8%）（OI 1.7k） ｜ Put Wall 150（-2.4%，弱）（OI 9.5k）

11-06（MEDIUM △）Top ΔOI: 145P -253 ｜ 155C -192
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 154（+0.2%，弱）（OI 0.1k） ｜ Put Wall 151（-1.8%）（OI 0.6k）

11-13（MEDIUM △）Top ΔOI: 150C +133 ｜ 151P -31
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 150（-2.4%）（OI 0.1k） ｜ Put Wall 153（-0.5%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/XBI_morning.json