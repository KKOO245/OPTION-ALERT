# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **单日价格波动**: -6.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 256.39 → 收盘 257.05（+0.3%） ｜ 今日高 261.70 ｜ 低 249.05 ｜ 昨收 275.75 → 收盘 257.05（-6.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.70 | OI比 0.85 | ATM IV 84.5% | Skew -1.6pp | Term 0.93 | ExpMove ±7.2%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（4D）±7.2% ｜ 09-25（11D）±10.8% ｜ 10-02（18D）±13.9% ｜ 10-09（25D）±16.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,285,153 | GEX Change vs 上次快照 641,942 | Flip: Primary Flip: 224.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 656 / LOW 94 / INVALID 210
结构观察区: Primary Flip 224.47（全链重定价，覆盖 100%）
Call Wall 250（弱结构｜现价高于该位 2.8%）
最近结构参考: Call Wall 250（现价高于该位 2.8%）
量化视角： 正 Gamma（1829万，无历史分位）｜正 Gamma 增强（+64万）｜现价位于 Flip 上方 14.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 240（MaxPain，仅结算参考） / 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 224（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 275.0C — Vol 1,786 | 最新价 $3.15 | OI 2629→5683 (ΔOI +3054张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3054张（+116.2% vs前日OI），连续性待观察（方向未知）
10-16 125.0P — Vol 4 | 最新价 $0.17 | OI 1732→3026 (ΔOI +1294张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1294张（+74.7% vs前日OI），连续性待观察（方向未知）
10-16 100.0P — Vol 23 | 最新价 $0.07 | OI 1541→2542 (ΔOI +1001张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1001张（+65.0% vs前日OI），连续性待观察（方向未知）
09-25 275.0C — Vol 223 | 最新价 $7.80 | OI 306→1135 (ΔOI +829张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增829张（+270.9% vs前日OI），连续性待观察（方向未知）
09-18 300.0C — Vol 2,320 | 最新价 $0.58 | OI 5050→5801 (ΔOI +751张) | ΔOI/Volume 32.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增751张（+14.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,929 张（Put 2,295 / Call 4,634），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 140.3k / P 119.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $8.94 / P $9.64 ｜ ATM IV 84.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 240 ｜ Call Wall 250（-2.7%）（OI 21.0k） ｜ Put Wall 260（+1.1%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 84.5%｜历史 Rank 44%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 245 ｜ Call Wall 280（+8.9%，弱）（OI 1.4k） ｜ Put Wall 250（-2.7%，弱）（OI 2.3k）

10-02（Activity LOW）仓位参考: Max Pain 245 ｜ Call Wall 275（+7.0%，弱）（OI 1.8k） ｜ Put Wall 245（-4.7%，弱）（OI 1.0k）

10-09（Activity LOW）仓位参考: Max Pain 250 ｜ Call Wall 275（+7.0%，弱）（OI 0.1k） ｜ Put Wall 240（-6.6%）（OI 1.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/BE_evening.json