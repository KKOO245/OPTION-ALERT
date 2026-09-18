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
🟡 **近现价集中开仓**: 10-02 160C ΔOI +872（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 136.58 → 收盘 153.92（+12.7%） ｜ 今日高 154.02 ｜ 低 136.43 ｜ 昨收 132.25 → 收盘 153.92（+16.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.59 | ATM IV 78.0% | Skew -2.3pp | Term 0.89 | ExpMove ±7.9%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（7D）±7.9% ｜ 10-02（14D）±11.0% ｜ 10-09（21D）±13.4% ｜ 10-16（28D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,641,614 | GEX Change vs 上次快照 -83,099,980 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 55%（带内） ｜ IV 有效性: VALID 705 / LOW 63 / INVALID 436
结构观察区: NO_CROSS
量化视角： 正 Gamma（3664万，无历史分位）｜正 Gamma 减弱（8310万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +29.7k / P +18.8k ｜ Activity HIGH ｜ 7D
10-02  C +0.7k / P +4.7k ｜ Activity HIGH ｜ 14D
10-09  C +1.0k / P +3.1k ｜ Activity HIGH ｜ 21D
10-16  C +2.4k / P +1.5k ｜ Activity MEDIUM △ ｜ 28D

📆 09-25 Forward Structure
存量OI: C 68.7k / P 83.5k，今日变化ΔOI: C +29.7k / P +18.8k，平值价格ATM: C $5.60 / P $6.55 ｜ ATM IV 70.6%，净 delta 敞口 2.4M shares
Top ΔOI: C 141 +11,861 ｜ C 135 +9,609
仓位参考: Max Pain 129 ｜ Call Wall 141（-8.4%，弱）（OI 12.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.6%｜历史 Rank 44%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,432,851 股

📆 10-02 Forward Structure
存量OI: C 27.2k / P 49.0k，今日变化ΔOI: C +0.7k / P +4.7k，平值价格ATM: C $8.03 / P $8.85 ｜ ATM IV 69.8%，净 delta 敞口 71k shares
Top ΔOI: C 160 +872
仓位参考: Max Pain 130 ｜ Call Wall 145（-5.8%，弱）（OI 2.9k） ｜ Put Wall 140（-9.0%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 69.8%｜历史 Rank 44%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 71,473 股

📆 10-09 Forward Structure
存量OI: C 9.7k / P 29.1k，今日变化ΔOI: C +1.0k / P +3.1k，平值价格ATM: C $9.95 / P $10.65 ｜ ATM IV 69.6%，净 delta 敞口 46k shares
仓位参考: Max Pain 135 ｜ Call Wall 150（-2.5%，弱）（OI 1.2k） ｜ Put Wall 140（-9.0%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 69.6%｜历史 Rank 44%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 正 45,654 股

10-16（MEDIUM △）Top ΔOI: 145C +532 ｜ 130P +430
10-16（MEDIUM △）仓位参考: Max Pain 100 ｜ Call Wall 150（-2.5%，弱）（OI 9.4k） ｜ Put Wall 140（-9.0%，弱）（OI 2.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/MSTR_evening.json