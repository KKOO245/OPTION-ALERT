# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $756.41 ｜ QQQ $687.06
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 96.1% vs 11-20 81.8%（差 +14.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 125C ΔOI +1,597（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 121.07 → 今开 120.49（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 123.63 ｜ 低 120.33

Options: P/C成交量 0.56 | OI比 0.60 | ATM IV 96.1% | Skew 3.5pp | Term 0.79 | ExpMove ±6.2%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 3.5pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±6.2% ｜ 11-20（9D）±10.3% ｜ 11-27（16D）±13.1% ｜ 12-04（23D）±15.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,086,844 | GEX Change vs 上次快照 1,092,757 | Flip: Primary Flip: 120.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 543 / LOW 179 / INVALID 260
结构观察区: Primary Flip 120.24（全链重定价，覆盖 100%）
最近结构参考: Flip 120（现价高于该位 0.7%）
量化视角： 正 Gamma（609万，无历史分位）｜正 Gamma 增强（+109万）｜现价位于 Flip 上方 0.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 126（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 120（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 80.0P — Vol 3,236 | 最新价 $0.28 | OI 5876→7726 (ΔOI +1850张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1850张（+31.5% vs前日OI），连续性待观察（方向未知）
11-13 125.0C — Vol 4,877 | 最新价 $2.54 | OI 1342→2939 (ΔOI +1597张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1597张（+119.0% vs前日OI），连续性待观察（方向未知）
11-20 105.0P — Vol 1,974 | 最新价 $1.56 | OI 4350→5640 (ΔOI +1290张) | ΔOI/Volume 65.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1290张（+29.7% vs前日OI），连续性待观察（方向未知）
11-13 123.0C — Vol 4,354 | 最新价 $3.30 | OI 149→1332 (ΔOI +1183张) | ΔOI/Volume 27.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1183张（+794.0% vs前日OI），连续性待观察（方向未知）
11-13 60.0P — Vol 1,000 | 最新价 $0.01 | OI 1726→2708 (ΔOI +982张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增982张（+56.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,902 张（Put 4,122 / Call 2,780），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +9.0k / P -0.5k ｜ Activity HIGH ｜ 2D
11-20  C +2.9k / P +8.1k ｜ Activity HIGH ｜ 9D
11-27  C +1.6k / P +5.2k ｜ Activity MEDIUM △ ｜ 16D
12-04  C +1.0k / P +5.0k ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 239.3k / P 144.6k，今日变化ΔOI: C +9.0k / P -0.5k，平值价格ATM: C $3.85 / P $3.65 ｜ ATM IV 96.1%，净 delta 敞口 561k shares
Top ΔOI: C 125 +1,597 ｜ C 123 +1,183
仓位参考: Max Pain 126 ｜ Call Wall 133（+9.8%，弱）（OI 43.8k） ｜ Put Wall 110（-9.2%，弱）（OI 5.1k）
量化解读： 存量 Call 重｜ATM IV 96.1%｜历史 Rank 76%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 560,512 股

📆 11-20 Forward Structure
存量OI: C 167.3k / P 157.8k，今日变化ΔOI: C +2.9k / P +8.1k，平值价格ATM: C $6.50 / P $6.00 ｜ ATM IV 81.8%，净 delta 敞口 108k shares
Top ΔOI: P 105 +1,290
仓位参考: Max Pain 135 ｜ Put Wall 110（-9.2%，弱）（OI 15.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.8%｜历史 Rank 76%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 107,762 股

11-27（MEDIUM △）Top ΔOI: 95P +680
11-27（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 130（+7.3%，弱）（OI 1.0k） ｜ Put Wall 115（-5.0%，弱）（OI 2.0k）

📆 12-04 Forward Structure
存量OI: C 16.6k / P 27.9k，今日变化ΔOI: C +1.0k / P +5.0k，平值价格ATM: C $10.05 / P $8.57 ｜ ATM IV 75.7%，净 delta 敞口 -94k shares
Top ΔOI: P 90 +684
仓位参考: Max Pain 150 ｜ Put Wall 130（+7.3%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 75.7%｜历史 Rank 76%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 94,110 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 96.1% vs 11-20 81.8%（差 +14.4pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/MSTR_morning.json