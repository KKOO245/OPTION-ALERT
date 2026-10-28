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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-30 ATM IV 106.1% vs 11-06 91.5%（差 +14.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 215C ΔOI +1,591（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 203.92 → 今开 214.12（+5.0%） | 较昨收变动（含盘初走势） ｜ 今日高 222.83 ｜ 低 211.29

Options: P/C成交量 0.42 | OI比 0.74 | ATM IV 106.1% | Skew -1.8pp | Term 0.76 | ExpMove ±8.1%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±8.1% ｜ 11-06（10D）±12.1% ｜ 11-13（17D）±15.5% ｜ 11-20（24D）±17.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,114,880 | GEX Change vs 上次快照 6,836,614 | Flip: Primary Flip: 211.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 561 / LOW 92 / INVALID 285
结构观察区: Primary Flip 211.12（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 9.9%）
最近结构参考: Flip 211（现价高于该位 4.1%）
量化视角： 正 Gamma（311万，无历史分位）｜由负转正（+684万）｜现价位于 Flip 上方 4.12%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构） / 210（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 211（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 215.0C — Vol 5,973 | 最新价 $4.20 | OI 1243→2834 (ΔOI +1591张) | ΔOI/Volume 26.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1591张（+128.0% vs前日OI），连续性待观察（方向未知）
10-30 200.0P — Vol 4,359 | 最新价 $6.45 | OI 1622→2978 (ΔOI +1356张) | ΔOI/Volume 31.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1356张（+83.6% vs前日OI），连续性待观察（方向未知）
10-30 220.0C — Vol 6,195 | 最新价 $3.00 | OI 3471→4681 (ΔOI +1210张) | ΔOI/Volume 19.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1210张（+34.9% vs前日OI），连续性待观察（方向未知）
10-30 190.0P — Vol 3,711 | 最新价 $3.05 | OI 2414→3557 (ΔOI +1143张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1143张（+47.4% vs前日OI），连续性待观察（方向未知）
10-30 195.0P — Vol 2,968 | 最新价 $4.45 | OI 1106→2184 (ΔOI +1078张) | ΔOI/Volume 36.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1078张（+97.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,378 张（Put 3,577 / Call 2,801），跨 1 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +10.3k / P +6.2k ｜ Activity HIGH ｜ 3D
11-06  C +1.8k / P +1.0k ｜ Activity HIGH ｜ 10D
11-13  C +0.4k / P +0.2k ｜ Activity HIGH ｜ 17D
11-20  C +1.6k / P +1.0k ｜ Activity HIGH ｜ 24D

📆 10-30 Forward Structure
存量OI: C 62.6k / P 46.2k，今日变化ΔOI: C +10.3k / P +6.2k，平值价格ATM: C $9.05 / P $8.75 ｜ ATM IV 106.1%，净 delta 敞口 515k shares
Top ΔOI: C 215 +1,591 ｜ P 200 +1,356 ｜ C 220 +1,210
仓位参考: Max Pain 210 ｜ Call Wall 220（+0.1%，弱）（OI 4.7k） ｜ Put Wall 200（-9.0%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 106.1%｜历史 Rank 66%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 515,090 股

📆 11-06 Forward Structure
存量OI: C 16.6k / P 15.1k，今日变化ΔOI: C +1.8k / P +1.0k，平值价格ATM: C $13.42 / P $13.25 ｜ ATM IV 91.5%，净 delta 敞口 87k shares
Top ΔOI: C 217 +567 ｜ C 177 +489
仓位参考: Max Pain 230 ｜ Call Wall 200（-9.0%，弱）（OI 1.4k） ｜ Put Wall 235（+6.9%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜ATM IV 91.5%｜历史 Rank 66%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 86,927 股

📆 11-13 Forward Structure
存量OI: C 6.9k / P 8.0k，今日变化ΔOI: C +0.4k / P +0.2k，平值价格ATM: C $16.84 / P $17.25 ｜ ATM IV 86.6%，净 delta 敞口 5k shares
Top ΔOI: C 255 +154 ｜ C 230 +128 ｜ P 200 -115
仓位参考: Max Pain 240 ｜ Call Wall 240（+9.2%，弱）（OI 0.5k） ｜ Put Wall 240（+9.2%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 86.6%｜历史 Rank 66%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,432 股

📆 11-20 Forward Structure
存量OI: C 57.3k / P 68.9k，今日变化ΔOI: C +1.6k / P +1.0k，平值价格ATM: C $19.39 / P $18.75 ｜ ATM IV 84.2%，净 delta 敞口 55k shares
Top ΔOI: C 320 +421 ｜ C 220 +328
仓位参考: Max Pain 230 ｜ Call Wall 240（+9.2%，弱）（OI 2.8k） ｜ Put Wall 200（-9.0%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 84.2%｜历史 Rank 66%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 55,138 股

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 106.1% vs 11-06 91.5%（差 +14.6pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/BE_morning.json