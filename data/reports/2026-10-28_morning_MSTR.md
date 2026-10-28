# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.58 ｜ QQQ $721.85
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　⏰ 今日
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4　⏰ 今日
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **事件差分**: 10-30（2D）ATM IV 103.7% vs 11-06 82.1%（差 +21.6pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 147C ΔOI +5,073（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 141.40 → 今开 139.57（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 142.38 ｜ 低 139.14

Options: P/C成交量 0.81 | OI比 0.73 | ATM IV 103.7% | Skew -0.2pp | Term 0.69 | ExpMove ±6.6%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±6.6% ｜ 11-06（9D）±10.3% ｜ 11-13（16D）±12.9% ｜ 11-20（23D）±15.1%
   ⇒ IV–VIX Spread: +86.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,471,457 | GEX Change vs 上次快照 4,616,177 | Flip: Primary Flip: 135.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 579 / LOW 92 / INVALID 245
结构观察区: Primary Flip 135.03（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 4.5%）
最近结构参考: Flip 135（现价高于该位 4.5%）
量化视角： 正 Gamma（2747万，无历史分位）｜正 Gamma 增强（+462万）｜现价位于 Flip 上方 4.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 147.0C — Vol 5,824 | 最新价 $2.70 | OI 1222→6295 (ΔOI +5073张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5073张（+415.1% vs前日OI），连续性待观察（方向未知）
10-30 95.0P — Vol 2,081 | 最新价 $0.05 | OI 2904→4881 (ΔOI +1977张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1977张（+68.1% vs前日OI），连续性待观察（方向未知）
10-30 145.0C — Vol 3,570 | 最新价 $3.40 | OI 2831→4269 (ΔOI +1438张) | ΔOI/Volume 40.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1438张（+50.8% vs前日OI），连续性待观察（方向未知）
10-30 150.0C — Vol 5,683 | 最新价 $1.89 | OI 10970→12263 (ΔOI +1293张) | ΔOI/Volume 22.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1293张（+11.8% vs前日OI），连续性待观察（方向未知）
11-06 202.5C — Vol 911 | 最新价 $0.15 | OI 0→904 (ΔOI +904张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增904张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,685 张（Put 1,977 / Call 8,708），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +13.0k / P -1.8k ｜ Activity HIGH ｜ 2D
11-06  C +1.8k / P +4.4k ｜ Activity HIGH ｜ 9D
11-13  C +0.4k / P +2.7k ｜ Activity MEDIUM △ ｜ 16D
11-20  C +0.9k / P +3.2k ｜ Activity HIGH ｜ 23D

📆 10-30 Forward Structure
存量OI: C 233.7k / P 171.4k，今日变化ΔOI: C +13.0k / P -1.8k，平值价格ATM: C $4.68 / P $4.65 ｜ ATM IV 103.7%，净 delta 敞口 510k shares
Top ΔOI: C 147 +5,073
仓位参考: Max Pain 142 ｜ Call Wall 152.5（+8.1%，弱）（OI 37.8k）
量化解读： 存量 Call 重｜ATM IV 103.7%｜历史 Rank 84%（近端代理）｜IV/RV 1.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 509,788 股

📆 11-06 Forward Structure
存量OI: C 24.2k / P 54.7k，今日变化ΔOI: C +1.8k / P +4.4k，平值价格ATM: C $7.31 / P $7.25 ｜ ATM IV 82.1%，净 delta 敞口 -6k shares
仓位参考: Max Pain 155 ｜ Call Wall 150（+6.3%，弱）（OI 1.4k） ｜ Put Wall 155（+9.9%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 82.1%｜历史 Rank 84%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,187 股

11-13（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 155（+9.9%，弱）（OI 2.4k）

📆 11-20 Forward Structure
存量OI: C 146.9k / P 111.8k，今日变化ΔOI: C +0.9k / P +3.2k，平值价格ATM: C $10.65 / P $10.70 ｜ ATM IV 74.1%，净 delta 敞口 -62k shares
Top ΔOI: P 157 +292
仓位参考: Max Pain 135 ｜ Call Wall 135（-4.3%）（OI 42.4k） ｜ Put Wall 130（-7.9%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.1%｜历史 Rank 84%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 61,652 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 103.7% vs 11-06 82.1%（差 +21.6pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/MSTR_morning.json