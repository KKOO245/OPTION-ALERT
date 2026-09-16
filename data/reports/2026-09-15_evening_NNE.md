# 期权晚报 2026-09-15（快照 18:31 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $nan
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 15.80 → 收盘 15.78（-0.1%） ｜ 今日高 15.97 ｜ 低 15.44 ｜ 昨收 15.89 → 收盘 15.78（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.45 | OI比 0.46 | ATM IV 83.1% | Skew 1.7pp | Term 0.96 | ExpMove ±6.3%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 0.96）｜保护溢价薄（Skew 1.7pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±6.3% ｜ 09-25（10D）±9.2% ｜ 10-02（17D）±11.1% ｜ 10-09（24D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 459,475 | GEX Change vs 上次快照 -88,764 | Flip: Primary Flip: 15.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 190 / LOW 95 / INVALID 165
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 15.11（全链重定价，覆盖 92%）
Put Wall 15（弱结构｜现价高于该位 5.2%）
最近结构参考: Flip 15（现价高于该位 4.4%）
量化视角： 正 Gamma（46万，无历史分位）｜正 Gamma 减弱（9万）｜现价位于 Flip 上方 4.41%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 17.0C — Vol 72 | 最新价 $0.15 | OI 85→369 (ΔOI +284张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增284张（+334.1% vs前日OI），值得跟踪（方向未知）
09-25 18.0C — Vol 14 | 最新价 $0.20 | OI 63→197 (ΔOI +134张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增134张（+212.7% vs前日OI），值得跟踪（方向未知）
09-18 18.0C — Vol 6 | 最新价 $0.06 | OI 237→364 (ΔOI +127张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增127张（+53.6% vs前日OI），值得跟踪（方向未知）
09-18 19.0C — Vol 23 | 最新价 $0.05 | OI 1545→1670 (ΔOI +125张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增125张（+8.1% vs前日OI），值得跟踪（方向未知）
09-18 15.0P — Vol 7 | 最新价 $0.22 | OI 372→491 (ΔOI +119张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增119张（+32.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 789 张（Put 119 / Call 670），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-18 Forward Structure
存量OI: C 8.7k / P 4.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.40 / P $0.59 ｜ ATM IV 83.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 18 ｜ Call Wall 17（+7.7%，弱）（OI 0.4k） ｜ Put Wall 16（+1.4%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 83.1%｜历史 Rank 10%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 15（-4.9%，弱）（OI 0.3k）

10-02（Activity LOW）仓位参考: Max Pain 19 ｜ Put Wall 15（-4.9%）（OI 0.3k）

10-09（Activity LOW）仓位参考: Max Pain 19 ｜ Put Wall 16（+1.4%）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/NNE_evening.json