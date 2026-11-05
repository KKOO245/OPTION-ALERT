# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $752.25 ｜ QQQ $657.51
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 90.5% vs 11-13 71.1%（差 +19.4pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🔵 **期限 OI 集中**: 11-06 360P ΔOI -38,114 占该期限总 OI 33.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 450.41 → 今开 142.96（-68.3%） | 较昨收变动（含盘初走势） ｜ 今日高 143.73 ｜ 低 136.88

Options: P/C成交量 4.68 | OI比 1.64 | ATM IV 90.5% | Skew 12.4pp | Term 0.57 | ExpMove ±2.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价显著（Skew 12.4pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 4.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.68×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.64×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±2.2% ｜ 11-13（8D）±3.9% ｜ 11-20（15D）±4.8% ｜ 11-27（22D）±0.0%
   ⇒ IV–VIX Spread: +69.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -22,909,489 | GEX Change vs 上次快照 5,648,700 | Flip: Candidates 152.61 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 74%（带内） ｜ IV 有效性: VALID 191 / LOW 601 / INVALID 2250
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈153（全链重定价，覆盖 74%，CONDITIONAL）
最近结构参考: Flip 153（现价低于该位 8.9%）
量化视角： 负 Gamma（2291万，无历史分位）｜负 Gamma 缓解（+565万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 163（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 74%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 120.0P — Vol 0 | 最新价 $0.00 | OI 0→38096 (ΔOI +38096张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增38096张（前日OI缺失），值得跟踪（方向未知）
11-06 183.33C — Vol 0 | 最新价 $0.00 | OI 0→16413 (ΔOI +16413张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增16413张（前日OI缺失），值得跟踪（方向未知）
11-06 180.0C — Vol 0 | 最新价 $0.00 | OI 0→14200 (ΔOI +14200张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增14200张（前日OI缺失），值得跟踪（方向未知）
11-20 166.67C — Vol 0 | 最新价 $0.00 | OI 0→11528 (ΔOI +11528张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增11528张（前日OI缺失），值得跟踪（方向未知）
11-13 163.33C — Vol 0 | 最新价 $0.00 | OI 0→9682 (ΔOI +9682张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增9682张（前日OI缺失），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 89,919 张（Put 38,096 / Call 51,823），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C -42.8k / P -64.2k ｜ Activity HIGH ｜ 1D（新行权价 C 43.7k / P 71.8k）
11-13  C -31.0k / P -23.4k ｜ Activity HIGH ｜ 8D（新行权价 C 32.6k / P 25.2k）
11-20  C -46.5k / P -74.4k ｜ Activity HIGH ｜ 15D（新行权价 C 43.2k / P 75.0k）
11-27  C -8.2k / P -6.8k ｜ Activity HIGH ｜ 22D（新行权价 C 8.3k / P 7.9k）

📆 11-06 Forward Structure
存量OI: C 43.7k / P 71.8k，今日变化ΔOI: C -42.8k / P -64.2k（新行权价 C 43.7k / P 71.8k），平值价格ATM: C $0.00 / P $3.00 ｜ ATM IV 90.5%，净 delta 敞口 0 shares
Top ΔOI: P 360 -38,114 ｜ C 550 -16,413
仓位参考: Max Pain 163
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 90.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

📆 11-13 Forward Structure
存量OI: C 32.6k / P 25.2k，今日变化ΔOI: C -31.0k / P -23.4k（新行权价 C 32.6k / P 25.2k），平值价格ATM: C $0.00 / P $5.35 ｜ ATM IV 71.1%，净 delta 敞口 0 shares
Top ΔOI: C 490 -9,678 ｜ C 570 -6,433 ｜ P 415 -4,983
仓位参考: Max Pain 160 ｜ Put Wall 138.33（-0.5%，弱）（OI 5.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 71.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

📆 11-20 Forward Structure
存量OI: C 58.2k / P 79.0k，今日变化ΔOI: C -46.5k / P -74.4k（新行权价 C 43.2k / P 75.0k），平值价格ATM: C $0.00 / P $6.66 ｜ ATM IV 62.1%，净 delta 敞口 -118k shares
Top ΔOI: C 500 -12,393 ｜ P 460 -7,571 ｜ P 450 -6,995
仓位参考: Max Pain 167 ｜ Put Wall 143.33（+3.1%，弱）（OI 7.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 118,006 股

📆 11-27 Forward Structure
存量OI: C 8.3k / P 7.9k，今日变化ΔOI: C -8.2k / P -6.8k（新行权价 C 8.3k / P 7.9k），平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 62.5%，净 delta 敞口 0 shares
Top ΔOI: C 485 -3,453 ｜ P 500 -2,108 ｜ C 550 -1,801
仓位参考: Max Pain 162 ｜ Put Wall 146.67（+5.5%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 62.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 0 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 90.5% vs 11-13 71.1%（差 +19.4pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/SOXX_morning.json