# 期权晨报 2026-09-02（快照 11:19 ET）

📊 市场环境

SPY $765.76 ｜ QQQ $708.91
VIX 15.51 ↓5.1%（5D +0.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-04 160C ΔOI +547（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-11 159P ΔOI -1,596 占该期限总 OI 21.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 163.40 → 今开 164.45（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 168.06 ｜ 低 162.27

Options: P/C成交量 0.58 | OI比 1.76 | ATM IV 35.5% | Skew 6.3pp | Term 0.85 | ExpMove ±2.9%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 6.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.76×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±2.9% ｜ 09-11（9D）±4.2% ｜ 09-18（16D）±5.7% ｜ 09-25（23D）±5.8%
   ⇒ IV–VIX Spread: +20.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,029,985 | GEX Change vs 上次快照 -1,177,543 | Flip: Primary Flip: 165.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 289 / LOW 158 / INVALID 425
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 165.37（全链重定价，覆盖 90%）
Put Wall 155（弱结构｜现价高于该位 4.9%） | Call Wall 170（弱结构｜现价低于该位 4.4%）
最近结构参考: Flip 165（现价低于该位 1.7%）
量化视角： 负 Gamma（1003万，无历史分位）｜负 Gamma 加深（118万）｜现价位于 Flip 下方 1.72%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（Put Wall，弱结构）；上方 163（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 160.0C — Vol 560 | 最新价 $4.25 | OI 114→661 (ΔOI +547张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增547张（+479.8% vs前日OI），连续性待观察（方向未知）
09-18 160.0P — Vol 1,113 | 最新价 $2.51 | OI 9716→10183 (ΔOI +467张) | ΔOI/Volume 42.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增467张（+4.8% vs前日OI），值得跟踪（方向未知）
09-18 170.0C — Vol 2,226 | 最新价 $1.67 | OI 9967→10309 (ΔOI +342张) | ΔOI/Volume 15.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增342张（+3.4% vs前日OI），值得跟踪（方向未知）
09-18 150.0P — Vol 763 | 最新价 $0.55 | OI 15157→15457 (ΔOI +300张) | ΔOI/Volume 39.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增300张（+2.0% vs前日OI），值得跟踪（方向未知）
09-11 156.0P — Vol 283 | 最新价 $0.69 | OI 93→371 (ΔOI +278张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增278张（+298.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,934 张（Put 1,045 / Call 889），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.8k / P +0.5k ｜ Activity HIGH ｜ 2D
09-11  C +63 / P -2.4k ｜ Activity HIGH ｜ 9D
09-18  C +0.4k / P +42 ｜ Activity MEDIUM △ ｜ 16D
09-25  C +47 / P +17 ｜ Activity MEDIUM △ ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 6.0k / P 10.5k
今日变化ΔOI: C +0.8k / P +0.5k
平值价格ATM:  C 2.48 / P 2.23
隐含波动率 ATM IV:  35.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 34k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 160 ｜ +547 ｜ $4.25 ｜ 名义 $232.5k* ｜ -1.6%
P 160 ｜ +233 ｜ $0.87 ｜ 名义 $20.3k* ｜ -1.6%
P 154 ｜ +162 ｜ $0.15 ｜ 名义 $2.4k* ｜ -5.2%
结构参考：160（-1.6%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.5%｜历史 Rank 64%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,954 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 1.5k / P 5.9k
今日变化ΔOI: C +63 / P -2.4k
平值价格ATM:  C 3.10 / P 3.69
隐含波动率 ATM IV:  28.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 48k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 159 ｜ -1,596 ｜ $1.40 ｜ 名义 $-223.4k* ｜ -2.2%
P 152 ｜ -687 ｜ $0.28 ｜ 名义 $-19.2k* ｜ -6.5%
P 153 ｜ -426 ｜ $0.46 ｜ 名义 $-19.6k* ｜ -5.9%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 28.1%｜历史 Rank 64%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 48,392 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 155P -488 ｜ 160P +467

09-25（MEDIUM △）Top ΔOI: 170C +23

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 35.5% vs 09-11 28.1%（差 +7.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=7 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=7）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/XBI_morning.json