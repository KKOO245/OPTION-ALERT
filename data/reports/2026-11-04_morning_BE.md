# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.96 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（2D）ATM IV 116.9% vs 11-13 97.6%（差 +19.3pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 205P ΔOI +1,506（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 214.01 → 今开 205.50（-4.0%） | 较昨收变动（含盘初走势） ｜ 今日高 213.96 ｜ 低 200.00

Options: P/C成交量 0.76 | OI比 0.68 | ATM IV 116.9% | Skew 3.4pp | Term 0.74 | ExpMove ±7.3%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价中性（Skew 3.4pp）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±7.3% ｜ 11-13（9D）±12.6% ｜ 11-20（16D）±15.6% ｜ 11-27（23D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,362,661 | GEX Change vs 上次快照 -3,707,700 | Flip: Primary Flip: 213.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 537 / LOW 107 / INVALID 202
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 213.18（全链重定价，覆盖 98%）
Put Wall 200（现价高于该位 2.4%）
最近结构参考: Put Wall 200（现价高于该位 2.4%）
量化视角： 负 Gamma（436万，无历史分位）｜负 Gamma 加深（371万）｜现价位于 Flip 下方 3.93%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 205.0P — Vol 2,135 | 最新价 $13.37 | OI 592→2098 (ΔOI +1506张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1506张（+254.4% vs前日OI），连续性待观察（方向未知）
11-20 90.0P — Vol 939 | 最新价 $0.07 | OI 1401→2309 (ΔOI +908张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增908张（+64.8% vs前日OI），连续性待观察（方向未知）
11-06 250.0C — Vol 3,068 | 最新价 $0.77 | OI 2498→3398 (ΔOI +900张) | ΔOI/Volume 29.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增900张（+36.0% vs前日OI），连续性待观察（方向未知）
11-20 80.0P — Vol 913 | 最新价 $0.04 | OI 193→981 (ΔOI +788张) | ΔOI/Volume 86.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增788张（+408.3% vs前日OI），连续性待观察（方向未知）
11-06 227.5C — Vol 1,298 | 最新价 $4.15 | OI 320→1086 (ΔOI +766张) | ΔOI/Volume 59.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增766张（+239.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,868 张（Put 3,202 / Call 1,666），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +6.0k / P +2.5k ｜ Activity HIGH ｜ 2D
11-13  C +1.2k / P +1.2k ｜ Activity HIGH ｜ 9D
11-20  C +0.9k / P +3.1k ｜ Activity HIGH ｜ 16D
11-27  C +0.3k / P +48 ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 49.2k / P 33.3k，今日变化ΔOI: C +6.0k / P +2.5k，平值价格ATM: C $7.70 / P $7.31 ｜ ATM IV 116.9%，净 delta 敞口 -15k shares
Top ΔOI: C 227 +766
仓位参考: Max Pain 215 ｜ Call Wall 225（+9.9%，弱）（OI 3.4k） ｜ Put Wall 190（-7.2%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 116.9%｜历史 Rank 75%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 15,042 股

📆 11-13 Forward Structure
存量OI: C 13.3k / P 12.5k，今日变化ΔOI: C +1.2k / P +1.2k，平值价格ATM: C $12.60 / P $13.28 ｜ ATM IV 97.6%，净 delta 敞口 -19k shares
Top ΔOI: P 210 +403 ｜ C 235 +241
仓位参考: Max Pain 232 ｜ Call Wall 222.5（+8.6%，弱）（OI 0.6k） ｜ Put Wall 210（+2.5%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 97.6%｜历史 Rank 75%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 19,448 股

📆 11-20 Forward Structure
存量OI: C 63.0k / P 75.5k，今日变化ΔOI: C +0.9k / P +3.1k，平值价格ATM: C $16.09 / P $15.75 ｜ ATM IV 93.5%，净 delta 敞口 -31k shares
Top ΔOI: P 205 +1,506
仓位参考: Max Pain 230 ｜ Call Wall 220（+7.4%，弱）（OI 2.6k） ｜ Put Wall 200（-2.3%，弱）（OI 5.8k）
量化解读： 存量 Put 重｜ATM IV 93.5%｜历史 Rank 75%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 31,206 股

11-27（MEDIUM △）Top ΔOI: 260C +127
11-27（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 225（+9.9%，弱）（OI 0.4k） ｜ Put Wall 200（-2.3%，弱）（OI 1.6k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 116.9% vs 11-13 97.6%（差 +19.3pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/BE_morning.json