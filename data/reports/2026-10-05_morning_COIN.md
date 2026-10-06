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
🟡 **近现价集中开仓**: 10-09 187C ΔOI +7,588（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 183.00 → 今开 187.14（+2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 191.78 ｜ 低 185.59

Options: P/C成交量 0.24 | OI比 0.54 | ATM IV 62.6% | Skew -3.1pp | Term 1.03 | ExpMove ±5.5%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构正常（Term 1.03）｜Put 保护异常便宜（Skew -3.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±5.5% ｜ 10-16（11D）±8.1% ｜ 10-23（18D）±10.7% ｜ 10-30（25D）±12.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 26,362,018 | GEX Change vs 上次快照 17,491,360 | Flip: Primary Flip: 173.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 448 / LOW 100 / INVALID 290
结构观察区: Primary Flip 173.38（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 5.5%）
最近结构参考: Call Wall 200（现价低于该位 5.5%）
量化视角： 正 Gamma（2636万，无历史分位）｜正 Gamma 增强（+1749万）｜现价位于 Flip 上方 8.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 173（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 187.5C — Vol 8,550 | 最新价 $3.60 | OI 245→7833 (ΔOI +7588张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7588张（+3097.1% vs前日OI），连续性待观察（方向未知）
10-09 195.0C — Vol 9,616 | 最新价 $1.72 | OI 5625→12723 (ΔOI +7098张) | ΔOI/Volume 73.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7098张（+126.2% vs前日OI），连续性待观察（方向未知）
10-16 220.0C — Vol 4,713 | 最新价 $0.74 | OI 6867→9290 (ΔOI +2423张) | ΔOI/Volume 51.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2423张（+35.3% vs前日OI），连续性待观察（方向未知）
10-09 207.5C — Vol 2,658 | 最新价 $0.55 | OI 236→2512 (ΔOI +2276张) | ΔOI/Volume 85.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2276张（+964.4% vs前日OI），连续性待观察（方向未知）
10-09 217.5C — Vol 2,536 | 最新价 $0.22 | OI 75→2282 (ΔOI +2207张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2207张（+2942.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,592 张（Put 0 / Call 21,592），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +26.2k / P +8.4k ｜ Activity HIGH ｜ 4D
10-16  C +6.3k / P +3.6k ｜ Activity MEDIUM △ ｜ 11D
10-23  C +1.1k / P +1.0k ｜ Activity MEDIUM △ ｜ 18D
10-30  C +1.7k / P +0.8k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 60.5k / P 32.8k，今日变化ΔOI: C +26.2k / P +8.4k，平值价格ATM: C $4.80 / P $5.52 ｜ ATM IV 62.6%，净 delta 敞口 814k shares
Top ΔOI: C 187 +7,588 ｜ C 195 +7,098 ｜ C 207 +2,276
仓位参考: Max Pain 188 ｜ Call Wall 195（+3.2%）（OI 12.7k） ｜ Put Wall 177.5（-6.1%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 62.6%｜历史 Rank 15%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 813,996 股

10-16（MEDIUM △）Top ΔOI: 220C +2,423 ｜ 215C +844
10-16（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+5.8%，弱）（OI 7.0k） ｜ Put Wall 200（+5.8%，弱）（OI 3.9k）

10-23（MEDIUM △）Top ΔOI: 170P +238 ｜ 167P +201
10-23（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 190（+0.5%，弱）（OI 0.7k） ｜ Put Wall 192.5（+1.9%，弱）（OI 0.4k）

📆 10-30 Forward Structure
存量OI: C 7.8k / P 7.0k，今日变化ΔOI: C +1.7k / P +0.8k，平值价格ATM: C $11.70 / P $12.76 ｜ ATM IV 64.5%，净 delta 敞口 80k shares
Top ΔOI: C 185 +951 ｜ C 200 +201
仓位参考: Max Pain 185 ｜ Call Wall 185（-2.1%）（OI 1.2k） ｜ Put Wall 197.5（+4.5%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 64.5%｜历史 Rank 15%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 正 80,409 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/COIN_morning.json