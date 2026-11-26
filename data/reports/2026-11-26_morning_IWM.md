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


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 268.87 → 今开 263.23（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 269.77 ｜ 低 260.84

Options: P/C成交量 1.26 | OI比 1.81 | ATM IV 20.0% | Skew 4.7pp | Term 1.17 | ExpMove ±0.0%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常偏陡（Term 1.17）｜保护溢价中性（Skew 4.7pp）｜当日成交偏 Put（P/C量 1.26）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.26×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.81×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（1D）±0.0% ｜ 11-30（4D）±1.8% ｜ 12-01（5D）±2.1% ｜ 12-02（6D）±2.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -716,748,070 | GEX Change vs 上次快照 80,132,408 | Flip: Primary Flip: 283.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1205 / LOW 205 / INVALID 1126
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.80（全链重定价，覆盖 98%）
Put Wall 250（弱结构｜现价高于该位 8.1%）
最近结构参考: Flip 284（现价低于该位 4.8%）
量化视角： 负 Gamma（7.17亿，无历史分位）｜负 Gamma 缓解（+8013万）｜现价位于 Flip 下方 4.81%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（Put Wall，弱结构） / 270（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
12-01  C +0 / P +0 ｜ Activity LOW ｜ 5D
12-02  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 11-27 Forward Structure
存量OI: C 124.0k / P 224.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 20.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 270 ｜ Call Wall 296（+9.6%，弱）（OI 12.1k） ｜ Put Wall 270（-0.1%，弱）（OI 35.0k）
量化解读： 存量 Put 重｜ATM IV 20.2%｜历史 Rank 28%（近端代理）｜IV/RV 0.66×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-30（Activity LOW）仓位参考: Max Pain 269 ｜ Call Wall 276（+2.2%，弱）（OI 3.9k） ｜ Put Wall 260（-3.8%，弱）（OI 8.9k）

12-01（Activity LOW）仓位参考: Max Pain 265 ｜ Call Wall 270（-0.1%，弱）（OI 3.4k） ｜ Put Wall 260（-3.8%）（OI 6.0k）

12-02（Activity LOW）仓位参考: Max Pain 265 ｜ Call Wall 273（+1.1%，弱）（OI 0.6k） ｜ Put Wall 260（-3.8%）（OI 2.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-26/IWM_morning.json