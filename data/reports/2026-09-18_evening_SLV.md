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
🟡 **近现价集中开仓**: 09-21 59P ΔOI +2,301（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-23 55P ΔOI +2,897 占该期限总 OI 14.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 56.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 60.08 → 收盘 59.93（-0.2%） ｜ 今日高 60.37 ｜ 低 59.58 ｜ 昨收 58.97 → 收盘 59.93（+1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.41 | ATM IV 26.8% | Skew 50.8pp | Term 1.36 | ExpMove ±1.7%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常偏陡（Term 1.36）｜保护溢价显著（Skew 50.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-21（3D）±1.7% ｜ 09-23（5D）±2.8% ｜ 09-25（7D）±3.7% ｜ 09-28（10D）±4.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 183,749,054 | GEX Change vs 上次快照 -7,839,673 | Flip: Candidates 56.10 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 825 / LOW 185 / INVALID 506
结构观察区: ≈56（全链重定价，覆盖 79%，CONDITIONAL）
最近结构参考: Flip 56（现价高于该位 6.8%）
量化视角： 正 Gamma（1.84亿，无历史分位）｜正 Gamma 减弱（784万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 56（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 56（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-21  C +6.4k / P +3.6k ｜ Activity HIGH ｜ 3D
09-23  C +4.3k / P +5.1k ｜ Activity HIGH ｜ 5D
09-25  C +5.5k / P +5.6k ｜ Activity HIGH ｜ 7D
09-28  C +0.8k / P +0.4k ｜ Activity HIGH ｜ 10D

📆 09-21 Forward Structure
存量OI: C 17.3k / P 12.5k，今日变化ΔOI: C +6.4k / P +3.6k，平值价格ATM: C $0.50 / P $0.54 ｜ ATM IV 23.5%，净 delta 敞口 14k shares
Top ΔOI: P 59 +2,301
仓位参考: Max Pain 58 ｜ Call Wall 57（-4.9%，弱）（OI 3.3k） ｜ Put Wall 59（-1.6%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 23.5%｜历史 Rank 26%（近端代理）｜IV/RV 0.64×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 13,523 股

📆 09-23 Forward Structure
存量OI: C 7.9k / P 12.6k，今日变化ΔOI: C +4.3k / P +5.1k，平值价格ATM: C $0.81 / P $0.85 ｜ ATM IV 31.0%，净 delta 敞口 49k shares
Top ΔOI: P 55 +2,897 ｜ C 65 +1,962 ｜ P 56 +1,469
仓位参考: Max Pain 59 ｜ Call Wall 65（+8.5%）（OI 2.0k） ｜ Put Wall 55（-8.2%）（OI 4.4k）
量化解读： 存量 Put 重｜ATM IV 31.0%｜历史 Rank 26%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,809 股

📆 09-25 Forward Structure
存量OI: C 98.4k / P 38.2k，今日变化ΔOI: C +5.5k / P +5.6k，平值价格ATM: C $1.07 / P $1.16 ｜ ATM IV 32.8%，净 delta 敞口 33k shares
Top ΔOI: P 55 +1,424 ｜ P 57 +1,266 ｜ P 58 +975
仓位参考: Max Pain 60 ｜ Put Wall 55（-8.2%，弱）（OI 5.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.8%｜历史 Rank 26%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 32,983 股

📆 09-28 Forward Structure
存量OI: C 1.9k / P 1.4k，今日变化ΔOI: C +0.8k / P +0.4k，平值价格ATM: C $1.24 / P $1.21 ｜ ATM IV 30.6%，净 delta 敞口 14k shares
Top ΔOI: C 59 +201 ｜ C 64 +125 ｜ C 62 +95
仓位参考: Max Pain 59 ｜ Call Wall 61（+1.8%，弱）（OI 0.3k） ｜ Put Wall 58（-3.2%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 30.6%｜历史 Rank 26%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 14,024 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/SLV_evening.json