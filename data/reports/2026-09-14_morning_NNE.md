# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $760.44 ｜ QQQ $706.11
VIX 17.27 ↑9.0%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-25 15P ΔOI +189（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 16.41 → 今开 15.85（-3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 16.24 ｜ 低 15.70

Options: P/C成交量 3.62 | OI比 0.49 | ATM IV 79.9% | Skew -1.5pp | Term 0.98 | ExpMove ±8.3%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.49）+ 当日成交偏 Put（P/C量 3.62）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 3.62×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±8.3% ｜ 09-25（11D）±11.4% ｜ 10-02（18D）±24.5% ｜ 10-09（25D）±25.7%
   ⇒ IV–VIX Spread: +62.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -22,887 | GEX Change vs 上次快照 -318,578 | Flip: Primary Flip: 15.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 190 / LOW 85 / INVALID 175
结构观察区: Primary Flip 15.99（全链重定价，覆盖 99%）
Put Wall 15（弱结构｜现价高于该位 6.3%）
最近结构参考: Flip 16（现价低于该位 0.2%）
量化视角： 负 Gamma（2万，无历史分位）｜由正转负（32万）｜现价位于 Flip 下方 0.23%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 21.0C — Vol 2,532 | 最新价 $0.40 | OI 153→2611 (ΔOI +2458张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2458张（+1606.5% vs前日OI），连续性待观察（方向未知）
10-02 15.0P — Vol 300 | 最新价 $0.47 | OI 43→325 (ΔOI +282张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增282张（+655.8% vs前日OI），连续性待观察（方向未知）
09-25 15.5P — Vol 189 | 最新价 $0.40 | OI 37→226 (ΔOI +189张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增189张（+510.8% vs前日OI），连续性待观察（方向未知）
09-25 17.0P — Vol 189 | 最新价 $0.98 | OI 95→268 (ΔOI +173张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增173张（+182.1% vs前日OI），连续性待观察（方向未知）
10-02 20.0C — Vol 155 | 最新价 $0.25 | OI 77→216 (ΔOI +139张) | ΔOI/Volume 89.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增139张（+180.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,241 张（Put 644 / Call 2,597），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0.2k / P +94 ｜ Activity MEDIUM △ ｜ 4D
09-25  C +77 / P +0.4k ｜ Activity HIGH ｜ 11D
10-02  C +0.1k / P +0.4k ｜ Activity HIGH ｜ 18D
10-09  C +9 / P +7 ｜ Activity MEDIUM △ ｜ 25D

📆 09-18 Forward Structure
存量OI: C 7.9k / P 3.9k，今日变化ΔOI: C +0.2k / P +94，平值价格ATM: C $0.90 / P $0.42 ｜ ATM IV 79.9%，净 delta 敞口 7k shares
Top ΔOI: P 17 +122
仓位参考: Max Pain 19 ｜ Put Wall 16（+0.3%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 79.9%｜历史 Rank 7%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,129 股

📆 09-25 Forward Structure
存量OI: C 4.8k / P 1.5k，今日变化ΔOI: C +77 / P +0.4k，平值价格ATM: C $1.12 / P $0.70 ｜ ATM IV 72.6%，净 delta 敞口 -17k shares
Top ΔOI: P 15 +189 ｜ P 17 +173
仓位参考: Max Pain 18 ｜ Put Wall 17（+6.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.6%｜历史 Rank 7%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 17,294 股

📆 10-02 Forward Structure
存量OI: C 2.7k / P 0.9k，今日变化ΔOI: C +0.1k / P +0.4k，平值价格ATM: C $3.06 / P $0.85 ｜ ATM IV 77.9%，净 delta 敞口 -8k shares
Top ΔOI: P 15 +282
仓位参考: Max Pain 19 ｜ Put Wall 15（-6.0%）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.9%｜历史 Rank 7%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,012 股

10-09（MEDIUM △）Top ΔOI: 15P +7 ｜ 14P +6
10-09（MEDIUM △）仓位参考: Max Pain 19 ｜ Put Wall 16（+0.3%）（OI 66）

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 79.9% vs 09-25 72.6%（差 +7.3pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/NNE_morning.json