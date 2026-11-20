# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 170.98 → 今开 181.00（+5.9%） | 较昨收变动（含盘初走势） ｜ 今日高 186.99 ｜ 低 178.41

Options: P/C成交量 0.56 | OI比 0.75 | ATM IV 132.3% | Skew 9.6pp | Term 0.71 | ExpMove ±6.3%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±6.3% ｜ 11-27（8D）±11.6% ｜ 12-04（15D）±15.8% ｜ 12-11（22D）±17.6%
   ⇒ IV–VIX Spread: +109.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,496,955 | GEX Change vs 上次快照 7,692,176 | Flip: Primary Flip: 191.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 486 / LOW 120 / INVALID 196
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 191.39（全链重定价，覆盖 99%）
Put Wall 200（弱结构｜现价低于该位 7.1%） | Call Wall 200（弱结构｜现价低于该位 7.1%）
最近结构参考: Flip 191（现价低于该位 3.0%）
量化视角： 负 Gamma（350万，无历史分位）｜负 Gamma 缓解（+769万）｜现价位于 Flip 下方 2.97%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 190（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 191（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 200.0C — Vol 4,580 | 最新价 $0.40 | OI 5217→6295 (ΔOI +1078张) | ΔOI/Volume 23.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1078张（+20.7% vs前日OI），连续性待观察（方向未知）
12-18 170.0P — Vol 1,430 | 最新价 $18.50 | OI 3314→4105 (ΔOI +791张) | ΔOI/Volume 55.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增791张（+23.9% vs前日OI），连续性待观察（方向未知）
11-20 180.0C — Vol 3,829 | 最新价 $3.20 | OI 2889→3472 (ΔOI +583张) | ΔOI/Volume 15.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增583张（+20.2% vs前日OI），连续性待观察（方向未知）
12-18 150.0P — Vol 861 | 最新价 $10.05 | OI 5806→6381 (ΔOI +575张) | ΔOI/Volume 66.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增575张（+9.9% vs前日OI），连续性待观察（方向未知）
11-20 205.0C — Vol 858 | 最新价 $0.22 | OI 1937→2439 (ΔOI +502张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增502张（+25.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,529 张（Put 1,366 / Call 2,163），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +4.1k / P -7.7k ｜ Activity HIGH ｜ 1D
11-27  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 8D
12-04  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 15D
12-11  C +33 / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 109.5k / P 82.1k，今日变化ΔOI: C +4.1k / P -7.7k，平值价格ATM: C $6.80 / P $5.00 ｜ ATM IV 132.3%，净 delta 敞口 939k shares
Top ΔOI: P 240 -2,141 ｜ P 230 -1,721 ｜ C 200 +1,078
仓位参考: Max Pain 190 ｜ Call Wall 200（+7.7%，弱）（OI 6.3k） ｜ Put Wall 200（+7.7%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 132.3%｜历史 Rank 84%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 939,340 股

📆 11-27 Forward Structure
存量OI: C 17.5k / P 13.5k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $11.62 / P $10.00 ｜ ATM IV 95.9%，净 delta 敞口 82k shares
Top ΔOI: C 200 +314 ｜ C 172 +267 ｜ C 205 +174
仓位参考: Max Pain 195 ｜ Call Wall 200（+7.7%）（OI 1.8k） ｜ Put Wall 190（+2.3%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 95.9%｜历史 Rank 84%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 81,736 股

📆 12-04 Forward Structure
存量OI: C 9.2k / P 8.2k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $14.90 / P $14.50 ｜ ATM IV 94.8%，净 delta 敞口 11k shares
Top ΔOI: C 220 +130
仓位参考: Max Pain 200 ｜ Call Wall 200（+7.7%，弱）（OI 0.8k） ｜ Put Wall 200（+7.7%）（OI 1.9k）
量化解读： 存量两侧均衡｜ATM IV 94.8%｜历史 Rank 84%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,267 股

12-11（MEDIUM △）Top ΔOI: 200C +53
12-11（MEDIUM △）仓位参考: Max Pain 205 ｜ Call Wall 200（+7.7%，弱）（OI 0.2k） ｜ Put Wall 175（-5.8%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/BE_morning.json