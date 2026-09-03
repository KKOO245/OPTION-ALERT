# 期权晨报 2026-09-03（快照 10:16 ET）

📊 市场环境

SPY $768.34 ｜ QQQ $712.44
VIX 15.00 ↓1.3%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 82.0% vs 09-11 65.1%（差 +16.8pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-11 1500P ΔOI +124（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,553.40 → 今开 1,543.75（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 1552.56 ｜ 低 1511.00

Options: P/C成交量 0.72 | OI比 1.22 | ATM IV 82.0% | Skew -1.6pp | Term 0.85 | ExpMove ±3.7%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.22×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±3.7% ｜ 09-11（8D）±8.0% ｜ 09-18（15D）±10.9% ｜ 09-25（22D）±12.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,534,339 | GEX Change vs 上次快照 313,568 | Flip: Primary Flip: 1525.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1890 / LOW 605 / INVALID 1027
结构观察区: Primary Flip 1525.36（全链重定价，覆盖 100%）
最近结构参考: Flip 1525（现价高于该位 1.4%）
量化视角： 正 Gamma（353万，无历史分位）｜正 Gamma 增强（+31万）｜现价位于 Flip 上方 1.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 1525（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 1650.0C — Vol 571 | 最新价 $3.35 | OI 1125→1650 (ΔOI +525张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增525张（+46.7% vs前日OI），连续性待观察（方向未知）
09-18 1750.0C — Vol 19 | 最新价 $22.25 | OI 536→937 (ΔOI +401张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增401张（+74.8% vs前日OI），值得跟踪（方向未知）
09-04 920.0P — Vol 348（Yahoo补） | 最新价 $0.05 | OI 106→430 (ΔOI +324张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增324张（+305.7% vs前日OI），连续性待观察（方向未知）
09-11 1000.0P — Vol 20 | 最新价 $0.10 | OI 445→762 (ΔOI +317张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增317张（+71.2% vs前日OI），值得跟踪（方向未知）
09-04 1550.0C — Vol 1,204 | 最新价 $22.00 | OI 982→1292 (ΔOI +310张) | ΔOI/Volume 25.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增310张（+31.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,877 张（Put 641 / Call 1,236），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C +3.7k / P +2.4k ｜ Activity HIGH ｜ 1D
09-11  C +1.3k / P +1.7k ｜ Activity HIGH ｜ 8D
09-18  C +1.1k / P +0.5k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 49.4k / P 60.3k
今日变化ΔOI: C +3.7k / P +2.4k
平值价格ATM:  C 23.82 / P 33.00
隐含波动率 ATM IV:  82.0%
净 delta 敞口变化 ΔOI Δ Exposure*: -15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1650 ｜ +525 ｜ $3.35 ｜ 名义 $175.9k* ｜ +6.7%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：1650（+6.7%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 82.0%｜历史 Rank 33%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 14,939 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 10.6k / P 14.5k
今日变化ΔOI: C +1.3k / P +1.7k
平值价格ATM:  C 63.80 / P 59.62
隐含波动率 ATM IV:  65.1%
净 delta 敞口变化 ΔOI Δ Exposure*: 4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1375 ｜ +188 ｜ $8.88 ｜ 名义 $166.9k* ｜ -11.1%
P 1500 ｜ +124 ｜ $43.24 ｜ 名义 $536.2k* ｜ -3.0%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：1375（-11.1%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 65.1%｜历史 Rank 33%（近端代理）｜净 delta 敞口 正 3,509 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 1750C +401 ｜ 1550C +108

09-25（MEDIUM △）Top ΔOI: 1600C +98 ｜ 1400P +97

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 82.0% vs 09-11 65.1%（差 +16.8pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/SNDK_morning.json