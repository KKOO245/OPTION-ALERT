# 期权晨报 2026-09-04（快照 10:52 ET）

📊 市场环境

SPY $771.00 ｜ QQQ $717.78
VIX 14.12 ↓1.4%（5D -2.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-11 360P ΔOI +43（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 369.83 → 今开 367.81（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 369.55 ｜ 低 363.75

Options: P/C成交量 0.25 | OI比 0.44 | ATM IV 46.6% | Skew -1.6pp | Term 0.67 | ExpMove ±3.3%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.67，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.25×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±3.3% ｜ 09-18（14D）±5.3% ｜ 09-25（21D）±6.8% ｜ 10-02（28D）±7.4%
   ⇒ IV–VIX Spread: +32.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,464,829 | GEX Change vs 上次快照 -192,088 | Flip: Primary Flip: 371.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 217 / LOW 190 / INVALID 487
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 371.52（全链重定价，覆盖 94%）
Call Wall 400（现价低于该位 8.5%）
最近结构参考: Flip 372（现价低于该位 1.5%）
量化视角： 负 Gamma（146万，无历史分位）｜负 Gamma 加深（19万）｜现价位于 Flip 下方 1.47%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 372（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 375.0C — Vol 238 | 最新价 $1.86 | OI 67→279 (ΔOI +212张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增212张（+316.4% vs前日OI），连续性待观察（方向未知）
09-04 365.0C — Vol 207 | 最新价 $6.35 | OI 10→209 (ΔOI +199张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增199张（+1990.0% vs前日OI），连续性待观察（方向未知）
09-04 370.0C — Vol 216 | 最新价 $3.61 | OI 35→231 (ΔOI +196张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增196张（+560.0% vs前日OI），连续性待观察（方向未知）
09-04 380.0C — Vol 233 | 最新价 $1.42 | OI 235→379 (ΔOI +144张) | ΔOI/Volume 61.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增144张（+61.3% vs前日OI），连续性待观察（方向未知）
09-18 372.5P — Vol 64 | 最新价 $10.30 | OI 30→94 (ΔOI +64张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增64张（+213.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 815 张（Put 64 / Call 751），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +33 / P +0.1k ｜ Activity HIGH ｜ 7D
09-18  C +2 / P +75 ｜ Activity LOW ｜ 14D
09-25  C +19 / P +34 ｜ Activity MEDIUM △ ｜ 21D
10-02  C +12 / P +10 ｜ Activity MEDIUM △ ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 0.8k / P 0.8k
今日变化ΔOI: C +33 / P +0.1k
平值价格ATM:  C 9.70 / P 2.30
隐含波动率 ATM IV:  34.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 360 ｜ +43 ｜ $2.80 ｜ 名义 $12.0k* ｜ -1.7%
P 342 ｜ +30 ｜ $0.90 ｜ 名义 $2.7k* ｜ -6.4%
P 345 ｜ +12 ｜ $0.70 ｜ 名义 $840* ｜ -5.8%
结构参考：360（-1.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.2%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,312 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 355P +10 ｜ 345P +8

10-02（MEDIUM △）Top ΔOI: 330P +3 ｜ 345P +2

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=11 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=11）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/ISRG_morning.json