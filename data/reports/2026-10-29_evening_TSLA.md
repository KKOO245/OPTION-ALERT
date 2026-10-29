# 期权晚报 2026-10-29（快照 16:40 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 410C ΔOI +2,974（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 405.93 → 收盘 403.30（-0.6%） ｜ 今日高 406.98 ｜ 低 400.50 ｜ 昨收 404.22 → 收盘 403.30（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.77 | OI比 1.22 | ATM IV 39.8% | Skew 0.2pp | Term 0.92 | ExpMove ±1.7%（近端） | Rank 11%
量化视角： IV 历史低位（Rank 11%，期权偏便宜）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 0.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.22×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±1.7% ｜ 11-02（4D）±2.6% ｜ 11-04（6D）±3.8% ｜ 11-06（8D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 133,878,262 | GEX Change vs 上次快照 499,057 | Flip: Primary Flip: 383.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1352 / LOW 136 / INVALID 754
结构观察区: Primary Flip 383.91（全链重定价，覆盖 97%）
Call Wall 420（弱结构｜现价低于该位 4.0%）
最近结构参考: Call Wall 420（现价低于该位 4.0%）
量化视角： 正 Gamma（1.34亿，无历史分位）｜正 Gamma 增强（+50万）｜现价位于 Flip 上方 5.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 382（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 384（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +19.0k / P +19.3k ｜ Activity HIGH ｜ 1D
11-02  C +11.4k / P +5.7k ｜ Activity HIGH ｜ 4D
11-04  C +2.2k / P +2.6k ｜ Activity HIGH ｜ 6D
11-06  C +3.3k / P +16.1k ｜ Activity HIGH ｜ 8D

📆 10-30 Forward Structure
存量OI: C 223.6k / P 272.7k，今日变化ΔOI: C +19.0k / P +19.3k，平值价格ATM: C $3.83 / P $2.91 ｜ ATM IV 39.8%，净 delta 敞口 128k shares
Top ΔOI: C 410 +2,974 ｜ C 405 +2,969
仓位参考: Max Pain 382 ｜ Call Wall 420（+4.1%）（OI 24.1k） ｜ Put Wall 380（-5.8%，弱）（OI 9.2k）
量化解读： 存量 Put 重｜ATM IV 39.8%｜历史 Rank 11%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 127,716 股

📆 11-02 Forward Structure
存量OI: C 49.6k / P 21.7k，今日变化ΔOI: C +11.4k / P +5.7k，平值价格ATM: C $5.70 / P $4.70 ｜ ATM IV 30.8%，净 delta 敞口 104k shares
Top ΔOI: C 410 +2,320
仓位参考: Max Pain 395 ｜ Call Wall 410（+1.7%，弱）（OI 3.5k） ｜ Put Wall 400（-0.8%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 30.8%｜历史 Rank 11%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 104,288 股

📆 11-04 Forward Structure
存量OI: C 11.1k / P 9.9k，今日变化ΔOI: C +2.2k / P +2.6k，平值价格ATM: C $8.35 / P $7.03 ｜ ATM IV 36.7%，净 delta 敞口 -26k shares
Top ΔOI: P 400 +1,422 ｜ C 440 +317 ｜ P 390 +308
仓位参考: Max Pain 400 ｜ Call Wall 410（+1.7%，弱）（OI 1.5k） ｜ Put Wall 400（-0.8%）（OI 2.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.7%｜历史 Rank 11%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 负 26,381 股

📆 11-06 Forward Structure
存量OI: C 61.2k / P 81.1k，今日变化ΔOI: C +3.3k / P +16.1k，平值价格ATM: C $9.90 / P $8.60 ｜ ATM IV 38.4%，净 delta 敞口 12k shares
Top ΔOI: P 400 +1,491
仓位参考: Max Pain 385 ｜ Call Wall 420（+4.1%，弱）（OI 4.8k） ｜ Put Wall 400（-0.8%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 38.4%｜历史 Rank 11%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 正 11,622 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 39.8% vs 11-02 30.8%（差 +9.0pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/TSLA_evening.json