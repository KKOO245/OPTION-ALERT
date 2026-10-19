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
🔴 **事件差分**: 10-21（2D）ATM IV 120.1% vs 10-23 96.2%（差 +23.9pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-21 155C ΔOI +3,200（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 148P ΔOI +998 占该期限总 OI 11.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 149.25 → 收盘 147.96（-0.9%） ｜ 今日高 151.01 ｜ 低 146.84 ｜ 昨收 146.03 → 收盘 147.96（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 1.24 | ATM IV 30.2% | Skew 4.8pp | Term 1.89 | ExpMove ±7.1%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.89）｜保护溢价中性（Skew 4.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-21（2D）±7.1% ｜ 10-23（4D）±8.1% ｜ 10-26（7D）±8.0% ｜ 10-28（9D）±9.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -15,438,662 | GEX Change vs 上次快照 3,078,029 | Flip: Primary Flip: 150.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 791 / LOW 77 / INVALID 504
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 150.52（全链重定价，覆盖 93%）
Put Wall 140（弱结构｜现价高于该位 5.7%）
最近结构参考: Flip 151（现价低于该位 1.7%）
量化视角： 负 Gamma（1544万，无历史分位）｜负 Gamma 缓解（+308万）｜现价位于 Flip 下方 1.70%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 146.0C — Vol 706 | 最新价 $7.00 | OI 634→7701 (ΔOI +7067张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7067张（+1114.7% vs前日OI），连续性待观察（方向未知）
10-23 80.0P — Vol 5,491 | 最新价 $0.02 | OI 89→6594 (ΔOI +6505张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6505张（+7309.0% vs前日OI），连续性待观察（方向未知）
量化视角： 2 个事件合计 ΔOI ≈ 13,572 张（Put 6,505 / Call 7,067），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-21  C +10.2k / P +19.8k ｜ Activity HIGH ｜ 2D
10-23  C +27.1k / P +38.8k ｜ Activity HIGH ｜ 4D
10-26  C +1.9k / P +0.9k ｜ Activity HIGH ｜ 7D
10-28  C +0.9k / P +1.8k ｜ Activity HIGH ｜ 9D

📆 10-21 Forward Structure
存量OI: C 30.9k / P 30.8k，今日变化ΔOI: C +10.2k / P +19.8k，平值价格ATM: C $5.27 / P $5.26 ｜ ATM IV 120.1%，净 delta 敞口 -121k shares
Top ΔOI: P 135 +4,375 ｜ P 140 +3,680 ｜ C 155 +3,200
仓位参考: Max Pain 149 ｜ Call Wall 155（+4.8%）（OI 4.2k） ｜ Put Wall 135（-8.8%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 120.1%｜历史 Rank 0%（近端代理）｜IV/RV 2.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 120,816 股

📆 10-23 Forward Structure
存量OI: C 107.2k / P 129.8k，今日变化ΔOI: C +27.1k / P +38.8k，平值价格ATM: C $6.00 / P $6.00 ｜ ATM IV 96.2%，净 delta 敞口 409k shares
Top ΔOI: C 146 +7,067 ｜ P 135 +4,906
仓位参考: Max Pain 150 ｜ Call Wall 155（+4.8%，弱）（OI 8.0k） ｜ Put Wall 140（-5.4%，弱）（OI 11.2k）
量化解读： 存量 Put 重｜ATM IV 96.2%｜历史 Rank 0%（近端代理）｜IV/RV 1.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 409,194 股

📆 10-26 Forward Structure
存量OI: C 6.1k / P 3.6k，今日变化ΔOI: C +1.9k / P +0.9k，平值价格ATM: C $5.95 / P $5.95 ｜ ATM IV 76.7%，净 delta 敞口 34k shares
Top ΔOI: C 147 +463
仓位参考: Max Pain 150 ｜ Call Wall 155（+4.8%，弱）（OI 0.8k） ｜ Put Wall 144（-2.7%）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 76.7%｜历史 Rank 0%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,595 股

📆 10-28 Forward Structure
存量OI: C 2.3k / P 6.3k，今日变化ΔOI: C +0.9k / P +1.8k，平值价格ATM: C $6.69 / P $7.02 ｜ ATM IV 72.6%，净 delta 敞口 -40k shares
Top ΔOI: P 148 +998 ｜ P 142 +304
仓位参考: Max Pain 150 ｜ Call Wall 160（+8.1%，弱）（OI 0.4k） ｜ Put Wall 148（+0.0%）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 72.6%｜历史 Rank 0%（近端代理）｜IV/RV 1.47×（近似）｜净 delta 敞口 负 40,133 股

📅 事件差分（观察，非因果）: 10-21（2D）ATM IV 120.1% vs 10-23 96.2%（差 +23.9pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SPCX_evening.json