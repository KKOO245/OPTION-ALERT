# 期权晚报 2026-09-17（快照 21:08 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.44 ↓12.8%（5D -13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 716.05 → 收盘 716.92（+0.1%） ｜ 今日高 718.04 ｜ 低 713.32 ｜ 昨收 704.72 → 收盘 716.92（+1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.29 | OI比 1.32 | ATM IV 17.0% | Skew 2.1pp | Term 1.00 | ExpMove ±0.7%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常（Term 1.00）｜保护溢价中性（Skew 2.1pp）｜当日成交偏 Put（P/C量 1.29）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.29×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.32×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 69% ｜ P/C OI(近端) 22%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 69%）｜近端持仓结构中性（P/C OI 分位 22%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-18（1D）±0.7% ｜ 09-21（4D）±1.1% ｜ 09-22（5D）±1.3% ｜ 09-23（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 182,453,328 | GEX Change vs 上次快照 -25,401,010 | Flip: Primary Flip: 715.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2940 / LOW 383 / INVALID 1649
结构观察区: Primary Flip 715.06（全链重定价，覆盖 94%）
Put Wall 690（弱结构｜现价高于该位 3.9%）
最近结构参考: Flip 715（现价高于该位 0.3%）
量化视角： 正 Gamma（1.82亿，历史分位 69%，中性区）｜正 Gamma 减弱（2540万）｜现价位于 Flip 上方 0.26%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 690（Put Wall，弱结构） / 700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 715（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-22  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-18 Forward Structure
存量OI: C 1158.6k / P 1530.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.35 / P $2.78 ｜ ATM IV 17.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 700 ｜ Call Wall 750（+4.6%，弱）（OI 50.6k） ｜ Put Wall 700（-2.4%，弱）（OI 90.8k）
量化解读： 存量 Put 重｜ATM IV 17.0%｜历史 Rank 42%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-21（Activity LOW）仓位参考: Max Pain 715 ｜ Call Wall 720（+0.4%，弱）（OI 2.3k） ｜ Put Wall 715（-0.3%，弱）（OI 7.3k）

09-22（Activity LOW）仓位参考: Max Pain 710 ｜ Call Wall 758（+5.7%，弱）（OI 3.4k） ｜ Put Wall 685（-4.5%，弱）（OI 1.9k）

09-23（Activity LOW）仓位参考: Max Pain 710 ｜ Call Wall 735（+2.5%，弱）（OI 1.9k） ｜ Put Wall 680（-5.1%）（OI 2.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/QQQ_evening.json