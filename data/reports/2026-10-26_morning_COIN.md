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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 164.45 → 今开 168.00（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 169.84 ｜ 低 163.33

Options: P/C成交量 0.40 | OI比 0.49 | ATM IV 87.8% | Skew 0.9pp | Term 0.79 | ExpMove ±9.8%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±9.8% ｜ 11-06（11D）±12.5% ｜ 11-13（18D）±14.7% ｜ 11-20（25D）±15.9%
   ⇒ IV–VIX Spread: +68.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,970,417 | GEX Change vs 上次快照 4,038,239 | Flip: Primary Flip: 153.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 464 / LOW 105 / INVALID 275
结构观察区: Primary Flip 153.16（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 5.6%）
最近结构参考: Flip 153（现价高于该位 4.8%）
量化视角： 正 Gamma（797万，无历史分位）｜正 Gamma 增强（+404万）｜现价位于 Flip 上方 4.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 172.5C — Vol 10,118 | 最新价 $4.79 | OI 1830→11600 (ΔOI +9770张) | ΔOI/Volume 96.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9770张（+533.9% vs前日OI），连续性待观察（方向未知）
10-30 180.0C — Vol 10,626 | 最新价 $2.75 | OI 2784→11977 (ΔOI +9193张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9193张（+330.2% vs前日OI），连续性待观察（方向未知）
10-30 170.0C — Vol 5,817 | 最新价 $5.70 | OI 388→5533 (ΔOI +5145张) | ΔOI/Volume 88.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5145张（+1326.0% vs前日OI），连续性待观察（方向未知）
10-30 177.5C — Vol 5,238 | 最新价 $3.29 | OI 1997→6435 (ΔOI +4438张) | ΔOI/Volume 84.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4438张（+222.2% vs前日OI），连续性待观察（方向未知）
11-06 90.0P — Vol 2,814 | 最新价 $0.17 | OI 3160→5145 (ΔOI +1985张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1985张（+62.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 30,531 张（Put 1,985 / Call 28,546），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +31.8k / P +9.9k ｜ Activity HIGH ｜ 4D
11-06  C +1.2k / P +3.9k ｜ Activity HIGH ｜ 11D
11-13  C +0.7k / P +0.7k ｜ Activity HIGH ｜ 18D
11-20  C +0.9k / P +1.2k ｜ Activity HIGH ｜ 25D

📆 10-30 Forward Structure
存量OI: C 66.6k / P 32.9k，今日变化ΔOI: C +31.8k / P +9.9k，平值价格ATM: C $10.00 / P $5.65 ｜ ATM IV 87.8%，净 delta 敞口 788k shares
Top ΔOI: C 172 +9,770 ｜ C 180 +9,193 ｜ C 170 +5,145
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+7.5%，弱）（OI 11.6k） ｜ Put Wall 150（-6.5%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 87.8%｜历史 Rank 78%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 787,875 股

📆 11-06 Forward Structure
存量OI: C 8.2k / P 16.1k，今日变化ΔOI: C +1.2k / P +3.9k，平值价格ATM: C $12.28 / P $7.80 ｜ ATM IV 77.9%，净 delta 敞口 6k shares
仓位参考: Max Pain 172 ｜ Call Wall 175（+9.1%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 77.9%｜历史 Rank 78%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,768 股

📆 11-13 Forward Structure
存量OI: C 6.8k / P 8.6k，今日变化ΔOI: C +0.7k / P +0.7k，平值价格ATM: C $14.44 / P $9.11 ｜ ATM IV 70.2%，净 delta 敞口 10k shares
Top ΔOI: C 175 +157 ｜ C 170 +133
仓位参考: Max Pain 175 ｜ Call Wall 170（+5.9%，弱）（OI 0.2k） ｜ Put Wall 160（-0.3%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.2%｜历史 Rank 78%（近端代理）｜IV/RV 1.32×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 9,816 股

📆 11-20 Forward Structure
存量OI: C 69.2k / P 47.8k，今日变化ΔOI: C +0.9k / P +1.2k，平值价格ATM: C $15.00 / P $10.55 ｜ ATM IV 74.0%，净 delta 敞口 34k shares
Top ΔOI: C 170 +278
仓位参考: Max Pain 170 ｜ Call Wall 170（+5.9%）（OI 13.6k） ｜ Put Wall 150（-6.5%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.0%｜历史 Rank 78%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 正 34,117 股

📅 事件差分（观察，非因果）: 10-30（4D）ATM IV 87.8% vs 11-06 77.9%（差 +9.9pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/COIN_morning.json