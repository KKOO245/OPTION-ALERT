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
🟡 **近现价集中开仓**: 10-09 197C ΔOI +5,042（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 193.24 → 收盘 188.75（-2.3%） ｜ 今日高 194.78 ｜ 低 188.26 ｜ 昨收 190.04 → 收盘 188.75（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 0.70 | ATM IV 50.6% | Skew 19.0pp | Term 0.83 | ExpMove ±4.3%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价显著（Skew 19.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±4.3% ｜ 10-16（14D）±6.2% ｜ 10-23（21D）±7.5% ｜ 10-30（28D）±9.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 58,556,064 | GEX Change vs 上次快照 -26,800,266 | Flip: Primary Flip: 171.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 81%（带内） ｜ IV 有效性: VALID 483 / LOW 101 / INVALID 252
结构观察区: Primary Flip 171.60（全链重定价，覆盖 81%）
Put Wall 170（弱结构｜现价高于该位 11.0%） | Call Wall 200（现价低于该位 5.6%）
最近结构参考: Call Wall 200（现价低于该位 5.6%）
量化视角： 正 Gamma（5856万，无历史分位）｜正 Gamma 减弱（2680万）｜现价位于 Flip 上方 9.99%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 185（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 172（全链重定价，覆盖 81%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +23.7k / P +6.9k ｜ Activity HIGH ｜ 7D
10-16  C +2.0k / P -0.4k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.3k / P +1.0k ｜ Activity HIGH ｜ 21D
10-30  C +1.2k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 60.3k / P 51.8k，今日变化ΔOI: C +23.7k / P +6.9k，平值价格ATM: C $4.77 / P $3.35 ｜ ATM IV 38.5%，净 delta 敞口 229k shares
Top ΔOI: C 197 +5,042 ｜ C 205 +4,744 ｜ C 195 +4,129
仓位参考: Max Pain 188 ｜ Call Wall 200（+6.0%，弱）（OI 6.8k） ｜ Put Wall 190（+0.7%，弱）（OI 5.8k）
量化解读： 存量两侧均衡｜ATM IV 38.5%｜历史 Rank 48%（近端代理）｜IV/RV 1.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 228,976 股

10-16（MEDIUM △）Top ΔOI: 205C -620
10-16（MEDIUM △）仓位参考: Max Pain 168 ｜ Call Wall 200（+6.0%，弱）（OI 15.4k） ｜ Put Wall 170（-9.9%，弱）（OI 14.9k）

📆 10-23 Forward Structure
存量OI: C 21.2k / P 15.2k，今日变化ΔOI: C +0.3k / P +1.0k，平值价格ATM: C $8.00 / P $6.15 ｜ ATM IV 40.6%，净 delta 敞口 -9k shares
Top ΔOI: P 175 +193
仓位参考: Max Pain 180 ｜ Call Wall 180（-4.6%）（OI 4.6k） ｜ Put Wall 175（-7.3%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.6%｜历史 Rank 48%（近端代理）｜IV/RV 1.66×（近似）｜净 delta 敞口 负 8,724 股

📆 10-30 Forward Structure
存量OI: C 21.9k / P 15.8k，今日变化ΔOI: C +1.2k / P +0.5k，平值价格ATM: C $9.50 / P $7.90 ｜ ATM IV 41.8%，净 delta 敞口 14k shares
Top ΔOI: P 185 +199
仓位参考: Max Pain 180 ｜ Call Wall 200（+6.0%，弱）（OI 2.2k） ｜ Put Wall 170（-9.9%）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 41.8%｜历史 Rank 48%（近端代理）｜IV/RV 1.71×（近似）｜净 delta 敞口 正 14,023 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/PLTR_evening.json