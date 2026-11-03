# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $755.37 ｜ QQQ $685.28
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 420C ΔOI +3,751（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 403.82 → 今开 406.31（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 406.49 ｜ 低 400.91

Options: P/C成交量 1.03 | OI比 1.15 | ATM IV 69.5% | Skew 3.6pp | Term 0.64 | ExpMove ±3.3%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价中性（Skew 3.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（1D）±3.3% ｜ 11-06（3D）±4.6% ｜ 11-09（6D）±5.3% ｜ 11-11（8D）±6.2%
   ⇒ IV–VIX Spread: +48.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 73,081,047 | GEX Change vs 上次快照 2,573,943 | Flip: Primary Flip: 385.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1394 / LOW 88 / INVALID 722
结构观察区: Primary Flip 385.94（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价高于该位 0.7%）
最近结构参考: Call Wall 400（现价高于该位 0.7%）
量化视角： 正 Gamma（7308万，无历史分位）｜正 Gamma 增强（+257万）｜现价位于 Flip 上方 4.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 400（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 386（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 150.0P — Vol 10,446 | 最新价 $0.01 | OI 15218→25510 (ΔOI +10292张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10292张（+67.6% vs前日OI），连续性待观察（方向未知）
11-06 440.0C — Vol 13,300 | 最新价 $0.89 | OI 2635→10274 (ΔOI +7639张) | ΔOI/Volume 57.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7639张（+289.9% vs前日OI），连续性待观察（方向未知）
11-27 410.0C — Vol 10,526 | 最新价 $16.25 | OI 1556→8530 (ΔOI +6974张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6974张（+448.2% vs前日OI），连续性待观察（方向未知）
11-27 435.0C — Vol 5,165 | 最新价 $7.60 | OI 1033→5065 (ΔOI +4032张) | ΔOI/Volume 78.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4032张（+390.3% vs前日OI），连续性待观察（方向未知）
11-06 435.0C — Vol 7,507 | 最新价 $1.34 | OI 2603→6591 (ΔOI +3988张) | ΔOI/Volume 53.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3988张（+153.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,925 张（Put 10,292 / Call 22,633），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-04  C +24.1k / P +27.0k ｜ Activity HIGH ｜ 1D
11-06  C +35.9k / P +46.7k ｜ Activity HIGH ｜ 3D
11-09  C +8.1k / P +3.7k ｜ Activity HIGH ｜ 6D
11-11  C +2.7k / P +1.5k ｜ Activity HIGH ｜ 8D

📆 11-04 Forward Structure
存量OI: C 46.7k / P 53.6k，今日变化ΔOI: C +24.1k / P +27.0k，平值价格ATM: C $6.45 / P $6.75 ｜ ATM IV 69.5%，净 delta 敞口 -60k shares
Top ΔOI: C 420 +3,751 ｜ P 400 +2,199
仓位参考: Max Pain 400 ｜ Call Wall 420（+4.3%）（OI 5.6k） ｜ Put Wall 370（-8.1%，弱）（OI 4.4k）
量化解读： 存量两侧均衡｜ATM IV 69.5%｜历史 Rank 83%（近端代理）｜IV/RV 2.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 60,043 股

📆 11-06 Forward Structure
存量OI: C 158.3k / P 252.5k，今日变化ΔOI: C +35.9k / P +46.7k，平值价格ATM: C $9.25 / P $9.10 ｜ ATM IV 61.7%，净 delta 敞口 -305k shares
Top ΔOI: C 440 +7,639 ｜ C 435 +3,988
仓位参考: Max Pain 395 ｜ Call Wall 440（+9.2%，弱）（OI 10.3k） ｜ Put Wall 380（-5.7%，弱）（OI 10.4k）
量化解读： 存量 Put 重｜ATM IV 61.7%｜历史 Rank 83%（近端代理）｜IV/RV 1.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 304,949 股

📆 11-09 Forward Structure
存量OI: C 13.6k / P 9.6k，今日变化ΔOI: C +8.1k / P +3.7k，平值价格ATM: C $10.80 / P $10.45 ｜ ATM IV 50.4%，净 delta 敞口 35k shares
Top ΔOI: C 420 +927
仓位参考: Max Pain 400 ｜ Call Wall 420（+4.3%）（OI 1.8k） ｜ Put Wall 380（-5.7%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 50.4%｜历史 Rank 83%（近端代理）｜IV/RV 1.54×（近似）｜净 delta 敞口 正 34,751 股

📆 11-11 Forward Structure
存量OI: C 7.6k / P 4.3k，今日变化ΔOI: C +2.7k / P +1.5k，平值价格ATM: C $12.66 / P $12.20 ｜ ATM IV 50.9%，净 delta 敞口 -18k shares
Top ΔOI: P 405 +475 ｜ C 410 +425
仓位参考: Max Pain 400 ｜ Call Wall 405（+0.5%，弱）（OI 0.7k） ｜ Put Wall 405（+0.5%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 50.9%｜历史 Rank 83%（近端代理）｜IV/RV 1.56×（近似）｜净 delta 敞口 负 17,819 股

📅 事件差分（观察，非因果）: 11-04（1D）ATM IV 69.5% vs 11-06 61.7%（差 +7.8pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/TSLA_morning.json