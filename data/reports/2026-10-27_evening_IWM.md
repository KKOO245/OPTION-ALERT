# 期权晚报 2026-10-27（快照 16:40 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $721.25
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-28 283C ΔOI +12,838（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 283C ΔOI +12,838 占该期限总 OI 17.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 277.96 → 收盘 280.18（+0.8%） ｜ 今日高 280.39 ｜ 低 276.89 ｜ 昨收 276.99 → 收盘 280.18（+1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.07 | OI比 0.84 | ATM IV 11.6% | Skew -4.7pp | Term 1.59 | ExpMove ±1.0%（近端） | Rank — (历史不足)
量化视角： 期限结构正常偏陡（Term 1.59）｜Put 保护异常便宜（Skew -4.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-28（1D）±1.0% ｜ 10-29（2D）±1.3% ｜ 10-30（3D）±1.6% ｜ 11-02（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -87,944,626 | GEX Change vs 上次快照 377,502,992 | Flip: Primary Flip: 281.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1216 / LOW 188 / INVALID 1222
结构观察区: Primary Flip 281.11（全链重定价，覆盖 97%）
Put Wall 260（弱结构｜现价高于该位 7.8%） | Call Wall 290（弱结构｜现价低于该位 3.4%）
最近结构参考: Flip 281（现价低于该位 0.3%）
量化视角： 负 Gamma（8794万，无历史分位）｜负 Gamma 缓解（+3.78亿）｜现价位于 Flip 下方 0.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 276（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 261.0P — Vol 483 | 最新价 $1.56 | OI 50763→86449 (ΔOI +35686张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35686张（+70.3% vs前日OI），连续性待观察（方向未知）
11-20 260.0P — Vol 8,215 | 最新价 $1.43 | OI 99553→132495 (ΔOI +32942张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32942张（+33.1% vs前日OI），连续性待观察（方向未知）
11-20 262.0P — Vol 48,406 | 最新价 $1.69 | OI 49982→77607 (ΔOI +27625张) | ΔOI/Volume 57.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27625张（+55.3% vs前日OI），连续性待观察（方向未知）
11-06 262.0P — Vol 89 | 最新价 $0.66 | OI 10824→24206 (ΔOI +13382张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13382张（+123.6% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 109,635 张（Put 109,635 / Call 0），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +27.2k / P +3.3k ｜ Activity HIGH ｜ 1D
10-29  C +1.4k / P +1.0k ｜ Activity HIGH ｜ 2D
10-30  C +3.8k / P -0.4k ｜ Activity MEDIUM △ ｜ 3D
11-02  C +2.1k / P +2.7k ｜ Activity HIGH ｜ 6D

📆 10-28 Forward Structure
存量OI: C 39.8k / P 33.1k，今日变化ΔOI: C +27.2k / P +3.3k，平值价格ATM: C $1.52 / P $1.32 ｜ ATM IV 24.1%，净 delta 敞口 661k shares
Top ΔOI: C 283 +12,838 ｜ C 284 +8,931 ｜ C 280 +1,216
仓位参考: Max Pain 275 ｜ Call Wall 283（+1.0%，弱）（OI 13.6k） ｜ Put Wall 275（-1.8%）（OI 6.3k）
量化解读： 存量 Call 重｜ATM IV 24.1%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 660,780 股

📆 10-29 Forward Structure
存量OI: C 47.8k / P 18.1k，今日变化ΔOI: C +1.4k / P +1.0k，平值价格ATM: C $1.98 / P $1.77 ｜ ATM IV 22.8%，净 delta 敞口 81k shares
Top ΔOI: P 274 -1,689
仓位参考: Max Pain 275 ｜ Call Wall 280（-0.1%，弱）（OI 15.4k） ｜ Put Wall 274（-2.2%）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 22.8%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 81,118 股

10-30（MEDIUM △）Top ΔOI: 270P -3,899 ｜ 265P -2,738
10-30（MEDIUM △）仓位参考: Max Pain 278 ｜ Call Wall 278（-0.8%）（OI 28.8k） ｜ Put Wall 260（-7.2%）（OI 86.2k）

📆 11-02 Forward Structure
存量OI: C 8.6k / P 8.8k，今日变化ΔOI: C +2.1k / P +2.7k，平值价格ATM: C $2.68 / P $2.38 ｜ ATM IV 17.4%，净 delta 敞口 45k shares
Top ΔOI: P 274 +537 ｜ C 282 +390 ｜ C 283 +362
仓位参考: Max Pain 275 ｜ Call Wall 287（+2.4%，弱）（OI 1.0k） ｜ Put Wall 270（-3.6%）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 17.4%｜净 delta 敞口 正 45,103 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/IWM_evening.json