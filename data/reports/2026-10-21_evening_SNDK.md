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
🟡 **近现价集中开仓**: 10-30 1350C ΔOI +306（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,417.00 → 收盘 1,378.22（-2.7%） ｜ 今日高 1424.48 ｜ 低 1327.62 ｜ 昨收 1,365.38 → 收盘 1,378.22（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.59 | OI比 0.83 | ATM IV 79.3% | Skew 1.1pp | Term 0.92 | ExpMove ±4.7%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 0.92）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±4.7% ｜ 10-30（9D）±11.4% ｜ 11-06（16D）±13.6% ｜ 11-13（23D）±15.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 77,044 | GEX Change vs 上次快照 1,271,239 | Flip: Primary Flip: 1377.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1916 / LOW 469 / INVALID 1069
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1377.41（全链重定价，覆盖 99%）
Call Wall 1,500（现价低于该位 8.1%）
最近结构参考: Flip 1377（现价高于该位 0.1%）
量化视角： 正 Gamma（8万，无历史分位）｜由负转正（+127万）｜现价位于 Flip 上方 0.06%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,405（MaxPain，仅结算参考） / 1,500（Call Wall）。
• Gamma 区域：切换参考 1377（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +3.8k / P +1.8k ｜ Activity HIGH ｜ 2D
10-30  C +1.3k / P +0.9k ｜ Activity HIGH ｜ 9D
11-06  C +0.5k / P +78 ｜ Activity MEDIUM △ ｜ 16D
11-13  C +0.4k / P -49 ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 47.1k / P 39.1k，今日变化ΔOI: C +3.8k / P +1.8k，平值价格ATM: C $32.40 / P $32.55 ｜ ATM IV 79.3%，净 delta 敞口 191k shares
Top ΔOI: C 1500 +280
仓位参考: Max Pain 1,405 ｜ Call Wall 1500（+8.8%）（OI 3.2k） ｜ Put Wall 1250（-9.3%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 79.3%｜历史 Rank 38%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 191,197 股

📆 10-30 Forward Structure
存量OI: C 26.1k / P 17.2k，今日变化ΔOI: C +1.3k / P +0.9k，平值价格ATM: C $78.55 / P $79.20 ｜ ATM IV 90.6%，净 delta 敞口 19k shares
Top ΔOI: C 1350 +306
仓位参考: Max Pain 1,500 ｜ Call Wall 1500（+8.8%，弱）（OI 1.4k） ｜ Put Wall 1400（+1.6%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 90.6%｜历史 Rank 38%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,603 股

11-06（MEDIUM △）Top ΔOI: 1040P -122 ｜ 1280P +52
11-06（MEDIUM △）仓位参考: Max Pain 1,500 ｜ Call Wall 1400（+1.6%，弱）（OI 0.7k） ｜ Put Wall 1400（+1.6%，弱）（OI 0.4k）

📆 11-13 Forward Structure
存量OI: C 4.2k / P 3.9k，今日变化ΔOI: C +0.4k / P -49，平值价格ATM: C $113.00 / P $101.59 ｜ ATM IV 76.2%，净 delta 敞口 2k shares
Top ΔOI: P 1040 -121 ｜ P 1280 +45
仓位参考: Max Pain 1,500 ｜ Call Wall 1480（+7.4%，弱）（OI 0.2k） ｜ Put Wall 1300（-5.7%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 76.2%｜历史 Rank 38%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 正 2,065 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/SNDK_evening.json