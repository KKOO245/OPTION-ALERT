# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $701.98 ｜ QQQ $610.48
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.1（extreme fear）
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
🟡 **近现价集中开仓**: 12-02 115P ΔOI +374（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 125.81 → 今开 118.46（-5.8%） | 较昨收变动（含盘初走势） ｜ 今日高 118.77 ｜ 低 113.93

Options: P/C成交量 0.72 | OI比 0.95 | ATM IV 130.2% | Skew 10.0pp | Term 0.59 | ExpMove ±5.1%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价显著（Skew 10.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-27（2D）±5.1% ｜ 11-30（5D）±7.4% ｜ 12-02（7D）±9.2% ｜ 12-04（9D）±11.3%
   ⇒ IV–VIX Spread: +98.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -54,198,890 | GEX Change vs 上次快照 6,668,356 | Flip: Primary Flip: 125.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 836 / LOW 191 / INVALID 611
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 125.72（全链重定价，覆盖 94%）
Put Wall 115（弱结构｜现价高于该位 2.1%）
最近结构参考: Put Wall 115（现价高于该位 2.1%）
量化视角： 负 Gamma（5420万，无历史分位）｜负 Gamma 缓解（+667万）｜现价位于 Flip 下方 6.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 115（Put Wall，弱结构）；上方 130（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 126（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-11 118.0P — Vol 10,903 | 最新价 $4.40 | OI 161→10038 (ΔOI +9877张) | ΔOI/Volume 90.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9877张（+6134.8% vs前日OI），连续性待观察（方向未知）
12-11 110.0P — Vol 11,769 | 最新价 $2.35 | OI 1901→11329 (ΔOI +9428张) | ΔOI/Volume 80.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9428张（+495.9% vs前日OI），连续性待观察（方向未知）
12-11 145.0C — Vol 10,155 | 最新价 $1.34 | OI 1809→10664 (ΔOI +8855张) | ΔOI/Volume 87.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8855张（+489.5% vs前日OI），连续性待观察（方向未知）
12-04 115.0P — Vol 6,886 | 最新价 $2.29 | OI 6381→11649 (ΔOI +5268张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5268张（+82.6% vs前日OI），连续性待观察（方向未知）
11-27 125.0C — Vol 10,154 | 最新价 $3.35 | OI 758→5725 (ΔOI +4967张) | ΔOI/Volume 48.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4967张（+655.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 38,395 张（Put 24,573 / Call 13,822），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $8M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 56.1k / P 53.4k，今日成交量: C 48.7k / P 35.3k，平值价格ATM: C $2.04 / P $1.31 ｜ ATM IV 130.2%，预期波动 ±2.8%，Max Pain 130
Top ΔOI: C 130 +3,177 ｜ P 130 +2,447 ｜ C 126 +2,252

📆 Forward Expiration Structure

11-27  C +13.0k / P +0.2k ｜ Activity HIGH ｜ 2D
11-30  C +6.4k / P +3.5k ｜ Activity HIGH ｜ 5D
12-02  C +4.4k / P +1.6k ｜ Activity HIGH ｜ 7D
12-04  C +10.1k / P +25.2k ｜ Activity HIGH ｜ 9D

📆 11-27 Forward Structure
存量OI: C 216.5k / P 101.0k，今日变化ΔOI: C +13.0k / P +0.2k，平值价格ATM: C $3.45 / P $2.53 ｜ ATM IV 81.3%，净 delta 敞口 505k shares
Top ΔOI: C 125 +4,967
仓位参考: Max Pain 133 ｜ Call Wall 125（+6.4%，弱）（OI 5.7k） ｜ Put Wall 120（+2.2%，弱）（OI 7.8k）
量化解读： 存量 Call 重｜ATM IV 81.3%｜历史 Rank 98%（近端代理）｜IV/RV 1.30×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 504,591 股

📆 11-30 Forward Structure
存量OI: C 26.0k / P 15.9k，今日变化ΔOI: C +6.4k / P +3.5k，平值价格ATM: C $4.77 / P $3.95 ｜ ATM IV 75.4%，净 delta 敞口 -93k shares
Top ΔOI: C 130 +1,524 ｜ C 126 +747
仓位参考: Max Pain 130 ｜ Put Wall 115（-2.1%）（OI 5.2k）
量化解读： 存量 Call 重｜ATM IV 75.4%｜历史 Rank 98%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 92,964 股

📆 12-02 Forward Structure
存量OI: C 10.4k / P 3.6k，今日变化ΔOI: C +4.4k / P +1.6k，平值价格ATM: C $5.80 / P $5.05 ｜ ATM IV 82.4%，净 delta 敞口 -26k shares
Top ΔOI: P 115 +374
仓位参考: Max Pain 130 ｜ Put Wall 115（-2.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 82.4%｜历史 Rank 98%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 负 26,340 股

📆 12-04 Forward Structure
存量OI: C 115.6k / P 91.5k，今日变化ΔOI: C +10.1k / P +25.2k，平值价格ATM: C $7.10 / P $6.15 ｜ ATM IV 86.1%，净 delta 敞口 -597k shares
Top ΔOI: P 115 +5,268 ｜ P 100 +4,670 ｜ P 118 +2,848
仓位参考: Max Pain 137 ｜ Put Wall 115（-2.1%，弱）（OI 11.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 86.1%｜历史 Rank 98%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 596,545 股

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 81.3% vs 11-30 75.4%（差 +5.9pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SPCX_morning.json