# 期权晨报 2026-09-03（快照 11:17 ET）

📊 市场环境

SPY $769.44 ｜ QQQ $716.10
VIX 14.85 ↓2.3%（5D -2.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 97.7% vs 09-11 73.9%（差 +23.8pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +12.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 140C ΔOI -11,638（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 123.19 → 今开 128.04（+3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 139.05 ｜ 低 127.59

Options: P/C成交量 0.44 | OI比 0.74 | ATM IV 97.7% | Skew -8.6pp | Term 0.77 | ExpMove ±4.5%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±4.5% ｜ 09-11（8D）±9.0% ｜ 09-18（15D）±12.3% ｜ 09-25（22D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 120,688,882 | GEX Change vs 上次快照 91,266,255 | Flip: Primary Flip: 118.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 952 / LOW 120 / INVALID 260
结构观察区: Primary Flip 118.98（全链重定价，覆盖 100%）
最近结构参考: Flip 119（现价高于该位 16.7%）
量化视角： 正 Gamma（1.21亿，无历史分位）｜正 Gamma 增强（+9127万）｜现价位于 Flip 上方 16.67%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 119（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 150.0C — Vol 3,626 | 最新价 $0.11 | OI 6749→9056 (ΔOI +2307张) | ΔOI/Volume 63.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2307张（+34.2% vs前日OI），连续性待观察（方向未知）
09-11 123.0C — Vol 48 | 最新价 $10.65 | OI 128→2090 (ΔOI +1962张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1962张（+1532.8% vs前日OI），连续性待观察（方向未知）
09-04 125.0C — Vol 1,174 | 最新价 $8.00 | OI 2272→3727 (ΔOI +1455张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1455张（+64.0% vs前日OI），连续性待观察（方向未知）
09-04 130.0C — Vol 4,890 | 最新价 $4.40 | OI 11841→13204 (ΔOI +1363张) | ΔOI/Volume 27.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1363张（+11.5% vs前日OI），连续性待观察（方向未知）
09-04 126.0C — Vol 2,162 | 最新价 $7.00 | OI 1565→2810 (ΔOI +1245张) | ΔOI/Volume 57.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1245张（+79.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,332 张（Put 0 / Call 8,332），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-04  C -21.1k / P -0.4k ｜ Activity HIGH ｜ 1D
09-11  C +6.4k / P +2.6k ｜ Activity HIGH ｜ 8D
09-18  C +1.6k / P +0.9k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.5k / P +1.7k ｜ Activity HIGH ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 239.3k / P 177.6k
今日变化ΔOI: C -21.1k / P -0.4k
平值价格ATM:  C 2.97 / P 3.30
隐含波动率 ATM IV:  97.7%
净 delta 敞口变化 ΔOI Δ Exposure*: -301k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 146 ｜ -14,575 ｜ $0.87 ｜ 名义 $-1.27M* ｜ +5.2%
C 140 ｜ -11,638 ｜ $2.57 ｜ 名义 $-2.99M* ｜ +0.9%
C 147 ｜ -2,721 ｜ $0.87 ｜ 名义 $-236.7k* ｜ +5.9%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 97.7%｜历史 Rank 76%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 300,708 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 45.6k / P 76.8k
今日变化ΔOI: C +6.4k / P +2.6k
平值价格ATM:  C 6.30 / P 6.15
隐含波动率 ATM IV:  73.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 400k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 123 ｜ +1,962 ｜ $15.98 ｜ 名义 $3.14M* ｜ -11.4%
C 170 ｜ +860 ｜ $0.68 ｜ 名义 $58.5k* ｜ +22.5%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：170（+22.5%） / 123（-11.4%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.9%｜历史 Rank 76%（近端代理）｜净 delta 敞口 正 400,378 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 120P -446 ｜ 170C +314

📆 09-25 Forward Structure
存量OI:      C 17.0k / P 24.9k
今日变化ΔOI: C +0.5k / P +1.7k
平值价格ATM:  C 10.18 / P 10.55
隐含波动率 ATM IV:  75.6%
净 delta 敞口变化 ΔOI Δ Exposure*: 22k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 75.6%｜历史 Rank 76%（近端代理）｜净 delta 敞口 正 21,994 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 97.7% vs 09-11 73.9%（差 +23.8pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/MSTR_morning.json