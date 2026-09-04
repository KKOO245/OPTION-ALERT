# 期权晚报 2026-09-04（快照 16:40 ET）

📊 市场环境

SPY $770.19 ｜ QQQ $718.96
VIX 14.53 ↑1.5%（5D +0.7%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: +4.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 220C ΔOI +3,074（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 209.89 → 收盘 226.39（+7.9%） ｜ 今日高 226.58 ｜ 低 209.40
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-11，窗口结束前不做对错判定）

Options: P/C成交量 0.41 | OI比 0.83 | ATM IV 168.9% | Skew -1.3pp | Term 0.49 | ExpMove ±8.7%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.49，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-11（7D）±8.7% ｜ 09-18（14D）±14.2% ｜ 09-25（21D）±15.9% ｜ 10-02（28D）±17.9%
   ⇒ IV–VIX Spread: +154.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,491,268 | GEX Change vs 上次快照 358,727 | Flip: Primary Flip: 211.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 470 / LOW 71 / INVALID 263
结构观察区: Primary Flip 211.08（全链重定价，覆盖 90%）
最近结构参考: Flip 211（现价高于该位 7.3%）
量化视角： 正 Gamma（749万，无历史分位）｜正 Gamma 增强（+36万）｜现价位于 Flip 上方 7.25%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 211（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 220.0C — Vol 3,306 | 最新价 $13.10 | OI 1167→4241 (ΔOI +3074张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3074张（+263.4% vs前日OI），连续性待观察（方向未知）
09-11 220.0P — Vol 2,389 | 最新价 $6.55 | OI 302→2268 (ΔOI +1966张) | ΔOI/Volume 82.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1966张（+651.0% vs前日OI），连续性待观察（方向未知）
09-11 230.0C — Vol 5,772 | 最新价 $8.40 | OI 823→2296 (ΔOI +1473张) | ΔOI/Volume 25.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1473张（+179.0% vs前日OI），连续性待观察（方向未知）
09-11 210.0P — Vol 1,565 | 最新价 $3.26 | OI 1057→2163 (ΔOI +1106张) | ΔOI/Volume 70.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1106张（+104.6% vs前日OI），连续性待观察（方向未知）
09-11 270.0C — Vol 3,693 | 最新价 $0.95 | OI 2230→3251 (ΔOI +1021张) | ΔOI/Volume 27.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1021张（+45.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,640 张（Put 3,072 / Call 5,568），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +8.3k / P +5.9k ｜ Activity HIGH ｜ 7D
09-18  C +0.8k / P +0.6k ｜ Activity MEDIUM △ ｜ 14D
09-25  C +1.1k / P +64 ｜ Activity HIGH ｜ 21D
10-02  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 32.4k / P 26.8k
今日变化ΔOI: C +8.3k / P +5.9k
平值价格ATM:  C 9.41 / P 10.30
隐含波动率 ATM IV:  78.0%
净 delta 敞口变化 ΔOI Δ Exposure*: 268k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 220 ｜ +3,074 ｜ $13.10 ｜ 名义 $4.03M* ｜ -2.8%
P 220 ｜ +1,966 ｜ $6.55 ｜ 名义 $1.29M* ｜ -2.8%
C 230 ｜ +1,473 ｜ $8.40 ｜ 名义 $1.24M* ｜ +1.6%
结构参考：230（+1.6%） / 220（-2.8%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 78.0%｜历史 Rank 97%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 267,666 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 280C +575 ｜ 230C +190

📆 09-25 Forward Structure
存量OI:      C 8.8k / P 13.5k
今日变化ΔOI: C +1.1k / P +64
平值价格ATM:  C 18.00 / P 18.03
隐含波动率 ATM IV:  81.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 25k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 300 ｜ +631 ｜ $2.45 ｜ 名义 $154.6k* ｜ +32.5%
C 215 ｜ +59 ｜ $23.70 ｜ 名义 $139.8k* ｜ -5.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：300（+32.5%） / 215（-5.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 81.1%｜历史 Rank 97%（近端代理）｜净 delta 敞口 正 25,272 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 10-02 Forward Structure
存量OI:      C 4.5k / P 7.5k
今日变化ΔOI: C +0.5k / P +0.2k
平值价格ATM:  C 21.02 / P 19.50
隐含波动率 ATM IV:  82.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 18k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 300 ｜ +195 ｜ $4.00 ｜ 名义 $78.0k* ｜ +32.5%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：300（+32.5%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 82.1%｜历史 Rank 97%（近端代理）｜净 delta 敞口 正 17,660 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/NBIS_evening.json