# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.74 ｜ QQQ $760.82
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 242C ΔOI -2,746（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 290C ΔOI +2,913 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 232.57 → 今开 237.22（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 249.20 ｜ 低 237.00

Options: P/C成交量 0.38 | OI比 0.94 | ATM IV 81.3% | Skew -3.4pp | Term 0.90 | ExpMove ±6.2%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -3.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±6.2% ｜ 10-16（10D）±9.8% ｜ 10-23（17D）±12.6% ｜ 10-30（24D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 17,150,012 | GEX Change vs 上次快照 10,292,191 | Flip: Primary Flip: 230.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 469 / LOW 29 / INVALID 154
结构观察区: Primary Flip 230.31（全链重定价，覆盖 100%）
最近结构参考: Flip 230（现价高于该位 7.3%）
量化视角： 正 Gamma（1715万，无历史分位）｜正 Gamma 增强（+1029万）｜现价位于 Flip 上方 7.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 232（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 230（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 245.0C — Vol 4,646 | 最新价 $6.70 | OI 972→4449 (ΔOI +3477张) | ΔOI/Volume 74.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3477张（+357.7% vs前日OI），连续性待观察（方向未知）
10-16 310.0C — Vol 5,083 | 最新价 $0.44 | OI 2892→6362 (ΔOI +3470张) | ΔOI/Volume 68.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3470张（+120.0% vs前日OI），连续性待观察（方向未知）
10-09 220.0P — Vol 4,910 | 最新价 $2.39 | OI 2993→6133 (ΔOI +3140张) | ΔOI/Volume 64.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3140张（+104.9% vs前日OI），连续性待观察（方向未知）
10-30 290.0C — Vol 4,202 | 最新价 $3.65 | OI 2418→5331 (ΔOI +2913张) | ΔOI/Volume 69.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2913张（+120.5% vs前日OI），连续性待观察（方向未知）
10-09 215.0P — Vol 3,003 | 最新价 $1.41 | OI 1421→3734 (ΔOI +2313张) | ΔOI/Volume 77.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2313张（+162.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,313 张（Put 5,453 / Call 9,860），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +5.0k / P +15.0k ｜ Activity HIGH ｜ 3D
10-16  C +10.5k / P +4.7k ｜ Activity HIGH ｜ 10D
10-23  C +2.9k / P +0.9k ｜ Activity HIGH ｜ 17D
10-30  C +4.2k / P +2.8k ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 47.0k / P 44.0k，今日变化ΔOI: C +5.0k / P +15.0k，平值价格ATM: C $8.20 / P $7.05 ｜ ATM IV 81.3%，净 delta 敞口 61k shares
Top ΔOI: P 220 +3,140 ｜ C 242 -2,746 ｜ P 215 +2,313
仓位参考: Max Pain 232 ｜ Call Wall 242.5（-1.9%，弱）（OI 4.4k） ｜ Put Wall 225（-8.9%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.3%｜历史 Rank 12%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,547 股

📆 10-16 Forward Structure
存量OI: C 82.9k / P 95.8k，今日变化ΔOI: C +10.5k / P +4.7k，平值价格ATM: C $12.70 / P $11.60 ｜ ATM IV 73.8%，净 delta 敞口 389k shares
Top ΔOI: C 245 +3,477 ｜ C 310 +3,470 ｜ C 210 +1,473
仓位参考: Max Pain 220 ｜ Call Wall 270（+9.3%，弱）（OI 6.2k） ｜ Put Wall 225（-8.9%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.8%｜历史 Rank 12%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 388,871 股

📆 10-23 Forward Structure
存量OI: C 11.5k / P 10.4k，今日变化ΔOI: C +2.9k / P +0.9k，平值价格ATM: C $15.36 / P $15.75 ｜ ATM IV 71.9%，净 delta 敞口 123k shares
Top ΔOI: C 237 +883 ｜ C 320 +365
仓位参考: Max Pain 225 ｜ Call Wall 237.5（-3.9%，弱）（OI 0.9k） ｜ Put Wall 225（-8.9%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 71.9%｜历史 Rank 12%（近端代理）｜IV/RV 1.38×（近似）｜净 delta 敞口 正 122,715 股

📆 10-30 Forward Structure
存量OI: C 15.4k / P 13.1k，今日变化ΔOI: C +4.2k / P +2.8k，平值价格ATM: C $19.69 / P $17.00 ｜ ATM IV 72.5%，净 delta 敞口 74k shares
Top ΔOI: C 290 +2,913 ｜ P 200 +811 ｜ P 220 +477
仓位参考: Max Pain 230 ｜ Put Wall 240（-2.9%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 72.5%｜历史 Rank 12%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 正 74,235 股

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 81.3% vs 10-16 73.8%（差 +7.5pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/NBIS_morning.json