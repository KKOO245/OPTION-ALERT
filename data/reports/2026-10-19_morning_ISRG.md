# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🔴 **事件差分**: 10-23（4D）ATM IV 92.1% vs 10-30 63.0%（差 +29.1pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-06 450P ΔOI +63（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 426.70 → 今开 427.34（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 432.75 ｜ 低 426.70

Options: P/C成交量 2.29 | OI比 0.71 | ATM IV 92.1% | Skew 1.5pp | Term 0.49 | ExpMove ±8.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.49，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.71）+ 当日成交偏 Put（P/C量 2.29）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.29×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±8.0% ｜ 10-30（11D）±8.6% ｜ 11-06（18D）±9.6% ｜ 11-13（25D）±10.4%
   ⇒ IV–VIX Spread: +73.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,412,195 | GEX Change vs 上次快照 142,163 | Flip: Primary Flip: 392.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 357 / LOW 79 / INVALID 470
结构观察区: Primary Flip 392.56（全链重定价，覆盖 100%）
Call Wall 420（弱结构｜现价高于该位 2.2%）
最近结构参考: Call Wall 420（现价高于该位 2.2%）
量化视角： 正 Gamma（141万，无历史分位）｜正 Gamma 增强（+14万）｜现价位于 Flip 上方 9.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 415（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 393（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 480.0C — Vol 145 | 最新价 $7.10 | OI 131→269 (ΔOI +138张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增138张（+105.3% vs前日OI），连续性待观察（方向未知）
11-20 475.0C — Vol 91 | 最新价 $7.70 | OI 67→150 (ΔOI +83张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增83张（+123.9% vs前日OI），连续性待观察（方向未知）
10-23 430.0P — Vol 68 | 最新价 $18.10 | OI 1→67 (ΔOI +66张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增66张（+6600.0% vs前日OI），连续性待观察（方向未知）
11-06 450.0P — Vol 68 | 最新价 $32.30 | OI 1→64 (ΔOI +63张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增63张（+6300.0% vs前日OI），连续性待观察（方向未知）
11-20 435.0C — Vol 62 | 最新价 $20.18 | OI 76→131 (ΔOI +55张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55张（+72.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 405 张（Put 129 / Call 276），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 4D
10-30  C +0.1k / P +60 ｜ Activity MEDIUM △ ｜ 11D
11-06  C +16 / P +79 ｜ Activity MEDIUM △ ｜ 18D
11-13  C +31 / P -29 ｜ Activity LOW ｜ 25D

📆 10-23 Forward Structure
存量OI: C 3.0k / P 2.2k，今日变化ΔOI: C +0.3k / P +0.1k，平值价格ATM: C $17.00 / P $17.50 ｜ ATM IV 92.1%，净 delta 敞口 8k shares
Top ΔOI: P 430 +66 ｜ C 432 +55 ｜ C 430 +38
仓位参考: Max Pain 415 ｜ Call Wall 425（-1.0%，弱）（OI 0.5k） ｜ Put Wall 415（-3.3%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 92.1%｜历史 Rank 100%（近端代理）｜IV/RV 3.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,683 股

10-30（MEDIUM △）Top ΔOI: 460C +31 ｜ 407P +24
10-30（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 460（+7.2%，弱）（OI 0.1k） ｜ Put Wall 410（-4.5%，弱）（OI 61）

11-06（MEDIUM △）Top ΔOI: 450P +63
11-06（MEDIUM △）仓位参考: Max Pain 420 ｜ Call Wall 455（+6.0%，弱）（OI 54） ｜ Put Wall 450（+4.8%，弱）（OI 64）

11-13（Activity LOW）仓位参考: Max Pain 410 ｜ Call Wall 410（-4.5%，弱）（OI 26）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 92.1% vs 10-30 63.0%（差 +29.1pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/ISRG_morning.json