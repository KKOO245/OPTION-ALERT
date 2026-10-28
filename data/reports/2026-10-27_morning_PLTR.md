# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $nan
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 198.84 → 今开 198.02（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 201.83 ｜ 低 196.79

Options: P/C成交量 0.46 | OI比 0.97 | ATM IV 56.0% | Skew 3.7pp | Term 1.12 | ExpMove ±4.2%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构正常（Term 1.12）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（3D）±4.2% ｜ 11-06（10D）±12.0% ｜ 11-13（17D）±13.1% ｜ 11-20（24D）±14.1%
   ⇒ IV–VIX Spread: +37.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 44,436,708 | GEX Change vs 上次快照 146,124 | Flip: Primary Flip: 188.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 638 / LOW 55 / INVALID 245
结构观察区: Primary Flip 188.54（全链重定价，覆盖 100%）
Put Wall 180（弱结构｜现价高于该位 9.8%） | Call Wall 200（弱结构｜现价低于该位 1.2%）
最近结构参考: Call Wall 200（现价低于该位 1.2%）
量化视角： 正 Gamma（4444万，无历史分位）｜正 Gamma 增强（+15万）｜现价位于 Flip 上方 4.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 192（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 189（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 212.5C — Vol 11,763 | 最新价 $0.59 | OI 5541→13423 (ΔOI +7882张) | ΔOI/Volume 67.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7882张（+142.2% vs前日OI），连续性待观察（方向未知）
11-06 100.0P — Vol 8,407 | 最新价 $0.05 | OI 347→6852 (ΔOI +6505张) | ΔOI/Volume 77.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6505张（+1874.6% vs前日OI），连续性待观察（方向未知）
10-30 210.0C — Vol 16,663 | 最新价 $0.91 | OI 9322→15584 (ΔOI +6262张) | ΔOI/Volume 37.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6262张（+67.2% vs前日OI），连续性待观察（方向未知）
10-30 185.0P — Vol 4,470 | 最新价 $0.66 | OI 4112→5382 (ΔOI +1270张) | ΔOI/Volume 28.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1270张（+30.9% vs前日OI），连续性待观察（方向未知）
10-30 215.0C — Vol 3,230 | 最新价 $0.37 | OI 3933→5093 (ΔOI +1160张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1160张（+29.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,079 张（Put 7,775 / Call 15,304），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +20.9k / P +6.6k ｜ Activity HIGH ｜ 3D
11-06  C +5.8k / P +13.0k ｜ Activity HIGH ｜ 10D
11-13  C +1.4k / P +0.7k ｜ Activity HIGH ｜ 17D
11-20  C +2.0k / P +1.9k ｜ Activity HIGH ｜ 24D

📆 10-30 Forward Structure
存量OI: C 127.9k / P 124.6k，今日变化ΔOI: C +20.9k / P +6.6k，平值价格ATM: C $3.95 / P $4.34 ｜ ATM IV 56.0%，净 delta 敞口 141k shares
Top ΔOI: C 212 +7,882 ｜ C 210 +6,262 ｜ P 185 +1,270
仓位参考: Max Pain 192 ｜ Call Wall 200（+1.2%，弱）（OI 15.6k） ｜ Put Wall 180（-8.9%，弱）（OI 9.5k）
量化解读： 存量两侧均衡｜ATM IV 56.0%｜历史 Rank 81%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 140,524 股

📆 11-06 Forward Structure
存量OI: C 39.6k / P 48.2k，今日变化ΔOI: C +5.8k / P +13.0k，平值价格ATM: C $11.70 / P $12.10 ｜ ATM IV 89.7%，净 delta 敞口 57k shares
仓位参考: Max Pain 192 ｜ Call Wall 215（+8.8%，弱）（OI 3.0k） ｜ Put Wall 190（-3.9%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜ATM IV 89.7%｜历史 Rank 81%（近端代理）｜IV/RV 2.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 57,326 股

📆 11-13 Forward Structure
存量OI: C 14.2k / P 17.2k，今日变化ΔOI: C +1.4k / P +0.7k，平值价格ATM: C $13.05 / P $12.80 ｜ ATM IV 75.5%，净 delta 敞口 34k shares
Top ΔOI: C 197 +292 ｜ C 205 +161 ｜ P 195 +157
仓位参考: Max Pain 195 ｜ Call Wall 210（+6.3%，弱）（OI 1.4k） ｜ Put Wall 180（-8.9%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 75.5%｜历史 Rank 81%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,983 股

📆 11-20 Forward Structure
存量OI: C 162.6k / P 168.6k，今日变化ΔOI: C +2.0k / P +1.9k，平值价格ATM: C $13.95 / P $13.88 ｜ ATM IV 68.5%，净 delta 敞口 -33k shares
Top ΔOI: C 260 +823 ｜ P 190 +251 ｜ C 187 +223
仓位参考: Max Pain 175 ｜ Call Wall 200（+1.2%，弱）（OI 12.8k） ｜ Put Wall 185（-6.4%，弱）（OI 10.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.5%｜历史 Rank 81%（近端代理）｜IV/RV 1.53×（近似）｜净 delta 敞口 负 32,933 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/PLTR_morning.json