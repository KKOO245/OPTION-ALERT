# 期权晚报 2026-10-26（快照 21:54 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 18.39 ↓5.5%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 195.02 → 收盘 198.84（+2.0%） ｜ 今日高 200.05 ｜ 低 192.91 ｜ 昨收 196.75 → 收盘 198.84（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 1.10 | ATM IV 52.5% | Skew 3.9pp | Term 1.19 | ExpMove ±4.5%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构正常偏陡（Term 1.19）｜保护溢价中性（Skew 3.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（4D）±4.5% ｜ 11-06（11D）±12.2% ｜ 11-13（18D）±13.1% ｜ 11-20（25D）±14.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 44,290,584 | GEX Change vs 上次快照 10,022,311 | Flip: Primary Flip: 188.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 594 / LOW 84 / INVALID 222
结构观察区: Primary Flip 188.64（全链重定价，覆盖 100%）
Put Wall 180（弱结构｜现价高于该位 10.5%） | Call Wall 200（弱结构｜现价低于该位 0.6%）
最近结构参考: Call Wall 200（现价低于该位 0.6%）
量化视角： 正 Gamma（4429万，无历史分位）｜正 Gamma 增强（+1002万）｜现价位于 Flip 上方 5.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 192（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 189（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 200.0C — Vol 18,022 | 最新价 $3.90 | OI 4487→14844 (ΔOI +10357张) | ΔOI/Volume 57.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10357张（+230.8% vs前日OI），连续性待观察（方向未知）
10-30 202.5C — Vol 5,674 | 最新价 $2.85 | OI 1512→10949 (ΔOI +9437张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9437张（+624.1% vs前日OI），连续性待观察（方向未知）
10-30 207.5C — Vol 5,758 | 最新价 $1.36 | OI 2393→10520 (ΔOI +8127张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8127张（+339.6% vs前日OI），连续性待观察（方向未知）
10-30 115.0P — Vol 1 | 最新价 $0.02 | OI 608→7177 (ΔOI +6569张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6569张（+1080.4% vs前日OI），连续性待观察（方向未知）
10-30 125.0P — Vol 3 | 最新价 $0.01 | OI 1926→7399 (ΔOI +5473张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5473张（+284.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 39,963 张（Put 12,042 / Call 27,921），跨 1 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-30 Forward Structure
存量OI: C 107.0k / P 118.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.90 / P $4.95 ｜ ATM IV 52.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 192 ｜ Call Wall 200（+0.6%，弱）（OI 14.8k） ｜ Put Wall 190（-4.4%，弱）（OI 8.4k）
量化解读： 存量两侧均衡｜ATM IV 52.5%｜历史 Rank 67%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 215（+8.1%，弱）（OI 2.6k） ｜ Put Wall 190（-4.4%，弱）（OI 3.1k）

11-13（Activity LOW）仓位参考: Max Pain 195 ｜ Call Wall 210（+5.6%，弱）（OI 1.3k） ｜ Put Wall 180（-9.5%，弱）（OI 1.3k）

11-20（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 200（+0.6%，弱）（OI 12.9k） ｜ Put Wall 185（-7.0%，弱）（OI 10.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/PLTR_evening.json