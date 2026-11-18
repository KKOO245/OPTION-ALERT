# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $737.42 ｜ QQQ $nan
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **近现价集中开仓**: 11-18 80P ΔOI +1,460（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 80P ΔOI +1,460 占该期限总 OI 21.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 78.95 → 今开 79.22（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 81.27 ｜ 低 79.05

Options: P/C成交量 2.94 | OI比 1.29 | ATM IV 54.5% | Skew -1.8pp | Term 0.83 | ExpMove ±2.6%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.94）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.94×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-18（1D）±2.6% ｜ 11-20（3D）±5.0% ｜ 11-23（6D）±4.9% ｜ 11-25（8D）±3.3%
   ⇒ IV–VIX Spread: +31.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -29,691,573 | GEX Change vs 上次快照 25,858,406 | Flip: Primary Flip: 82.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 545 / LOW 194 / INVALID 541
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 82.05（全链重定价，覆盖 96%）
最近结构参考: Flip 82（现价低于该位 1.8%）
量化视角： 负 Gamma（2969万，无历史分位）｜负 Gamma 缓解（+2586万）｜现价位于 Flip 下方 1.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 82（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 85.0C — Vol 15,166 | 最新价 $2.07 | OI 16283→26053 (ΔOI +9770张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9770张（+60.0% vs前日OI），连续性待观察（方向未知）
12-18 84.0C — Vol 8,371 | 最新价 $2.37 | OI 741→8023 (ΔOI +7282张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7282张（+982.7% vs前日OI），连续性待观察（方向未知）
11-18 80.0P — Vol 1,810 | 最新价 $1.72 | OI 217→1677 (ΔOI +1460张) | ΔOI/Volume 80.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1460张（+672.8% vs前日OI），连续性待观察（方向未知）
12-18 71.0P — Vol 1,059 | 最新价 $1.29 | OI 1243→2119 (ΔOI +876张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增876张（+70.5% vs前日OI），连续性待观察（方向未知）
12-18 80.0P — Vol 2,033 | 最新价 $4.65 | OI 15318→16137 (ΔOI +819张) | ΔOI/Volume 40.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增819张（+5.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,207 张（Put 3,155 / Call 17,052），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-18  C +1.3k / P +2.4k ｜ Activity HIGH ｜ 1D
11-20  C +2.3k / P -2.1k ｜ Activity MEDIUM △ ｜ 3D
11-23  C +0.1k / P +0.3k ｜ Activity HIGH ｜ 6D
11-25  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 8D

📆 11-18 Forward Structure
存量OI: C 2.9k / P 3.8k，今日变化ΔOI: C +1.3k / P +2.4k，平值价格ATM: C $0.84 / P $1.28 ｜ ATM IV 54.5%，净 delta 敞口 -19k shares
Top ΔOI: P 80 +1,460 ｜ P 79 +632 ｜ C 80 +335
仓位参考: Max Pain 80 ｜ Call Wall 80（-0.7%，弱）（OI 0.3k） ｜ Put Wall 80（-0.7%）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 54.5%｜历史 Rank 87%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,912 股

11-20（MEDIUM △）Top ΔOI: 80P -1,468 ｜ 90P -603
11-20（MEDIUM △）仓位参考: Max Pain 84 ｜ Call Wall 84（+4.3%，弱）（OI 22.2k） ｜ Put Wall 80（-0.7%，弱）（OI 22.7k）

📆 11-23 Forward Structure
存量OI: C 0.5k / P 0.5k，今日变化ΔOI: C +0.1k / P +0.3k，平值价格ATM: C $1.18 / P $2.78 ｜ ATM IV 43.1%，净 delta 敞口 -8k shares
Top ΔOI: P 78 +74 ｜ P 82 +65 ｜ P 79 +58
仓位参考: Max Pain 84 ｜ Call Wall 85（+5.5%，弱）（OI 44） ｜ Put Wall 78（-3.2%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 43.1%｜历史 Rank 87%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 8,255 股

11-25（MEDIUM △）Top ΔOI: 78P +68 ｜ 85C +66
11-25（MEDIUM △）仓位参考: Max Pain 83 ｜ Call Wall 83（+3.0%）（OI 0.2k） ｜ Put Wall 80（-0.7%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/GDX_morning.json