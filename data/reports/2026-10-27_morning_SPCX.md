# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $769.58 ｜ QQQ $721.25
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
🟡 **近现价集中开仓**: 10-28 155C ΔOI +4,548（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 146.90 → 今开 147.49（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 149.74 ｜ 低 146.63

Options: P/C成交量 0.43 | OI比 0.95 | ATM IV 62.4% | Skew -0.0pp | Term 0.81 | ExpMove ±2.9%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-28（1D）±2.9% ｜ 10-30（3D）±4.5% ｜ 11-02（6D）±5.2% ｜ 11-04（8D）±6.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,305,209 | GEX Change vs 上次快照 55,640,350 | Flip: Primary Flip: 148.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 720 / LOW 140 / INVALID 534
结构观察区: Primary Flip 148.02（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 148（现价高于该位 1.1%）
量化视角： 正 Gamma（2231万，无历史分位）｜由负转正（+5564万）｜现价位于 Flip 上方 1.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 175.0C — Vol 40,398 | 最新价 $0.28 | OI 3036→36172 (ΔOI +33136张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33136张（+1091.4% vs前日OI），连续性待观察（方向未知）
10-30 160.0C — Vol 45,093 | 最新价 $0.37 | OI 12356→39941 (ΔOI +27585张) | ΔOI/Volume 61.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27585张（+223.2% vs前日OI），连续性待观察（方向未知）
10-30 162.5C — Vol 24,987 | 最新价 $0.24 | OI 4306→24969 (ΔOI +20663张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20663张（+479.9% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 13,602 | 最新价 $6.80 | OI 19802→26369 (ΔOI +6567张) | ΔOI/Volume 48.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6567张（+33.2% vs前日OI），连续性待观察（方向未知）
10-28 100.0P — Vol 5,933 | 最新价 $0.01 | OI 89→5411 (ΔOI +5322张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5322张（+5979.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 93,273 张（Put 5,322 / Call 87,951），跨 4 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +14.7k / P +15.6k ｜ Activity HIGH ｜ 1D
10-30  C +67.5k / P +8.5k ｜ Activity HIGH ｜ 3D
11-02  C +5.9k / P +2.6k ｜ Activity HIGH ｜ 6D
11-04  C +1.5k / P +1.9k ｜ Activity HIGH ｜ 8D

📆 10-28 Forward Structure
存量OI: C 42.0k / P 39.8k，今日变化ΔOI: C +14.7k / P +15.6k，平值价格ATM: C $1.91 / P $2.40 ｜ ATM IV 62.4%，净 delta 敞口 164k shares
Top ΔOI: C 155 +4,548 ｜ C 152 +2,239
仓位参考: Max Pain 150 ｜ Call Wall 155（+3.6%）（OI 8.3k） ｜ Put Wall 160（+7.0%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 62.4%｜历史 Rank 71%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 164,155 股

📆 10-30 Forward Structure
存量OI: C 257.9k / P 183.3k，今日变化ΔOI: C +67.5k / P +8.5k，平值价格ATM: C $3.09 / P $3.60 ｜ ATM IV 58.9%，净 delta 敞口 1.1M shares
Top ΔOI: C 160 +27,585 ｜ C 162 +20,663 ｜ C 150 +4,955
仓位参考: Max Pain 150 ｜ Call Wall 160（+7.0%，弱）（OI 39.9k） ｜ Put Wall 150（+0.3%，弱）（OI 14.3k）
量化解读： 存量 Call 重｜ATM IV 58.9%｜历史 Rank 71%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,054,688 股

📆 11-02 Forward Structure
存量OI: C 16.8k / P 8.0k，今日变化ΔOI: C +5.9k / P +2.6k，平值价格ATM: C $3.60 / P $4.25 ｜ ATM IV 48.5%，净 delta 敞口 148k shares
Top ΔOI: C 152 +1,242 ｜ C 157 +1,028 ｜ C 160 +982
仓位参考: Max Pain 148 ｜ Call Wall 160（+7.0%，弱）（OI 2.4k） ｜ Put Wall 140（-6.4%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 48.5%｜历史 Rank 71%（近端代理）｜IV/RV 0.81×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 148,358 股

📆 11-04 Forward Structure
存量OI: C 6.8k / P 3.1k，今日变化ΔOI: C +1.5k / P +1.9k，平值价格ATM: C $4.50 / P $4.95 ｜ ATM IV 52.0%，净 delta 敞口 -110k shares
Top ΔOI: C 160 +616 ｜ P 200 +593 ｜ P 180 +582
仓位参考: Max Pain 150 ｜ Call Wall 160（+7.0%，弱）（OI 1.3k） ｜ Put Wall 150（+0.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.0%｜历史 Rank 71%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 负 110,358 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SPCX_morning.json