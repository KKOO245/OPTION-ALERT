# 期权晨报 2026-09-14（快照 10:20 ET）

📊 市场环境

SPY $760.44 ｜ QQQ $706.08
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
🟡 **单日价格波动**: -4.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-18 225P ΔOI +1,032（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 224.55 → 今开 204.98（-8.7%） | 较昨收变动（含盘初走势） ｜ 今日高 218.86 ｜ 低 203.87

Options: P/C成交量 0.71 | OI比 1.28 | ATM IV 90.8% | Skew 2.4pp | Term 0.91 | ExpMove ±7.8%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.28×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±7.8% ｜ 09-25（11D）±11.9% ｜ 10-02（18D）±14.1% ｜ 10-09（25D）±17.1%
   ⇒ IV–VIX Spread: +73.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,964,432 | GEX Change vs 上次快照 -3,616,695 | Flip: Primary Flip: 229.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 531 / LOW 63 / INVALID 172
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 229.60（全链重定价，覆盖 100%）
Put Wall 210（弱结构｜现价高于该位 2.2%）
最近结构参考: Put Wall 210（现价高于该位 2.2%）
量化视角： 负 Gamma（696万，无历史分位）｜负 Gamma 加深（362万）｜现价位于 Flip 下方 6.53%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 210（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 230（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 240.0C — Vol 4,051 | 最新价 $3.75 | OI 4947→6572 (ΔOI +1625张) | ΔOI/Volume 40.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1625张（+32.9% vs前日OI），连续性待观察（方向未知）
09-18 250.0C — Vol 5,692 | 最新价 $2.05 | OI 8091→9210 (ΔOI +1119张) | ΔOI/Volume 19.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1119张（+13.8% vs前日OI），连续性待观察（方向未知）
09-18 225.0P — Vol 1,653 | 最新价 $9.22 | OI 1265→2297 (ΔOI +1032张) | ΔOI/Volume 62.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1032张（+81.6% vs前日OI），连续性待观察（方向未知）
09-18 205.0C — Vol 889 | 最新价 $21.95 | OI 272→1150 (ΔOI +878张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增878张（+322.8% vs前日OI），连续性待观察（方向未知）
09-18 230.0C — Vol 2,345 | 最新价 $6.70 | OI 4767→5488 (ΔOI +721张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增721张（+15.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,375 张（Put 1,032 / Call 4,343），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +7.5k / P +7.1k ｜ Activity HIGH ｜ 4D
09-25  C +0.7k / P +1.2k ｜ Activity HIGH ｜ 11D
10-02  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 18D
10-09  C +90 / P +0.7k ｜ Activity MEDIUM △ ｜ 25D

📆 09-18 Forward Structure
存量OI: C 137.5k / P 175.4k，今日变化ΔOI: C +7.5k / P +7.1k，平值价格ATM: C $8.21 / P $8.51 ｜ ATM IV 90.8%，净 delta 敞口 -119k shares
Top ΔOI: C 240 +1,625 ｜ C 250 +1,119 ｜ P 225 +1,032
仓位参考: Max Pain 220
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 90.8%｜历史 Rank 24%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 119,375 股

📆 09-25 Forward Structure
存量OI: C 13.7k / P 17.3k，今日变化ΔOI: C +0.7k / P +1.2k，平值价格ATM: C $12.90 / P $12.58 ｜ ATM IV 82.8%，净 delta 敞口 -12k shares
仓位参考: Max Pain 222
量化解读： 存量 Put 重｜ATM IV 82.8%｜历史 Rank 24%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,583 股

📆 10-02 Forward Structure
存量OI: C 7.3k / P 9.6k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $15.10 / P $15.24 ｜ ATM IV 82.0%，净 delta 敞口 -9k shares
Top ΔOI: P 215 +91
仓位参考: Max Pain 220
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 82.0%｜历史 Rank 24%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,231 股

10-09（MEDIUM △）仓位参考: Max Pain 230

📅 事件差分（观察，非因果）: 09-18（4D）ATM IV 90.8% vs 09-25 82.8%（差 +8.0pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=16 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=16）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/NBIS_morning.json