# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $774.21 ｜ QQQ $747.58
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 242C ΔOI +8,274（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 237.47 → 今开 234.93（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 236.37 ｜ 低 233.71

Options: P/C成交量 0.79 | OI比 1.14 | ATM IV 29.7% | Skew 2.4pp | Term 0.99 | ExpMove ±1.4%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常（Term 0.99）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.14×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±1.4% ｜ 10-12（4D）±2.0% ｜ 10-14（6D）±2.8% ｜ 10-16（8D）±3.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 320,181,888 | GEX Change vs 上次快照 -168,665,891 | Flip: Primary Flip: 226.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 628 / LOW 173 / INVALID 639
结构观察区: Primary Flip 226.98（全链重定价，覆盖 97%）
Put Wall 220（弱结构｜现价高于该位 6.7%） | Call Wall 240（弱结构｜现价低于该位 2.2%）
最近结构参考: Call Wall 240（现价低于该位 2.2%）
量化视角： 正 Gamma（3.20亿，无历史分位）｜正 Gamma 减弱（1.69亿）｜现价位于 Flip 上方 3.42%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 232（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 227（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 242.5C — Vol 33,461 | 最新价 $0.49 | OI 25727→34001 (ΔOI +8274张) | ΔOI/Volume 24.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8274张（+32.2% vs前日OI），连续性待观察（方向未知）
10-16 212.5P — Vol 6,333 | 最新价 $0.20 | OI 2171→7891 (ΔOI +5720张) | ΔOI/Volume 90.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5720张（+263.5% vs前日OI），连续性待观察（方向未知）
10-09 245.0C — Vol 33,299 | 最新价 $0.21 | OI 54229→59653 (ΔOI +5424张) | ΔOI/Volume 16.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5424张（+10.0% vs前日OI），连续性待观察（方向未知）
10-16 240.0C — Vol 23,160 | 最新价 $3.20 | OI 58106→63100 (ΔOI +4994张) | ΔOI/Volume 21.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4994张（+8.6% vs前日OI），连续性待观察（方向未知）
10-09 237.5C — Vol 43,929 | 最新价 $2.14 | OI 9298→14219 (ΔOI +4921张) | ΔOI/Volume 11.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4921张（+52.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,333 张（Put 5,720 / Call 23,613），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +28.9k / P +45.2k ｜ Activity HIGH ｜ 1D
10-12  C +3.6k / P +7.5k ｜ Activity HIGH ｜ 4D
10-14  C +5.1k / P +2.2k ｜ Activity HIGH ｜ 6D
10-16  C +4.8k / P +16.3k ｜ Activity HIGH ｜ 8D

📆 10-09 Forward Structure
存量OI: C 427.5k / P 487.4k，今日变化ΔOI: C +28.9k / P +45.2k，平值价格ATM: C $1.66 / P $1.62 ｜ ATM IV 29.6%，净 delta 敞口 -249k shares
Top ΔOI: C 242 +8,274 ｜ C 245 +5,424 ｜ C 237 +4,921
仓位参考: Max Pain 232 ｜ Call Wall 240（+2.2%，弱）（OI 76.7k） ｜ Put Wall 230（-2.0%，弱）（OI 34.4k）
量化解读： 存量两侧均衡｜ATM IV 29.6%｜历史 Rank 8%（近端代理）｜IV/RV 1.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 249,148 股

📆 10-12 Forward Structure
存量OI: C 38.9k / P 33.3k，今日变化ΔOI: C +3.6k / P +7.5k，平值价格ATM: C $2.36 / P $2.37 ｜ ATM IV 23.1%，净 delta 敞口 55k shares
Top ΔOI: P 215 +1,222 ｜ C 245 +1,133
仓位参考: Max Pain 238 ｜ Call Wall 240（+2.2%）（OI 7.0k） ｜ Put Wall 237.5（+1.2%，弱）（OI 3.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 23.1%｜历史 Rank 8%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 54,505 股

📆 10-14 Forward Structure
存量OI: C 19.0k / P 10.6k，今日变化ΔOI: C +5.1k / P +2.2k，平值价格ATM: C $3.25 / P $3.30 ｜ ATM IV 26.4%，净 delta 敞口 52k shares
Top ΔOI: C 250 +1,134 ｜ C 237 +969 ｜ C 240 +722
仓位参考: Max Pain 235 ｜ Call Wall 250（+6.5%，弱）（OI 2.8k） ｜ Put Wall 237.5（+1.2%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 26.4%｜历史 Rank 8%（近端代理）｜IV/RV 1.55×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 51,970 股

📆 10-16 Forward Structure
存量OI: C 910.8k / P 678.1k，今日变化ΔOI: C +4.8k / P +16.3k，平值价格ATM: C $4.04 / P $3.88 ｜ ATM IV 27.9%，净 delta 敞口 -360k shares
Top ΔOI: P 212 +5,720 ｜ C 240 +4,994
仓位参考: Max Pain 212 ｜ Call Wall 220（-6.3%，弱）（OI 99.7k） ｜ Put Wall 220（-6.3%）（OI 52.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.9%｜历史 Rank 8%（近端代理）｜IV/RV 1.64×（近似）｜净 delta 敞口 负 359,593 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 29.6% vs 10-12 23.1%（差 +6.6pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/NVDA_morning.json