# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $nan
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-21 375C ΔOI +1,732（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 350.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 369.28 → 收盘 364.27（-1.4%） ｜ 今日高 370.90 ｜ 低 360.75 ｜ 昨收 366.20 → 收盘 364.27（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.68 | OI比 0.81 | ATM IV 26.6% | Skew 10.8pp | Term 1.49 | ExpMove ±1.9%（近端） | Rank 1%
量化视角： IV 历史低位（Rank 1%，期权偏便宜）｜期限结构正常偏陡（Term 1.49）｜保护溢价显著（Skew 10.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-21（3D）±1.9% ｜ 09-23（5D）±3.2% ｜ 09-25（7D）±4.0% ｜ 09-28（10D）±4.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 106,998,271 | GEX Change vs 上次快照 41,780,317 | Flip: Candidates 350.09 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 1128 / LOW 117 / INVALID 755
结构观察区: ≈350（全链重定价，覆盖 76%，CONDITIONAL）
Call Wall 400（弱结构｜现价低于该位 8.9%）
最近结构参考: Flip 350（现价高于该位 4.0%）
量化视角： 正 Gamma（1.07亿，无历史分位）｜正 Gamma 增强（+4178万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 350（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-21  C +9.1k / P +9.1k ｜ Activity HIGH ｜ 3D
09-23  C +3.8k / P +3.1k ｜ Activity HIGH ｜ 5D
09-25  C +12.4k / P +33.8k ｜ Activity HIGH ｜ 7D
09-28  C +2.1k / P +1.1k ｜ Activity HIGH ｜ 10D

📆 09-21 Forward Structure
存量OI: C 33.1k / P 29.9k，今日变化ΔOI: C +9.1k / P +9.1k，平值价格ATM: C $3.18 / P $3.85 ｜ ATM IV 26.5%，净 delta 敞口 -61k shares
Top ΔOI: C 375 +1,732
仓位参考: Max Pain 365 ｜ Call Wall 400（+9.8%）（OI 5.3k） ｜ Put Wall 350（-3.9%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 26.5%｜历史 Rank 1%（近端代理）｜IV/RV 0.59×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 61,499 股

📆 09-23 Forward Structure
存量OI: C 16.4k / P 13.0k，今日变化ΔOI: C +3.8k / P +3.1k，平值价格ATM: C $5.55 / P $6.10 ｜ ATM IV 34.2%，净 delta 敞口 -71k shares
Top ΔOI: P 365 +857 ｜ P 370 +734 ｜ C 367 +470
仓位参考: Max Pain 365 ｜ Call Wall 400（+9.8%，弱）（OI 1.5k） ｜ Put Wall 330（-9.4%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 34.2%｜历史 Rank 1%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 负 70,529 股

📆 09-25 Forward Structure
存量OI: C 95.4k / P 111.1k，今日变化ΔOI: C +12.4k / P +33.8k，平值价格ATM: C $7.20 / P $7.55 ｜ ATM IV 36.6%，净 delta 敞口 -48k shares
仓位参考: Max Pain 360 ｜ Call Wall 400（+9.8%，弱）（OI 8.0k） ｜ Put Wall 350（-3.9%，弱）（OI 4.2k）
量化解读： 存量两侧均衡｜ATM IV 36.6%｜历史 Rank 1%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 47,995 股

📆 09-28 Forward Structure
存量OI: C 6.2k / P 3.4k，今日变化ΔOI: C +2.1k / P +1.1k，平值价格ATM: C $8.23 / P $8.60 ｜ ATM IV 34.5%，净 delta 敞口 -5k shares
Top ΔOI: C 400 +370 ｜ C 390 +308
仓位参考: Max Pain 360 ｜ Call Wall 400（+9.8%）（OI 0.9k） ｜ Put Wall 355（-2.5%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 34.5%｜历史 Rank 1%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 负 5,308 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/TSLA_evening.json