# 期权晨报 2026-09-04（快照 10:52 ET）

📊 市场环境

SPY $769.49 ｜ QQQ $718.96
VIX 14.12 ↓1.4%（5D -2.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -2.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.65 → 今开 17.75（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 18.01 ｜ 低 17.20

Options: P/C成交量 0.34 | OI比 0.59 | ATM IV 100.2% | Skew -26.2pp | Term 0.72 | ExpMove ±9.0%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜Put 保护异常便宜（Skew -26.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±9.0% ｜ 09-18（14D）±12.3% ｜ 09-25（21D）±16.6% ｜ 10-02（28D）±22.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 345,420 | GEX Change vs 上次快照 -289,901 | Flip: Primary Flip: 16.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 155 / LOW 88 / INVALID 223
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.80（全链重定价，覆盖 83%）
Put Wall 16（弱结构｜现价高于该位 7.6%）
最近结构参考: Flip 17（现价高于该位 2.4%）
量化视角： 正 Gamma（35万，无历史分位）｜正 Gamma 减弱（29万）｜现价位于 Flip 上方 2.43%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 18.5C — Vol 145 | 最新价 $0.10 | OI 164→287 (ΔOI +123张) | ΔOI/Volume 84.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增123张（+75.0% vs前日OI），连续性待观察（方向未知）
10-02 18.5P — Vol 85 | 最新价 $1.95 | OI 15→100 (ΔOI +85张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增85张（+566.7% vs前日OI），连续性待观察（方向未知）
09-18 20.0C — Vol 64 | 最新价 $0.30 | OI 556→617 (ΔOI +61张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增61张（+11.0% vs前日OI），连续性待观察（方向未知）
09-11 16.0P — Vol 60 | 最新价 $0.13 | OI 401→460 (ΔOI +59张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增59张（+14.7% vs前日OI），连续性待观察（方向未知）
10-02 19.0P — Vol 57 | 最新价 $2.20 | OI 8→65 (ΔOI +57张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增57张（+712.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 385 张（Put 201 / Call 184），跨 4 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-11  C +92 / P +0.2k ｜ Activity HIGH ｜ 7D
09-18  C +54 / P +17 ｜ Activity LOW ｜ 14D
09-25  C +17 / P +11 ｜ Activity LOW ｜ 21D
10-02  C +10 / P +0.2k ｜ Activity MEDIUM △ ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 2.7k / P 2.2k
今日变化ΔOI: C +92 / P +0.2k
平值价格ATM:  C 1.10 / P 0.45
隐含波动率 ATM IV:  64.4%
净 delta 敞口变化 ΔOI Δ Exposure*: -7k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +59 ｜ $0.15 ｜ 名义 $885* ｜ -7.0%
P 17 ｜ +53 ｜ $0.60 ｜ 名义 $3.2k* ｜ +1.7%
P 16 ｜ +41 ｜ $0.23 ｜ 名义 $943* ｜ -4.1%
结构参考：17（+1.7%） / 16（-7.0%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.4%｜历史 Rank 33%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 6,523 股（方向不可观测）——方向不可观测，观察点，非方向信号

10-02（MEDIUM △）Top ΔOI: 18P +85

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/NNE_morning.json