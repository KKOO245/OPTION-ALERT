# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 86P ΔOI -1,517（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 89.07 → 今开 89.72（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 89.75 ｜ 低 88.43

Options: P/C成交量 1.24 | OI比 0.49 | ATM IV 46.8% | Skew -1.1pp | Term 0.89 | ExpMove ±3.4%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.49）+ 当日成交偏 Put（P/C量 1.24）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±3.4% ｜ 10-09（9D）±5.1% ｜ 10-16（16D）±6.8% ｜ 10-23（23D）±8.0%
   ⇒ IV–VIX Spread: +31.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -17,832,583 | GEX Change vs 上次快照 -1,988,733 | Flip: Primary Flip: 89.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 461 / LOW 104 / INVALID 247
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 89.60（全链重定价，覆盖 95%）
Put Wall 90（弱结构｜现价低于该位 1.6%） | Call Wall 94（弱结构｜现价低于该位 5.8%）
最近结构参考: Flip 90（现价低于该位 1.2%）
量化视角： 负 Gamma（1783万，无历史分位）｜负 Gamma 加深（199万）｜现价位于 Flip 下方 1.17%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 93（MaxPain，仅结算参考） / 94（Call Wall，弱结构）。
• Gamma 区域：切换参考 90（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 86.0P — Vol 3,084 | 最新价 $1.78 | OI 2140→5118 (ΔOI +2978张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2978张（+139.2% vs前日OI），连续性待观察（方向未知）
10-02 83.5P — Vol 1,597 | 最新价 $0.14 | OI 1583→3110 (ΔOI +1527张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1527张（+96.5% vs前日OI），连续性待观察（方向未知）
10-02 90.5C — Vol 1,638 | 最新价 $0.93 | OI 2865→4361 (ΔOI +1496张) | ΔOI/Volume 91.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1496张（+52.2% vs前日OI），连续性待观察（方向未知）
10-02 78.0P — Vol 647 | 最新价 $0.01 | OI 121→750 (ΔOI +629张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增629张（+519.8% vs前日OI），连续性待观察（方向未知）
10-02 88.0P — Vol 2,487 | 最新价 $1.03 | OI 2277→2838 (ΔOI +561张) | ΔOI/Volume 22.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增561张（+24.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,191 张（Put 5,695 / Call 1,496），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.3k / P +1.8k ｜ Activity HIGH ｜ 2D
10-09  C +0.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 9D
10-16  C -33 / P +3.4k ｜ Activity HIGH ｜ 16D
10-23  C +73 / P +83 ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 130.1k / P 63.5k，今日变化ΔOI: C +0.3k / P +1.8k，平值价格ATM: C $1.86 / P $1.13 ｜ ATM IV 46.9%，净 delta 敞口 72k shares
Top ΔOI: C 95 -1,720 ｜ P 83 +1,527 ｜ P 86 -1,517
仓位参考: Max Pain 93 ｜ Call Wall 94（+6.2%，弱）（OI 35.6k） ｜ Put Wall 90（+1.6%，弱）（OI 9.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.9%｜历史 Rank 76%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 71,850 股

10-09（MEDIUM △）Top ΔOI: 88P +221 ｜ 90C +191
10-09（MEDIUM △）仓位参考: Max Pain 94 ｜ Call Wall 94（+6.2%，弱）（OI 0.8k） ｜ Put Wall 90（+1.6%，弱）（OI 1.9k）

📆 10-16 Forward Structure
存量OI: C 93.9k / P 106.1k，今日变化ΔOI: C -33 / P +3.4k，平值价格ATM: C $3.25 / P $2.81 ｜ ATM IV 40.9%，净 delta 敞口 -103k shares
Top ΔOI: P 86 +2,978 ｜ P 89 +277 ｜ P 87 +224
仓位参考: Max Pain 92 ｜ Call Wall 90（+1.6%，弱）（OI 5.2k） ｜ Put Wall 90（+1.6%，弱）（OI 10.9k）
量化解读： 存量两侧均衡｜ATM IV 40.9%｜历史 Rank 76%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 103,409 股

10-23（MEDIUM △）Top ΔOI: 85P +66 ｜ 80P -34
10-23（MEDIUM △）仓位参考: Max Pain 95 ｜ Call Wall 91（+2.8%，弱）（OI 0.2k） ｜ Put Wall 85（-4.0%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/GDX_morning.json