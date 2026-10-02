# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
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
🟡 **近现价集中开仓**: 10-02 16C ΔOI +48（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.85 → 今开 15.87（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 15.98 ｜ 低 15.62

Options: P/C成交量 0.15 | OI比 0.40 | ATM IV 81.0% | Skew -15.7pp | Term 0.96 | ExpMove ±5.4%（近端） | Rank 9%
量化视角： IV 历史低位（Rank 9%，期权偏便宜）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -15.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.15×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±5.4% ｜ 10-09（8D）±9.0% ｜ 10-16（15D）±13.3% ｜ 10-23（22D）±16.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 297,489 | GEX Change vs 上次快照 76,035 | Flip: Primary Flip: 15.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 185 / LOW 97 / INVALID 154
结构观察区: Primary Flip 15.65（全链重定价，覆盖 92%）
Put Wall 15（现价高于该位 5.6%）
最近结构参考: Flip 16（现价高于该位 1.2%）
量化视角： 正 Gamma（30万，无历史分位）｜正 Gamma 增强（+8万）｜现价位于 Flip 上方 1.16%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 17.0C — Vol 200 | 最新价 $0.10 | OI 447→637 (ΔOI +190张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增190张（+42.5% vs前日OI），连续性待观察（方向未知）
10-16 15.0P — Vol 50 | 最新价 $0.55 | OI 796→846 (ΔOI +50张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增50张（+6.3% vs前日OI），连续性待观察（方向未知）
10-16 15.5P — Vol 50 | 最新价 $0.76 | OI 2→52 (ΔOI +50张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增50张（+2500.0% vs前日OI），连续性待观察（方向未知）
10-02 16.5C — Vol 82 | 最新价 $0.05 | OI 167→215 (ΔOI +48张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增48张（+28.7% vs前日OI），连续性待观察（方向未知）
10-09 17.5C — Vol 42 | 最新价 $0.25 | OI 61→102 (ΔOI +41张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增41张（+67.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 379 张（Put 100 / Call 279），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.3k / P -19 ｜ Activity MEDIUM △ ｜ 1D
10-09  C +0.1k / P +34 ｜ Activity MEDIUM △ ｜ 8D
10-16  C +26 / P -0.1k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +1 / P +13 ｜ Activity MEDIUM △ ｜ 22D

📆 10-02 Forward Structure
存量OI: C 5.8k / P 2.3k，今日变化ΔOI: C +0.3k / P -19，平值价格ATM: C $0.30 / P $0.55 ｜ ATM IV 81.0%，净 delta 敞口 8k shares
Top ΔOI: C 17 +190 ｜ C 16 +48
仓位参考: Max Pain 17 ｜ Call Wall 17（+7.4%，弱）（OI 0.6k） ｜ Put Wall 15.5（-2.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 81.0%｜历史 Rank 9%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,142 股

10-09（MEDIUM △）Top ΔOI: 15P +24
10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（-5.3%）（OI 0.4k）

10-16（MEDIUM △）Top ΔOI: 23P -202 ｜ 15P +50
10-16（MEDIUM △）仓位参考: Max Pain 19 ｜ Put Wall 15（-5.3%，弱）（OI 0.8k）

10-23（MEDIUM △）Top ΔOI: 15P +3
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（+1.0%）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 81.0% vs 10-09 72.3%（差 +8.7pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/NNE_morning.json