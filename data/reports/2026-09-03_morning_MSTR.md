# 期权晨报 2026-09-03（快照 10:16 ET）

📊 市场环境

SPY $769.39 ｜ QQQ $712.31
VIX 15.00 ↓1.3%（5D -1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 94.9% vs 09-11 71.5%（差 +23.4pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +7.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 123.19 → 今开 128.04（+3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 134.73 ｜ 低 127.59

Options: P/C成交量 0.47 | OI比 0.74 | ATM IV 94.9% | Skew -8.3pp | Term 0.75 | ExpMove ±4.7%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±4.7% ｜ 09-11（8D）±8.6% ｜ 09-18（15D）±11.7% ｜ 09-25（22D）±14.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 97,240,029 | GEX Change vs 上次快照 67,817,401 | Flip: Primary Flip: 119.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 836 / LOW 219 / INVALID 277
结构观察区: Primary Flip 119.68（全链重定价，覆盖 99%）
最近结构参考: Flip 120（现价高于该位 10.3%）
量化视角： 正 Gamma（9724万，无历史分位）｜正 Gamma 增强（+6782万）｜现价位于 Flip 上方 10.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 120（全链重定价，覆盖 99%）。
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
09-18  C +1.6k / P +0.9k ｜ Activity HIGH ｜ 15D
09-25  C +0.5k / P +1.7k ｜ Activity HIGH ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 239.3k / P 177.6k
今日变化ΔOI: C -21.1k / P -0.4k
平值价格ATM:  C 3.30 / P 2.89
隐含波动率 ATM IV:  94.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 158k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 146 ｜ -14,575 ｜ $0.25 ｜ 名义 $-364.4k* ｜ +10.6%
C 140 ｜ -11,638 ｜ $0.84 ｜ 名义 $-977.6k* ｜ +6.0%
C 147 ｜ -2,721 ｜ $0.20 ｜ 名义 $-54.4k* ｜ +11.3%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 94.9%｜历史 Rank 72%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 157,511 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 45.6k / P 76.8k
今日变化ΔOI: C +6.4k / P +2.6k
平值价格ATM:  C 6.10 / P 5.20
隐含波动率 ATM IV:  71.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 323k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 123 ｜ +1,962 ｜ $10.65 ｜ 名义 $2.09M* ｜ -6.9%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：123（-6.9%）附近形成 OI 变化集中（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.5%｜历史 Rank 72%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 323,083 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-18 Forward Structure
存量OI:      C 269.3k / P 187.8k
今日变化ΔOI: C +1.6k / P +0.9k
平值价格ATM:  C 7.65 / P 7.80
隐含波动率 ATM IV:  71.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 65k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 120 ｜ -446 ｜ $2.50 ｜ 名义 $-111.5k* ｜ -9.1%
（已过滤 2 条低相关性彩票：名义 <$50k 且距现价 >10%）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜ATM IV 71.8%｜历史 Rank 72%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 65,070 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-25 Forward Structure
存量OI:      C 17.0k / P 24.9k
今日变化ΔOI: C +0.5k / P +1.7k
平值价格ATM:  C 9.22 / P 9.35
隐含波动率 ATM IV:  71.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 13k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 71.4%｜历史 Rank 72%（近端代理）｜净 delta 敞口 正 12,984 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 94.9% vs 09-11 71.5%（差 +23.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/MSTR_morning.json