# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 235C ΔOI +641（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 235.76 → 收盘 242.81（+3.0%） ｜ 今日高 248.34 ｜ 低 235.34 ｜ 昨收 232.28 → 收盘 242.81（+4.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 0.63 | ATM IV 85.5% | Skew 7.3pp | Term 0.86 | ExpMove ±7.3%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 7.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±7.3% ｜ 10-16（14D）±10.8% ｜ 10-23（21D）±14.1% ｜ 10-30（28D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 17,401,939 | GEX Change vs 上次快照 -6,593,550 | Flip: Primary Flip: 220.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 444 / LOW 46 / INVALID 208
结构观察区: Primary Flip 220.53（全链重定价，覆盖 82%）
最近结构参考: Flip 221（现价高于该位 10.1%）
量化视角： 正 Gamma（1740万，无历史分位）｜正 Gamma 减弱（659万）｜现价位于 Flip 上方 10.10%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 221（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +1.9k / P +4.0k ｜ Activity HIGH ｜ 7D
10-16  C +2.8k / P +2.9k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.9k / P +0.6k ｜ Activity HIGH ｜ 21D
10-30  C +0.3k / P +1.2k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 32.6k / P 25.0k，今日变化ΔOI: C +1.9k / P +4.0k，平值价格ATM: C $9.10 / P $8.70 ｜ ATM IV 66.4%，净 delta 敞口 38k shares
Top ΔOI: P 210 +808 ｜ C 212 -739 ｜ C 235 +641
仓位参考: Max Pain 222 ｜ Call Wall 242.5（-0.1%）（OI 6.7k） ｜ Put Wall 220（-9.4%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.4%｜历史 Rank 16%（近端代理）｜IV/RV 1.29×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 38,097 股

10-16（MEDIUM △）Top ΔOI: 220P +1,262 ｜ 210P +835
10-16（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 250（+3.0%，弱）（OI 6.0k） ｜ Put Wall 220（-9.4%，弱）（OI 4.5k）

📆 10-23 Forward Structure
存量OI: C 8.0k / P 9.8k，今日变化ΔOI: C +0.9k / P +0.6k，平值价格ATM: C $16.35 / P $17.90 ｜ ATM IV 72.5%，净 delta 敞口 51k shares
Top ΔOI: C 220 +672 ｜ P 220 +196 ｜ C 230 +63
仓位参考: Max Pain 225 ｜ Call Wall 220（-9.4%，弱）（OI 0.9k） ｜ Put Wall 220（-9.4%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.5%｜历史 Rank 16%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 正 50,567 股

📆 10-30 Forward Structure
存量OI: C 10.3k / P 10.4k，今日变化ΔOI: C +0.3k / P +1.2k，平值价格ATM: C $19.20 / P $19.49 ｜ ATM IV 73.4%，净 delta 敞口 -7k shares
Top ΔOI: P 180 +543 ｜ C 275 -383 ｜ C 295 +261
仓位参考: Max Pain 225 ｜ Call Wall 260（+7.1%，弱）（OI 0.5k） ｜ Put Wall 220（-9.4%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 73.4%｜历史 Rank 16%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 负 7,468 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/NBIS_evening.json