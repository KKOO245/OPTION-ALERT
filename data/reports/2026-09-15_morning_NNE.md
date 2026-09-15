# 期权晨报 2026-09-15（快照 10:20 ET）

📊 市场环境

SPY $759.03 ｜ QQQ $706.34
VIX 17.08 ↓0.1%（5D +8.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.6（fear）
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
🟡 **近现价集中开仓**: 09-25 16P ΔOI +78（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.89 → 今开 15.80（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 15.94 ｜ 低 15.66

Options: P/C成交量 0.35 | OI比 0.46 | ATM IV 87.7% | Skew -3.4pp | Term 0.96 | ExpMove ±7.9%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -3.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（3D）±7.9% ｜ 09-25（10D）±11.4% ｜ 10-02（17D）±24.7% ｜ 10-09（24D）±15.9%
   ⇒ IV–VIX Spread: +70.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 379,724 | GEX Change vs 上次快照 22,648 | Flip: Primary Flip: 15.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 197 / LOW 90 / INVALID 163
结构观察区: Primary Flip 15.38（全链重定价，覆盖 99%）
Put Wall 15（弱结构｜现价高于该位 5.5%）
最近结构参考: Flip 15（现价高于该位 2.9%）
量化视角： 正 Gamma（38万，无历史分位）｜正 Gamma 增强（+2万）｜现价位于 Flip 上方 2.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 17.0C — Vol 356 | 最新价 $0.20 | OI 85→369 (ΔOI +284张) | ΔOI/Volume 79.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增284张（+334.1% vs前日OI），连续性待观察（方向未知）
09-25 18.0C — Vol 152 | 最新价 $0.25 | OI 63→197 (ΔOI +134张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增134张（+212.7% vs前日OI），连续性待观察（方向未知）
09-18 18.0C — Vol 173 | 最新价 $0.15 | OI 237→364 (ΔOI +127张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增127张（+53.6% vs前日OI），连续性待观察（方向未知）
09-18 19.0C — Vol 272 | 最新价 $0.10 | OI 1545→1670 (ΔOI +125张) | ΔOI/Volume 46.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增125张（+8.1% vs前日OI），连续性待观察（方向未知）
09-18 15.0P — Vol 134 | 最新价 $0.20 | OI 372→491 (ΔOI +119张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增119张（+32.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 789 张（Put 119 / Call 670），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 3D
09-25  C +0.2k / P +0.2k ｜ Activity HIGH ｜ 10D
10-02  C -24 / P +35 ｜ Activity MEDIUM △ ｜ 17D
10-09  C +29 / P +59 ｜ Activity HIGH ｜ 24D

📆 09-18 Forward Structure
存量OI: C 8.7k / P 4.0k，今日变化ΔOI: C +0.8k / P +0.2k，平值价格ATM: C $0.60 / P $0.65 ｜ ATM IV 87.7%，净 delta 敞口 19k shares
Top ΔOI: C 17 +284
仓位参考: Max Pain 18 ｜ Call Wall 17（+7.5%，弱）（OI 0.4k） ｜ Put Wall 16（+1.1%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 87.7%｜历史 Rank 15%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,558 股

📆 09-25 Forward Structure
存量OI: C 5.1k / P 1.8k，今日变化ΔOI: C +0.2k / P +0.2k，平值价格ATM: C $0.93 / P $0.88 ｜ ATM IV 79.1%，净 delta 敞口 -3k shares
Top ΔOI: P 15 +98 ｜ P 16 +78
仓位参考: Max Pain 18 ｜ Put Wall 15（-5.2%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 79.1%｜历史 Rank 15%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,422 股

10-02（MEDIUM △）Top ΔOI: 15P +7
10-02（MEDIUM △）仓位参考: Max Pain 19 ｜ Put Wall 15（-5.2%）（OI 0.3k）

📆 10-09 Forward Structure
存量OI: C 4.1k / P 0.3k，今日变化ΔOI: C +29 / P +59，平值价格ATM: C $1.25 / P $1.27 ｜ ATM IV 79.0%，净 delta 敞口 -2k shares
Top ΔOI: P 16 +35
仓位参考: Max Pain 19 ｜ Put Wall 16（+1.1%）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.0%｜历史 Rank 15%（近端代理）｜净 delta 敞口 负 2,286 股

📅 事件差分（观察，非因果）: 09-18（3D）ATM IV 87.7% vs 09-25 79.1%（差 +8.7pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/NNE_morning.json