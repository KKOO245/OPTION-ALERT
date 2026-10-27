# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $769.68 ｜ QQQ $721.25
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
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
🟡 **近现价集中开仓**: 10-28 50C ΔOI +2,511（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 47P ΔOI +586 占该期限总 OI 11.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 48.66 → 今开 48.50（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 48.90 ｜ 低 48.48

Options: P/C成交量 0.21 | OI比 0.69 | ATM IV 47.7% | Skew 4.3pp | Term 0.78 | ExpMove ±2.2%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 4.3pp）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-28（1D）±2.2% ｜ 10-30（3D）±3.3% ｜ 11-02（6D）±4.1% ｜ 11-04（8D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 303,446 | GEX Change vs 上次快照 10,203,387 | Flip: Primary Flip: 48.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 745 / LOW 95 / INVALID 352
结构观察区: Primary Flip 48.66（全链重定价，覆盖 99%）
Put Wall 50（弱结构｜现价低于该位 2.7%）
最近结构参考: Flip 49（现价高于该位 0.0%）
量化视角： 正 Gamma（30万，无历史分位）｜由负转正（+1020万）｜现价位于 Flip 上方 0.02%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 49（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 41.0P — Vol 10,085 | 最新价 $0.20 | OI 539→10458 (ΔOI +9919张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9919张（+1840.3% vs前日OI），连续性待观察（方向未知）
10-28 50.0C — Vol 5,102 | 最新价 $0.17 | OI 3925→6436 (ΔOI +2511张) | ΔOI/Volume 49.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2511张（+64.0% vs前日OI），连续性待观察（方向未知）
10-30 52.5C — Vol 1,171 | 最新价 $0.06 | OI 1503→3484 (ΔOI +1981张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1981张（+131.8% vs前日OI），连续性待观察（方向未知）
11-20 52.5C — Vol 1,992 | 最新价 $0.69 | OI 391→2336 (ΔOI +1945张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1945张（+497.4% vs前日OI），连续性待观察（方向未知）
10-28 49.5C — Vol 2,095 | 最新价 $0.29 | OI 329→1923 (ΔOI +1594张) | ΔOI/Volume 76.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1594张（+484.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,950 张（Put 9,919 / Call 8,031），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +9.2k / P +4.2k ｜ Activity HIGH ｜ 1D
10-30  C +5.8k / P +0.3k ｜ Activity MEDIUM △ ｜ 3D
11-02  C +0.8k / P +1.1k ｜ Activity HIGH ｜ 6D
11-04  C +0.9k / P +2.1k ｜ Activity HIGH ｜ 8D

📆 10-28 Forward Structure
存量OI: C 25.5k / P 17.6k，今日变化ΔOI: C +9.2k / P +4.2k，平值价格ATM: C $0.66 / P $0.42 ｜ ATM IV 47.7%，净 delta 敞口 201k shares
Top ΔOI: C 50 +2,511 ｜ C 49 +1,594 ｜ C 49 +1,102
仓位参考: Max Pain 49 ｜ Call Wall 50（+2.7%）（OI 6.4k） ｜ Put Wall 45.5（-6.5%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 47.7%｜历史 Rank 80%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 201,067 股

10-30（MEDIUM △）Top ΔOI: 52C +1,981 ｜ 50C +1,483
10-30（MEDIUM △）仓位参考: Max Pain 51 ｜ Call Wall 52.5（+7.9%，弱）（OI 3.5k） ｜ Put Wall 45（-7.5%，弱）（OI 4.2k）

📆 11-02 Forward Structure
存量OI: C 2.8k / P 2.6k，今日变化ΔOI: C +0.8k / P +1.1k，平值价格ATM: C $1.11 / P $0.90 ｜ ATM IV 36.6%，净 delta 敞口 -8k shares
Top ΔOI: P 47 +586 ｜ C 49 +166 ｜ C 50 +149
仓位参考: Max Pain 50 ｜ Call Wall 50.5（+3.8%，弱）（OI 0.5k） ｜ Put Wall 47.5（-2.4%）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.6%｜历史 Rank 80%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 7,844 股

📆 11-04 Forward Structure
存量OI: C 8.3k / P 2.9k，今日变化ΔOI: C +0.9k / P +2.1k，平值价格ATM: C $1.19 / P $1.01 ｜ ATM IV 39.1%，净 delta 敞口 -3k shares
Top ΔOI: P 44 +1,434
仓位参考: Max Pain 48 ｜ Call Wall 51.5（+5.8%）（OI 3.0k） ｜ Put Wall 44（-9.6%）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 39.1%｜历史 Rank 80%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 3,340 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SLV_morning.json