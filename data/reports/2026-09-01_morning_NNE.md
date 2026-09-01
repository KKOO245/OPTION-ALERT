# 期权晨报 2026-09-01（快照 10:20 ET）

📊 市场环境

SPY $761.99 ｜ QQQ $707.64
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
🟡 **单日价格波动**: -4.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 18P ΔOI +54（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 18.29 → 今开 17.50（-4.3%） | 较昨收变动（含盘初走势） ｜ 今日高 17.80 ｜ 低 17.02

Options: P/C成交量 0.43 | OI比 0.64 | ATM IV 81.1% | Skew 7.6pp | Term 1.05 | ExpMove ±8.1%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常（Term 1.05）｜保护溢价显著（Skew 7.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（3D）±8.1% ｜ 09-11（10D）±10.9% ｜ 09-18（17D）±5.8% ｜ 09-25（24D）±20.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 147,283 | GEX Change vs 上次快照 -715,837 | Flip: Primary Flip: 17.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 234 / LOW 77 / INVALID 155
结构观察区: Primary Flip 17.34（全链重定价，覆盖 96%）
Put Wall 16（弱结构｜现价高于该位 9.3%）
最近结构参考: Flip 17（现价高于该位 0.8%）
量化视角： 正 Gamma（15万，无历史分位）｜正 Gamma 减弱（72万）｜现价位于 Flip 上方 0.80%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 17（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 19.0C — Vol 245 | 最新价 $0.35 | OI 316→542 (ΔOI +226张) | ΔOI/Volume 92.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增226张（+71.5% vs前日OI），连续性待观察（方向未知）
09-04 20.0C — Vol 262 | 最新价 $0.12 | OI 281→506 (ΔOI +225张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增225张（+80.1% vs前日OI），连续性待观察（方向未知）
09-04 19.5C — Vol 257 | 最新价 $0.24 | OI 199→410 (ΔOI +211张) | ΔOI/Volume 82.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增211张（+106.0% vs前日OI），连续性待观察（方向未知）
09-04 17.0P — Vol 174 | 最新价 $0.20 | OI 194→361 (ΔOI +167张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增167张（+86.1% vs前日OI），连续性待观察（方向未知）
09-04 21.0C — Vol 191 | 最新价 $0.06 | OI 482→614 (ΔOI +132张) | ΔOI/Volume 69.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增132张（+27.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 961 张（Put 167 / Call 794），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +0.9k / P +0.3k ｜ Activity HIGH ｜ 3D
09-11  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 10D
09-18  C +79 / P +34 ｜ Activity MEDIUM △ ｜ 17D
09-25  C +0.1k / P +13 ｜ Activity MEDIUM △ ｜ 24D

📆 09-04 Forward Structure
存量OI:      C 3.3k / P 2.1k
今日变化ΔOI: C +0.9k / P +0.3k
平值价格ATM:  C 1.12 / P 0.29
隐含波动率 ATM IV:  81.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 18k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +226 ｜ $0.35 ｜ 名义 $7.9k* ｜ +8.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：19（+8.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 81.1%｜历史 Rank 7%（近端代理）｜净 delta 敞口 正 17,812 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 2.5k / P 1.7k
今日变化ΔOI: C +0.3k / P +0.2k
平值价格ATM:  C 1.25 / P 0.65
隐含波动率 ATM IV:  76.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 463 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +126 ｜ $0.32 ｜ 名义 $4.0k* ｜ -5.6%
P 18 ｜ +54 ｜ $0.81 ｜ 名义 $4.4k* ｜ +3.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：18（+3.0%） / 16（-5.6%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 76.6%｜历史 Rank 7%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 463 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 16P +39

09-25（MEDIUM △）Top ΔOI: 19C +7

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-01/NNE_morning.json