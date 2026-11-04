# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.96 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-06 150C ΔOI +1,025（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 151.64 → 今开 145.63（-4.0%） | 较昨收变动（含盘初走势） ｜ 今日高 152.88 ｜ 低 144.54

Options: P/C成交量 0.22 | OI比 0.53 | ATM IV 137.2% | Skew 5.6pp | Term 0.79 | ExpMove ±8.8%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 5.6pp）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.22×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±8.8% ｜ 11-13（9D）±17.2% ｜ 11-20（16D）±21.2% ｜ 11-27（23D）±24.2%
   ⇒ IV–VIX Spread: +120.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,441,993 | GEX Change vs 上次快照 -1,921,396 | Flip: Primary Flip: 153.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 568 / LOW 58 / INVALID 110
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 153.60（全链重定价，覆盖 100%）
最近结构参考: Flip 154（现价低于该位 4.9%）
量化视角： 负 Gamma（544万，无历史分位）｜负 Gamma 加深（192万）｜现价位于 Flip 下方 4.92%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 154（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 230.0C — Vol 3,585 | 最新价 $0.66 | OI 2556→5841 (ΔOI +3285张) | ΔOI/Volume 91.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3285张（+128.5% vs前日OI），连续性待观察（方向未知）
11-06 245.0C — Vol 1,610 | 最新价 $0.01 | OI 437→1970 (ΔOI +1533张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1533张（+350.8% vs前日OI），连续性待观察（方向未知）
11-13 220.0C — Vol 1,670 | 最新价 $1.02 | OI 1345→2860 (ΔOI +1515张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1515张（+112.6% vs前日OI），连续性待观察（方向未知）
11-06 130.0P — Vol 2,005 | 最新价 $1.27 | OI 1484→2894 (ΔOI +1410张) | ΔOI/Volume 70.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1410张（+95.0% vs前日OI），连续性待观察（方向未知）
11-06 150.0C — Vol 7,390 | 最新价 $8.80 | OI 3014→4039 (ΔOI +1025张) | ΔOI/Volume 13.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1025张（+34.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,768 张（Put 1,410 / Call 7,358），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +8.3k / P +2.5k ｜ Activity HIGH ｜ 2D
11-13  C +10.2k / P +1.0k ｜ Activity HIGH ｜ 9D
11-20  C +1.8k / P +0.6k ｜ Activity MEDIUM △ ｜ 16D
11-27  C +0.3k / P +11 ｜ Activity LOW ｜ 23D

📆 11-06 Forward Structure
存量OI: C 84.3k / P 44.9k，今日变化ΔOI: C +8.3k / P +2.5k，平值价格ATM: C $6.70 / P $6.19 ｜ ATM IV 137.2%，净 delta 敞口 178k shares
Top ΔOI: P 130 +1,410 ｜ C 150 +1,025
仓位参考: Max Pain 160 ｜ Call Wall 150（+2.7%，弱）（OI 4.0k） ｜ Put Wall 145（-0.7%）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 137.2%｜历史 Rank 86%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 178,367 股

📆 11-13 Forward Structure
存量OI: C 37.8k / P 28.6k，今日变化ΔOI: C +10.2k / P +1.0k，平值价格ATM: C $13.50 / P $11.60 ｜ ATM IV 140.6%，净 delta 敞口 54k shares
Top ΔOI: C 230 +3,285 ｜ C 220 +1,515
仓位参考: Max Pain 190 ｜ Put Wall 150（+2.7%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 140.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,995 股

11-20（MEDIUM △）Top ΔOI: 200C +970 ｜ 130P +373
11-20（MEDIUM △）仓位参考: Max Pain 180 ｜ Put Wall 150（+2.7%，弱）（OI 7.4k）

11-27（Activity LOW）仓位参考: Max Pain 180 ｜ Call Wall 150（+2.7%，弱）（OI 0.6k） ｜ Put Wall 155（+6.1%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/NBIS_morning.json