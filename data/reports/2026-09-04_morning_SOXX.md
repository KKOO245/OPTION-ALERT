# 期权晨报 2026-09-04（快照 10:52 ET）

📊 市场环境

SPY $769.55 ｜ QQQ $718.96
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
🟡 **单日价格波动**: +2.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 502.20 → 今开 509.40（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 520.07 ｜ 低 507.25

Options: P/C成交量 0.23 | OI比 0.79 | ATM IV 50.3% | Skew 11.8pp | Term 0.73 | ExpMove ±3.9%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 11.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±3.9% ｜ 09-18（14D）±5.7% ｜ 09-25（21D）±9.4% ｜ 10-02（28D）±9.7%
   ⇒ IV–VIX Spread: +36.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,255,297 | GEX Change vs 上次快照 27,160,817 | Flip: Primary Flip: 516.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 458 / LOW 364 / INVALID 740
结构观察区: Primary Flip 516.09（全链重定价，覆盖 93%）
最近结构参考: Flip 516（现价高于该位 0.2%）
量化视角： 正 Gamma（126万，无历史分位）｜由负转正（+2716万）｜现价位于 Flip 上方 0.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 516（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 550.0C — Vol 1 | 最新价 $2.00 | OI 366→1661 (ΔOI +1295张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1295张（+353.8% vs前日OI），连续性待观察（方向未知）
09-04 520.0C — Vol 762 | 最新价 $0.80 | OI 570→1068 (ΔOI +498张) | ΔOI/Volume 65.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增498张（+87.4% vs前日OI），连续性待观察（方向未知）
09-04 500.0C — Vol 40 | 最新价 $11.10 | OI 286→664 (ΔOI +378张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增378张（+132.2% vs前日OI），值得跟踪（方向未知）
09-04 515.0C — Vol 55 | 最新价 $1.60 | OI 860→1186 (ΔOI +326张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增326张（+37.9% vs前日OI），值得跟踪（方向未知）
09-18 500.0C — Vol 33 | 最新价 $20.40 | OI 895→1137 (ΔOI +242张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增242张（+27.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,739 张（Put 0 / Call 2,739），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +0.3k / P -1.5k ｜ Activity MEDIUM △ ｜ 7D
09-18  C +1.2k / P -1.2k ｜ Activity MEDIUM △ ｜ 14D
09-25  C -9 / P +34 ｜ Activity MEDIUM △ ｜ 21D
10-02  C +97 / P +0.3k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 12.4k / P 14.2k
今日变化ΔOI: C +0.3k / P -1.5k
平值价格ATM:  C 11.20 / P 8.93
隐含波动率 ATM IV:  33.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 111k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 550 ｜ -785 ｜ $33.68 ｜ 名义 $-2.64M* ｜ +6.4%
P 485 ｜ -457 ｜ $1.45 ｜ 名义 $-66.3k* ｜ -6.2%
P 500 ｜ -341 ｜ $3.60 ｜ 名义 $-122.8k* ｜ -3.3%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.9%｜历史 Rank 86%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 110,950 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 550C +1,295 ｜ 485P -571

09-25（MEDIUM △）Top ΔOI: 470P -99 ｜ 490P +67

📆 10-02 Forward Structure
存量OI:      C 5.4k / P 6.6k
今日变化ΔOI: C +97 / P +0.3k
平值价格ATM:  C 30.00 / P 20.25
隐含波动率 ATM IV:  37.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 495 ｜ +80 ｜ $16.20 ｜ 名义 $129.6k* ｜ -4.2%
P 500 ｜ +61 ｜ $13.42 ｜ 名义 $81.9k* ｜ -3.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：495（-4.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 37.0%｜历史 Rank 86%（近端代理）｜净 delta 敞口 负 6,204 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/SOXX_morning.json