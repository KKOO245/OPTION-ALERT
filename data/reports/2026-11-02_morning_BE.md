# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $760.66 ｜ QQQ $699.02
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.4（fear）
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
🟡 **事件差分**: 11-06 ATM IV 105.0% vs 11-13 92.9%（差 +12.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 207C ΔOI +1,146（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 203.17 → 今开 206.03（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 207.78 ｜ 低 199.00

Options: P/C成交量 0.53 | OI比 0.90 | ATM IV 105.1% | Skew 7.9pp | Term 0.80 | ExpMove ±9.4%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 7.9pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（4D）±9.4% ｜ 11-13（11D）±12.2% ｜ 11-20（18D）±16.2% ｜ 11-27（25D）±17.5%
   ⇒ IV–VIX Spread: +86.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,637,796 | GEX Change vs 上次快照 344,851 | Flip: Primary Flip: 225.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 521 / LOW 99 / INVALID 226
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 225.69（全链重定价，覆盖 100%）
Put Wall 200（现价高于该位 1.0%）
最近结构参考: Put Wall 200（现价高于该位 1.0%）
量化视角： 负 Gamma（564万，无历史分位）｜负 Gamma 缓解（+34万）｜现价位于 Flip 下方 10.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 218（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 226（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 140.0P — Vol 1,526 | 最新价 $2.70 | OI 43→1566 (ΔOI +1523张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1523张（+3541.9% vs前日OI），连续性待观察（方向未知）
11-06 175.0C — Vol 1,402 | 最新价 $28.33 | OI 6→1406 (ΔOI +1400张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1400张（+23333.3% vs前日OI），连续性待观察（方向未知）
11-06 207.5C — Vol 1,564 | 最新价 $7.89 | OI 90→1236 (ΔOI +1146张) | ΔOI/Volume 73.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1146张（+1273.3% vs前日OI），连续性待观察（方向未知）
11-06 215.0C — Vol 1,842 | 最新价 $5.35 | OI 217→1357 (ΔOI +1140张) | ΔOI/Volume 61.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1140张（+525.4% vs前日OI），连续性待观察（方向未知）
11-06 167.5C — Vol 1,053 | 最新价 $35.38 | OI 1→1053 (ΔOI +1052张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1052张（+105200.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,261 张（Put 1,523 / Call 4,738），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +9.8k / P +6.2k ｜ Activity HIGH ｜ 4D
11-13  C +1.7k / P +1.4k ｜ Activity MEDIUM △ ｜ 11D
11-20  C +1.8k / P +1.2k ｜ Activity HIGH ｜ 18D
11-27  C +0.4k / P -0.4k ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 30.4k / P 27.4k，今日变化ΔOI: C +9.8k / P +6.2k，平值价格ATM: C $9.20 / P $9.85 ｜ ATM IV 105.0%，净 delta 敞口 272k shares
Top ΔOI: C 175 +1,400 ｜ C 207 +1,146 ｜ C 215 +1,140
仓位参考: Max Pain 218 ｜ Call Wall 200（-1.0%，弱）（OI 1.4k） ｜ Put Wall 200（-1.0%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜ATM IV 105.0%｜历史 Rank 66%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 272,146 股

11-13（MEDIUM △）Top ΔOI: 222C +648 ｜ 232P +254
11-13（MEDIUM △）仓位参考: Max Pain 235 ｜ Call Wall 220（+8.9%，弱）（OI 0.4k） ｜ Put Wall 200（-1.0%，弱）（OI 0.6k）

📆 11-20 Forward Structure
存量OI: C 61.4k / P 72.3k，今日变化ΔOI: C +1.8k / P +1.2k，平值价格ATM: C $17.35 / P $15.45 ｜ ATM IV 88.8%，净 delta 敞口 86k shares
Top ΔOI: P 205 -590 ｜ P 150 +501 ｜ P 200 +452
仓位参考: Max Pain 230 ｜ Call Wall 200（-1.0%，弱）（OI 2.0k） ｜ Put Wall 200（-1.0%，弱）（OI 5.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 88.8%｜历史 Rank 66%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 85,560 股

11-27（MEDIUM △）Top ΔOI: 190P -759 ｜ 265C +236
11-27（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 215（+6.4%，弱）（OI 0.2k） ｜ Put Wall 200（-1.0%，弱）（OI 1.6k）

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 105.0% vs 11-13 92.9%（差 +12.1pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/BE_morning.json