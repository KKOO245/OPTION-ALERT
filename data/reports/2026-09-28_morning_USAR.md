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
🟡 **近现价集中开仓**: 10-02 15P ΔOI +1,453（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 15.18 → 今开 14.95（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 15.01 ｜ 低 14.78

Options: P/C成交量 0.37 | OI比 0.63 | ATM IV 70.2% | Skew -4.6pp | Term 1.01 | ExpMove ±6.0%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -4.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±6.0% ｜ 10-09（11D）±8.8% ｜ 10-16（18D）±12.6% ｜ 10-23（25D）±17.0%
   ⇒ IV–VIX Spread: +54.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,456,168 | GEX Change vs 上次快照 -1,929,217 | Flip: Primary Flip: 16.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 200 / LOW 59 / INVALID 145
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.04（全链重定价，覆盖 99%）
Put Wall 15（现价低于该位 0.6%）
最近结构参考: Put Wall 15（现价低于该位 0.6%）
量化视角： 负 Gamma（346万，无历史分位）｜负 Gamma 加深（193万）｜现价位于 Flip 下方 7.04%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall） / 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 14.0P — Vol 1,676 | 最新价 $0.62 | OI 345→2010 (ΔOI +1665张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1665张（+482.6% vs前日OI），连续性待观察（方向未知）
10-02 15.5P — Vol 1,646 | 最新价 $0.66 | OI 1215→2668 (ΔOI +1453张) | ΔOI/Volume 88.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1453张（+119.6% vs前日OI），连续性待观察（方向未知）
10-02 15.0P — Vol 815 | 最新价 $0.41 | OI 1006→1694 (ΔOI +688张) | ΔOI/Volume 84.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增688张（+68.4% vs前日OI），连续性待观察（方向未知）
10-16 20.0C — Vol 631 | 最新价 $0.09 | OI 5257→5768 (ΔOI +511张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增511张（+9.7% vs前日OI），连续性待观察（方向未知）
10-09 17.0P — Vol 448 | 最新价 $1.98 | OI 470→876 (ΔOI +406张) | ΔOI/Volume 90.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增406张（+86.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,723 张（Put 4,212 / Call 511），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.2k / P +2.8k ｜ Activity HIGH ｜ 4D
10-09  C +0.1k / P +0.7k ｜ Activity MEDIUM △ ｜ 11D
10-16  C +0.5k / P +0.3k ｜ Activity LOW ｜ 18D
10-23  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 10-02 Forward Structure
存量OI: C 21.3k / P 13.5k，今日变化ΔOI: C +1.2k / P +2.8k，平值价格ATM: C $0.37 / P $0.53 ｜ ATM IV 70.2%，净 delta 敞口 -144k shares
Top ΔOI: P 15 +1,453 ｜ P 15 +688 ｜ P 14 +391
仓位参考: Max Pain 16 ｜ Call Wall 16（+7.3%，弱）（OI 1.1k） ｜ Put Wall 15.5（+4.0%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.2%｜历史 Rank 3%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 143,516 股

10-09（MEDIUM △）Top ΔOI: 17P +406 ｜ 15P +96
10-09（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 16（+7.3%）（OI 1.3k）

10-16（Activity LOW）仓位参考: Max Pain 17 ｜ Put Wall 15（+0.6%）（OI 5.6k）

10-23（MEDIUM △）Top ΔOI: 14P +31
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（+0.6%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=29 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=29）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/USAR_morning.json