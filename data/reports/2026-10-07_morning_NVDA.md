# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 235P ΔOI +11,576（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 239.24 → 今开 237.68（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 239.08 ｜ 低 237.06

Options: P/C成交量 0.70 | OI比 1.04 | ATM IV 35.5% | Skew 2.5pp | Term 0.82 | ExpMove ±2.0%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价中性（Skew 2.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.0% ｜ 10-12（5D）±2.4% ｜ 10-14（7D）±3.1% ｜ 10-16（9D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 558,464,665 | GEX Change vs 上次快照 -44,748,073 | Flip: Primary Flip: 227.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 667 / LOW 165 / INVALID 676
结构观察区: Primary Flip 227.90（全链重定价，覆盖 96%）
Put Wall 220（弱结构｜现价高于该位 8.4%） | Call Wall 240（弱结构｜现价低于该位 0.6%）
最近结构参考: Call Wall 240（现价低于该位 0.6%）
量化视角： 正 Gamma（5.58亿，无历史分位）｜正 Gamma 减弱（4475万）｜现价位于 Flip 上方 4.68%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 238（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 228（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 240.0C — Vol 55,255 | 最新价 $5.65 | OI 9783→52734 (ΔOI +42951张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增42951张（+439.0% vs前日OI），连续性待观察（方向未知）
10-07 245.0C — Vol 142,296 | 最新价 $0.12 | OI 14169→28465 (ΔOI +14296张) | ΔOI/Volume 10.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14296张（+100.9% vs前日OI），连续性待观察（方向未知）
10-07 247.5C — Vol 53,482 | 最新价 $0.05 | OI 13212→27254 (ΔOI +14042张) | ΔOI/Volume 26.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14042张（+106.3% vs前日OI），连续性待观察（方向未知）
10-07 242.5C — Vol 174,281 | 最新价 $0.36 | OI 12365→24794 (ΔOI +12429张) | ΔOI/Volume 7.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12429张（+100.5% vs前日OI），连续性待观察（方向未知）
10-09 222.5P — Vol 14,709 | 最新价 $0.12 | OI 9316→21470 (ΔOI +12154张) | ΔOI/Volume 82.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12154张（+130.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 95,872 张（Put 12,154 / Call 83,718），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 158.9k / P 165.5k，今日成交量: C 158.7k / P 111.4k，平值价格ATM: C $1.59 / P $0.46 ｜ ATM IV 35.5%，预期波动 ±0.9%，Max Pain 238
Top ΔOI: C 245 +14,296 ｜ C 247 +14,042 ｜ C 242 +12,429

📆 Forward Expiration Structure

10-09  C +2.7k / P +21.3k ｜ Activity HIGH ｜ 2D
10-12  C +9.7k / P +7.6k ｜ Activity HIGH ｜ 5D
10-14  C +2.6k / P +2.7k ｜ Activity HIGH ｜ 7D
10-16  C -8.5k / P +17.1k ｜ Activity HIGH ｜ 9D

📆 10-09 Forward Structure
存量OI: C 398.6k / P 442.3k，今日变化ΔOI: C +2.7k / P +21.3k，平值价格ATM: C $2.98 / P $1.71 ｜ ATM IV 30.6%，净 delta 敞口 -846k shares
Top ΔOI: P 222 +12,154 ｜ P 235 +11,576 ｜ P 217 -9,159
仓位参考: Max Pain 232 ｜ Call Wall 240（+0.6%，弱）（OI 75.1k） ｜ Put Wall 230（-3.6%，弱）（OI 35.2k）
量化解读： 存量两侧均衡｜ATM IV 30.6%｜历史 Rank 23%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 846,282 股

📆 10-12 Forward Structure
存量OI: C 35.3k / P 25.7k，今日变化ΔOI: C +9.7k / P +7.6k，平值价格ATM: C $3.50 / P $2.19 ｜ ATM IV 24.3%，净 delta 敞口 -71k shares
Top ΔOI: P 240 +1,971 ｜ C 250 +1,684 ｜ C 242 +1,500
仓位参考: Max Pain 238 ｜ Call Wall 240（+0.6%）（OI 7.1k） ｜ Put Wall 237.5（-0.4%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 24.3%｜历史 Rank 23%（近端代理）｜IV/RV 1.49×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 71,212 股

📆 10-14 Forward Structure
存量OI: C 13.9k / P 8.4k，今日变化ΔOI: C +2.6k / P +2.7k，平值价格ATM: C $4.32 / P $3.05 ｜ ATM IV 27.1%，净 delta 敞口 -26k shares
Top ΔOI: C 260 +804 ｜ C 245 +601 ｜ P 230 +518
仓位参考: Max Pain 235 ｜ Call Wall 260（+9.0%，弱）（OI 2.1k） ｜ Put Wall 237.5（-0.4%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.1%｜历史 Rank 23%（近端代理）｜IV/RV 1.66×（近似）｜净 delta 敞口 负 26,173 股

📆 10-16 Forward Structure
存量OI: C 906.0k / P 661.8k，今日变化ΔOI: C -8.5k / P +17.1k，平值价格ATM: C $5.00 / P $3.62 ｜ ATM IV 28.3%，净 delta 敞口 -1.2M shares
Top ΔOI: C 250 -6,379 ｜ P 242 +5,165 ｜ C 245 -2,457
仓位参考: Max Pain 210 ｜ Call Wall 220（-7.8%，弱）（OI 99.8k） ｜ Put Wall 220（-7.8%，弱）（OI 51.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 28.3%｜历史 Rank 23%（近端代理）｜IV/RV 1.74×（近似）｜净 delta 敞口 负 1,246,275 股

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 30.6% vs 10-12 24.3%（差 +6.3pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/NVDA_morning.json