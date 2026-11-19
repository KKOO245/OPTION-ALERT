# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $nan
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-19（1D）ATM IV 28.4% vs 11-20 0.0%（差 +28.4pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-19 262P ΔOI +3,774（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 268.15 → 收盘 270.12（+0.7%） ｜ 今日高 272.36 ｜ 低 267.90 ｜ 昨收 269.05 → 收盘 270.12（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.89 | OI比 0.70 | ATM IV 21.2% | Skew -6.3pp | Term 1.07 | ExpMove ±1.2%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 1.07）｜Put 保护异常便宜（Skew -6.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-19（1D）±1.2% ｜ 11-20（2D）±0.0% ｜ 11-23（5D）±2.1% ｜ 11-24（6D）±2.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,905,492,638 | GEX Change vs 上次快照 -82,263,023 | Flip: Primary Flip: 281.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1181 / LOW 271 / INVALID 1130
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 281.68（全链重定价，覆盖 94%）
Put Wall 270（弱结构｜现价高于该位 0.0%）
最近结构参考: Put Wall 270（现价高于该位 0.0%）
量化视角： 负 Gamma（19.05亿，无历史分位）｜负 Gamma 加深（8226万）｜现价位于 Flip 下方 4.10%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 273（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-19  C +5.5k / P +14.2k ｜ Activity HIGH ｜ 1D
11-20  C +16.3k / P -64.5k ｜ Activity HIGH ｜ 2D
11-23  C +3.8k / P +4.2k ｜ Activity HIGH ｜ 5D
11-24  C +2.3k / P +5.4k ｜ Activity HIGH ｜ 6D

📆 11-19 Forward Structure
存量OI: C 20.6k / P 41.2k，今日变化ΔOI: C +5.5k / P +14.2k，平值价格ATM: C $1.59 / P $1.63 ｜ ATM IV 28.4%，净 delta 敞口 63k shares
Top ΔOI: P 262 +3,774 ｜ P 263 +2,878 ｜ P 257 +2,791
仓位参考: Max Pain 275 ｜ Call Wall 287（+6.2%）（OI 3.4k） ｜ Put Wall 262.5（-2.8%，弱）（OI 4.2k）
量化解读： 存量 Put 重｜ATM IV 28.4%｜历史 Rank 34%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 62,824 股

📆 11-20 Forward Structure
存量OI: C 585.5k / P 1436.5k，今日变化ΔOI: C +16.3k / P -64.5k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 4.6M shares
Top ΔOI: P 270 -19,678 ｜ P 264 -17,053 ｜ P 262 +15,856
仓位参考: Max Pain 277 ｜ Call Wall 285（+5.5%，弱）（OI 51.0k） ｜ Put Wall 265（-1.9%，弱）（OI 131.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜净 delta 敞口 正 4,646,442 股

📆 11-23 Forward Structure
存量OI: C 16.5k / P 25.9k，今日变化ΔOI: C +3.8k / P +4.2k，平值价格ATM: C $2.91 / P $2.80 ｜ ATM IV 22.3%，净 delta 敞口 13k shares
Top ΔOI: P 265 +1,215 ｜ P 250 +626 ｜ P 255 +608
仓位参考: Max Pain 275 ｜ Call Wall 282（+4.4%，弱）（OI 1.9k） ｜ Put Wall 270（-0.0%）（OI 12.3k）
量化解读： 存量 Put 重｜ATM IV 22.3%｜历史 Rank 34%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 12,827 股

📆 11-24 Forward Structure
存量OI: C 6.4k / P 11.7k，今日变化ΔOI: C +2.3k / P +5.4k，平值价格ATM: C $3.50 / P $2.94 ｜ ATM IV 23.2%，净 delta 敞口 -43k shares
Top ΔOI: P 260 +1,492 ｜ P 250 +1,488 ｜ C 275 +529
仓位参考: Max Pain 275 ｜ Call Wall 286（+5.9%，弱）（OI 0.9k） ｜ Put Wall 270（-0.0%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 23.2%｜历史 Rank 34%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 负 42,547 股

📅 事件差分（观察，非因果）: 11-19（1D）ATM IV 28.4% vs 11-20 0.0%（差 +28.4pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/IWM_evening.json