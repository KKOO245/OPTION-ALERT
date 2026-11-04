# 期权晚报 2026-11-04（快照 16:40 ET）

📊 市场环境

SPY $766.81 ｜ QQQ $691.95
VIX 16.61 ↓20.3%（5D -1.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-05 730P ΔOI +3,887（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 762.99 → 收盘 766.81（+0.5%） ｜ 今日高 769.22 ｜ 低 762.64 ｜ 昨收 754.35 → 收盘 766.81（+1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.11 | OI比 1.83 | ATM IV 14.7% | Skew -0.6pp | Term 0.91 | ExpMove ±0.6%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.83×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 50% ｜ P/C OI(近端) 50%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 50%）｜近端持仓结构中性（P/C OI 分位 50%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-05（1D）±0.6% ｜ 11-06（2D）±0.9% ｜ 11-09（5D）±1.1% ｜ 11-10（6D）±1.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -291,758,621 | GEX Change vs 上次快照 -161,776,121 | Flip: Primary Flip: 769.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2676 / LOW 406 / INVALID 2176
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 769.56（全链重定价，覆盖 94%）
最近结构参考: Flip 770（现价低于该位 0.4%）
量化视角： 负 Gamma（2.92亿，历史分位 50%，中性区）｜负 Gamma 加深（1.62亿）｜现价位于 Flip 下方 0.36%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 757（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-05  C +30.5k / P +39.8k ｜ Activity HIGH ｜ 1D
11-06  C +20.9k / P +31.7k ｜ Activity HIGH ｜ 2D
11-09  C +9.6k / P +9.9k ｜ Activity HIGH ｜ 5D
11-10  C +8.8k / P +7.6k ｜ Activity HIGH ｜ 6D

📆 11-05 Forward Structure
存量OI: C 85.0k / P 130.8k，今日变化ΔOI: C +30.5k / P +39.8k，平值价格ATM: C $2.70 / P $1.75 ｜ ATM IV 13.7%，净 delta 敞口 1.6M shares
Top ΔOI: P 730 +3,887 ｜ C 745 +3,614
仓位参考: Max Pain 755 ｜ Call Wall 780（+1.7%）（OI 16.3k） ｜ Put Wall 750（-2.2%，弱）（OI 6.0k）
量化解读： 存量 Put 重｜ATM IV 13.7%｜历史 Rank 63%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,586,984 股

📆 11-06 Forward Structure
存量OI: C 238.3k / P 450.8k，今日变化ΔOI: C +20.9k / P +31.7k，平值价格ATM: C $4.10 / P $2.80 ｜ ATM IV 14.9%，净 delta 敞口 993k shares
Top ΔOI: P 730 +4,405
仓位参考: Max Pain 762 ｜ Call Wall 770（+0.4%，弱）（OI 17.7k） ｜ Put Wall 750（-2.2%）（OI 42.4k）
量化解读： 存量 Put 重｜ATM IV 14.9%｜历史 Rank 63%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 992,622 股

📆 11-09 Forward Structure
存量OI: C 34.6k / P 56.7k，今日变化ΔOI: C +9.6k / P +9.9k，平值价格ATM: C $4.94 / P $3.59 ｜ ATM IV 11.8%，净 delta 敞口 440k shares
Top ΔOI: C 757 +1,237 ｜ C 790 -1,177 ｜ C 786 +1,025
仓位参考: Max Pain 760 ｜ Call Wall 775（+1.1%，弱）（OI 4.1k） ｜ Put Wall 745（-2.8%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜ATM IV 11.8%｜历史 Rank 63%（近端代理）｜IV/RV 1.10×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 439,892 股

📆 11-10 Forward Structure
存量OI: C 28.8k / P 27.1k，今日变化ΔOI: C +8.8k / P +7.6k，平值价格ATM: C $5.76 / P $4.20 ｜ ATM IV 12.6%，净 delta 敞口 270k shares
Top ΔOI: C 780 +865 ｜ C 782 +854
仓位参考: Max Pain 760 ｜ Call Wall 775（+1.1%，弱）（OI 4.4k） ｜ Put Wall 755（-1.5%）（OI 3.3k）
量化解读： 存量两侧均衡｜ATM IV 12.6%｜历史 Rank 63%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 269,656 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/SPY_evening.json