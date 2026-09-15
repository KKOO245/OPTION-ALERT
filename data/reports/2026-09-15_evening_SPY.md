# 期权晚报 2026-09-15（快照 16:40 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $704.54
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **近现价集中开仓**: 09-16 721P ΔOI +12,865（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 760.12 → 收盘 757.39（-0.4%） ｜ 今日高 760.34 ｜ 低 756.15 ｜ 昨收 760.88 → 收盘 757.39（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.04 | OI比 3.19 | ATM IV 10.1% | Skew 1.0pp | Term 1.37 | ExpMove ±0.8%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常偏陡（Term 1.37）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 3.19×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 17% ｜ P/C OI(近端) 97%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 17%）｜近端 Put 显著偏重（P/C OI 分位 97%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-16（1D）±0.8% ｜ 09-17（2D）±1.1% ｜ 09-18（3D）±1.3% ｜ 09-21（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,906,390,601 | GEX Change vs 上次快照 269,292,433 | Flip: Primary Flip: 769.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3074 / LOW 385 / INVALID 2171
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 769.38（全链重定价，覆盖 94%）
Call Wall 800（弱结构｜现价低于该位 5.3%）
最近结构参考: Flip 769（现价低于该位 1.6%）
量化视角： 负 Gamma（19.06亿，历史分位偏负区，比 83% 的交易日更负）｜负 Gamma 缓解（+2.69亿）｜现价位于 Flip 下方 1.56%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 761（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-16  C +22.9k / P +58.7k ｜ Activity HIGH ｜ 1D
09-17  C +12.0k / P +26.0k ｜ Activity HIGH ｜ 2D
09-18  C +55.4k / P +22.9k ｜ Activity MEDIUM △ ｜ 3D
09-21  C +11.4k / P +16.8k ｜ Activity HIGH ｜ 6D

📆 09-16 Forward Structure
存量OI: C 60.5k / P 103.9k，今日变化ΔOI: C +22.9k / P +58.7k，平值价格ATM: C $3.73 / P $2.50 ｜ ATM IV 19.4%，净 delta 敞口 -202k shares
Top ΔOI: P 721 +12,865 ｜ P 731 +11,011 ｜ P 726 +9,312
仓位参考: Max Pain 761 ｜ Call Wall 766（+1.1%，弱）（OI 5.0k） ｜ Put Wall 721（-4.8%，弱）（OI 12.9k）
量化解读： 存量 Put 重｜ATM IV 19.4%｜历史 Rank 24%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 202,126 股

📆 09-17 Forward Structure
存量OI: C 54.0k / P 84.9k，今日变化ΔOI: C +12.0k / P +26.0k，平值价格ATM: C $4.81 / P $3.47 ｜ ATM IV 18.3%，净 delta 敞口 -56k shares
仓位参考: Max Pain 760 ｜ Call Wall 775（+2.3%，弱）（OI 4.7k） ｜ Put Wall 750（-1.0%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 18.3%｜历史 Rank 24%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 56,098 股

09-18（MEDIUM △）Top ΔOI: 804C +8,451 ｜ 800C +6,704
09-18（MEDIUM △）仓位参考: Max Pain 755 ｜ Call Wall 790（+4.3%，弱）（OI 56.1k） ｜ Put Wall 750（-1.0%，弱）（OI 134.8k）

📆 09-21 Forward Structure
存量OI: C 38.0k / P 41.4k，今日变化ΔOI: C +11.4k / P +16.8k，平值价格ATM: C $5.43 / P $5.59 ｜ ATM IV 14.2%，净 delta 敞口 49k shares
Top ΔOI: P 720 +1,576 ｜ P 722 +1,459 ｜ P 685 +1,457
仓位参考: Max Pain 757 ｜ Call Wall 760（+0.3%）（OI 4.2k） ｜ Put Wall 755（-0.3%）（OI 4.0k）
量化解读： 存量两侧均衡｜ATM IV 14.2%｜历史 Rank 24%（近端代理）｜净 delta 敞口 正 48,836 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SPY_evening.json