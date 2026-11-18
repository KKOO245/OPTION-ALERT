# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $737.42 ｜ QQQ $nan
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（3D）ATM IV 89.2% vs 11-27 69.0%（差 +20.1pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 140P ΔOI +5,810（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 141.22 → 今开 142.84（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 142.99 ｜ 低 140.32

Options: P/C成交量 5.62 | OI比 1.81 | ATM IV 89.2% | Skew 18.7pp | Term 0.65 | ExpMove ±6.6%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价显著（Skew 18.7pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 5.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 5.62×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.81×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±6.6% ｜ 11-27（10D）±9.8% ｜ 12-04（17D）±12.7% ｜ 12-11（24D）±18.7%
   ⇒ IV–VIX Spread: +66.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -59,859,232 | GEX Change vs 上次快照 -2,822,234 | Flip: Primary Flip: 154.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 626 / LOW 385 / INVALID 615
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 154.97（全链重定价，覆盖 100%）
最近结构参考: Flip 155（现价低于该位 8.6%）
量化视角： 负 Gamma（5986万，无历史分位）｜负 Gamma 加深（282万）｜现价位于 Flip 下方 8.59%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 157（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 160.0C — Vol 6,039 | 最新价 $0.75 | OI 491→6503 (ΔOI +6012张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6012张（+1224.4% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 7,811 | 最新价 $4.20 | OI 16225→22035 (ΔOI +5810张) | ΔOI/Volume 74.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5810张（+35.8% vs前日OI），连续性待观察（方向未知）
12-18 170.0C — Vol 5,604 | 最新价 $1.30 | OI 49434→54100 (ΔOI +4666张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4666张（+9.4% vs前日OI），连续性待观察（方向未知）
11-20 130.0P — Vol 6,983 | 最新价 $1.37 | OI 12240→16701 (ΔOI +4461张) | ΔOI/Volume 63.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4461张（+36.5% vs前日OI），连续性待观察（方向未知）
11-20 135.0P — Vol 6,480 | 最新价 $2.52 | OI 7888→10171 (ΔOI +2283张) | ΔOI/Volume 35.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2283张（+28.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,232 张（Put 12,554 / Call 10,678），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +4.4k / P +8.1k ｜ Activity MEDIUM △ ｜ 3D
11-27  C +2.3k / P +3.1k ｜ Activity MEDIUM △ ｜ 10D
12-04  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
12-11  C +51 / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 11-20 Forward Structure
存量OI: C 199.7k / P 362.3k，今日变化ΔOI: C +4.4k / P +8.1k，平值价格ATM: C $4.90 / P $4.50 ｜ ATM IV 89.2%，净 delta 敞口 341k shares
Top ΔOI: P 140 +5,810 ｜ P 130 +4,461 ｜ P 171 -4,164
仓位参考: Max Pain 157 ｜ Call Wall 145（+2.4%，弱）（OI 5.8k） ｜ Put Wall 140（-1.2%，弱）（OI 22.0k）
量化解读： 存量 Put 重｜ATM IV 89.2%｜历史 Rank 99%（近端代理）｜IV/RV 0.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 340,661 股

11-27（MEDIUM △）Top ΔOI: 160C +6,012 ｜ 161C -4,381
11-27（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 150（+5.9%，弱）（OI 3.6k）

12-04（MEDIUM △）Top ΔOI: 141P +62
12-04（MEDIUM △）仓位参考: Max Pain 157 ｜ Call Wall 150（+5.9%，弱）（OI 0.3k） ｜ Put Wall 140（-1.2%，弱）（OI 5.2k）

12-11（MEDIUM △）仓位参考: Max Pain 148 ｜ Call Wall 147（+3.8%，弱）（OI 0.2k） ｜ Put Wall 140（-1.2%）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 89.2% vs 11-27 69.0%（差 +20.1pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/SOXX_morning.json