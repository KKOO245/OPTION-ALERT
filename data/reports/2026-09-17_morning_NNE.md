# 期权晨报 2026-09-17（快照 11:28 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.87 ↓10.4%（5D -11.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 09-18 ATM IV 94.1% vs 09-25 80.9%（差 +13.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.64 → 今开 16.22（+3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 16.65 ｜ 低 16.06

Options: P/C成交量 0.18 | OI比 0.44 | ATM IV 94.1% | Skew 11.2pp | Term 0.85 | ExpMove ±5.4%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 11.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±5.4% ｜ 09-25（8D）±9.8% ｜ 10-02（15D）±16.7% ｜ 10-09（22D）±29.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 708,272 | GEX Change vs 上次快照 1,152,193 | Flip: Primary Flip: 16.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 212 / LOW 98 / INVALID 140
结构观察区: Primary Flip 16.02（全链重定价，覆盖 93%）
Put Wall 15（弱结构｜现价高于该位 9.6%）
最近结构参考: Flip 16（现价高于该位 2.6%）
量化视角： 正 Gamma（71万，无历史分位）｜由负转正（+115万）｜现价位于 Flip 上方 2.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 14.0P — Vol 308 | 最新价 $0.27 | OI 10→315 (ΔOI +305张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增305张（+3050.0% vs前日OI），连续性待观察（方向未知）
09-25 15.0P — Vol 274 | 最新价 $0.50 | OI 271→518 (ΔOI +247张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增247张（+91.1% vs前日OI），连续性待观察（方向未知）
09-18 15.5C — Vol 132 | 最新价 $0.35 | OI 12→130 (ΔOI +118张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增118张（+983.3% vs前日OI），连续性待观察（方向未知）
09-25 14.5P — Vol 120 | 最新价 $0.42 | OI 54→133 (ΔOI +79张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增79张（+146.3% vs前日OI），连续性待观察（方向未知）
09-18 16.5C — Vol 95 | 最新价 $0.11 | OI 122→199 (ΔOI +77张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增77张（+63.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 826 张（Put 631 / Call 195），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.2k / P -80 ｜ Activity MEDIUM △ ｜ 1D
09-25  C +45 / P +0.6k ｜ Activity HIGH ｜ 8D
10-02  C +10 / P +9 ｜ Activity MEDIUM △ ｜ 15D
10-09  C +10 / P +18 ｜ Activity LOW ｜ 22D

📆 09-18 Forward Structure
存量OI: C 9.2k / P 4.0k，今日变化ΔOI: C +0.2k / P -80，平值价格ATM: C $0.32 / P $0.57 ｜ ATM IV 94.1%，净 delta 敞口 27k shares
Top ΔOI: C 15 +118 ｜ C 16 +77
仓位参考: Max Pain 18 ｜ Call Wall 17（+3.4%，弱）（OI 0.5k） ｜ Put Wall 16（-2.7%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 94.1%｜历史 Rank 26%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 27,445 股

📆 09-25 Forward Structure
存量OI: C 5.2k / P 2.3k，今日变化ΔOI: C +45 / P +0.6k，平值价格ATM: C $0.73 / P $0.88 ｜ ATM IV 80.9%，净 delta 敞口 -6k shares
Top ΔOI: P 15 +247
仓位参考: Max Pain 18 ｜ Put Wall 15（-8.8%）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 80.9%｜历史 Rank 26%（近端代理）｜净 delta 敞口 负 5,558 股

10-02（MEDIUM △）Top ΔOI: 15P +10
10-02（MEDIUM △）仓位参考: Max Pain 19 ｜ Put Wall 15（-8.8%）（OI 0.2k）

10-09（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 16（-2.7%）（OI 0.1k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 94.1% vs 09-25 80.9%（差 +13.2pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/NNE_morning.json