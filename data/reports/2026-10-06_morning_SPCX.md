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
🟡 **事件差分**: 10-09 ATM IV 58.6% vs 10-12 48.5%（差 +10.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 177C ΔOI +14,137（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-12 180C ΔOI +2,778 占该期限总 OI 11.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 171.09 → 今开 172.10（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 176.42 ｜ 低 172.00

Options: P/C成交量 0.47 | OI比 1.15 | ATM IV 58.6% | Skew -2.7pp | Term 0.88 | ExpMove ±4.4%（近端） | Rank 64%
量化视角： IV 中性（Rank 64%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.4% ｜ 10-12（6D）±5.1% ｜ 10-14（8D）±6.5% ｜ 10-16（10D）±6.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 132,364,492 | GEX Change vs 上次快照 14,042,010 | Flip: Primary Flip: 156.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 670 / LOW 68 / INVALID 486
结构观察区: Primary Flip 156.82（全链重定价，覆盖 100%）
Call Wall 160（弱结构｜现价高于该位 9.0%）
最近结构参考: Call Wall 160（现价高于该位 9.0%）
量化视角： 正 Gamma（1.32亿，无历史分位）｜正 Gamma 增强（+1404万）｜现价位于 Flip 上方 11.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（MaxPain，仅结算参考） / 160（Call Wall，弱结构）。
• Gamma 区域：切换参考 157（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 190.0C — Vol 32,249 | 最新价 $2.85 | OI 1663→28337 (ΔOI +26674张) | ΔOI/Volume 82.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26674张（+1604.0% vs前日OI），连续性待观察（方向未知）
10-09 160.0P — Vol 42,333 | 最新价 $0.61 | OI 3150→19617 (ΔOI +16467张) | ΔOI/Volume 38.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16467张（+522.8% vs前日OI），连续性待观察（方向未知）
10-16 185.0C — Vol 20,032 | 最新价 $1.69 | OI 8088→22870 (ΔOI +14782张) | ΔOI/Volume 73.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14782张（+182.8% vs前日OI），连续性待观察（方向未知）
10-09 177.5C — Vol 25,608 | 最新价 $1.72 | OI 0→14137 (ΔOI +14137张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14137张（前日OI缺失），连续性待观察（方向未知）
10-09 165.0P — Vol 47,967 | 最新价 $1.52 | OI 552→11529 (ΔOI +10977张) | ΔOI/Volume 22.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10977张（+1988.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 83,037 张（Put 27,444 / Call 55,593），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +39.5k / P +63.0k ｜ Activity HIGH ｜ 3D
10-12  C +15.5k / P +8.2k ｜ Activity HIGH ｜ 6D
10-14  C N/A / P N/A ｜ Activity LOW ｜ 8D（新上架）
10-16  C +3.5k / P -8.9k ｜ Activity HIGH ｜ 10D

📆 10-09 Forward Structure
存量OI: C 168.8k / P 193.4k，今日变化ΔOI: C +39.5k / P +63.0k，平值价格ATM: C $3.60 / P $4.11 ｜ ATM IV 58.6%，净 delta 敞口 200k shares
Top ΔOI: P 160 +16,467 ｜ C 177 +14,137 ｜ P 165 +10,977
仓位参考: Max Pain 160 ｜ Call Wall 180（+3.2%）（OI 24.1k） ｜ Put Wall 160（-8.3%，弱）（OI 19.6k）
量化解读： 存量两侧均衡｜ATM IV 58.6%｜历史 Rank 64%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 199,658 股

📆 10-12 Forward Structure
存量OI: C 15.5k / P 8.2k，今日变化ΔOI: C +15.5k / P +8.2k，平值价格ATM: C $4.25 / P $4.65 ｜ ATM IV 48.5%，净 delta 敞口 552k shares
Top ΔOI: C 180 +2,778 ｜ C 170 +2,269 ｜ C 190 +2,001
仓位参考: Max Pain 165 ｜ Call Wall 180（+3.2%，弱）（OI 2.8k） ｜ Put Wall 165（-5.4%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 48.5%｜历史 Rank 64%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 551,659 股

📆 10-16 Forward Structure
存量OI: C 347.1k / P 345.8k，今日变化ΔOI: C +3.5k / P -8.9k，平值价格ATM: C $5.60 / P $6.01 ｜ ATM IV 49.9%，净 delta 敞口 -839k shares
Top ΔOI: C 185 +14,782
仓位参考: Max Pain 145 ｜ Call Wall 160（-8.3%，弱）（OI 36.0k）
量化解读： 存量两侧均衡｜ATM IV 49.9%｜历史 Rank 64%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 负 838,575 股

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 58.6% vs 10-12 48.5%（差 +10.1pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SPCX_morning.json