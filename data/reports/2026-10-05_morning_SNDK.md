# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $nan
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 1800C ΔOI +832（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,719.99 → 今开 1,723.80（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 1743.24 ｜ 低 1713.00

Options: P/C成交量 0.81 | OI比 1.09 | ATM IV 60.7% | Skew -2.0pp | Term 1.09 | ExpMove ±5.2%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常（Term 1.09）｜Put 保护异常便宜（Skew -2.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±5.2% ｜ 10-16（11D）±8.2% ｜ 10-23（18D）±11.0% ｜ 10-30（25D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,656 | GEX Change vs 上次快照 600,567 | Flip: Primary Flip: 1718.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1458 / LOW 386 / INVALID 1256
结构观察区: Primary Flip 1718.80（全链重定价，覆盖 100%）
最近结构参考: Flip 1719（现价高于该位 0.0%）
量化视角： 正 Gamma（1万，无历史分位）｜由负转正（+60万）｜现价位于 Flip 上方 0.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1719（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 1000.0P — Vol 1,690 | 最新价 $0.05 | OI 705→1883 (ΔOI +1178张) | ΔOI/Volume 69.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1178张（+167.1% vs前日OI），连续性待观察（方向未知）
10-09 1850.0C — Vol 2,466 | 最新价 $13.80 | OI 503→1415 (ΔOI +912张) | ΔOI/Volume 37.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增912张（+181.3% vs前日OI），连续性待观察（方向未知）
10-09 1800.0C — Vol 2,729 | 最新价 $23.70 | OI 559→1391 (ΔOI +832张) | ΔOI/Volume 30.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增832张（+148.8% vs前日OI），连续性待观察（方向未知）
10-09 1695.0P — Vol 646 | 最新价 $39.00 | OI 44→595 (ΔOI +551张) | ΔOI/Volume 85.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增551张（+1252.3% vs前日OI），连续性待观察（方向未知）
10-09 1500.0P — Vol 1,170 | 最新价 $2.90 | OI 582→1105 (ΔOI +523张) | ΔOI/Volume 44.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增523张（+89.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,996 张（Put 2,252 / Call 1,744），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +8.8k / P +8.9k ｜ Activity HIGH ｜ 4D
10-16  C +1.3k / P +0.8k ｜ Activity HIGH ｜ 11D
10-23  C +1.2k / P +0.9k ｜ Activity MEDIUM △ ｜ 18D
10-30  C +0.5k / P +0.7k ｜ Activity MEDIUM △ ｜ 25D

📆 10-09 Forward Structure
存量OI: C 26.2k / P 28.6k，今日变化ΔOI: C +8.8k / P +8.9k，平值价格ATM: C $45.10 / P $44.60 ｜ ATM IV 60.7%，净 delta 敞口 28k shares
Top ΔOI: C 1850 +912 ｜ C 1800 +832
仓位参考: Max Pain 1,700 ｜ Call Wall 1850（+7.6%，弱）（OI 1.4k） ｜ Put Wall 1800（+4.7%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 60.7%｜历史 Rank 17%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 27,845 股

📆 10-16 Forward Structure
存量OI: C 41.0k / P 50.8k，今日变化ΔOI: C +1.3k / P +0.8k，平值价格ATM: C $69.80 / P $70.84 ｜ ATM IV 58.5%，净 delta 敞口 38k shares
Top ΔOI: C 1700 +163
仓位参考: Max Pain 1,670 ｜ Call Wall 1800（+4.7%，弱）（OI 1.2k） ｜ Put Wall 1600（-6.9%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.5%｜历史 Rank 17%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 38,226 股

10-23（MEDIUM △）Top ΔOI: 1850C +167 ｜ 1420P +111
10-23（MEDIUM △）仓位参考: Max Pain 1,725 ｜ Call Wall 1800（+4.7%，弱）（OI 0.3k） ｜ Put Wall 1650（-4.0%，弱）（OI 0.3k）

10-30（MEDIUM △）Top ΔOI: 1500P +73 ｜ 1870C +59
10-30（MEDIUM △）仓位参考: Max Pain 1,720 ｜ Call Wall 1800（+4.7%，弱）（OI 0.2k） ｜ Put Wall 1600（-6.9%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SNDK_morning.json