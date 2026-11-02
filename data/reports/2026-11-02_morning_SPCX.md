# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $753.20 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 134P ΔOI +1,335（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 134.72 → 今开 137.04（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 141.70 ｜ 低 136.35

Options: P/C成交量 0.47 | OI比 1.01 | ATM IV 83.8% | Skew 6.0pp | Term 0.65 | ExpMove ±4.7%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价中性（Skew 6.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（2D）±4.7% ｜ 11-06（4D）±6.0% ｜ 11-09（7D）±7.0% ｜ 11-11（9D）±7.3%
   ⇒ IV–VIX Spread: +65.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -26,376,689 | GEX Change vs 上次快照 31,854,576 | Flip: Primary Flip: 143.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 768 / LOW 187 / INVALID 473
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 143.58（全链重定价，覆盖 99%）
Put Wall 135（弱结构｜现价高于该位 3.9%）
最近结构参考: Flip 144（现价低于该位 2.3%）
量化视角： 负 Gamma（2638万，无历史分位）｜负 Gamma 缓解（+3185万）｜现价位于 Flip 下方 2.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构） / 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-02 85.0P — Vol 11,036 | 最新价 $0.01 | OI 13→11041 (ΔOI +11028张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11028张（+84830.8% vs前日OI），连续性待观察（方向未知）
11-06 80.0P — Vol 7,579 | 最新价 $0.05 | OI 156→7687 (ΔOI +7531张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7531张（+4827.6% vs前日OI），连续性待观察（方向未知）
11-06 140.0C — Vol 12,630 | 最新价 $2.34 | OI 884→7425 (ΔOI +6541张) | ΔOI/Volume 51.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6541张（+739.9% vs前日OI），连续性待观察（方向未知）
11-06 135.0P — Vol 11,111 | 最新价 $4.63 | OI 10615→16589 (ΔOI +5974张) | ΔOI/Volume 53.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5974张（+56.3% vs前日OI），连续性待观察（方向未知）
11-06 115.0P — Vol 8,630 | 最新价 $0.43 | OI 3789→9365 (ΔOI +5576张) | ΔOI/Volume 64.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5576张（+147.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,650 张（Put 30,109 / Call 6,541），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 45.6k / P 46.0k，今日成交量: C 80.9k / P 48.8k，平值价格ATM: C $1.31 / P $1.22 ｜ ATM IV 83.8%，预期波动 ±1.8%，Max Pain 140
Top ΔOI: P 85 +11,028 ｜ P 120 +2,665 ｜ C 157 -2,333

📆 Forward Expiration Structure

11-04  C +5.4k / P +11.8k ｜ Activity HIGH ｜ 2D
11-06  C +31.3k / P +46.4k ｜ Activity HIGH ｜ 4D
11-09  C +1.4k / P +1.1k ｜ Activity HIGH ｜ 7D
11-11  C +0.9k / P +0.7k ｜ Activity HIGH ｜ 9D

📆 11-04 Forward Structure
存量OI: C 18.9k / P 23.5k，今日变化ΔOI: C +5.4k / P +11.8k，平值价格ATM: C $3.37 / P $3.18 ｜ ATM IV 75.2%，净 delta 敞口 85k shares
Top ΔOI: P 125 +3,504 ｜ P 134 +1,335
仓位参考: Max Pain 143 ｜ Call Wall 145（+3.4%，弱）（OI 2.0k） ｜ Put Wall 140（-0.1%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 75.2%｜历史 Rank 95%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 84,575 股

📆 11-06 Forward Structure
存量OI: C 169.3k / P 147.1k，今日变化ΔOI: C +31.3k / P +46.4k，平值价格ATM: C $4.32 / P $4.05 ｜ ATM IV 69.5%，净 delta 敞口 640k shares
Top ΔOI: C 140 +6,541 ｜ P 135 +5,974
仓位参考: Max Pain 145 ｜ Call Wall 150（+7.0%，弱）（OI 12.6k） ｜ Put Wall 140（-0.1%，弱）（OI 17.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.5%｜历史 Rank 95%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 639,902 股

📆 11-09 Forward Structure
存量OI: C 5.5k / P 3.6k，今日变化ΔOI: C +1.4k / P +1.1k，平值价格ATM: C $5.10 / P $4.65 ｜ ATM IV 59.1%，净 delta 敞口 22k shares
Top ΔOI: C 150 +322 ｜ P 135 +211 ｜ C 140 +199
仓位参考: Max Pain 144 ｜ Call Wall 150（+7.0%，弱）（OI 0.6k） ｜ Put Wall 134（-4.4%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 59.1%｜历史 Rank 95%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 21,995 股

📆 11-11 Forward Structure
存量OI: C 2.1k / P 1.5k，今日变化ΔOI: C +0.9k / P +0.7k，平值价格ATM: C $5.25 / P $5.00 ｜ ATM IV 59.0%，净 delta 敞口 8k shares
Top ΔOI: C 150 +274 ｜ C 145 +118 ｜ P 150 +98
仓位参考: Max Pain 142 ｜ Call Wall 150（+7.0%，弱）（OI 0.4k） ｜ Put Wall 135（-3.7%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 59.0%｜历史 Rank 95%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 7,546 股

📅 事件差分（观察，非因果）: 11-04（2D）ATM IV 75.2% vs 11-06 69.5%（差 +5.7pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/SPCX_morning.json