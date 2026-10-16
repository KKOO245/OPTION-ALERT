# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-19 49P ΔOI +1,521（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 48P ΔOI +2,573 占该期限总 OI 12.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 50.4）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 51.85 → 收盘 51.51（-0.7%） ｜ 今日高 52.33 ｜ 低 51.36 ｜ 昨收 51.92 → 收盘 51.51（-0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.70 | OI比 0.32 | ATM IV 36.1% | Skew 28.7pp | Term 0.98 | ExpMove ±1.8%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 0.98）｜保护溢价显著（Skew 28.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±1.8% ｜ 10-21（5D）±2.8% ｜ 10-23（7D）±3.5% ｜ 10-26（10D）±4.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,849,746 | GEX Change vs 上次快照 -63,204,930 | Flip: Candidates 50.37 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 651 / LOW 137 / INVALID 460
结构观察区: ≈50（全链重定价，覆盖 77%，CONDITIONAL）
Put Wall 50（弱结构｜现价高于该位 3.0%）
最近结构参考: Flip 50（现价高于该位 2.3%）
量化视角： 正 Gamma（2785万，无历史分位）｜正 Gamma 减弱（6320万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 52（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 77%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +2.6k / P +3.3k ｜ Activity HIGH ｜ 3D
10-21  C +1.6k / P +3.3k ｜ Activity HIGH ｜ 5D
10-23  C +4.5k / P +7.7k ｜ Activity HIGH ｜ 7D
10-26  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 10D

📆 10-19 Forward Structure
存量OI: C 11.6k / P 9.4k，今日变化ΔOI: C +2.6k / P +3.3k，平值价格ATM: C $0.45 / P $0.48 ｜ ATM IV 24.2%，净 delta 敞口 23k shares
Top ΔOI: P 49 +1,521 ｜ C 53 +979 ｜ C 52 +601
仓位参考: Max Pain 52 ｜ Call Wall 53（+2.9%，弱）（OI 1.5k） ｜ Put Wall 49（-4.9%）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 24.2%｜历史 Rank 58%（近端代理）｜IV/RV 0.62×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 22,588 股

📆 10-21 Forward Structure
存量OI: C 11.6k / P 8.5k，今日变化ΔOI: C +1.6k / P +3.3k，平值价格ATM: C $0.72 / P $0.72 ｜ ATM IV 30.1%，净 delta 敞口 -8k shares
Top ΔOI: P 48 +2,573 ｜ C 52 +517 ｜ C 54 +371
仓位参考: Max Pain 51 ｜ Call Wall 51（-1.0%，弱）（OI 0.9k） ｜ Put Wall 48（-6.8%）（OI 2.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.1%｜历史 Rank 58%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,104 股

📆 10-23 Forward Structure
存量OI: C 61.9k / P 48.2k，今日变化ΔOI: C +4.5k / P +7.7k，平值价格ATM: C $0.94 / P $0.88 ｜ ATM IV 32.1%，净 delta 敞口 11k shares
Top ΔOI: P 51 +2,996 ｜ C 52 +2,715 ｜ P 47 +2,092
仓位参考: Max Pain 54 ｜ Call Wall 55（+6.8%，弱）（OI 4.9k） ｜ Put Wall 50（-2.9%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.1%｜历史 Rank 58%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,394 股

📆 10-26 Forward Structure
存量OI: C 3.2k / P 2.5k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $1.08 / P $0.99 ｜ ATM IV 29.9%，净 delta 敞口 -5k shares
Top ΔOI: P 50 +273 ｜ C 55 +131
仓位参考: Max Pain 50 ｜ Call Wall 50.5（-2.0%）（OI 1.4k） ｜ Put Wall 49（-4.9%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 29.9%｜历史 Rank 58%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 负 5,283 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/SLV_evening.json