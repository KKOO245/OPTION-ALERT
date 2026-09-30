# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $nan
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-30 235C ΔOI +12,292（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-07 247C ΔOI +4,252 占该期限总 OI 34.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 228.86 → 今开 230.99（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 232.82 ｜ 低 229.22

Options: P/C成交量 0.45 | OI比 0.76 | ATM IV 33.6% | Skew 1.6pp | Term 0.93 | ExpMove ±1.6%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 0.93）｜保护溢价薄（Skew 1.6pp）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（1D）±1.6% ｜ 10-02（3D）±2.6% ｜ 10-05（6D）±3.0% ｜ 10-07（8D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 527,804,474 | GEX Change vs 上次快照 42,548,195 | Flip: Primary Flip: 217.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 671 / LOW 201 / INVALID 514
结构观察区: Primary Flip 217.32（全链重定价，覆盖 99%）
Call Wall 250（弱结构｜现价低于该位 8.1%）
最近结构参考: Flip 217（现价高于该位 5.8%）
量化视角： 正 Gamma（5.28亿，无历史分位）｜正 Gamma 增强（+4255万）｜现价位于 Flip 上方 5.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 225（MaxPain，仅结算参考）；上方 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 217（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 240.0C — Vol 51,254 | 最新价 $0.35 | OI 18821→34691 (ΔOI +15870张) | ΔOI/Volume 31.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15870张（+84.3% vs前日OI），连续性待观察（方向未知）
10-02 245.0C — Vol 29,874 | 最新价 $0.14 | OI 10472→23713 (ΔOI +13241张) | ΔOI/Volume 44.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13241张（+126.4% vs前日OI），连续性待观察（方向未知）
09-30 235.0C — Vol 109,524 | 最新价 $0.41 | OI 5817→18109 (ΔOI +12292张) | ΔOI/Volume 11.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12292张（+211.3% vs前日OI），连续性待观察（方向未知）
09-30 240.0C — Vol 40,513 | 最新价 $0.08 | OI 3603→14672 (ΔOI +11069张) | ΔOI/Volume 27.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11069张（+307.2% vs前日OI），连续性待观察（方向未知）
10-02 242.5C — Vol 19,088 | 最新价 $0.21 | OI 6062→15474 (ΔOI +9412张) | ΔOI/Volume 49.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9412张（+155.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 61,884 张（Put 0 / Call 61,884），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-30  C +50.8k / P +39.0k ｜ Activity HIGH ｜ 1D
10-02  C +66.7k / P +21.0k ｜ Activity HIGH ｜ 3D
10-05  C +14.2k / P +8.1k ｜ Activity HIGH ｜ 6D
10-07  C +7.0k / P +3.1k ｜ Activity HIGH ｜ 8D

📆 09-30 Forward Structure
存量OI: C 106.2k / P 80.5k，今日变化ΔOI: C +50.8k / P +39.0k，平值价格ATM: C $1.79 / P $1.87 ｜ ATM IV 33.6%，净 delta 敞口 -185k shares
Top ΔOI: C 235 +12,292 ｜ C 240 +11,069 ｜ C 237 +9,372
仓位参考: Max Pain 225 ｜ Call Wall 235（+2.3%，弱）（OI 18.1k） ｜ Put Wall 220（-4.3%，弱）（OI 7.5k）
量化解读： 存量 Call 重｜ATM IV 33.6%｜历史 Rank 16%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 184,671 股

📆 10-02 Forward Structure
存量OI: C 444.5k / P 358.0k，今日变化ΔOI: C +66.7k / P +21.0k，平值价格ATM: C $3.02 / P $3.04 ｜ ATM IV 34.9%，净 delta 敞口 -265k shares
Top ΔOI: C 240 +15,870 ｜ C 245 +13,241 ｜ C 242 +9,412
仓位参考: Max Pain 225 ｜ Call Wall 227.5（-1.0%，弱）（OI 76.5k） ｜ Put Wall 215（-6.4%，弱）（OI 25.1k）
量化解读： 存量 Call 重｜ATM IV 34.9%｜历史 Rank 16%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 264,822 股

📆 10-05 Forward Structure
存量OI: C 33.4k / P 16.5k，今日变化ΔOI: C +14.2k / P +8.1k，平值价格ATM: C $3.49 / P $3.45 ｜ ATM IV 29.0%，净 delta 敞口 210k shares
Top ΔOI: C 240 +3,424 ｜ C 242 +1,935 ｜ C 235 +1,713
仓位参考: Max Pain 225 ｜ Call Wall 230（+0.1%，弱）（OI 5.8k） ｜ Put Wall 222.5（-3.2%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 29.0%｜历史 Rank 16%（近端代理）｜IV/RV 1.21×（近似）｜净 delta 敞口 正 209,631 股

📆 10-07 Forward Structure
存量OI: C 8.3k / P 3.9k，今日变化ΔOI: C +7.0k / P +3.1k，平值价格ATM: C $4.25 / P $4.17 ｜ ATM IV 30.4%，净 delta 敞口 38k shares
Top ΔOI: C 247 +4,252 ｜ C 232 +681
仓位参考: Max Pain 228 ｜ Call Wall 247.5（+7.7%）（OI 4.3k） ｜ Put Wall 215（-6.4%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 30.4%｜历史 Rank 16%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 正 37,970 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/NVDA_morning.json