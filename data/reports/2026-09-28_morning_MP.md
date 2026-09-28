# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $765.39 ｜ QQQ $736.53
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 48.83 → 今开 47.68（-2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 47.83 ｜ 低 46.95

Options: P/C成交量 0.95 | OI比 0.65 | ATM IV 60.4% | Skew -4.5pp | Term 0.92 | ExpMove ±5.2%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -4.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±5.2% ｜ 10-09（11D）±11.8% ｜ 10-16（18D）±3.9% ｜ 10-23（25D）±13.4%
   ⇒ IV–VIX Spread: +44.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,695,112 | GEX Change vs 上次快照 -1,316,583 | Flip: Primary Flip: 49.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 256 / LOW 45 / INVALID 141
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 49.24（全链重定价，覆盖 96%）
Put Wall 50（弱结构｜现价低于该位 5.4%）
最近结构参考: Flip 49（现价低于该位 3.9%）
量化视角： 负 Gamma（170万，无历史分位）｜负 Gamma 加深（132万）｜现价位于 Flip 下方 3.91%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 53.0C — Vol 298 | 最新价 $0.30 | OI 216→473 (ΔOI +257张) | ΔOI/Volume 86.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增257张（+119.0% vs前日OI），连续性待观察（方向未知）
10-02 48.0P — Vol 738 | 最新价 $0.96 | OI 380→633 (ΔOI +253张) | ΔOI/Volume 34.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增253张（+66.6% vs前日OI），连续性待观察（方向未知）
10-02 51.0C — Vol 296 | 最新价 $0.64 | OI 713→943 (ΔOI +230张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增230张（+32.3% vs前日OI），连续性待观察（方向未知）
10-02 50.0P — Vol 248 | 最新价 $2.14 | OI 1569→1775 (ΔOI +206张) | ΔOI/Volume 83.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增206张（+13.1% vs前日OI），连续性待观察（方向未知）
10-09 45.0P — Vol 219 | 最新价 $0.51 | OI 139→345 (ΔOI +206张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增206张（+148.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,152 张（Put 665 / Call 487），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.0k / P +1.2k ｜ Activity HIGH ｜ 4D
10-09  C +0.2k / P +0.5k ｜ Activity MEDIUM △ ｜ 11D
10-16  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
10-23  C +29 / P +53 ｜ Activity MEDIUM △ ｜ 25D

📆 10-02 Forward Structure
存量OI: C 10.6k / P 6.9k，今日变化ΔOI: C +1.0k / P +1.2k，平值价格ATM: C $1.03 / P $1.42 ｜ ATM IV 60.4%，净 delta 敞口 -44k shares
Top ΔOI: P 48 +253 ｜ C 51 +230
仓位参考: Max Pain 50 ｜ Call Wall 49（+3.6%，弱）（OI 1.1k） ｜ Put Wall 50（+5.7%）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 60.4%｜历史 Rank 37%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 44,004 股

10-09（MEDIUM △）Top ΔOI: 45P +206 ｜ 50C +45
10-09（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 47（-0.7%）（OI 1.1k）

10-16（MEDIUM △）Top ΔOI: 50P +94 ｜ 50C +69
10-16（MEDIUM △）仓位参考: Max Pain 52 ｜ Call Wall 50（+5.7%，弱）（OI 3.1k） ｜ Put Wall 50（+5.7%，弱）（OI 3.4k）

10-23（MEDIUM △）Top ΔOI: 45P +30
10-23（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 45（-4.9%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=29 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=29）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/MP_morning.json