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
🟡 **近现价集中开仓**: 11-06 151P ΔOI -76（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 150.35 → 收盘 154.84（+3.0%） ｜ 今日高 154.92 ｜ 低 149.37 ｜ 昨收 150.47 → 收盘 154.84（+2.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 8.35 | OI比 5.43 | ATM IV 38.4% | Skew 4.9pp | Term 0.88 | ExpMove ±2.8%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 4.9pp）｜当日成交偏 Put（P/C量 8.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 8.35×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 5.43×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±2.8% ｜ 11-06（10D）±4.5% ｜ 11-13（17D）±6.4% ｜ 11-20（24D）±7.0%
   ⇒ IV–VIX Spread: +20.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,267,823 | GEX Change vs 上次快照 14,663,566 | Flip: Primary Flip: 158.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 321 / LOW 84 / INVALID 365
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 158.44（全链重定价，覆盖 96%）
最近结构参考: Flip 158（现价低于该位 2.3%）
量化视角： 负 Gamma（1027万，无历史分位）｜负 Gamma 缓解（+1466万）｜现价位于 Flip 下方 2.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 142.0C — Vol 1,520（Yahoo补） | 最新价 $8.00 | OI 0→1520 (ΔOI +1520张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1520张（前日OI缺失），连续性待观察（方向未知）
11-06 135.0P — Vol 1 | 最新价 $0.34 | OI 51→551 (ΔOI +500张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增500张（+980.4% vs前日OI），连续性待观察（方向未知）
11-06 145.0P — Vol 208 | 最新价 $1.70 | OI 143→637 (ΔOI +494张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增494张（+345.4% vs前日OI），值得跟踪（方向未知）
11-13 160.0C — Vol 3 | 最新价 $1.45 | OI 45→406 (ΔOI +361张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增361张（+802.2% vs前日OI），值得跟踪（方向未知）
10-30 154.0C — Vol 61 | 最新价 $1.02 | OI 94→438 (ΔOI +344张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增344张（+366.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,219 张（Put 994 / Call 2,225），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.3k / P -0.3k ｜ Activity MEDIUM △ ｜ 3D
11-06  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 10D
11-13  C -2 / P +64 ｜ Activity MEDIUM △ ｜ 17D
11-20  C +0.1k / P +3.4k ｜ Activity HIGH ｜ 24D

📆 10-30 Forward Structure
存量OI: C 10.0k / P 54.4k，今日变化ΔOI: C +0.3k / P -0.3k，平值价格ATM: C $1.90 / P $2.41 ｜ ATM IV 38.4%，净 delta 敞口 17k shares
Top ΔOI: P 142 -493 ｜ P 150 -206 ｜ P 144 +177
仓位参考: Max Pain 150 ｜ Call Wall 155（+0.1%，弱）（OI 2.1k） ｜ Put Wall 150（-3.1%，弱）（OI 9.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.4%｜历史 Rank 78%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,668 股

📆 11-06 Forward Structure
存量OI: C 1.6k / P 3.6k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $3.33 / P $3.69 ｜ ATM IV 34.0%，净 delta 敞口 5k shares
Top ΔOI: P 145 +198 ｜ P 147 +122 ｜ P 151 -76
仓位参考: Max Pain 152 ｜ Call Wall 154（-0.5%，弱）（OI 0.2k） ｜ Put Wall 145（-6.4%）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 34.0%｜历史 Rank 78%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 4,532 股

11-13（MEDIUM △）Top ΔOI: 141P +49 ｜ 145P -4
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 160（+3.3%）（OI 0.4k） ｜ Put Wall 153（-1.2%，弱）（OI 0.4k）

📆 11-20 Forward Structure
存量OI: C 19.8k / P 37.5k，今日变化ΔOI: C +0.1k / P +3.4k，平值价格ATM: C $5.00 / P $5.86 ｜ ATM IV 35.5%，净 delta 敞口 -49k shares
Top ΔOI: P 145 +1,873 ｜ P 133 +1,378 ｜ P 159 +110
仓位参考: Max Pain 154 ｜ Call Wall 160（+3.3%，弱）（OI 1.9k） ｜ Put Wall 145（-6.4%，弱）（OI 9.3k）
量化解读： 存量 Put 重｜ATM IV 35.5%｜历史 Rank 78%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 48,971 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/XBI_evening.json