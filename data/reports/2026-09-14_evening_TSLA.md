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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 359.95 → 收盘 358.97（-0.3%） ｜ 今日高 367.73 ｜ 低 357.04 ｜ 昨收 365.44 → 收盘 358.97（-1.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.75 | OI比 0.76 | ATM IV 27.3% | Skew -6.0pp | Term 1.47 | ExpMove ±2.7%（近端） | Rank 1%
量化视角： IV 历史低位（Rank 1%，期权偏便宜）｜期限结构正常偏陡（Term 1.47）｜Put 保护异常便宜（Skew -6.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-16（2D）±2.7% ｜ 09-18（4D）±3.7% ｜ 09-21（7D）±4.2% ｜ 09-23（9D）±4.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 7,789,196 | GEX Change vs 上次快照 -23,378,583 | Flip: Primary Flip: 357.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1240 / LOW 181 / INVALID 605
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 357.18（全链重定价，覆盖 94%）
最近结构参考: Flip 357（现价高于该位 0.5%）
量化视角： 正 Gamma（779万，无历史分位）｜正 Gamma 减弱（2338万）｜现价位于 Flip 上方 0.50%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 365（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 357（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 145.0P — Vol 150 | 最新价 $0.01 | OI 2547→24672 (ΔOI +22125张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22125张（+868.7% vs前日OI），连续性待观察（方向未知）
09-18 220.0P — Vol 195 | 最新价 $0.01 | OI 3723→21074 (ΔOI +17351张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17351张（+466.1% vs前日OI），连续性待观察（方向未知）
10-02 200.0P — Vol 37 | 最新价 $0.06 | OI 215→10104 (ΔOI +9889张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9889张（+4599.5% vs前日OI），连续性待观察（方向未知）
09-18 367.5C — Vol 3,935 | 最新价 $3.45 | OI 2059→8291 (ΔOI +6232张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6232张（+302.7% vs前日OI），连续性待观察（方向未知）
09-18 370.0C — Vol 16,305 | 最新价 $2.84 | OI 13153→19371 (ΔOI +6218张) | ΔOI/Volume 38.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6218张（+47.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 61,815 张（Put 49,365 / Call 12,450），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-16  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-16 Forward Structure
存量OI: C 25.9k / P 16.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.40 / P $5.28 ｜ ATM IV 45.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 362 ｜ Call Wall 370（+3.1%，弱）（OI 3.3k） ｜ Put Wall 340（-5.3%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 45.2%｜历史 Rank 1%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-18（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 370（+3.1%，弱）（OI 19.4k） ｜ Put Wall 350（-2.5%，弱）（OI 17.7k）

09-21（Activity LOW）仓位参考: Max Pain 365 ｜ Call Wall 380（+5.9%，弱）（OI 0.8k） ｜ Put Wall 345（-3.9%）（OI 0.7k）

09-23（Activity LOW）仓位参考: Max Pain 368 ｜ Call Wall 390（+8.6%，弱）（OI 0.6k） ｜ Put Wall 382.5（+6.6%）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/TSLA_evening.json