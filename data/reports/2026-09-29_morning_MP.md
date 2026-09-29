# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.86 ｜ QQQ $738.92
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 45P ΔOI +1,030（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 46.45 → 今开 46.88（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 46.63 ｜ 低 45.01

Options: P/C成交量 0.45 | OI比 0.80 | ATM IV 58.8% | Skew -3.5pp | Term 0.97 | ExpMove ±4.5%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -3.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±4.5% ｜ 10-09（10D）±7.1% ｜ 10-16（17D）±9.1% ｜ 10-23（24D）±11.9%
   ⇒ IV–VIX Spread: +42.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,875,604 | GEX Change vs 上次快照 -1,377,085 | Flip: Primary Flip: 48.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 257 / LOW 58 / INVALID 131
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.04（全链重定价，覆盖 94%）
最近结构参考: Flip 48（现价低于该位 5.9%）
量化视角： 负 Gamma（388万，无历史分位）｜负 Gamma 加深（138万）｜现价位于 Flip 下方 5.95%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 45.0P — Vol 1,244 | 最新价 $0.52 | OI 354→1384 (ΔOI +1030张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1030张（+291.0% vs前日OI），连续性待观察（方向未知）
10-16 49.0C — Vol 1,043 | 最新价 $1.40 | OI 111→1086 (ΔOI +975张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增975张（+878.4% vs前日OI），连续性待观察（方向未知）
10-02 45.5P — Vol 907 | 最新价 $0.58 | OI 93→991 (ΔOI +898张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增898张（+965.6% vs前日OI），连续性待观察（方向未知）
10-02 46.0P — Vol 672 | 最新价 $0.98 | OI 241→618 (ΔOI +377张) | ΔOI/Volume 56.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增377张（+156.4% vs前日OI），连续性待观察（方向未知）
10-16 47.5C — Vol 292 | 最新价 $1.92 | OI 0→285 (ΔOI +285张) | ΔOI/Volume 97.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增285张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,565 张（Put 2,305 / Call 1,260），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +1.0k / P +2.4k ｜ Activity HIGH ｜ 3D
10-09  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 10D
10-16  C +1.2k / P +0.7k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +19 / P +0.1k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 11.6k / P 9.3k，今日变化ΔOI: C +1.0k / P +2.4k，平值价格ATM: C $1.22 / P $0.80 ｜ ATM IV 58.8%，净 delta 敞口 -54k shares
Top ΔOI: P 45 +1,030 ｜ P 45 +898 ｜ P 46 +377
仓位参考: Max Pain 50 ｜ Call Wall 49（+8.4%，弱）（OI 1.3k） ｜ Put Wall 45（-0.4%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.8%｜历史 Rank 34%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 53,609 股

10-09（MEDIUM △）Top ΔOI: 42P +149 ｜ 46P +107
10-09（MEDIUM △）仓位参考: Max Pain 51 ｜ Put Wall 47（+4.0%）（OI 1.1k）

10-16（MEDIUM △）Top ΔOI: 49C +975 ｜ 47C +285
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 49（+8.4%，弱）（OI 1.1k） ｜ Put Wall 45（-0.4%，弱）（OI 3.3k）

10-23（MEDIUM △）Top ΔOI: 46P +30
10-23（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 45（-0.4%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 58.8% vs 10-09 52.6%（差 +6.2pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/MP_morning.json