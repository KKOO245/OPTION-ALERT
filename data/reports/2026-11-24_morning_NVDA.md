# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $718.15 ｜ QQQ $638.10
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-25 150P ΔOI +11,887（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 200C ΔOI +10,908 占该期限总 OI 15.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 165.05 → 今开 159.06（-3.6%） | 较昨收变动（含盘初走势） ｜ 今日高 159.92 ｜ 低 153.20

Options: P/C成交量 0.89 | OI比 0.85 | ATM IV 103.3% | Skew 8.3pp | Term 0.68 | ExpMove ±4.8%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价显著（Skew 8.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-25（1D）±4.8% ｜ 11-27（3D）±0.0% ｜ 11-30（6D）±7.3% ｜ 12-02（8D）±8.8%
   ⇒ IV–VIX Spread: +76.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 91,479,969 | GEX Change vs 上次快照 -135,579,443 | Flip: Primary Flip: 147.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1415 / LOW 170 / INVALID 937
结构观察区: Primary Flip 147.28（全链重定价，覆盖 100%）
最近结构参考: Flip 147（现价高于该位 5.3%）
量化视角： 正 Gamma（9148万，无历史分位）｜正 Gamma 减弱（1.36亿）｜现价位于 Flip 上方 5.33%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 158（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 80.0P — Vol 5,315 | 最新价 $0.06 | OI 19849→44583 (ΔOI +24734张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24734张（+124.6% vs前日OI），连续性待观察（方向未知）
11-27 95.0P — Vol 25,142 | 最新价 $0.03 | OI 9556→33728 (ΔOI +24172张) | ΔOI/Volume 96.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24172张（+252.9% vs前日OI），连续性待观察（方向未知）
11-27 200.0C — Vol 64,138 | 最新价 $0.28 | OI 22729→40037 (ΔOI +17308张) | ΔOI/Volume 27.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17308张（+76.2% vs前日OI），连续性待观察（方向未知）
11-25 180.0C — Vol 64,729 | 最新价 $1.04 | OI 2063→16771 (ΔOI +14708张) | ΔOI/Volume 22.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14708张（+712.9% vs前日OI），连续性待观察（方向未知）
11-27 190.0C — Vol 36,889 | 最新价 $0.58 | OI 8889→23432 (ΔOI +14543张) | ΔOI/Volume 39.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14543张（+163.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 95,465 张（Put 48,906 / Call 46,559），跨 3 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-25  C +103.1k / P +108.0k ｜ Activity HIGH ｜ 1D
11-27  C +69.1k / P +109.6k ｜ Activity HIGH ｜ 3D
11-30  C +24.1k / P +23.3k ｜ Activity HIGH ｜ 6D
12-02  C +21.3k / P +12.7k ｜ Activity HIGH ｜ 8D

📆 11-25 Forward Structure
存量OI: C 202.0k / P 171.3k，今日变化ΔOI: C +103.1k / P +108.0k，平值价格ATM: C $3.65 / P $3.86 ｜ ATM IV 103.3%，净 delta 敞口 -4.2M shares
Top ΔOI: C 180 +14,708 ｜ P 150 +11,887 ｜ P 140 +10,986
仓位参考: Max Pain 158 ｜ Call Wall 170（+9.6%，弱）（OI 14.5k） ｜ Put Wall 140（-9.8%，弱）（OI 15.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 103.3%｜历史 Rank 96%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,160,453 股

📆 11-27 Forward Structure
存量OI: C 561.0k / P 379.2k，今日变化ΔOI: C +69.1k / P +109.6k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 116.8%，净 delta 敞口 -5.1M shares
Top ΔOI: C 200 +17,308 ｜ C 190 +14,543
仓位参考: Max Pain 150 ｜ Call Wall 165（+6.4%，弱）（OI 30.6k） ｜ Put Wall 160（+3.1%，弱）（OI 22.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 116.8%｜历史 Rank 96%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,074,353 股

📆 11-30 Forward Structure
存量OI: C 85.1k / P 48.8k，今日变化ΔOI: C +24.1k / P +23.3k，平值价格ATM: C $5.67 / P $5.60 ｜ ATM IV 70.0%，净 delta 敞口 -1.1M shares
Top ΔOI: C 200 +6,026 ｜ C 180 +4,995 ｜ C 177 +3,898
仓位参考: Max Pain 150 ｜ Call Wall 170（+9.6%，弱）（OI 6.8k） ｜ Put Wall 140（-9.8%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 70.0%｜历史 Rank 96%（近端代理）｜IV/RV 0.56×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,122,249 股

📆 12-02 Forward Structure
存量OI: C 51.2k / P 19.7k，今日变化ΔOI: C +21.3k / P +12.7k，平值价格ATM: C $6.60 / P $7.00 ｜ ATM IV 73.6%，净 delta 敞口 -644k shares
Top ΔOI: C 200 +10,908 ｜ C 170 +5,260 ｜ P 160 +1,913
仓位参考: Max Pain 160 ｜ Call Wall 170（+9.6%，弱）（OI 6.7k） ｜ Put Wall 160（+3.1%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 73.6%｜历史 Rank 96%（近端代理）｜IV/RV 0.58×（近似）｜净 delta 敞口 负 643,546 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/NVDA_morning.json