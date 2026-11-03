# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $755.34 ｜ QQQ $685.28
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 274P ΔOI +16,541（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 274P ΔOI +16,541 占该期限总 OI 19.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 279.14 → 今开 279.84（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 281.26 ｜ 低 279.34

Options: P/C成交量 0.65 | OI比 0.81 | ATM IV 29.8% | Skew 1.5pp | Term 0.71 | ExpMove ±1.6%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（1D）±1.6% ｜ 11-05（2D）±1.9% ｜ 11-06（3D）±2.3% ｜ 11-09（6D）±2.5%
   ⇒ IV–VIX Spread: +8.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -464,110,950 | GEX Change vs 上次快照 41,858,049 | Flip: Primary Flip: 285.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1318 / LOW 109 / INVALID 935
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 285.50（全链重定价，覆盖 100%）
Put Wall 270（弱结构｜现价高于该位 3.7%） | Call Wall 285（弱结构｜现价低于该位 1.7%）
最近结构参考: Call Wall 285（现价低于该位 1.7%）
量化视角： 负 Gamma（4.64亿，无历史分位）｜负 Gamma 缓解（+4186万）｜现价位于 Flip 下方 1.90%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 280（MaxPain，仅结算参考）；上方 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 285（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 266.0P — Vol 64,042 | 最新价 $1.86 | OI 32396→75041 (ΔOI +42645张) | ΔOI/Volume 66.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增42645张（+131.6% vs前日OI），连续性待观察（方向未知）
11-06 277.0P — Vol 58,151 | 最新价 $2.38 | OI 3685→33035 (ΔOI +29350张) | ΔOI/Volume 50.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29350张（+796.5% vs前日OI），连续性待观察（方向未知）
11-04 274.0P — Vol 17,764 | 最新价 $0.77 | OI 618→17159 (ΔOI +16541张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16541张（+2676.5% vs前日OI），连续性待观察（方向未知）
11-20 267.0P — Vol 76,023 | 最新价 $2.03 | OI 35388→49176 (ΔOI +13788张) | ΔOI/Volume 18.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13788张（+39.0% vs前日OI），连续性待观察（方向未知）
11-03 284.0C — Vol 16,729 | 最新价 $0.22 | OI 2175→11555 (ΔOI +9380张) | ΔOI/Volume 56.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9380张（+431.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 111,704 张（Put 102,324 / Call 9,380），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $18M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 45.5k / P 36.8k，今日成交量: C 80.1k / P 51.7k，平值价格ATM: C $0.89 / P $0.91 ｜ ATM IV 29.8%，预期波动 ±0.6%，Max Pain 280
Top ΔOI: C 284 +9,380 ｜ C 285 +7,199 ｜ P 276 +3,366

📆 Forward Expiration Structure

11-04  C +19.1k / P +18.4k ｜ Activity HIGH ｜ 1D
11-05  C +3.5k / P +1.2k ｜ Activity HIGH ｜ 2D
11-06  C +13.5k / P +20.1k ｜ Activity MEDIUM △ ｜ 3D
11-09  C +8.4k / P +7.9k ｜ Activity HIGH ｜ 6D

📆 11-04 Forward Structure
存量OI: C 40.5k / P 45.8k，今日变化ΔOI: C +19.1k / P +18.4k，平值价格ATM: C $2.22 / P $2.13 ｜ ATM IV 33.0%，净 delta 敞口 -78k shares
Top ΔOI: P 274 +16,541 ｜ C 287 +9,161 ｜ C 288 +4,145
仓位参考: Max Pain 280 ｜ Call Wall 288（+2.8%，弱）（OI 10.3k） ｜ Put Wall 274（-2.2%）（OI 17.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.0%｜历史 Rank 75%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 77,560 股

📆 11-05 Forward Structure
存量OI: C 10.8k / P 18.7k，今日变化ΔOI: C +3.5k / P +1.2k，平值价格ATM: C $2.75 / P $2.52 ｜ ATM IV 30.2%，净 delta 敞口 26k shares
Top ΔOI: C 286 +2,850 ｜ P 268 +240 ｜ P 280 +193
仓位参考: Max Pain 280 ｜ Call Wall 286（+2.1%）（OI 3.0k） ｜ Put Wall 260（-7.2%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 30.2%｜历史 Rank 75%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,356 股

11-06（MEDIUM △）Top ΔOI: 277P +29,350 ｜ 267P -20,907
11-06（MEDIUM △）仓位参考: Max Pain 280 ｜ Call Wall 285（+1.8%，弱）（OI 13.0k） ｜ Put Wall 277（-1.1%，弱）（OI 33.0k）

📆 11-09 Forward Structure
存量OI: C 13.0k / P 17.3k，今日变化ΔOI: C +8.4k / P +7.9k，平值价格ATM: C $3.69 / P $3.43 ｜ ATM IV 24.6%，净 delta 敞口 21k shares
Top ΔOI: C 285 +7,175 ｜ P 275 +2,567 ｜ P 268 +939
仓位参考: Max Pain 280 ｜ Call Wall 285（+1.8%）（OI 7.2k） ｜ Put Wall 275（-1.8%）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.6%｜历史 Rank 75%（近端代理）｜净 delta 敞口 正 20,541 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/IWM_morning.json