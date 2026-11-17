# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.92 ｜ QQQ $656.95
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
🟡 **事件差分**: 11-20 ATM IV 50.0% vs 11-27 38.8%（差 +11.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 143P ΔOI +2,313（距现价 -1.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 145.88 → 今开 147.07（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 147.72 ｜ 低 144.15

Options: P/C成交量 1.95 | OI比 1.91 | ATM IV 50.0% | Skew 5.2pp | Term 0.75 | ExpMove ±4.3%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 5.2pp）｜当日成交偏 Put（P/C量 1.95）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.95×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.91×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±4.3% ｜ 11-27（10D）±5.7% ｜ 12-04（17D）±6.4% ｜ 12-11（24D）±9.9%
   ⇒ IV–VIX Spread: +27.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -28,759,305 | GEX Change vs 上次快照 -7,308,961 | Flip: Primary Flip: 152.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 441 / LOW 128 / INVALID 333
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.40（全链重定价，覆盖 94%）
最近结构参考: Flip 152（现价低于该位 4.6%）
量化视角： 负 Gamma（2876万，无历史分位）｜负 Gamma 加深（731万）｜现价位于 Flip 下方 4.58%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 152（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 133.0P — Vol 5,417 | 最新价 $1.61 | OI 67→5254 (ΔOI +5187张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5187张（+7741.8% vs前日OI），连续性待观察（方向未知）
12-18 143.0P — Vol 5,497 | 最新价 $4.40 | OI 227→5038 (ΔOI +4811张) | ΔOI/Volume 87.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4811张（+2119.4% vs前日OI），连续性待观察（方向未知）
11-20 143.0P — Vol 3,137 | 最新价 $1.73 | OI 2183→4496 (ΔOI +2313张) | ΔOI/Volume 73.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2313张（+106.0% vs前日OI），连续性待观察（方向未知）
11-20 140.0C — Vol 1,500 | 最新价 $7.22 | OI 27→1527 (ΔOI +1500张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1500张（+5555.6% vs前日OI），连续性待观察（方向未知）
11-20 137.0P — Vol 561 | 最新价 $0.30 | OI 150→688 (ΔOI +538张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增538张（+358.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,349 张（Put 12,849 / Call 1,500），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +0.3k / P +2.4k ｜ Activity MEDIUM △ ｜ 3D
11-27  C +0.2k / P -11 ｜ Activity MEDIUM △ ｜ 10D
12-04  C +32 / P +22 ｜ Activity LOW ｜ 17D
12-11  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 11-20 Forward Structure
存量OI: C 31.9k / P 61.0k，今日变化ΔOI: C +0.3k / P +2.4k，平值价格ATM: C $4.23 / P $2.00 ｜ ATM IV 50.0%，净 delta 敞口 53k shares
Top ΔOI: P 143 +2,313 ｜ C 140 +1,500 ｜ C 145 -981
仓位参考: Max Pain 152 ｜ Call Wall 153（+5.2%，弱）（OI 2.7k） ｜ Put Wall 140（-3.7%，弱）（OI 9.8k）
量化解读： 存量 Put 重｜ATM IV 50.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,116 股

11-27（MEDIUM △）Top ΔOI: 145C +96 ｜ 165P -48
11-27（MEDIUM △）仓位参考: Max Pain 156 ｜ Call Wall 152.5（+4.9%，弱）（OI 0.1k） ｜ Put Wall 146（+0.4%）（OI 1.1k）

12-04（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 145（-0.3%，弱）（OI 20） ｜ Put Wall 148（+1.8%，弱）（OI 0.1k）

12-11（MEDIUM △）Top ΔOI: 147C +108 ｜ 135P +66
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 147（+1.1%，弱）（OI 0.1k） ｜ Put Wall 143（-1.7%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 50.0% vs 11-27 38.8%（差 +11.2pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/XBI_morning.json