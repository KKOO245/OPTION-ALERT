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

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 150P ΔOI +559（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 156.41 → 今开 144.82（-7.4%） | 较昨收变动（含盘初走势） ｜ 今日高 144.85 ｜ 低 137.72

Options: P/C成交量 0.49 | OI比 0.62 | ATM IV 126.2% | Skew 16.8pp | Term 0.91 | ExpMove ±7.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 16.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±7.8% ｜ 12-04（9D）±17.6% ｜ 12-11（16D）±22.6% ｜ 12-18（23D）±22.6%
   ⇒ IV–VIX Spread: +94.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,530,333 | GEX Change vs 上次快照 -201,585 | Flip: Primary Flip: 163.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 563 / LOW 130 / INVALID 269
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.71（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价低于该位 4.2%）
最近结构参考: Put Wall 150（现价低于该位 4.2%）
量化视角： 负 Gamma（753万，无历史分位）｜负 Gamma 加深（20万）｜现价位于 Flip 下方 12.22%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall，弱结构） / 162（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 150.0C — Vol 1,694 | 最新价 $21.05 | OI 625→1685 (ΔOI +1060张) | ΔOI/Volume 62.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1060张（+169.6% vs前日OI），连续性待观察（方向未知）
11-27 185.0C — Vol 2,133 | 最新价 $0.35 | OI 1757→2642 (ΔOI +885张) | ΔOI/Volume 41.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增885张（+50.4% vs前日OI），连续性待观察（方向未知）
11-27 175.0C — Vol 3,421 | 最新价 $1.14 | OI 873→1698 (ΔOI +825张) | ΔOI/Volume 24.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增825张（+94.5% vs前日OI），连续性待观察（方向未知）
11-27 124.0P — Vol 799 | 最新价 $0.32 | OI 101→847 (ΔOI +746张) | ΔOI/Volume 93.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增746张（+738.6% vs前日OI），连续性待观察（方向未知）
12-18 147.0P — Vol 722 | 最新价 $13.55 | OI 9→711 (ΔOI +702张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增702张（+7800.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,218 张（Put 1,448 / Call 2,770），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +4.3k / P +1.1k ｜ Activity HIGH ｜ 2D
12-04  C +1.8k / P +1.0k ｜ Activity HIGH ｜ 9D
12-11  C +0.7k / P +66 ｜ Activity MEDIUM △ ｜ 16D
12-18  C +1.5k / P +2.5k ｜ Activity HIGH ｜ 23D

📆 11-27 Forward Structure
存量OI: C 51.9k / P 32.0k，今日变化ΔOI: C +4.3k / P +1.1k，平值价格ATM: C $5.50 / P $5.72 ｜ ATM IV 126.2%，净 delta 敞口 199k shares
Top ΔOI: P 124 +746
仓位参考: Max Pain 162 ｜ Call Wall 150（+4.4%，弱）（OI 2.3k） ｜ Put Wall 155（+7.9%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 126.2%｜历史 Rank 80%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 199,096 股

📆 12-04 Forward Structure
存量OI: C 14.3k / P 16.3k，今日变化ΔOI: C +1.8k / P +1.0k，平值价格ATM: C $11.44 / P $13.78 ｜ ATM IV 128.8%，净 delta 敞口 4k shares
Top ΔOI: P 150 +559 ｜ C 170 +406
仓位参考: Max Pain 185 ｜ Put Wall 140（-2.6%）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 128.8%｜历史 Rank 80%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,639 股

12-11（MEDIUM △）Top ΔOI: 170C +101 ｜ 155C +92
12-11（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 155（+7.9%，弱）（OI 0.2k） ｜ Put Wall 150（+4.4%，弱）（OI 0.4k）

📆 12-18 Forward Structure
存量OI: C 64.9k / P 77.5k，今日变化ΔOI: C +1.5k / P +2.5k，平值价格ATM: C $15.25 / P $17.20 ｜ ATM IV 119.1%，净 delta 敞口 4k shares
Top ΔOI: C 150 +1,060 ｜ P 147 +702 ｜ P 90 +330
仓位参考: Max Pain 200 ｜ Call Wall 150（+4.4%，弱）（OI 1.7k） ｜ Put Wall 150（+4.4%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜ATM IV 119.1%｜历史 Rank 80%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 3,933 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/BE_morning.json