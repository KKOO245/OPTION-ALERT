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
🟡 **近现价集中开仓**: 10-07 250C ΔOI +5,612（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 236.07 → 收盘 238.90（+1.2%） ｜ 今日高 240.10 ｜ 低 235.15 ｜ 昨收 233.95 → 收盘 238.90（+2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.65 | OI比 1.56 | ATM IV 42.4% | Skew -4.0pp | Term 0.68 | ExpMove ±1.8%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.56×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-07（2D）±1.8% ｜ 10-09（4D）±2.5% ｜ 10-12（7D）±2.9% ｜ 10-14（9D）±3.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 589,521,362 | GEX Change vs 上次快照 32,875,605 | Flip: Primary Flip: 221.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 629 / LOW 186 / INVALID 559
结构观察区: Primary Flip 221.70（全链重定价，覆盖 94%）
Put Wall 220（弱结构｜现价高于该位 8.6%） | Call Wall 240（弱结构｜现价低于该位 0.5%）
最近结构参考: Call Wall 240（现价低于该位 0.5%）
量化视角： 正 Gamma（5.90亿，无历史分位）｜正 Gamma 增强（+3288万）｜现价位于 Flip 上方 7.76%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构） / 232（MaxPain，仅结算参考）；上方 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 222（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 240.0C — Vol 78,880 | 最新价 $2.57 | OI 19594→78334 (ΔOI +58740张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增58740张（+299.8% vs前日OI），连续性待观察（方向未知）
10-09 110.0P — Vol 26 | 最新价 $0.01 | OI 9921→46135 (ΔOI +36214张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36214张（+365.0% vs前日OI），连续性待观察（方向未知）
10-09 245.0C — Vol 44,243 | 最新价 $0.91 | OI 11268→43713 (ΔOI +32445张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32445张（+287.9% vs前日OI），连续性待观察（方向未知）
10-09 247.5C — Vol 37,029 | 最新价 $0.50 | OI 2344→33368 (ΔOI +31024张) | ΔOI/Volume 83.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31024张（+1323.5% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 158,423 张（Put 36,214 / Call 122,209），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-07  C +28.8k / P +17.8k ｜ Activity HIGH ｜ 2D
10-09  C +152.5k / P +118.9k ｜ Activity HIGH ｜ 4D
10-12  C +4.0k / P +4.0k ｜ Activity HIGH ｜ 7D
10-14  C +1.7k / P +1.6k ｜ Activity HIGH ｜ 9D

📆 10-07 Forward Structure
存量OI: C 59.5k / P 41.5k，今日变化ΔOI: C +28.8k / P +17.8k，平值价格ATM: C $1.59 / P $2.69 ｜ ATM IV 29.6%，净 delta 敞口 480k shares
Top ΔOI: C 250 +5,612 ｜ C 240 +5,039 ｜ C 242 +5,033
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+3.6%，弱）（OI 9.9k） ｜ Put Wall 230（-3.7%）（OI 10.2k）
量化解读： 存量 Call 重｜ATM IV 29.6%｜历史 Rank 49%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 480,241 股

📆 10-09 Forward Structure
存量OI: C 342.2k / P 356.7k，今日变化ΔOI: C +152.5k / P +118.9k，平值价格ATM: C $2.57 / P $3.35 ｜ ATM IV 29.2%，净 delta 敞口 3.5M shares
Top ΔOI: C 240 +58,740 ｜ C 245 +32,445
仓位参考: Max Pain 230 ｜ Call Wall 240（+0.5%）（OI 78.3k） ｜ Put Wall 230（-3.7%，弱）（OI 26.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 29.2%｜历史 Rank 49%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,540,313 股

📆 10-12 Forward Structure
存量OI: C 13.3k / P 7.9k，今日变化ΔOI: C +4.0k / P +4.0k，平值价格ATM: C $2.83 / P $3.97 ｜ ATM IV 25.3%，净 delta 敞口 138k shares
Top ΔOI: C 240 +1,848 ｜ P 222 +1,257 ｜ P 220 +583
仓位参考: Max Pain 230 ｜ Call Wall 240（+0.5%）（OI 4.7k） ｜ Put Wall 222.5（-6.9%）（OI 1.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 25.3%｜历史 Rank 49%（近端代理）｜IV/RV 1.21×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 137,874 股

📆 10-14 Forward Structure
存量OI: C 6.0k / P 3.2k，今日变化ΔOI: C +1.7k / P +1.6k，平值价格ATM: C $3.60 / P $4.63 ｜ ATM IV 26.9%，净 delta 敞口 41k shares
Top ΔOI: P 215 +521 ｜ C 237 +420 ｜ C 250 +332
仓位参考: Max Pain 230 ｜ Call Wall 255（+6.7%，弱）（OI 1.0k） ｜ Put Wall 225（-5.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 26.9%｜历史 Rank 49%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 41,415 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NVDA_evening.json