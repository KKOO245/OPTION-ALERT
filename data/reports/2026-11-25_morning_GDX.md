# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $701.98 ｜ QQQ $610.46
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🔵 **期限 OI 集中**: 11-30 80C ΔOI +1,038 占该期限总 OI 18.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 71.37 → 今开 68.76（-3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 69.36 ｜ 低 67.93

Options: P/C成交量 0.69 | OI比 0.63 | ATM IV 87.3% | Skew 9.4pp | Term 0.59 | ExpMove ±3.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价显著（Skew 9.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±3.4% ｜ 11-30（5D）±4.8% ｜ 12-02（7D）±3.9% ｜ 12-04（9D）±7.9%
   ⇒ IV–VIX Spread: +55.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -31,186,413 | GEX Change vs 上次快照 -24,887,885 | Flip: Primary Flip: 71.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 529 / LOW 246 / INVALID 537
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 71.69（全链重定价，覆盖 94%）
最近结构参考: Flip 72（现价低于该位 3.4%）
量化视角： 负 Gamma（3119万，无历史分位）｜负 Gamma 加深（2489万）｜现价位于 Flip 下方 3.38%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 72（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 72（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 65.0P — Vol 1,674 | 最新价 $0.05 | OI 331→1863 (ΔOI +1532张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1532张（+462.8% vs前日OI），连续性待观察（方向未知）
11-25 75.0C — Vol 1,352 | 最新价 $0.08 | OI 938→2190 (ΔOI +1252张) | ΔOI/Volume 92.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1252张（+133.5% vs前日OI），连续性待观察（方向未知）
11-27 35.0P — Vol 1,111 | 最新价 $0.01 | OI 1→1112 (ΔOI +1111张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1111张（+111100.0% vs前日OI），连续性待观察（方向未知）
11-30 80.0C — Vol 1,044 | 最新价 $0.04 | OI 702→1740 (ΔOI +1038张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1038张（+147.9% vs前日OI），连续性待观察（方向未知）
11-25 67.0P — Vol 827 | 最新价 $0.06 | OI 24→839 (ΔOI +815张) | ΔOI/Volume 98.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增815张（+3395.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,748 张（Put 3,458 / Call 2,290），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 7.3k / P 4.6k，今日成交量: C 4.0k / P 2.8k，平值价格ATM: C $0.80 / P $0.52 ｜ ATM IV 87.3%，预期波动 ±1.9%，Max Pain 72
Top ΔOI: C 75 +1,252 ｜ P 67 +815 ｜ P 64 +792

📆 Forward Expiration Structure

11-27  C -5.7k / P +1.4k ｜ Activity HIGH ｜ 2D
11-30  C +1.1k / P +0.5k ｜ Activity HIGH ｜ 5D
12-02  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 7D
12-04  C +0.4k / P -0.1k ｜ Activity LOW ｜ 9D

📆 11-27 Forward Structure
存量OI: C 85.0k / P 15.0k，今日变化ΔOI: C -5.7k / P +1.4k，平值价格ATM: C $1.31 / P $1.03 ｜ ATM IV 52.1%，净 delta 敞口 169k shares
Top ΔOI: P 65 +1,532
仓位参考: Max Pain 71 ｜ Call Wall 71（+2.5%，弱）（OI 15.0k） ｜ Put Wall 70（+1.1%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.1%｜历史 Rank 100%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 169,006 股

📆 11-30 Forward Structure
存量OI: C 3.4k / P 2.2k，今日变化ΔOI: C +1.1k / P +0.5k，平值价格ATM: C $1.41 / P $1.90 ｜ ATM IV 49.1%，净 delta 敞口 -10k shares
Top ΔOI: P 65 +301 ｜ P 70 +96
仓位参考: Max Pain 72 ｜ Put Wall 65（-6.2%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 49.1%｜历史 Rank 100%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 9,819 股

12-02（MEDIUM △）Top ΔOI: 71P +250 ｜ 75C +55
12-02（MEDIUM △）仓位参考: Max Pain 73 ｜ Call Wall 73（+5.4%，弱）（OI 0.1k） ｜ Put Wall 71（+2.5%）（OI 0.3k）

12-04（Activity LOW）仓位参考: Max Pain 76 ｜ Put Wall 70（+1.1%）（OI 6.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/GDX_morning.json