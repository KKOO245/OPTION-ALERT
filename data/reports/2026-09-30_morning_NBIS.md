# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $763.55 ｜ QQQ $739.77
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 94.2% vs 10-09 79.4%（差 +14.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 250C ΔOI +769（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 237.35 → 今开 243.96（+2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 250.48 ｜ 低 238.83

Options: P/C成交量 0.31 | OI比 0.68 | ATM IV 94.2% | Skew -0.8pp | Term 0.84 | ExpMove ±6.1%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±6.1% ｜ 10-09（9D）±11.0% ｜ 10-16（16D）±13.6% ｜ 10-23（23D）±16.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,569,309 | GEX Change vs 上次快照 4,763,173 | Flip: Primary Flip: 224.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 557 / LOW 22 / INVALID 119
结构观察区: Primary Flip 224.86（全链重定价，覆盖 100%）
最近结构参考: Flip 225（现价高于该位 7.9%）
量化视角： 正 Gamma（1657万，无历史分位）｜正 Gamma 增强（+476万）｜现价位于 Flip 上方 7.91%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 225（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 280.0C — Vol 2,154 | 最新价 $0.35 | OI 1747→3126 (ΔOI +1379张) | ΔOI/Volume 64.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1379张（+78.9% vs前日OI），连续性待观察（方向未知）
10-02 270.0C — Vol 3,475 | 最新价 $0.65 | OI 2434→3283 (ΔOI +849张) | ΔOI/Volume 24.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增849张（+34.9% vs前日OI），连续性待观察（方向未知）
10-02 250.0C — Vol 5,368 | 最新价 $3.15 | OI 4696→5465 (ΔOI +769张) | ΔOI/Volume 14.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增769张（+16.4% vs前日OI），连续性待观察（方向未知）
10-02 260.0C — Vol 3,844 | 最新价 $1.41 | OI 2558→3181 (ΔOI +623张) | ΔOI/Volume 16.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+24.4% vs前日OI），连续性待观察（方向未知）
10-02 290.0C — Vol 823 | 最新价 $0.18 | OI 1492→2069 (ΔOI +577张) | ΔOI/Volume 70.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增577张（+38.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,197 张（Put 0 / Call 4,197），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +7.1k / P +2.1k ｜ Activity HIGH ｜ 2D
10-09  C +3.0k / P -0.1k ｜ Activity HIGH ｜ 9D
10-16  C +0.2k / P -0.7k ｜ Activity HIGH ｜ 16D
10-23  C +1.8k / P -62 ｜ Activity HIGH ｜ 23D

📆 10-02 Forward Structure
存量OI: C 64.9k / P 44.4k，今日变化ΔOI: C +7.1k / P +2.1k，平值价格ATM: C $7.35 / P $7.40 ｜ ATM IV 94.2%，净 delta 敞口 -6k shares
Top ΔOI: C 270 +849 ｜ C 250 +769
仓位参考: Max Pain 230 ｜ Call Wall 235（-3.2%，弱）（OI 7.2k） ｜ Put Wall 220（-9.3%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 94.2%｜历史 Rank 32%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,968 股

📆 10-09 Forward Structure
存量OI: C 20.6k / P 16.3k，今日变化ΔOI: C +3.0k / P -0.1k，平值价格ATM: C $11.88 / P $14.75 ｜ ATM IV 79.4%，净 delta 敞口 27k shares
Top ΔOI: C 300 +558
仓位参考: Max Pain 225 ｜ Call Wall 240（-1.1%，弱）（OI 2.1k） ｜ Put Wall 225（-7.3%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 79.4%｜历史 Rank 32%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,655 股

📆 10-16 Forward Structure
存量OI: C 66.0k / P 83.7k，今日变化ΔOI: C +0.2k / P -0.7k，平值价格ATM: C $16.65 / P $16.30 ｜ ATM IV 79.2%，净 delta 敞口 -9k shares
Top ΔOI: C 250 -654 ｜ C 232 +324
仓位参考: Max Pain 220 ｜ Call Wall 240（-1.1%，弱）（OI 5.2k） ｜ Put Wall 220（-9.3%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.2%｜历史 Rank 32%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 9,143 股

📆 10-23 Forward Structure
存量OI: C 7.1k / P 9.3k，今日变化ΔOI: C +1.8k / P -62，平值价格ATM: C $18.75 / P $20.80 ｜ ATM IV 79.2%，净 delta 敞口 60k shares
Top ΔOI: C 350 +491 ｜ C 230 +354
仓位参考: Max Pain 225 ｜ Call Wall 230（-5.2%，弱）（OI 0.5k） ｜ Put Wall 220（-9.3%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.2%｜历史 Rank 32%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 59,770 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 94.2% vs 10-09 79.4%（差 +14.8pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/NBIS_morning.json