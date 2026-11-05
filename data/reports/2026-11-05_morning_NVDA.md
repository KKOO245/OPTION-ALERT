# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $751.25 ｜ QQQ $656.33
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.0（fear）
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
🔴 **事件差分**: 11-06（1D）ATM IV 81.8% vs 11-09 57.6%（差 +24.2pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 185P ΔOI +7,636（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 200.13 → 今开 196.07（-2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 196.25 ｜ 低 186.13

Options: P/C成交量 0.66 | OI比 0.72 | ATM IV 81.9% | Skew 10.7pp | Term 0.66 | ExpMove ±3.9%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价显著（Skew 10.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±3.9% ｜ 11-09（4D）±5.0% ｜ 11-11（6D）±6.2% ｜ 11-13（8D）±7.0%
   ⇒ IV–VIX Spread: +60.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -137,833,402 | GEX Change vs 上次快照 -65,056,533 | Flip: Primary Flip: 198.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 736 / LOW 146 / INVALID 540
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 198.93（全链重定价，覆盖 99%）
Put Wall 190（弱结构｜现价低于该位 0.1%）
最近结构参考: Put Wall 190（现价低于该位 0.1%）
量化视角： 负 Gamma（1.38亿，无历史分位）｜负 Gamma 加深（6506万）｜现价位于 Flip 下方 4.61%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（Put Wall，弱结构） / 208（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 199（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 210.0C — Vol 52,318 | 最新价 $0.45 | OI 27679→37588 (ΔOI +9909张) | ΔOI/Volume 18.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9909张（+35.8% vs前日OI），连续性待观察（方向未知）
11-06 185.0P — Vol 15,319 | 最新价 $0.31 | OI 9821→17457 (ΔOI +7636张) | ΔOI/Volume 49.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7636张（+77.8% vs前日OI），连续性待观察（方向未知）
11-06 220.0C — Vol 28,310 | 最新价 $0.06 | OI 55385→61901 (ΔOI +6516张) | ΔOI/Volume 23.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6516张（+11.8% vs前日OI），连续性待观察（方向未知）
11-06 215.0C — Vol 29,779 | 最新价 $0.14 | OI 41079→47340 (ΔOI +6261张) | ΔOI/Volume 21.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6261张（+15.2% vs前日OI），连续性待观察（方向未知）
11-06 205.0C — Vol 47,483 | 最新价 $1.43 | OI 5560→11536 (ΔOI +5976张) | ΔOI/Volume 12.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5976张（+107.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,298 张（Put 7,636 / Call 28,662），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +43.6k / P +28.7k ｜ Activity HIGH ｜ 1D
11-09  C +11.8k / P +13.7k ｜ Activity HIGH ｜ 4D
11-11  C +7.3k / P +6.1k ｜ Activity HIGH ｜ 6D
11-13  C +13.0k / P +5.9k ｜ Activity HIGH ｜ 8D

📆 11-06 Forward Structure
存量OI: C 446.6k / P 321.3k，今日变化ΔOI: C +43.6k / P +28.7k，平值价格ATM: C $3.30 / P $4.03 ｜ ATM IV 81.8%，净 delta 敞口 -568k shares
Top ΔOI: C 210 +9,909 ｜ P 185 +7,636
仓位参考: Max Pain 208 ｜ Call Wall 207.5（+9.4%，弱）（OI 30.3k） ｜ Put Wall 200（+5.4%，弱）（OI 22.4k）
量化解读： 存量 Call 重｜ATM IV 81.8%｜历史 Rank 94%（近端代理）｜IV/RV 2.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 568,318 股

📆 11-09 Forward Structure
存量OI: C 27.8k / P 30.6k，今日变化ΔOI: C +11.8k / P +13.7k，平值价格ATM: C $4.35 / P $5.05 ｜ ATM IV 57.6%，净 delta 敞口 -333k shares
Top ΔOI: P 180 +3,096 ｜ P 170 +2,254
仓位参考: Max Pain 208 ｜ Call Wall 207.5（+9.4%，弱）（OI 1.9k） ｜ Put Wall 180（-5.1%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜ATM IV 57.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.78×（近似）｜净 delta 敞口 负 333,446 股

📆 11-11 Forward Structure
存量OI: C 16.4k / P 23.4k，今日变化ΔOI: C +7.3k / P +6.1k，平值价格ATM: C $5.53 / P $6.20 ｜ ATM IV 59.3%，净 delta 敞口 -196k shares
Top ΔOI: C 210 +1,643 ｜ P 187 +868 ｜ P 192 +865
仓位参考: Max Pain 205 ｜ Call Wall 207.5（+9.4%，弱）（OI 1.0k） ｜ Put Wall 190（+0.1%）（OI 5.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 59.3%｜历史 Rank 94%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 195,819 股

📆 11-13 Forward Structure
存量OI: C 183.7k / P 189.5k，今日变化ΔOI: C +13.0k / P +5.9k，平值价格ATM: C $6.38 / P $7.00 ｜ ATM IV 58.3%，净 delta 敞口 -16k shares
Top ΔOI: C 215 +3,896 ｜ P 150 +2,186
仓位参考: Max Pain 210 ｜ Call Wall 205（+8.0%，弱）（OI 5.0k） ｜ Put Wall 200（+5.4%，弱）（OI 15.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.3%｜历史 Rank 94%（近端代理）｜IV/RV 1.80×（近似）｜净 delta 敞口 负 16,253 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 81.8% vs 11-09 57.6%（差 +24.2pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/NVDA_morning.json