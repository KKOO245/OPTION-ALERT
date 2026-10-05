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
🟡 **近现价集中开仓**: 10-09 140C ΔOI +687（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 135.22 → 收盘 136.08（+0.6%） ｜ 今日高 137.90 ｜ 低 134.15 ｜ 昨收 134.38 → 收盘 136.08（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.79 | ATM IV 52.8% | Skew -0.6pp | Term 1.11 | ExpMove ±4.6%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 1.11）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±4.6% ｜ 10-16（11D）±6.8% ｜ 10-23（18D）±8.9% ｜ 10-30（25D）±12.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,988,491 | GEX Change vs 上次快照 27,485 | Flip: Primary Flip: 132.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 512 / LOW 33 / INVALID 145
结构观察区: Primary Flip 132.67（全链重定价，覆盖 100%）
最近结构参考: Flip 133（现价高于该位 2.6%）
量化视角： 正 Gamma（699万，无历史分位）｜正 Gamma 增强（+3万）｜现价位于 Flip 上方 2.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 140.0C — Vol 2,498 | 最新价 $1.56 | OI 1981→2668 (ΔOI +687张) | ΔOI/Volume 27.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增687张（+34.7% vs前日OI），连续性待观察（方向未知）
10-09 129.0P — Vol 471 | 最新价 $0.69 | OI 150→817 (ΔOI +667张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增667张（+444.7% vs前日OI），连续性待观察（方向未知）
10-16 155.0C — Vol 97 | 最新价 $0.39 | OI 3475→4066 (ΔOI +591张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增591张（+17.0% vs前日OI），值得跟踪（方向未知）
10-09 130.0P — Vol 411 | 最新价 $0.88 | OI 467→1038 (ΔOI +571张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增571张（+122.3% vs前日OI），连续性待观察（方向未知）
10-09 150.0C — Vol 1,012 | 最新价 $0.18 | OI 4283→4776 (ΔOI +493张) | ΔOI/Volume 48.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增493张（+11.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,009 张（Put 1,238 / Call 1,771），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +3.9k / P +3.9k ｜ Activity HIGH ｜ 4D
10-16  C +1.2k / P +1.2k ｜ Activity HIGH ｜ 11D
10-23  C -32 / P +1.0k ｜ Activity HIGH ｜ 18D
10-30  C +0.4k / P +0.9k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 19.9k / P 15.7k，今日变化ΔOI: C +3.9k / P +3.9k，平值价格ATM: C $3.15 / P $3.15 ｜ ATM IV 52.8%，净 delta 敞口 42k shares
Top ΔOI: C 140 +687 ｜ P 129 +667 ｜ P 130 +571
仓位参考: Max Pain 135 ｜ Call Wall 140（+2.9%，弱）（OI 2.7k） ｜ Put Wall 130（-4.5%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.8%｜历史 Rank 24%（近端代理）｜IV/RV 1.37×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 41,815 股

📆 10-16 Forward Structure
存量OI: C 77.8k / P 63.2k，今日变化ΔOI: C +1.2k / P +1.2k，平值价格ATM: C $4.65 / P $4.56 ｜ ATM IV 49.0%，净 delta 敞口 2k shares
仓位参考: Max Pain 130 ｜ Call Wall 140（+2.9%，弱）（OI 5.9k） ｜ Put Wall 125（-8.1%，弱）（OI 5.6k）
量化解读： 存量 Call 重｜ATM IV 49.0%｜历史 Rank 24%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,094 股

📆 10-23 Forward Structure
存量OI: C 9.8k / P 15.8k，今日变化ΔOI: C -32 / P +1.0k，平值价格ATM: C $6.22 / P $5.85 ｜ ATM IV 49.1%，净 delta 敞口 -24k shares
Top ΔOI: C 134 -306
仓位参考: Max Pain 134 ｜ Call Wall 140（+2.9%，弱）（OI 0.9k） ｜ Put Wall 125（-8.1%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 49.1%｜历史 Rank 24%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 24,413 股

📆 10-30 Forward Structure
存量OI: C 6.1k / P 8.5k，今日变化ΔOI: C +0.4k / P +0.9k，平值价格ATM: C $8.75 / P $8.35 ｜ ATM IV 60.0%，净 delta 敞口 -4k shares
Top ΔOI: P 130 +262 ｜ P 140 +107
仓位参考: Max Pain 134 ｜ Call Wall 140（+2.9%，弱）（OI 0.6k） ｜ Put Wall 123（-9.6%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 60.0%｜历史 Rank 24%（近端代理）｜IV/RV 1.56×（近似）｜净 delta 敞口 负 3,855 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NOW_evening.json