# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $752.25 ｜ QQQ $656.90
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-20 10P ΔOI +30（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 10.95 → 今开 10.48（-4.3%） | 较昨收变动（含盘初走势） ｜ 今日高 10.83 ｜ 低 9.64

Options: P/C成交量 1.04 | OI比 0.44 | ATM IV 105.6% | Skew 24.2pp | Term 0.75 | ExpMove ±14.2%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价显著（Skew 24.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±14.2% ｜ 11-13（8D）±2.6% ｜ 11-20（15D）±60.2% ｜ 11-27（22D）±17.2%
   ⇒ IV–VIX Spread: +84.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 175,209 | GEX Change vs 上次快照 614,838 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 166 / LOW 89 / INVALID 153
结构观察区: NO_CROSS
量化视角： 正 Gamma（18万，无历史分位）｜由负转正（+61万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 12.5C — Vol 4,463 | 最新价 $0.32 | OI 3→4006 (ΔOI +4003张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4003张（+133433.3% vs前日OI），连续性待观察（方向未知）
11-13 11.0P — Vol 175 | 最新价 $0.62 | OI 67→237 (ΔOI +170张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增170张（+253.7% vs前日OI），连续性待观察（方向未知）
11-06 11.5C — Vol 188 | 最新价 $0.13 | OI 286→409 (ΔOI +123张) | ΔOI/Volume 65.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增123张（+43.0% vs前日OI），连续性待观察（方向未知）
11-13 11.5C — Vol 130 | 最新价 $0.35 | OI 19→124 (ΔOI +105张) | ΔOI/Volume 80.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增105张（+552.6% vs前日OI），连续性待观察（方向未知）
11-13 13.5C — Vol 101 | 最新价 $0.05 | OI 121→205 (ΔOI +84张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增84张（+69.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,485 张（Put 170 / Call 4,315），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.2k / P -0.3k ｜ Activity HIGH ｜ 1D
11-13  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 8D
11-20  C +46 / P +5 ｜ Activity MEDIUM △ ｜ 15D
11-27  C +4.0k / P +10 ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 3.6k / P 1.6k，今日变化ΔOI: C +0.2k / P -0.3k，平值价格ATM: C $1.34 / P $0.05 ｜ ATM IV 52.8%，净 delta 敞口 32k shares
仓位参考: Max Pain 12
量化解读： 存量 Call 重｜ATM IV 52.8%｜历史 Rank 51%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 31,508 股

📆 11-13 Forward Structure
存量OI: C 1.4k / P 0.9k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $0.00 / P $0.26 ｜ ATM IV 82.1%，净 delta 敞口 -564 shares
仓位参考: Max Pain 12 ｜ Put Wall 10.5（+7.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 82.1%｜历史 Rank 51%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 564 股

11-20（MEDIUM △）Top ΔOI: 10P +30
11-20（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 9（-8.1%，弱）（OI 0.2k）

📆 11-27 Forward Structure
存量OI: C 4.5k / P 0.7k，今日变化ΔOI: C +4.0k / P +10，平值价格ATM: C $1.34 / P $0.35 ｜ ATM IV 80.8%，净 delta 敞口 114k shares
Top ΔOI: C 12 +4,003 ｜ C 10 +10
仓位参考: Max Pain 12
量化解读： 存量 Call 重｜ATM IV 80.8%｜历史 Rank 51%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 正 113,821 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/NNE_morning.json