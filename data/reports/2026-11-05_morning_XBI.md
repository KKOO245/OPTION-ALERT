# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $751.25 ｜ QQQ $656.86
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 157C ΔOI +265（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 159.10 → 今开 157.45（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 157.61 ｜ 低 152.92

Options: P/C成交量 1.87 | OI比 1.70 | ATM IV 40.7% | Skew 8.7pp | Term 0.88 | ExpMove ±3.0%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 8.7pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.87）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.87×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.70×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±3.0% ｜ 11-13（8D）±5.0% ｜ 11-20（15D）±6.0% ｜ 11-27（22D）±8.1%
   ⇒ IV–VIX Spread: +19.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -8,939,079 | GEX Change vs 上次快照 -10,942,298 | Flip: Primary Flip: 157.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 311 / LOW 92 / INVALID 379
结构观察区: Primary Flip 157.98（全链重定价，覆盖 96%）
Put Wall 145（现价高于该位 6.7%）
最近结构参考: Flip 158（现价低于该位 2.1%）
量化视角： 负 Gamma（894万，无历史分位）｜由正转负（1094万）｜现价位于 Flip 下方 2.10%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 145（Put Wall） / 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 164.0C — Vol 1,021 | 最新价 $1.15 | OI 313→1187 (ΔOI +874张) | ΔOI/Volume 85.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增874张（+279.2% vs前日OI），连续性待观察（方向未知）
11-20 153.0P — Vol 1,003 | 最新价 $2.63 | OI 551→1375 (ΔOI +824张) | ΔOI/Volume 82.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增824张（+149.6% vs前日OI），连续性待观察（方向未知）
11-20 168.0C — Vol 495 | 最新价 $1.43 | OI 52→347 (ΔOI +295张) | ΔOI/Volume 59.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增295张（+567.3% vs前日OI），连续性待观察（方向未知）
11-06 157.0C — Vol 309 | 最新价 $3.05 | OI 131→396 (ΔOI +265张) | ΔOI/Volume 85.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增265张（+202.3% vs前日OI），连续性待观察（方向未知）
11-20 178.0C — Vol 450 | 最新价 $0.36 | OI 88→337 (ΔOI +249张) | ΔOI/Volume 55.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增249张（+282.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,507 张（Put 824 / Call 1,683），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 1D
11-13  C +0.1k / P +0.3k ｜ Activity HIGH ｜ 8D
11-20  C +0.8k / P -0.6k ｜ Activity HIGH ｜ 15D
11-27  C +0.1k / P +15 ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 5.9k / P 10.1k，今日变化ΔOI: C +0.2k / P +0.2k，平值价格ATM: C $3.52 / P $1.17 ｜ ATM IV 40.6%，净 delta 敞口 13k shares
Top ΔOI: C 157 +265 ｜ P 150 +192 ｜ P 153 -106
仓位参考: Max Pain 153 ｜ Call Wall 159（+2.8%，弱）（OI 0.4k） ｜ Put Wall 153（-1.1%）（OI 3.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 40.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,185 股

📆 11-13 Forward Structure
存量OI: C 2.7k / P 2.6k，今日变化ΔOI: C +0.1k / P +0.3k，平值价格ATM: C $5.12 / P $2.64 ｜ ATM IV 37.6%，净 delta 敞口 -3k shares
Top ΔOI: P 156 +103 ｜ P 155 +82 ｜ P 157 +53
仓位参考: Max Pain 155 ｜ Call Wall 160（+3.5%）（OI 0.6k） ｜ Put Wall 148（-4.3%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 37.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,452 股

📆 11-20 Forward Structure
存量OI: C 24.1k / P 46.1k，今日变化ΔOI: C +0.8k / P -0.6k，平值价格ATM: C $6.35 / P $2.90 ｜ ATM IV 35.3%，净 delta 敞口 8k shares
Top ΔOI: C 164 +874 ｜ P 153 +824
仓位参考: Max Pain 154 ｜ Call Wall 160（+3.5%，弱）（OI 2.4k） ｜ Put Wall 145（-6.2%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.3%｜历史 Rank 86%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,287 股

📆 11-27 Forward Structure
存量OI: C 1.1k / P 1.5k，今日变化ΔOI: C +0.1k / P +15，平值价格ATM: C $6.60 / P $5.88 ｜ ATM IV 34.1%，净 delta 敞口 6k shares
Top ΔOI: C 157 +69 ｜ C 160 +52 ｜ C 167 -33
仓位参考: Max Pain 158 ｜ Call Wall 152.5（-1.4%，弱）（OI 0.1k） ｜ Put Wall 156（+0.9%）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.1%｜历史 Rank 86%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 5,553 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/XBI_morning.json