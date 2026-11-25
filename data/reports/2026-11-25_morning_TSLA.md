# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $716.47 ｜ QQQ $633.93
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-27 380P ΔOI +1,264（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 352P ΔOI +4,104 占该期限总 OI 26.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 384.68 → 今开 370.23（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 370.23 ｜ 低 357.64

Options: P/C成交量 1.08 | OI比 1.04 | ATM IV 94.6% | Skew 10.7pp | Term 0.73 | ExpMove ±3.8%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 10.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-27（2D）±3.8% ｜ 11-30（5D）±5.4% ｜ 12-02（7D）±6.9% ｜ 12-04（9D）±8.3%
   ⇒ IV–VIX Spread: +63.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,247,582 | GEX Change vs 上次快照 -64,964,646 | Flip: Primary Flip: 364.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1333 / LOW 222 / INVALID 853
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 364.45（全链重定价，覆盖 98%）
最近结构参考: Flip 364（现价低于该位 0.3%）
量化视角： 负 Gamma（325万，无历史分位）｜由正转负（6496万）｜现价位于 Flip 下方 0.25%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 380（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 364（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-25 400.0C — Vol 40,495 | 最新价 $0.56 | OI 3520→7871 (ΔOI +4351张) | ΔOI/Volume 10.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4351张（+123.6% vs前日OI），连续性待观察（方向未知）
12-02 352.5P — Vol 4,519 | 最新价 $2.90 | OI 81→4185 (ΔOI +4104张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4104张（+5066.7% vs前日OI），连续性待观察（方向未知）
12-11 420.0C — Vol 9,022 | 最新价 $5.60 | OI 1453→5156 (ΔOI +3703张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3703张（+254.8% vs前日OI），连续性待观察（方向未知）
11-25 390.0C — Vol 47,880 | 最新价 $2.70 | OI 1498→4786 (ΔOI +3288张) | ΔOI/Volume 6.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3288张（+219.5% vs前日OI），连续性待观察（方向未知）
11-30 420.0C — Vol 7,947 | 最新价 $0.51 | OI 8007→10840 (ΔOI +2833张) | ΔOI/Volume 35.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2833张（+35.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,279 张（Put 4,104 / Call 14,175），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 60.1k / P 62.5k，今日成交量: C 111.2k / P 119.9k，平值价格ATM: C $4.55 / P $2.95 ｜ ATM IV 94.6%，预期波动 ±2.1%，Max Pain 380
Top ΔOI: C 400 +4,351 ｜ C 390 +3,288 ｜ P 360 +2,007

📆 Forward Expiration Structure

11-27  C +7.0k / P +11.1k ｜ Activity HIGH ｜ 2D
11-30  C +7.9k / P +4.5k ｜ Activity HIGH ｜ 5D
12-02  C +2.8k / P +5.0k ｜ Activity HIGH ｜ 7D
12-04  C +4.5k / P +5.5k ｜ Activity HIGH ｜ 9D

📆 11-27 Forward Structure
存量OI: C 150.1k / P 218.2k，今日变化ΔOI: C +7.0k / P +11.1k，平值价格ATM: C $7.62 / P $6.11 ｜ ATM IV 61.9%，净 delta 敞口 -358k shares
Top ΔOI: C 400 +1,859 ｜ P 380 +1,264 ｜ P 360 +1,030
仓位参考: Max Pain 368 ｜ Call Wall 390（+7.3%，弱）（OI 8.3k）
量化解读： 存量 Put 重｜ATM IV 61.9%｜历史 Rank 95%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 负 358,085 股

📆 11-30 Forward Structure
存量OI: C 26.7k / P 14.3k，今日变化ΔOI: C +7.9k / P +4.5k，平值价格ATM: C $10.82 / P $8.85 ｜ ATM IV 54.8%，净 delta 敞口 -123k shares
Top ΔOI: P 370 +902 ｜ C 400 +766
仓位参考: Max Pain 388 ｜ Put Wall 392.5（+8.0%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 54.8%｜历史 Rank 95%（近端代理）｜IV/RV 0.75×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 123,422 股

📆 12-02 Forward Structure
存量OI: C 7.3k / P 8.3k，今日变化ΔOI: C +2.8k / P +5.0k，平值价格ATM: C $13.50 / P $11.56 ｜ ATM IV 61.3%，净 delta 敞口 -140k shares
Top ΔOI: P 352 +4,104 ｜ C 395 +402
仓位参考: Max Pain 372 ｜ Call Wall 372.5（+2.5%，弱）（OI 0.8k） ｜ Put Wall 352.5（-3.0%）（OI 4.2k）
量化解读： 存量两侧均衡｜ATM IV 61.3%｜历史 Rank 95%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 140,095 股

📆 12-04 Forward Structure
存量OI: C 60.0k / P 58.2k，今日变化ΔOI: C +4.5k / P +5.5k，平值价格ATM: C $16.30 / P $13.80 ｜ ATM IV 64.9%，净 delta 敞口 8k shares
Top ΔOI: P 295 +1,400
仓位参考: Max Pain 378 ｜ Call Wall 360（-1.0%，弱）（OI 3.0k） ｜ Put Wall 350（-3.7%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.9%｜历史 Rank 95%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 正 7,820 股

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 61.9% vs 11-30 54.8%（差 +7.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/TSLA_morning.json