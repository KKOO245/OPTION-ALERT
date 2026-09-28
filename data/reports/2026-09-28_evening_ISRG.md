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
🟡 **近现价集中开仓**: 10-02 420C ΔOI +90（距现价 +1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 405.18 → 收盘 414.79（+2.4%） ｜ 今日高 416.51 ｜ 低 402.75 ｜ 昨收 405.18 → 收盘 414.79（+2.4%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-10-01，窗口结束前不做对错判定）

Options: P/C成交量 0.21 | OI比 2.02 | ATM IV 39.1% | Skew 5.6pp | Term 1.09 | ExpMove ±3.3%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构正常（Term 1.09）｜保护溢价中性（Skew 5.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.02×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（4D）±3.3% ｜ 10-09（11D）±12.9% ｜ 10-16（18D）±6.1% ｜ 10-23（25D）±9.3%
   ⇒ IV–VIX Spread: +23.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,810,264 | GEX Change vs 上次快照 272,415 | Flip: Primary Flip: 386.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 237 / LOW 145 / INVALID 456
结构观察区: Primary Flip 386.21（全链重定价，覆盖 96%）
Call Wall 400（弱结构｜现价高于该位 3.7%）
最近结构参考: Call Wall 400（现价高于该位 3.7%）
量化视角： 正 Gamma（281万，无历史分位）｜正 Gamma 增强（+27万）｜现价位于 Flip 上方 7.40%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 385（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 386（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 397.5P — Vol 6 | 最新价 $5.37 | OI 13→266 (ΔOI +253张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增253张（+1946.2% vs前日OI），值得跟踪（方向未知）
10-02 402.5C — Vol 27 | 最新价 $15.37 | OI 11→161 (ΔOI +150张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增150张（+1363.6% vs前日OI），值得跟踪（方向未知）
10-16 410.0P — Vol 47 | 最新价 $9.50 | OI 122→239 (ΔOI +117张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增117张（+95.9% vs前日OI），值得跟踪（方向未知）
10-02 420.0C — Vol 202 | 最新价 $4.25 | OI 104→194 (ΔOI +90张) | ΔOI/Volume 44.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增90张（+86.5% vs前日OI），连续性待观察（方向未知）
10-16 405.0P — Vol 20 | 最新价 $8.00 | OI 44→124 (ΔOI +80张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增80张（+181.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 690 张（Put 450 / Call 240），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.5k / P +0.1k ｜ Activity HIGH ｜ 4D
10-09  C +73 / P +11 ｜ Activity HIGH ｜ 11D
10-16  C +96 / P +0.5k ｜ Activity HIGH ｜ 18D
10-23  C +40 / P +0.1k ｜ Activity HIGH ｜ 25D

📆 10-02 Forward Structure
存量OI: C 1.6k / P 3.3k，今日变化ΔOI: C +0.5k / P +0.1k，平值价格ATM: C $7.20 / P $6.55 ｜ ATM IV 39.1%，净 delta 敞口 27k shares
Top ΔOI: C 402 +150 ｜ C 420 +90 ｜ C 390 +44
仓位参考: Max Pain 385 ｜ Call Wall 410（-1.2%）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.1%｜历史 Rank 49%（近端代理）｜IV/RV 1.51×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 26,569 股

📆 10-09 Forward Structure
存量OI: C 1.1k / P 0.3k，今日变化ΔOI: C +73 / P +11，平值价格ATM: C $10.63 / P $43.00 ｜ ATM IV 30.6%，净 delta 敞口 3k shares
Top ΔOI: C 430 +19 ｜ C 420 +14 ｜ C 425 +14
仓位参考: Max Pain 370 ｜ Call Wall 420（+1.3%，弱）（OI 0.1k） ｜ Put Wall 385（-7.2%，弱）（OI 16）
量化解读： 存量 Call 重｜ATM IV 30.6%｜历史 Rank 49%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,219 股

📆 10-16 Forward Structure
存量OI: C 10.5k / P 9.3k，今日变化ΔOI: C +96 / P +0.5k，平值价格ATM: C $13.00 / P $12.20 ｜ ATM IV 34.3%，净 delta 敞口 -10k shares
Top ΔOI: P 397 +253 ｜ P 410 +117 ｜ P 405 +80
仓位参考: Max Pain 390 ｜ Call Wall 400（-3.6%，弱）（OI 1.0k） ｜ Put Wall 380（-8.4%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.3%｜历史 Rank 49%（近端代理）｜IV/RV 1.32×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 10,014 股

📆 10-23 Forward Structure
存量OI: C 0.8k / P 0.7k，今日变化ΔOI: C +40 / P +0.1k，平值价格ATM: C $20.05 / P $18.70 ｜ ATM IV 43.7%，净 delta 敞口 -836 shares
Top ΔOI: P 390 +73 ｜ C 390 +31
仓位参考: Max Pain 395 ｜ Call Wall 455（+9.7%，弱）（OI 88） ｜ Put Wall 420（+1.3%，弱）（OI 92）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.7%｜历史 Rank 49%（近端代理）｜IV/RV 1.68×（近似）｜净 delta 敞口 负 836 股

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 39.1% vs 10-09 30.6%（差 +8.5pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/ISRG_evening.json