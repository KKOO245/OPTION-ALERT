# 期权晨报 2026-09-04（快照 10:52 ET）

📊 市场环境

SPY $771.00 ｜ QQQ $717.82
VIX 14.12 ↓1.4%（5D -2.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-11 52P ΔOI +137（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 53.78 → 今开 56.57（+5.2%） | 较昨收变动（含盘初走势） ｜ 今日高 58.52 ｜ 低 54.19

Options: P/C成交量 0.25 | OI比 0.74 | ATM IV 103.8% | Skew -3.4pp | Term 0.61 | ExpMove ±6.9%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.25×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±6.9% ｜ 09-18（14D）±7.6% ｜ 09-25（21D）±17.1% ｜ 10-02（28D）±16.2%
   ⇒ IV–VIX Spread: +89.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -28,929 | GEX Change vs 上次快照 2,564,600 | Flip: Primary Flip: 54.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 280 / LOW 86 / INVALID 128
结构观察区: Primary Flip 54.37（全链重定价，覆盖 97%）
Put Wall 55（弱结构｜现价低于该位 1.2%）
最近结构参考: Flip 54（现价低于该位 0.0%）
量化视角： 负 Gamma（3万，无历史分位）｜负 Gamma 缓解（+256万）｜现价位于 Flip 下方 0.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall，弱结构）；上方 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 65.0C — Vol 1,057 | 最新价 $0.08 | OI 452→1483 (ΔOI +1031张) | ΔOI/Volume 97.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1031张（+228.1% vs前日OI），连续性待观察（方向未知）
09-18 55.0C — Vol 388 | 最新价 $1.97 | OI 3214→3455 (ΔOI +241张) | ΔOI/Volume 62.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增241张（+7.5% vs前日OI），连续性待观察（方向未知）
09-04 55.0C — Vol 618 | 最新价 $0.35 | OI 1038→1276 (ΔOI +238张) | ΔOI/Volume 38.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增238张（+22.9% vs前日OI），连续性待观察（方向未知）
09-18 60.0C — Vol 401 | 最新价 $0.79 | OI 6140→6366 (ΔOI +226张) | ΔOI/Volume 56.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增226张（+3.7% vs前日OI），值得跟踪（方向未知）
09-04 54.0C — Vol 650 | 最新价 $0.70 | OI 290→497 (ΔOI +207张) | ΔOI/Volume 31.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增207张（+71.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,943 张（Put 0 / Call 1,943），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +1.8k / P +0.6k ｜ Activity HIGH ｜ 7D
09-18  C +0.5k / P -75 ｜ Activity HIGH ｜ 14D
09-25  C +15 / P +73 ｜ Activity LOW ｜ 21D
10-02  C +0.1k / P +0.3k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 6.2k / P 4.5k
今日变化ΔOI: C +1.8k / P +0.6k
平值价格ATM:  C 2.34 / P 1.41
隐含波动率 ATM IV:  58.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 25k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 54 ｜ +145 ｜ $1.41 ｜ 名义 $20.4k* ｜ -0.6%
P 52 ｜ +137 ｜ $0.69 ｜ 名义 $9.5k* ｜ -4.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：54（-0.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 58.4%｜历史 Rank 93%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 24,664 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 47.8k / P 44.2k
今日变化ΔOI: C +0.5k / P -75
平值价格ATM:  C 2.99 / P 1.15
隐含波动率 ATM IV:  60.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 39k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 55 ｜ +241 ｜ $2.67 ｜ 名义 $64.3k* ｜ +1.2%
P 80 ｜ -101 ｜ $25.29 ｜ 名义 $-255.4k* ｜ +47.2%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：55（+1.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜ATM IV 60.9%｜历史 Rank 93%（近端代理）｜净 delta 敞口 正 39,425 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 1.9k / P 2.7k
今日变化ΔOI: C +0.1k / P +0.3k
平值价格ATM:  C 5.65 / P 3.15
隐含波动率 ATM IV:  63.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 53 ｜ +121 ｜ $2.81 ｜ 名义 $34.0k* ｜ -2.5%
C 59 ｜ +23 ｜ $2.50 ｜ 名义 $5.8k* ｜ +8.6%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：59（+8.6%） / 53（-2.5%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 63.3%｜历史 Rank 93%（近端代理）｜净 delta 敞口 负 1,960 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/MP_morning.json