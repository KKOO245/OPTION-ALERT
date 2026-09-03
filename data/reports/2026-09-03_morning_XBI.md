# 期权晨报 2026-09-03（快照 12:15 ET）

📊 市场环境

SPY $772.61 ｜ QQQ $717.67
VIX 14.69 ↓3.4%（5D +1.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 09-04 ATM IV 39.0% vs 09-11 27.3%（差 +11.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 164P ΔOI +1,874（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-11 154P ΔOI +1,186 占该期限总 OI 11.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 165.37 → 今开 165.22（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 165.95 ｜ 低 162.85

Options: P/C成交量 3.14 | OI比 1.90 | ATM IV 39.0% | Skew 5.9pp | Term 0.77 | ExpMove ±1.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价中性（Skew 5.9pp）｜当日成交偏 Put（P/C量 3.14）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.14×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.90×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±1.8% ｜ 09-11（8D）±3.4% ｜ 09-18（15D）±4.8% ｜ 09-25（22D）±7.9%
   ⇒ IV–VIX Spread: +24.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -15,091,414 | GEX Change vs 上次快照 -13,768,854 | Flip: Primary Flip: 167.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 351 / LOW 132 / INVALID 397
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 167.18（全链重定价，覆盖 96%）
Put Wall 158（弱结构｜现价高于该位 4.0%） | Call Wall 170（弱结构｜现价低于该位 3.3%）
最近结构参考: Flip 167（现价低于该位 1.7%）
量化视角： 负 Gamma（1509万，无历史分位）｜负 Gamma 加深（1377万）｜现价位于 Flip 下方 1.70%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 158（Put Wall，弱结构）；上方 164（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 158.0P — Vol 16,595 | 最新价 $1.50 | OI 1560→17010 (ΔOI +15450张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15450张（+990.4% vs前日OI），连续性待观察（方向未知）
09-04 164.0P — Vol 2,032 | 最新价 $1.04 | OI 491→2365 (ΔOI +1874张) | ΔOI/Volume 92.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1874张（+381.7% vs前日OI），连续性待观察（方向未知）
09-11 154.0P — Vol 1,574 | 最新价 $0.23 | OI 372→1558 (ΔOI +1186张) | ΔOI/Volume 75.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1186张（+318.8% vs前日OI），连续性待观察（方向未知）
09-11 162.0P — Vol 1,104 | 最新价 $1.77 | OI 11→1002 (ΔOI +991张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增991张（+9009.1% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 1,080 | 最新价 $1.98 | OI 10183→10671 (ΔOI +488张) | ΔOI/Volume 45.2% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增488张（+4.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,989 张（Put 19,989 / Call 0），跨 3 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.7k / P +2.2k ｜ Activity HIGH ｜ 1D
09-11  C +0.6k / P +2.3k ｜ Activity HIGH ｜ 8D
09-18  C -11 / P +13.3k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +15 / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 6.7k / P 12.7k
今日变化ΔOI: C +0.7k / P +2.2k
平值价格ATM:  C 1.12 / P 1.76
隐含波动率 ATM IV:  39.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -89k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 164 ｜ +1,874 ｜ $1.76 ｜ 名义 $329.8k* ｜ -0.2%
P 163 ｜ -497 ｜ $0.60 ｜ 名义 $-29.8k* ｜ -0.8%
P 162 ｜ +384 ｜ $0.38 ｜ 名义 $14.6k* ｜ -1.4%
结构参考：164（-0.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 39.0%｜历史 Rank 80%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 89,092 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 2.1k / P 8.2k
今日变化ΔOI: C +0.6k / P +2.3k
平值价格ATM:  C 2.75 / P 2.75
隐含波动率 ATM IV:  27.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -27k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 154 ｜ +1,186 ｜ $0.28 ｜ 名义 $33.2k* ｜ -6.3%
P 162 ｜ +991 ｜ $2.00 ｜ 名义 $198.2k* ｜ -1.4%
C 174 ｜ +208 ｜ $0.38 ｜ 名义 $7.9k* ｜ +5.9%
结构参考：174（+5.9%） / 154（-6.3%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 27.3%｜历史 Rank 80%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 26,513 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 158P +15,450 ｜ 155P -1,520

09-25（MEDIUM △）Top ΔOI: 157P +56 ｜ 161P +38

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 39.0% vs 09-11 27.3%（差 +11.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=10 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=10）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/XBI_morning.json