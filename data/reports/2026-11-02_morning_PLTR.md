# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　✅ 今日已公布
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **事件差分**: 11-06（4D）ATM IV 142.7% vs 11-13 97.6%（差 +45.1pp），覆盖 ISM 制造业 PMI、Midterm Elections 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-06 187C ΔOI +10,604（距现价 +1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 184.11 → 今开 186.52（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 186.95 ｜ 低 181.63

Options: P/C成交量 1.87 | OI比 0.86 | ATM IV 142.7% | Skew 12.1pp | Term 0.48 | ExpMove ±12.3%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜保护溢价显著（Skew 12.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.87）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.87×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（4D）±12.3% ｜ 11-13（11D）±13.8% ｜ 11-20（18D）±14.9% ｜ 11-27（25D）±15.4%
   ⇒ IV–VIX Spread: +123.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 13,091,459 | GEX Change vs 上次快照 9,083,666 | Flip: Primary Flip: 171.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 745 / LOW 13 / INVALID 148
结构观察区: Primary Flip 171.85（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 7.9%）
最近结构参考: Flip 172（现价高于该位 7.2%）
量化视角： 正 Gamma（1309万，无历史分位）｜正 Gamma 增强（+908万）｜现价位于 Flip 上方 7.23%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考） / 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 172（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 100.0P — Vol 18,496 | 最新价 $0.18 | OI 7196→22816 (ΔOI +15620张) | ΔOI/Volume 84.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15620张（+217.1% vs前日OI），连续性待观察（方向未知）
11-06 195.0C — Vol 12,375 | 最新价 $7.69 | OI 2180→12961 (ΔOI +10781张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10781张（+494.5% vs前日OI），连续性待观察（方向未知）
11-06 187.5C — Vol 11,606 | 最新价 $10.73 | OI 400→11004 (ΔOI +10604张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10604张（+2651.0% vs前日OI），连续性待观察（方向未知）
11-06 190.0C — Vol 8,365 | 最新价 $9.65 | OI 981→7160 (ΔOI +6179张) | ΔOI/Volume 73.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6179张（+629.9% vs前日OI），连续性待观察（方向未知）
11-06 197.5C — Vol 6,389 | 最新价 $6.80 | OI 1406→6647 (ΔOI +5241张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5241张（+372.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 48,425 张（Put 15,620 / Call 32,805），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +45.5k / P +41.0k ｜ Activity HIGH ｜ 4D
11-13  C +4.7k / P +3.7k ｜ Activity HIGH ｜ 11D
11-20  C -0.6k / P +3.1k ｜ Activity HIGH ｜ 18D
11-27  C +0.5k / P +1.5k ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 121.6k / P 104.7k，今日变化ΔOI: C +45.5k / P +41.0k，平值价格ATM: C $10.81 / P $11.82 ｜ ATM IV 142.7%，净 delta 敞口 1.5M shares
Top ΔOI: P 100 +15,620 ｜ C 195 +10,781 ｜ C 187 +10,604
仓位参考: Max Pain 188 ｜ Call Wall 195（+5.8%，弱）（OI 13.0k）
量化解读： 存量两侧均衡｜ATM IV 142.7%｜历史 Rank 100%（近端代理）｜IV/RV 2.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,450,369 股

📆 11-13 Forward Structure
存量OI: C 24.1k / P 23.4k，今日变化ΔOI: C +4.7k / P +3.7k，平值价格ATM: C $12.35 / P $12.98 ｜ ATM IV 97.6%，净 delta 敞口 40k shares
Top ΔOI: C 260 +1,936
仓位参考: Max Pain 192 ｜ Call Wall 197.5（+7.2%，弱）（OI 0.8k） ｜ Put Wall 180（-2.3%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 97.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,726 股

📆 11-20 Forward Structure
存量OI: C 165.4k / P 170.1k，今日变化ΔOI: C -0.6k / P +3.1k，平值价格ATM: C $13.45 / P $14.00 ｜ ATM IV 83.5%，净 delta 敞口 -123k shares
Top ΔOI: P 160 +1,750 ｜ C 230 -772 ｜ C 190 +768
仓位参考: Max Pain 175 ｜ Call Wall 200（+8.5%，弱）（OI 12.4k） ｜ Put Wall 180（-2.3%，弱）（OI 10.5k）
量化解读： 存量两侧均衡｜ATM IV 83.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 123,312 股

📆 11-27 Forward Structure
存量OI: C 10.4k / P 11.8k，今日变化ΔOI: C +0.5k / P +1.5k，平值价格ATM: C $14.05 / P $14.35 ｜ ATM IV 73.5%，净 delta 敞口 -27k shares
Top ΔOI: P 175 +369
仓位参考: Max Pain 195 ｜ Call Wall 200（+8.5%，弱）（OI 0.5k） ｜ Put Wall 180（-2.3%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 73.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.46×（近似）｜净 delta 敞口 负 26,690 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 142.7% vs 11-13 97.6%（差 +45.1pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/PLTR_morning.json