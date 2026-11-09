# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $748.41 ｜ QQQ $674.69
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 46.87 → 今开 47.50（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 47.67 ｜ 低 47.36

Options: P/C成交量 0.43 | OI比 1.11 | ATM IV 41.9% | Skew -1.0pp | Term 0.94 | ExpMove ±2.9%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.11×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-11（2D）±2.9% ｜ 11-13（4D）±3.9% ｜ 11-16（7D）±4.4% ｜ 11-18（9D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 43,702,116 | GEX Change vs 上次快照 20,755,922 | Flip: Primary Flip: 46.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 749 / LOW 138 / INVALID 375
结构观察区: Primary Flip 46.15（全链重定价，覆盖 98%）
最近结构参考: Flip 46（现价高于该位 2.9%）
量化视角： 正 Gamma（4370万，无历史分位）｜正 Gamma 增强（+2076万）｜现价位于 Flip 上方 2.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 46（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 46（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-11 37.0P — Vol 1,100 | 最新价 $0.01 | OI 5→1104 (ΔOI +1099张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1099张（+21980.0% vs前日OI），连续性待观察（方向未知）
11-09 47.0C — Vol 2,811 | 最新价 $0.47 | OI 1185→2259 (ΔOI +1074张) | ΔOI/Volume 38.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1074张（+90.6% vs前日OI），连续性待观察（方向未知）
11-09 46.0P — Vol 2,396 | 最新价 $0.23 | OI 708→1701 (ΔOI +993张) | ΔOI/Volume 41.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增993张（+140.2% vs前日OI），连续性待观察（方向未知）
11-11 40.0P — Vol 1,268 | 最新价 $0.04 | OI 1444→2387 (ΔOI +943张) | ΔOI/Volume 74.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增943张（+65.3% vs前日OI），连续性待观察（方向未知）
11-09 48.5C — Vol 1,252 | 最新价 $0.09 | OI 335→1232 (ΔOI +897张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增897张（+267.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,006 张（Put 3,035 / Call 1,971），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 18.0k / P 20.0k，今日成交量: C 7.2k / P 3.1k，平值价格ATM: C $0.21 / P $0.22 ｜ ATM IV 41.9%，预期波动 ±0.9%，Max Pain 46
Top ΔOI: C 47 +1,074 ｜ P 45 -1,052 ｜ P 46 +993

📆 Forward Expiration Structure

11-11  C +3.5k / P +4.1k ｜ Activity HIGH ｜ 2D
11-13  C +4.1k / P +0.2k ｜ Activity HIGH ｜ 4D
11-16  C +0.5k / P +0.3k ｜ Activity HIGH ｜ 7D
11-18  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 11-11 Forward Structure
存量OI: C 18.5k / P 14.1k，今日变化ΔOI: C +3.5k / P +4.1k，平值价格ATM: C $0.69 / P $0.68 ｜ ATM IV 46.5%，净 delta 敞口 100k shares
Top ΔOI: P 44 +788
仓位参考: Max Pain 46 ｜ Call Wall 51（+7.4%，弱）（OI 2.8k） ｜ Put Wall 44（-7.3%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.5%｜历史 Rank 68%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 100,369 股

📆 11-13 Forward Structure
存量OI: C 62.5k / P 32.9k，今日变化ΔOI: C +4.1k / P +0.2k，平值价格ATM: C $0.94 / P $0.90 ｜ ATM IV 45.1%，净 delta 敞口 118k shares
Top ΔOI: C 50 +573
仓位参考: Max Pain 48 ｜ Call Wall 50（+5.3%）（OI 7.5k） ｜ Put Wall 45（-5.2%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 45.1%｜历史 Rank 68%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 117,867 股

📆 11-16 Forward Structure
存量OI: C 3.5k / P 1.6k，今日变化ΔOI: C +0.5k / P +0.3k，平值价格ATM: C $1.10 / P $0.97 ｜ ATM IV 39.0%，净 delta 敞口 6k shares
Top ΔOI: C 49 +148 ｜ P 46 +115 ｜ P 47 +110
仓位参考: Max Pain 46 ｜ Call Wall 51（+7.4%）（OI 1.1k） ｜ Put Wall 46.5（-2.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 39.0%｜历史 Rank 68%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 6,485 股

📆 11-18 Forward Structure
存量OI: C 1.7k / P 1.0k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $1.22 / P $1.14 ｜ ATM IV 40.1%，净 delta 敞口 6k shares
Top ΔOI: P 44 +261 ｜ C 49 +251 ｜ P 45 +129
仓位参考: Max Pain 45 ｜ Call Wall 50（+5.3%）（OI 0.5k） ｜ Put Wall 44.5（-6.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 40.1%｜历史 Rank 68%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 6,349 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SLV_morning.json