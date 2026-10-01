# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $764.48 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 68.0% vs 10-09 53.7%（差 +14.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 47P ΔOI +1,046（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 47.29 → 今开 46.51（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 46.89 ｜ 低 44.80

Options: P/C成交量 0.23 | OI比 0.68 | ATM IV 68.0% | Skew -8.4pp | Term 0.88 | ExpMove ±3.4%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±3.4% ｜ 10-09（8D）±5.0% ｜ 10-16（15D）±10.7% ｜ 10-23（22D）±10.7%
   ⇒ IV–VIX Spread: +50.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,587,970 | GEX Change vs 上次快照 -2,153,610 | Flip: Primary Flip: 46.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 249 / LOW 67 / INVALID 140
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 46.90（全链重定价，覆盖 89%）
Put Wall 45（弱结构｜现价低于该位 0.2%）
最近结构参考: Put Wall 45（现价低于该位 0.2%）
量化视角： 负 Gamma（459万，无历史分位）｜负 Gamma 加深（215万）｜现价位于 Flip 下方 4.26%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 45（Put Wall，弱结构） / 49（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 47（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 47.0P — Vol 1,815 | 最新价 $1.57 | OI 1155→2201 (ΔOI +1046张) | ΔOI/Volume 57.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1046张（+90.6% vs前日OI），连续性待观察（方向未知）
10-16 50.0C — Vol 1,252 | 最新价 $1.32 | OI 3156→4032 (ΔOI +876张) | ΔOI/Volume 70.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增876张（+27.8% vs前日OI），连续性待观察（方向未知）
10-02 50.0C — Vol 1,147 | 最新价 $0.21 | OI 992→1497 (ΔOI +505张) | ΔOI/Volume 44.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增505张（+50.9% vs前日OI），连续性待观察（方向未知）
10-16 47.0C — Vol 512 | 最新价 $2.99 | OI 47→506 (ΔOI +459张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增459张（+976.6% vs前日OI），连续性待观察（方向未知）
10-16 45.0C — Vol 403 | 最新价 $4.10 | OI 348→619 (ΔOI +271张) | ΔOI/Volume 67.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增271张（+77.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,157 张（Put 1,046 / Call 2,111），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.9k / P -0.2k ｜ Activity HIGH ｜ 1D
10-09  C +0.3k / P +1.1k ｜ Activity HIGH ｜ 8D
10-16  C +1.8k / P -0.9k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +0.2k / P -12 ｜ Activity MEDIUM △ ｜ 22D

📆 10-02 Forward Structure
存量OI: C 13.5k / P 9.2k，今日变化ΔOI: C +0.9k / P -0.2k，平值价格ATM: C $0.71 / P $0.80 ｜ ATM IV 68.0%，净 delta 敞口 16k shares
Top ΔOI: C 48 +178 ｜ C 48 +111
仓位参考: Max Pain 49 ｜ Call Wall 49（+9.1%，弱）（OI 1.1k） ｜ Put Wall 45（+0.2%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 68.0%｜历史 Rank 51%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,721 股

📆 10-09 Forward Structure
存量OI: C 6.1k / P 5.6k，今日变化ΔOI: C +0.3k / P +1.1k，平值价格ATM: C $1.58 / P $0.67 ｜ ATM IV 53.7%，净 delta 敞口 -86k shares
Top ΔOI: P 47 +1,046
仓位参考: Max Pain 50 ｜ Put Wall 47（+4.7%）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.7%｜历史 Rank 51%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 负 86,357 股

10-16（MEDIUM △）Top ΔOI: 55P -1,008 ｜ 50C +876
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 49（+9.1%，弱）（OI 1.1k） ｜ Put Wall 45（+0.2%，弱）（OI 3.6k）

10-23（MEDIUM △）仓位参考: Max Pain 51 ｜ Put Wall 45（+0.2%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 68.0% vs 10-09 53.7%（差 +14.3pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=38 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=38）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/MP_morning.json