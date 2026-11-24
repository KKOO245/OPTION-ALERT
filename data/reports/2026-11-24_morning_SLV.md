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
🟡 **近现价集中开仓**: 11-27 39C ΔOI +1,705（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-25 43C ΔOI +11,309 占该期限总 OI 16.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 38.91 → 今开 38.17（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 38.31 ｜ 低 37.38

Options: P/C成交量 0.84 | OI比 0.39 | ATM IV 61.8% | Skew 3.1pp | Term 0.81 | ExpMove ±3.0%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-25（1D）±3.0% ｜ 11-27（3D）±4.0% ｜ 11-30（6D）±5.2% ｜ 12-02（8D）±6.2%
   ⇒ IV–VIX Spread: +34.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,160,256 | GEX Change vs 上次快照 1,345,513 | Flip: Primary Flip: 38.19（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 720 / LOW 228 / INVALID 672
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 38.19（全链重定价，覆盖 94%）
Put Wall 40（弱结构｜现价低于该位 5.2%）
最近结构参考: Flip 38（现价低于该位 0.7%）
量化视角： 负 Gamma（516万，无历史分位）｜负 Gamma 缓解（+135万）｜现价位于 Flip 下方 0.69%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 39（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 38（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-25 43.0C — Vol 11,496 | 最新价 $0.01 | OI 169→11478 (ΔOI +11309张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11309张（+6691.7% vs前日OI），连续性待观察（方向未知）
12-24 46.0C — Vol 5,107 | 最新价 $0.39 | OI 137→5187 (ΔOI +5050张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5050张（+3686.1% vs前日OI），连续性待观察（方向未知）
12-24 44.0C — Vol 5,111 | 最新价 $0.62 | OI 287→5261 (ΔOI +4974张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4974张（+1733.1% vs前日OI），连续性待观察（方向未知）
12-18 45.0C — Vol 12,127 | 最新价 $0.37 | OI 14153→17409 (ΔOI +3256张) | ΔOI/Volume 26.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3256张（+23.0% vs前日OI），连续性待观察（方向未知）
11-25 41.0C — Vol 4,413 | 最新价 $0.11 | OI 888→3613 (ΔOI +2725张) | ΔOI/Volume 61.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2725张（+306.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,314 张（Put 0 / Call 27,314），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-25  C +21.9k / P +6.5k ｜ Activity HIGH ｜ 1D
11-27  C +5.7k / P +2.6k ｜ Activity MEDIUM △ ｜ 3D
11-30  C +2.2k / P +0.9k ｜ Activity MEDIUM △ ｜ 6D
12-02  C +0.5k / P +0.7k ｜ Activity HIGH ｜ 8D

📆 11-25 Forward Structure
存量OI: C 50.5k / P 19.7k，今日变化ΔOI: C +21.9k / P +6.5k，平值价格ATM: C $0.52 / P $0.60 ｜ ATM IV 61.8%，净 delta 敞口 -36k shares
Top ΔOI: C 41 +2,725
仓位参考: Max Pain 39 ｜ Call Wall 40.5（+6.8%，弱）（OI 5.7k） ｜ Put Wall 39（+2.8%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 61.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 36,426 股

11-27（MEDIUM △）Top ΔOI: 39C +1,705 ｜ 41C +1,104
11-27（MEDIUM △）仓位参考: Max Pain 41 ｜ Call Wall 40（+5.5%，弱）（OI 6.3k） ｜ Put Wall 40（+5.5%）（OI 9.2k）

11-30（MEDIUM △）Top ΔOI: 40C +714 ｜ 39C +363
11-30（MEDIUM △）仓位参考: Max Pain 40 ｜ Put Wall 39（+2.8%）（OI 4.1k）

📆 12-02 Forward Structure
存量OI: C 8.5k / P 3.6k，今日变化ΔOI: C +0.5k / P +0.7k，平值价格ATM: C $1.29 / P $1.06 ｜ ATM IV 49.8%，净 delta 敞口 -16k shares
Top ΔOI: P 37 +474 ｜ C 40 +349 ｜ C 41 -110
仓位参考: Max Pain 40 ｜ Put Wall 39（+2.8%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 49.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 负 16,069 股

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 61.8% vs 11-27 55.4%（差 +6.4pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/SLV_morning.json