# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-23（3D）ATM IV 87.0% vs 10-30 69.7%（差 +17.3pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-23 10C ΔOI +823（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 9.87 → 收盘 10.06（+1.9%） ｜ 今日高 10.40 ｜ 低 9.72 ｜ 昨收 10.09 → 收盘 10.06（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.23 | OI比 0.30 | ATM IV 87.0% | Skew -1.3pp | Term 0.97 | ExpMove ±5.8%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（3D）±5.8% ｜ 10-30（10D）±10.8% ｜ 11-06（17D）±15.7% ｜ 11-13（24D）±18.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 384,836 | GEX Change vs 上次快照 795,910 | Flip: Primary Flip: 9.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 210 / LOW 84 / INVALID 142
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.96（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价高于该位 0.6%）
最近结构参考: Put Wall 10（现价高于该位 0.6%）
量化视角： 正 Gamma（38万，无历史分位）｜由负转正（+80万）｜现价位于 Flip 上方 1.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构）；上方 11（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +2.5k / P -0.2k ｜ Activity HIGH ｜ 3D
10-30  C +7.1k / P -0.4k ｜ Activity HIGH ｜ 10D
11-06  C +0.3k / P -0.5k ｜ Activity HIGH ｜ 17D
11-13  C +0.2k / P -37 ｜ Activity HIGH ｜ 24D

📆 10-23 Forward Structure
存量OI: C 21.1k / P 6.3k，今日变化ΔOI: C +2.5k / P -0.2k，平值价格ATM: C $0.33 / P $0.25 ｜ ATM IV 87.0%，净 delta 敞口 122k shares
Top ΔOI: C 10 +823 ｜ C 11 +694
仓位参考: Max Pain 11 ｜ Call Wall 11（+9.3%，弱）（OI 1.8k） ｜ Put Wall 9.5（-5.6%）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 87.0%｜历史 Rank 18%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 121,924 股

📆 10-30 Forward Structure
存量OI: C 17.3k / P 8.9k，今日变化ΔOI: C +7.1k / P -0.4k，平值价格ATM: C $0.57 / P $0.52 ｜ ATM IV 69.7%，净 delta 敞口 198k shares
Top ΔOI: C 11 +2,140
仓位参考: Max Pain 12 ｜ Call Wall 11（+9.3%，弱）（OI 2.5k） ｜ Put Wall 10（-0.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 69.7%｜历史 Rank 18%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 198,466 股

📆 11-06 Forward Structure
存量OI: C 4.2k / P 4.5k，今日变化ΔOI: C +0.3k / P -0.5k，平值价格ATM: C $0.84 / P $0.74 ｜ ATM IV 81.0%，净 delta 敞口 62k shares
Top ΔOI: P 17 -341 ｜ C 11 +101
仓位参考: Max Pain 13 ｜ Call Wall 11（+9.3%，弱）（OI 0.4k） ｜ Put Wall 10（-0.6%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 81.0%｜历史 Rank 18%（近端代理）｜IV/RV 1.48×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 61,797 股

📆 11-13 Forward Structure
存量OI: C 2.2k / P 3.4k，今日变化ΔOI: C +0.2k / P -37，平值价格ATM: C $1.00 / P $0.89 ｜ ATM IV 86.0%，净 delta 敞口 7k shares
仓位参考: Max Pain 15 ｜ Call Wall 10.5（+4.4%，弱）（OI 0.2k） ｜ Put Wall 11（+9.3%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 86.0%｜历史 Rank 18%（近端代理）｜IV/RV 1.57×（近似）｜净 delta 敞口 正 7,121 股

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 87.0% vs 10-30 69.7%（差 +17.3pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/USAR_evening.json