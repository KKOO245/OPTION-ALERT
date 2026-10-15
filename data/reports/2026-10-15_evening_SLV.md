# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 42.2% vs 10-19 29.5%（差 +12.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 51C ΔOI +4,377（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 51.25 → 收盘 51.92（+1.3%） ｜ 今日高 51.94 ｜ 低 50.97 ｜ 昨收 50.22 → 收盘 51.92（+3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.91 | OI比 0.37 | ATM IV 42.2% | Skew 3.0pp | Term 0.83 | ExpMove ±1.8%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 3.0pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.37）+ 当日成交偏 Put（P/C量 1.91）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.91×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±1.8% ｜ 10-19（4D）±2.5% ｜ 10-21（6D）±3.2% ｜ 10-23（8D）±3.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 35,141,278 | GEX Change vs 上次快照 3,520,607 | Flip: Primary Flip: 50.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 803 / LOW 147 / INVALID 298
结构观察区: Primary Flip 50.11（全链重定价，覆盖 97%）
Put Wall 50（弱结构｜现价高于该位 3.8%）
最近结构参考: Flip 50（现价高于该位 3.6%）
量化视角： 正 Gamma（3514万，无历史分位）｜正 Gamma 增强（+352万）｜现价位于 Flip 上方 3.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 55（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 50（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +15.5k / P -15.7k ｜ Activity HIGH ｜ 1D
10-19  C +3.1k / P +2.8k ｜ Activity HIGH ｜ 4D
10-21  C +4.3k / P +2.7k ｜ Activity HIGH ｜ 6D
10-23  C +12.4k / P +5.4k ｜ Activity HIGH ｜ 8D

📆 10-16 Forward Structure
存量OI: C 490.5k / P 180.8k，今日变化ΔOI: C +15.5k / P -15.7k，平值价格ATM: C $0.44 / P $0.49 ｜ ATM IV 42.2%，净 delta 敞口 3.0M shares
Top ΔOI: P 59 -6,746 ｜ P 60 -6,638 ｜ C 51 +4,377
仓位参考: Max Pain 55 ｜ Call Wall 50（-3.7%，弱）（OI 27.9k） ｜ Put Wall 50（-3.7%，弱）（OI 24.0k）
量化解读： 存量 Call 重｜ATM IV 42.2%｜历史 Rank 71%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,958,220 股

📆 10-19 Forward Structure
存量OI: C 9.0k / P 6.1k，今日变化ΔOI: C +3.1k / P +2.8k，平值价格ATM: C $0.60 / P $0.67 ｜ ATM IV 29.5%，净 delta 敞口 195k shares
Top ΔOI: C 51 +834 ｜ C 51 +621 ｜ P 48 +512
仓位参考: Max Pain 52 ｜ Call Wall 53（+2.1%）（OI 1.3k） ｜ Put Wall 49.5（-4.7%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 29.5%｜历史 Rank 71%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 194,984 股

📆 10-21 Forward Structure
存量OI: C 10.0k / P 5.2k，今日变化ΔOI: C +4.3k / P +2.7k，平值价格ATM: C $0.79 / P $0.88 ｜ ATM IV 31.8%，净 delta 敞口 122k shares
Top ΔOI: C 51 +905 ｜ P 49 +547
仓位参考: Max Pain 51 ｜ Call Wall 51（-1.8%，弱）（OI 0.9k） ｜ Put Wall 49（-5.6%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 31.8%｜历史 Rank 71%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 122,463 股

📆 10-23 Forward Structure
存量OI: C 57.4k / P 40.5k，今日变化ΔOI: C +12.4k / P +5.4k，平值价格ATM: C $0.97 / P $1.02 ｜ ATM IV 33.1%，净 delta 敞口 428k shares
Top ΔOI: C 55 +3,850 ｜ C 50 +2,079 ｜ C 51 +1,861
仓位参考: Max Pain 55 ｜ Call Wall 57（+9.8%，弱）（OI 6.8k） ｜ Put Wall 50（-3.7%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 33.1%｜历史 Rank 71%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 正 428,054 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 42.2% vs 10-19 29.5%（差 +12.7pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SLV_evening.json