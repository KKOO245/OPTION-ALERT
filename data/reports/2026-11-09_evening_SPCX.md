# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
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

🔍 重点速览
🟡 **近现价集中开仓**: 11-11 140C ΔOI +554（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 136.53 → 收盘 142.07（+4.1%） ｜ 今日高 143.20 ｜ 低 135.37 ｜ 昨收 134.27 → 收盘 142.07（+5.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.80 | OI比 1.23 | ATM IV 67.3% | Skew -11.8pp | Term 0.85 | ExpMove ±4.3%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -11.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-11（2D）±4.3% ｜ 11-13（4D）±6.0% ｜ 11-16（7D）±6.7% ｜ 11-18（9D）±8.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 37,418,151 | GEX Change vs 上次快照 -5,096,951 | Flip: Primary Flip: 137.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 844 / LOW 169 / INVALID 697
结构观察区: Primary Flip 137.11（全链重定价，覆盖 96%）
Put Wall 130（弱结构｜现价高于该位 9.3%）
最近结构参考: Flip 137（现价高于该位 3.6%）
量化视角： 正 Gamma（3742万，无历史分位）｜正 Gamma 减弱（510万）｜现价位于 Flip 上方 3.62%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（Put Wall，弱结构） / 131（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 160.0C — Vol 10,772 | 最新价 $1.30 | OI 40334→72305 (ΔOI +31971张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31971张（+79.3% vs前日OI），连续性待观察（方向未知）
11-13 75.0P — Vol 127 | 最新价 $0.02 | OI 1268→8586 (ΔOI +7318张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7318张（+577.1% vs前日OI），连续性待观察（方向未知）
11-13 80.0P — Vol 2,959 | 最新价 $0.02 | OI 5050→10692 (ΔOI +5642张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5642张（+111.7% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 7,055 | 最新价 $3.38 | OI 29250→34874 (ΔOI +5624张) | ΔOI/Volume 79.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5624张（+19.2% vs前日OI），连续性待观察（方向未知）
11-20 155.0C — Vol 4,221 | 最新价 $2.13 | OI 11273→15809 (ΔOI +4536张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4536张（+40.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 55,091 张（Put 12,960 / Call 42,131），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-11  C +3.8k / P +3.0k ｜ Activity HIGH ｜ 2D
11-13  C +23.0k / P +34.2k ｜ Activity HIGH ｜ 4D
11-16  C +1.9k / P +0.5k ｜ Activity HIGH ｜ 7D
11-18  C +0.9k / P +0.4k ｜ Activity HIGH ｜ 9D

📆 11-11 Forward Structure
存量OI: C 17.9k / P 13.9k，今日变化ΔOI: C +3.8k / P +3.0k，平值价格ATM: C $3.15 / P $3.00 ｜ ATM IV 72.5%，净 delta 敞口 223k shares
Top ΔOI: C 140 +554 ｜ P 130 +467 ｜ C 144 +451
仓位参考: Max Pain 130 ｜ Call Wall 140（-1.5%，弱）（OI 1.8k） ｜ Put Wall 130（-8.5%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 72.5%｜历史 Rank 78%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 222,532 股

📆 11-13 Forward Structure
存量OI: C 116.3k / P 112.1k，今日变化ΔOI: C +23.0k / P +34.2k，平值价格ATM: C $4.37 / P $4.15 ｜ ATM IV 70.1%，净 delta 敞口 989k shares
Top ΔOI: C 135 +3,678
仓位参考: Max Pain 140 ｜ Call Wall 150（+5.6%，弱）（OI 6.5k） ｜ Put Wall 135（-5.0%，弱）（OI 6.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.1%｜历史 Rank 78%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 988,557 股

📆 11-16 Forward Structure
存量OI: C 5.1k / P 2.0k，今日变化ΔOI: C +1.9k / P +0.5k，平值价格ATM: C $4.85 / P $4.71 ｜ ATM IV 62.5%，净 delta 敞口 57k shares
Top ΔOI: C 150 +148
仓位参考: Max Pain 132 ｜ Call Wall 150（+5.6%，弱）（OI 1.0k） ｜ Put Wall 130（-8.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 62.5%｜历史 Rank 78%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 56,562 股

📆 11-18 Forward Structure
存量OI: C 2.7k / P 1.7k，今日变化ΔOI: C +0.9k / P +0.4k，平值价格ATM: C $5.65 / P $5.82 ｜ ATM IV 64.4%，净 delta 敞口 52k shares
Top ΔOI: C 130 +187 ｜ C 140 +131 ｜ C 145 +115
仓位参考: Max Pain 130 ｜ Call Wall 145（+2.1%，弱）（OI 0.4k） ｜ Put Wall 130（-8.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 64.4%｜历史 Rank 78%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 正 51,925 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SPCX_evening.json