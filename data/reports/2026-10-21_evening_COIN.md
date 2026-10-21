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
🟡 **近现价集中开仓**: 10-23 175C ΔOI +738（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 175.00 → 收盘 177.08（+1.2%） ｜ 今日高 180.60 ｜ 低 172.04 ｜ 昨收 170.85 → 收盘 177.08（+3.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 0.62 | ATM IV 70.0% | Skew -0.1pp | Term 0.97 | ExpMove ±4.2%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±4.2% ｜ 10-30（9D）±10.3% ｜ 11-06（16D）±11.8% ｜ 11-13（23D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 21,954,193 | GEX Change vs 上次快照 7,927,736 | Flip: Primary Flip: 166.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 478 / LOW 128 / INVALID 236
结构观察区: Primary Flip 166.27（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价高于该位 4.2%）
最近结构参考: Call Wall 170（现价高于该位 4.2%）
量化视角： 正 Gamma（2195万，无历史分位）｜正 Gamma 增强（+793万）｜现价位于 Flip 上方 6.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 175（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +6.4k / P +0.6k ｜ Activity HIGH ｜ 2D
10-30  C +0.5k / P +1.2k ｜ Activity HIGH ｜ 9D
11-06  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
11-13  C +0.4k / P +0.5k ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 66.9k / P 41.4k，今日变化ΔOI: C +6.4k / P +0.6k，平值价格ATM: C $3.50 / P $3.85 ｜ ATM IV 70.0%，净 delta 敞口 193k shares
Top ΔOI: C 190 +3,279 ｜ C 175 +738 ｜ C 180 +713
仓位参考: Max Pain 175 ｜ Call Wall 180（+1.6%，弱）（OI 7.8k）
量化解读： 存量 Call 重｜ATM IV 70.0%｜历史 Rank 33%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 正 193,414 股

📆 10-30 Forward Structure
存量OI: C 17.8k / P 18.6k，今日变化ΔOI: C +0.5k / P +1.2k，平值价格ATM: C $9.40 / P $8.89 ｜ ATM IV 80.9%，净 delta 敞口 4k shares
Top ΔOI: P 167 +250 ｜ P 170 +131
仓位参考: Max Pain 180 ｜ Call Wall 185（+4.5%，弱）（OI 1.8k） ｜ Put Wall 170（-4.0%，弱）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 80.9%｜历史 Rank 33%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,272 股

11-06（MEDIUM △）Top ΔOI: 175P +96 ｜ 180C +93
11-06（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（-1.2%，弱）（OI 0.3k）

📆 11-13 Forward Structure
存量OI: C 5.4k / P 7.6k，今日变化ΔOI: C +0.4k / P +0.5k，平值价格ATM: C $13.10 / P $12.23 ｜ ATM IV 73.0%，净 delta 敞口 4k shares
Top ΔOI: P 160 +311 ｜ C 190 +126 ｜ C 172 +103
仓位参考: Max Pain 178 ｜ Call Wall 177.5（+0.2%）（OI 1.1k） ｜ Put Wall 160（-9.6%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 73.0%｜历史 Rank 33%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 正 3,924 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/COIN_evening.json