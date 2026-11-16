# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $740.16 ｜ QQQ $661.75
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
🔴 **事件差分**: 11-20（4D）ATM IV 83.0% vs 11-27 66.2%（差 +16.7pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-20 148P ΔOI +9,287（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 149.30 → 今开 142.98（-4.2%） | 较昨收变动（含盘初走势） ｜ 今日高 144.50 ｜ 低 140.88

Options: P/C成交量 3.05 | OI比 1.81 | ATM IV 83.0% | Skew 6.5pp | Term 0.70 | ExpMove ±7.2%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 6.5pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 3.05）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.05×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.81×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±7.2% ｜ 11-27（11D）±12.1% ｜ 12-04（18D）±3.7% ｜ 12-11（25D）±4.1%
   ⇒ IV–VIX Spread: +61.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -42,232,306 | GEX Change vs 上次快照 -29,475,765 | Flip: Primary Flip: 152.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 543 / LOW 348 / INVALID 735
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.53（全链重定价，覆盖 94%）
最近结构参考: Flip 153（现价低于该位 6.9%）
量化视角： 负 Gamma（4223万，无历史分位）｜负 Gamma 加深（2948万）｜现价位于 Flip 下方 6.91%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 158（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 105.0P — Vol 90,684 | 最新价 $0.10 | OI 8440→94528 (ΔOI +86088张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增86088张（+1020.0% vs前日OI），连续性待观察（方向未知）
11-20 148.33P — Vol 9,717 | 最新价 $4.80 | OI 942→10229 (ΔOI +9287张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9287张（+985.9% vs前日OI），连续性待观察（方向未知）
11-27 161.67C — Vol 6,108 | 最新价 $1.85 | OI 11058→16196 (ΔOI +5138张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5138张（+46.5% vs前日OI），连续性待观察（方向未知）
12-04 122.0P — Vol 5,002 | 最新价 $0.92 | OI 0→5000 (ΔOI +5000张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5000张（前日OI缺失），连续性待观察（方向未知）
12-04 140.0P — Vol 5,072 | 最新价 $3.85 | OI 446→5254 (ΔOI +4808张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4808张（+1078.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 110,321 张（Put 105,183 / Call 5,138），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $6M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -3.9k / P +106.1k ｜ Activity HIGH ｜ 4D
11-27  C +5.4k / P +0.8k ｜ Activity MEDIUM △ ｜ 11D
12-04  C +0.3k / P +11.6k ｜ Activity HIGH ｜ 18D
12-11  C +0.1k / P +0.4k ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 195.3k / P 354.2k，今日变化ΔOI: C -3.9k / P +106.1k，平值价格ATM: C $5.40 / P $4.80 ｜ ATM IV 83.0%，净 delta 敞口 -1.2M shares
Top ΔOI: P 105 +86,088 ｜ P 148 +9,287 ｜ C 166 -6,487
仓位参考: Max Pain 158 ｜ Call Wall 145（+2.1%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 83.0%｜历史 Rank 99%（近端代理）｜IV/RV 0.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,156,268 股

11-27（MEDIUM △）Top ΔOI: 161C +5,138 ｜ 135P +329
11-27（MEDIUM △）仓位参考: Max Pain 162 ｜ Put Wall 150（+5.6%，弱）（OI 3.6k）

📆 12-04 Forward Structure
存量OI: C 11.1k / P 21.6k，今日变化ΔOI: C +0.3k / P +11.6k，平值价格ATM: C $0.00 / P $5.25 ｜ ATM IV 66.4%，净 delta 敞口 -339k shares
Top ΔOI: P 122 +5,000 ｜ P 140 +4,808 ｜ P 120 +921
仓位参考: Max Pain 158 ｜ Put Wall 140（-1.4%，弱）（OI 5.3k）
量化解读： 存量 Put 重｜ATM IV 66.4%｜历史 Rank 99%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 339,441 股

12-11（MEDIUM △）Top ΔOI: 150P +93 ｜ 155C +43
12-11（MEDIUM △）仓位参考: Max Pain 148 ｜ Call Wall 147（+3.5%，弱）（OI 0.2k） ｜ Put Wall 140（-1.4%）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 83.0% vs 11-27 66.2%（差 +16.7pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SOXX_morning.json