# 期权晚报 2026-09-23（快照 16:40 ET）

📊 市场环境

SPY $767.81 ｜ QQQ $741.21
VIX 15.18 ↑2.1%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　⏰ 今日
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 772.79 → 收盘 767.81（-0.6%） ｜ 今日高 773.02 ｜ 低 766.50 ｜ 昨收 773.38 → 收盘 767.81（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.95 | OI比 0.92 | ATM IV 11.2% | Skew 0.5pp | Term 1.10 | ExpMove ±0.9%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 1.10）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 50% ｜ P/C OI(近端) 1%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 50%）｜近端持仓极端 Call 重（P/C OI 分位 1%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-24（1D）±0.9% ｜ 09-25（2D）±1.1% ｜ 09-28（5D）±1.2% ｜ 09-29（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -298,767,339 | GEX Change vs 上次快照 -997,851,405 | Flip: Primary Flip: 769.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2871 / LOW 347 / INVALID 1656
结构观察区: Primary Flip 769.52（全链重定价，覆盖 99%）
Call Wall 785（弱结构｜现价低于该位 2.2%）
最近结构参考: Flip 770（现价低于该位 0.2%）
量化视角： 负 Gamma（2.99亿，历史分位 50%，中性区）｜由正转负（9.98亿）｜现价位于 Flip 下方 0.22%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考） / 785（Call Wall，弱结构）。
• Gamma 区域：切换参考 770（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-24  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-29  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-24 Forward Structure
存量OI: C 62.3k / P 66.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.38 / P $0.61 ｜ ATM IV 11.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 764 ｜ Call Wall 771（+0.4%）（OI 5.4k） ｜ Put Wall 752（-2.1%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜ATM IV 11.0%｜历史 Rank 34%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 766 ｜ Call Wall 772（+0.5%，弱）（OI 30.3k） ｜ Put Wall 745（-3.0%，弱）（OI 151.5k）

09-28（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 780（+1.6%）（OI 10.8k） ｜ Put Wall 770（+0.3%，弱）（OI 3.5k）

09-29（Activity LOW）仓位参考: Max Pain 766 ｜ Call Wall 771（+0.4%，弱）（OI 1.0k） ｜ Put Wall 748（-2.6%，弱）（OI 2.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/SPY_evening.json