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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.62 → 今开 15.70（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 15.91 ｜ 低 15.27

Options: P/C成交量 0.28 | OI比 0.39 | ATM IV 80.1% | Skew -0.0pp | Term 0.94 | ExpMove ±6.8%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±6.8% ｜ 10-16（11D）±12.2% ｜ 10-23（18D）±13.7% ｜ 10-30（25D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 954,545 | GEX Change vs 上次快照 263,953 | Flip: Primary Flip: 14.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 145 / LOW 83 / INVALID 200
结构观察区: Primary Flip 14.43（全链重定价，覆盖 90%）
Put Wall 15（弱结构｜现价高于该位 3.4%）
最近结构参考: Put Wall 15（现价高于该位 3.4%）
量化视角： 正 Gamma（95万，无历史分位）｜正 Gamma 增强（+26万）｜现价位于 Flip 上方 7.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 15.5P — Vol 165 | 最新价 $0.45 | OI 220→382 (ΔOI +162张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增162张（+73.6% vs前日OI），连续性待观察（方向未知）
10-09 17.0C — Vol 128 | 最新价 $0.15 | OI 109→221 (ΔOI +112张) | ΔOI/Volume 87.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增112张（+102.8% vs前日OI），连续性待观察（方向未知）
10-09 17.0P — Vol 69 | 最新价 $1.39 | OI 147→216 (ΔOI +69张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69张（+46.9% vs前日OI），连续性待观察（方向未知）
10-09 16.5C — Vol 86 | 最新价 $0.25 | OI 96→161 (ΔOI +65张) | ΔOI/Volume 75.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增65张（+67.7% vs前日OI），连续性待观察（方向未知）
10-09 16.5P — Vol 55 | 最新价 $1.02 | OI 140→195 (ΔOI +55张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55张（+39.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 463 张（Put 286 / Call 177），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.3k / P +0.4k ｜ Activity HIGH ｜ 4D
10-16  C +42 / P -3 ｜ Activity MEDIUM △ ｜ 11D
10-23  C +3 / P +12 ｜ Activity LOW ｜ 18D
10-30  C +20 / P +30 ｜ Activity LOW ｜ 25D

📆 10-09 Forward Structure
存量OI: C 5.6k / P 2.2k，今日变化ΔOI: C +0.3k / P +0.4k，平值价格ATM: C $0.50 / P $0.55 ｜ ATM IV 80.1%，净 delta 敞口 -15k shares
Top ΔOI: P 15 +162 ｜ C 17 +112 ｜ P 17 +69
仓位参考: Max Pain 17 ｜ Put Wall 15.5（-0.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 80.1%｜历史 Rank 8%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 15,480 股

10-16（MEDIUM △）仓位参考: Max Pain 19 ｜ Put Wall 15（-3.3%，弱）（OI 0.9k）

10-23（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 14（-9.7%）（OI 0.3k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（-9.7%）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NNE_morning.json