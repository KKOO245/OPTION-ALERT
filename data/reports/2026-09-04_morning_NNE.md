# 期权晨报 2026-09-04（快照 10:20 ET）

📊 市场环境

SPY $772.01 ｜ QQQ $719.85
VIX 14.05 ↓1.9%（5D -2.6%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 43.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 162 ｜ 前值 21　✅ 今日已公布
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 4.1 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-11 17P ΔOI +53（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.65 → 今开 17.75（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 18.01 ｜ 低 17.27

Options: P/C成交量 0.37 | OI比 0.59 | ATM IV 93.0% | Skew -4.4pp | Term 0.80 | ExpMove ±7.7%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-11（7D）±7.7% ｜ 09-18（14D）±12.9% ｜ 09-25（21D）±13.3% ｜ 10-02（28D）±16.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 323,651 | GEX Change vs 上次快照 -311,670 | Flip: Primary Flip: 17.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 184 / LOW 97 / INVALID 185
结构观察区: Primary Flip 17.27（全链重定价，覆盖 84%）
Put Wall 16（弱结构｜现价高于该位 9.1%）
最近结构参考: Flip 17（现价高于该位 1.0%）
量化视角： 正 Gamma（32万，无历史分位）｜正 Gamma 减弱（31万）｜现价位于 Flip 上方 1.04%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall，弱结构）；上方 18（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 84%）。
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
09-18  C +54 / P +17 ｜ Activity MEDIUM △ ｜ 14D
09-25  C +17 / P +11 ｜ Activity MEDIUM △ ｜ 21D
10-02  C +10 / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-11 Forward Structure
存量OI:      C 2.7k / P 2.2k
今日变化ΔOI: C +92 / P +0.2k
平值价格ATM:  C 0.75 / P 0.59
隐含波动率 ATM IV:  68.1%
净 delta 敞口变化 ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +59 ｜ $0.13 ｜ 名义 $767* ｜ -8.3%
P 17 ｜ +53 ｜ $0.59 ｜ 名义 $3.1k* ｜ +0.3%
P 16 ｜ +41 ｜ $0.20 ｜ 名义 $820* ｜ -5.4%
结构参考：17（+0.3%） / 16（-8.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 68.1%｜历史 Rank 22%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 4,788 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 16P +5

09-25（MEDIUM △）Top ΔOI: 18C +4

📆 10-02 Forward Structure
存量OI:      C 2.5k / P 0.6k
今日变化ΔOI: C +10 / P +0.2k
平值价格ATM:  C 1.48 / P 1.42
隐含波动率 ATM IV:  74.6%
净 delta 敞口变化 ΔOI Δ Exposure*: -8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ +85 ｜ $1.95 ｜ 名义 $16.6k* ｜ +6.0%
P 19 ｜ +57 ｜ $2.20 ｜ 名义 $12.5k* ｜ +8.9%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：18（+6.0%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.6%｜历史 Rank 22%（近端代理）｜净 delta 敞口 负 7,964 股（方向不可观测）——方向不可观测，观察点，非方向信号

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-04/NNE_morning.json