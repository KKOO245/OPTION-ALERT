# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 157C ΔOI -2,946（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 146.20 → 收盘 153.48（+5.0%） ｜ 今日高 155.69 ｜ 低 143.93 ｜ 昨收 142.72 → 收盘 153.48（+7.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.75 | OI比 0.78 | ATM IV 77.3% | Skew -1.8pp | Term 0.89 | ExpMove ±4.6%（近端） | Rank 45%
量化视角： IV 中性（Rank 45%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±4.6% ｜ 10-30（9D）±9.1% ｜ 11-06（16D）±12.2% ｜ 11-13（23D）±14.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 78,167,930 | GEX Change vs 上次快照 11,340,301 | Flip: Primary Flip: 134.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 655 / LOW 78 / INVALID 171
结构观察区: Primary Flip 134.72（全链重定价，覆盖 100%）
最近结构参考: Flip 135（现价高于该位 13.9%）
量化视角： 正 Gamma（7817万，无历史分位）｜正 Gamma 增强（+1134万）｜现价位于 Flip 上方 13.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C -1.5k / P +4.6k ｜ Activity MEDIUM △ ｜ 2D
10-30  C +3.4k / P +9.1k ｜ Activity HIGH ｜ 9D
11-06  C +0.9k / P +3.9k ｜ Activity HIGH ｜ 16D
11-13  C +1.0k / P +4.4k ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 228.8k / P 179.0k，今日变化ΔOI: C -1.5k / P +4.6k，平值价格ATM: C $4.05 / P $3.05 ｜ ATM IV 77.3%，净 delta 敞口 -289k shares
Top ΔOI: C 157 -2,946 ｜ C 155 +2,869 ｜ C 147 -2,605
仓位参考: Max Pain 141 ｜ Call Wall 155（+1.0%，弱）（OI 29.2k） ｜ Put Wall 140（-8.8%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.3%｜历史 Rank 45%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 289,289 股

📆 10-30 Forward Structure
存量OI: C 50.5k / P 87.1k，今日变化ΔOI: C +3.4k / P +9.1k，平值价格ATM: C $7.60 / P $6.39 ｜ ATM IV 73.0%，净 delta 敞口 176k shares
Top ΔOI: P 120 +1,917 ｜ C 150 +936
仓位参考: Max Pain 155 ｜ Call Wall 160（+4.2%，弱）（OI 3.5k） ｜ Put Wall 155（+1.0%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 73.0%｜历史 Rank 45%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 176,068 股

📆 11-06 Forward Structure
存量OI: C 14.7k / P 32.9k，今日变化ΔOI: C +0.9k / P +3.9k，平值价格ATM: C $9.90 / P $8.85 ｜ ATM IV 71.5%，净 delta 敞口 -12k shares
仓位参考: Max Pain 160 ｜ Call Wall 160（+4.2%）（OI 2.0k） ｜ Put Wall 160（+4.2%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜ATM IV 71.5%｜历史 Rank 45%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 12,365 股

📆 11-13 Forward Structure
存量OI: C 13.1k / P 27.4k，今日变化ΔOI: C +1.0k / P +4.4k，平值价格ATM: C $11.78 / P $9.80 ｜ ATM IV 70.2%，净 delta 敞口 -6k shares
仓位参考: Max Pain 160 ｜ Call Wall 167.5（+9.1%，弱）（OI 1.2k） ｜ Put Wall 160（+4.2%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 70.2%｜历史 Rank 45%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 负 6,476 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/MSTR_evening.json