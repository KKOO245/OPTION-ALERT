# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $761.90 ｜ QQQ $707.64
VIX 15.71 ↑5.3%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 7.271 ｜ 前值 7.182　✅ 今日已公布
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 54.6 ｜ 前值 55.6　✅ 今日已公布
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 09-04 ATM IV 71.5% vs 09-11 61.3%（差 +10.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 55C ΔOI +543（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 54.75 → 今开 53.50（-2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 54.48 ｜ 低 52.35

Options: P/C成交量 0.61 | OI比 0.75 | ATM IV 71.5% | Skew -6.3pp | Term 0.91 | ExpMove ±6.2%（近端） | Rank 56%
量化视角： IV 中性（Rank 56%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -6.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（3D）±6.2% ｜ 09-11（10D）±9.3% ｜ 09-18（17D）±12.2% ｜ 09-25（24D）±15.7%
   ⇒ IV–VIX Spread: +55.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,004,428 | GEX Change vs 上次快照 -1,523,618 | Flip: Primary Flip: 55.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 321 / LOW 44 / INVALID 125
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 55.14（全链重定价，覆盖 100%）
Put Wall 55（弱结构｜现价低于该位 2.1%）
最近结构参考: Put Wall 55（现价低于该位 2.1%）
量化视角： 负 Gamma（200万，无历史分位）｜负 Gamma 加深（152万）｜现价位于 Flip 下方 2.37%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 55（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 55.0C — Vol 625 | 最新价 $1.70 | OI 585→1128 (ΔOI +543张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增543张（+92.8% vs前日OI），连续性待观察（方向未知）
09-04 52.0P — Vol 415 | 最新价 $0.51 | OI 553→904 (ΔOI +351张) | ΔOI/Volume 84.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增351张（+63.5% vs前日OI），连续性待观察（方向未知）
09-04 60.0C — Vol 590 | 最新价 $0.27 | OI 2068→2406 (ΔOI +338张) | ΔOI/Volume 57.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增338张（+16.3% vs前日OI），连续性待观察（方向未知）
09-04 50.0P — Vol 493 | 最新价 $0.20 | OI 338→551 (ΔOI +213张) | ΔOI/Volume 43.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增213张（+63.0% vs前日OI），连续性待观察（方向未知）
09-04 54.0P — Vol 243 | 最新价 $1.23 | OI 392→568 (ΔOI +176张) | ΔOI/Volume 72.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增176张（+44.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,621 张（Put 740 / Call 881），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +2.1k / P +1.3k ｜ Activity HIGH ｜ 3D
09-11  C +0.5k / P +0.3k ｜ Activity HIGH ｜ 10D
09-18  C -16 / P +14 ｜ Activity LOW ｜ 17D
09-25  C +25 / P +39 ｜ Activity MEDIUM △ ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 11.7k / P 8.8k
今日变化ΔOI: C +2.1k / P +1.3k
平值价格ATM:  C 2.09 / P 1.23
隐含波动率 ATM IV:  71.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 34k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 55 ｜ +543 ｜ $1.70 ｜ 名义 $92.3k* ｜ +2.2%
P 52 ｜ +351 ｜ $0.51 ｜ 名义 $17.9k* ｜ -3.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：55（+2.2%） / 52（-3.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 71.5%｜历史 Rank 56%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,466 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 3.4k / P 3.6k
今日变化ΔOI: C +0.5k / P +0.3k
平值价格ATM:  C 2.84 / P 2.17
隐含波动率 ATM IV:  61.3%
净 delta 敞口变化 ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 55 ｜ +68 ｜ $2.71 ｜ 名义 $18.4k* ｜ +2.2%
P 50 ｜ +61 ｜ $0.61 ｜ 名义 $3.7k* ｜ -7.1%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：55（+2.2%） / 50（-7.1%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 61.3%｜历史 Rank 56%（近端代理）｜净 delta 敞口 负 2,357 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-25（MEDIUM △）Top ΔOI: 50P +16

📅 事件差分（观察，非因果）: 09-04（3D）ATM IV 71.5% vs 09-11 61.3%（差 +10.2pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=4 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=4）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/MP_morning.json