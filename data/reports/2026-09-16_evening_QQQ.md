# 期权晚报 2026-09-16（快照 21:12 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 17.71 ↑3.0%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 708.06 → 收盘 704.72（-0.5%） ｜ 今日高 711.88 ｜ 低 700.00 ｜ 昨收 704.54 → 收盘 704.72（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.38 | OI比 1.98 | ATM IV 23.1% | Skew 4.4pp | Term 0.83 | ExpMove ±1.0%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 4.4pp）｜当日成交偏 Put（P/C量 1.38）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.38×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.98×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 9% ｜ P/C OI(近端) 76%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 9%）｜近端持仓结构中性（P/C OI 分位 76%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-17（1D）±1.0% ｜ 09-18（2D）±1.3% ｜ 09-21（5D）±1.7% ｜ 09-22（6D）±1.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -870,660,890 | GEX Change vs 上次快照 -527,655,485 | Flip: Primary Flip: 714.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2916 / LOW 363 / INVALID 2003
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 714.92（全链重定价，覆盖 95%）
Put Wall 700（弱结构｜现价高于该位 0.7%）
最近结构参考: Put Wall 700（现价高于该位 0.7%）
量化视角： 负 Gamma（8.71亿，历史分位偏负区，比 91% 的交易日更负）｜负 Gamma 加深（5.28亿）｜现价位于 Flip 下方 1.43%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 707（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 715（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-17  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-22  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-17 Forward Structure
存量OI: C 60.4k / P 119.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.46 / P $3.38 ｜ ATM IV 23.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 707 ｜ Call Wall 723（+2.6%）（OI 10.4k） ｜ Put Wall 650（-7.8%）（OI 9.5k）
量化解读： 存量 Put 重｜ATM IV 23.1%｜历史 Rank 73%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-18（Activity LOW）仓位参考: Max Pain 700 ｜ Call Wall 750（+6.4%，弱）（OI 50.6k） ｜ Put Wall 700（-0.7%）（OI 115.0k）

09-21（Activity LOW）仓位参考: Max Pain 715 ｜ Call Wall 735（+4.3%，弱）（OI 2.1k） ｜ Put Wall 715（+1.5%）（OI 6.3k）

09-22（Activity LOW）仓位参考: Max Pain 710 ｜ Call Wall 725（+2.9%）（OI 1.1k） ｜ Put Wall 685（-2.8%，弱）（OI 1.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/QQQ_evening.json