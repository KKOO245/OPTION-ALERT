# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $721.45
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
🟡 **近现价集中开仓**: 09-21 225C ΔOI +4,031（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-23 225C ΔOI +8,539 占该期限总 OI 15.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 209.0）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 219.36 → 收盘 222.27（+1.3%） ｜ 今日高 222.73 ｜ 低 218.04 ｜ 昨收 219.34 → 收盘 222.27（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.45 | OI比 0.90 | ATM IV 27.3% | Skew 22.8pp | Term 1.13 | ExpMove ±1.6%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常（Term 1.13）｜保护溢价显著（Skew 22.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-21（3D）±1.6% ｜ 09-23（5D）±2.5% ｜ 09-25（7D）±3.1% ｜ 09-28（10D）±3.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 644,719,483 | GEX Change vs 上次快照 -52,234,717 | Flip: Candidates 209.00 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 673 / LOW 200 / INVALID 547
结构观察区: ≈209（全链重定价，覆盖 79%，CONDITIONAL）
Call Wall 220（弱结构｜现价高于该位 1.0%）
最近结构参考: Call Wall 220（现价高于该位 1.0%）
量化视角： 正 Gamma（6.45亿，无历史分位）｜正 Gamma 减弱（5223万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 205（MaxPain，仅结算参考） / 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 209（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-21  C +12.6k / P +5.2k ｜ Activity HIGH ｜ 3D
09-23  C +13.6k / P +5.6k ｜ Activity HIGH ｜ 5D
09-25  C +42.8k / P +52.3k ｜ Activity HIGH ｜ 7D
09-28  C +2.6k / P +2.0k ｜ Activity HIGH ｜ 10D

📆 09-21 Forward Structure
存量OI: C 53.0k / P 47.4k，今日变化ΔOI: C +12.6k / P +5.2k，平值价格ATM: C $1.52 / P $1.96 ｜ ATM IV 21.4%，净 delta 敞口 300k shares
Top ΔOI: C 225 +4,031 ｜ C 220 +2,571 ｜ P 217 +1,852
仓位参考: Max Pain 215 ｜ Call Wall 225（+1.2%，弱）（OI 7.1k） ｜ Put Wall 210（-5.5%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜ATM IV 21.4%｜历史 Rank 4%（近端代理）｜IV/RV 0.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 299,747 股

📆 09-23 Forward Structure
存量OI: C 38.4k / P 17.7k，今日变化ΔOI: C +13.6k / P +5.6k，平值价格ATM: C $2.57 / P $3.07 ｜ ATM IV 27.3%，净 delta 敞口 387k shares
Top ΔOI: C 225 +8,539 ｜ C 227 +1,824 ｜ P 205 +1,788
仓位参考: Max Pain 215 ｜ Call Wall 225（+1.2%，弱）（OI 10.7k） ｜ Put Wall 205（-7.8%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 27.3%｜历史 Rank 4%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 386,508 股

📆 09-25 Forward Structure
存量OI: C 287.3k / P 224.3k，今日变化ΔOI: C +42.8k / P +52.3k，平值价格ATM: C $3.25 / P $3.62 ｜ ATM IV 28.0%，净 delta 敞口 560k shares
Top ΔOI: C 222 +18,572 ｜ C 220 -16,846
仓位参考: Max Pain 218 ｜ Call Wall 225（+1.2%，弱）（OI 31.1k） ｜ Put Wall 210（-5.5%，弱）（OI 27.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 28.0%｜历史 Rank 4%（近端代理）｜IV/RV 0.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 559,883 股

📆 09-28 Forward Structure
存量OI: C 16.5k / P 12.6k，今日变化ΔOI: C +2.6k / P +2.0k，平值价格ATM: C $3.78 / P $4.05 ｜ ATM IV 26.5%，净 delta 敞口 57k shares
Top ΔOI: C 225 +775 ｜ C 222 +765 ｜ C 230 +427
仓位参考: Max Pain 215 ｜ Call Wall 225（+1.2%）（OI 4.3k） ｜ Put Wall 205（-7.8%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 26.5%｜历史 Rank 4%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 正 57,113 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/NVDA_evening.json