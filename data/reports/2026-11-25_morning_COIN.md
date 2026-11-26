# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $720.30 ｜ QQQ $633.93
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 102.35 → 今开 98.18（-4.1%） | 较昨收变动（含盘初走势） ｜ 今日高 98.69 ｜ 低 94.88

Options: P/C成交量 0.16 | OI比 0.61 | ATM IV 87.0% | Skew 7.1pp | Term 0.95 | ExpMove ±5.5%（近端） | Rank 75%
量化视角： IV 历史高位（Rank 75%，期权偏贵）｜期限结构正常（Term 0.95）｜保护溢价显著（Skew 7.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.16×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±5.5% ｜ 12-04（9D）±12.8% ｜ 12-11（16D）±22.9% ｜ 12-18（23D）±16.0%
   ⇒ IV–VIX Spread: +55.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,332,346 | GEX Change vs 上次快照 -3,869,942 | Flip: Primary Flip: 103.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 454 / LOW 232 / INVALID 304
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 103.94（全链重定价，覆盖 98%）
最近结构参考: Flip 104（现价低于该位 5.3%）
量化视角： 负 Gamma（1033万，无历史分位）｜负 Gamma 加深（387万）｜现价位于 Flip 下方 5.28%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 109（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 104（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 108.0P — Vol 2,438 | 最新价 $6.58 | OI 123→2452 (ΔOI +2329张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2329张（+1893.5% vs前日OI），连续性待观察（方向未知）
11-27 114.0P — Vol 1,928 | 最新价 $11.05 | OI 2193→3055 (ΔOI +862张) | ΔOI/Volume 44.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增862张（+39.3% vs前日OI），连续性待观察（方向未知）
12-18 75.0P — Vol 2,489 | 最新价 $1.04 | OI 818→1602 (ΔOI +784张) | ΔOI/Volume 31.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增784张（+95.8% vs前日OI），连续性待观察（方向未知）
12-24 105.0P — Vol 568 | 最新价 $10.17 | OI 48→608 (ΔOI +560张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增560张（+1166.7% vs前日OI），连续性待观察（方向未知）
11-27 113.0C — Vol 980 | 最新价 $0.25 | OI 1518→2062 (ΔOI +544张) | ΔOI/Volume 55.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增544张（+35.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,079 张（Put 4,535 / Call 544），跨 3 个期限｜有实质成本保护 4 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +1.8k / P +3.2k ｜ Activity HIGH ｜ 2D
12-04  C +1.9k / P +0.1k ｜ Activity HIGH ｜ 9D
12-11  C +0.6k / P -0.1k ｜ Activity MEDIUM △ ｜ 16D
12-18  C +1.1k / P -1.9k ｜ Activity HIGH ｜ 23D

📆 11-27 Forward Structure
存量OI: C 64.8k / P 39.6k，今日变化ΔOI: C +1.8k / P +3.2k，平值价格ATM: C $2.83 / P $2.56 ｜ ATM IV 87.0%，净 delta 敞口 -163k shares
Top ΔOI: P 108 +2,329 ｜ P 114 +862
仓位参考: Max Pain 109 ｜ Put Wall 100（+1.6%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 87.0%｜历史 Rank 75%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 162,994 股

📆 12-04 Forward Structure
存量OI: C 15.0k / P 18.9k，今日变化ΔOI: C +1.9k / P +0.1k，平值价格ATM: C $5.70 / P $6.85 ｜ ATM IV 85.9%，净 delta 敞口 50k shares
Top ΔOI: C 107 +213
仓位参考: Max Pain 122 ｜ Put Wall 97（-1.5%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 85.9%｜历史 Rank 75%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 49,819 股

12-11（MEDIUM △）Top ΔOI: 106C +128
12-11（MEDIUM △）仓位参考: Max Pain 120 ｜ Put Wall 100（+1.6%，弱）（OI 0.7k）

📆 12-18 Forward Structure
存量OI: C 145.3k / P 53.7k，今日变化ΔOI: C +1.1k / P -1.9k，平值价格ATM: C $7.84 / P $7.95 ｜ ATM IV 84.5%，净 delta 敞口 292k shares
Top ΔOI: P 160 -2,229 ｜ P 75 +784
仓位参考: Max Pain 130 ｜ Put Wall 100（+1.6%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 84.5%｜历史 Rank 75%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 291,639 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/COIN_morning.json