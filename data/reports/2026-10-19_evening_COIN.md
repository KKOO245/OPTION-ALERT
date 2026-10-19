# 期权晚报 2026-10-19（快照 16:40 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🔵 **期限 OI 集中**: 11-06 90P ΔOI +2,810 占该期限总 OI 17.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 175.58 → 收盘 168.45（-4.1%） ｜ 今日高 176.26 ｜ 低 167.49 ｜ 昨收 173.16 → 收盘 168.45（-2.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.62 | OI比 0.70 | ATM IV 67.9% | Skew -0.5pp | Term 1.02 | ExpMove ±5.8%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±5.8% ｜ 10-30（11D）±11.2% ｜ 11-06（18D）±13.4% ｜ 11-13（25D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,257,503 | GEX Change vs 上次快照 -3,694,618 | Flip: Primary Flip: 163.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 450 / LOW 118 / INVALID 238
结构观察区: Primary Flip 163.36（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 0.9%）
最近结构参考: Call Wall 170（现价低于该位 0.9%）
量化视角： 正 Gamma（526万，无历史分位）｜正 Gamma 减弱（369万）｜现价位于 Flip 上方 3.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 178（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 180.0C — Vol 2,541 | 最新价 $1.20 | OI 1156→5901 (ΔOI +4745张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4745张（+410.5% vs前日OI），连续性待观察（方向未知）
10-23 187.5C — Vol 918 | 最新价 $0.52 | OI 1077→5470 (ΔOI +4393张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4393张（+407.9% vs前日OI），连续性待观察（方向未知）
10-23 182.5C — Vol 713 | 最新价 $0.91 | OI 335→3836 (ΔOI +3501张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3501张（+1045.1% vs前日OI），连续性待观察（方向未知）
10-23 177.5C — Vol 858 | 最新价 $1.75 | OI 288→3644 (ΔOI +3356张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3356张（+1165.3% vs前日OI），连续性待观察（方向未知）
11-06 90.0P — Vol 40 | 最新价 $0.07 | OI 1→2811 (ΔOI +2810张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2810张（+281000.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,805 张（Put 2,810 / Call 15,995），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +23.3k / P +12.0k ｜ Activity HIGH ｜ 4D
10-30  C +1.2k / P +2.7k ｜ Activity HIGH ｜ 11D
11-06  C +0.4k / P +3.1k ｜ Activity HIGH ｜ 18D
11-13  C +2.0k / P +0.4k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 54.0k / P 37.9k，今日变化ΔOI: C +23.3k / P +12.0k，平值价格ATM: C $5.50 / P $4.35 ｜ ATM IV 67.8%，净 delta 敞口 63k shares
Top ΔOI: C 180 +4,745 ｜ C 187 +4,393 ｜ C 182 +3,501
仓位参考: Max Pain 178 ｜ Call Wall 180（+6.9%，弱）（OI 5.9k）
量化解读： 存量 Call 重｜ATM IV 67.8%｜历史 Rank 28%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 63,065 股

📆 10-30 Forward Structure
存量OI: C 15.7k / P 16.4k，今日变化ΔOI: C +1.2k / P +2.7k，平值价格ATM: C $10.15 / P $8.70 ｜ ATM IV 80.7%，净 delta 敞口 -6k shares
Top ΔOI: C 200 +469
仓位参考: Max Pain 180 ｜ Call Wall 185（+9.8%，弱）（OI 1.6k） ｜ Put Wall 180（+6.9%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜ATM IV 80.7%｜历史 Rank 28%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,098 股

📆 11-06 Forward Structure
存量OI: C 5.5k / P 10.5k，今日变化ΔOI: C +0.4k / P +3.1k，平值价格ATM: C $12.05 / P $10.45 ｜ ATM IV 75.6%，净 delta 敞口 2k shares
Top ΔOI: P 165 +126
仓位参考: Max Pain 175 ｜ Call Wall 175（+3.9%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 75.6%｜历史 Rank 28%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,760 股

📆 11-13 Forward Structure
存量OI: C 4.7k / P 6.5k，今日变化ΔOI: C +2.0k / P +0.4k，平值价格ATM: C $13.67 / P $11.38 ｜ ATM IV 69.8%，净 delta 敞口 47k shares
Top ΔOI: C 177 +1,093 ｜ C 205 +370
仓位参考: Max Pain 178 ｜ Call Wall 177.5（+5.4%）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.8%｜历史 Rank 28%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 正 47,251 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/COIN_evening.json