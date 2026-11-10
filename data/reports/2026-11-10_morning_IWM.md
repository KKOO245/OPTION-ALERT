# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $750.86 ｜ QQQ $674.76
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-11 290C ΔOI +17,351（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-11 290C ΔOI +17,351 占该期限总 OI 16.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 282.51 → 今开 279.79（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 281.33 ｜ 低 279.25

Options: P/C成交量 1.24 | OI比 1.00 | ATM IV 28.8% | Skew 2.6pp | Term 0.69 | ExpMove ±1.1%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜当日成交偏 Put（P/C量 1.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-11（1D）±1.1% ｜ 11-12（2D）±1.3% ｜ 11-13（3D）±1.6% ｜ 11-16（6D）±2.0%
   ⇒ IV–VIX Spread: +9.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -438,766,491 | GEX Change vs 上次快照 -201,192,583 | Flip: Primary Flip: 284.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1434 / LOW 183 / INVALID 1051
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.06（全链重定价，覆盖 99%）
Put Wall 270（弱结构｜现价高于该位 4.0%） | Call Wall 290（弱结构｜现价低于该位 3.1%）
最近结构参考: Flip 284（现价低于该位 1.1%）
量化视角： 负 Gamma（4.39亿，无历史分位）｜负 Gamma 加深（2.01亿）｜现价位于 Flip 下方 1.11%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 280（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 275.0P — Vol 30,654 | 最新价 $2.94 | OI 1381→31839 (ΔOI +30458张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30458张（+2205.5% vs前日OI），连续性待观察（方向未知）
11-20 270.0P — Vol 55,253 | 最新价 $0.91 | OI 135579→162586 (ΔOI +27007张) | ΔOI/Volume 48.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27007张（+19.9% vs前日OI），连续性待观察（方向未知）
11-20 266.0P — Vol 79,289 | 最新价 $0.60 | OI 66659→84560 (ΔOI +17901张) | ΔOI/Volume 22.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17901张（+26.9% vs前日OI），连续性待观察（方向未知）
11-11 290.0C — Vol 18,922 | 最新价 $0.10 | OI 687→18038 (ΔOI +17351张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17351张（+2525.6% vs前日OI），连续性待观察（方向未知）
11-11 289.0C — Vol 14,266 | 最新价 $0.14 | OI 417→13624 (ΔOI +13207张) | ΔOI/Volume 92.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13207张（+3167.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 105,924 张（Put 75,366 / Call 30,558），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 54.4k / P 54.2k，今日成交量: C 77.1k / P 95.5k，平值价格ATM: C $0.85 / P $0.89 ｜ ATM IV 28.8%，预期波动 ±0.6%，Max Pain 280
Top ΔOI: P 275 +5,416 ｜ C 286 +4,781 ｜ C 283 -2,556

📆 Forward Expiration Structure

11-11  C +61.0k / P +7.2k ｜ Activity HIGH ｜ 1D
11-12  C +3.5k / P +4.1k ｜ Activity HIGH ｜ 2D
11-13  C +12.8k / P +13.7k ｜ Activity MEDIUM △ ｜ 3D
11-16  C +3.5k / P +2.8k ｜ Activity HIGH ｜ 6D

📆 11-11 Forward Structure
存量OI: C 74.9k / P 31.8k，今日变化ΔOI: C +61.0k / P +7.2k，平值价格ATM: C $1.49 / P $1.58 ｜ ATM IV 22.9%，净 delta 敞口 149k shares
Top ΔOI: C 290 +17,351 ｜ C 289 +13,207 ｜ C 287 +7,613
仓位参考: Max Pain 280 ｜ Call Wall 290（+3.2%，弱）（OI 18.0k） ｜ Put Wall 280（-0.3%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 22.9%｜历史 Rank 64%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 149,139 股

📆 11-12 Forward Structure
存量OI: C 22.6k / P 15.4k，今日变化ΔOI: C +3.5k / P +4.1k，平值价格ATM: C $1.96 / P $1.81 ｜ ATM IV 21.9%，净 delta 敞口 -6k shares
Top ΔOI: C 290 +1,576 ｜ P 265 +1,247 ｜ P 263 +782
仓位参考: Max Pain 278 ｜ Call Wall 285（+1.5%）（OI 4.6k） ｜ Put Wall 265（-5.7%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 21.9%｜历史 Rank 64%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,163 股

11-13（MEDIUM △）Top ΔOI: 277P +9,406 ｜ 268P +4,181
11-13（MEDIUM △）仓位参考: Max Pain 278 ｜ Call Wall 302（+7.5%，弱）（OI 13.7k） ｜ Put Wall 272（-3.2%，弱）（OI 12.7k）

📆 11-16 Forward Structure
存量OI: C 8.3k / P 15.1k，今日变化ΔOI: C +3.5k / P +2.8k，平值价格ATM: C $2.85 / P $2.71 ｜ ATM IV 18.4%，净 delta 敞口 -14k shares
Top ΔOI: C 287 +1,022 ｜ P 265 -757 ｜ P 279 +480
仓位参考: Max Pain 280 ｜ Call Wall 287（+2.2%，弱）（OI 1.3k） ｜ Put Wall 270（-3.9%）（OI 3.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 18.4%｜历史 Rank 64%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 负 14,253 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=93 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=93）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/IWM_morning.json