# 期权晨报 2026-09-03（快照 12:15 ET）

📊 市场环境

SPY $773.21 ｜ QQQ $717.23
VIX 14.69 ↓3.4%（5D +1.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 55.4 ｜ 前值 54.1　✅ 今日已公布
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 56 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（1D）ATM IV 95.5% vs 09-11 74.7%（差 +20.8pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +13.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 146C ΔOI -14,575（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 123.19 → 今开 128.04（+3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 140.25 ｜ 低 127.59

Options: P/C成交量 0.55 | OI比 0.74 | ATM IV 95.4% | Skew -7.4pp | Term 0.77 | ExpMove ±4.4%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（1D）±4.4% ｜ 09-11（8D）±8.9% ｜ 09-18（15D）±12.1% ｜ 09-25（22D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 119,365,925 | GEX Change vs 上次快照 89,943,298 | Flip: Primary Flip: 120.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 897 / LOW 125 / INVALID 310
结构观察区: Primary Flip 120.19（全链重定价，覆盖 99%）
最近结构参考: Flip 120（现价高于该位 16.5%）
量化视角： 正 Gamma（1.19亿，无历史分位）｜正 Gamma 增强（+8994万）｜现价位于 Flip 上方 16.50%——观察点，非方向信号
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
09-18  C +1.6k / P +0.9k ｜ Activity MEDIUM △ ｜ 15D
09-25  C +0.5k / P +1.7k ｜ Activity HIGH ｜ 22D

📆 09-04 Forward Structure
存量OI:      C 239.3k / P 177.6k
今日变化ΔOI: C -21.1k / P -0.4k
平值价格ATM:  C 3.15 / P 2.97
隐含波动率 ATM IV:  95.5%
净 delta 敞口变化 ΔOI Δ Exposure*: -437k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 146 ｜ -14,575 ｜ $1.14 ｜ 名义 $-1.66M* ｜ +4.3%
C 140 ｜ -11,638 ｜ $3.15 ｜ 名义 $-3.67M* ｜ -0.0%
C 147 ｜ -2,721 ｜ $0.97 ｜ 名义 $-263.9k* ｜ +5.0%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 95.5%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 436,810 股（方向不可观测）——方向不可观测，观察点，非方向信号

📆 09-11 Forward Structure
存量OI:      C 45.6k / P 76.8k
今日变化ΔOI: C +6.4k / P +2.6k
平值价格ATM:  C 6.30 / P 6.10
隐含波动率 ATM IV:  74.7%
净 delta 敞口变化 ΔOI Δ Exposure*: 414k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 123 ｜ +1,962 ｜ $17.90 ｜ 名义 $3.51M* ｜ -12.2%
C 170 ｜ +860 ｜ $0.75 ｜ 名义 $64.5k* ｜ +21.4%
（已过滤 1 条低相关性彩票：名义 <$50k 且距现价 >10%）
结构参考：170（+21.4%） / 123（-12.2%）形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.7%｜历史 Rank 73%（近端代理）｜净 delta 敞口 正 414,448 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（MEDIUM △）Top ΔOI: 120P -446 ｜ 170C +314

📆 09-25 Forward Structure
存量OI:      C 17.0k / P 24.9k
今日变化ΔOI: C +0.5k / P +1.7k
平值价格ATM:  C 10.45 / P 10.00
隐含波动率 ATM IV:  74.8%
净 delta 敞口变化 ΔOI Δ Exposure*: 24k shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
量化解读： 存量 Put 重｜ATM IV 74.8%｜历史 Rank 73%（近端代理）｜净 delta 敞口 正 24,192 股（方向不可观测）——方向不可观测，观察点，非方向信号

📅 事件差分（观察，非因果）: 09-04（1D）ATM IV 95.5% vs 09-11 74.7%（差 +20.8pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-03/MSTR_morning.json