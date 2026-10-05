# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 56C ΔOI +647（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 55.60 → 收盘 55.13（-0.8%） ｜ 今日高 55.61 ｜ 低 54.92 ｜ 昨收 54.74 → 收盘 55.13（+0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.83 | OI比 0.60 | ATM IV 32.8% | Skew -25.2pp | Term 1.01 | ExpMove ±1.9%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -25.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-07（2D）±1.9% ｜ 10-09（4D）±2.6% ｜ 10-12（7D）±3.0% ｜ 10-14（9D）±3.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 30,892,432 | GEX Change vs 上次快照 -10,817,081 | Flip: Primary Flip: 54.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 642 / LOW 140 / INVALID 460
结构观察区: Primary Flip 54.04（全链重定价，覆盖 97%）
Put Wall 60（弱结构｜现价低于该位 8.1%）
最近结构参考: Flip 54（现价高于该位 2.0%）
量化视角： 正 Gamma（3089万，无历史分位）｜正 Gamma 减弱（1082万）｜现价位于 Flip 上方 2.03%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（MaxPain，仅结算参考）；上方 60（Put Wall，弱结构）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 60.0C — Vol 586 | 最新价 $0.71 | OI 2434→5844 (ΔOI +3410张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3410张（+140.1% vs前日OI），连续性待观察（方向未知）
10-07 51.5P — Vol 588 | 最新价 $0.01 | OI 301→2824 (ΔOI +2523张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2523张（+838.2% vs前日OI），连续性待观察（方向未知）
10-16 60.0C — Vol 1,845 | 最新价 $0.13 | OI 53242→55713 (ΔOI +2471张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2471张（+4.6% vs前日OI），值得跟踪（方向未知）
量化视角： 3 个事件合计 ΔOI ≈ 8,404 张（Put 2,523 / Call 5,881），跨 3 个期限｜彩票/名义 1 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-07  C +3.7k / P +4.3k ｜ Activity HIGH ｜ 2D
10-09  C +9.2k / P +4.9k ｜ Activity HIGH ｜ 4D
10-12  C +0.5k / P +0.3k ｜ Activity HIGH ｜ 7D
10-14  C +0.3k / P +0.1k ｜ Activity HIGH ｜ 9D

📆 10-07 Forward Structure
存量OI: C 22.3k / P 11.5k，今日变化ΔOI: C +3.7k / P +4.3k，平值价格ATM: C $0.58 / P $0.46 ｜ ATM IV 30.9%，净 delta 敞口 95k shares
Top ΔOI: P 51 +2,523 ｜ C 56 +647
仓位参考: Max Pain 55 ｜ Call Wall 58（+5.2%，弱）（OI 3.1k） ｜ Put Wall 51.5（-6.6%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.9%｜历史 Rank 50%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 95,127 股

📆 10-09 Forward Structure
存量OI: C 82.7k / P 23.3k，今日变化ΔOI: C +9.2k / P +4.9k，平值价格ATM: C $0.79 / P $0.65 ｜ ATM IV 31.3%，净 delta 敞口 67k shares
Top ΔOI: C 58 +1,831 ｜ P 54 +1,073
仓位参考: Max Pain 56 ｜ Call Wall 60（+8.8%，弱）（OI 5.0k） ｜ Put Wall 55（-0.2%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 31.3%｜历史 Rank 50%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 67,155 股

📆 10-12 Forward Structure
存量OI: C 2.2k / P 4.2k，今日变化ΔOI: C +0.5k / P +0.3k，平值价格ATM: C $0.91 / P $0.77 ｜ ATM IV 27.4%，净 delta 敞口 11k shares
Top ΔOI: P 50 +104 ｜ C 57 +97 ｜ C 56 +68
仓位参考: Max Pain 55 ｜ Call Wall 58（+5.2%，弱）（OI 0.4k） ｜ Put Wall 54（-2.0%）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 27.4%｜历史 Rank 50%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 11,270 股

📆 10-14 Forward Structure
存量OI: C 1.6k / P 1.3k，今日变化ΔOI: C +0.3k / P +0.1k，平值价格ATM: C $1.20 / P $0.94 ｜ ATM IV 30.0%，净 delta 敞口 8k shares
Top ΔOI: C 56 +99 ｜ C 57 +98 ｜ C 60 +55
仓位参考: Max Pain 55 ｜ Call Wall 58（+5.2%，弱）（OI 0.4k） ｜ Put Wall 55（-0.2%）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 30.0%｜历史 Rank 50%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 7,601 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SLV_evening.json