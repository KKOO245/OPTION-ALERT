# 期权晨报 2026-11-26（快照 10:20 ET）

📊 市场环境

SPY $720.30 ｜ QQQ $633.93
VIX 26.96 ↓4.7%（5D -5.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 103.72 → 今开 98.12（-5.4%） | 较昨收变动（含盘初走势） ｜ 今日高 104.31 ｜ 低 94.88

Options: P/C成交量 0.31 | OI比 0.61 | ATM IV 71.5% | Skew 4.6pp | Term 1.10 | ExpMove ±4.8%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 1.10）｜保护溢价中性（Skew 4.6pp）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（1D）±4.8% ｜ 12-04（8D）±10.7% ｜ 12-11（15D）±14.2% ｜ 12-18（22D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,650,968 | GEX Change vs 上次快照 9,258,427 | Flip: Primary Flip: 106.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 439 / LOW 240 / INVALID 311
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 106.50（全链重定价，覆盖 94%）
Put Wall 110（弱结构｜现价低于该位 3.5%）
最近结构参考: Flip 106（现价低于该位 0.3%）
量化视角： 负 Gamma（165万，无历史分位）｜负 Gamma 缓解（+926万）｜现价位于 Flip 下方 0.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 110（Put Wall，弱结构） / 109（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 106（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 8D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 15D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 11-27 Forward Structure
存量OI: C 64.8k / P 39.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.28 / P $3.76 ｜ ATM IV 71.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 109 ｜ Call Wall 114（+7.4%，弱）（OI 7.3k） ｜ Put Wall 114（+7.4%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 71.5%｜历史 Rank 36%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

12-04（Activity LOW）仓位参考: Max Pain 122 ｜ Put Wall 113（+6.4%，弱）（OI 1.6k）

12-11（Activity LOW）仓位参考: Max Pain 120 ｜ Call Wall 110（+3.6%，弱）（OI 0.3k） ｜ Put Wall 100（-5.8%，弱）（OI 0.7k）

12-18（Activity LOW）仓位参考: Max Pain 130 ｜ Put Wall 110（+3.6%）（OI 7.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-26/COIN_morning.json