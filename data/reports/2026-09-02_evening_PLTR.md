# 期权晚报 2026-09-02（快照 17:13 ET）

📊 市场环境

SPY $765.16 ｜ QQQ $709.24
VIX 15.20 ↓7.0%（5D -1.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **单日价格波动**: -2.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-04 ATM IV 56.9% vs 09-11 46.2%（差 +10.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 175P ΔOI -918（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 176.99 → 收盘 169.46（-4.3%） ｜ 今日高 177.55 ｜ 低 165.71
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-07，窗口结束前不做对错判定）

Options: P/C成交量 0.66 | OI比 0.80 | ATM IV 56.9% | Skew 3.8pp | Term 0.82 | ExpMove ±3.4%（近端） | Rank — (历史不足)
量化视角： 期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（2D）±3.4% ｜ 09-11（9D）±5.8% ｜ 09-18（16D）±7.9% ｜ 09-25（23D）±9.4%
   ⇒ IV–VIX Spread: +41.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,349,088 | GEX Change vs 上次快照 -9,914,440 | Flip: Primary Flip: 171.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 522 / LOW 119 / INVALID 285
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 171.72（全链重定价，覆盖 100%）
最近结构参考: Flip 172（现价低于该位 1.3%）
量化视角： 负 Gamma（935万，无历史分位）｜由正转负（991万）｜现价位于 Flip 下方 1.32%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 172（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 180.0P — Vol 4,102 | 最新价 $11.90 | OI 1373→5169 (ΔOI +3796张) | ΔOI/Volume 92.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3796张（+276.5% vs前日OI），连续性待观察（方向未知）
09-04 185.0C — Vol 10,203 | 最新价 $0.13 | OI 4463→6560 (ΔOI +2097张) | ΔOI/Volume 20.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2097张（+47.0% vs前日OI），连续性待观察（方向未知）
09-04 190.0C — Vol 21,149 | 最新价 $0.07 | OI 19804→21818 (ΔOI +2014张) | ΔOI/Volume 9.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2014张（+10.2% vs前日OI），连续性待观察（方向未知）
09-04 200.0C — Vol 2,938 | 最新价 $0.03 | OI 12917→14538 (ΔOI +1621张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1621张（+12.6% vs前日OI），连续性待观察（方向未知）
09-25 170.0P — Vol 3,620 | 最新价 $7.91 | OI 1876→3496 (ΔOI +1620张) | ΔOI/Volume 44.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1620张（+86.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,148 张（Put 5,416 / Call 5,732），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +7.7k / P +2.2k ｜ Activity MEDIUM △ ｜ 2D
09-11  C +1.8k / P +5.9k ｜ Activity HIGH ｜ 9D
09-18  C -0.8k / P -2.7k ｜ Activity MEDIUM △ ｜ 16D
09-25  C +0.4k / P +1.7k ｜ Activity HIGH ｜ 23D

📆 09-04 Forward Structure
存量OI:      C 152.1k / P 121.1k
今日变化ΔOI: C +7.7k / P +2.2k
平值价格ATM:  C 2.66 / P 3.15
隐含波动率 ATM IV:  56.9%
净 delta 敞口变化 ΔOI Δ Exposure*: -156k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 185 ｜ +2,097 ｜ $0.13 ｜ 名义 $27.3k* ｜ +9.2%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：185（+9.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 56.9%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 155,553 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 35.1k / P 68.6k
今日变化ΔOI: C +1.8k / P +5.9k
平值价格ATM:  C 4.75 / P 5.10
隐含波动率 ATM IV:  46.2%
净 delta 敞口变化 ΔOI Δ Exposure*: -286k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 180 ｜ +3,796 ｜ $11.90 ｜ 名义 $4.52M* ｜ +6.2%
P 175 ｜ -918 ｜ $8.23 ｜ 名义 $-755.5k* ｜ +3.3%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：180（+6.2%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 46.2%｜净 delta 敞口 负 286,201 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 170P -1,988 ｜ 160P -952

📆 09-25 Forward Structure
存量OI:      C 16.6k / P 23.5k
今日变化ΔOI: C +0.4k / P +1.7k
平值价格ATM:  C 7.95 / P 7.91
隐含波动率 ATM IV:  46.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -62k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 170 ｜ +1,620 ｜ $7.91 ｜ 名义 $1.28M* ｜ +0.3%
P 180 ｜ -380 ｜ $14.06 ｜ 名义 $-534.3k* ｜ +6.2%
P 192 ｜ +129 ｜ $24.15 ｜ 名义 $311.5k* ｜ +13.6%
结构参考：170（+0.3%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 46.5%｜净 delta 敞口 负 62,239 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（2D）ATM IV 56.9% vs 09-11 46.2%（差 +10.8pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=7 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=7）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-02/PLTR_evening.json