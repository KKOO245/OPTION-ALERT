# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-18（2D）ATM IV 139.9% vs 11-20 0.0%（差 +139.9pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-18 160P ΔOI +6,700（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 162.85 → 今开 159.00（-2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 163.00 ｜ 低 158.11

Options: P/C成交量 0.57 | OI比 0.57 | ATM IV 98.1% | Skew 2.1pp | Term 0.43 | ExpMove ±8.8%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.43，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（2D）±8.8% ｜ 11-20（4D）±0.7% ｜ 11-23（7D）±10.4% ｜ 11-25（9D）±11.1%
   ⇒ IV–VIX Spread: +76.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,782,564 | GEX Change vs 上次快照 25,556,645 | Flip: Primary Flip: 159.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1257 / LOW 244 / INVALID 659
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.84（全链重定价，覆盖 99%）
Put Wall 160（弱结构｜现价低于该位 0.3%）
最近结构参考: Flip 160（现价低于该位 0.2%）
量化视角： 负 Gamma（478万，无历史分位）｜负 Gamma 缓解（+2556万）｜现价位于 Flip 下方 0.19%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（Put Wall，弱结构） / 162（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 175.0C — Vol 23,879 | 最新价 $5.33 | OI 3151→22377 (ΔOI +19226张) | ΔOI/Volume 80.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19226张（+610.2% vs前日OI），连续性待观察（方向未知）
11-20 170.0C — Vol 40,230 | 最新价 $4.92 | OI 30210→47389 (ΔOI +17179张) | ΔOI/Volume 42.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17179张（+56.9% vs前日OI），连续性待观察（方向未知）
11-20 175.0C — Vol 33,400 | 最新价 $3.40 | OI 35651→51939 (ΔOI +16288张) | ΔOI/Volume 48.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16288张（+45.7% vs前日OI），连续性待观察（方向未知）
11-16 212.5C — Vol 16,753 | 最新价 $0.03 | OI 1791→17792 (ΔOI +16001张) | ΔOI/Volume 95.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16001张（+893.4% vs前日OI），连续性待观察（方向未知）
11-20 167.5C — Vol 19,794 | 最新价 $5.80 | OI 3596→18396 (ΔOI +14800张) | ΔOI/Volume 74.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14800张（+411.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 83,494 张（Put 0 / Call 83,494），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 314.0k / P 179.4k，今日成交量: C 376.1k / P 214.7k，平值价格ATM: C $1.39 / P $2.05 ｜ ATM IV 98.1%，预期波动 ±2.2%，Max Pain 162
Top ΔOI: C 212 +16,001 ｜ C 202 +14,088 ｜ P 160 +12,983

📆 Forward Expiration Structure

11-18  C +41.0k / P +56.3k ｜ Activity HIGH ｜ 2D
11-20  C +106.1k / P +90.9k ｜ Activity MEDIUM △ ｜ 4D
11-23  C +4.9k / P +2.0k ｜ Activity HIGH ｜ 7D
11-25  C +2.9k / P +1.3k ｜ Activity HIGH ｜ 9D

📆 11-18 Forward Structure
存量OI: C 171.6k / P 143.6k，今日变化ΔOI: C +41.0k / P +56.3k，平值价格ATM: C $6.75 / P $7.33 ｜ ATM IV 139.9%，净 delta 敞口 -386k shares
Top ΔOI: P 145 +11,558 ｜ P 160 +6,700
仓位参考: Max Pain 165 ｜ Call Wall 175（+9.7%，弱）（OI 11.8k） ｜ Put Wall 150（-6.0%，弱）（OI 14.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 139.9%｜历史 Rank 96%（近端代理）｜IV/RV 2.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 385,933 股

11-20（MEDIUM △）Top ΔOI: 170C +17,179 ｜ 175C +16,288
11-20（MEDIUM △）仓位参考: Max Pain 185 ｜ Call Wall 175（+9.7%，弱）（OI 52.1k） ｜ Put Wall 150（-6.0%，弱）（OI 45.1k）

📆 11-23 Forward Structure
存量OI: C 33.9k / P 18.6k，今日变化ΔOI: C +4.9k / P +2.0k，平值价格ATM: C $8.00 / P $8.55 ｜ ATM IV 91.8%，净 delta 敞口 66k shares
Top ΔOI: C 180 +674 ｜ C 170 +587 ｜ P 160 +526
仓位参考: Max Pain 165 ｜ Call Wall 170（+6.6%，弱）（OI 2.7k） ｜ Put Wall 150（-6.0%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 91.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 66,441 股

📆 11-25 Forward Structure
存量OI: C 19.7k / P 5.7k，今日变化ΔOI: C +2.9k / P +1.3k，平值价格ATM: C $8.65 / P $9.05 ｜ ATM IV 87.1%，净 delta 敞口 14k shares
Top ΔOI: C 185 +584
仓位参考: Max Pain 162 ｜ Call Wall 165（+3.4%，弱）（OI 3.0k） ｜ Put Wall 150（-6.0%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 87.1%｜历史 Rank 96%（近端代理）｜IV/RV 1.71×（近似）｜净 delta 敞口 正 13,501 股

📅 事件差分（观察，非因果）: 11-18（2D）ATM IV 139.9% vs 11-20 0.0%（差 +139.9pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/NVDA_morning.json