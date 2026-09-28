# 期权晚报 2026-09-28（快照 16:40 ET）

📊 市场环境

SPY $765.61 ｜ QQQ $736.53
VIX 16.07 ↑8.1%（5D +8.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-30 375C ΔOI +2,529（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-07 400C ΔOI +452 占该期限总 OI 18.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 368.06 → 收盘 357.45（-2.9%） ｜ 今日高 369.43 ｜ 低 356.80 ｜ 昨收 372.11 → 收盘 357.45（-3.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.66 | OI比 0.52 | ATM IV 33.5% | Skew 3.7pp | Term 1.34 | ExpMove ±2.5%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常偏陡（Term 1.34）｜保护溢价中性（Skew 3.7pp）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（2D）±2.5% ｜ 10-02（4D）±3.8% ｜ 10-05（7D）±4.3% ｜ 10-07（9D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 13,540,437 | GEX Change vs 上次快照 -14,537,250 | Flip: Primary Flip: 353.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 1134 / LOW 126 / INVALID 602
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 353.93（全链重定价，覆盖 91%）
最近结构参考: Flip 354（现价高于该位 1.0%）
量化视角： 正 Gamma（1354万，无历史分位）｜正 Gamma 减弱（1454万）｜现价位于 Flip 上方 1.00%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 372（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 354（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 235.0P — Vol 56 | 最新价 $0.02 | OI 383→23020 (ΔOI +22637张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22637张（+5910.4% vs前日OI），连续性待观察（方向未知）
10-02 150.0P — Vol 10 | 最新价 $0.01 | OI 3623→24140 (ΔOI +20517张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20517张（+566.3% vs前日OI），连续性待观察（方向未知）
10-02 130.0P — Vol 17,565（Yahoo补） | 最新价 $0.01 | OI 2179→19744 (ΔOI +17565张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17565张（+806.1% vs前日OI），连续性待观察（方向未知）
10-02 390.0C — Vol 6,382 | 最新价 $0.47 | OI 3881→16113 (ΔOI +12232张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12232张（+315.2% vs前日OI），连续性待观察（方向未知）
10-02 377.5C — Vol 4,732 | 最新价 $1.32 | OI 1073→12791 (ΔOI +11718张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11718张（+1092.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 84,669 张（Put 60,719 / Call 23,950），跨 1 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-30  C +17.4k / P +12.1k ｜ Activity HIGH ｜ 2D
10-02  C +45.6k / P +92.2k ｜ Activity HIGH ｜ 4D
10-05  C +4.8k / P +1.9k ｜ Activity HIGH ｜ 7D
10-07  C +1.5k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 09-30 Forward Structure
存量OI: C 38.9k / P 27.3k，今日变化ΔOI: C +17.4k / P +12.1k，平值价格ATM: C $4.40 / P $4.46 ｜ ATM IV 41.4%，净 delta 敞口 -148k shares
Top ΔOI: C 375 +2,529
仓位参考: Max Pain 372 ｜ Call Wall 380（+6.3%，弱）（OI 3.3k） ｜ Put Wall 360（+0.7%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 41.4%｜历史 Rank 5%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 148,425 股

📆 10-02 Forward Structure
存量OI: C 169.4k / P 218.0k，今日变化ΔOI: C +45.6k / P +92.2k，平值价格ATM: C $6.90 / P $6.80 ｜ ATM IV 45.4%，净 delta 敞口 -485k shares
仓位参考: Max Pain 365 ｜ Call Wall 390（+9.1%，弱）（OI 16.1k）
量化解读： 存量 Put 重｜ATM IV 45.4%｜历史 Rank 5%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 485,122 股

📆 10-05 Forward Structure
存量OI: C 11.4k / P 7.7k，今日变化ΔOI: C +4.8k / P +1.9k，平值价格ATM: C $7.88 / P $7.62 ｜ ATM IV 39.1%，净 delta 敞口 -20k shares
Top ΔOI: C 390 +876
仓位参考: Max Pain 375 ｜ Call Wall 390（+9.1%，弱）（OI 1.4k） ｜ Put Wall 375（+4.9%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 39.1%｜历史 Rank 5%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 20,420 股

📆 10-07 Forward Structure
存量OI: C 1.8k / P 0.7k，今日变化ΔOI: C +1.5k / P +0.5k，平值价格ATM: C $9.09 / P $8.60 ｜ ATM IV 40.1%，净 delta 敞口 -2k shares
Top ΔOI: C 375 +154
仓位参考: Max Pain 370 ｜ Call Wall 375（+4.9%，弱）（OI 0.2k） ｜ Put Wall 360（+0.7%，弱）（OI 90）
量化解读： 存量 Call 重｜ATM IV 40.1%｜历史 Rank 5%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 1,906 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/TSLA_evening.json