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
🟡 **近现价集中开仓**: 09-23 375C ΔOI +1,883（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 371.64 → 收盘 375.30（+1.0%） ｜ 今日高 378.36 ｜ 低 371.10 ｜ 昨收 364.27 → 收盘 375.30（+3.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.62 | OI比 0.97 | ATM IV 19.5% | Skew -2.1pp | Term 2.30 | ExpMove ±2.5%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常偏陡（Term 2.30）｜Put 保护异常便宜（Skew -2.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-23（2D）±2.5% ｜ 09-25（4D）±3.6% ｜ 09-28（7D）±4.1% ｜ 09-30（9D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 133,670,803 | GEX Change vs 上次快照 4,050,572 | Flip: Primary Flip: 351.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1187 / LOW 115 / INVALID 596
结构观察区: Primary Flip 351.23（全链重定价，覆盖 94%）
Call Wall 400（弱结构｜现价低于该位 6.2%）
最近结构参考: Call Wall 400（现价低于该位 6.2%）
量化视角： 正 Gamma（1.34亿，无历史分位）｜正 Gamma 增强（+405万）｜现价位于 Flip 上方 6.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 362（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 351（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 160.0P — Vol 1 | 最新价 $0.01 | OI 13593→37443 (ΔOI +23850张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23850张（+175.5% vs前日OI），连续性待观察（方向未知）
10-02 200.0P — Vol 256 | 最新价 $0.02 | OI 10097→27603 (ΔOI +17506张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17506张（+173.4% vs前日OI），连续性待观察（方向未知）
09-25 220.0P — Vol 53 | 最新价 $0.02 | OI 2252→19103 (ΔOI +16851张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16851张（+748.3% vs前日OI），连续性待观察（方向未知）
09-25 140.0P — Vol 200 | 最新价 $0.01 | OI 4322→19968 (ΔOI +15646张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15646张（+362.0% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 73,853 张（Put 73,853 / Call 0），跨 2 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-23  C +9.6k / P +8.8k ｜ Activity HIGH ｜ 2D
09-25  C +59.8k / P +87.3k ｜ Activity HIGH ｜ 4D
09-28  C +3.4k / P +1.1k ｜ Activity HIGH ｜ 7D
09-30  C +1.5k / P +0.8k ｜ Activity HIGH ｜ 9D

📆 09-23 Forward Structure
存量OI: C 26.1k / P 21.7k，今日变化ΔOI: C +9.6k / P +8.8k，平值价格ATM: C $4.87 / P $4.50 ｜ ATM IV 42.2%，净 delta 敞口 440k shares
Top ΔOI: P 340 +2,244 ｜ C 375 +1,883
仓位参考: Max Pain 365 ｜ Call Wall 375（-0.1%，弱）（OI 2.9k） ｜ Put Wall 340（-9.4%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 42.2%｜历史 Rank 10%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 440,137 股

📆 09-25 Forward Structure
存量OI: C 155.2k / P 198.4k，今日变化ΔOI: C +59.8k / P +87.3k，平值价格ATM: C $6.95 / P $6.47 ｜ ATM IV 42.5%，净 delta 敞口 2.6M shares
仓位参考: Max Pain 360 ｜ Call Wall 367.5（-2.1%，弱）（OI 17.0k）
量化解读： 存量 Put 重｜ATM IV 42.5%｜历史 Rank 10%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,606,185 股

📆 09-28 Forward Structure
存量OI: C 9.6k / P 4.5k，今日变化ΔOI: C +3.4k / P +1.1k，平值价格ATM: C $7.97 / P $7.40 ｜ ATM IV 37.0%，净 delta 敞口 73k shares
Top ΔOI: C 405 +939 ｜ C 385 +448 ｜ C 390 +288
仓位参考: Max Pain 360 ｜ Call Wall 405（+7.9%，弱）（OI 1.1k） ｜ Put Wall 355（-5.4%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 37.0%｜历史 Rank 10%（近端代理）｜IV/RV 0.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 73,316 股

📆 09-30 Forward Structure
存量OI: C 6.5k / P 3.3k，今日变化ΔOI: C +1.5k / P +0.8k，平值价格ATM: C $9.76 / P $8.86 ｜ ATM IV 39.1%，净 delta 敞口 58k shares
Top ΔOI: C 400 +215 ｜ C 365 +196 ｜ C 390 +160
仓位参考: Max Pain 362 ｜ Call Wall 400（+6.6%，弱）（OI 0.6k） ｜ Put Wall 355（-5.4%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 39.1%｜历史 Rank 10%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 57,764 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-21/TSLA_evening.json