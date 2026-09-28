# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $767.62 ｜ QQQ $737.21
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.8（fear）
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
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-30 375C ΔOI +2,529（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-07 400C ΔOI +452 占该期限总 OI 18.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 372.11 → 今开 368.06（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 369.43 ｜ 低 360.72

Options: P/C成交量 0.96 | OI比 0.52 | ATM IV 52.4% | Skew -4.2pp | Term 0.84 | ExpMove ±2.8%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.96×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-30（2D）±2.8% ｜ 10-02（4D）±4.3% ｜ 10-05（7D）±4.7% ｜ 10-07（9D）±5.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,077,687 | GEX Change vs 上次快照 -3,067,103 | Flip: Primary Flip: 357.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1215 / LOW 98 / INVALID 549
结构观察区: Primary Flip 357.53（全链重定价，覆盖 98%）
最近结构参考: Flip 358（现价高于该位 1.4%）
量化视角： 正 Gamma（2808万，无历史分位）｜正 Gamma 减弱（307万）｜现价位于 Flip 上方 1.40%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 372（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 358（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 235.0P — Vol 23,054 | 最新价 $0.04 | OI 383→23020 (ΔOI +22637张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22637张（+5910.4% vs前日OI），连续性待观察（方向未知）
10-02 150.0P — Vol 21,916 | 最新价 $0.01 | OI 3623→24140 (ΔOI +20517张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20517张（+566.3% vs前日OI），连续性待观察（方向未知）
10-02 130.0P — Vol 17,565 | 最新价 $0.01 | OI 2179→19744 (ΔOI +17565张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17565张（+806.1% vs前日OI），连续性待观察（方向未知）
10-02 390.0C — Vol 19,181 | 最新价 $2.87 | OI 3881→16113 (ΔOI +12232张) | ΔOI/Volume 63.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12232张（+315.2% vs前日OI），连续性待观察（方向未知）
10-02 377.5C — Vol 15,184 | 最新价 $6.40 | OI 1073→12791 (ΔOI +11718张) | ΔOI/Volume 77.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11718张（+1092.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 84,669 张（Put 60,719 / Call 23,950），跨 1 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 88.9k / P 46.5k，今日成交量: C 175.1k / P 167.3k，平值价格ATM: C $2.00 / P $2.13 ｜ ATM IV 52.4%，预期波动 ±1.1%，Max Pain 372
Top ΔOI: C 420 +8,221 ｜ C 390 +7,523 ｜ C 385 +4,212

📆 Forward Expiration Structure

09-30  C +17.4k / P +12.1k ｜ Activity HIGH ｜ 2D
10-02  C +45.6k / P +92.2k ｜ Activity HIGH ｜ 4D
10-05  C +4.8k / P +1.9k ｜ Activity HIGH ｜ 7D
10-07  C +1.5k / P +0.5k ｜ Activity HIGH ｜ 9D

📆 09-30 Forward Structure
存量OI: C 38.9k / P 27.3k，今日变化ΔOI: C +17.4k / P +12.1k，平值价格ATM: C $4.95 / P $5.15 ｜ ATM IV 44.0%，净 delta 敞口 3k shares
Top ΔOI: C 375 +2,529
仓位参考: Max Pain 372 ｜ Call Wall 380（+4.8%，弱）（OI 3.3k） ｜ Put Wall 360（-0.7%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 44.0%｜历史 Rank 52%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,144 股

📆 10-02 Forward Structure
存量OI: C 169.4k / P 218.0k，今日变化ΔOI: C +45.6k / P +92.2k，平值价格ATM: C $7.95 / P $7.70 ｜ ATM IV 50.3%，净 delta 敞口 -147k shares
Top ΔOI: P 235 +22,637
仓位参考: Max Pain 365 ｜ Call Wall 390（+7.6%，弱）（OI 16.1k）
量化解读： 存量 Put 重｜ATM IV 50.3%｜历史 Rank 52%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 147,413 股

📆 10-05 Forward Structure
存量OI: C 11.4k / P 7.7k，今日变化ΔOI: C +4.8k / P +1.9k，平值价格ATM: C $8.70 / P $8.45 ｜ ATM IV 42.0%，净 delta 敞口 14k shares
Top ΔOI: C 400 +1,052 ｜ C 390 +876
仓位参考: Max Pain 375 ｜ Call Wall 390（+7.6%，弱）（OI 1.4k） ｜ Put Wall 375（+3.4%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 42.0%｜历史 Rank 52%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,983 股

📆 10-07 Forward Structure
存量OI: C 1.8k / P 0.7k，今日变化ΔOI: C +1.5k / P +0.5k，平值价格ATM: C $9.95 / P $9.30 ｜ ATM IV 41.7%，净 delta 敞口 9k shares
Top ΔOI: C 400 +452 ｜ C 375 +154
仓位参考: Max Pain 370 ｜ Call Wall 375（+3.4%，弱）（OI 0.2k） ｜ Put Wall 360（-0.7%，弱）（OI 90）
量化解读： 存量 Call 重｜ATM IV 41.7%｜历史 Rank 52%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 8,605 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/TSLA_morning.json