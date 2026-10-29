# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-29 288C ΔOI +13,820（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-29 288C ΔOI +13,820 占该期限总 OI 13.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 280.18 → 今开 280.35（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 281.23 ｜ 低 279.94

Options: P/C成交量 0.61 | OI比 1.23 | ATM IV 41.1% | Skew 1.1pp | Term 0.45 | ExpMove ±1.2%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.45，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-29（1D）±1.2% ｜ 10-30（2D）±1.5% ｜ 11-02（5D）±1.7% ｜ 11-03（6D）±1.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -49,119,040 | GEX Change vs 上次快照 33,610,102 | Flip: Primary Flip: 281.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1277 / LOW 140 / INVALID 1099
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 281.56（全链重定价，覆盖 99%）
Put Wall 260（弱结构｜现价高于该位 8.1%） | Call Wall 290（弱结构｜现价低于该位 3.1%）
最近结构参考: Flip 282（现价低于该位 0.2%）
量化视角： 负 Gamma（4912万，无历史分位）｜负 Gamma 缓解（+3361万）｜现价位于 Flip 下方 0.16%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 278（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 266.0P — Vol 56,679 | 最新价 $1.55 | OI 11044→58092 (ΔOI +47048张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47048张（+426.0% vs前日OI），连续性待观察（方向未知）
10-29 288.0C — Vol 13,827 | 最新价 $0.08 | OI 17→13837 (ΔOI +13820张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13820张（+81294.1% vs前日OI），连续性待观察（方向未知）
11-13 262.0P — Vol 13,666 | 最新价 $0.72 | OI 379→13781 (ΔOI +13402张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13402张（+3536.2% vs前日OI），连续性待观察（方向未知）
11-13 273.0P — Vol 13,631 | 最新价 $2.12 | OI 1024→14378 (ΔOI +13354张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13354张（+1304.1% vs前日OI），连续性待观察（方向未知）
10-29 286.0C — Vol 15,519 | 最新价 $0.20 | OI 3568→13349 (ΔOI +9781张) | ΔOI/Volume 63.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9781张（+274.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 97,405 张（Put 73,804 / Call 23,601），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $10M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 38.1k / P 46.8k，今日成交量: C 79.4k / P 48.3k，平值价格ATM: C $1.15 / P $1.35 ｜ ATM IV 41.1%，预期波动 ±0.9%，Max Pain 278
Top ΔOI: C 284 -5,972 ｜ P 279 +3,417 ｜ P 280 +3,339

📆 Forward Expiration Structure

10-29  C +32.2k / P +8.0k ｜ Activity HIGH ｜ 1D
10-30  C -5.4k / P -6.8k ｜ Activity HIGH ｜ 2D
11-02  C +1.7k / P +1.9k ｜ Activity HIGH ｜ 5D
11-03  C +2.2k / P +3.3k ｜ Activity HIGH ｜ 6D

📆 10-29 Forward Structure
存量OI: C 80.0k / P 26.0k，今日变化ΔOI: C +32.2k / P +8.0k，平值价格ATM: C $1.66 / P $1.82 ｜ ATM IV 26.4%，净 delta 敞口 474k shares
Top ΔOI: C 288 +13,820 ｜ C 286 +9,781 ｜ C 282 +7,674
仓位参考: Max Pain 276 ｜ Call Wall 282（+0.3%，弱）（OI 18.3k） ｜ Put Wall 265（-5.7%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 26.4%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 474,121 股

📆 10-30 Forward Structure
存量OI: C 209.3k / P 487.6k，今日变化ΔOI: C -5.4k / P -6.8k，平值价格ATM: C $2.01 / P $2.16 ｜ ATM IV 23.4%，净 delta 敞口 -505k shares
Top ΔOI: P 259 -10,435 ｜ C 278 -7,924 ｜ C 287 -2,870
仓位参考: Max Pain 278 ｜ Call Wall 278（-1.1%，弱）（OI 20.9k） ｜ Put Wall 260（-7.5%）（OI 86.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 23.4%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 504,540 股

📆 11-02 Forward Structure
存量OI: C 10.3k / P 10.7k，今日变化ΔOI: C +1.7k / P +1.9k，平值价格ATM: C $2.31 / P $2.41 ｜ ATM IV 17.6%，净 delta 敞口 4k shares
Top ΔOI: P 275 +998 ｜ C 284 +439 ｜ C 286 +386
仓位参考: Max Pain 276 ｜ Call Wall 287（+2.1%，弱）（OI 1.3k） ｜ Put Wall 270（-4.0%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 17.6%｜净 delta 敞口 正 4,143 股

📆 11-03 Forward Structure
存量OI: C 7.4k / P 11.5k，今日变化ΔOI: C +2.2k / P +3.3k，平值价格ATM: C $2.58 / P $2.66 ｜ ATM IV 17.8%，净 delta 敞口 -20k shares
Top ΔOI: C 282 +972 ｜ P 279 +830 ｜ P 275 +751
仓位参考: Max Pain 277 ｜ Call Wall 282（+0.3%，弱）（OI 1.2k） ｜ Put Wall 270（-4.0%）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 17.8%｜净 delta 敞口 负 20,360 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/IWM_morning.json