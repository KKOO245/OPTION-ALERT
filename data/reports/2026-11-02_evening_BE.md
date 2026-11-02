# 期权晚报 2026-11-02（快照 16:40 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 21.15 ↑8.9%（5D +15.0%） ｜ Vol Regime: ELEVATED
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
🔴 **事件差分**: 11-06（4D）ATM IV 121.2% vs 11-13 103.9%（差 +17.3pp），覆盖 ISM 制造业 PMI、Midterm Elections 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-20 205P ΔOI -590（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 206.03 → 收盘 196.25（-4.7%） ｜ 今日高 210.09 ｜ 低 194.87 ｜ 昨收 203.17 → 收盘 196.25（-3.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.54 | OI比 0.90 | ATM IV 121.2% | Skew 11.0pp | Term 0.75 | ExpMove ±10.1%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价显著（Skew 11.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（4D）±10.1% ｜ 11-13（11D）±14.3% ｜ 11-20（18D）±17.2% ｜ 11-27（25D）±19.2%
   ⇒ IV–VIX Spread: +100.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,655,672 | GEX Change vs 上次快照 -17,876 | Flip: Primary Flip: 224.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 547 / LOW 88 / INVALID 211
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 224.15（全链重定价，覆盖 100%）
Put Wall 200（现价低于该位 1.9%）
最近结构参考: Put Wall 200（现价低于该位 1.9%）
量化视角： 负 Gamma（566万，无历史分位）｜负 Gamma 加深（2万）｜现价位于 Flip 下方 12.45%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall） / 218（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 224（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 140.0P — Vol 56 | 最新价 $2.69 | OI 43→1566 (ΔOI +1523张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1523张（+3541.9% vs前日OI），连续性待观察（方向未知）
11-06 175.0C — Vol 17 | 最新价 $24.89 | OI 6→1406 (ΔOI +1400张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1400张（+23333.3% vs前日OI），连续性待观察（方向未知）
11-06 207.5C — Vol 706 | 最新价 $5.33 | OI 90→1236 (ΔOI +1146张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1146张（+1273.3% vs前日OI），连续性待观察（方向未知）
11-06 215.0C — Vol 1,848 | 最新价 $3.30 | OI 217→1357 (ΔOI +1140张) | ΔOI/Volume 61.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1140张（+525.4% vs前日OI），连续性待观察（方向未知）
11-06 167.5C — Vol 10 | 最新价 $31.60 | OI 1→1053 (ΔOI +1052张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1052张（+105200.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,261 张（Put 1,523 / Call 4,738），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +9.8k / P +6.2k ｜ Activity HIGH ｜ 4D
11-13  C +1.7k / P +1.4k ｜ Activity HIGH ｜ 11D
11-20  C +1.8k / P +1.2k ｜ Activity HIGH ｜ 18D
11-27  C +0.4k / P -0.4k ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 30.4k / P 27.4k，今日变化ΔOI: C +9.8k / P +6.2k，平值价格ATM: C $10.50 / P $9.35 ｜ ATM IV 121.2%，净 delta 敞口 181k shares
Top ΔOI: C 175 +1,400 ｜ C 207 +1,146 ｜ C 215 +1,140
仓位参考: Max Pain 218 ｜ Call Wall 200（+1.9%，弱）（OI 1.4k） ｜ Put Wall 200（+1.9%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜ATM IV 121.2%｜历史 Rank 79%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 180,809 股

📆 11-13 Forward Structure
存量OI: C 11.3k / P 10.3k，今日变化ΔOI: C +1.7k / P +1.4k，平值价格ATM: C $14.40 / P $13.68 ｜ ATM IV 103.9%，净 delta 敞口 -45k shares
Top ΔOI: C 222 +648 ｜ P 232 +254
仓位参考: Max Pain 235 ｜ Call Wall 215（+9.6%，弱）（OI 0.2k） ｜ Put Wall 200（+1.9%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 103.9%｜历史 Rank 79%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 44,508 股

📆 11-20 Forward Structure
存量OI: C 61.4k / P 72.3k，今日变化ΔOI: C +1.8k / P +1.2k，平值价格ATM: C $17.61 / P $16.25 ｜ ATM IV 98.9%，净 delta 敞口 76k shares
Top ΔOI: P 205 -590 ｜ P 150 +501 ｜ P 200 +452
仓位参考: Max Pain 230 ｜ Call Wall 200（+1.9%，弱）（OI 2.0k） ｜ Put Wall 200（+1.9%，弱）（OI 5.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 98.9%｜历史 Rank 79%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 76,009 股

📆 11-27 Forward Structure
存量OI: C 5.4k / P 8.5k，今日变化ΔOI: C +0.4k / P -0.4k，平值价格ATM: C $19.70 / P $18.00 ｜ ATM IV 91.8%，净 delta 敞口 22k shares
Top ΔOI: P 190 -759 ｜ C 265 +236 ｜ C 225 -132
仓位参考: Max Pain 230 ｜ Call Wall 215（+9.6%，弱）（OI 0.2k） ｜ Put Wall 200（+1.9%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 91.8%｜历史 Rank 79%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 22,036 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 121.2% vs 11-13 103.9%（差 +17.3pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/BE_evening.json