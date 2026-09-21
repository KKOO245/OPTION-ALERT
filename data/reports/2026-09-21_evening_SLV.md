# 期权晚报 2026-09-21（快照 16:40 ET）

📊 市场环境

SPY $773.50 ｜ QQQ $741.47
VIX 14.87 ↑0.4%（5D -13.0%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 33.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.3 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 61P ΔOI +1,405（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-28 62C ΔOI +2,077 占该期限总 OI 23.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 60.14 → 收盘 59.63（-0.8%） ｜ 今日高 60.15 ｜ 低 59.35 ｜ 昨收 59.93 → 收盘 59.63（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.44 | OI比 0.53 | ATM IV 29.3% | Skew -43.8pp | Term 1.22 | ExpMove ±2.1%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构正常偏陡（Term 1.22）｜Put 保护异常便宜（Skew -43.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-23（2D）±2.1% ｜ 09-25（4D）±3.0% ｜ 09-28（7D）±3.5% ｜ 09-30（9D）±4.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 83,937,771 | GEX Change vs 上次快照 -9,595,159 | Flip: Primary Flip: 56.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 850 / LOW 169 / INVALID 323
结构观察区: Primary Flip 56.58（全链重定价，覆盖 96%）
Put Wall 60（弱结构｜现价低于该位 0.6%）
最近结构参考: Put Wall 60（现价低于该位 0.6%）
量化视角： 正 Gamma（8394万，无历史分位）｜正 Gamma 减弱（960万）｜现价位于 Flip 上方 5.39%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 58（MaxPain，仅结算参考）；上方 60（Put Wall，弱结构）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 60.0C — Vol 2,131 | 最新价 $1.34 | OI 873→5926 (ΔOI +5053张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5053张（+578.8% vs前日OI），连续性待观察（方向未知）
10-16 62.0C — Vol 1,671 | 最新价 $1.38 | OI 5851→9973 (ΔOI +4122张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4122张（+70.5% vs前日OI），连续性待观察（方向未知）
10-16 59.0P — Vol 3,516 | 最新价 $1.79 | OI 2621→6443 (ΔOI +3822张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3822张（+145.8% vs前日OI），连续性待观察（方向未知）
10-16 60.0P — Vol 1,120 | 最新价 $2.29 | OI 32427→35979 (ΔOI +3552张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增3552张（+10.9% vs前日OI），值得跟踪（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 16,549 张（Put 7,374 / Call 9,175），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-23  C +6.3k / P +0.6k ｜ Activity HIGH ｜ 2D
09-25  C +8.3k / P +3.6k ｜ Activity HIGH ｜ 4D
09-28  C +3.0k / P +2.5k ｜ Activity HIGH ｜ 7D
09-30  C +1.9k / P -73 ｜ Activity HIGH ｜ 9D

📆 09-23 Forward Structure
存量OI: C 14.2k / P 13.2k，今日变化ΔOI: C +6.3k / P +0.6k，平值价格ATM: C $0.71 / P $0.54 ｜ ATM IV 35.4%，净 delta 敞口 60k shares
Top ΔOI: C 63 +675
仓位参考: Max Pain 59 ｜ Call Wall 65（+9.0%）（OI 2.1k） ｜ Put Wall 55（-7.8%）（OI 4.4k）
量化解读： 存量两侧均衡｜ATM IV 35.4%｜历史 Rank 37%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,606 股

📆 09-25 Forward Structure
存量OI: C 106.7k / P 41.8k，今日变化ΔOI: C +8.3k / P +3.6k，平值价格ATM: C $0.98 / P $0.79 ｜ ATM IV 35.6%，净 delta 敞口 -79k shares
Top ΔOI: P 61 +1,405 ｜ C 61 +1,384 ｜ C 63 +1,252
仓位参考: Max Pain 60 ｜ Put Wall 55（-7.8%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜ATM IV 35.6%｜历史 Rank 37%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 79,008 股

📆 09-28 Forward Structure
存量OI: C 4.9k / P 3.9k，今日变化ΔOI: C +3.0k / P +2.5k，平值价格ATM: C $1.15 / P $0.92 ｜ ATM IV 31.0%，净 delta 敞口 12k shares
Top ΔOI: C 62 +2,077 ｜ P 60 +554
仓位参考: Max Pain 60 ｜ Call Wall 62.5（+4.8%）（OI 2.1k） ｜ Put Wall 60.5（+1.5%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 31.0%｜历史 Rank 37%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 正 12,306 股

📆 09-30 Forward Structure
存量OI: C 270.7k / P 151.9k，今日变化ΔOI: C +1.9k / P -73，平值价格ATM: C $1.35 / P $1.07 ｜ ATM IV 32.4%，净 delta 敞口 60k shares
Top ΔOI: P 55 +711
仓位参考: Max Pain 62 ｜ Put Wall 55（-7.8%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 32.4%｜历史 Rank 37%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 60,189 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/SLV_evening.json