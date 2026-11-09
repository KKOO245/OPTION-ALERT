# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.91 ｜ QQQ $679.35
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-11 380C ΔOI +652（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 120P ΔOI +53,822 占该期限总 OI 17.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 358.22 → 今开 360.25（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 378.89 ｜ 低 360.02

Options: P/C成交量 0.45 | OI比 0.78 | ATM IV 70.6% | Skew 5.1pp | Term 0.52 | ExpMove ±3.8%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-11（2D）±3.8% ｜ 11-13（4D）±5.1% ｜ 11-16（7D）±5.5% ｜ 11-18（9D）±6.8%
   ⇒ IV–VIX Spread: +49.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 69,560,359 | GEX Change vs 上次快照 62,949,198 | Flip: Primary Flip: 355.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1438 / LOW 241 / INVALID 963
结构观察区: Primary Flip 355.86（全链重定价，覆盖 98%）
Call Wall 400（弱结构｜现价低于该位 5.9%）
最近结构参考: Flip 356（现价高于该位 5.8%）
量化视角： 正 Gamma（6956万，无历史分位）｜正 Gamma 增强（+6295万）｜现价位于 Flip 上方 5.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 362（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 356（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 120.0P — Vol 54,132 | 最新价 $0.01 | OI 349→54171 (ΔOI +53822张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增53822张（+15421.8% vs前日OI），连续性待观察（方向未知）
11-13 200.0P — Vol 19,620 | 最新价 $0.07 | OI 2365→19277 (ΔOI +16912张) | ΔOI/Volume 86.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16912张（+715.1% vs前日OI），连续性待观察（方向未知）
11-13 180.0P — Vol 22,314 | 最新价 $0.05 | OI 238→15132 (ΔOI +14894张) | ΔOI/Volume 66.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14894张（+6258.0% vs前日OI），连续性待观察（方向未知）
11-13 220.0P — Vol 14,859 | 最新价 $0.11 | OI 1417→15636 (ΔOI +14219张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14219张（+1003.5% vs前日OI），连续性待观察（方向未知）
11-13 380.0C — Vol 9,234 | 最新价 $3.40 | OI 2522→7571 (ΔOI +5049张) | ΔOI/Volume 54.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5049张（+200.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 104,896 张（Put 99,847 / Call 5,049），跨 1 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 67.0k / P 52.1k，今日成交量: C 220.8k / P 98.6k，平值价格ATM: C $2.25 / P $3.60 ｜ ATM IV 70.6%，预期波动 ±1.6%，Max Pain 362
Top ΔOI: C 415 +2,502 ｜ C 420 +2,218 ｜ P 250 +1,727

📆 Forward Expiration Structure

11-11  C +3.7k / P +7.1k ｜ Activity HIGH ｜ 2D
11-13  C +35.4k / P +128.1k ｜ Activity HIGH ｜ 4D
11-16  C +2.7k / P +1.2k ｜ Activity HIGH ｜ 7D
11-18  C +0.6k / P +0.7k ｜ Activity HIGH ｜ 9D

📆 11-11 Forward Structure
存量OI: C 30.3k / P 25.8k，今日变化ΔOI: C +3.7k / P +7.1k，平值价格ATM: C $6.50 / P $7.73 ｜ ATM IV 60.0%，净 delta 敞口 167k shares
Top ΔOI: C 380 +652
仓位参考: Max Pain 365 ｜ Call Wall 390（+3.6%，弱）（OI 1.9k） ｜ Put Wall 340（-9.7%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 60.0%｜历史 Rank 83%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 166,556 股

📆 11-13 Forward Structure
存量OI: C 124.1k / P 187.8k，今日变化ΔOI: C +35.4k / P +128.1k，平值价格ATM: C $9.05 / P $10.10 ｜ ATM IV 57.9%，净 delta 敞口 1.6M shares
Top ΔOI: P 120 +53,822
仓位参考: Max Pain 360 ｜ Call Wall 362.5（-3.7%，弱）（OI 7.9k）
量化解读： 存量 Put 重｜ATM IV 57.9%｜历史 Rank 83%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,600,490 股

📆 11-16 Forward Structure
存量OI: C 11.9k / P 6.1k，今日变化ΔOI: C +2.7k / P +1.2k，平值价格ATM: C $10.00 / P $10.55 ｜ ATM IV 49.7%，净 delta 敞口 53k shares
Top ΔOI: C 400 +364
仓位参考: Max Pain 368 ｜ Call Wall 400（+6.2%，弱）（OI 0.8k） ｜ Put Wall 380（+0.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 49.7%｜历史 Rank 83%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 正 53,145 股

📆 11-18 Forward Structure
存量OI: C 4.7k / P 3.5k，今日变化ΔOI: C +0.6k / P +0.7k，平值价格ATM: C $12.80 / P $12.75 ｜ ATM IV 51.3%，净 delta 敞口 24k shares
Top ΔOI: C 387 -150 ｜ C 370 +121
仓位参考: Max Pain 355 ｜ Call Wall 380（+0.9%，弱）（OI 0.3k） ｜ Put Wall 350（-7.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.3%｜历史 Rank 83%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 23,534 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/TSLA_morning.json