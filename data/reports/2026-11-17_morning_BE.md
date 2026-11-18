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
🔴 **事件差分**: 11-20（3D）ATM IV 137.3% vs 11-27 106.1%（差 +31.2pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 177.28 → 今开 181.00（+2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 181.16 ｜ 低 169.25

Options: P/C成交量 0.36 | OI比 0.92 | ATM IV 137.3% | Skew 13.6pp | Term 0.71 | ExpMove ±10.4%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价显著（Skew 13.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（3D）±10.4% ｜ 11-27（10D）±13.9% ｜ 12-04（17D）±19.0% ｜ 12-11（24D）±22.4%
   ⇒ IV–VIX Spread: +114.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,641,852 | GEX Change vs 上次快照 1,091,307 | Flip: Primary Flip: 195.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 556 / LOW 102 / INVALID 140
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 195.61（全链重定价，覆盖 100%）
最近结构参考: Flip 196（现价低于该位 11.0%）
量化视角： 负 Gamma（964万，无历史分位）｜负 Gamma 缓解（+109万）｜现价位于 Flip 下方 11.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 196（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 150.0P — Vol 4,338 | 最新价 $8.96 | OI 3229→5834 (ΔOI +2605张) | ΔOI/Volume 60.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2605张（+80.7% vs前日OI），连续性待观察（方向未知）
11-20 220.0C — Vol 3,203 | 最新价 $0.57 | OI 4957→6721 (ΔOI +1764张) | ΔOI/Volume 55.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1764张（+35.6% vs前日OI），连续性待观察（方向未知）
11-20 210.0C — Vol 2,828 | 最新价 $1.09 | OI 1507→2962 (ΔOI +1455张) | ΔOI/Volume 51.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1455张（+96.5% vs前日OI），连续性待观察（方向未知）
11-20 200.0C — Vol 2,316 | 最新价 $2.37 | OI 4287→5069 (ΔOI +782张) | ΔOI/Volume 33.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增782张（+18.2% vs前日OI），连续性待观察（方向未知）
11-20 177.5C — Vol 1,701 | 最新价 $9.50 | OI 167→905 (ΔOI +738张) | ΔOI/Volume 43.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增738张（+441.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,344 张（Put 2,605 / Call 4,739），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +8.0k / P -0.7k ｜ Activity HIGH ｜ 3D
11-27  C +2.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 10D
12-04  C +0.7k / P -0.2k ｜ Activity MEDIUM △ ｜ 17D
12-11  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 24D

📆 11-20 Forward Structure
存量OI: C 99.8k / P 91.7k，今日变化ΔOI: C +8.0k / P -0.7k，平值价格ATM: C $8.75 / P $9.32 ｜ ATM IV 137.3%，净 delta 敞口 414k shares
Top ΔOI: C 220 +1,764 ｜ C 210 +1,455 ｜ P 260 -1,003
仓位参考: Max Pain 200 ｜ Call Wall 190（+9.2%，弱）（OI 3.6k） ｜ Put Wall 170（-2.3%，弱）（OI 4.9k）
量化解读： 存量两侧均衡｜ATM IV 137.3%｜历史 Rank 86%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 413,904 股

11-27（MEDIUM △）Top ΔOI: 185C +543 ｜ 190C +299
11-27（MEDIUM △）仓位参考: Max Pain 200 ｜ Call Wall 185（+6.3%，弱）（OI 0.7k） ｜ Put Wall 190（+9.2%，弱）（OI 1.3k）

12-04（MEDIUM △）Top ΔOI: 185P -473 ｜ 220C +216
12-04（MEDIUM △）仓位参考: Max Pain 200 ｜ Call Wall 190（+9.2%，弱）（OI 0.3k） ｜ Put Wall 185（+6.3%，弱）（OI 0.4k）

12-11（MEDIUM △）Top ΔOI: 170P +51
12-11（MEDIUM △）仓位参考: Max Pain 210 ｜ Put Wall 175（+0.6%）（OI 2.1k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 137.3% vs 11-27 106.1%（差 +31.2pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/BE_morning.json