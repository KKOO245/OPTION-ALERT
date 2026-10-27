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
🟡 **近现价集中开仓**: 10-30 200C ΔOI +10,357（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 196.75 → 今开 195.02（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 197.49 ｜ 低 190.57

Options: P/C成交量 0.85 | OI比 1.10 | ATM IV 58.4% | Skew 3.7pp | Term 1.09 | ExpMove ±5.4%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构正常（Term 1.09）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.85×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（4D）±5.4% ｜ 11-06（11D）±12.4% ｜ 11-13（18D）±13.7% ｜ 11-20（25D）±14.5%
   ⇒ IV–VIX Spread: +39.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 34,268,273 | GEX Change vs 上次快照 20,119,015 | Flip: Primary Flip: 187.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 512 / LOW 180 / INVALID 208
结构观察区: Primary Flip 187.46（全链重定价，覆盖 100%）
Put Wall 180（弱结构｜现价高于该位 9.8%） | Call Wall 200（弱结构｜现价低于该位 1.2%）
最近结构参考: Call Wall 200（现价低于该位 1.2%）
量化视角： 正 Gamma（3427万，无历史分位）｜正 Gamma 增强（+2012万）｜现价位于 Flip 上方 5.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 192（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 187（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 200.0C — Vol 20,399 | 最新价 $3.80 | OI 4487→14844 (ΔOI +10357张) | ΔOI/Volume 50.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10357张（+230.8% vs前日OI），连续性待观察（方向未知）
10-30 202.5C — Vol 13,907 | 最新价 $2.88 | OI 1512→10949 (ΔOI +9437张) | ΔOI/Volume 67.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9437张（+624.1% vs前日OI），连续性待观察（方向未知）
10-30 207.5C — Vol 12,892 | 最新价 $1.52 | OI 2393→10520 (ΔOI +8127张) | ΔOI/Volume 63.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8127张（+339.6% vs前日OI），连续性待观察（方向未知）
10-30 115.0P — Vol 6,837 | 最新价 $0.02 | OI 608→7177 (ΔOI +6569张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6569张（+1080.4% vs前日OI），连续性待观察（方向未知）
10-30 125.0P — Vol 6,766 | 最新价 $0.02 | OI 1926→7399 (ΔOI +5473张) | ΔOI/Volume 80.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5473张（+284.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 39,963 张（Put 12,042 / Call 27,921），跨 1 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +42.0k / P +31.1k ｜ Activity HIGH ｜ 4D
11-06  C +3.5k / P +4.2k ｜ Activity HIGH ｜ 11D
11-13  C +0.7k / P +0.8k ｜ Activity HIGH ｜ 18D
11-20  C +0.5k / P +0.9k ｜ Activity MEDIUM △ ｜ 25D

📆 10-30 Forward Structure
存量OI: C 107.0k / P 118.0k，今日变化ΔOI: C +42.0k / P +31.1k，平值价格ATM: C $5.05 / P $5.61 ｜ ATM IV 58.4%，净 delta 敞口 1.1M shares
Top ΔOI: C 200 +10,357 ｜ C 202 +9,437 ｜ C 207 +8,127
仓位参考: Max Pain 192 ｜ Call Wall 200（+1.2%，弱）（OI 14.8k） ｜ Put Wall 190（-3.8%，弱）（OI 8.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.4%｜历史 Rank 87%（近端代理）｜IV/RV 1.29×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,124,155 股

📆 11-06 Forward Structure
存量OI: C 33.8k / P 35.2k，今日变化ΔOI: C +3.5k / P +4.2k，平值价格ATM: C $12.02 / P $12.45 ｜ ATM IV 87.2%，净 delta 敞口 54k shares
Top ΔOI: P 150 +880 ｜ C 215 +496
仓位参考: Max Pain 190 ｜ Call Wall 215（+8.8%，弱）（OI 2.6k） ｜ Put Wall 190（-3.8%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜ATM IV 87.2%｜历史 Rank 87%（近端代理）｜IV/RV 1.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 54,343 股

📆 11-13 Forward Structure
存量OI: C 12.8k / P 16.5k，今日变化ΔOI: C +0.7k / P +0.8k，平值价格ATM: C $12.81 / P $14.22 ｜ ATM IV 75.5%，净 delta 敞口 3k shares
Top ΔOI: P 160 +329
仓位参考: Max Pain 195 ｜ Call Wall 210（+6.3%，弱）（OI 1.3k） ｜ Put Wall 180（-8.9%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 75.5%｜历史 Rank 87%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,979 股

11-20（MEDIUM △）Top ΔOI: 165P +285 ｜ 180C -189
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+1.2%，弱）（OI 12.9k） ｜ Put Wall 185（-6.4%，弱）（OI 10.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/PLTR_morning.json