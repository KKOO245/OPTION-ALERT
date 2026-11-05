# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $751.25 ｜ QQQ $656.81
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


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 141.52 → 今开 134.16（-5.2%） | 较昨收变动（含盘初走势） ｜ 今日高 134.80 ｜ 低 119.41

Options: P/C成交量 0.71 | OI比 0.47 | ATM IV 171.1% | Skew 19.7pp | Term 0.70 | ExpMove ±7.9%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 19.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±7.9% ｜ 11-13（8D）±20.3% ｜ 11-20（15D）±22.8% ｜ 11-27（22D）±24.7%
   ⇒ IV–VIX Spread: +150.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,856,275 | GEX Change vs 上次快照 -556,122 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 532 / LOW 62 / INVALID 208
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 115（弱结构｜现价高于该位 8.2%）
最近结构参考: Put Wall 115（现价高于该位 8.2%）
量化视角： 负 Gamma（1086万，无历史分位）｜负 Gamma 加深（56万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 115（Put Wall，弱结构）；上方 150（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 147.0C — Vol 5,498 | 最新价 $3.25 | OI 862→2196 (ΔOI +1334张) | ΔOI/Volume 24.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1334张（+154.8% vs前日OI），连续性待观察（方向未知）
11-06 165.0C — Vol 3,867 | 最新价 $0.36 | OI 2264→3267 (ΔOI +1003张) | ΔOI/Volume 25.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1003张（+44.3% vs前日OI），连续性待观察（方向未知）
11-13 160.0C — Vol 1,107 | 最新价 $6.23 | OI 559→1300 (ΔOI +741张) | ΔOI/Volume 66.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增741张（+132.6% vs前日OI），连续性待观察（方向未知）
11-06 148.0C — Vol 1,128 | 最新价 $2.96 | OI 303→918 (ΔOI +615张) | ΔOI/Volume 54.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增615张（+203.0% vs前日OI），连续性待观察（方向未知）
11-20 200.0C — Vol 1,821 | 最新价 $1.89 | OI 8388→8985 (ΔOI +597张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增597张（+7.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,290 张（Put 0 / Call 4,290），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +5.6k / P -2.5k ｜ Activity HIGH ｜ 1D
11-13  C +5.0k / P +1.3k ｜ Activity HIGH ｜ 8D
11-20  C +0.6k / P -1.0k ｜ Activity HIGH ｜ 15D
11-27  C +0.7k / P +0.3k ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 89.9k / P 42.4k，今日变化ΔOI: C +5.6k / P -2.5k，平值价格ATM: C $4.90 / P $4.94 ｜ ATM IV 171.1%，净 delta 敞口 376k shares
Top ΔOI: P 200 -1,824
仓位参考: Max Pain 150 ｜ Put Wall 130（+4.5%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 171.1%｜历史 Rank 98%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 376,107 股

📆 11-13 Forward Structure
存量OI: C 42.8k / P 30.0k，今日变化ΔOI: C +5.0k / P +1.3k，平值价格ATM: C $12.30 / P $12.90 ｜ ATM IV 167.1%，净 delta 敞口 -7k shares
Top ΔOI: C 160 +741
仓位参考: Max Pain 185 ｜ Put Wall 130（+4.5%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 167.1%｜历史 Rank 98%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,415 股

📆 11-20 Forward Structure
存量OI: C 114.9k / P 110.1k，今日变化ΔOI: C +0.6k / P -1.0k，平值价格ATM: C $13.25 / P $15.10 ｜ ATM IV 142.7%，净 delta 敞口 120k shares
Top ΔOI: C 170 -449
仓位参考: Max Pain 180 ｜ Put Wall 115（-7.6%）（OI 11.9k）
量化解读： 存量两侧均衡｜ATM IV 142.7%｜历史 Rank 98%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 119,730 股

📆 11-27 Forward Structure
存量OI: C 11.1k / P 10.3k，今日变化ΔOI: C +0.7k / P +0.3k，平值价格ATM: C $14.77 / P $15.92 ｜ ATM IV 126.9%，净 delta 敞口 -10k shares
Top ΔOI: P 175 +136
仓位参考: Max Pain 180 ｜ Put Wall 130（+4.5%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 126.9%｜历史 Rank 98%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 9,899 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/NBIS_morning.json