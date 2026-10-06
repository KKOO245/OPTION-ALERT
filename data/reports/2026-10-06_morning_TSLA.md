# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.55 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 380C ΔOI +8,566（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 378.73 → 今开 382.04（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 383.33 ｜ 低 378.52

Options: P/C成交量 0.41 | OI比 0.65 | ATM IV 42.3% | Skew -0.7pp | Term 1.03 | ExpMove ±2.0%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构正常（Term 1.03）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-07（1D）±2.0% ｜ 10-09（3D）±3.1% ｜ 10-12（6D）±3.5% ｜ 10-14（8D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 144,691,763 | GEX Change vs 上次快照 26,420,155 | Flip: Primary Flip: 362.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1182 / LOW 115 / INVALID 523
结构观察区: Primary Flip 362.75（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 5.0%）
最近结构参考: Flip 363（现价高于该位 4.7%）
量化视角： 正 Gamma（1.45亿，无历史分位）｜正 Gamma 增强（+2642万）｜现价位于 Flip 上方 4.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 372（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 363（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-07 380.0C — Vol 46,599 | 最新价 $3.85 | OI 1654→10220 (ΔOI +8566张) | ΔOI/Volume 18.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8566张（+517.9% vs前日OI），连续性待观察（方向未知）
10-09 400.0C — Vol 33,839 | 最新价 $0.90 | OI 11761→19649 (ΔOI +7888张) | ΔOI/Volume 23.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7888张（+67.1% vs前日OI），连续性待观察（方向未知）
10-09 160.0P — Vol 6,000 | 最新价 $0.01 | OI 3451→9409 (ΔOI +5958张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5958张（+172.7% vs前日OI），连续性待观察（方向未知）
10-09 350.0P — Vol 8,809 | 最新价 $0.34 | OI 3682→7970 (ΔOI +4288张) | ΔOI/Volume 48.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4288张（+116.5% vs前日OI），连续性待观察（方向未知）
10-09 320.0P — Vol 5,377 | 最新价 $0.10 | OI 2654→6939 (ΔOI +4285张) | ΔOI/Volume 79.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4285张（+161.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 30,985 张（Put 14,531 / Call 16,454），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-07  C +47.1k / P +25.8k ｜ Activity HIGH ｜ 1D
10-09  C +31.6k / P +36.8k ｜ Activity HIGH ｜ 3D
10-12  C +3.5k / P +6.1k ｜ Activity HIGH ｜ 6D
10-14  C +1.9k / P +2.5k ｜ Activity HIGH ｜ 8D

📆 10-07 Forward Structure
存量OI: C 72.8k / P 47.5k，今日变化ΔOI: C +47.1k / P +25.8k，平值价格ATM: C $3.75 / P $3.80 ｜ ATM IV 42.2%，净 delta 敞口 780k shares
Top ΔOI: C 380 +8,566 ｜ C 410 +4,109 ｜ C 390 +3,680
仓位参考: Max Pain 372 ｜ Call Wall 380（+0.0%）（OI 10.2k） ｜ Put Wall 370（-2.6%，弱）（OI 5.1k）
量化解读： 存量 Call 重｜ATM IV 42.2%｜历史 Rank 15%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 780,466 股

📆 10-09 Forward Structure
存量OI: C 177.4k / P 205.6k，今日变化ΔOI: C +31.6k / P +36.8k，平值价格ATM: C $6.00 / P $5.75 ｜ ATM IV 40.7%，净 delta 敞口 26k shares
Top ΔOI: C 400 +7,888 ｜ P 350 +4,288
仓位参考: Max Pain 368 ｜ Call Wall 400（+5.3%，弱）（OI 19.6k） ｜ Put Wall 350（-7.9%，弱）（OI 8.0k）
量化解读： 存量两侧均衡｜ATM IV 40.7%｜历史 Rank 15%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,030 股

📆 10-12 Forward Structure
存量OI: C 13.8k / P 13.3k，今日变化ΔOI: C +3.5k / P +6.1k，平值价格ATM: C $6.85 / P $6.62 ｜ ATM IV 34.0%，净 delta 敞口 -38k shares
Top ΔOI: P 352 +688 ｜ C 415 +597
仓位参考: Max Pain 370 ｜ Call Wall 380（+0.0%，弱）（OI 1.7k） ｜ Put Wall 352.5（-7.2%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.0%｜历史 Rank 15%（近端代理）｜IV/RV 1.16×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 37,568 股

📆 10-14 Forward Structure
存量OI: C 5.7k / P 4.6k，今日变化ΔOI: C +1.9k / P +2.5k，平值价格ATM: C $8.45 / P $8.08 ｜ ATM IV 36.2%，净 delta 敞口 17k shares
Top ΔOI: C 400 +645
仓位参考: Max Pain 370 ｜ Call Wall 400（+5.3%）（OI 1.1k） ｜ Put Wall 370（-2.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.2%｜历史 Rank 15%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 正 17,353 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/TSLA_morning.json