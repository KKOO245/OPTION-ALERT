# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-28 375C ΔOI +1,859（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 462C ΔOI +3,165 占该期限总 OI 10.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 372.22 → 今开 373.20（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 377.32 ｜ 低 365.27

Options: P/C成交量 0.92 | OI比 0.63 | ATM IV 88.9% | Skew 12.0pp | Term 0.44 | ExpMove ±4.1%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.44，近月 IV 高于远月）｜保护溢价显著（Skew 12.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.92×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-28（2D）±4.1% ｜ 10-30（4D）±4.8% ｜ 11-02（7D）±5.2% ｜ 11-04（9D）±6.7%
   ⇒ IV–VIX Spread: +69.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 96,024,815 | GEX Change vs 上次快照 80,465,980 | Flip: Primary Flip: 360.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 862 / LOW 563 / INVALID 701
结构观察区: Primary Flip 360.90（全链重定价，覆盖 94%）
Call Wall 400（弱结构｜现价低于该位 4.6%）
最近结构参考: Call Wall 400（现价低于该位 4.6%）
量化视角： 正 Gamma（9602万，无历史分位）｜正 Gamma 增强（+8047万）｜现价位于 Flip 上方 5.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 372（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 361（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 230.0P — Vol 21,615 | 最新价 $0.03 | OI 2752→21935 (ΔOI +19183张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19183张（+697.1% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 14,000 | 最新价 $0.01 | OI 804→14512 (ΔOI +13708张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13708张（+1705.0% vs前日OI），连续性待观察（方向未知）
11-06 210.0P — Vol 7,637 | 最新价 $0.06 | OI 176→7055 (ΔOI +6879张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6879张（+3908.5% vs前日OI），连续性待观察（方向未知）
11-20 380.0C — Vol 7,704 | 最新价 $13.30 | OI 5422→10009 (ΔOI +4587张) | ΔOI/Volume 59.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4587张（+84.6% vs前日OI），连续性待观察（方向未知）
10-30 382.5C — Vol 5,869 | 最新价 $4.25 | OI 715→5281 (ΔOI +4566张) | ΔOI/Volume 77.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4566张（+638.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 48,923 张（Put 39,770 / Call 9,153），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 93.9k / P 59.6k，今日成交量: C 149.3k / P 138.0k，平值价格ATM: C $2.72 / P $5.30 ｜ ATM IV 88.9%，预期波动 ±2.1%，Max Pain 372
Top ΔOI: P 252 +4,557 ｜ P 247 +2,997 ｜ C 417 +2,281

📆 Forward Expiration Structure

10-28  C +6.8k / P +9.3k ｜ Activity HIGH ｜ 2D
10-30  C +37.0k / P +48.6k ｜ Activity HIGH ｜ 4D
11-02  C +10.2k / P +0.9k ｜ Activity HIGH ｜ 7D
11-04  C +0.6k / P +0.4k ｜ Activity HIGH ｜ 9D

📆 10-28 Forward Structure
存量OI: C 21.6k / P 25.6k，今日变化ΔOI: C +6.8k / P +9.3k，平值价格ATM: C $2.61 / P $12.87 ｜ ATM IV 46.5%，净 delta 敞口 270k shares
Top ΔOI: C 375 +1,859
仓位参考: Max Pain 375 ｜ Call Wall 375（-1.7%，弱）（OI 2.2k） ｜ Put Wall 350（-8.3%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 46.5%｜历史 Rank 93%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 269,767 股

📆 10-30 Forward Structure
存量OI: C 144.5k / P 161.7k，今日变化ΔOI: C +37.0k / P +48.6k，平值价格ATM: C $4.25 / P $14.21 ｜ ATM IV 45.9%，净 delta 敞口 1.5M shares
Top ΔOI: P 230 +19,183 ｜ C 382 +4,566
仓位参考: Max Pain 372 ｜ Call Wall 400（+4.8%，弱）（OI 13.1k）
量化解读： 存量两侧均衡｜ATM IV 45.9%｜历史 Rank 93%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,505,280 股

📆 11-02 Forward Structure
存量OI: C 23.4k / P 7.0k，今日变化ΔOI: C +10.2k / P +0.9k，平值价格ATM: C $5.03 / P $14.61 ｜ ATM IV 40.7%，净 delta 敞口 71k shares
仓位参考: Max Pain 378 ｜ Put Wall 380（-0.4%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 40.7%｜历史 Rank 93%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 70,646 股

📆 11-04 Forward Structure
存量OI: C 2.2k / P 2.3k，今日变化ΔOI: C +0.6k / P +0.4k，平值价格ATM: C $6.57 / P $19.00 ｜ ATM IV 42.7%，净 delta 敞口 20k shares
Top ΔOI: C 400 +162 ｜ C 372 +67 ｜ C 375 +66
仓位参考: Max Pain 380 ｜ Call Wall 400（+4.8%）（OI 0.4k） ｜ Put Wall 385（+0.9%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.7%｜历史 Rank 93%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 19,953 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/TSLA_morning.json