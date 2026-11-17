# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🔵 **期限 OI 集中**: 11-23 460C ΔOI +9,933 占该期限总 OI 41.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 390.22 → 今开 387.11（-0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 389.80 ｜ 低 376.18

Options: P/C成交量 1.16 | OI比 0.71 | ATM IV 71.2% | Skew 5.6pp | Term 0.67 | ExpMove ±3.7%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价中性（Skew 5.6pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.71）+ 当日成交偏 Put（P/C量 1.16）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.16×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（2D）±3.7% ｜ 11-20（4D）±5.1% ｜ 11-23（7D）±6.2% ｜ 11-25（9D）±6.6%
   ⇒ IV–VIX Spread: +49.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,313,348 | GEX Change vs 上次快照 -14,706,750 | Flip: Primary Flip: 371.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1435 / LOW 254 / INVALID 901
结构观察区: Primary Flip 371.28（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 5.5%）
最近结构参考: Flip 371（现价高于该位 1.8%）
量化视角： 正 Gamma（2931万，无历史分位）｜正 Gamma 减弱（1471万）｜现价位于 Flip 上方 1.82%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 385（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 371（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 140.0P — Vol 55,021 | 最新价 $0.01 | OI 13695→67852 (ΔOI +54157张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54157张（+395.4% vs前日OI），连续性待观察（方向未知）
11-20 220.0P — Vol 24,495 | 最新价 $0.05 | OI 2060→23654 (ΔOI +21594张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21594张（+1048.2% vs前日OI），连续性待观察（方向未知）
11-20 230.0P — Vol 22,521 | 最新价 $0.07 | OI 4447→20768 (ΔOI +16321张) | ΔOI/Volume 72.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16321张（+367.0% vs前日OI），连续性待观察（方向未知）
11-20 195.0P — Vol 16,705 | 最新价 $0.04 | OI 1762→14743 (ΔOI +12981张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12981张（+736.7% vs前日OI），连续性待观察（方向未知）
11-20 397.5C — Vol 11,466 | 最新价 $7.00 | OI 358→10885 (ΔOI +10527张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10527张（+2940.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 115,580 张（Put 105,053 / Call 10,527），跨 1 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 77.5k / P 55.4k，今日成交量: C 162.3k / P 188.5k，平值价格ATM: C $3.05 / P $2.78 ｜ ATM IV 71.2%，预期波动 ±1.5%，Max Pain 385
Top ΔOI: P 300 +4,708 ｜ P 250 +3,252 ｜ C 410 +3,178

📆 Forward Expiration Structure

11-18  C +4.8k / P +6.6k ｜ Activity HIGH ｜ 2D
11-20  C +47.3k / P +131.6k ｜ Activity HIGH ｜ 4D
11-23  C +15.3k / P +0.9k ｜ Activity HIGH ｜ 7D
11-25  C +0.3k / P +1.1k ｜ Activity HIGH ｜ 9D

📆 11-18 Forward Structure
存量OI: C 19.6k / P 22.2k，今日变化ΔOI: C +4.8k / P +6.6k，平值价格ATM: C $7.15 / P $6.88 ｜ ATM IV 59.4%，净 delta 敞口 -69k shares
Top ΔOI: C 400 +771
仓位参考: Max Pain 390 ｜ Call Wall 400（+5.8%，弱）（OI 1.8k） ｜ Put Wall 392.5（+3.8%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 59.4%｜历史 Rank 84%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 69,350 股

📆 11-20 Forward Structure
存量OI: C 345.1k / P 481.4k，今日变化ΔOI: C +47.3k / P +131.6k，平值价格ATM: C $9.83 / P $9.35 ｜ ATM IV 59.0%，净 delta 敞口 402k shares
Top ΔOI: P 140 +54,157 ｜ P 230 +16,321
仓位参考: Max Pain 375 ｜ Call Wall 400（+5.8%，弱）（OI 25.8k）
量化解读： 存量 Put 重｜ATM IV 59.0%｜历史 Rank 84%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 401,753 股

📆 11-23 Forward Structure
存量OI: C 18.9k / P 5.1k，今日变化ΔOI: C +15.3k / P +0.9k，平值价格ATM: C $13.18 / P $10.30 ｜ ATM IV 50.7%，净 delta 敞口 16k shares
Top ΔOI: C 460 +9,933 ｜ C 440 +3,873 ｜ C 415 +334
仓位参考: Max Pain 390 ｜ Put Wall 360（-4.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 50.7%｜历史 Rank 84%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 16,368 股

📆 11-25 Forward Structure
存量OI: C 1.7k / P 3.2k，今日变化ΔOI: C +0.3k / P +1.1k，平值价格ATM: C $12.99 / P $11.97 ｜ ATM IV 52.0%，净 delta 敞口 -6k shares
仓位参考: Max Pain 390 ｜ Call Wall 400（+5.8%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜ATM IV 52.0%｜历史 Rank 84%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 负 6,472 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/TSLA_morning.json