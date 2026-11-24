# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $717.83 ｜ QQQ $636.91
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 155P ΔOI +1,135（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 168.15 → 今开 162.69（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 164.18 ｜ 低 153.45

Options: P/C成交量 0.77 | OI比 0.65 | ATM IV 124.2% | Skew 13.9pp | Term 0.83 | ExpMove ±9.4%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价显著（Skew 13.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±9.4% ｜ 12-04（10D）±15.8% ｜ 12-11（17D）±19.2% ｜ 12-18（24D）±22.3%
   ⇒ IV–VIX Spread: +96.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,000,917 | GEX Change vs 上次快照 -3,064,221 | Flip: Primary Flip: 178.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 594 / LOW 105 / INVALID 261
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 178.51（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价高于该位 5.6%）
最近结构参考: Put Wall 150（现价高于该位 5.6%）
量化视角： 负 Gamma（600万，无历史分位）｜负 Gamma 加深（306万）｜现价位于 Flip 下方 11.26%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 168（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 179（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 140.0P — Vol 3,157 | 最新价 $3.47 | OI 740→3115 (ΔOI +2375张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2375张（+320.9% vs前日OI），连续性待观察（方向未知）
11-27 155.0P — Vol 2,171 | 最新价 $3.34 | OI 466→1601 (ΔOI +1135张) | ΔOI/Volume 52.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1135张（+243.6% vs前日OI），连续性待观察（方向未知）
11-27 129.0P — Vol 1,164 | 最新价 $0.43 | OI 231→1313 (ΔOI +1082张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1082张（+468.4% vs前日OI），连续性待观察（方向未知）
11-27 200.0C — Vol 4,015 | 最新价 $0.59 | OI 2566→3618 (ΔOI +1052张) | ΔOI/Volume 26.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1052张（+41.0% vs前日OI），连续性待观察（方向未知）
11-27 170.0P — Vol 3,925 | 最新价 $8.96 | OI 770→1805 (ΔOI +1035张) | ΔOI/Volume 26.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1035张（+134.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,679 张（Put 5,627 / Call 1,052），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +7.1k / P +8.1k ｜ Activity HIGH ｜ 3D
12-04  C +1.3k / P +4.4k ｜ Activity HIGH ｜ 10D
12-11  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
12-18  C +1.0k / P -0.4k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 47.6k / P 30.9k，今日变化ΔOI: C +7.1k / P +8.1k，平值价格ATM: C $8.17 / P $6.70 ｜ ATM IV 124.2%，净 delta 敞口 -224k shares
Top ΔOI: P 155 +1,135 ｜ P 129 +1,082
仓位参考: Max Pain 168 ｜ Call Wall 150（-5.3%，弱）（OI 2.2k） ｜ Put Wall 170（+7.3%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 124.2%｜历史 Rank 79%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 223,923 股

📆 12-04 Forward Structure
存量OI: C 12.5k / P 15.3k，今日变化ΔOI: C +1.3k / P +4.4k，平值价格ATM: C $13.25 / P $11.82 ｜ ATM IV 115.9%，净 delta 敞口 -138k shares
Top ΔOI: P 140 +2,375 ｜ P 160 +512 ｜ P 144 +442
仓位参考: Max Pain 195 ｜ Call Wall 165（+4.2%，弱）（OI 0.3k） ｜ Put Wall 150（-5.3%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 115.9%｜历史 Rank 79%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 138,029 股

12-11（MEDIUM △）Top ΔOI: 170C -70
12-11（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 165（+4.2%，弱）（OI 0.1k） ｜ Put Wall 150（-5.3%，弱）（OI 0.4k）

📆 12-18 Forward Structure
存量OI: C 63.3k / P 75.0k，今日变化ΔOI: C +1.0k / P -0.4k，平值价格ATM: C $18.32 / P $17.05 ｜ ATM IV 108.8%，净 delta 敞口 44k shares
Top ΔOI: C 190 -276 ｜ P 230 -199
仓位参考: Max Pain 200 ｜ Call Wall 170（+7.3%，弱）（OI 1.9k） ｜ Put Wall 150（-5.3%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 108.8%｜历史 Rank 79%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 正 44,107 股

📅 事件差分（观察，非因果）: 11-27（3D）ATM IV 124.2% vs 12-04 115.9%（差 +8.3pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/BE_morning.json