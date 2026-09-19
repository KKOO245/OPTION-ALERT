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
🟡 **近现价集中开仓**: 09-25 185C ΔOI +1,965（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 165.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 178.15 → 收盘 194.25（+9.0%） ｜ 今日高 196.21 ｜ 低 177.67 ｜ 昨收 173.97 → 收盘 194.25（+11.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.51 | ATM IV 78.8% | Skew -6.3pp | Term 0.81 | ExpMove ±7.2%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±7.2% ｜ 10-02（14D）±10.0% ｜ 10-09（21D）±13.0% ｜ 10-16（28D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 26,949,688 | GEX Change vs 上次快照 -11,217,810 | Flip: Candidates 165.14 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 65%（带内） ｜ IV 有效性: VALID 404 / LOW 109 / INVALID 479
结构观察区: ≈165（全链重定价，覆盖 65%，CONDITIONAL）
Call Wall 200（弱结构｜现价低于该位 2.9%）
最近结构参考: Call Wall 200（现价低于该位 2.9%）
量化视角： 正 Gamma（2695万，无历史分位）｜正 Gamma 减弱（1122万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 172（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 65%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +8.5k / P +2.1k ｜ Activity HIGH ｜ 7D
10-02  C +1.4k / P +0.9k ｜ Activity HIGH ｜ 14D
10-09  C +0.5k / P +45 ｜ Activity MEDIUM △ ｜ 21D
10-16  C +0.7k / P +1.1k ｜ Activity MEDIUM △ ｜ 28D

📆 09-25 Forward Structure
存量OI: C 31.7k / P 20.5k，今日变化ΔOI: C +8.5k / P +2.1k，平值价格ATM: C $6.67 / P $7.30 ｜ ATM IV 64.3%，净 delta 敞口 656k shares
Top ΔOI: C 177 +2,349 ｜ C 185 +1,965 ｜ C 175 +1,323
仓位参考: Max Pain 172 ｜ Call Wall 185（-4.8%）（OI 4.3k） ｜ Put Wall 180（-7.3%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 64.3%｜历史 Rank 57%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 656,462 股

📆 10-02 Forward Structure
存量OI: C 13.6k / P 18.0k，今日变化ΔOI: C +1.4k / P +0.9k，平值价格ATM: C $9.56 / P $9.93 ｜ ATM IV 64.2%，净 delta 敞口 93k shares
Top ΔOI: C 175 +202 ｜ C 190 +201
仓位参考: Max Pain 182 ｜ Call Wall 187.5（-3.5%，弱）（OI 1.3k） ｜ Put Wall 187.5（-3.5%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.2%｜历史 Rank 57%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 92,639 股

10-09（MEDIUM △）Top ΔOI: 180C +133 ｜ 182C +50
10-09（MEDIUM △）仓位参考: Max Pain 182 ｜ Call Wall 185（-4.8%，弱）（OI 0.2k） ｜ Put Wall 187.5（-3.5%，弱）（OI 0.4k）

10-16（MEDIUM △）Top ΔOI: 195C +292
10-16（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 200（+3.0%，弱）（OI 5.5k） ｜ Put Wall 200（+3.0%，弱）（OI 2.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/COIN_evening.json